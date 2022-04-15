from pandas import read_csv,DataFrame
print("Analysing data ...")
data_frame = read_csv("../res/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_series_primary_fur_color =data_frame["Primary Fur Color"]
gray_squirrels =data_frame[data_series_primary_fur_color=="Gray"]
red_squirrels =data_frame[data_series_primary_fur_color=="Cinnamon"]
black_squirrels =data_frame[data_series_primary_fur_color=="Black"]
print(f"gray squirrels : {len(gray_squirrels)}")
print(f"red squirrels : {len(red_squirrels)}")
print(f"black squirrels : {len(black_squirrels)}")
print("Analysis Done.")
print("--------------")
print("Writing data..")
data_set={
    "fur_color":['gray','red','black'],
    "counts" : [len(gray_squirrels),len(red_squirrels),len(black_squirrels)]
}
print(data_set)
new_data_frame=DataFrame(data_set)
new_data_frame.to_csv("../out/suirrels_data.csv")

