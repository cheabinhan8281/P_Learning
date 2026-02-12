import csv

li = [
    [10,20,30,40,50],
    [60,70,80,90,100],
    [110,120,130,140,150]
]

# csv file 읽고 쓰기
# Comma Separated Value, CSV
# with open('test.csv', 'w',encoding='utf-8') as f:

#     for data in li:
#         s=','.join([str(n) for n in data])
#         f.write(s)
#         f.write('\n')

with open('test.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for r in reader:
        print([int(n) for n in r])