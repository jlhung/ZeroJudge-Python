'''
20200717    v1.0    jlhung  
'''

while True:
    try:
        a, b, c = list(map(int, input().split()))
        
        if b**2 - 4*a*c >= 0:
            a1 = (-1*b + ((b**2 - 4*a*c) ** 0.5)) / (2*a)
            a2 = (-1*b - ((b**2 - 4*a*c) ** 0.5)) / (2*a)
        
            x1 = int(max(a1, a2))
            x2 = int(min(a1, a2))
        
            if x1 != x2:
                print("Two different roots x1={} , x2={}".format(x1, x2))
            elif  x1 == x2:
                print("Two same roots x={}".format(x1))
            else:
                print("No real root")
        else:
            print("No real root")
            
    except(EOFError):
        break