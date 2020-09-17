from OperacjeUjednolicaniaObrazów import UjednolicenieObrazow
from OperacjeArytmetyczneNaObrazachSzarych import OperacjeArytmetyczneSzare
from OperacjeArytmetyczneNaObrazachBarwowych import  OperacjeArytmetyczneKolor
from OperacjeGeometryczneNaObrazie import OperacjeGeometryczne
import numpy as np

from PIL import Image
a=1


print("Proszę najpierw wpisać numer zadania a następnie numer podpunktu danego zadania")
print("Aby zakończyć działanie programu wpisz 0")

while(a>=1):
    print("\nZadanie 1 Operacje ujednolicania obrazów:")
    print("\n 1. Ujednolicenie obrazów szarych geometryczne"
          "\n 2. Ujednolicenie obrazów szarych roździelczościowe"
          "\n 3. Ujednolicenie obrazów RGB geometryczne"
          "\n 4. Ujednolicenie obrazów RGB rodzielczościowe")
    print("\nZadanie 2 Operacje arytmetyczne na obrazach szarych:")
    print("\n 1. Sumowanie liczby z obrazem"
          "\n 2. Sumowanie dwóch obrazów"
          "\n 3. Mnozenie obrazu przez liczbe"
          "\n 4. Mnozenie dwóch obrazów"
          "\n 5. Mieszanie obrazów z współczynnikiem"
          "\n 6. Potęgowanie obrazu"
          "\n 7. Dzielenie obrazu przez liczbe"
          "\n 8. Dzielenie obrazu przez obraz"
          "\n 9. Pierwiastkowanie obrazu"
          "\n 10. Logarytmowanie obrazu")
    print("\nZadanie 3 Operacje arytmetyczne na obrazach barwowych:")
    print("\n 1. Sumowanie liczby z obrazem""\n 2. Sumowanie dwóch obrazów"
          "\n 3. Mnozenie obrazu przez liczbe"
          "\n 4. Mnozenie dwóch obrazów"
          "\n 5. Mieszanie obrazów z współczynnikiem"
          "\n 6. Potęgowanie obrazu"
          "\n 7. Dzielenie obrazu przez liczbe"
          "\n 8. Dzielenie obrazu przez obraz"
          "\n 9. Pierwiastkowanie obrazu"
          "\n 10. Logarytmowanie obrazu")
    print("\nZadanie 4 Operacje geometryczne na obrazie:")
    print("\n 1. Przemieszcznie obrazu o wektor"
          "\n 2. Jednorodne skalowanie obrazu"
          "\n 3. Niejednorodne skalowanie obrazu"
          "\n 4. Obracanie obrazu o dowolny kąt"
          "\n 5. Symetria wzgledem osi X"
          "\n 6. Symetria względem osi Y"
          "\n 7. Symetria względem zadanej na osi X"
          "\n 8. Symetira względem zadanej na osi Y"
          "\n 9. Wycinanie fragmentow obrazu"
          "\n 10. Kopiowanie fragmentów obrazu")
    print("\nPodaj numer zadania")
    sector=input()

    if int(sector) == 0:
        print("\nKoniec działania")
        break

    print("Teraz podaj numer podpunktu")
    excer=input()

    if int(sector)==1:
        if int(excer) == 0:
            print("\nKoniec działania programu")
            break
        Zad1 = UjednolicenieObrazow()

        if int(excer)==1:
            N=1
            img1 = Image.open("obrazy/warzywa256.bmp")
            img2 = Image.open("obrazy/warzywa512.bmp")
            Zad1.Geometryczne(img1, img2, N)

            N=2
            img1 = Image.open("obrazy/womann256.bmp")
            img2 = Image.open("obrazy/womann512.bmp")
            Zad1.Geometryczne(img1, img2, N)

        if int(excer)==2:
            N=1
            img1 = Image.open("obrazy/houseee512.bmp")
            img2 = Image.open("obrazy/houseee256.bmp")
            Zad1.Rozdzielczosciowe(img1, img2, N)

            N=2
            img1 = Image.open("obrazy/parots512.bmp")
            img2 = Image.open("obrazy/parots256.bmp")
            Zad1.Rozdzielczosciowe(img1, img2, N)

        if int(excer)==3:
            N=1
            img1 = Image.open("obrazy/shreksmile256.bmp")
            img2 = Image.open("obrazy/shreksmile512.bmp")
            Zad1.GeometryczneRGB(img1, img2, N)

            N=2
            img1 = Image.open("obrazy/shrek256.bmp")
            img2 = Image.open("obrazy/shrek512.bmp")
            Zad1.GeometryczneRGB(img1, img2, N)

        if int(excer)==4:
            N=1
            img1 = Image.open("obrazy/moto512.bmp")
            img2 = Image.open("obrazy/moto256.bmp")
            Zad1.RozdzielczoscioweRGB(img1, img2, N)

            N=2
            img1 = Image.open("obrazy/ducati512.bmp")
            img2 = Image.open("obrazy/ducati256.bmp")
            Zad1.RozdzielczoscioweRGB(img1, img2, N)

        else:
            print("Nieprawidlowy numer podpunktu")

    if int(sector) == 2:
        if int(excer) == 0:
            print("\nKoniec działania programu")
            break
        Zad2 = OperacjeArytmetyczneSzare()

        if int(excer)==1:
            N=1
            print("Podaj wartosc ktora zsumowac z obrazem")
            val=input()
            img1 = Image.open("obrazy/duck512.bmp")
            Zad2.sumowaniePrzezStala(img1, int(val), N)

            N=2
            print("Podaj wartosc ktora chcesz zsumowac z obrazem")
            val = input()
            img1 = Image.open("obrazy/warzywa512.bmp")
            Zad2.sumowaniePrzezStala(img1, int(val), N)

        if int(excer)==2:
            N=1
            img1 = Image.open("obrazy/Bear512.bmp")
            img2 = Image.open("obrazy/rys512.bmp")
            Zad2.sumowanieObrazow(img1, img2, N)

            N=2
            img1 = Image.open("obrazy/rys512.bmp")
            img2 = Image.open("obrazy/dogo512.bmp")
            Zad2.sumowanieObrazow(img1, img2, N)

        if int(excer)==3:
            N=1
            print("Podaj wartosc przez ktora chcesz pomnozyc obraz")
            val = input()
            img1 = Image.open("obrazy/rys512.bmp")
            Zad2.obrazMnozenie(img1, int(val), N)

            N=2
            print("Podaj wartosc przez ktora chcesz pomnozyc obraz")
            val = input()
            img1 = Image.open("obrazy/womann512.bmp")
            Zad2.obrazMnozenie(img1, int(val), N)

        if int(excer)==4:
            N=1
            img1 = Image.open("obrazy/epep512.bmp")
            img2 = Image.open("obrazy/rys512.bmp")
            Zad2.mnozenieObraz(img1, img2, N)

            N=2
            img1 = Image.open("obrazy/owl512.bmp")
            img2 = Image.open("obrazy/house512.bmp")
            Zad2.mnozenieObraz(img1, img2, N)

        if int(excer)==5:
            N=1
            print("Podaj wartosc wspolczynnika")
            val = input()

            img1 = Image.open("obrazy/lighthouse512.bmp")
            img2 = Image.open("obrazy/house512.bmp")
            Zad2.mieszanieObrazow(img1, img2, N)

            N=2
            print("Podaj wartosc wspolczynnika")
            val = input()
            img1 = Image.open("obrazy/duck512.bmp")
            img2 = Image.open("obrazy/city512.bmp")
            Zad2.mieszanieObrazow(img1, img2, N)

        if int(excer)==6:
            N=1
            print("Podaj wartosc przez ktora chcesz pomnozyc obraz")
            val = input()
            img1 = Image.open("obrazy/cat512.bmp")
            Zad2.potegowanieObrazow(img1, int(val), N)

            N=2
            print("Podaj wartosc przez ktora chcesz pomnozyc obraz")
            val = input()
            img1 = Image.open("obrazy/cityy512.bmp")
            Zad2.potegowanieObrazow(img1, int(val), N)

        if int(excer)==7:
            N=1
            print("Podaj wartosc przez ktora chcesz podzielic obraz")
            val = input()
            img1 = Image.open("obrazy/owl512.bmp")
            Zad2.dzielenieObrazu(img1, int(val), N)

            N=2
            print("Podaj wartosc przez ktora chcesz podzielic obraz")
            val = input()
            img1 = Image.open("obrazy/city512.bmp")
            Zad2.dzielenieObrazu(img1, int(val), N)

        if int(excer)==8:
            N=1
            img1 = Image.open("obrazy/bear512.bmp")
            img2 = Image.open("obrazy/lion512.bmp")
            Zad2.dzielenieObrazObraz(img1, img2, N)

            N=2
            img1 = Image.open("obrazy/volvo512.bmp")
            img2 = Image.open("obrazy/ducati512.bmp")
            Zad2.dzielenieObrazObraz(img1, img2, N)

        if int(excer)==9:
            N=1
            img1 = Image.open("obrazy/womann512.bmp")
            Zad2.pierwiastkowanieObrazow(img1, N)

            N=2
            img1 = Image.open("obrazy/owl512.bmp")
            Zad2.pierwiastkowanieObrazow(img1, N)

        if int(excer)==10:
            N=1
            img1 = Image.open("obrazy/rys512.bmp")
            Zad2.logarytmowanieObrazu(img1, N)

            N=2
            img1 = Image.open("obrazy/duck512.bmp")
            Zad2.logarytmowanieObrazu(img1, N)

        else:
             print("Podales nieprawidlowy numer podpunktu, sprobuj ponownie!")

    if int(sector) == 3:
        if int(excer) == 0:
            print("\nKoniec działania programu")
            break
        Zad3 = OperacjeArytmetyczneKolor()

        if int(excer)==1:
            N=1
            print("Podaj wartosc ktora chcesz zsumowac z obrazem")
            val = input()
            img1 = Image.open("obrazy/ducati512.bmp")
            Zad3.sumowanie(img1, int(val), N)

            N=2
            print("Podaj wartosc ktora chcesz zsumowac z obrazem")
            val = input()
            img1 = Image.open("obrazy/backcar512.bmp")
            Zad3.sumowanie(img1, int(val), N)

        if int(excer)==2:
            N=1
            img1 = Image.open("obrazy/ducati256.bmp")
            img2 = Image.open("obrazy/BMW512.bmp")
            Zad3.sumowanieObrazow(img1, img2, N)

            N=2
            img1 = Image.open("obrazy/512x512bb.bmp")
            img2 = Image.open("obrazy/monkey512.bmp")
            Zad3.sumowanieObrazow(img1, img2, N)

        if int(excer)==3:
            N=1
            print("Podaj wartosc przez ktora chcesz pomnozyc obraz")
            val = input()
            img1 = Image.open("obrazy/warzywa512.bmp")
            Zad3.obrazMnozenie(img1, int(val), N)

            N=2
            print("Podaj wartosc przez ktora chcesz pomnozyc obraz")
            val = input()
            img1 = Image.open("obrazy/flat512.bmp")
            Zad3.obrazMnozenie(img1, int(val), N)

        if int(excer)==4:
            N=1
            img1 = Image.open("obrazy/moutain512.bmp")
            img2 = Image.open("obrazy/BMW512.bmp")
            Zad3.mnozenieObrazow(img1, img2, N)

            N=2
            img1 = Image.open("obrazy/volvo512.bmp")
            img2 = Image.open("obrazy/ducati512.bmp")
            Zad3.mnozenieObrazow(img1, img2, N)

        if int(excer)==5:
            N=1
            img1 = Image.open("obrazy/monkey512.bmp")
            img2 = Image.open("obrazy/moto512.bmp")
            Zad3.mieszanieObrazow(img1, img2, N)

            N=2
            img1 = Image.open("obrazy/honda512.bmp")
            img2 = Image.open("obrazy/flat512.bmp")
            Zad3.mieszanieObrazow(img1, img2, N)

        if int(excer)==6:
            N=1
            print("Podaj wartosc przez ktora chcesz potegowac obraz")
            val = input()
            img1 = Image.open("obrazy/BMW2512.bmp")
            Zad3.potegowanieObrazu(img1, int(val), N)

            N=2
            print("Podaj wartosc przez ktora chcesz potegowac obraz")
            val = input()
            img1 = Image.open("obrazy/vegetables512.bmp")
            Zad3.potegowanieObrazu(img1, int(val), N)

        if int(excer)==7:
            N=1
            print("Podaj wartosc przez ktora chcesz podzielic obraz")
            val = input()
            img1 = Image.open("obrazy/lake512.bmp")
            Zad3.obrazDzielenie(img1, int(val), N)

            N=2
            print("Podaj wartosc przez ktora chcesz podzielic obraz")
            val = input()
            img1 = Image.open("obrazy/monkey512.bmp")
            Zad3.obrazDzielenie(img1, int(val), N)

        if int(excer)==8:
            N=1
            img1 = Image.open("obrazy/flat512.bmp")
            img2 = Image.open("obrazy/shreksmile512.bmp")
            Zad3.dzielenieObrazow(img1, img2, N)

            N=2
            img1 = Image.open("obrazy/lake512.bmp")
            img2 = Image.open("obrazy/512x512bb.bmp")
            Zad3.dzielenieObrazow(img1, img2, N)

        if int(excer)==9:
            N=1
            img1 = Image.open("obrazy/lake512.bmp")
            Zad3.pierwiastkowanieObrazu(img1, N)

            N=2
            img1 = Image.open("obrazy/waterfall512.bmp")
            Zad3.pierwiastkowanieObrazu(img1, N)

        if int(excer)==10:
            N=1
            img1 = Image.open("obrazy/BMW512.bmp")
            Zad3.logarytmowanieObrazu(img1, N)

            N=2
            img1 = Image.open("obrazy/moutain512.bmp")
            Zad3.logarytmowanieObrazu(img1, N)

    if int(sector) == 4:
        if int(excer) == 0:
            print("\nKoniec działania programu")
            break
        Zad4 = OperacjeGeometryczne()

        if int(excer)==1:
            N=1
            print("Podaj wartość przesuniecia na osi X")
            x = input()
            print("Podaj wartość przesunięcia na osi Y")
            y = input()
            img1 = Image.open("obrazy/Bear512.bmp")
            Zad4.przesuniecieObrazu(img1, int(x), int(y), N)

            N=2
            print("Podaj wartość przesuniecia na osi X")
            x = input()
            print("Podaj wartość przesunięcia na osi Y")
            y = input()
            img1 = Image.open("obrazy/BMW512.bmp")
            Zad4.przesuniecieObrazu(img1, int(x), int(y), N)

        if int(excer)==2:
            N=1
            img1 = Image.open("obrazy/vegetables512.bmp")
            Zad4.skalowanieJednorodne(img1, N)

            N=2
            img1 = Image.open("obrazy/BMW2512.bmp")
            Zad4.skalowanieJednorodne(img1, N)

        if int(excer)==3:
            N=1
            print("Podaj wartość wektora na osi X")
            x = input()
            print("Podaj wartość wektora na osi Y")
            y = input()
            img1 = Image.open("obrazy/BMW512.bmp")
            Zad4.skalowanieNieJednordone(img1, int(x), int(y), N)

            N=2
            print("Podaj wartość wektora na osi X")
            x = input()
            print("Podaj wartość wektora na osi Y")
            y = input()
            img1 = Image.open("obrazy/monkey512.bmp")
            Zad4.skalowanieNieJednordone(img1, int(x), int(y), N)

        if int(excer)==4:
            N=1
            img1 = Image.open("obrazy/lake512.bmp")
            Zad4.obracanieObrazu(img1, N)

            N=2
            img1 = Image.open("obrazy/shreksmile512.bmp")
            Zad4.obracanieObrazu(img1, N)

        if int(excer)==5:
            N=1
            img1 = Image.open("obrazy/backcar512.bmp")
            Zad4.symetriaObrazuX(img1, N)

            N=2
            img1 = Image.open("obrazy/flat512.bmp")
            Zad4.symetriaObrazuX(img1, N)

        if int(excer)==6:
            N=1
            img1 = Image.open("obrazy/way512.bmp")
            Zad4.symetriaObrazuY(img1, N)

            N=2
            img1 = Image.open("obrazy/backcar512.bmp")
            Zad4.symetriaObrazuY(img1, N)

        if int(excer)==7:
            N=1
            img1 = Image.open("obrazy/monkey512.bmp")
            Zad4.symetriaObrazuValX(img1, N)

            N=2
            img1 = Image.open("obrazy/moto512.bmp")
            Zad4.symetriaObrazuValX(img1, N)

        if int(excer)==8:
            N=1
            img1 = Image.open("obrazy/flat512.bmp")
            Zad4.symetriaObrazuValY(img1, N)

            N=2
            img1 = Image.open("obrazy/pepper512.bmp")
            Zad4.symetriaObrazuValY(img1, N)

        if int(excer)==9:
            N=1
            print("Podaj poczatkowa wartosc wektora x")
            startX = input()
            print("Podaj koncowa wartosc wektora x")
            endX = input()
            print("Podaj poczatkowa wartosc wektora y")
            startY = input()
            print("Podaj koncowa wartosc wektora y")
            endY = input()
            img1 = Image.open("obrazy/shreksmile512.bmp")
            Zad4.wycinanieFragemntowObrazu(img1, int(startX), int(endX), int(startY), int(endY), N)

            N=2
            print("Podaj poczatkowa wartosc wektora x")
            startX = input()
            print("Podaj koncowa wartosc wektora x")
            endX = input()
            print("Podaj poczatkowa wartosc wektora y")
            startY = input()
            print("Podaj koncowa wartosc wektora y")
            endY = input()
            img1 = Image.open("obrazy/honda512.bmp")
            Zad4.wycinanieFragemntowObrazu(img1, int(startX), int(endX), int(startY), int(endY), N)

        if int(excer)==10:
            N=1
            print("Podaj poczatkowa wartosc wektora x")
            startX = input()
            print("Podaj koncowa wartosc wektora x")
            endX = input()
            print("Podaj poczatkowa wartosc wektora y")
            startY = input()
            print("Podaj koncowa wartosc wektora y")
            endY = input()
            img1 = Image.open("obrazy/vegetables512.bmp")
            Zad4.kopiowanieFragmentowObrazu(img1, int(startX), int(endX), int(startY), int(endY), N)

            N=2
            print("Podaj poczatkowa wartosc wektora x")
            startX = input()
            print("Podaj koncowa wartosc wektora x")
            endX = input()
            print("Podaj poczatkowa wartosc wektora y")
            startY = input()
            print("Podaj koncowa wartosc wektora y")
            endY = input()
            img1 = Image.open("obrazy/512x512bb.bmp")
            Zad4.kopiowanieFragmentowObrazu(img1, int(startX), int(endX), int(startY), int(endY), N)

        else:
            print()
    else:
        print("Podales nieprawidlowy numer zadania, sprobuj ponownie!")