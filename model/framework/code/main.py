# imports
import os
import csv
import sys
import numpy as np
from macaw import MACAW


# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# my model
def my_model(smiles_list):
    mcw = MACAW(random_state=42)

    outputs=[]

    emb = mcw.fit_transform(smiles_list)
    for row in emb:
        vals=[]
        for x in row:
            if isinstance(x,float) and np.isnan(x):
                vals.append('nan')
        else:
            vals.append(f"{float(x):.6g}")
            outputs.append(" ".join(vals))

    return outputs


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = my_model(smiles_list)

# #check input and output have the same lenght
# input_len = len(smiles_list)
# output_len = len(outputs)
# assert input_len == output_len

header = [f"macaw_{i:03d}" for i in range(outputs.shape[1])]

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["value"])  # header
    for o in outputs:
        writer.writerow([o])
