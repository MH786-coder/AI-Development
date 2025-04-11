import pandas

data1 = {
    'names':['1','2','3']
}

data2 = {
    'names2':['4','5','6']
}

getd1 = pandas.DataFrame(data1)
# print(getd1)
getd2 = pandas.DataFrame(data2)
# print(getd2)

print(pandas.concat([getd1,getd2],axis=1))