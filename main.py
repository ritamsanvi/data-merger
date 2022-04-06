import csv
data=[]
with open("bright_stars.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)

headers=data[0]
star_data=data[1:]

#converting all the planet names to lowcase
for data_point in star_data:
    data_point[2]=data_point[2].lower()

#sorting planet name in alphabetical order
star_data.sort(key= lambda planet_data:planet_data[2])

with open("dwarf_stars.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)
    