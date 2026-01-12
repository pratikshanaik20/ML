import pandas as pd
dict={'name':["aparna","pankaj","sudhir","geeku"],
      'degree':["MBA","BCA","M.TECH","MBA"],
      'score':[90,40,80,98]}
df=pd.DataFrame(dict)
for i,j in df.iterrows():
    print(i,j)
    print()