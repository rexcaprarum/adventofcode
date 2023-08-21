
d = open("day1_data.txt", "r")
data_list = []
biggest = 0
t = 0

for i in d.readlines():
    data_list.append(i.strip('\n'))
    
for i in range(0, len(data_list)):
    if not data_list[i] == '':
        t += int(data_list[i])
    elif data_list[i] == '':
        if t > biggest:
            biggest = t 
            t = 0
        else:
            t = 0
    
    
return biggest
