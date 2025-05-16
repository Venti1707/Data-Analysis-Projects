from matplotlib import pyplot as plt
import requests
import pandas as pd

dataset_id = "d_b9d53bcdd4f307fef1c6da82a90ac0dc"
url = "https://data.gov.sg/api/action/datastore_search?resource_id=" + dataset_id
response = requests.get(url)
data = response.json()
records = data["result"]["records"]
df = pd.DataFrame(records)
df["year"] = pd.to_numeric(df["year"])
df["interestgroups"] = pd.to_numeric(df["interestgroups"])

pivot_df = df.pivot(index="year", columns="category", values="interestgroups")
labels = [str(int(year)) for year in pivot_df.index]

ax = pivot_df.plot(kind="line", marker="x", figsize=(12, 6))
plt.title("Number of Performing Arts Interest Groups in CCs and RCs")
plt.xlabel("Year")
plt.ylabel("Interest Groups")
plt.grid(True)
plt.legend(title="Museum")
plt.xticks(ticks=pivot_df.index, labels=labels)
plt.tight_layout()
plt.style.use("fivethirtyeight")
plt.savefig("C:/OtherProjects/Data-Analysis-Projects/Arts & Culture/Number of Performing Arts Interest Groups in CCs and RCs/Index.png")
plt.show()