# Still working. If you are reading this, just know that I know I am doing too much and I need to do less.


f = open("day2_data.txt", 'r')
data = []
nums = ['1','2','3','4','5','6','7','8','9','0']


for i in f:
    data.append(i)
    
for p in data:
    ran = []
    for i in range(len(p)):
        
        
        
        s = 0
        e = 0
        
        if p[i] in nums:
            ran.append(p[i])
        elif p[i] == '-':
            ran.append('-')
            
