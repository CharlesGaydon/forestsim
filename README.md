# Forest-Induced-Similarity
Supervised & Unsupervised Similarity Matrix using ensemble of decision trees (e.g. Random Forest and Extra Trees).

See for instance ((Dalleau et al. 2019))[https://hal.inria.fr/hal-01982232/document].

### Getting started

  - Git clone this project
  - Go into project's folder
  - Create and activate the conda env using

        conda env create -f forestsim_env.yml
        conda activate forestsim

  - Install package using pip:

        pip install .

  - Use main.py to get a similarity/distance matrix from a numeric or encoded dataset in csv format

        python main.py --input_file="input_data.csv" --method="extra-trees" --output_type="distance" --output_format="csv" --output_file="distance_matrix.csv" # not impletemented yet !

    OR

  - Use functions inside of a notebook to have more control on input data, as described in the examples.
