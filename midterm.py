import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

es = Elasticsearch("http://localhost:9200")

data1 = pd.read_csv("G:\\Nazanin\\takmili\\organizations-10000.csv")
data = data1.dropna()

def make_data(data, index):
    for _, row in data.iterrows():
        yield {
            "_index": index,
            "_source": {"Organization Id": row["Organization Id"],
                        "Name": row["Name"],
                        "Website": row["Website"],
                        "Country": row["Country"],
                        "Description": row["Description"],
                        "Founded": row["Founded"],
                        "Industry": row["Industry"],
                        "Number of employees": row["Number of employees"]
                        }
        }

bulk(es, make_data(data,"organization-10000"))

#1
unique_Country = pd.DataFrame(data["Country"].unique())

print("number of unique countries:", len(unique_Country))
#2
unique_Organization = pd.DataFrame(data["Name"].unique())

print("number of unique organizations:", len(unique_Organization))
#3
organizations_in_same_country = data.groupby("Country")["Name"].count()
print(organizations_in_same_country)
#4
Organizations_Over100 = pd.DataFrame(data[data["Number of employees"] > 100]["Name"].unique())

print("number of organizations with over 100 employees:", len(Organizations_Over100))
#5
max_employee = data["Number of employees"].max()

Organization_maxEmployee = data[data["Number of employees"] == max_employee]["Name"].tolist()

print("name of organization with maximum employee:", Organization_maxEmployee)
#6
min_employee = data["Number of employees"].min()

Organization_minEmployee = data[data["Number of employees"] == min_employee]["Name"].tolist()

print("name of organization with minimum employee:", Organization_minEmployee)
