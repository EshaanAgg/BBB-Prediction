# RGCN for predicting BBB Permeability of drug molecules

### Getting started

1. First we need to install all the libraries and packages listed down under requiremnets.txt.

```
pip install requirements.txt
```

2. Calculate the drug-drug similarity by running `drug_similarity.py`. The results will be stored in `drug_similarity.csv`.

```
python drug_similarity.py
```

1. Run `graph.py` to generate the drug features and to structure the data into graphs. Two graphs will be built and be saved separately in the following files.

   - They include the drug-drug similarity as the edges, and the Mordred descriptors as the node features.

```
python graph.py
```

1. Run `rgcn.py` to train and evaluate the RGCN model with `graph.pt` as the input.

```
python rgcn.py
```
