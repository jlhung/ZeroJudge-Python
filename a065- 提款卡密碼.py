'''
20200724    v1.0    jlhung  轉成ASCII處理 
'''

while True:
    try:
        n = input()
        
        pwd = ""
        for i in range(0, len(n)-1):
            pwd += str(abs(ord(n[i]) - ord(n[i+1])))    #取絕對值轉字串
        
        print(pwd)
        
    except(EOFError):
        break