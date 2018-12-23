import glob
import os
import numpy as np
import pandas as pd

home_dir = "02 KNIME Processed/"

if not os.path.exists("02 KNIME Processed\\python_processed\\"):
    os.mkdir("02 KNIME Processed\\python_processed\\")

for file in glob.glob(home_dir+"book*.csv"):
    data = pd.read_csv(file)

    df = pd.DataFrame(data)
    df.head()
    df["Split Value 1"] = [x.split("[")[0] for x in df["Split Value 1"]]
    df["Split Value 2"] = [x.split("[")[0] for x in df["Split Value 2"]]

    df2 = pd.DataFrame()
    df2[["node1", "node2", "weight", "relative_weight"]] = df[["Split Value 1", "Split Value 2", "ItemSetSupport", "RelativeItemSetSupport%"]]
    df2.head()

    df2.to_csv("02 KNIME Processed/python_processed/"+os.path.basename(file), index=False)

from fixNames import *