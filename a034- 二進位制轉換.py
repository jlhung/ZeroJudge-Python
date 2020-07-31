'''
20200723    v1.0    jlhung  處理後再反轉字串
'''

while True:
    try:
        n = int(input())

        b = ""
        while n > 0:
            b += str(n % 2)
            n //= 2
            
        print(b[::-1])
            
    except(EOFError):
        break