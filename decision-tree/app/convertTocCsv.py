import json
import csv

with open("D:/MonBureau/GL4/semestre2/DataMining/decision-tree/app/data.json") as file:
    data = json.load(file)
    fieldnames = ['temperature', 'heartbeat', 'humidity', 'sick']
with open("D:/MonBureau/GL4/semestre2/DataMining/decision-tree/app/dataSet.csv", "wb+") as file:
    #csv_file = csv.writer(file)
    #for item in data:
        #csv_file.writerow(item['temperature'], item['heartbeat'], item['humidity'], item['sick'])
		

    csv_file = csv.writer(file)
    for item in data:
        csv_file.writerow([item['temperature'], item['humidity'] , item['heartbeat'],item['sick']])