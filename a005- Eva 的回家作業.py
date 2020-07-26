'''
20200717    v1.0    jlhung  
'''

m = int(input())

for _ in range(m):
    n = list(map(int, input().split()))
    
    if n[1]-n[0] == n[2]-n[1]:
        n.append(n[3] + (n[1]-n[0]))
    else:
        n.append(n[3] * (n[1]//n[0]))
    
    print(" ".join([str(c) for c in n]))
            