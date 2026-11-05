from googlesearch import search
import pandas as pd
queries=["site:linkedin.com/posts AWS Data Engineer","site:linkedin.com/posts Spark Interview Questions"]
rows=[]
for q in queries:
    for url in search(q,num_results=100):
        rows.append({"query":q,"post_url":url})
pd.DataFrame(rows).to_csv("linkedin_post_urls.csv",index=False)