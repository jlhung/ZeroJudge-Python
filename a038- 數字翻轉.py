'''
20200723    v1.0    jlhung  "0"也要輸出  要消除尾數的0
'''

while True:
    try:
        n = int(input())
        
        if n == 0:
            print(0)
            break
    
        while n % 10 == 0:
            n //= 10
            
        print(str(n)[::-1])
        
    except(EOFError):
        break