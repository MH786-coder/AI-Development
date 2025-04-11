import numpy as n
import pandas as p
import traceback

students = ['mohamed','naveen','mazeeth','azim','hasan','lakshmi']
subjects = ['English','Math','Computer']

marks = n.random.randint(0,100,size=(6,3))
data = p.DataFrame(marks,columns=subjects,index=students)

data['Marks'] = data.sum(axis=1)
data['Percentage'] = data[subjects].mean(axis=1).astype(int)

def grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 75 and percentage <= 89:
        return 'B'
    elif percentage >= 50 and percentage <= 74:
        return 'C'
    else:
        return 'D'
    
data['Grade'] = data['Percentage'].apply(grade)

try:
    data.to_csv('datas.csv',index=False)
    print('Data uploaded successfully')
except Exception as error:
    traceback.print_exception(error)