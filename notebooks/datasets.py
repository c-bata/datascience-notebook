import numpy as np
import pandas as pd
from numpy.random import normal as rnorm


def generate_linearly_separable_dataset(n):
    """ 線形分離可能なデータセットを生成 """
    p1 = pd.DataFrame(np.hstack((rnorm(loc=2.0, scale=0.5, size=(n,1)), rnorm(loc=2.0, scale=0.5, size=(n,1)))), columns=['x','y'])
    p1['label'] = 0
    p2 = pd.DataFrame(np.hstack((rnorm(loc=1.0, scale=0.5, size=(n,1)), rnorm(loc=1.0, scale=0.5, size=(n,1)))), columns=['x','y'])
    p2['label'] = 1
    return pd.concat([p1, p2])


def generate_not_linearly_separable_dataset(n):
    """ 線形分離可能なXORパターンのデータセットを生成 """
    p1 = pd.DataFrame(np.hstack((rnorm(loc=1.0, scale=1.0, size=(n,1)), rnorm(loc=1.0, scale=1.0, size=(n,1)))), columns=['x','y'])
    p1['label'] = 0
    p2 = pd.DataFrame(np.hstack((rnorm(loc=-1.0, scale=1.0, size=(n,1)), rnorm(loc=1.0, scale=1.0, size=(n,1)))), columns=['x','y'])
    p2['label'] = 1
    p3 = pd.DataFrame(np.hstack((rnorm(loc=-1.0, scale=1.0, size=(n,1)), rnorm(loc=-1.0, scale=1.0, size=(n,1)))), columns=['x','y'])
    p3['label'] = 0
    p4 = pd.DataFrame(np.hstack((rnorm(loc=1.0, scale=1.0, size=(n,1)),  rnorm(loc=-1.0, scale=1.0, size=(n,1)))), columns=['x','y'])
    p4['label'] = 1
    return pd.concat([p1,p2,p3,p4])

