'''
20200728    v1.0    jlhung  注意0
'''

while True:
    try:
        m = int(input())
        
        for i in range(m):
            n = int(input())
            
            total = 1
            if n == 0:
                total = 0
                      
            while n > 0:
                total *= (n % 10)
                n //= 10
            
            print(total)
            
    except(EOFError):
        break