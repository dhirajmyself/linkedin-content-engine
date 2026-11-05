TOPICS={"AWS":["s3","glue"],"SPARK":["spark"],"DATABRICKS":["delta"],"SQL":["sql"]}

def classify(text):
    t=text.lower()
    for topic,keys in TOPICS.items():
        if any(k in t for k in keys):
            return topic
    return "OTHER"