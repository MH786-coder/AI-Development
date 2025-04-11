import pandas as p

datafile = p.read_csv('titanic.csv')

while True:
    pass_id = int(input('Enter passanger id : '))

    if pass_id > 891:
        print(f'No passengers found at the id {pass_id}')
        continue
    else:
        print('\n',datafile[datafile['PassengerId'] == pass_id].to_string(index=False))
