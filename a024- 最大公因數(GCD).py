'''
20200723    v1.0    jlhung  注意大小 也可以呼叫函數
'''

def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 
  
while True:
    try:
        a, b = map(int, input().split())
        
        print(gcd(max(a, b), min(a, b)))
        
    except(EOFError):
        break