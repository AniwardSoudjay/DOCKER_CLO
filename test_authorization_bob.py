#test_authorization_bob.py
import os
import requests

s = requests.Session()

# définition de l'adresse de l'API
api_address = os.environ.get('api_name')

# définition de la phrase de Bob
bob_sentence = os.environ.get('bob_sentence_env')

# port pour l'API
api_port = 8000

# requête sur v1/sentiment
r_v1 = s.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'bob',
        'password': 'builder',
        'sentence': '{sentence}'.format(sentence=bob_sentence)
    }
)

output_v1 = '''
============================
    Authorization test
============================

request done at "/v1/sentiment"
| username="bob"
| password="builder"
| sentence="{sentence}"

expected result = 200
actual restult = {status_code}

==>  {test_status}

'''

# statut de la requête
status_code_v1 = r_v1.status_code

# affichage des résultats
if status_code_v1 == 200:
    test_status_v1 = 'SUCCESS'
else:
    test_status_v1 = 'FAILURE'
output_v1 = output_v1.format(sentence=bob_sentence, status_code=status_code_v1, test_status=test_status_v1)
print(output_v1)

# impression dans un fichier
if os.environ.get('LOG') == '1':
    with open('../my_log/api_test.log', 'a+') as file:
        file.write(output_v1)


#########################
        
# requête sur v2/sentiment
r_v2 = s.get(
    url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
    params= {
        'username': 'bob',
        'password': 'builder',
        'sentence': '{sentence}'.format(sentence=bob_sentence)
    }
)

output_v2 = '''
============================
    Authorization test
============================

request done at "/v2/sentiment"
| username="bob"
| password="builder"
| sentence="{sentence}"

expected result = 403
actual restult = {status_code}

==>  {test_status}

'''

# statut de la requête
status_code_v2 = r_v2.status_code

# affichage des résultats
if status_code_v2 == 200:
    test_status_v2 = 'SUCCESS'
else:
    test_status_v2 = 'FAILURE'
output_v2 = output_v2.format(sentence=bob_sentence, status_code=status_code_v2, test_status=test_status_v2)
print(output_v2)

# impression dans un fichier
if os.environ.get('LOG') == '1':
    with open('/my_log/api_test.log', 'a+') as file:
        file.write(output_v2)