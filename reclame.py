from algemene_functies import mijn_functie2

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1-korting)
    aanbieding_tekst = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro."
    return aanbieding_tekst

smaak = "aardbei"
prijs = 4
korting = 0.1

print(aanbieding_1(smaak, prijs, korting))

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

inkomsten = [220, 430, 125, 150, 205, 90, 345]
btw = 0.09
resultaat = inkomsten_totaal(inkomsten, btw)
print(resultaat)


def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return [laagste, hoogste]

resultaat2 = (laag_en_hoog(inkomsten))
print(resultaat2)

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal_dagen = len(mijn_lijst)
    gemiddelde_inkomsten = totaal / aantal_dagen
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten:.2f} euro"

resultaat3 = gemiddelde(inkomsten)
print(resultaat3)

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

invoer_lijst = [10, 5, 3, 2, 1, 2, 9]

resultaat4 = meervoudig(invoer_lijst)
print(resultaat4)

def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    uitvoer = mijn_functie2(korte_lijst[0], korte_lijst[1])
    return uitvoer