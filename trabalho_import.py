import csv
import trabalho


arquivo = open(r"D:\Arquivos Luiz\Documents\trabalho senac\trabalho\US_births_2000-2014_SSA.csv")
birth = list(csv.DictReader(arquivo))

dois_mil = trabalho.total_nascimento_doismil(birth)
print(dois_mil)

doismil_um = trabalho.total_nascimento_doismil_um(birth)
print(doismil_um)

doismil_dois = trabalho.total_nascimento_doismil_dois(birth)
print(doismil_dois)

doismil_tres = trabalho.total_nascimento_doismil_tres(birth)
print(doismil_tres)

doismil_quatro = trabalho.total_nascimento_doismil_quatro(birth)
print(doismil_quatro)

doismil_cinco = trabalho.total_nascimento_doismil_cinco(birth)
print(doismil_cinco)

doismil_seis = trabalho.total_nascimento_doismil_seis(birth)
print(doismil_seis)

doismil_sete = trabalho.total_nascimento_doismil_sete(birth)
print(doismil_sete)

doismil_oito = trabalho.total_nascimento_doismil_oito(birth)
print(doismil_oito)

doismil_nove = trabalho.total_nascimento_doismil_nove(birth)
print(doismil_nove)

doismil_dez = trabalho.total_nascimento_doismil_dez(birth)
print(doismil_dez)

doismil_onze = trabalho.total_nascimento_doismil_onze(birth)
print(doismil_onze)

doismil_doze = trabalho.total_nascimento_doismil_doze(birth)
print(doismil_doze)

doismil_treze = trabalho.total_nascimento_doismil_treze(birth)
print(doismil_treze)

doismil_quatorze =trabalho.total_nascimento_doismil_quatorze(birth)
print(doismil_quatorze)

todos_nascimentos_anos = trabalho.todos_nascimentos(birth)

import matplotlib.pyplot as plt

y = [dois_mil,doismil_um,doismil_dois,doismil_tres,doismil_quatro,doismil_cinco,doismil_seis,doismil_sete,doismil_oito,doismil_nove,doismil_dez,doismil_onze,doismil_doze,doismil_treze,doismil_quatorze]
x = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]

plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.xlabel('Ano')
plt.ylabel('Nascimentos')
plt.title('Gráfico de Linha')
plt.grid(True)
plt.show()

# Ano de mais nascimento: 2007 com 4380784 
# Ano de menos nascimento: 2013 com 3973337

nascimento_durante_semana = trabalho.nascimento_durante_semana(birth)
print(nascimento_durante_semana)

nascimento_fim_semana = trabalho.nascimento_fim_semana(birth)
print(nascimento_fim_semana)

categorias = ['Segunda-feira à Quinta-feira', 'Sexta à Domingo']
valores = [nascimento_durante_semana, nascimento_fim_semana]

plt.bar(categorias, valores)
plt.xlabel('Dias da semana')
plt.ylabel('Nascimentos')
plt.title('Gráfico de Barras')
plt.show()


import pandas as pd
df= pd.read_csv(r"D:\Arquivos Luiz\Documents\trabalho senac\trabalho\US_births_2000-2014_SSA.csv")


tabela_maior = trabalho.achar_maior_valor_tabela(df)
print(tabela_maior)

tabela_menor = trabalho.achar_menor_valor_tabela(df)
print(tabela_menor)

categoria = ['Maior nascimento por dia', 'Menor nascimento por dia']
valore = [tabela_maior, tabela_menor]

plt.bar(categoria, valore)
plt.xlabel('Por dia')
plt.ylabel('Nascimentos')
plt.title('Gráfico de Barras')
plt.show()

informacao_mais_nascimento = trabalho.dia_mais_nascimento(birth) 
print(informacao_mais_nascimento)

informacao_menos_nascimento = trabalho.dia_menor_nascimento(birth)
print(informacao_menos_nascimento)

domingo_onze_anos = trabalho.domingo_anos(birth)
print(domingo_onze_anos)

segunda_onze_anos = trabalho.segundas_anos(birth)
print(segunda_onze_anos)

terca_onze_anos = trabalho.terça_anos(birth)
print(terca_onze_anos)

quarta_onze_anos = trabalho.quarta_anos(birth)
print(quarta_onze_anos)

quinta_onze_anos = trabalho.quinta_anos(birth)
print(quinta_onze_anos)

sexta_onze_anos = trabalho.sexta_anos(birth)
print(sexta_onze_anos)

sabado_onze_anos = trabalho.sabado_anos(birth)
print(sabado_onze_anos)

x = ['Domingo', 'Segunda-feira',' Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sábado']
y = [domingo_onze_anos,segunda_onze_anos,terca_onze_anos,quarta_onze_anos,quinta_onze_anos,sexta_onze_anos,sabado_onze_anos]

plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.xlabel('Dias da semana')
plt.ylabel('Quantidade de dias')
plt.title('Gráfico de Linha')
plt.grid(True)
plt.show()


janeiro = trabalho.janeiro_anos(birth)
print(janeiro)

fevereiro = trabalho.fevereiro_anos(birth)
print(fevereiro)

marco = trabalho.marco_anos(birth)
print(marco)

abril = trabalho.abril_anos(birth)
print(abril)

maio = trabalho.maio_anos(birth)
print(maio)

junho = trabalho.junho_anos(birth)
print(junho)

julho = trabalho.julho_anos(birth)
print(julho)

agosto = trabalho.agosto_anos(birth)
print(agosto)

setembro = trabalho.setembro_anos(birth)
print(setembro)

outubro = trabalho.outubro_anos(birth)
print(outubro)

novembro = trabalho.novembro_anos(birth)
print(novembro)

dezembro = trabalho.dezembro_anos(birth)
print(dezembro)

catego = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
valo = [janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro]

plt.bar(catego, valo)
plt.xlabel('Meses')
plt.ylabel('Nascimentos')
plt.title('Gráfico de Barras')
plt.show()

# mes que mais houve nascimentos: Agosto: 5540170
# mes que menos houve nascimentos: Fevereiro: 4725693

segunda = trabalho.segunda_feira_anos(birth)
print(segunda)

terça = trabalho.terça_feira_anos(birth)
print(terça)

quarta = trabalho.quartas_feira_anos(birth)
print(quarta)

quinta = trabalho.quintas_feira_anos(birth)
print(quinta)

sexta = trabalho.sextas_feira_anos(birth)
print(sexta)

sabado = trabalho.sabados_feira_anos(birth)
print(sabado)

domingo = trabalho.domingos_feira_anos(birth)
print(domingo)

todos_anos = trabalho.todos_nascimentos_numero(birth)

resultado = (domingo / todos_anos) * 100
print(resultado)

resultado2 = (segunda / todos_anos) * 100
print(resultado2)

resultado3 = (terça / todos_anos) * 100
print(resultado3)

resultado4 = (quarta / todos_anos) * 100
print(resultado4)

resultado5 = (quinta / todos_anos) * 100
print(resultado5)

resultado6 = (sexta / todos_anos) * 100
print(resultado6)

resultado7 = (sabado / todos_anos) * 100
print(resultado7)

categoria_5 = ["segunda feira", "terça feira", "quarta feira", "quinta feira", "sexta feira", "sabado", "domingo"]
valores_5 = [resultado, resultado2, resultado3, resultado4, resultado5, resultado6, resultado7]

plt.bar(categoria_5, valores_5)
plt.xlabel('dias da semana')
plt.ylabel('Nascimentos')
plt.title('Gráfico de Barras')
plt.show()

#o dia que da semana que mais nasceu pessoas foi na terça feira
#o dia que da semana que menos nasceu pessoas foi no domingo

"""
A partir desse momento usaremos outras fontes de dados com outros links que sera anexado ao trabalho.
"""
arquivo_2 = open(r"D:\Arquivos Luiz\Documents\trabalho senac\trabalho\NCHS_-_Leading_Causes_of_Death__United_States.csv")
arquivo_3 = open(r"D:\Arquivos Luiz\Documents\trabalho senac\trabalho\gun_deaths_us_1999_2019.csv")

pop = list(csv.DictReader(arquivo_3))
deaths = list(csv.DictReader(arquivo_2))

total_pop = trabalho.total_populacao(pop)
print(total_pop)

mortes_anos = trabalho.total_mortes(deaths)
print(mortes_anos)

categoria_7 = ["População", "Nascimentos", "Mortes"]
valores_7 = [total_pop ,todos_anos, mortes_anos]

plt.plot(categoria_7, valores_7, marker='o', linestyle='-', color='b')
plt.xlabel("Comparação")
plt.ylabel("Valores")
plt.title('Gráfico de Linha')
plt.grid(True)
plt.show()

suicidio_mortes = trabalho.mortes_suicidio(deaths)
print(suicidio_mortes)

mortes_outras = trabalho.outras_mortes(deaths)
print(mortes_outras)

categoria_9 = ["Suicidio", "Outras mortes"]
valores_9 = [mortes_outras, suicidio_mortes]

plt.bar(categoria_9, valores_9)
plt.xlabel('Suicidio e outras mortes')
plt.ylabel('Quantidade')
plt.title('Gráfico de Barras')
plt.show()

