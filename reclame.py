def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1-korting)
    aanbieding_tekst = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs:.2f} euro voor {nieuwe_prijs:.2f} euro."
    return aanbieding_tekst

smaak = "aardbei"
prijs = 4
korting = 0.1

print(aanbieding_1(smaak, prijs, korting))