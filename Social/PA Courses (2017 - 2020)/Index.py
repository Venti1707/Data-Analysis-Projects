from matplotlib import pyplot as plt
import requests
import pandas as pd

dataset_id = "d_80ece7b4cf25e843592ef0431f96f6e2"
url = "https://data.gov.sg/api/action/datastore_search?resource_id=" + dataset_id
response = requests.get(url)
data = response.json()
records = data["result"]["records"]
df = pd.DataFrame(records)
df["year"] = pd.to_numeric(df["year"])
df["no_of_classes"] = pd.to_numeric(df["no_of_classes"])
df["course_category"] = df["course_category"].replace({
    'ARTS, CRAFTS & HOBBIES"': 'ARTS, CRAFTS & HOBBIES'
}) # There is an erroneous double quote in the data

pivot_df = df.pivot(index="year", columns="course_category", values="no_of_classes")
labels = [str(int(year)) for year in pivot_df.index]

ax = pivot_df.plot(kind="line", marker="x", figsize=(12, 6))
plt.title("PA Courses (2017 - 2020)")
plt.xlabel("Year")
plt.ylabel("Number of classes")
plt.grid(True)
plt.legend(title="Course Category")
plt.xticks(ticks=pivot_df.index, labels=labels)
plt.tight_layout()
plt.style.use("fivethirtyeight")
plt.savefig("C:/OtherProjects/Data-Analysis-Projects/Social/PA Courses (2017 - 2020)/Index.png")
plt.show()