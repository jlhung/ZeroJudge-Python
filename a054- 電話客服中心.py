'''
20200724    v1.0    jlhung  
'''

P = {"A":10, "B":11, "C":12, 
     "D":13, "E":14, "F":15, 
     "G":16, "H":17, "I":34, 
     "J":18, "K":19, "L":20, 
     "M":21, "N":22, "O":35, 
     "P":23, "Q":24, "R":25,
     "S":26, "T":27, "U":28, 
     "V":29, "W":32, "X":30, 
     "Y":31, "Z":33 }      
     
while True:
    try:
        n = input()        
        total = 0
        
        #處理英文 轉ASCII處理
        #total = P[n[0]] // 10 + P[n[0]] % 10 * 9

        #處理中間8碼
        c = 8
        for t in n[0:8]:
            total += int(t) * c
            c -= 1
        
        #處理尾碼
        total += int(n[8])

        ans = ""
        for keys, values in P.items():
            if (P[keys] // 10 + P[keys] % 10 * 9 + total) % 10 == 0:
                ans = ans + keys
        
        print(ans)
        
    except(EOFError):
        break