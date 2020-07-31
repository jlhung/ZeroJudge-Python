'''
20200723    v1.0    jlhung  
'''

#製表
p = [1,2,3,4,5,6,7,8,9,153,370,371,407,1634,8208,9474,54748,92727,93084,548834,1741725,4210818,9800817,9926315]
        
while True:
    try:
        a, b = map(int, input().split())
        
        ans = ""
        for i in range(0, len(p)):
            if a <= p[i] and p[i] <= b:
                if len(ans) > 0:
                    ans += " "
                ans += str(p[i])
        
        if len(ans) == 0:
            print("none")
        else:
            print(ans)
        
    except(EOFError):
        break