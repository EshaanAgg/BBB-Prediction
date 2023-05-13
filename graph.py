import pandas as pd
import numpy as np
import torch
import deepchem as dc
from sklearn.preprocessing import StandardScaler
from torch_geometric.data import Data

df_drug = pd.read_csv("dataset.csv")

# Create Edges
df_drugsim = pd.read_csv("drug.csv")
df_drugpro = pd.read_csv("protein.csv")

sourcenode = df_drugsim["Drug_1"].to_list() + df_drugpro["Drug_ID"].to_list()
destinnode = df_drugsim["Drug_2"].to_list() + df_drugpro["Gene_ID"].to_list()
edge_index = torch.tensor(
    [sourcenode + destinnode, destinnode + sourcenode], dtype=torch.long
)
relation_list = df_drugsim["Relation"].to_list() + df_drugpro["Relation"].to_list()
edge_type = torch.tensor(relation_list * 2, dtype=torch.long)

# Node features
# Mordred descriptors
featurizer = dc.feat.MordredDescriptors(ignore_3D=True)
mordred_des = featurizer.featurize(df_drug["CanonicalSMILES"].to_list())
mordred_des = StandardScaler().fit_transform(mordred_des)
mordred_des = torch.tensor(mordred_des, dtype=torch.float)

# Node labels
y = torch.tensor(df_drug["P_NP"].values)

# Graph with both drug-protein interactions and drug-drug similarity as the edges
# Mordred descriptors as the node features
data_drugsim = Data(x=mordred_des, edge_index=edge_index, edge_type=edge_type, y=y)
torch.save(data_drugsim, "graph_protein.pt")

# Graph with only drug-protein interactions as the edges
# Mordred descriptors as the node features
edge_type_sub = edge_type[(edge_type != 0)]
edge_index_sub = edge_index[:, (edge_type != 0)]
edge_type_sub[edge_type_sub == 4] = 0
data = Data(x=mordred_des, edge_index=edge_index_sub, edge_type=edge_type_sub, y=y)
torch.save(data, "graph.pt")
