from matplotlib import pyplot as plt
import requests
import pandas as pd

dataset_id = "d_618a1224b896b436ce650be1f77c804e"
url = "https://data.gov.sg/api/action/datastore_search?resource_id=" + dataset_id
response = requests.get(url)
data = response.json()
records = data["result"]["records"]
df = pd.DataFrame(records)
df["year"] = pd.to_numeric(df["year"])
df["visitorship"] = pd.to_numeric(df["visitorship"].replace("-", 0))

pivot_df = df.pivot(index="year", columns="museum", values="visitorship")
labels = [str(int(year)) for year in pivot_df.index]

ax = pivot_df.plot(kind="line", marker="x", figsize=(18, 9))
plt.title("Visitorship to National Museums and Heritage Institutions")
plt.xlabel("Year")
plt.ylabel("Visitorship")
plt.grid(True)
plt.legend(title="Museum")
plt.xticks(ticks=pivot_df.index, labels=labels)
plt.tight_layout()
plt.style.use("fivethirtyeight")
plt.savefig("C:/OtherProjects/Data-Analysis-Projects/Arts & Culture/Visitorship to National Museums and Heritage Institutions/Index.png")
plt.show()