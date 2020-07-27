'''
20200717	jlhung	v1.0
'''

P = {"A":10, "J":18, "S":26,
     "B":11, "K":19, "T":27, 
     "C":12, "L":20, "U":28, 
     "D":13, "M":21, "V":29, 
     "E":14, "N":22, "W":32, 
     "F":15, "O":35, "X":30, 
     "G":16, "P":23, "Y":31, 
     "H":17, "Q":24, "Z":33, 
     "I":34, "R":25 }

while True:
    try:
        n = input()        
        total = 0
        
        #處理英文 轉ASCII處理
        total = P[n[0]] // 10 + P[n[0]] % 10 * 9

        #處理中間8碼
        c = 8
        for t in n[1:9]:
            total += int(t) * c
            c -= 1
        
        #處理尾碼
        total += int(n[9])

        if total % 10 == 0:
            print("real")
        else:
            print("fake")
        
    except(EOFError):
        break