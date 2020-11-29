inFile = open('input.txt', 'r', encoding='utf-8')
outFile = open('output.txt', 'w', encoding='utf-8')
m = []
for line in inFile:
    m.append(line.split())
for i in range(len(m)):
    m[i].pop(2)
m.sort()
for i in range(len(m)):
    print(*m[i], file=outFile)
inFile.close()
outFile.close()
