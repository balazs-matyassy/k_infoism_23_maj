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


# 6.1. érettségi feladat: maximális utasszámot visszaadó segédfüggvény létrehozása
# Pl. '220-336' -> 336
# Pl. '218' -> 218
def max_utasszam(utasszallito):
    if '-' in utasszallito.utas:
        ertekek = utasszallito.utas.split('-')
        return int(ertekek[1])
    else:
        return int(utasszallito.utas)


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
legtobb_utast_szallito = utasszallitok[0]

for utasszallito in utasszallitok:
    if max_utasszam(utasszallito) > max_utasszam(legtobb_utast_szallito):
        legtobb_utast_szallito = utasszallito

print('6. feladat: A legtöbb utast szállító repülőgéptípus:')
print(f'\tTípus: {legtobb_utast_szallito.tipus}')
print(f'\tElső felszállás: {legtobb_utast_szallito.ev}')
print(f'\tUtasok száma: {legtobb_utast_szallito.utas}')
print(f'\tSzemélyzet: {legtobb_utast_szallito.szemelyzet}')
print(f'\tUtazósebesség: {legtobb_utast_szallito.utazosebesseg}')
