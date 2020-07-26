'''
20200717    v1.0    jlhung  
'''

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except(EOFError):
        break