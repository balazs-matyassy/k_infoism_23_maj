# 1. feladat: adattároló osztály létrehozása
class Utasszallito:
    def __init__(self, tipus, ev, utas, szemelyzet, utazosebesseg, felszallotomeg, fesztav):
        self.tipus = tipus
        self.ev = ev
        self.utas = utas
        self.szemelyzet = szemelyzet
        self.utazosebesseg = utazosebesseg
        self.felszallotomeg = felszallotomeg
        self.fesztav = fesztav


# 2. feladat: sorokat (a fájl 1 sorát) példányokká alakító függvény létrehozása
def sorbol_utasszallito(sor):
    sor = sor.strip()  # enter levágása a sor végéről
    ertekek = sor.split(';')

    tipus = ertekek[0]  # szöveg
    ev = int(ertekek[1])  # egész
    utas = ertekek[2]  # szöveg
    szemelyzet = ertekek[3]  # szöveg
    utazosebesseg = int(ertekek[4])  # egész
    felszallotomeg = int(ertekek[5])  # egész
    fesztav = float(ertekek[6].replace(',', '.'))

    utasszallito = Utasszallito(tipus, ev, utas, szemelyzet, utazosebesseg, felszallotomeg, fesztav)

    return utasszallito


# 3. feladat: fájlból utasszállítókat beolvasó függvény létrehozása
def fajlbol_utasszallitok(fajlnev):
    fajl = open(fajlnev, encoding='utf-8')
    utasszallitok = []

    # Ha van, akkor be kell olvasni a fejlécet.
    fejlec = fajl.readline()

    for sor in fajl:
        utasszallito = sorbol_utasszallito(sor)
        utasszallitok.append(utasszallito)

    fajl.close()

    return utasszallitok


# 4. feladat: beolvasás tesztelése
utasszallitok = fajlbol_utasszallitok('utasszallitok.txt')
# print(utasszallitok)

# 4. érettségi feladat: Határozza meg és írja ki a képernyőre a forrásállományban lévő adatsorok
# (repülőgéptípusok) darabszámát!
print(f'4. feladat: Adatsorok száma: {len(utasszallitok)}')

# 5. érettségi feladat: Határozza meg és írja ki a képernyőre a Boeing vállalat által gyártott repülőgéptípusok
# darabszámát! Feltételezheti, hogy minden általuk gyártott típus neve a „Boeing”
# szórészlettel kezdődik.
boeingek_szama = 0

for utasszallito in utasszallitok:
    if utasszallito.tipus.startswith('Boeing'):
        boeingek_szama += 1

print(f'5. feladat: Boeing típusok száma: {boeingek_szama}')

# 6. érettségi feladat: Határozza meg azt a repülőgéptípust, amely a legtöbb utas szállítására volt alkalmas! Ha az
# utasok száma „tól-ig” formában (például: 150-179) van megadva, akkor mindig az „ig”
# értéket használja az összehasonlításnál! A típus adatait a feladat végén található minta szerint
# írja a képernyőre! Feltételezheti, hogy nem alakult ki az élen holtverseny!
