import pandas as pd
import numpy as np

def average_influenza_doses():
    df = pd.read_csv("assets/NISPUF17.csv", index_col = 0)
    df["CBF_01"].replace({2:0},inplace=True)
    df.head()
    s1 = df[df["CBF_01"] == 1]["P_NUMFLU"].dropna()
    s2 = df[df["CBF_01"] == 0]["P_NUMFLU"].dropna()
    x = s1.sum()/s1.size
    y = s2.sum()/s2.size
    return (x,y)
