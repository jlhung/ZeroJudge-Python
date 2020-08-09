'''
20200727    v1.0    jlhung  
'''

while True:
    try:
        m = input()
        n = list(map(int, input().split()))
        n.sort()
        
        print(" ".join([str(c) for c in n]))
        
    except(EOFError):
        break