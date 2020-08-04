'''
Created on 29-06-2020

@author: emendoca
'''

import urllib.request
from bs4 import BeautifulSoup
#import pandas as pd

URL = 'https://www.tripadvisor.cl/Restaurants-g187438-Malaga_Costa_del_Sol_Province_of_Malaga_Andalucia.html'
datos = urllib.request.urlopen(URL).read()

' imprime el texto completo '
#print (textourl)

soup = BeautifulSoup(datos,"lxml")

' metodo find, encuentra primer elemento'
' metodo get_text: solo el texto sin los tags'
#res=soup.find(class_="_15_ydu6b").get_text()

' metodo find_all, encuentra todos los elementos que cumplan la condicion'
' strip = True: elimina los espacios en blanco al principio y al final'
res = [i.get_text(strip=True) for i in soup.find_all(class_="_15_ydu6b")]
print(res)

#tags = soup('a')
#for tag in tags
#    print(tag.get('href'))
