from sqlalchemy import create_engine
import pandas as pd
from collections import Counter



engine = create_engine('sqlite://', echo = False)
df = pd.read_excel('Aliments.xlsx')
df.to_sql('aliments', engine, if_exists='replace', index=False)

dg = pd.DataFrame(columns=['Nom'])
df = pd.read_excel('Sondage.xlsx')
df.to_sql('sondage', engine, if_exists='replace', index=False)
requete = engine.execute("select * from sondage")
final2 = pd.DataFrame(requete)

def getEnergie(code):
    score = 0
    requete = engine.execute("select `Energie, Règlement UE N° 1169/2011 (kJ/100 g)` from aliments where alim_code = :code1", code)
    final = pd.DataFrame(requete)
    tmp = final.values[0][0]
    if tmp != '-' and tmp!= 'traces':
        tab = tmp.split()
        if len(tab) > 1:
            tmp = tab[1]
        energie = float(tmp.replace(',', '.'))
        if energie > 3350:
            score = score + 10
        elif energie > 3015:
            score = score + 9
        elif energie > 2680:
            score = score + 8
        elif energie > 2345:
            score = score + 7
        elif energie > 2010:
            score = score + 6
        elif energie > 1675:
            score = score + 5
        elif energie > 1340:
            score = score + 4
        elif energie > 1005:
            score = score + 3
        elif energie > 670:
            score = score + 2
        elif energie > 335:
            score = score + 1
        return score
    return 0

def getSucre(code):
    score = 0
    requete = engine.execute("select `Sucres (g/100 g)` from aliments where alim_code = :code1", code)
    final = pd.DataFrame(requete)
    tmp = final.values[0][0]
    if tmp != '-' and tmp!= 'traces':
        tab = tmp.split()
        if len(tab) > 1:
            tmp = tab[1]
        sucre = float(tmp.replace(',', '.'))
        if sucre <= 0:
            score = score + 0
        elif sucre <= 1.5 :
            score = score + 1
        elif sucre <= 3 :
            score = score + 2
        elif sucre <= 4.5 :
            score = score + 3
        elif sucre <= 6 :
            score = score + 4
        elif sucre <= 7.5 :
            score = score + 5
        elif sucre <= 9 :
            score = score + 6
        elif sucre <= 10.5 :
            score = score + 7
        elif sucre <= 12 :
            score = score + 8
        elif sucre <= 13.5 :
            score = score + 9
        else:
            score = score + 10
        return score
    return 0

def getGraisse(code):
    score = 0
    requete = engine.execute("select `AG saturés (g/100 g)` from aliments where alim_code = :code1", code)
    final = pd.DataFrame(requete)
    tmp = final.values[0][0]
    if(tmp != '-' and tmp!='traces'):
        tab = tmp.split()
        if(len(tab) > 1):
            tmp = tab[1]
        graisse = float(tmp.replace(',', '.'))
        if graisse > 10 :
            score = score + 10
        elif graisse > 9 :
            score = score + 9
        elif graisse > 8 :
            score = score + 8
        elif graisse > 7 :
            score = score + 7
        elif graisse > 6 :
            score = score + 6
        elif graisse > 5 :
            score = score + 5
        elif graisse > 4 :
            score = score + 4
        elif graisse > 3 :
            score = score + 3
        elif graisse > 2 :
            score = score + 2
        elif graisse > 1 :
            score = score + 1
        return score
    return 0

def getSel(code):
    score = 0
    requete = engine.execute("select `Sel chlorure de sodium (g/100 g)` from aliments where alim_code = :code1", code)
    final = pd.DataFrame(requete)
    tmp = final.values[0][0]
    if(tmp != '-' and tmp!='traces'):
        tab = tmp.split()
        if(len(tab) > 1):
            tmp = tab[1]
        sodium = float(tmp.replace(',', '.'))
        if sodium > 0.9 :
            score = score + 10
        elif sodium > 0.810 :
            score = score + 9
        elif sodium > 0.720 :
            score = score + 8
        elif sodium > 0.630 :
            score = score + 7
        elif sodium > 0.540 :
            score = score + 6
        elif sodium > 0.450 :
            score = score + 5
        elif sodium > 0.360 :
            score = score + 4
        elif sodium > 0.270 :
            score = score + 3
        elif sodium > 0.180 :
            score = score + 2
        elif sodium > 0.090 :
            score = score + 1
        return score
    return 0

def getFibre(code):
    score = 0
    requete = engine.execute("select `Fibres alimentaires (g/100 g)` from aliments where alim_code = :code1", code)
    final = pd.DataFrame(requete)
    tmp = final.values[0][0]
    if(tmp != '-' and tmp!='traces'):
        tab = tmp.split()
        if(len(tab) > 1):
            tmp = tab[1]
        fibre = float(tmp.replace(',', '.'))
        if fibre > 3.5 :
            score = score + 5
        elif fibre > 2.8 :
            score = score + 4
        elif fibre > 2.1 :
            score = score + 3
        elif fibre > 1.4 :
            score = score + 2
        elif fibre > 0.7 :
            score = score + 1
        return score
    return 0

def getProteine(code):
    score = 0
    requete = engine.execute("select `Protéines, N x facteur de Jones (g/100 g)` from aliments where alim_code = :code1", code)
    final = pd.DataFrame(requete)
    tmp = final.values[0][0]
    if(tmp != '-' and tmp!='traces'):
        tab = tmp.split()
        if(len(tab) > 1):
            tmp = tab[1]
        proteine = float(tmp.replace(',', '.'))
        if proteine > 8 :
            score = score + 5
        elif proteine > 6.4 :
            score = score + 4
        elif proteine > 4.8 :
            score = score + 3
        elif proteine > 3.2 :
            score = score + 2
        elif proteine > 1.6 :
            score = score + 1
        return score
    return 0

def getSucreBoisson(code):
    score = 0
    requete = engine.execute("select `Sucres (g/100 g)` from aliments where alim_code = :code1", code)
    final = pd.DataFrame(requete)
    tmp = final.values[0][0]
    if(tmp != '-' and tmp!='traces'):
        tab = tmp.split()
        if(len(tab) > 1):
            tmp = tab[1]
        sucre = float(tmp.replace(',', '.'))
        if sucre > 45 :
            score = score + 10
        elif sucre > 40 :
            score = score + 9
        elif sucre > 36 :
            score = score + 8
        elif sucre > 31 :
            score = score + 7
        elif sucre > 27 :
            score = score + 6
        elif sucre > 22.5 :
            score = score + 5
        elif sucre > 18 :
            score = score + 4
        elif sucre > 13.5 :
            score = score + 3
        elif sucre > 9 :
            score = score + 2
        elif sucre > 4.5 :
            score = score + 1
        return score
    return 0

def getEnergieBoisson(code):
    score = 0
    requete = engine.execute("select `Energie, Règlement UE N° 1169/2011 (kJ/100 g)` from aliments where alim_code = :code1", code)
    final = pd.DataFrame(requete)
    tmp = final.values[0][0]
    if tmp != '-' and tmp!= 'traces':
        tab = tmp.split()
        if(len(tab) > 1):
            tmp = tab[1]
        energie = float(tmp.replace(',', '.'))
        if energie <= 0:
            score = score + 0
        elif energie <= 30 :
            score = score + 1
        elif energie <= 60 :
            score = score + 2
        elif energie <= 90 :
            score = score + 3
        elif energie <= 120 :
            score = score + 4
        elif energie <= 150 :
            score = score + 5
        elif energie <= 180 :
            score = score + 6
        elif energie <= 210 :
            score = score + 7
        elif energie <= 240 :
            score = score + 8
        elif energie <= 270 :
            score = score + 9
        else:
            score = score + 10
        return score

    return 0

# modif à faire pour passer du gramme à %
def getGraisseGraisse(code):
    score = 0
    requete = engine.execute("select `AG saturés (g/100 g)` from aliments where alim_code = :code1", code)
    final = pd.DataFrame(requete)
    tmp = final.values[0][0]
    if(tmp != '-' and tmp!='traces'):
        tab = tmp.split()
        if(len(tab) > 1):
            tmp = tab[1]
        graisse = float(tmp.replace(',', '.'))
        if graisse < 10:
            score = score + 0
        elif graisse < 16 :
            score = score + 1
        elif graisse < 22 :
            score = score + 2
        elif graisse < 28 :
            score = score + 3
        elif graisse < 34 :
            score = score + 4
        elif graisse < 40 :
            score = score + 5
        elif graisse < 46 :
            score = score + 6
        elif graisse < 52 :
            score = score + 7
        elif graisse < 58 :
            score = score + 8
        elif graisse < 64 :
            score = score + 9
        else:
            score = score + 10
        return score
    return 0

def nutriScore (code):
    requete = engine.execute("select `alim_grp_code` from aliments where alim_code = :code1", code)
    final = pd.DataFrame(requete)
    tmp = final.values[0][0]
    categorie = int(tmp)
    scoreBon = 0
    scoreMauvais = 0
    if categorie == 6:
        scoreMauvais+=getEnergieBoisson(code)
        scoreMauvais+=getSucreBoisson(code)
    else :
        scoreMauvais+=getEnergie(code)
        scoreMauvais+=getSucre(code)
    if categorie == 9:
        scoreMauvais+=getGraisseGraisse(code)
    else :
        scoreMauvais+=getGraisse(code)
    scoreMauvais+=getSel(code)
    scoreBon+=getFibre(code)
    scoreBon+=getProteine(code)
    return scoreMauvais - scoreBon

def trad(result):
    if result <= -1:
        return 'A'
    elif result <= 2:
        return 'B'
    elif result <= 10:
        return 'C'
    elif result <= 18:
        return 'D'
    else:
        return 'E'


def getListe(i):
    tab = []
    tab.append(final2.values[i][8])
    tab.append(final2.values[i][9])
    tab.append(final2.values[i][10])
    tab.append(final2.values[i][11])
    tab.append(final2.values[i][12])
    tab.append(final2.values[i][13])
    tab.append(final2.values[i][14])
    tab.append(final2.values[i][15])
    tab.append(final2.values[i][16])
    tab.append(final2.values[i][17])
    write(tab, i)

def write(tab, i):
    global dg
    nom = final2.values[i][1]
    nutriTab = []
    for i in range(len(tab)):
        nutriTab.append(nutriScore(tab[i]))

    data = {'Nom' : nom, 'Nutriscore' : trad(sum(nutriTab)/len(nutriTab))}
    dg = dg.append(data, ignore_index=True)
    tab.clear()
    nutriTab.clear()


for i in range(len(final2)):
    getListe(i)

letter_counts = Counter(dg['Nutriscore'])
figure = pd.DataFrame.from_dict(letter_counts, orient='index')
figure = figure.plot(xlabel='Note', ylabel='Nombre', kind="bar", title='Répartition des nutriscores', legend=False, color="green")
figure = figure.get_figure()
figure.savefig('hist.png')

dg.to_excel('Result.xlsx', index=False)