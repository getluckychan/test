import requests
import os
import json

nameUser = input()  #ввод ника

def jprint(obj):
    # адекватно форматирует строки
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
def run_query(query):
    user = requests.get('https://api.github.com/users/{0}'.format(nameUser)) #вывод имени
    a = [user.json()] #создаю массив с json ибо вывести данные без него никак
    for name in a:
        jprint(name['name'])
        
query = """{name}"""
result = run_query(query)


def run_query1(query1):
    repos = requests.get('https://api.github.com/users/{0}/repos'.format(nameUser)) #вывод репрезиториев
    for repo in repos.json():
        if not repo['private']:
            jprint('- ' + repo['name'])
        else:
            jprint('private')
        
query1 = """{name}"""
result = run_query1(query1)