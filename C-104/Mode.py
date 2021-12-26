import csv
with open('D:/C-104/HeightWeight.csv', newline='')as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
newData = []
for i in range(len(file_data)):
    num = file_data[i][1]
    newData.append(float(num))
n = len(newData)
total = 0
for x in newData:
    total = total + x
mean = total/n

newData.sort()
if n % 2 == 0:
	median1 = float(newData[n//2])
	median2 = float(newData[n//2 + 1])
	median = (median1 + median2)/2
else:
	median = newData[n//2 + 0.5]

mode = (median*3 - mean*2)
print("The mode is "+str(mode))