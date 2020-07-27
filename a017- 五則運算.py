'''
20200717	jlhung	v1.0
'''

while True:
    try:
        print(eval(input().replace("/", "//")))
        
    except(EOFError):
        break