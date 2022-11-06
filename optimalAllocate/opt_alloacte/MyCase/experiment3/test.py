sot = [((1, 2), 5), ((1, 1), 8), ((2, 4), 5)]
print(sot)
sot.pop(1)
sot.remove(((1, 2), 5))

dic = {(1, 2): 4}
dic[(1, 1)] = 2
print(dic[1, 1])
print(dic)
dic.pop((1,1))
print(dic)