import pandas as pd
df=pd.read_csv("clean_posts.csv")
df.to_excel("master_posts.xlsx",index=False)