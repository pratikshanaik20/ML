import pandas as pd
import numpy as np
dict={'First score':[100,90,np.nan,95],
      'Second score':[30,45,56,np.nan],
      'Third score':[np.nan,40,80,98]}
df=pd.DataFrame(dict)
print(df.isnull())