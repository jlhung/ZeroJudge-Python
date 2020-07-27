'''
20200717	jlhung	v1.0
'''

while True:
    try:
        n = int(input())
        
        x = 2       #因數
        count = 0   #次方
        ans = ""
        chk = 0     #檢查乘號
        while True:
            #整除則繼續
            if n % x == 0:
                count += 1
                n //= x
                continue
            
            #不整除檢查次數後印出 或因數x大於n也印出
            if n % x != 0 or x > n:
                if count == 0:
                    x += 1
                    continue
                
                #檢查乘號
                if chk != 0:
                    ans = ans + " * "
                
                if count > 1:
                    ans = ans + "{}^{}".format(x, count)
                elif count == 1:
                    ans = ans + "{}".format(x)
                    
                x += 1
                count = 0
                chk = 1
                    
                if x > n:
                    break
        
        print(ans)        
        
    except(EOFError):
        break