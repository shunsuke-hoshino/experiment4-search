import csv

word = "ロボット"
csv_file = open("./kaken.csv","r",encoding="UTF-8")

reader = csv.reader(csv_file)
header = next(reader)

i = header.index("研究代表者")
j = header.index("研究開始時の研究の概要")

for row in reader :
    person = row[i]
    topic = row[j]
    if word in topic:
        print(person, topic[:30])