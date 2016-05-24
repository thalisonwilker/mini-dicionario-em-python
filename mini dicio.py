# -*- coding: latin1 -*-
from bs4 import BeautifulSoup
from urllib import urlopen
from Tkinter import *

janela = Tk()

def abrir(word):
    url = 'http://www.dicio.com.br/'
    url += word
    try:
        resp = urlopen(url)
        text = resp.read()
        sopa = BeautifulSoup(text)
        sig = sopa.find_all(id='significado')
        global janela
        t = ''
        janela.title("Significado de "+word)
        org(sig)
    except Exception, e:
        import sys
        sys.stderr.write("Ops...\n%s " % (str(e)))        
        
def org(string):
    sig = ''
    string = str(string)
    param = string.split(">")
    param = param[1:]
    s = ''
    for i in param:
        s += i
    param = s.split("<br /")
    s =''
    for i in param:
        s +=i
    param = s.split("</p]")
    for i in param:
        sig += i.decode('utf-8')
    org2(sig)

def org2(text):
    i = 1
    pronto = ''
    text = text.split(' ')
    for k in text:
        if i == 8:
            pronto += '\n'
            i = 0
        pronto += ' '+k+' '
        i = i + 1
    resultado['text'] = pronto
        
    
def get():
    abrir(entrada.get())

resultado = Label(janela)
resultado['font'] = 'Consolas'
buscar = Button(janela, widt = 6, text = 'Buscar', command = get)
buscar['font'] = 'Consolas'
entrada = Entry(janela)
entrada['font'] = 'Consolas'
entrada.pack(side = TOP )
buscar.pack(side = TOP)
resultado.pack(side = TOP)


janela.mainloop()
