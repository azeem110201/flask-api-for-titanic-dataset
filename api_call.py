import requests

BASE_URL = 'http://127.0.0.1:1234/api?'

Pclass = str(input('Enter the class in which the person was:'))
age = str(input('Enter the age of the person:'))
sibsp = str(input('Enter the total number of family members that where with him:'))
fare = str(input('Enter the fare paid by that person:'))

url = BASE_URL + 'Pclass=' + Pclass + '&Age=' + age + '&SibSp=' + sibsp + '&Fare=' + fare

r = requests.get(url)

if r.status_code == 200:
    r = r.json()
    if r == 1:
        print('The person survived the titanic attack')
    else:
        print('Sorry,he/she is no more')    