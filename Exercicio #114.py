"""
Crie um código em Python que teste se o site Pudim está acessivel pelo computador usado
"""

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu erro')
else:
    print('Deu certo')
