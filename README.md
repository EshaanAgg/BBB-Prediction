# RGCN for predicting BBB Permeability of Drug Molecules

### Running the model

```
pip install requirements.txt
python drug.py
python protein.py
python graph.py
python train_rgcn_protein.py
```

## Datasets used

#### DRKG - Drug Repurpose Knowledge Graph Dataset

Drug Repurposing Knowledge Graph (DRKG) is a comprehensive biological knowledge graph relating genes, compounds, diseases, biological processes, side effects and symptoms. DRKG includes information from six existing databases including DrugBank, Hetionet, GNBR, String, IntAct and DGIdb, and data collected from recent publications particularly related to Covid19. It includes 97,238 entities belonging to 13 entity-types; and 5,874,261 triplets belonging to 107 edge-types.

#### Hugo Gene Nomenclature

The HGNC is a resource for approved human gene nomenclature containing ~42000 gene symbols and names and 1300+ gene families and sets.
