#-------------------------------------------------------------------------------
# Name:        lowcy_gwiazd.py
# Purpose:     WDI, Projekt I
#
# Author:      Mikołaj Pazera
# Author:      Krzysztof Piątkowski
# Created:     18/10/2018
# Copyright:   (c) Mikołaj Pazera, Krzysztof Piątkowski 2018
#-------------------------------------------------------------------------------

from sys import *
from math import *
from random import *
from time import *


print ("Witaj w grze Lowcy Gwiazd!")
print ("Jestes zamkniety w labiryncie pokoi, aby sie wydostac zbierz piec gwiazdek")
print ("Tylko w ten sposob otrzymasz tytul Lowcy Gwiazd")
print ("Gwiazdki mozesz znalezc w skrzyniach (na mapie oznaczone 'S') lub otrzymywac je")
print ("za wykonywanie zadan (na mapie oznaczone 'Q')")
print ("Pamietaj, ze kazde zadanie znika po jego pomyslnym ukonczeniu")
print ("Twoja pozycja na mapie oznaczona jest litera 'T'")
print ("Aby przemieszczac sie miedzy pokojami uzywaj polecen: ")
print ("g - w gore\nd - w dol\np - w prawo\nl - w lewo")
print ("Inne komendy ktorych mozesz uzyc: ")
print ("q - rozpocznij zadanie, jesli jestes w pokoju, w ktorym znajduje się 'Q'")
print ("s - otworz skrzynke, jesli jestes w pokoju, w ktorym znajduje się 'S'")
print ("e - aby zamknac program")
print ("gwiazdki - sprawdza ile gwiazdek zebrales do tej pory")
print ("UWAGA, wszystkie polecenia zatwierdzaj klawiszem Enter")


#tworzenie pustego pokoju polnocno - zachodniego
pokojNW = [[" " for x in range(11)] for y in range(11)]

#tworzenie pokoju polnocnego
pokojN = [[" " for x in range(11)] for y in range(11)]

#tworzenie pokoju polnocno - wschodniego
pokojNE = [[" " for x in range(11)] for y in range(11)]

#tworzenie pokoju zachodniego
pokojW = [[" " for x in range(11)] for y in range(11)]

#tworzenie pokoju centralnego
pokojC = [[" " for x in range(11)] for y in range(11)]

#tworzenie pokoju wschodniego
pokojE = [[" " for x in range(11)] for y in range(11)]

#tworzenie pokoju poludniowo - zachodniego
pokojSW = [[" " for x in range(11)] for y in range(11)]

#tworzenie pokoju poludniowego
pokojS = [[" " for x in range(11)] for y in range(11)]

#tworzenie pustego pokoju poludniowo - wschodniego
pokojSE = [[" " for x in range(11)] for y in range(11)]

#pozycja startowa to pokoj srodkowy
pozycja = "C"
#poczatkowy stan gwiazdek gracza
status_gwiazdek = 0
#warunek wygranej jest okreslany w sprawdz_gwiazdki()
wygrana = 0
#odwrocony licznik wykonanych zadan i otwartych skrzynek
#odwrocony bo na takim latwiej wykonuje sie beta testy
wydarzenia_na_mapie = 10

#funkcja drukuje na ekranie zbior wszystkich dostepnych komend
def pokaz_pomoc():

    print ("Dostepne komendy: ")
    print ("g - w gore\nd - w dol\np - w prawo\nl - w lewo")
    print ("q - rozpocznij zadanie, jesli jestes w pokoju, w ktorym znajduje się 'Q'")
    print ("s - otworz skrzynke, jesli jestes w pokoju, w ktorym znajduje się 'S'")
    print ("m - pokaz mape")
    print ("e - aby zamknac program")
    print ("gwiazdki - sprawdza ile gwiazdek zebrales do tej pory")
    print ("UWAGA, wszystkie polecenia zatwierdzaj klawiszem Enter")

    return;


#funkcja wypelnia pokoje scianami, naroznikami i symbolami
def utworz_sciany():

    #wypelnianie naroznikow
    pokojN[0][0] = '\u2554'
    pokojN[0][10] = '\u2557'
    pokojN[10][0] = '\u255a'
    pokojN[10][10] = '\u255d'

    pokojNE[0][0] = '\u2554'
    pokojNE[0][10] = '\u2557'
    pokojNE[10][0] = '\u255a'
    pokojNE[10][10] = '\u255d'

    pokojW[0][0] = '\u2554'
    pokojW[0][10] = '\u2557'
    pokojW[10][0] = '\u255a'
    pokojW[10][10] = '\u255d'

    pokojC[0][0] = '\u2554'
    pokojC[0][10] = '\u2557'
    pokojC[10][0] = '\u255a'
    pokojC[10][10] = '\u255d'

    pokojE[0][0] = '\u2554'
    pokojE[0][10] = '\u2557'
    pokojE[10][0] = '\u255a'
    pokojE[10][10] = '\u255d'

    pokojSW[0][0] = '\u2554'
    pokojSW[0][10] = '\u2557'
    pokojSW[10][0] = '\u255a'
    pokojSW[10][10] = '\u255d'

    pokojS[0][0] = '\u2554'
    pokojS[0][10] = '\u2557'
    pokojS[10][0] = '\u255a'
    pokojS[10][10] = '\u255d'

    #petla wypelnia sciany horyzontalne
    for i in range(9):
        pokojN[0][i+1] = '\u2550'
        pokojN[10][i+1] = '\u2550'

        pokojNE[0][i+1] = '\u2550'
        pokojNE[10][i+1] = '\u2550'

        pokojW[0][i+1] = '\u2550'
        pokojW[10][i+1] = '\u2550'

        pokojC[0][i+1] = '\u2550'
        pokojC[10][i+1] = '\u2550'

        pokojE[0][i+1] = '\u2550'
        pokojE[10][i+1] = '\u2550'

        pokojSW[0][i+1] = '\u2550'
        pokojSW[10][i+1] = '\u2550'

        pokojS[0][i+1] = '\u2550'
        pokojS[10][i+1] = '\u2550'

    #petla wypelnia sciany wertykalne
    for i in range(9):
        pokojN[i+1][0] = '\u2551'
        pokojN[i+1][10] = '\u2551'

        pokojNE[i+1][0] = '\u2551'
        pokojNE[i+1][10] = '\u2551'

        pokojW[i+1][0] = '\u2551'
        pokojW[i+1][10] = '\u2551'

        pokojC[i+1][0] = '\u2551'
        pokojC[i+1][10] = '\u2551'

        pokojE[i+1][0] = '\u2551'
        pokojE[i+1][10] = '\u2551'

        pokojSW[i+1][0] = '\u2551'
        pokojSW[i+1][10] = '\u2551'

        pokojS[i+1][0] = '\u2551'
        pokojS[i+1][10] = '\u2551'

    #dodawanie drzwi
    pokojN[10][5] = " "

    pokojNE[10][5] = " "

    pokojW[5][10] = " "

    pokojC[0][5] = " "
    pokojC[5][0] = " "
    pokojC[5][10] = " "
    pokojC[10][5] = " "

    pokojE[0][5] = " "
    pokojE[5][0] = " "

    pokojSW[5][10] = " "

    pokojS[0][5] = " "
    pokojS[5][0] = " "

    #pozycja startowa
    pokojC[5][5] = "T"

    #dodawanie skrzynek i zadan
    pokojN[1][5] = "S"
    pokojN[5][1] = "Q"

    pokojNE[1][5] = "S"
    pokojNE[5][9] = "Q"

    pokojW[9][5] = "Q"

    pokojC[9][9] = "S"

    pokojE[5][9] = "Q"

    pokojSW[1][5] = "Q"
    pokojSW[9][5] = "S"

    pokojS[5][9] = "Q"
    return;


#funkcja rysuje wszystkie pokoje w ich aktualnym stanie
def rysuj_mape():

    #petla dla pierwszego wiersza pokoi
    for x in range(11):
        line = ""
        for y in range(11):
            line += str(pokojNW[x][y]) + " "
        for y in range(11):
            line += str(pokojN[x][y]) + " "
        for y in range(11):
            line += str(pokojNE[x][y]) + " "
        print (line)

    #petla dla drugiego wiersza pokoi
    for x in range(11):
        line = ""
        for y in range(11):
            line += str(pokojW[x][y]) + " "
        for y in range(11):
            line += str(pokojC[x][y]) + " "
        for y in range(11):
            line += str(pokojE[x][y]) + " "
        print (line)

    #petla dla trzeciego wiersza pokoi
    for x in range(11):
        line = ""
        for y in range(11):
            line += str(pokojSW[x][y]) + " "
        for y in range(11):
            line += str(pokojS[x][y]) + " "
        for y in range(11):
            line += str(pokojSE[x][y]) + " "
        print (line)

    return;


#funckja poruszania sie oraz wyswietlania aktualnej pozycji gracza
def poruszanie_sie(kierunek):
    #globalna zmienna pozycji bedzie zmieniana przy kazdym ruchu
    global pozycja

    #dla pokoju centralnego
    if pozycja == "C":
        if kierunek == "g":
            pozycja = "N"
            pokojN[5][5] = "T"
        elif kierunek == "d":
            pozycja = "S"
            pokojS[5][5] = "T"
        elif kierunek == "p":
            pozycja = "E"
            pokojE[5][5] = "T"
        elif kierunek == "l":
            pozycja = "W"
            pokojW[5][5] = "T"

        pokojC[5][5] = " "


    #dla pokoju polnocnego
    elif pozycja == "N":
        if kierunek == "d":
            pozycja = "C"
            pokojC[5][5] = "T"
        elif kierunek == "g":
            print ("Nie mozesz poruszyc sie w tym kierunku!")
            komendy()
        elif kierunek == "p":
            print ("Nie mozesz poruszyc sie w tym kierunku!")
            komendy()
        elif kierunek == "l":
            print ("Nie mozesz poruszyc sie w tym kierunku!")
            komendy()

        pokojN[5][5] = " "

    #dla pokoju wschodniego
    elif pozycja == "E":
        if kierunek == "g":
            pozycja = "NE"
            pokojNE[5][5] = "T"
        elif kierunek == "l":
            pozycja = "C"
            pokojC[5][5] = "T"
        elif kierunek == "p":
            print ("Nie mozesz poruszyc sie w tym kierunku!")
            komendy()
        elif kierunek == "d":
            print ("Nie mozesz poruszyc sie w tym kierunku!")
            komendy()

        pokojE[5][5] = " "

    #dla pokoju polnocno - wschodniego
    elif pozycja == "NE":
        if kierunek == "d":
            pozycja = "E"
            pokojE[5][5] = "T"
        elif kierunek == "g":
            print ("Nie mozesz poruszyc sie w tym kierunku!")
            komendy()
        elif kierunek == "p":
            print ("Nie mozesz poruszyc sie w tym kierunku!")
            komendy()
        elif kierunek == "l":
            print ("Nie mozesz poruszyc sie w tym kierunku!")
            komendy()

        pokojNE[5][5] = " "

    #dla pokoju zachodniego
    elif pozycja == "W":
        if kierunek == "g":
            print ("Nie mozesz poruszyc sie w tym kierunku!")
            komendy()
        elif kierunek == "l":
            print ("Nie mozesz poruszyc sie w tym kierunku!")
            komendy()
        elif kierunek == "d":
            print ("Nie mozesz poruszyc sie w tym kierunku!")
            komendy()
        elif kierunek == "p":
            pozycja = "C"
            pokojC[5][5] = "T"

        pokojW[5][5] = " "

    #dla pokoju poludniowego
    elif pozycja == "S":
        if kierunek == "g":
            pozycja = "C"
            pokojC[5][5] = "T"
        elif kierunek == "l":
            pozycja = "SW"
            pokojSW[5][5] = "T"
        elif kierunek == "d":
            print ("Nie mozesz poruszyc sie w tym kierunku!")
            komendy()
        elif kierunek == "p":
            print ("Nie mozesz poruszyc sie w tym kierunku!")
            komendy()

        pokojS[5][5] = " "

    #dla pokoju poludniowo - zachodniego
    elif pozycja == "SW":
        if kierunek == "g":
            print ("Nie mozesz poruszyc sie w tym kierunku!")
            komendy()
        elif kierunek == "p":
            pozycja = "S"
            pokojS[5][5] = "T"
        elif kierunek == "d":
            print ("Nie mozesz poruszyc sie w tym kierunku!")
            komendy()
        elif kierunek == "l":
            print ("Nie mozesz poruszyc sie w tym kierunku!")
            komendy()

        pokojSW[5][5] = " "

    rysuj_mape()
    return;


#funkcja rozpoczyna odpowiedni quest w zaleznosci od aktualnej pozycji gracza
def wczytaj_quest(pokoj):

    #zmienna typu bool do sprawdzania czy w aktualnym pokoju jest mozliwosc wlaczenia zadania
    quest_istnieje = 0

    # w pokoju centralnym nie ma questow
    if pokoj == "C":
        print ("W tym pokoju nie ma dostepnych zadan! Sprobuj w innym")

    #pokoj polnocny
    elif pokoj == "N":
        #petla sprawdza czy w pokoju jest quest
        for x in range(11):
            for y in range(11):
                if pokojN[x][y] == "Q":
                    #jesli jest to zmienna przyjmuje wartosc true
                    quest_istnieje = 1
        #jesli jest quest to wlaczana jest funcja zadania
        if quest_istnieje == 1:
            print("=============================\nRozpoczyna sie zadanie!")
            losuj_pudelko()
            print("Koniec zadania\n=============================")
        #jesli nie ma to wyswietlany jest kominukat
        else:
            print ("W tym pokoju nie ma dostepnych zadan! Sprobuj w innym")

    #pokoj polnocno - wschodni
    elif pokoj == "NE":
        #petla sprawdza czy w pokoju jest quest
        for x in range(11):
            for y in range(11):
                if pokojNE[x][y] == "Q":
                    #jesli jest to zmienna przyjmuje wartosc true
                    quest_istnieje = 1
        #jesli jest quest to wlaczana jest funcja zadania
        if quest_istnieje == 1:
            print("=============================\nRozpoczyna sie zadanie!")
            piec_pytan()
            print("Koniec zadania\n=============================")
        #jesli nie ma to wyswietlany jest kominukat
        else:
            print ("W tym pokoju nie ma dostepnych zadan! Sprobuj w innym")

    #pokoj zachodni
    elif pokoj == "W":
        #petla sprawdza czy w pokoju jest quest
        for x in range(11):
            for y in range(11):
                if pokojW[x][y] == "Q":
                    #jesli jest to zmienna przyjmuje wartosc true
                    quest_istnieje = 1
        #jesli jest quest to wlaczana jest funcja zadania
        if quest_istnieje == 1:
            print("=============================\nRozpoczyna sie zadanie!")
            f_kwadratowa()
            print("Koniec zadania\n=============================")
        #jesli nie ma to wyswietlany jest kominukat
        else:
            print ("W tym pokoju nie ma dostepnych zadan! Sprobuj w innym")

    #pokoj wschodni
    elif pokoj == "E":
        #petla sprawdza czy w pokoju jest quest
        for x in range(11):
            for y in range(11):
                if pokojE[x][y] == "Q":
                    #jesli jest to zmienna przyjmuje wartosc true
                    quest_istnieje = 1
        #jesli jest quest to wlaczana jest funcja zadania
        if quest_istnieje == 1:
            print("=============================\nRozpoczyna sie zadanie!")
            test_abcd()
            print("Koniec zadania\n=============================")
        #jesli nie ma to wyswietlany jest kominukat
        else:
            print ("W tym pokoju nie ma dostepnych zadan! Sprobuj w innym")

    #pokoj poludniowo - zachodni
    elif pokoj == "SW":
        #petla sprawdza czy w pokoju jest quest
        for x in range(11):
            for y in range(11):
                if pokojSW[x][y] == "Q":
                    #jesli jest to zmienna przyjmuje wartosc true
                    quest_istnieje = 1
        #jesli jest quest to wlaczana jest funcja zadania
        if quest_istnieje == 1:
            print("=============================\nRozpoczyna sie zadanie!")
            zamiana_na_binarny()
            print("Koniec zadania\n=============================")
        #jesli nie ma to wyswietlany jest kominukat
        else:
            print ("W tym pokoju nie ma dostepnych zadan! Sprobuj w innym")

    #pokoj poludniowy
    elif pokoj == "S":
        #petla sprawdza czy w pokoju jest quest
        for x in range(11):
            for y in range(11):
                if pokojS[x][y] == "Q":
                    #jesli jest to zmienna przyjmuje wartosc true
                    quest_istnieje = 1
        #jesli jest quest to wlaczana jest funcja zadania
        if quest_istnieje == 1:
            print("=============================\nRozpoczyna sie zadanie!")
            losowanie_liczby()
            print("Koniec zadania\n=============================")
        #jesli nie ma to wyswietlany jest kominukat
        else:
            print ("W tym pokoju nie ma dostepnych zadan! Sprobuj w innym")
    return;


#funkcja losuje zawartosc otwieranej skrzynki
def losuj_w_skrzynce():
    global wydarzenia_na_mapie
    global status_gwiazdek

    #losujemy zawartos skrzynki
    zawartosc = randint(-1, 1)

    #imersja
    print ("=========================\nZnalazles skrzynke!")
    sleep(2)
    print ("Otwierasz ja a w srodku...")
    sleep(2)

    #jesli wylosowa wartosc jest ujemna
    if zawartosc == -1:
        #gracz nie moze utracic gwiazdek jesli ich nie ma, wtedy przyjmujemy ze skrzynka byla pusta
        if status_gwiazdek <= 0:
            print ("Niestety... w skrzynce nie ma nic pozytecznego")
        #jesli ma gwiazdki to w tym przypadku jedna traci
        else:
            status_gwiazdek -= 1
            print ("Oj! Skrzynka pochlanela jedna z Twoich gwiazdek! Coz za nieszczescie...")

    #jesli skrzynka jest pusta
    elif zawartosc == 0:
        print ("Niestety... w skrzynce nie ma nic pozytecznego")

    #jesli w skrzynce bylo 1 to dodajemy gwiazdke
    else:
        status_gwiazdek += 1
        print ("To Twoj szczesliwy dzien! Znalazles w skrzynce jedna gwiazdke!")

    sleep(3)
    print ("Skrzynka zamyka sie i niespodziewanie znika...")
    print ("=========================")
    wydarzenia_na_mapie -= 1
    sprawdz_gwiazdki()
    return;


#funkcja otwiera skrzynke w aktualnym pokoju i losuje ilosc gwiazdek
def otworz_skrzynke(pokoj):

    if pokoj == "W" or pokoj =="E" or pokoj == "S":
        print ("W tym pokoju nie ma skrzynek!")
    elif pokoj == "N":
        if pokojN[1][5] == "S":
            losuj_w_skrzynce()
            pokojN[1][5] = " "
        else:
            print ("Juz otworzyles skrzynke w tym pokoju!")

    elif pokoj == "NE":
        if pokojNE[1][5] == "S":
            losuj_w_skrzynce()
            pokojNE[1][5] = " "
        else:
            print ("Juz otworzyles skrzynke w tym pokoju!")

    elif pokoj == "C":
        if pokojC[9][9] == "S":
            losuj_w_skrzynce()
            pokojC[9][9] = " "
        else:
            print ("Juz otworzyles skrzynke w tym pokoju!")

    elif pokoj == "SW":
        if pokojSW[9][5] == "S":
            losuj_w_skrzynce()
            pokojSW[9][5] = " "
        else:
            print ("Juz otworzyles skrzynke w tym pokoju!")
    return;


#funkcja wywolywana jest po kazdym zadaniu aby sprawdzic czy gracz nie przekroczyl 5 gwiazdek
def sprawdz_gwiazdki():
    global status_gwiazdek
    global wydarzenia_na_mapie
    global wygrana
    #warunek zwyciestwa

    #jesli mapa nie jest pusta
    if wydarzenia_na_mapie != 0:
        #jesli cel 5 gwiazdek nie zostal osiagniety
        if wygrana == 0:
            #wypisz ilosc gwiazdek (poprawna gramatyka)
            if status_gwiazdek == 0:
                print ("Do tej pory zebrales " + str(status_gwiazdek) + " gwiazdek")
            elif status_gwiazdek == 1:
                print ("Do tej pory zebrales " + str(status_gwiazdek) + " gwiazdke")
            elif status_gwiazdek < 5:
                print ("Do tej pory zebrales " + str(status_gwiazdek) + " gwiazdki")
            #w tym przypadku gracz moze zakonczyc gre, zdobyl 5 gwiazdek
            elif status_gwiazdek == 5:
                print ("Gratulacje Lowco Gwiazd! Zdobyles 5 gwiazdek, a wiec ukonczyles gre")
                print ("Jesli chcesz mozesz grac dalej, na mapie nadal sa niezwiedzone przez Ciebie miejsca!")

                #gracz musi odpowiedziec tak lub nie
                while True:
                    decyzja = input("Czy chcesz grac nadal? (tak/nie): ")
                    #jesli gracz chce zakonczyc rozgrywke
                    if decyzja == "nie":
                        print ("Dziekujemy za gre!")
                        #dowolny klawisz wylaczy gre
                        wylacz_gre =  input("Wpisz dowolny znak i nacisnij Enter aby wylaczyc gre")
                        while wylacz_gre != "":
                            exit()
                    elif decyzja == "tak":
                        print ("Powodzenia w dalszej rozgrywce!")
                        break
                    else:
                        print ("Wpisz tak lub nie")

                #warunek zwyciestwa zostaje spełniony
                wygrana = 1
        #jesli gracz zdobyl juz 5 gwiazdek i gra nadal
        elif wygrana == 1:
            if status_gwiazdek == 0:
                print ("Łowco Gwiazd,\nNa swoim koncie aktualnie posiadasz " + str(status_gwiazdek) + " gwiazdek")
            elif status_gwiazdek == 1:
                print ("Łowco Gwiazd,\nNa swoim koncie aktualnie posiadasz " + str(status_gwiazdek) + " gwiazdke")
            elif status_gwiazdek < 5:
                print ("Łowco Gwiazd,\nNa swoim koncie aktualnie posiadasz " + str(status_gwiazdek) + " gwiazdki")
            elif status_gwiazdek >= 5:
                print ("Łowco Gwiazd,\nNa swoim koncie aktualnie posiadasz " + str(status_gwiazdek) + " gwiazdek")
    #jesli mapa jest pusta
    else:
        #jesli gracz nie zostal Lowca Gwiazd
        if wygrana == 0:
            #jesli gracz zdobyl wlasnie 5 gwiazdke
            if status_gwiazdek >= 5:
                print ("Gratulacje Lowco Gwiazd! Zdobyles 5 gwiazdek, a wiec ukonczyles gre")
                print ("Dziekujemy za gre!")
                #dowolny klawisz wylaczy gre
                wylacz_gre =  input("Wpisz dowolny znak i nacisnij Enter aby wylaczyc gre")
                while wylacz_gre != "":
                    exit()
            #jesli gracz nie zdobyl 5 gwiazdek to przegrywa
            else:
                print ("Wypelniles wszystkie zadania i otworzyles wszystkie skrzynki")
                print ("To nie jest Twoj szczesliwy dzien. Konczysz gre z wynikiem zebranych gwiazdek: " + str(status_gwiazdek))
                #dowolny klawisz wylaczy gre
                wylacz_gre =  input("Wpisz dowolny znak i nacisnij Enter aby wylaczyc gre")
                while wylacz_gre != "":
                    exit()
        #jesli gracz zdobyl 5 gwiazdek wczesniej i gral nadal
        elif wygrana == 1:
            print ("Lowco Gwiazd! Przeszedles cala mape")
            print ("Ilosc zebranych gwiazdek: " + str(status_gwiazdek))
            print ("Dziekujemy za gre!")
            #dowolny klawisz wylaczy gre
            wylacz_gre =  input("Wpisz dowolny znak i nacisnij Enter aby wylaczyc gre")
            while wylacz_gre != "":
                exit()

    return;


#funckja wczytuje komende gracza i decyduje ktora funckja zostanie uruchomiona jako nastepna
def komendy():

    #wczytanie nastepnej komendy gracza
    print ("m - wyswiela mape, h - wyswietla liste komend")
    komenda = input("Co chcesz zrobic? ")

    if komenda == "h" or komenda == "help":
        pokaz_pomoc()
    elif komenda == "g":
        poruszanie_sie(komenda)
    elif komenda == "d":
        poruszanie_sie(komenda)
    elif komenda == "p":
        poruszanie_sie(komenda)
    elif komenda == "l":
        poruszanie_sie(komenda)
    elif komenda == "q":
        wczytaj_quest(pozycja)
    elif komenda == "s":
        otworz_skrzynke(pozycja)
    elif komenda == "e":
        exit()
    elif komenda == "m" or komenda == "mapa":
        rysuj_mape()
    elif komenda == "gwiazdki":
        sprawdz_gwiazdki()
    else:
        print ("Wpisz 'help' aby wyswietlic pomoc ")

    komendy()
    return;


#   questy tutaj:


#quest obliczania miejsca zerowego funkcji kwadratowej
def f_kwadratowa():
    global wydarzenia_na_mapie
    global status_gwiazdek

    #imersja
    print ("W pokoju widzisz starego matematyka:")
    print ("'Dostaniesz ode mnie gwiazdke jesli poprawnie odpowiesz na moje pytanie")
    print ("Przygotuj sie...")
    sleep(6)

    #losowanie parametrow funkcji
    a = randint(-30, -1)
    b = randint(1, 20)
    c = randint(1, 50)

    #imersja
    print ("Podaj prosze miejsca zerowe tej oto funkcji:")
    print ("f(x) = " + str(a) + "x^2 +" + str(b) + "x +" + str(c))
    print ("Pamietaj o uzywaniu kropki a nie przecinka, wynik nalezy zaokraglic do 2 miejsc po przecinku")
    sleep(10)

    #wyznaczanie miejsc zerowych
    delta = (b * b) - (4 * a * c)
    x1 = (- b - sqrt(delta)) / (2 * a)
    x2 = (- b + sqrt(delta)) / (2 * a)

    #zaokraglenie do 2 miejsc po przecinku
    x1 = round(x1, 2)
    x1 = float(x1)
    x2 = round(x2, 2)
    x2 = float(x2)


    #wczytanie odpowiedzi gracza (dopuszczamy tylko typ float)
    while True:
        try:
            odpowiedz_1 = float(input("Pierwsze miejsce zerowe: "))
            break
        except:
            print ("Podaj wynik w poprawnym formacie")

    while True:
        try:
            odpowiedz_2 = float(input("Drugie miejsce zerowe: "))
            break
        except:
            print ("Podaj wynik w poprawnym formacie")

    print ("Uhhh niech pomysle...")
    sleep(2)

    #okreslenie poprawnosci odpowiedzi (uwzgledniajac kolejnosc wynikow)
    if (str(x1) == str(odpowiedz_1) and str(x2) == str(odpowiedz_2)) or (str(x1) == str(odpowiedz_2) and str(x2) == str(odpowiedz_1)):
        print("Zdaje sie, ze odpowiedziales poprawnie! Prosze, oto Twoja gwiazdka")
        status_gwiazdek += 1
        pokojW[9][5] = " "
        wydarzenia_na_mapie -= 1
    else:
        print("Chyba zartujesz! To nie sa poprawne wyniki")

    sprawdz_gwiazdki()

    return;


#zadanie z losowaniem pudelek
def losuj_pudelko():
    global wydarzenia_na_mapie
    global status_gwiazdek

    #czyscimy Q z mapy
    pokojN[5][1] = " "

    #losujemy ile gwiazdek znajdzie sie w wybranym pudelku
    gwiazdki = randint(-1,2)
    #losujemy ilosc pudelek od 3 do 6
    ilosc_pudelek = randint(3,6)

    #wazna jest w jezyku poprawnosc, ten warunek to okresli
    if ilosc_pudelek == 3 or ilosc_pudelek == 4:
        print ("W pokoju widzisz "  + str(ilosc_pudelek) + " pudelka, ktore wybierasz?")
    else:
        print ("W pokoju widzisz "  + str(ilosc_pudelek) + " pudelek, ktore wybierasz?")

    #gracz wybiera pudelko, ktore chce otworzyc, petla dopuszcza tylko wartosci typu int
    while True:
        try:
            wybor_gracza = int(input("Wpisz jego numer: "))
            break
        except:
            print("Wpisz liczbe!")

    #sprawdzamy czy gracz wybral poprawnie pudelko ktore chce otworzyc
    while wybor_gracza < 1 or wybor_gracza > ilosc_pudelek:
        while True:
            try:
                wybor_gracza = int(input("Wpisales nieprawidlowy numer pudelka, sprobuj ponownie: "))
                break
            except:
                print("Wpisz liczbe!")

    #immersja
    sleep(2)
    print ("Wybrales "+ str(wybor_gracza) + " pudelko, widzisz jak pozostale pudelka chowaja sie pod podloga")
    sleep(3)
    print ("Otwierasz pudelko, a w srodku: ")
    sleep(2)
    #koniec immersji

    #opis co sie wydarzylo, stracilismy gwiazdke
    if gwiazdki == -1:
        if status_gwiazdek <= 0:
            print ("Pudelko jest puste")
        else:
            print ("Coz za pech, pudelko okazalo sie pulapka! Tracisz gwiazdke")
            #"dodanie" wartosci uzyskanej gwiazdki do ogolnego stanu ich posiadania
            status_gwiazdek -= 1

    #opis co sie wydarzylo, puste pudelko
    elif gwiazdki == 0:
        print ("Pudelko jest puste")

    #opis co sie wydarzylo, dostalismy gwiazdke
    elif gwiazdki == 1:
        print ("Znajdujesz jedna gwiazdke, gratulacje!")
        #dodanie wartosci uzyskanych gwiazdek do ogolnego stanu ich posiadania
        status_gwiazdek +=1

    #opis co sie wydarzylo, dostalismy 2 gwiazdki
    elif gwiazdki == 2:
        print ("Znajdujesz dwie gwiazdki, niesamowite!")
        #dodanie wartosci uzyskanych gwiazdek do ogolnego stanu ich posiadania
        status_gwiazdek +=2
    else:
        print ("Cos jest nie tak")

    wydarzenia_na_mapie -= 1
    sprawdz_gwiazdki()

    return;


#zadanie z zamianda dziesietnego na binarny
def zamiana_na_binarny():
    global wydarzenia_na_mapie
    global status_gwiazdek

    print ("W pokoju spotykasz profesora, widzisz ze w reku trzyma gwiazdke")
    sleep(1)
    print ("- Co moge zrobic aby ja dostac?")
    sleep(2)
    print ("- Hmm, mam dla Ciebie zadanie, ale nie wiem czy podołasz...")
    sleep(2)
    print ("Podam Ci trzy losowo generowane liczby. Aby udowodnic, ze jestes godzien tej gwiazdki ")
    print ("zamienisz je na system binarny.")


    #liczymy ile razy pytanie zostalo zadane
    licznik = 0

    #petla nalicza pytania do max 3
    while licznik < 3:

        #losujemy liczbe
        liczba = randint(33, 255)

        #zamieniamy na wartosc binarna
        binarna = bin(liczba)
        #ucinamy pierwsze dwa znaki, bo bin() generuje zmiena w formacie 0b1010101
        binarna = binarna[2:]

        #pokazujemy liczbe o ktora pytamy
        print ("Liczba to: " + str(liczba))

        #wczytujemy odpowiedz gracza
        odpowiedz = input("Jej wartosc w systemie binarnym: ")

        #dla dwoch pierwszych poprawnych odpowiedzi
        if odpowiedz == binarna and licznik < 2:
            print ("Odpowiedzales poprawnie, przygotuj sie na nastepna liczbe")
            sleep(2)

        #dla trzeciej odpowiedzi, jesli jest poprawna
        elif odpowiedz == binarna:
            print ("Odpowiedzales poprawnie")

            #gracz odpowiedzial poprawnie wiec dodajemy gwiazdke
            status_gwiazdek += 1
            #i czyscimy questa z mapy
            pokojSW[1][5] = " "
            wydarzenia_na_mapie -= 1

        #jesli odpowiedz jest bledna
        else:
            print ("To nie jest poprawna wartosc binarna tej liczby!")
            print ("Poprawna wartosc: " + str(binarna))
            sleep(2)
            print ("Wroc wykonac zadanie kiedy przypomnisz sobie jak wykonuje sie taka konwersje")
            sleep(3)
            #przerywamy questa
            break

        licznik += 1

    sprawdz_gwiazdki()
    return;


#zadanie ze zgadywaniem losowo generowanej liczby
def losowanie_liczby():
    global wydarzenia_na_mapie
    global status_gwiazdek

    #losujemy liczby, odpowiednio dla poczatku i konca przedzialu
    przedzial_pocz = randint(0, 100)
    przedzial_konc = randint(0, 1000)

    #chcemy zeby przedzial koncowy byl wiekszy od poczatkowego
    while przedzial_konc < przedzial_pocz:
        przedzial_konc = randint(0, 1000)

    #z wylosowanego przedzialu losujemy liczbe
    liczba_wylosowana = randint(przedzial_pocz, przedzial_konc)




    #immersja, tlumaczymy zasady
    print ("W pokoju widzisz starca, on widzac Cie mowi: ")
    sleep(1)
    print ("Zgaduje, ze znalazles sie tutaj w poszukiwaniu gwiazdek,")
    sleep(1)
    print ("Jezeli z przedzialu (" + str(przedzial_pocz) + " ; " + str(przedzial_konc) + ") odgadniesz wybrana przeze mnie liczbe dostaniesz gwiazdke")
    sleep(1)
    print ("Bedziesz mial na to zadanie minute")
    sleep(0.5)
    print ("Jezeli podasz liczbe wieksza od wybranej, to powiadomie Cie, ze liczba ta jest zbyt duza")
    sleep(0.5)
    print ("Jezeli podasz liczbe mniejsza od wybranej, to powiadomie Cie, ze liczba ta jest zbyt mala")
    sleep(0.5)
    print ("Jezeli odgadniesz liczbe to dostaniesz gwiazdke")
    sleep(0.5)
    print ("Jezeli skonczy Ci sie czas to stracisz gwiazdke, jezeli jakakolwiek masz")
    sleep(2)

    #gracz gdy jest gotowy, wpisuje tak, dodatkowo nie ma znaczenia czy slowo tak napisze wielkimi literami czy malymi
    gotowosc = str(input("Czy jestes juz gotowy?(tak): ")).lower()

    #sprawdzamy czy gracz nie napisal czegos innego niz tak
    while gotowosc != "tak":
        print ("Nie jest to poprawna forma, wprowadz ja jeszcze raz")
        gotowosc = str(input("Czy jestes juz gotowy?(tak): ")).lower()
    else:
        #informujemy gracza ze zadanie sie rozpoczyna
        print ("To zaczynamy, czas start")


    #wymuszamy typ int
    while True:
        try:
            liczba_uzytkownika = int(input("Podaj liczbe z przedzialu (" + str(przedzial_pocz) + " ; " + str(przedzial_konc) + ")"))
            break
        except:
            print("Wpisz poprawnie!")

    #zaczynamy liczyc czas
    start = time()

    #sprawdzamy warunek dopoki liczba wybrana przez uzytkownika nie bedzie rowna liczbie wylosowanej
    while liczba_uzytkownika!=liczba_wylosowana:

        #dodatkowo sprawdzamy czy nie skonczyl sie czas
        if time() - start > 60:
            print ("Skonczyl Ci sie czas! Zawiodles!")
            break

        #sprawdzamy czy uzytkownik podaje liczbe z zakresu
        elif liczba_uzytkownika < przedzial_pocz or liczba_uzytkownika > przedzial_konc:
            #wymuszamy typ int
            while True:
                try:
                    liczba_uzytkownika = int(input("Liczba nie pasuje do przedzialu (" + str(przedzial_pocz) + " ; " + str(przedzial_konc) +  "), podaj ja jeszcze raz: "))
                    break
                except:
                    print("Wpisz poprawnie!")

        #sprawdzamy czy gracz podal liczbe za duza lub za mala
        elif liczba_uzytkownika > liczba_wylosowana:
            #wymuszamy typ int
            while True:
                try:
                    liczba_uzytkownika = int(input("Twoja liczba jest za duza (" + str(przedzial_pocz) + " ; " + str(przedzial_konc) +  "), podaj ja jeszcze raz: "))
                    break
                except:
                    print("Wpisz poprawnie!")

        elif liczba_uzytkownika < liczba_wylosowana:
            #wymuszamy typ int
            while True:
                try:
                    liczba_uzytkownika = int(input("Twoja liczba jest za mala (" + str(przedzial_pocz) + " ; " + str(przedzial_konc) +  "), podaj ja jeszcze raz: "))
                    break
                except:
                    print("Wpisz poprawnie!")

    #jezeli graczowi sie powiedzie dostaje gwiazdke
    if liczba_uzytkownika == liczba_wylosowana:
            print ("Brawo, odgadles moja liczbe, otrzymujesz gwiazdke!")
            status_gwiazdek += 1

            #w przypadku wygranej usuwamy questa z mapy
            pokojS[5][9] = " "
            wydarzenia_na_mapie -= 1

    sprawdz_gwiazdki()
    return;


#zadanie ze sprawdzianem ABCD
def test_abcd():

    #ta funkcja wczytuje odpowiedz gracza i sprawdza czy nie jest ona typem int
    def walidacja_odpowiedzi():

        #dopuszcza tylko odpowiedzi a, b, c, d
        while True:
            #wczytaj odpowiedz
            odpowiedz = input("Poprawna odpowiedz: ")
            #jesli jest typem string...
            if odpowiedz.isalpha():
                #... o dlugosci 1...
                if len(odpowiedz) == 1:
                    #...z przedzialu a-d
                    if ord(odpowiedz) >= 97 and ord(odpowiedz) <= 100:
                        break
            #jesli jest niepoprawne to petla wykonuje sie ponownie
            print ("Wpisz litere z przedzialu a - d!")

        #zamieniamy wartosc z litery na jej odpowiednik typu int
        odpowiedz = ord(odpowiedz)
        #usuwamy wartosci tablicyu ASCII i wracamy do przedzialu od 0 do 1
        odpowiedz = odpowiedz - 97

        #funkcja zwraca odpowiedz gracza
        return odpowiedz;

    global wydarzenia_na_mapie
    global status_gwiazdek

    print ("Widzisz przed soba stolik, a na nim krotki sprawdzian")
    print ("\"Odpowiedz poprawnie na minimum 2 pytania a otrzymasz jedna gwiazdke\"")
    sleep(2)

    #tworzmy tablice z pytaniami
    pytanie_1 = ["(a+b) / 2", "(a*h) / 2", "(a+b)*h / 2", "(a*b) / h"]
    pytanie_2 = ["Wolt", "Wat", "Amper", "Ohm"]
    pytanie_3 = ["996", "966", "969", "696"]
    pytanie_4 = ["64", "10", "16", "24"]

    #zapamietujemy ktore indexy to poprawne odpowiedzi
    poprawne_1 = pytanie_1[2]
    poprawne_2 = pytanie_2[0]
    poprawne_3 = pytanie_3[1]
    poprawne_4 = pytanie_4[3]

    #mieszamy odpowiedzi
    shuffle(pytanie_1)
    shuffle(pytanie_2)
    shuffle(pytanie_3)
    shuffle(pytanie_4)

    #po wymieszaniu odpowiedzi trzeba znalezc indeksy poprawnych odpowiedzi i na nowo przypisac je do zmiennych
    for x in range(len(pytanie_1)):
        if poprawne_1 == pytanie_1[x]:
            poprawne_1 = x
    for x in range(len(pytanie_2)):
        if poprawne_2 == pytanie_2[x]:
            poprawne_2 = x
    for x in range(len(pytanie_3)):
        if poprawne_3 == pytanie_3[x]:
            poprawne_3 = x
    for x in range(len(pytanie_4)):
        if poprawne_4 == pytanie_4[x]:
            poprawne_4 = x

    #sluzy do zmiany literki przed odpowiedzia, w ASCII 97 to 'a'
    #zmienna wykorzystywana w petlach for ponizej
    litera = 97

    #zliczamy ilosc poprawnych odpowiedzi
    licznik = 0

    #pytanie 1
    sleep(1)
    print ("1. Wzor na pole trapezu to: ")
    sleep(1)

    #wyswietlamy a, b, c, d
    for x in range(len(pytanie_1)):
        #drukujemy kolejne litery zaczynajac od 'a' i tresc
        sleep(1)
        print (chr(litera) + ") " + pytanie_1[x])
        #inkrementacja, w nastepnym wykonaniu petli chcemy kolejna litere
        litera += 1
    litera -= 4
    #sprawdzamy odpowiedz

    if poprawne_1 == walidacja_odpowiedzi():
        #doliczamy punkt za poprawna odpowiedz
        licznik += 1

    #pytanie 2
    sleep(1)
    print ("2. Jednostka napiecia elektrycznego jest: ")
    sleep(1)

    #wyswietlamy a, b, c, d
    for x in range(len(pytanie_2)):
        #drukujemy kolejne litery zaczynajac od 'a' i tresc
        sleep(1)
        print (chr(litera) + ") " + pytanie_2[x])
        #inkrementacja, w nastepnym wykonaniu petli chcemy kolejna litere
        litera += 1
    litera -= 4

    if poprawne_2 == walidacja_odpowiedzi():
        #doliczamy punkt za poprawna odpowiedz
        licznik += 1

    #pytanie 3
    sleep(1)
    print ("3. Przyjmuje sie, ze Chrzest Polski byl w roku: ")
    sleep(1)

    #wyswietlamy a, b, c, d
    for x in range(len(pytanie_3)):
        #drukujemy kolejne litery zaczynajac od 'a' i tresc
        sleep(1)
        print (chr(litera) + ") " + pytanie_3[x])
        #inkrementacja, w nastepnym wykonaniu petli chcemy kolejna litere
        litera += 1
    litera -= 4

    if poprawne_3 == walidacja_odpowiedzi():
        #doliczamy punkt za poprawna odpowiedz
        licznik += 1

    #pytanie 4
    sleep(1)
    print ("4. Wskaz poprawny wynik. 4! = ")
    sleep(1)

    #wyswietlamy a, b, c, d
    for x in range(len(pytanie_4)):
        #drukujemy kolejne litery zaczynajac od 'a' i tresc
        sleep(1)
        print (chr(litera) + ") " + pytanie_4[x])
        #inkrementacja, w nastepnym wykonaniu petli chcemy kolejna litere
        litera += 1
    litera -= 4

    if poprawne_4 == walidacja_odpowiedzi():
        #doliczamy punkt za poprawna odpowiedz
        licznik += 1

    #sprawdzamy ilosc poprawnych odpowiedzi
    if licznik >= 2:
        print ("Gratulacje! Odpowiedziales poprawnie na " + str(licznik) + " pytania")
        print ("Prosze, oto Twoja gwiazdka")
        status_gwiazdek += 1
        pokojE[5][9] = " "
        wydarzenia_na_mapie -= 1
    else:
        print ("Niestety, udzieliles zbyt malo poprawnych odpowiedzi. Sprobuj ponownie!")

    sprawdz_gwiazdki()
    return;


#zadanie z testem tak/nie
def piec_pytan():
    global status_gwiazdek
    global wydarzenia_na_mapie
    odpowiedzi_prawidlowe = 0
    #immersja
    print ("Wchodzac do pokoju widzisz stol z monitorem oraz dwoma dosc sporymi guzikami, jeden jest czerwony z napisem nie, drugi jest zielony z napisem tak.")
    sleep(1)
    print ("Podchodzac blizej do stolika zapala sie ekran tego monitora i zaczyna byc wypisywana nastepujaca wiadomosc:")
    sleep(1)
    print ("        Witaj lowco gwiazd, jezeli wykonasz dla mnie pewne zadanie dostaniesz gwiazdke.")
    sleep(1)
    print ("        Twoim zadaniem bedzie odpowiedzenie na 5 pytan z wybranej przez siebie dziedziny")
    sleep(1)
    print ("        Wystarczy, ze odpowiesz poprawnie na 3 z nich. Pytania beda w formacie TAK lub NIE")
    sleep(1)
    print ("        Zestaw pytan mozesz wybrac z nastepujacych dziedzin:")
    print ("            -Matematyka")
    print ("            -Informatyka")
    print ("            -Fizyka")
    print ("            -Historia")
    sleep(1)
    #koniec immersji

    #sprawdzamy jaka dziedzine gracz wybral i czy zrobil to poprawnie
    wybrana_dziedzina = str(input("Ktora dziedzine wybierasz?: (wpisz slownie)")).lower()
    while wybrana_dziedzina != "matematyka" and wybrana_dziedzina != "informatyka" and wybrana_dziedzina != "fizyka" and wybrana_dziedzina != "historia":
        wybrana_dziedzina = str(input("Wpisz poprawnie ktora wybierasz dziedzine: ")).lower()

    #potrzebna nam jest tablica z pytaniami z kazdej dziedziny
    pytania_matematyka = ["Calka nieoznaczona z 1 rowna jest x",
    "Dodawanie i mnozenie jest przemienne",
    "Implikacja Falszu w Prawde to Prawda",
    "Granica funkcji moze byc liczona w dowolnym punkcie funkcji",
    "System dwojkowy sklada sie z liczb 0, 1 , 2"]

    pytania_informatyka = ["Command Prompt to tzw. cmd",
    "Plyta glowna sluzy do przechowywania danych",
    "Pierwsza konsola do gier wideo bylo Atari PONG",
    "Znak @ pochodzi z laciny",
    "Darmowym oprogramowanie bedzie oprogramowanie typu shareware"]

    pytania_fizyka = ["Predkosc jaka musi osiagnac rakieta zeby osiagnac przestrzen kosmiczna zalezy od jej masy",
    "Interferencja fal to zjawisko pojawiajace sie przy pochlanianiu fal",
    "Refraktometer sluzy do pomiaru zalamania swiatla",
    "Woda wrze zawsze w temperaturze 100 stopni Celsjusza",
    "We wzorze E=mc^2, 'c' oznacza ladunek elektryczny"]

    pytania_historia = ["W legendach arturianskich nazwa zamku w ktorym zamieszkiwal Krol Artur to Lancelot",
    "Najczescie uzywana bronia przez wikingow byly topory",
    "Mieszko I nie byl pierwszym krolem polski",
    "John F. Kennedy byl prezydentem USA przez 1036 dni",
    "Veni, vidi, vici to slynne slowa Juliusza Cezara"]

    #wybieramy dziedzine
    if wybrana_dziedzina == "matematyka":
        #gracz wybral dziedzine matematyki
        sleep(1)
        print ("Wybrales dziedzine matematyki, zaczynajmy!")
        sleep(2)

        #potrzebujemy funkcje dla kazdego pytania gdzie gracz bedzie wybieral odpowiedz tak/nie

        def pytanie_a():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_matematyka[0])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "nie":
                odpowiedzi_prawidlowe += 1

        def pytanie_b():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_matematyka[1])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "tak":
                odpowiedzi_prawidlowe += 1

        def pytanie_c():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_matematyka[2])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "tak":
                odpowiedzi_prawidlowe += 1

        def pytanie_d():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_matematyka[3])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "nie":
                odpowiedzi_prawidlowe += 1

        def pytanie_e():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_matematyka[4])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "nie":
                odpowiedzi_prawidlowe += 1

        #"wrzucamy" funkcje do tablicy w celu pozniejszego wylosowania konkretnej funckji dla pytania 1, 2, ..., 5
        funkcje = [pytanie_a, pytanie_b, pytanie_c, pytanie_d, pytanie_e]

        #petla dziala dopoki tablica posiada jakiekolwiek elementy
        while funkcje:
            #losujemy 1 funkcje z tablicy
            losowanie_funkcji = choice(funkcje)
            #usuwamy ta wylosowana funkcje z tablicy zeby jej ponownie nie wylosowac
            funkcje.remove(losowanie_funkcji)
            #wywolujemy wylosowana funkcje
            losowanie_funkcji()
            sleep(0.5)

        #jezeli gracz wygra to dostaje gwiazdke, w przeciwnym wypadku dostaje komunikat ze przegral
        if odpowiedzi_prawidlowe >= 3:
            status_gwiazdek += 1
            pokojNE[5][9] = " "
            wydarzenia_na_mapie -= 1
            print ("Gratulacje, udalo Ci sie wykonac zadanie, otrzymujesz gwiazdke!")
        else:
            print ("Nie udalo Ci sie wykonac mojego zadania!")

    #analogicznie do wybrania matematyki
    elif wybrana_dziedzina == "informatyka":
        sleep(1)
        print ("Wybrales dziedzine informatyki, zaczynajmy!")
        sleep(2)

        def pytanie_a():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_informatyka[0])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "tak":
                odpowiedzi_prawidlowe += 1

        def pytanie_b():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_informatyka[1])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "nie":
                odpowiedzi_prawidlowe += 1

        def pytanie_c():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_informatyka[2])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "nie":
                odpowiedzi_prawidlowe += 1

        def pytanie_d():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_informatyka[3])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "tak":
                odpowiedzi_prawidlowe += 1

        def pytanie_e():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_informatyka[4])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "nie":
                odpowiedzi_prawidlowe += 1

        funkcje = [pytanie_a, pytanie_b, pytanie_c, pytanie_d, pytanie_e]
        while funkcje:
            losowanie_funkcji = choice(funkcje)
            funkcje.remove(losowanie_funkcji)
            losowanie_funkcji()
            sleep(0.5)
        if odpowiedzi_prawidlowe >= 3:
            status_gwiazdek += 1
            pokojNE[5][9] = " "
            wydarzenia_na_mapie -= 1
            print ("Gratulacje, udalo Ci sie wykonac zadanie, otrzymujesz gwiazdke!")
        else:
            print ("Nie udalo Ci sie wykonac mojego zadania!")

    #analogicznie do wybrania matematyki
    elif wybrana_dziedzina == "fizyka":
        sleep(1)
        print ("Wybrales dziedzine fizyki, zaczynajmy!")
        sleep(2)

        def pytanie_a():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_fizyka[0])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "nie":
                odpowiedzi_prawidlowe += 1

        def pytanie_b():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_fizyka[1])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "nie":
                odpowiedzi_prawidlowe += 1

        def pytanie_c():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_fizyka[2])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "tak":
                odpowiedzi_prawidlowe += 1

        def pytanie_d():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_fizyka[3])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "nie":
                odpowiedzi_prawidlowe += 1

        def pytanie_e():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_fizyka[4])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "nie":
                odpowiedzi_prawidlowe += 1

        funkcje = [pytanie_a, pytanie_b, pytanie_c, pytanie_d, pytanie_e]
        while funkcje:
            losowanie_funkcji = choice(funkcje)
            funkcje.remove(losowanie_funkcji)
            losowanie_funkcji()
            sleep(0.5)
        if odpowiedzi_prawidlowe >= 3:
            status_gwiazdek += 1
            pokojNE[5][9] = " "
            wydarzenia_na_mapie -= 1
            print ("Gratulacje, udalo Ci sie wykonac zadanie, otrzymujesz gwiazdke!")
        else:
            print ("Nie udalo Ci sie wykonac mojego zadania!")

    #analogicznie do wybrania matematyki
    elif wybrana_dziedzina == "historia":
        sleep(1)
        print ("Wybrales dziedzine historii, zaczynajmy!")
        sleep(2)

        def pytanie_a():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_historia[0])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "nie":
                odpowiedzi_prawidlowe += 1

        def pytanie_b():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_historia[1])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "tak":
                odpowiedzi_prawidlowe += 1

        def pytanie_c():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_historia[2])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "tak":
                odpowiedzi_prawidlowe += 1

        def pytanie_d():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_historia[3])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "tak":
                odpowiedzi_prawidlowe += 1

        def pytanie_e():
            nonlocal odpowiedzi_prawidlowe
            print (pytania_historia[4])
            odpowiedz = str(input("Podaj swoja odpowiedz (TAK/NIE):")).lower()
            while odpowiedz != "tak" and odpowiedz != "nie":
                odpowiedz = str(input("Poprawnie podaj swoja odpowiedz (TAK/NIE):")).lower()
            if odpowiedz == "tak":
                odpowiedzi_prawidlowe += 1

        funkcje = [pytanie_a, pytanie_b, pytanie_c, pytanie_d, pytanie_e]
        while funkcje:
            losowanie_funkcji = choice(funkcje)
            funkcje.remove(losowanie_funkcji)
            losowanie_funkcji()
            sleep(0.5)
        if odpowiedzi_prawidlowe >= 3:
            status_gwiazdek += 1
            pokojNE[5][9] = " "
            wydarzenia_na_mapie -= 1
            print ("Gratulacje, udalo Ci sie wykonac zadanie, otrzymujesz gwiazdke!")
        else:
            print ("Nie udalo Ci sie wykonac mojego zadania!")

    sprawdz_gwiazdki()
    return;


#tworzenie scian i innych elementow otoczenia:
utworz_sciany()

#pierwsze wyrysowanie mapy:
#wylaczone z powodu natloku informacji przy pierwszym uruchomieniu gry
#rysuj_mape()

#oczekiwanie na pierwsza komende gracza:
komendy()
