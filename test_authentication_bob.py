#test_authentication_bob.py
import os
import requests

s = requests.Session()

# définition de l'adresse de l'API
api_address = os.environ.get('api_name')
# port pour l'API
api_port = 8000

# requête
r = s.get(
    url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
    params= {
        'username': 'bob',
        'password': 'builder'
    }
)

output = '''
============================
    Authentication test
============================
request done at "/permissions"
| username="bob"
| password="builder"
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

# impression 
if os.environ.get('LOG') == '1':
    log_path = '/my_log/api_test.log'
    with open(log_path, 'a+') as file:
        file.write(output)