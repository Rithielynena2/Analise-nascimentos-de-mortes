# grafico total de nascimentos 2000 - 2014


def total_nascimento_doismil(birth:list):
    doismil = 0

    for b in birth:
        if int(b["year"]) == 2000:
            doismil = doismil+ int(b["births"])
    return doismil

def total_nascimento_doismil_um(birth:list):
    doismil_um = 0

    for b in birth:
        if int(b["year"]) == 2001:
            doismil_um += int(b["births"])
    return doismil_um

def total_nascimento_doismil_dois(birth:list):
    doismil_dois = 0

    for b in birth:
        if int(b["year"]) == 2002:
            doismil_dois += int(b["births"])
    return doismil_dois

def total_nascimento_doismil_tres(birth:list):
    doismil_tres = 0
    for b in birth:
        if int(b["year"]) == 2003:
            doismil_tres += int(b["births"])
    return doismil_tres

  
def total_nascimento_doismil_quatro(birth:list):
    doismil_quatro = 0
    for b in birth:
        if int(b["year"]) == 2004:
            doismil_quatro += int(b["births"])
    return doismil_quatro

def total_nascimento_doismil_cinco(birth:list):
    doismil_cinco = 0
    for b in birth:
        if int(b["year"]) == 2005:
            doismil_cinco += int(b["births"])
    return doismil_cinco

def total_nascimento_doismil_seis(birth:list):
    doismil_seis = 0
    for b in birth:
        if int(b["year"]) == 2006:
            doismil_seis += int(b["births"])
    return doismil_seis

def total_nascimento_doismil_sete(birth:list):
    doismil_sete = 0
    for b in birth:
        if int(b["year"]) == 2007:
            doismil_sete += int(b["births"])
    return doismil_sete

def total_nascimento_doismil_oito(birth:list):
    doismil_oito = 0
    for b in birth:
        if int(b["year"]) == 2008:
            doismil_oito += int(b["births"])
    return doismil_oito

def total_nascimento_doismil_nove(birth:list):
    doismil_nove = 0
    for b in birth:
        if int(b["year"]) == 2009:
            doismil_nove += int(b["births"])
    return doismil_nove

def total_nascimento_doismil_dez(birth:list):
    doismil_dez = 0
    for b in birth:
        if int(b["year"]) == 2010:
            doismil_dez += int(b["births"])
    return doismil_dez

def total_nascimento_doismil_onze(birth:list):
    doismil_onze = 0
    for b in birth:
        if int(b["year"]) == 2011:
            doismil_onze += int(b["births"])
    return doismil_onze

def total_nascimento_doismil_doze(birth:list):
    doismil_doze = 0
    for b in birth:
        if int(b["year"]) == 2012:
            doismil_doze += int(b["births"])
    return doismil_doze

def total_nascimento_doismil_treze(birth:list):
    doismil_treze = 0
    for b in birth:
        if int(b["year"]) == 2013:
            doismil_treze += int(b["births"])
    return doismil_treze

def total_nascimento_doismil_quatorze(birth:list):
    doismil_quatorze = 0
    for b in birth:
        if int(b["year"]) == 2014:
            doismil_quatorze += int(b["births"])
    return doismil_quatorze






#quantas pessoas no periodo de 14 anos durante a semana e
# e fim de semana


def nascimento_durante_semana(birth:list):
    nascimentosemana = 0
    for b in birth:
        if int(b["day_of_week"]) >= 2 and int(b["day_of_week"]) <= 5:
            nascimentosemana += int(b["births"])
    return nascimentosemana

def nascimento_fim_semana(birth:list):
    nascimentofimsemana = 0
    for b in birth:
        if int(b["day_of_week"]) >= 6 or int(b["day_of_week"]) == 7 or int(b["day_of_week"]) ==1:
            nascimentofimsemana += int(b["births"])
    return nascimentofimsemana



# total de nascimentos nos 14 anos juntos 
#somar 1 coluna nascimento



import pandas as pd


df= pd.read_csv(r"D:\Arquivos Luiz\Documents\trabalho senac\trabalho\US_births_2000-2014_SSA.csv")


def dia_mais_nascimento(birth:list):
    mais_nascimento = 0
    dia = ""
    mes = ""
    ano = ""
    dia_semana = ""

    for b in birth:
        if int(b["births"]) > mais_nascimento:
            mais_nascimento = int(b["births"])
            dia = int(b["date_of_month"])
            mes = int(b["month"])
            ano = int(b["year"])
            dia_semana = int (b["day_of_week"])
    return {
        "Dia": dia,
        "Mes": mes,
        "Ano": ano,
        "Dia_semana": dia_semana
    }


def dia_menor_nascimento(birth:list):
    menor_nascimento = 12000
    dia = ""
    mes = ""
    ano = ""
    dia_semana = ""
    
    for b in birth:
        if int(b["births"]) < menor_nascimento:
            menor_nascimento = int(b["births"])
            dia = int(b["date_of_month"])
            mes = int(b["month"])
            ano = int(b["year"])
            dia_semana = int (b["day_of_week"])
    return {
        "Dia": dia,
        "Mes": mes,
        "Ano": ano,
        "Dia_semana": dia_semana
    }
    
        




def achar_menor_valor_tabela(df):
    menor_nascimento = df['births'].min()
    return menor_nascimento

def achar_maior_valor_tabela(df):
    maior_nascimento = df['births'].max()
    return maior_nascimento

# graficos nascimento janeiro (1) a junho (2)
#grafico nascimento de julho a dezembro


def todos_nascimentos(birth:list):
    todos_nascimentos= 0
    for b in birth:
        todos_nascimentos += int(b["births"])
    return print(f' O total de nascimento de todos os anos é de {todos_nascimentos}')


def domingo_anos(birth:list):
    domingo= 0
    for b in birth:
        if int(b["year"]) >= 2000 and int(b["year"]) <=2011:
            if int(b["day_of_week"]) == 1:
                domingo +=1
    return domingo

def segundas_anos(birth:list):
    segunda = 0
    for b in birth:
        if int(b["year"]) >= 2000 and int(b["year"]) <=2011:
            if int(b["day_of_week"]) == 2:
                segunda +=1
    return segunda

def terça_anos(birth:list):
    terca= 0
    for b in birth:
        if int(b["year"]) >= 2000 and int(b["year"]) <=2011:
            if int(b["day_of_week"]) == 3:
                terca +=1
    return terca
def quarta_anos(birth:list):
    quarta= 0
    for b in birth:
        if int(b["year"]) >= 2000 and int(b["year"]) <=2011:
            if int(b["day_of_week"]) == 4:
                quarta +=1
    return quarta

def quinta_anos(birth:list):
    quinta= 0
    for b in birth:
        if int(b["year"]) >= 2000 and int(b["year"]) <=2011:
            if int(b["day_of_week"]) == 5:
                quinta +=1
    return quinta

def sexta_anos(birth:list):
    sexta = 0
    for b in birth:
        if int(b["year"]) >= 2000 and int(b["year"]) <=2011:
            if int(b["day_of_week"]) == 6:
                sexta +=1
    return sexta

def sabado_anos(birth:list):
    sabado = 0
    for b in birth:
        if int(b["year"]) >= 2000 and int(b["year"]) <=2011:
            if int(b["day_of_week"]) == 7:
                sabado +=1
    return sabado
                

# janeiro de todos os anos

def janeiro_anos(birth:list):
    janeiro = 0 
    for b in birth:
        if int(b["month"]) == 1:
            janeiro += int(b["births"])
    return janeiro

def fevereiro_anos(birth:list):
    fevereiro = 0
    for b in birth:
        if int (b["month"]) == 2:
            fevereiro += int(b["births"])
    return fevereiro

def marco_anos(birth:list):
    marco = 0 
    for b in birth:
        if int(b["month"]) == 3:
            marco += int(b["births"])
    return marco

def abril_anos(birth:list):
    abril = 0
    for b in birth:
        if int(b["month"]) == 4:
            abril += int(b["births"])
    return abril

def maio_anos(birth:list):
    maio = 0
    for b in birth:
        if int(b["month"]) == 5:
            maio += int(b["births"])
    return maio 

def junho_anos(birth:list):
    junho = 0
    for b in birth:
        if int(b["month"]) == 6:
            junho += int(b["births"])
    return junho

def julho_anos(birth:list):
    julho = 0
    for b in birth:
        if int(b["month"]) == 7:
            julho += int(b["births"])
    return julho

def agosto_anos(birth:list):
    agosto = 0
    for b in birth:
        if int(b["month"]) == 8:
            agosto += int(b["births"])
    return agosto

def setembro_anos(birth:list):
    setembro = 0
    for b in birth:
        if int(b["month"]) == 9:
            setembro += int(b["births"])
    return setembro

def outubro_anos(birth:list):
    outubro = 0
    for b in birth:
        if int(b["month"]) == 10:
            outubro += int(b["births"])
    return outubro

def novembro_anos(birth:list):
    novembro = 0
    for b in birth:
        if int(b["month"]) == 11:
            novembro += int(b["births"])
    return novembro 

def dezembro_anos(birth:list):
    dezembro = 0
    for b in birth:
        if int(b["month"]) == 12:
            dezembro += int(b["births"])
    return dezembro






def todos_nascimentos_numero(birth:list):
    todos_nascimentos= 0
    for b in birth:
        todos_nascimentos += int(b["births"])
    return todos_nascimentos

def segunda_feira_anos(birth:list):
    segundas = 0
    for b in birth:
        if int(b["day_of_week"]) == 2:
            segundas += int(b["births"])
    return segundas

def terça_feira_anos(birth:list):
    terças = 0
    for b in birth:
        if int(b["day_of_week"]) == 3:
            terças += int(b["births"])
    return terças

def quartas_feira_anos(birth:list):
    quartas = 0
    for b in birth:
        if int(b["day_of_week"]) == 4:
            quartas += int(b["births"])
    return quartas

def quintas_feira_anos(birth:list):
    quintas = 0
    for b in birth:
        if int(b["day_of_week"]) == 5:
            quintas += int(b["births"])
    return quintas

def sextas_feira_anos(birth:list):
    sextas = 0
    for b in birth:
        if int(b["day_of_week"]) == 6:
            sextas += int(b["births"])
    return sextas

def sabados_feira_anos(birth:list):
    sabados = 0
    for b in birth:
        if int(b["day_of_week"]) == 7:
            sabados += int(b["births"])
    return sabados

def domingos_feira_anos(birth:list):
    domingos = 0
    for b in birth:
        if int(b["day_of_week"]) == 1:
            domingos += int(b["births"])
    return domingos



def total_populacao(pop:list):
    populacao = 0
    for p in pop:
        populacao += int(p["Population"])
    return populacao



def todos_nascimentos_numero(birth:list):
    todos_nascimentos= 0
    for b in birth:
        todos_nascimentos += int(b["births"])
    return todos_nascimentos

def total_mortes(deaths:list):
    mortes = 0
    for d in deaths:
        if int(d["ï»¿Year"]) >= 2000 and int(d["ï»¿Year"]) <= 2014:
            mortes += float(d["Deaths"].replace(",", "."))
    return mortes


def mortes_suicidio(deaths:list):
    mortes2 = 0
    for d in deaths:
        if int(d["ï»¿Year"]) >= 2000 and int(d["ï»¿Year"]) <= 2014:
            if d["Cause Name"] == "Suicide":
                mortes2 += float(d["Deaths"].replace(",", "."))
    return mortes2

def outras_mortes(deaths:list):
    mortes3 = 0
    for d in deaths:
        if int(d["ï»¿Year"]) == 2000 and int(d["ï»¿Year"]) <= 2014:
            if (d["Cause Name"]) != "Suicide":
                mortes3 += float(d["Deaths"].replace(",", "."))
    return mortes3
        
