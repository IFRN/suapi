#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
O token/ficha e a autorização devem ser obtidos, separadamente, em

    https://suap.ifrn.edu.br/api/docs/
    
No canto superior direito há os botões:

* Django login (necessário para o token);
* e Authorize (necessário para obter a autorização).
'''

from urllib.request import Request, urlopen
import json

MATRICULA = ''
TOKEN = ''
AUTHORIZATION = ''

req = Request('https://suap.ifrn.edu.br/api/v2/edu/alunos/{}/'.format(MATRICULA))
req.add_header('Accept', 'application/json')
req.add_header('X-CSRFToken', TOKEN)
req.add_header('Authorization', AUTHORIZATION)

dados_byte = urlopen(req).read()
dados_txt = dados_byte.decode('utf-8')
print(dados_txt)
