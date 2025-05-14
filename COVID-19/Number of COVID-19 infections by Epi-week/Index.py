from matplotlib import dates as mdates
from matplotlib import pyplot as plt
import pandas as pd
import requests

dataset_id = "d_11e68bba3b3c76733475a72d09759eeb"
url = "https://data.gov.sg/api/action/datastore_search?resource_id=" + dataset_id
response = requests.get(url)
result = response.json()["result"]
records = result["records"]
df = pd.DataFrame(records)
df_est_count = df["est_count"]
df_week = df["epi_week"]

count = pd.to_numeric(df_est_count)
date = pd.to_datetime(df_week.str.replace("-", "-W") + "-1", format="%G-W%V-%u")
df_sort = df.sort_values("epi_week")
mean_val = count.mean()
above = count > mean_val
below = ~above

plt.plot(date, count, marker="o", linestyle="-")
plt.axhline(mean_val, color="red", linestyle="--", label=f"Mean: {mean_val:.2f}")
plt.fill_between(date, count, mean_val, where=above, interpolate=True, color="red", alpha=0.3, label="Above mean")
plt.fill_between(date, count, mean_val, where=below, interpolate=True, color="green", alpha=0.3, label="Below mean")
plt.title("Number of COVID-19 Infections by Week")
plt.xlabel("Month")
plt.ylabel("Estimated count")
plt.grid(True)
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.style.use("fivethirtyeight")
plt.savefig("C:/OtherProjects/Data-Analysis-Projects/COVID-19/Number of COVID-19 infections by Epi-week/Index.png")
plt.show()