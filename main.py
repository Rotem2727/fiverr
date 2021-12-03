import json
import csv
from tkinter import filedialog as fd

lists = []

toDo = 0 
complete = 0

lineOne = True

with open("file.txt", "w") as f:
    f.write("")

csv_file = fd.askopenfilename()

file = open(csv_file, "r")
csv_reader = csv.reader(file)

for row in csv_reader:
    with open("file.txt", "a") as f:
        if lineOne == False:
            f.write(
                str(row[2:19]).replace("'", "").replace("[", "").replace(
                    "]", "").replace(",", "") + '\n')
        else:
            lineOne = False

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
            json.dump(data, f, indent=4)


with open("file.txt", "r") as file:
    lines = file.readlines()
    linesCount = sum(1 for line in open('file.txt'))
    for line in lines:
        line = line.split()
        for i in range(len(line)):
            line[i] = int(line[i])

        lists.append(line)

    for l in range(linesCount):
        toDo += l

    for i in range(linesCount):
        appearTimes = 1
        for j in range(linesCount - i - 1):
            matchingTimes = 0
            series = []
            if lists[i][0] in lists[i + j + 1]:
                matchingTimes += 1
                series.append(lists[i][0])
            if lists[i][1] in lists[i + j + 1]:
                matchingTimes += 1
                series.append(lists[i][1])
            if lists[i][2] in lists[i + j + 1]:
                matchingTimes += 1
                series.append(lists[i][2])
            if lists[i][3] in lists[i + j + 1]:
                matchingTimes += 1
                series.append(lists[i][3])
            if lists[i][4] in lists[i + j + 1]:
                matchingTimes += 1
                series.append(lists[i][4])
            if lists[i][5] in lists[i + j + 1]:
                matchingTimes += 1
                series.append(lists[i][5])
            if lists[i][6] in lists[i + j + 1]:
                matchingTimes += 1
                series.append(lists[i][6])
            if lists[i][7] in lists[i + j + 1]:
                matchingTimes += 1
                series.append(lists[i][7])
            if lists[i][8] in lists[i + j + 1]:
                matchingTimes += 1
                series.append(lists[i][8])
            if lists[i][9] in lists[i + j + 1]:
                matchingTimes += 1
                series.append(lists[i][9])
            if lists[i][10] in lists[i + j + 1]:
                matchingTimes += 1
                series.append(lists[i][10])
            if lists[i][11] in lists[i + j + 1]:
                matchingTimes += 1
                series.append(lists[i][11])
            if lists[i][12] in lists[i + j + 1]:
                matchingTimes += 1
                series.append(lists[i][12])
            if lists[i][13] in lists[i + j + 1]:
                matchingTimes += 1
                series.append(lists[i][13])
            if lists[i][14] in lists[i + j + 1]:
                matchingTimes += 1
                series.append(lists[i][14])
            if lists[i][15] in lists[i + j + 1]:
                matchingTimes += 1
                series.append(lists[i][15])
            if lists[i][16] in lists[i + j + 1]:
                matchingTimes += 1
                series.append(lists[i][16])

            if matchingTimes == 7:
                creatingJsonFile(series, len(series))
            if matchingTimes == 6:
                creatingJsonFile(series, len(series))
            if matchingTimes == 5:
                creatingJsonFile(series, len(series))

            complete+= 1
            print(f"{complete}/{toDo} | {(complete*100)/toDo} %\r", end="")

    with open("series.json", "r") as f:
        data = json.load(f)

        highestSevenKey = ""
        highestSevenValue = 0
        secondSevenKey = ""
        secondSevenValue = 0
        thirdSevenKey = ""
        thirdSevenValue = 0

        highestSixKey = ""
        highestSixValue = 0
        secondSixKey = ""
        secondSixValue = 0
        thirdSixKey = ""
        thirdSixValue = 0

        highestFiveKey = ""
        highestFiveValue = 0
        secondFiveKey = ""
        secondFiveValue = 0
        thirdFiveKey = ""
        thirdFiveValue = 0
        for key, value in data.items():
            if data[key]["length"] == 7:
                if data[key]["appearTimes"] > highestSevenValue:
                    highestSevenValue = data[key]["appearTimes"]
                    highestSevenKey = data[key]["series"].replace("[",
                                                                  "").replace(
                                                                      "]", "")
                elif data[key]["appearTimes"] > secondSevenValue:
                    secondSevenValue = data[key]["appearTimes"]
                    secondSevenKey = data[key]["series"].replace("[",
                                                                 "").replace(
                                                                     "]", "")
                elif data[key]["appearTimes"] > thirdSevenValue:
                    thirdSevenValue = data[key]["appearTimes"]
                    thirdSevenKey = data[key]["series"].replace("[",
                                                                "").replace(
                                                                    "]", "")

            if data[key]["length"] == 6:
                if data[key]["appearTimes"] > highestSixValue:
                    highestSixValue = data[key]["appearTimes"]
                    highestSixKey = data[key]["series"].replace("[",
                                                                "").replace(
                                                                    "]", "")
                elif data[key]["appearTimes"] > secondSixValue:
                    secondSixValue = data[key]["appearTimes"]
                    secondSixKey = data[key]["series"].replace("[",
                                                               "").replace(
                                                                   "]", "")
                elif data[key]["appearTimes"] > thirdSixValue:
                    thirdSixValue = data[key]["appearTimes"]
                    thirdSixKey = data[key]["series"].replace("[", "").replace(
                        "]", "")

            if data[key]["length"] == 5:
                if data[key]["appearTimes"] > highestFiveValue:
                    highestFiveValue = data[key]["appearTimes"]
                    highestFiveKey = data[key]["series"].replace("[",
                                                                 "").replace(
                                                                     "]", "")
                elif data[key]["appearTimes"] > secondFiveValue:
                    secondFiveValue = data[key]["appearTimes"]
                    secondFiveKey = data[key]["series"].replace("[",
                                                                "").replace(
                                                                    "]", "")
                elif data[key]["appearTimes"] > thirdFiveValue:
                    thirdFiveValue = data[key]["appearTimes"]
                    thirdFiveKey = data[key]["series"].replace("[",
                                                               "").replace(
                                                                   "]", "")

        if highestSevenValue != 0:
            print(
                f"\nFirst Prize:\n	1. series: {highestSevenKey}, appears: {highestSevenValue}."
            )
        else:
            print("Sorry, no 7 numbers series.")
        if secondSevenValue != 0:
            print(
                f"	2. series: {secondSevenKey}, appears: {secondSevenValue}.")
        if thirdSevenValue != 0:
            print(f"	3. series: {thirdSevenKey}, appears: {thirdSevenValue}.")

        if highestSixValue != 0:
            print(
                f"\nSecond Prize:\n	1. series: {highestSixKey}, appears: {highestSixValue}."
            )
        else:
            print("Sorry, no 6 numbers series.")
        if secondSixValue != 0:
            print(f"	2. series: {secondSixKey}, appears: {secondSixValue}.")
        if thirdSixValue != 0:
            print(f"	3. series: {thirdSixKey}, appears: {thirdSixValue}.")

        if highestFiveValue != 0:
            print(
                f"\nThird Prize:\n	1. series: {highestFiveKey}, appears: {highestFiveValue}."
            )
        else:
            print("Sorry, no 5 numbers series.")
        if secondFiveValue != 0:
            print(f"	2. series: {secondFiveKey}, appears: {secondFiveValue}.")
        if thirdFiveValue != 0:
            print(f"	3. series: {thirdFiveKey}, appears: {thirdFiveValue}.")
