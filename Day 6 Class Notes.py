# Class Notes
# Thursday, July 5, 2018

import pandas as pd
df = pd.DataFrame({'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8], 'c': [9, 10, 11, 12]}
    ,index=['i', 'ii', 'iii', 'iv'])
df
df.describe()
df.describe().loc['mean']
df.describe().iloc[1]
df.describe().loc[['mean','min']]
