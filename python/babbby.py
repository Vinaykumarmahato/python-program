#creating data frame from the  list
import pandas as pd
data=[['tom',10],['nick',15],['juli',14]]
df=pd.dataframe(data, colums=['name','aage'])
prinnt(df)
