import numpy as np
from PIL import Image
import math
class OperacjeGeometryczne:
    def przesuniecieObrazu(self, img1, x, y, N):
        Array = np.array(img1)
        height = img1.height
        width = img1.width
        ImgRew = np.zeros((height, width, 3), dtype=np.uint8)
        y = 0 - y

        for i in range(height):
            for j in range(width):
                if 0 < i + y < height and 0 < j + x < width:
                    ImgRew[i + y][j + x] = Array[i][j]
        Image.fromarray(Array).show()
        Image.fromarray(ImgRew).show()
        im1 = Image.fromarray(ImgRew)
        im1.convert('RGB')
        im1.save("przetworzone/zad4/241" + str(N) + ".png")

    def skalowanieJednorodne(self, img1, N):
        V = 2
        Array = np.array(img1)
        height = img1.height
        width = img1.width
        ImgRew = np.zeros((height, width, 3), dtype=np.uint8)
        ImgRew2 = np.copy(ImgRew)
        for i in range(height):
            for j in range(width):
                if V * i < height and V * j < width:
                    ImgRew[int(V * i)][int(V * j)] = Array[i][j]


        pom = np.ones((height, width, 3), dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                red = 0
                green = 0
                blue = 0
                buf = 1
                pom[i, j] = ImgRew2[i, j]
                if (ImgRew2[i, j][0] < 1) & (ImgRew2[i, j][1] < 1) & (ImgRew2[i, j][2] < 1):
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            k = i if ((i + i) > (height - 2)) | ((i + i) < 0) else (i + i)
                            l = j if ((j + j) > (width - 2)) | ((j + j) < 0) else (j + j)
                            if (ImgRew2[k, l][0] > 0) | (ImgRew2[k, l][1] > 0) | (
                                    ImgRew2[k, l][2] > 0):
                                red += ImgRew2[k, l][0]
                                green += ImgRew2[k, l][1]
                                blue += ImgRew2[k, l][2]
                                buf += 1
                    pom[i, j] = (red / buf, green / buf, blue / buf)
                    ImgRew2[i, j] = pom[i, j]
        Image.fromarray(Array).show()
        Image.fromarray(ImgRew2).show()
        im1 = Image.fromarray(ImgRew2)
        obraz = self.obraz1
        szerokosc = obraz.width
        wysokosc = obraz.height

        macierz_obrazu = np.array(obraz)

        # zmieniam na 3 kanaly , jesli ma 4 kanaly
        if (macierz_obrazu.shape[2] == 4):
            print("zmieniam na 3 kanaly")
            macierz_obrazu = macierz_obrazu[..., :3]

        rezultat = np.zeros((wysokosc, szerokosc, 3), dtype=np.uint8)

        for i in range(wysokosc):
            for k in range(szerokosc):
                if V * i < wysokosc and V * k < szerokosc:
                    rezultat[int(V * i)][int(V * k)] = macierz_obrazu[i][k]

        rezultat_obrazu2 = np.copy(rezultat)
        tymczasowa_zmienna = np.ones((wysokosc, szerokosc, 3), dtype=np.uint8)

        # interpolacja
        for i in range(wysokosc):
            for j in range(szerokosc):
                r, g, b = 0, 0, 0
                n = 1
                tymczasowa_zmienna[i, j] = rezultat_obrazu2[i, j]
                if (rezultat_obrazu2[i, j][0] < 1) & (rezultat_obrazu2[i, j][1] < 1) & (rezultat_obrazu2[i, j][2] < 1):
                    for a in range(-1, 2):
                        for jOff in range(-1, 2):
                            b = i if ((i + a) > (wysokosc - 2)) | ((i + a) < 0) else (i + a)
                            c = j if ((j + jOff) > (szerokosc - 2)) | ((j + jOff) < 0) else (j + jOff)
                            if (rezultat_obrazu2[b, c][0] > 0) | (rezultat_obrazu2[b, c][1] > 0) | (
                                    rezultat_obrazu2[b, c][2] > 0):
                                r += rezultat_obrazu2[b, c][0]
                                g += rezultat_obrazu2[b, c][1]
                                b += rezultat_obrazu2[b, c][2]
                                n += 1
                    tymczasowa_zmienna[i, j] = (r / n, g / n, b / n)
                    rezultat_obrazu2[i, j] = tymczasowa_zmienna[i, j]

        # poczatek
        Image._show(self.obraz1)
        # po skalowaniu
        self.pokazZdjecie(Image.fromarray(rezultat, "RGB"), self.obraz1_nazwa)
        # interpolacja
        self.pokazZdjecie(Image.fromarray(rezultat_obrazu2, "RGB"), self.obraz1_nazwa)

        self.convert('RGB')
        self.save("przetworzone/zad4/242" + str(N) + ".png")

    def skalowanieNieJednordone(self, img1, x, y, N):

        Array = np.array(img1)
        height = img1.height
        width = img1.width
        ImgRew = np.zeros((height, width, 3), dtype=np.uint8)
        P = np.ones((height, width, 3), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                if y * i < height and x * j < width:
                    ImgRew[int(y * i)][int(x * j)] = Array[i][j]

        ImgRew2 = np.copy(ImgRew)
        for i in range(height):
            for j in range(width):
                red = 0
                green = 0
                blue = 0
                x = 1
                P[i, j] = ImgRew2[i, j]
                if (ImgRew2[i, j][0] < 1) & (ImgRew2[i, j][1] < 1) & (ImgRew2[i, j][2] < 1):
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            iS = i if ((i + k) > (height - 2)) | ((i + k) < 0) else (i + k)
                            jS = j if ((j + l) > (width - 2)) | ((j + l) < 0) else (j + l)
                            if (ImgRew2[iS, jS][0] > 0) | (ImgRew2[iS, jS][1] > 0) | (
                                    ImgRew2[iS, jS][2] > 0):
                                red += ImgRew2[iS, jS][0]
                                green += ImgRew2[iS, jS][1]
                                blue += ImgRew2[iS, jS][2]
                                x += 1
                    P[i, j] = (red / x, green / x, blue / x)
                    ImgRew2[i, j] = P[i, j]
        Image.fromarray(Array).show()
        Image.fromarray(ImgRew).show()
        Image.fromarray(ImgRew2).show()
        im1 = Image.fromarray(ImgRew)
        im1.convert('RGB')
        im1.save("przetworzone/zad4/243" + str(N) + ".png")
        im1 = Image.fromarray(ImgRew2)
        im1.convert('RGB')
        im1.save("przetworzone/zad4/244" + str(N) + ".png")

    def obracanieObrazu(self, img1, N):
        Array = np.array(img1)
        height = img1.height
        width = img1.width
        V = 150
        turn = math.radians(V)
        ImgRew = np.zeros((height, width, 3), dtype=np.uint8)
        ImgRew2 = np.copy(ImgRew)
        P = np.ones((height, width, 3), dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                new_x = (j - width / 2) * math.cos(turn) - (i - height / 2) * math.sin(turn) + (width / 2)
                new_y = (j - width / 2) * math.sin(turn) + (i - height / 2) * math.cos(turn) + (height / 2)
                if new_y < height and new_y >= 0 and new_x >= 0 and new_x < width:
                    ImgRew[int(new_y)][int(new_x)] = Array[i][j]
        for i in range(height):
            for j in range(width):
                red = 0
                green = 0
                blue = 0
                x = 1
                P[i, j] = ImgRew2[i, j]
                if (ImgRew2[i, j][0] < 1) & (ImgRew2[i, j][1] < 1) & (ImgRew2[i, j][2] < 1):
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            iS = i if ((i + k) > (height - 2)) | ((i + k) < 0) else (i + k)
                            jS = j if ((j + l) > (width - 2)) | ((j + l) < 0) else (j + l)
                            if (ImgRew2[iS, jS][0] > 0) | (ImgRew2[iS, jS][1] > 0) | (
                                    ImgRew2[iS, jS][2] > 0):
                                red += ImgRew2[iS, jS][0]
                                green += ImgRew2[iS, jS][1]
                                blue += ImgRew2[iS, jS][2]
                                x += 1
                    P[i, j] = (red / x, green / x, blue / x)
                    ImgRew2[i, j] = P[i, j]
        Image.fromarray(Array).show()
        Image.fromarray(ImgRew).show()

        im1 = Image.fromarray(ImgRew)
        im1.convert('RGB')
        im1.save("przetworzone/zad4/245" + str(N) + ".png")
        im1 = Image.fromarray(ImgRew2)
        im1.convert('RGB')
        im1.save("przetworzone/zad4/246" + str(N) + ".png")

    def symetriaObrazuX(self, img1, N):

        Array = np.array(img1)
        height = img1.height
        width = img1.width
        ImgRew = np.zeros((height, width, 3), dtype=np.uint8)
        H = height - 1
        for i in range(height):
            for j in range(width):
                ImgRew[i][j] = Array[H - i][j]

        Image.fromarray(Array).show()
        Image.fromarray(ImgRew).show()
        im1 = Image.fromarray(ImgRew)
        im1.convert('RGB')
        im1.save("przetworzone/zad4/247" + str(N) + ".png")

    def symetriaObrazuY(self, img1, N):
        Array = np.array(img1)
        height = img1.height
        width = img1.width
        ImgRew = np.zeros((height, width, 3), dtype=np.uint8)
        W = width - 1
        for i in range(height):
            for j in range(width):
                ImgRew[i][j] = Array[i][W - j]

        Image.fromarray(Array).show()
        Image.fromarray(ImgRew).show()
        im1 = Image.fromarray(ImgRew)
        im1.convert('RGB')
        im1.save("przetworzone/zad4/248" + str(N) + ".png")

    def symetriaObrazuValY(self, img1, N):

        Array = np.array(img1)
        height = img1.height
        width = img1.width
        ImgRew = np.zeros((height, width, 3), dtype=np.uint8)
        W = width - 1
        V = width / 2
        for i in range(height):
            for j in range(width):
                if j < V:
                    ImgRew[i][j] = Array[i][j]
                else:
                    ImgRew[i][j] = Array[i][W - j]
        Image.fromarray(Array).show()
        Image.fromarray(ImgRew).show()
        im1 = Image.fromarray(ImgRew)
        im1.convert('RGB')
        im1.save("przetworzone/zad4/250" + str(N) + ".png")

    def symetriaObrazuValX(self, img1, N):

        Array = np.array(img1)
        height = img1.height
        width = img1.width
        ImgRew = np.zeros((height, width, 3), dtype=np.uint8)
        H = height - 1
        V = height / 2
        for i in range(height):
            for j in range(width):
                if i < V:
                    ImgRew[i][j] = Array[i][j]
                else:
                    ImgRew[i][j] = Array[H - i][j]
        Image.fromarray(Array).show()
        Image.fromarray(ImgRew).show()
        im1 = Image.fromarray(ImgRew)
        im1.convert('RGB')
        im1.save("przetworzone/zad4/249" + str(N) + ".png")

    def wycinanieFragemntowObrazu(self, img1, X, _X, Y, _Y, N):

        Array = np.array(img1)
        if (Array.shape[2] == 4):
            Array = Array[..., :3]

        height = img1.height
        width = img1.width
        ImgRew = np.zeros((height, width, 3), dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                if j > X and j < _X and i < height - Y and i > height - _Y:
                    ImgRew[i][j] = 0
                else:
                    ImgRew[i][j] = Array[i][j]

        Image.fromarray(Array).show()
        Image.fromarray(ImgRew).show()
        im1 = Image.fromarray(ImgRew)
        im1.convert('RGB')
        im1.save("przetworzone/zad4/251" + str(N) + ".png")


    def kopiowanieFragmentowObrazu(self, img1, X, _X, Y, _Y, N):

        O_Y = 0
        Array = np.array(img1)
        height = img1.height
        width = img1.width
        ImgRew = np.zeros((height, width, 3), dtype=np.uint8)
        Fragment = np.zeros((_Y - Y + 1, _X - X + 1, 3), dtype=np.uint8)

        for i in range(height):
            O_X = 0
            for j in range(width):
                if j >= X and j <= _X and i <= height - Y and i >= height - _Y:
                    ImgRew[i][j] = Array[i][j]
                    Fragment[O_Y][O_X] = Array[i][j]
                    O_X += 1
            if O_X > 0:
                O_Y += 1
        Image.fromarray(Array).show()
        Image.fromarray(ImgRew).show()
        Image.fromarray(Fragment, "RGB").show()
        im1 = Image.fromarray(Fragment)
        im1.convert('RGB')
        im1.save("przetworzone/zad4/252" + str(N) + ".png")
