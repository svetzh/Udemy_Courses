import csv
import pandas as pd

with open("weather_data.csv", "r") as weather_file:
    raw_data = weather_file.readlines()
    for d in raw_data:
        strip_data = d.strip()
        # print(strip_data)

with open("weather_data.csv") as data_file:
    data = csv.DictReader(data_file)
    temperatures = []
    for row in data:
        temperature = int(row["temp"])
        temperatures.append(temperature)
    # print(temperatures)


with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    next(data)
    temperatures = []
    for row in data:
        temperature = int(row[1])
        temperatures.append(temperature)
    # print(temperatures)

data = pd.read_csv("weather_data.csv")
print(data)

data_dict = data.to_dict()
# print(data_dict)

temp_lst = data["temp"].to_list()
#
# print(data[data["day"] == "Tuesday"])
# print(data[data.day == "Sunday"])
# print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)

student_dict = {
    "students": ["Any", "Moni", "Gosho", "Stoq"],
    "scores": [55, 35, 14, 89]
}
dd = pd.DataFrame(student_dict)
dd.to_csv("studets_data.csv")

# data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# fur_lst = data["Primary Fur Color"].to_list()
# fur_set = set(fur_lst)
#
# squirrel_dict = {
#     "Fur Color": [],
#     "Count": []
# }
# for color in fur_set:
#     count_fur = fur_lst.count(color)
#     if pd.notna(color):
#         squirrel_dict["Fur Color"].append(color)
#         squirrel_dict["Count"].append(count_fur)
#
# squirrel_count = pd.DataFrame(squirrel_dict)
#
# squirrel_count.to_csv("squirrel_count.csv")


