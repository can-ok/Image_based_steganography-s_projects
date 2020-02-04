from scipy.stats import entropy
import numpy as np
from math import log, e
import math
import pandas as pd


def entropy3(labels, base=2):
    vc = pd.Series(labels).value_counts(normalize=True, sort=False)
    base = e if base is None else base
    return -(vc * np.log(vc)/np.log(base)).sum()


listem= [1,1]

print(entropy3(listem))
