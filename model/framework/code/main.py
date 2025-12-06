# imports
import os
import csv
import sys
import numpy as np
from joblib import load
from macaw import MACAW
from ersilia_pack_utils.core import write_out, read_smiles

root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(root)

# current file directory
checkpoints_dir = os.path.join(root, "..", "..", "checkpoints")

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]
checkpoints_path=os.path.join(checkpoints_dir,'macaw_chembl_trained.joblib')

# --------------------------------
REQ_COMPONENTS = 100
RANDOM_STATE = 42
# --------------------------------

# my model
def my_model(smiles_list):
    n_samples = len(smiles_list)
    if n_samples == 0:
        return np.empty((0, 0))

    mcw = load(checkpoints_path)

    emb = mcw.transform(smiles_list)  # shape: (n_samples, n_components)
    return emb

cols, smiles_list= read_smiles(input_file)

# run model
emb = my_model(smiles_list)


n_components = emb.shape[1] if emb.size else 0
headers= [f"dim_{i:02d}" for i in range(n_components)]

#write output
write_out(emb, headers, output_file, np.float32)

