'''
20200723    v1.0    jlhung  
'''

while True:
    try:
        n = int(input())
        print((n * n * n + 5 * n + 6) // 6)

    except(EOFError):
        break