'''
20200728    v1.0    jlhung  轉成小寫處理 單數字母只能一個
'''

while True:
    try:
        n = input()
        
        t = [0 for i in range(26)]
        for c in n:
            if c.isalpha():
                t[ord(c.lower())-97] += 1    
        
        if sum(c%2 for c in t) <= 1:
            print("yes !")
        else:
            print("no...")
               
    except(EOFError):
        break