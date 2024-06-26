#test_authentication_alice.py
import os
import requests

s = requests.Session()

# définition de l'adresse de l'API
api_address = os.environ.get('api_name')
# port de l'API
api_port = 8000

# requête
r = requests.get(
    url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
    params= {
        'username': 'alice',
        'password': 'wonderland'
    }
)

output = '''
============================
    Authentication test
============================
request done at "/permissions"
| username="alice"
| password="wonderland"
expected result = 200
actual restult = {status_code}
==>  {test_status}
'''


# statut de la requête
status_code = r.status_code

# affichage résultats
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'
output = output.format(status_code=status_code, test_status=test_status)
print(output)
print(os.environ.get('LOG'))

# impression 
if os.environ.get('LOG') == '1':
    log_path = '/my_log/api_test.log'
    with open(log_path, 'a+') as file:
        file.write(output)