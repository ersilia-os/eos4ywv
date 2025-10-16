# imports
import os
import csv
import sys
import numpy as np
from joblib import load
from macaw import MACAW

# parse arguments
print(os.getcwd())
input_file = sys.argv[1]
output_file = sys.argv[2]
checkpoints_path='../checkpoints/macaw_chembl_trained.joblib'


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

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r", newline="") as f:
    reader = csv.reader(f)
    next(reader, None)  # skip header if present
    smiles_list = [r[0] for r in reader if r]

# run model
emb = my_model(smiles_list)

# write output as one column per component
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    n_components = emb.shape[1] if emb.size else 0
    header = [f"dim_{i:02d}" for i in range(n_components)]
    writer.writerow(header)

    for row in emb:
        formatted = [
            "nan" if (isinstance(x, float) and np.isnan(x)) else f"{float(x):.6g}"
            for x in row
        ]
        writer.writerow(formatted)

