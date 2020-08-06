'''
20200724    v1.0    jlhung  
'''

P = []
for i in range(1, 32):
    P.append(i*i)
    
    
while True:
    try:
        n = int(input())
            
        case = 0    
        for i in range(n):
            a = int(input())
            b = int(input())
            
            total = 0
            for i in range(a, b+1):
                if i in P:
                    total += i
            
            case += 1
            print("Case {}: {}".format(case, total))

    except(EOFError):
        break

    