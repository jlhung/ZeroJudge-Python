'''
20200723    v1.0    jlhung  
'''
'''
a1 = 2
a2 = a1 + 2 * 1
a3 = a2 + 2 * 2
....
an = an-1 + 2 * ( n - 1)
+)-------------------------
an = 2 * (n-1) * n / 2 + 2 = n2 - n + 2 
'''

while True:
    try:
        n = int(input())
        print(n * n - n + 2)
        
    except(EOFError):
        break