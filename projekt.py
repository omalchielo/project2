import random,time
def carky():
    return ("-" * 47)

def intro():
    print(carky())
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(carky())

def main():
    intro()
    pokusy = 0
    cislo = nahodne_cislo()
    zacatek = time.time()
    print(cislo)
    while True:
        tip = input("Zadej cislo: ")
        print(carky())
        if moje_cislo(tip):
            continue
        pokusy += 1
        porovnani(tip,cislo,pokusy,zacatek)
        print(carky())

def nahodne_cislo():
    cislo = ""
    while len(set(cislo)) != 4:
        cislo = str(random.randint(1000, 9999))
    return cislo

def moje_cislo(tip):
    vysledek = False
    if len(tip) != 4:
        print('musis zadat 4 ciferne cislo')
        vysledek = True
    if len(tip) != len(set(tip)):
        print('cislo nesmi obsahovat duplicity')
        vysledek = True
    if not tip.isdigit():
        print('nesmi byt jine znaky nez cislice')
        vysledek = True
    if tip[0] == '0':
        print('nesmi byt nula na zacatku')
        vysledek = True
    return vysledek

def porovnani(tip,cislo,pokusy,zacatek):
    a = []
    bulls = cows = 0
    for i in range(len(tip)):
        if cislo[i] == tip[i]:
            bulls += 1


    for j in range(len(tip)):
        if cislo[j] != tip[j]:
            if cislo[j] in tip:
                if cislo[j] not in a:
                    a.append(j)
                    cows += 1
    konec_hry(bulls,cows,pokusy,zacatek)

def konec_hry(bulls,cows,pokusy,zacatek):
    if bulls == 4:
        konec = time.time()
        delka = (konec - zacatek)
        print("{0:.2f}".format(delka),"sekund")
        if pokusy == 1:
            vysledek = "Excelentně!"
        if 5 > pokusy > 1:
            vysledek = "Výborně"
        else:
            vysledek = "Dobré!"
        print(f"Správné čislo si uhádl na {pokusy} pokus, {vysledek}")
        quit()
    else:
        if bulls == 1:
            gramatika1 = "bull"
        else:
            gramatika1 = "bulls"
        if cows == 1:
            gramatika2 = "cow"
        else:
            gramatika2 = "cows"
        print(f"Máš {bulls} {gramatika1} a {cows} {gramatika2}")

if __name__ == "__main__":
    main()
