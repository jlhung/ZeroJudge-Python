'''
20200727    v1.0    jlhung  
'''

while True:
    try:
        n = int(input())
        
        if n == 0:
            break
        
        ans = ""
        for i in range(1, n):
            if i % 7 > 0:
                if i > 1:
                    ans += " "
                ans += str(i)
                
        print(ans)
        
    except(EOFError):
        break