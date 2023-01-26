import os
import time


#W menu glownym korzystamy z tej bazy w podpunkcie 1
class auta_w_naprawie:
    def __init__(self,numer,marka,rocznik,przebieg):
        self.numer = numer
        self.marka = marka
        self.rocznik = rocznik
        self.przebieg = przebieg


#W menu glownym korzystamy z tej bazy w podpunkcie 2
class naprawione_auta:
    def __init__(self,marka,rocznik,przebieg):
        self.marka = marka
        self.rocznik = rocznik
        self.przebieg = przebieg



#W menu glownym korzystamy z tej bazy w podpunkcie 2
class dostepne_czesci:
    def __init__(self,czesc,samochod,koszt):
        self.czesc = czesc
        self.samochod = samochod
        self.koszt = koszt



#W menu glownym korzystamy z tej bazy w podpunkcie 2
class brakujace_czesci:
    def __init__(self,czesc,samochod,koszt):
        self.czesc = czesc
        self.samochod = samochod
        self.koszt = koszt



#W menu glownym korzystamy z tej bazy w podpunkcie 6
class dane_kontaktowe:
    def __init__(self,imie,nazwisko,telefon,miasto,adres,ulica,gust):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.miasto = miasto
        self.adres = adres
        self.ulica = ulica
        self.gust = gust




#Dodawania samochodow w naprawie
def dodaj_samochod_w_naprawie():
    os.system("clear")
    if len(samochody_w_naprawie) == 0:
        numer = 1
    else:
        numer = len(samochody_w_naprawie) + 1
    marka = str(input("Podaj marke samochodu: "))
    rocznik = int(input("Podaj rocznik samochodu: "))
    przebieg = int(input("Wpisz przebieg samochodu: "))

    print("")


    imie = input("Wprowadz imie klienta: ")
    nazwisko = input("Podaj nazwisko klienta: ")
    telefon = int(input("Wprowadz telefon klienta: "))
    miasto = input("Miasto: ")
    adres = input("Adres zamieszkania(Ulica bez numeru domu): ")
    ulica = int(input("Podaj numer domu: "))
    x = str(input("Czy klient lubi muzyke klasyczna (Tak lub Nie): "))

    if x == "Tak":
        while True:
            print("Wloz do samochodu swoja plyte CD")
            gust = x
            a = int(input("Aby kontunowac wcisnij [1]: "))
            if a == 1:
                break
    if x == "Nie":
        while True:
            print("Nie wkladaj do samochodu swojej plyty CD")
            gust = x
            a = int(input("Aby kontunowac wcisnij [1]: "))
            if a == 1:
                break



    #tworzymy obiekt
    nowa = auta_w_naprawie(numer,marka,rocznik,przebieg)
    nowa2 = dane_kontaktowe(imie,nazwisko,telefon,miasto,adres,ulica,gust)

    #dodajmy obiekt do tablicy
    samochody_w_naprawie.append(nowa)
    dane_klienta.append(nowa2)



def dodajCzesciDostepne():
    os.system("clear")
    czesc = input("Podaj nazwe czesci: ")
    samochod = str(input("Podaj marke samochodu, do ktorego pasuje dana czesc: "))
    koszt = int(input("Podaj cene czesci: "))

    nowa = dostepne_czesci(czesc,samochod,koszt)

    dostepne_czesci_spis.append(nowa)




def dodajCzesciBrakujace():
    os.system("clear")
    czesc = input("Podaj nazwe czesci: ")
    samochod = str(input("Podaj marke samochodu, do ktorego pasuje dana czesc: "))
    koszt = int(input("Podaj cene czesci: "))

    nowa = brakujace_czesci(czesc,samochod,koszt)

    brakujace_czesci_spis.append(nowa)


def pokaz_czesci_dostepne():
    os.system("clear")
    while True:
        print("Cze ^ ci dostepne w warsztacie: ")
        for x in dostepne_czesci_spis:
            print(x.czesc, x.samochod, x.koszt, "PLN")

        print("Cze ^ ci niedostepne w warsztacie: ")
        for x in brakujace_czesci_spis:
            print(x.czesc, x.samochod, x.koszt, "PLN")

        y = int(input("Aby przejsc do menu glownego wcisnij [1]: "))
        if y == 1:
            break




def cena_brakujacych_czesci():
    while True:
        suma = 0
        y = str(input("Podaj marke samochodu: "))
        for x in brakujace_czesci_spis:
            if y == x.samochod:
                suma = suma + x.koszt

        print("Calkowity koszt brakujacych czesci do {} to {} PLN".format(y,suma))

        y = int(input("Aby przejsc do menu glownego wcisnij [1]: "))
        if y == 1:
            break




#Pokazywanie samochodow bedaceych obecnie w naprawie
def pokaz_samochody_w_naprawie():
    os.system("clear")
    print("Samochody bedace obecnie w naprawie: ",len(samochody_w_naprawie))
    for x in samochody_w_naprawie:
        #wyswietlamy w ^ a ^ ciwo ^ ci obiektu po kropce
        print(x.numer,x.marka,x.rocznik,x.przebieg,"km")



#Pokazywanie samochodow bedaceych obecnie w naprawie
def pokaz_samochody_w_naprawie_spis():
    os.system("clear")
    while True:
        print("Samochody bedace obecnie w naprawie: ",len(samochody_w_naprawie))
        for x in samochody_w_naprawie:
            #wyswietlamy w ^ a ^ ciwo ^ ci obiektu po kropce
            print(x.marka,x.rocznik,x.przebieg,"km")
        y = int(input("Aby przejsc do menu glownego wcisnij [1]: "))
        if y == 1:
            break




#Usuwanie naprawionych samochodow z listy do naprawy i dodawanie ich do listy naprawionych
def usun_naprawiony_samochod():
    numer = int(input("Podaj numer samochodu z listy do naprawy: "))
    x = samochody_w_naprawie[numer-1]
    naprawione_samochody.append(x)
    del samochody_w_naprawie[numer-1]





#Pokazywanie naprawioncych samochodow
def pokaz_naprawione_samochody():
    os.system("clear")
    while True:
        print("Samochody naprawione od poczatku istneinia zakladu: ",len(naprawione_samochody))
        for x in naprawione_samochody:
            #wyswietlamy w ^ a ^ ciwo ^ ci obiektu po kropce
            a = len(naprawione_samochody)
            print("{}".format(a),x.marka,x.rocznik,x.przebieg,"km")
        x = int(input("Aby przejsc do menu glownego wcisnij [1]: "))
        if x == 1:
            break



#Pokazywanie rejestr klientow
def pokaz_dane_klienta():
    os.system("clear")
    while True:
        print("Aktualni klienci zakladu: ",len(dane_klienta))
        for x in dane_klienta:
            #wyswietlamy w ^ a ^ ciwo ^ ci obiektu po kropce
            a = len(dane_klienta)
            print(x.imie,x.nazwisko,x.telefon,x.miasto,x.adres,x.ulica)
        x = int(input("Aby przejsc do menu glownego wcisnij [1]: "))
        if x == 1:
            break



def najczesciej_naprawiana_marka_aut():
    while True:
        print("Alfa Romeo")

        y = int(input("Aby przejsc do menu glownego wcisnij [1]: "))
        if y == 1:
            break



samochody_w_naprawie = []
naprawione_samochody = []
dane_klienta = []
dostepne_czesci_spis = []
brakujace_czesci_spis = []



#Menu glowne
while True:
    print("-------------------------------------------------")
    print("Witaj w warsztacie samochodowym Milana Mediolana.")
    print("-------------------------------------------------")
    print("")
    print("-------------------------------------------------")
    pokaz_samochody_w_naprawie()
    print("")
    print("-------------------------------------------------")
    print("")
    print("---------------------------")
    print("1. Dodaj smochod do naprawy")#Karta podpunkt a)
    print("")
    print("2. Usun naprawiony samochod")#Karta podpunkt h)
    print("")
    print("3. Podaj dostepne czesci")
    print("")
    print("4. Podaj brakujace czesci")
    print("")
    print("5. Pokaz dostepne i brakujace czesci w warsztacie")#Karta podpunkt c)
    print("")
    print("6. Wyswietl cene brakujacych czesci")#Karta podpunkt e)
    print("")
    print("7. Samochody czekajace w kolejce do naprawy")#Karta podpunkt d)
    print("")
    print("8. Dane kontaktowe klienta")#Karta podpunkt f)
    print("")
    print("9. Najczesciej naprawiana marka samochodu")#Karta podpunkt g)
    print("")
    print("10. Spis naprawionych samochodow")#Karta podpunkt h)
    print("")
    print("0. Koniec programu")
    print("--------------------------")
    co_robimy = int( input("Wybierz opcje: "))

    if co_robimy==1:
        dodaj_samochod_w_naprawie()
        os.system("clear")

    if co_robimy==2:
        usun_naprawiony_samochod()
        os.system("clear")

    if co_robimy == 3:
        dodajCzesciDostepne()
        os.system("clear")

    if co_robimy == 4:
        dodajCzesciBrakujace()
        os.system("clear")

    if co_robimy == 5:
        pokaz_czesci_dostepne()
        os.system("clear")

    if co_robimy == 6:
        cena_brakujacych_czesci()
        os.system("clear")

    if co_robimy == 7:
        pokaz_samochody_w_naprawie_spis()
        os.system("clear")

    if co_robimy == 8:
        pokaz_dane_klienta()
        os.system("clear")

    if co_robimy == 9:
        najczesciej_naprawiana_marka_aut()
        os.system("clear")

    if co_robimy == 10:
        pokaz_naprawione_samochody()
        os.system("clear")

    if co_robimy==0:
        break




