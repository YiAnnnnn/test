import csv, json
csvFilePath = "test.csv"
jsonFilePath = "test.json"

data = {}
with open(csvFilePath) as csvFile:
	csvReader = csv.DictReader(csvFile)
	for csvRow in csvReader:
		team = csvRow['Team']
		data[team] = csvRow
root = {}
root["test"] = data

with open(jsonFilePath, "w") as jsonFile:
	jsonFile.write(json.dumps(root, indent=4))
