'''
20200724    v1.0    jlhung  
'''

while True:
    try:
        n, m = map(int, input().split())
        
        if n != m:
            print(m+1)
        else:
            print(m)
        
    except(EOFError):
        break