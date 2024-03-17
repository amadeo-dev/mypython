import pandas as pd
import numpy as np
import seaborn as sns

ep = pd.read_csv('nat2015.csv')

ep = ep.drop(['annais'], axis=1)
ep = ep.drop(['nombre'], axis=1)


ep.info()
sns.countplot(ep['sexe'], sexe = 'Count')