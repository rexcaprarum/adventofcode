
f = open("day1_data.txt", 'r')
data = []
x = 0

for i in f:
    data.append(int(i))\

for i in range(0, len(data)-1):
    for y in data:
        for s in data:
            if y + s + data [i] == 2020:
                x = y * s * data[i]

print(x)
