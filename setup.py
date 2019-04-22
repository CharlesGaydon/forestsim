from setuptools import setup, find_packages

import forestsim

setup(name='forestsim',
      version=forestsim.__version__,
      description='Similarity & Distance matrices based on forest of decision trees.',
      long_description=open('README.md').read(),
      url='https://github.com/CharlesGaydon/forestsim',
      author='Charles Gaydon',
      author_email='charles.gaydon@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=["scikit-learn","seaborn","numpy","pandas"],
      include_package_data=True,
      classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "License :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        ],
      zip_safe=False)