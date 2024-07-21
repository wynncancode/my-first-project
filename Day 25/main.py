# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #     print(temperature)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
#
# data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
# # print(temp_list)
#
# # print(sum(temp_list)/len(temp_list))
# # print(data["temp"].mean())
# # print(data["temp"].max())
#
# #Get Data in Column
# #print(data["condition"])
# # print(data.condition)
#
# # Get Data in Row
# # Pull out the data row where 'day' column is equal to 'Monday'.
# # print(data[data.day == "Monday"])
# # Pull out the row with the maximum temperature.
# # print(data[data.temp == data.temp.max()])
#
# # monday = data[data.day == "Monday"]
# # monday_temp = monday.temp[0]
# # monday_temp_F = monday_temp * 9/5 + 32
# # print(monday_temp_F)
#
# # Create a DataFrame from scratch
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
#
#
#
#

import pandas

data = pandas.read_csv("Squirrel_Data.csv")
# color = data['Primary Fur Color'].value_counts()
# color.to_csv("New_Table.csv")
# print(color)
#print(type(color)) #series

grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnammon", "Black"],
    "Count" : [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")