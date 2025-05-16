from matplotlib import pyplot as plt
import pandas as pd
import requests

# Fetch data
dataset_id = "d_abeeab6fb3b739d7b234e7452bafd07c"
url = "https://data.gov.sg/api/action/datastore_search?resource_id=" + dataset_id
response = requests.get(url)
records = response.json()["result"]["records"]
df = pd.DataFrame(records)
df["count"] = pd.to_numeric(df["count"])

# Define month order
month_order = ["Jan 23", "Feb 23", "Mar 23", "Apr 23", "May 23", "Jun 23", "Jul 23", "Aug 23", "Sep 23", "Oct 23", "Nov 23", "Dec 23"]
df["as_of_month"] = pd.Categorical(df["as_of_month"], categories=month_order)

# Group and reshape
grouped = df.groupby(["as_of_month", "age_groups"])["count"].sum()
chart = grouped.unstack("age_groups")

chart.plot(kind="bar", stacked=True)
plt.xlabel("Month")
plt.ylabel("Count")
plt.title("Number of COVID-19 deaths by month")
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.style.use("fivethirtyeight")
plt.savefig("C:/OtherProjects/Data-Analysis-Projects/COVID-19/Number of COVID-19 deaths by month/Index.png")
plt.show()