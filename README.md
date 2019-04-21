# Forest-Induced-Similarity
Supervised & Unsupervised Similarity Matrix using ensemble of decision trees (e.g. Random Forest)

### Getting started

  - Git clone this project
  - Go into project's folder
  - Install using pip:

    pip install .

  - Use main.py to get a similarity/distance matrix from a numeric or encoded dataset in csv format

      python main.py --input_file="input_data.csv" --method="extra-trees" --output_type="distance" --output_format="csv" --output_file="distance_matrix.csv"

    OR

  - Use functions inside of a notebook to have more control on input data.
