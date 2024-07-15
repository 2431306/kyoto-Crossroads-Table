import math

tozai = ["三条", "四条", "五条"]
nanboku = ["堀川", "烏丸", "河原町"]
for i in tozai:
    for j in nanboku:
        cross = i+j
        print(tozai.index(i),nanboku.index(j),cross)
        


tozai = ["三条", "四条", "五条"]
nanboku = ["堀川", "烏丸", "河原町"]
for i in range(len(tozai)):
    for j in range(len(nanboku)):
        cross = tozai[i]+nanboku[j]
        print(i,j,cross)


tozai = [ '三条', '四条', '五条' ]
namboku = [ '堀川', '烏丸', '河原町' ]
cross = [['']*3]*3
for i in range(len(tozai)):
    for j in range(len(namboku)):
        cross[i][j] = tozai[i]+namboku[j]
        print(i,j, cross[i][j])