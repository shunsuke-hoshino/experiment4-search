import csv

def search(word):
    searchname = word
    csv_file = open("\tmp\8daaccf9c411f4e\\search\\db\\kaken.csv","r",encoding="UTF-8")

    reader = csv.reader(csv_file)
    header = next(reader)

    i = header.index("研究代表者")
    j = header.index("研究開始時の研究の概要")
    count = 0
    personlist= []

    for row in reader :
        person = row[i]
        topic = row[j]
        if word in topic:
            personlist.append(person)
            count = count + 1

            #print(person, topic[:30])
            
    if(count == 0):
        return count
    return personlist
