import sys
cake = sys.argv[1]
price = 600 #jakýkoli korpus s krémem

#Menu ("help")
if cake=='help':
    print(f"""Vítejte v Cukrárně FUTURE SAILORS, kde si můžete objednat dort podle Vašeho na přání.
Parametry ve formátu: (Druh_dortu) (Korpus-Krém) (Počet_porcí) (Bezlepkový) (Počet svíček)
Máte na výběr z těchto dortů:
Druh dortu: 
    Rozkvetlý dort (květy z cukru a ovoce) - FLOVER (700 Kč)
    Královský (ovoce, makronky, krém, dekorace) - KINGS (700 Kč)
    Jednorožec (marcip.roh a uši, krém) -  UNICORN (500 Kč)
    Naked cake zdobený ovocem - NAKED (0 Kč)
    Zdobený lesním ovocem - FRUIT (100 Kč)
    Přelitý polevou ze slaného karamelu a čokolády - CARAMEL (100 Kč)
    Čokoládou vysypaný ornament - ORNAMENT (0 Kč)
Korpus:
    Čokoládový - CHOCO (200 Kč)
    Vanilkový - VANILA (200 Kč)
    Oříškový - NUTS (200 Kč)
Krém:
    Ovocný - FRUIT (400 Kč)
    Čokoládový - CHOCO (400 Kč)
    Praliné - PRALIN (500 Kč)
    Vanilkový - VANILA (400 Kč)
    Karamelový - CARAMEL (400 Kč)
    Kávový - COFFEE (400 Kč)
Počet porcí min. porce 8, max. 25 porcí - základní cena  je pro 12 - 16 osob:
    8-11 osob (80 % ceny)
    12-16 osob (100 % ceny)
    17-20 osob (120 % ceny)
    21-25 osob (140 % ceny)
Bezlepkový:
    1 (ANO) (ano + 200 Kč)
    0 (NE) 
Počet svíček (5 Kč/svíčka)""")

#druh dortu
elif cake == "FLOVER":
    price = price + 700
    kindCake = "rozkvetlý "
    kindCake2 = "s ovocem"
elif cake == "KINGS":
    price = price + 700
    kindCake = "královský "
    kindCake2 = "s makronkami a cukrovými ozdobami"
elif cake == "UNICORN":
    price = price + 500
    kindCake = "dětský "
    kindCake2 = "jednorožec"
elif cake == "FRUIT":
    price = price + 100
    kindCake = ""
    kindCake2 = "s lesním ovocem"
elif cake == "CARAMEL":
    price = price + 100
    kindCake = ""   
    kindCake2 = "se slaným karamelem"
elif cake == "NAKED":
    kindCake = "naked "
    kindCake2 = "zdobený ovocem"
elif cake == "ORNAMENT":
    kindCake = ""
    kindCake2 = "zdobený ornamentem"

#corpus and cream split
cc = (sys.argv[2]).split(sep="-")

#corpus
if cc[0] == "CHOCO":
    corpus = "čokoládovým"
elif cc[0] == "VANILA":
    corpus = "vanilkovým"
elif cc[0] == "NUTS":
    corpus = "oříškovým"

#cream
if cc[1] == "FRUIT":
    cream = "ovocným"
elif cc[1] == "CHOCO":
    cream = "čokoládovým"
elif cc[1] == "PRALIN":
    cream = "pralinkovým"
    price += 100
elif cc[1] == "VANILA":
    cream = "vanilkovým"
elif cc[1] == "CARAMEL":
    cream = "karamelovým"
elif cc[1] == "COFFEE":
    cream = "kávovým"

#Gluten Free
if int(sys.argv[4]) == 1:
    glutenFreePrint = "bezlepkový "
    price = price + 200
else:
    glutenFreePrint = ""

#pieces
pieces = int(sys.argv[3])
if pieces <= 11:
    price = 0.8 * price
    piecesPrint = "8 až 11"
elif pieces <= 20 and pieces >= 17:
    price = 1.2 * price
    piecesPrint = "17 až 20"
elif pieces >= 21:
    price = 1.4 * price
    piecesPrint = "21 až 25"
else:
    piecesPrint = "12 až 16"

#candles
candles = int(sys.argv[5])
price = price + (candles*5)
if candles > 0:
    candlePrint = f"Na dortu bude {candles} svíček."
else:
    candlePrint = "Dort bude bez svíček."

#print(f'Vybral sis {kindCake} dort s {solid} korpusem a {cream} krémem. Dort bude pro {pieces} {candles}.')
print(f'Vybral sis {glutenFreePrint}{kindCake}dort {kindCake2} s {corpus} korpusem a {cream} krémem.')
print (f'Dort bude mít {piecesPrint} porcí.{candlePrint} ')
print (f'Cena dortu bude {int(price)} korun.')