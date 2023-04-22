# import csv
#
# with open("./weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if(row[1] != "temp"):
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Red"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur color": ["Gray", "Red", "Black"],
    "Count": [gray_count, red_count, black_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
