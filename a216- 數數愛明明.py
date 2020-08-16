'''
20200728    v1.0    jlhung  
'''

while True:
    try:
        n = int(input())    
        print(n*(n+1)//2, n*(n+1)*(n+2)//6)
                
    except(EOFError):
        break