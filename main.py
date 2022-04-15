from pandas import read_csv
data=read_csv("res/weather_data.csv")
temp_list=data["temp"].to_list()
max_temp=max(temp_list)
print(f"Max Temprature : {max_temp}")
print(f"Details :\n{data[data['temp']==max_temp]}")
print(f"Average Temprature : {(sum(temp_list)/len(temp_list))}")
