'''
20200728    v1.0    jlhung  
'''

while True:
    try:
        n = list(map(int, input().split()))
        
        if sum(n[1:]) / (len(n)-1) > 59:
            print("no")
        else:
            print("yes")
            
    except(EOFError):
        break