import numpy as np
import collections
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.manifold import MDS
from time import time

from warnings import warn

class ForestSim():

	def __init__(self, forest):
		# TODO : adapt if non sklearn forest used
		self.forest = forest

	def fit(self, X, y = 2, randomize = False, nb_repet = 1, keep_all_mat = False):

		self.X = np.float32(X) #used in tree.apply function
		self.y = y
		self.n = self.X.shape[0]
		self.similarity_matrix = np.zeros((self.n,self.n))
		# True to keep all sim matrices
		if keep_all_mat:
			self.co_ocs = []

		# create the target vector if needed
		if not isinstance(self.y, collections.Sequence):
			self.y_ = np.random.choice(self.y, size = (self.n,))
		else:
			self.y_ = self.y
		t0 = time()
		for repet_id in range(nb_repet):
			t = time()
			print("Fitting - {}/{} iteration".format(repet_id,nb_repet))
			# random seed to have changing bootstrapping in forest.fit

			np.random.seed(repet_id)
			if randomize:
				np.random.shuffle(self.y_)

			self.forest.fit(self.X,self.y_) # check inplace op
			sim = self.calculate_a_sim_mat()
			self.similarity_matrix += sim

			if keep_all_mat:
				self.co_ocs.append(sim)
			print("Took {} seconds".format(np.round(time()-t, decimals=2)))
		print("Total time : {} seconds".format(np.round(time()-t0, decimals=2)))


		self.similarity_matrix /= nb_repet

		return (self)

	def calculate_a_sim_mat(self):

		co_oc = np.zeros((self.n,self.n))
		for iter_, dt in enumerate(self.forest.estimators_):

		    leafs_id = dt.tree_.apply(self.X)
		    ser = pd.DataFrame(data={"ser":leafs_id, "ones":1})
		    ser = ser.pivot(columns="ser").fillna(0)
		    ser = ser.dot(ser.T)
		    co_oc+= ser.values
		    # pondération par unique n of leaf a reflechir

		co_oc = co_oc/len(self.forest.estimators_)
		return (co_oc)

	# should we return a copy ?
	def get_similarity_matrix(self):
		return (self.similarity_matrix)

	def get_distance_matrix(self):
		return (np.sqrt(1-self.similarity_matrix))

	# use sklearn.manifold.MDS kwags
	def apply_MDS(self,n_instance=100, dissimilarity = "precomputed",**kwargs):
		np.random.seed(0)
		if isinstance(n_instance,int) and 0<n_instance and n_instance<=self.n:
			idx = np.random.choice(self.n,n_instance,replace=False)
		elif isinstance(n_instance,float) and 0<n_instance and n_instance<=1:
			idx = np.random.choice(self.n,int(self.n*n_instance),replace=False)
		else:
			warn("invalid n_instance argument - should be in [0.0;1.0] or [0,self.n]")
			idx = np.arange(self.n)
		if len(idx) == self.n:
			print("Computing MDS on all {} instances.".format(self.n))
		else:
			print("Computing MDS on {} / {} instances.".format(len(idx),self.n))

		kwargs.update({"dissimilarity":dissimilarity})

		if "dissimilarity" not in kwargs.keys():
			print("Computing non precomputed MDS - set dissimilarity to precomputed to use the distance matrix")
			mds = MDS(**kwargs)
			self.X_mds = mds.fit_transform(self.X[idx,:])
		else:
			print("Computing MDS on precomputed dissimilarities.")
			mds = MDS(**kwargs)
			dist_mat_ = self.get_distance_matrix()[idx][:,idx]
			self.X_mds = mds.fit_transform(dist_mat_)
		
		return (self.X_mds)

	def project_MDS_2D(self, **kwargs):
		# TODO  : add saving options
		# TODO : add the necessary sampling, then stratified sampling...
		plt.figure(figsize=(8,8))
		sns.scatterplot(x = self.X_mds[:,0],
			y=self.X_mds[:,1]
			)
		plt.show()



def main():
	# should be able to take a standard csv file somewhere, apply one of the two methods, and output the sim mat in a csv file 
    print("work in progress")

if __name__ == "__main__":
    main()