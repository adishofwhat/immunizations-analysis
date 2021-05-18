import pandas as pd
import numpy as np

def chickenpox_by_sex():
    df = pd.read_csv("assets/NISPUF17.csv", index_col = 0)
    df["SEX"].replace({2:0},inplace=True)
    df["HAD_CPOX"].replace({2:0},inplace=True)
    female = df[df["SEX"]==0]
    male = df[df["SEX"]==1]
    xf = female[female["P_NUMVRC"]>0]
    xxf = xf[xf["HAD_CPOX"]==1]
    yf = female[female["P_NUMVRC"]>0]
    yyf = yf[yf["HAD_CPOX"]==0]
    xm = male[male["P_NUMVRC"]>0]
    xxm = xm[xm["HAD_CPOX"]==1]
    ym = male[male["P_NUMVRC"]>0]
    yym = ym[ym["HAD_CPOX"]==0]
    dict = { "male" : len(xxm.index)/len(yym.index),
             "female" : len(xxf.index)/len(yyf.index) }
    return dict
