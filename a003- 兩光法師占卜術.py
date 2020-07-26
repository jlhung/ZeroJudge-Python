'''
20200717    v1.0    jlhung  
'''

lucky = {0:"普通", 1:"吉", 2:"大吉"}

while True:
    try:
        M, D = map(int, input().split())
        print(lucky[(M * 2 + D) % 3])
    except(EOFError):
        break