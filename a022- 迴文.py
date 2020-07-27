'''
20200723    v1.0    jlhung  
'''

while True:
    try:
        n = input()
        
        if n == n[::-1]:
            print("yes")
        else:
            print("no")
        
    except(EOFError):
        break