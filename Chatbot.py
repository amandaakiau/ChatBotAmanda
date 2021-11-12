import json
import sys
import os
import subprocess as s

class Chatbot():
    def __init__(self, nome):
        try:
            memoria = open(nome+'.json','r')
        except FileNotFoundError:
            memoria = open(nome+'.json','w')
            memoria.write('{"oi": "Olá, qual é o seu nome?"}')
            #memoria.write('["Isadora","Victor"]')
            memoria.close()
            memoria = open(nome+'.json','r')

        self.nome = nome
        self.frases = json.load(memoria)
        #self.conhecidos = json.load(memoria)
        memoria.close()
        self.historico = []
        #self.frases = {'oi': 'Olá, qual é o seu nome?', 'tchau': 'tchau'}

    def escuta(self):
        frase = input('>: ')
        frase = frase.lower()
        frase = frase.replace('é','eh')
        return frase

    def pensa(self, frase):
        if frase in self.frases:
            return self.frases[frase]

        if frase == 'aprende':
            chave = input('Digite a frase: ')
            resp = input('Digite a resposta: ')
            self.frases[chave] = resp
            memoria = open(self.nome + '.json', 'w')
            json.dump(self.frases, memoria)
            memoria.close()
            return 'Aprendido'

        if self.historico[-1] == 'Olá, qual é o seu nome?':
            nome = self.pegaNome(frase)
            frase = self.respondeNome(nome)
            return frase
        try:
            resp = str(eval(frase))
            return resp
# a função EVAL realiza algumas operações matemáticas etc:q
        except:
            pass
        return 'Não entendi'

    def pegaNome(self,nome):
        if 'o meu nome eh' in nome:
            nome = nome[14:]
        nome = nome.title()
        return nome

    def respondeNome(self,nome):
        if nome == "Amanda":
            frase = 'Eaiii '
        else:
            frase = 'Muito prazer '

        return frase + nome

    def fala(self, frase):
        if 'executa ' in frase:
            plataforma = sys.platform
    #identificar qual sistema operacional
            comando = frase.replace('executa ','')
            if 'win' in plataforma:
                os.startfile(comando)
            if 'linux' in plataforma:
                try:
                    s.Popen(comando)
                except FileNotFoundError:
                    s.Popen(['xdg-open', comando])
        else:
            print(frase)
        self.historico.append(frase)

