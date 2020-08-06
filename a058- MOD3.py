'''
20200724    v1.0    jlhung  
'''

while True:
    try:
        n = int(input())
        
        x = [0, 0, 0]
        for _ in range(n):
            x[int(input()) % 3] += 1
        
        print(" ".join([str(c) for c in x]))

    except(EOFError):
        break
