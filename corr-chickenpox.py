def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    df = pd.read_csv("assets/NISPUF17.csv", index_col = 0)  
    df = df[df["HAD_CPOX"]<=2]
    dataf = pd.DataFrame({"had_chickenpox_column":df["HAD_CPOX"],
                   "num_chickenpox_vaccine_column":df["P_NUMVRC"]})
    dataf = dataf.dropna()
    corr, pval=stats.pearsonr(dataf["had_chickenpox_column"],dataf["num_chickenpox_vaccine_column"])
    return corr
