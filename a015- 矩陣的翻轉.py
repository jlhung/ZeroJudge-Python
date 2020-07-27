'''
20200717	jlhung	v1.0
'''

while True:
    try:
        m, n = map(int, input().split())
        m_t, n_t = n, m
        
        X =  [[0 for i in range(n)] for j in range(m)]
        Y =  [[0 for i in range(m)] for j in range(n)]
        
        for i in range(m):
            X[i] = list(map(int, input().split()))
            
        for i in range(n):
            msg = ""
            for j in range(m):
                if len(msg) > 0:
                    msg += " "
                msg += str(X[j][i])
            print(msg)
    
    except(EOFError):
        break