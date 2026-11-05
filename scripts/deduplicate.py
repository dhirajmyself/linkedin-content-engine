import pandas as pd
df=pd.read_csv("posts.csv")
df=df.drop_duplicates(subset=["post_url"])
df.to_csv("clean_posts.csv",index=False)