import json

lists = []

with open("series.json", "r") as f:
	data = json.load(f)
	data = {}

	with open("series.json", "w") as f:
		json.dump(data, f)

def creatingJsonFile(series, seriesLen):
	with open("series.json", "r") as file:
		data = json.load(file)
		
		if str(series) in data:
			data[str(series)]["appearTimes"] += 1
		else:
			data[str(series)] = {}
			data[str(series)]["series"] = str(series)
			data[str(series)]["appearTimes"] = 2
			data[str(series)]["length"] = int(seriesLen)

		with open("series.json", 'w') as f:
			json.dump(data, f)

with open("file.txt", "r") as file:
	lines = file.readlines()
	linesCount = sum(1 for line in open('file.txt'))
	for line in lines:
		line = line.split()
		for i in range(len(line)):
			line[i] = int(line[i])
			
		lists.append(line)

	for i in range(linesCount):
		appearTimes = 1
		for j in range(linesCount-i-1):
			matchingTimes = 0
			series = []
			if lists[i][0] in lists[i+j+1]:
				matchingTimes += 1
				series.append(lists[i][0])
			if lists[i][1] in lists[i+j+1]:
				matchingTimes += 1
				series.append(lists[i][1])
			if lists[i][2] in lists[i+j+1]:
				matchingTimes += 1
				series.append(lists[i][2])
			if lists[i][3] in lists[i+j+1]:
				matchingTimes += 1
				series.append(lists[i][3])
			if lists[i][4] in lists[i+j+1]:
				matchingTimes += 1
				series.append(lists[i][4])
			if lists[i][5] in lists[i+j+1]:
				matchingTimes += 1
				series.append(lists[i][5])
			if lists[i][6] in lists[i+j+1]:
				matchingTimes += 1
				series.append(lists[i][6])
			if lists[i][7] in lists[i+j+1]:
				matchingTimes += 1
				series.append(lists[i][7])
			if lists[i][8] in lists[i+j+1]:
				matchingTimes += 1
				series.append(lists[i][8])
			if lists[i][9] in lists[i+j+1]:
				matchingTimes += 1
				series.append(lists[i][9])
			if lists[i][10] in lists[i+j+1]:
				matchingTimes += 1
				series.append(lists[i][10])
			if lists[i][11] in lists[i+j+1]:
				matchingTimes += 1
				series.append(lists[i][11])
			if lists[i][12] in lists[i+j+1]:
				matchingTimes += 1
				series.append(lists[i][12])
			if lists[i][13] in lists[i+j+1]:
				matchingTimes += 1
				series.append(lists[i][13])
			if lists[i][14] in lists[i+j+1]:
				matchingTimes += 1
				series.append(lists[i][14])
			if lists[i][15] in lists[i+j+1]:
				matchingTimes += 1
				series.append(lists[i][15])
			if lists[i][16] in lists[i+j+1]:
				matchingTimes += 1
				series.append(lists[i][16])

			if matchingTimes == 7:
				creatingJsonFile(series, len(series))
			if matchingTimes == 6:
				creatingJsonFile(series, len(series))
			if matchingTimes == 5:
				creatingJsonFile(series, len(series))

	with open("series.json", "r") as f:
		data = json.load(f)

		for i in range(3):
			highstKey = ""
			highstValue = 0
			secondKey = ""
			secondValue = 0
			thirdKey = ""
			thirdValue = 0
			for key, value in data.items():
				if data[key]["appearTimes"] > highstValue and data[key]["length"] == i+5:
					highstKey = data[key]["series"]
					highstValue = data[key]["appearTimes"]
				if data[key]["appearTimes"] > secondValue and data[key]["length"] == i+5:
					secondKey = data[key]["series"]
					secondValue = data[key]["appearTimes"]
					thirdValue = data[key]["appearTimes"]
				if data[key]["appearTimes"] > thirdValue and data[key]["length"] == i+5:
					thirdKey = data[key]["series"]
					thirdValue = data[key]["appearTimes"]