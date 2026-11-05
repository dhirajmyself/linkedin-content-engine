from googlesearch import search
query = "site:linkedin.com/posts AWS Data Engineer"
count = 0
for url in search(query, num_results=10):
    count += 1
    print(url)
print(f"Total URLs Found: {count}")