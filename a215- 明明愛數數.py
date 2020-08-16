'''
20200728    v1.0    jlhung  
'''

while True:
    try:
        n, m = map(int, input().split())
        
        count = 1   #次數
        total = n   #總和
        while total <= m:
            n += 1
            count += 1
            total += n
            
        print(count)    
        
            
    except(EOFError):
        break