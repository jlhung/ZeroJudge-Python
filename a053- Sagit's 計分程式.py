'''
20200724    v1.0    jlhung  
'''

score = [0 for i in range(101)]
for i in range(101):
    if i <= 10:
        score[i] = i * 6
    elif i >= 11 and i <= 20:
        score[i] = 60 + (i - 10) * 2
    elif i >= 21 and i <= 40:
        score[i] = 80 + (i - 20)
    else:
        score[i] = 100

while True:
    try:
        print(score[int(input())])

    except(EOFError):
        break