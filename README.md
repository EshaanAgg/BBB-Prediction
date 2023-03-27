# RGCN for predicting BBB Permeability of Drug Molecules

### Getting started

1. First we need to install all the libraries and packages listed down under requiremets.txt.

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

## Description of the Data Sets used

#### DRKG - Drug Repurpose Knowledge Graph Dataset

Drug Repurposing Knowledge Graph (DRKG) is a comprehensive biological knowledge graph relating genes, compounds, diseases, biological processes, side effects and symptoms. DRKG includes information from six existing databases including DrugBank, Hetionet, GNBR, String, IntAct and DGIdb, and data collected from recent publications particularly related to Covid19. It includes 97,238 entities belonging to 13 entity-types; and 5,874,261 triplets belonging to 107 edge-types.

#### Hugo Gene Nomenclature

The HGNC is a resource for approved human gene nomenclature containing ~42000 gene symbols and names and 1300+ gene families and sets.
