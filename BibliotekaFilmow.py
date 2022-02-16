import random

class Film:
    def __init__(self, tytul, rok_wydania, gatunek):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek

        #Variables
        self.liczba_odtworzen = 0

    def __repr__(self):
        return f"{self.tytul} ({self.rok_wydania})"

    def play(self, step=1):
        self.liczba_odtworzen += step


class Serial(Film):
    def __init__(self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu

    def __repr__(self):
        return f"{self.tytul} S{self.numer_sezonu}E{self.numer_odcinka}"

def get_entries_by_type(lista, type):
    nowa_lista = []
    for object in lista:
        if object.__class__.__name__ == type:
            nowa_lista.append(object)
    return sorted(nowa_lista, key=lambda x: x.tytul)

def get_movies(lista):
    return get_entries_by_type(lista, "Film")

def get_series(lista):
    return get_entries_by_type(lista, "Serial")

def search(tytul, list):
    for obiekt in list:
        if tytul == obiekt.tytul:
            return obiekt
    return None

def generate_views(list):
    random.choice(list).liczba_odtworzen += random.randint(1, 100)

def ten_generate_views():
    for i in range (0,9):
        generate_views(lista)

def top_titles(list, ilosc=1, type=None):
    if type is not None:
        list = get_entries_by_type(list, type)
    return sorted(list, key=lambda x: x.liczba_odtworzen, reverse=True)[0:ilosc]




lista = []
lista.append(Film(tytul="Wladca Pierscieni", rok_wydania=1994, gatunek="fantastyka"))
lista.append(Serial(tytul="The Office", rok_wydania=2000, gatunek="Komedia", numer_odcinka="S01", numer_sezonu="E01"))
lista.append(Film(tytul="Ogniem i Mieczem", rok_wydania=1996, gatunek="fantastyka"))
lista.append(Film(tytul="Star Wars", rok_wydania=1986, gatunek="fantastyka"))
lista.append(Serial(tytul="Mentalista", rok_wydania=2000, gatunek="Komedia", numer_odcinka="S01", numer_sezonu="E01"))
lista.append(Serial(tytul="Gra o Tron", rok_wydania=2000, gatunek="Komedia", numer_odcinka="S01", numer_sezonu="E01"))


listaa = []
listaa = get_series(lista)
print(listaa[0].tytul)
print(lista[0])
print(search("Wladca Pierscieni", lista).tytul)

ten_generate_views()

for obiekt in lista:
    print(f"{obiekt.liczba_odtworzen} filmu {obiekt.tytul}")

sortowana_lista = get_series(lista)

for obiekt in sortowana_lista:
    print(f"{obiekt.tytul}")
print("-----------------------------------")
tt = top_titles(lista, 3, "Serial")
for entry in tt:
    print(entry, f"wyswietlenia: {entry.liczba_odtworzen}")