'''
20200717    v1.0    jlhung  
'''

while True:
    try:
        n = input()    
        print("".join([chr(ord(c)-7) for c in n])) 
        
    except(EOFError):
        break