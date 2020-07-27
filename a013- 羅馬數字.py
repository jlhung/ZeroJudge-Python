'''
20200717	jlhung	v1.0
'''

num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
Roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]

def calc(p):   
    tmp = 0 #讀取位置
    total = 0
    while tmp < len(p):
        #print(p[tmp:tmp+2], Roman.index(p[tmp:tmp+2]))
        if p[tmp:tmp+2] in Roman:
            total += num[Roman.index(p[tmp:tmp+2])]
            tmp += 2
        else:
            total += num[Roman.index(p[tmp:tmp+1])]
            tmp += 1
    return total    
   
def tran(m):
    t = 0
    ans = ""
    
    while m > 0:
        if m >= num[t]:
            ans += Roman[t]
            m -= num[t]
        else:
            t += 1          
    return ans
   
while True:
    n = input()
    
    if n == "#":
        break
        
    a, b = n.split()
    ans = abs(calc(a)-calc(b))
    
    if ans == 0:
        print("ZERO")
    else:
        print(tran(ans))