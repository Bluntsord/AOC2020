with open("AOCD3 dataset.py",'r') as f:
    data = f.readlines()

collen = len(data)
Dataset = []
for i in range(collen):
    Dataset.append(data[i].replace("\n",""))
# print(Dataset)
rowlen = len(Dataset[0])

treeCounter = 0

for i in range(collen-1):


