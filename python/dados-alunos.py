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
from pprint import pprint

MATRICULA = '20171148060024'
TOKEN = 'uqrHAd6bFe66aRVQjDrFsa3xlEtqumFue77WLbIit6DhMoyosxpvG7B1DtAcJyh8'
AUTHORIZATION = 'Basic MjAxNzExNDgwNjAwMjQ6aWZybi4yMTAyODI='

req = Request('https://suap.ifrn.edu.br/api/v2/edu/alunos/{}/'.format(MATRICULA))
req.add_header('Accept', 'application/json')
req.add_header('X-CSRFToken', TOKEN)
req.add_header('Authorization', AUTHORIZATION)

resposta = urlopen(req)
dados_byte = resposta.read()
dados_txt = dados_byte.decode('utf-8')
dados = json.loads(dados_txt)

pprint(dados)
