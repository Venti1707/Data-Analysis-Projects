from matplotlib import pyplot as plt
import requests
import pandas as pd

dataset_id = "d_ad1036159bf22ebfc6d1425175701ea7"
url = "https://data.gov.sg/api/action/datastore_search?resource_id=" + dataset_id
response = requests.get(url)
data = response.json()
records = data["result"]["records"]
df = pd.DataFrame(records)
df["year"] = pd.to_numeric(df["year"])
df["no_of_participants"] = pd.to_numeric(df["no_of_participants"])

pivot_df = df.pivot(index="year", columns="course_category", values="no_of_participants")
labels = [str(int(year)) for year in pivot_df.index]

ax = pivot_df.plot(kind="line", marker="x", figsize=(12, 6))
plt.title("PA Course Participation (2021 - 2023)")
plt.xlabel("Year")
plt.ylabel("Number of participants")
plt.grid(True)
plt.legend(title="Course Category")
plt.xticks(ticks=pivot_df.index, labels=labels)
plt.tight_layout()
plt.style.use("fivethirtyeight")
plt.savefig("C:/OtherProjects/Data-Analysis-Projects/Social/PA Course Participation (2021 - 2023)/Index.png")
plt.show()