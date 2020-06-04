import pandas as pd
import numpy as np
data=pd.read_csv('test4.csv')
dd=pd.DataFrame(data)
dd['NTN'] = dd['NTN'].str.split('/')

# convert list of pd.Series then stack it
dd = (dd
 .set_index(['SR_NO','NAME','BUSINESS_NAME'])['NTN']
 .apply(pd.Series)
 .stack()
 .reset_index()
 .drop('level_3', axis=1)
 .rename(columns={0:'NTN'}))
print(dd)