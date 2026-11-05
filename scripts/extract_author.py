import pandas as pd
import requests
from bs4 import BeautifulSoup

records = []

df = pd.read_csv(
    "data/raw/linkedin_posts.csv",
    header=None,
    names=["post_url"]
)

for _, row in df.iterrows():

    url = row["post_url"]

    try:

        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=20
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        title = soup.title.text.strip() if soup.title else ""

        records.append({
            "post_url": url,
            "title": title,
            "status": response.status_code
        })

    except Exception as e:

        records.append({
            "post_url": url,
            "title": "",
            "status": str(e)
        })


result = pd.DataFrame(records)

result.to_excel(
    "output/master_posts.xlsx",
    index=False
)

print(result)
print("\nSaved: output/master_posts.xlsx")