import numpy as np
from PIL import Image
import math
class OperacjeArytmetyczneKolor:
    def sumowanie(self, img1, val, N):

        imgArray1 = np.array(img1)
        height = img1.height
        width = img1.width
        ImgRew1 = np.empty((width, height, 3), dtype=np.uint8)
        Normalizacja = np.zeros((width, height, 3), dtype=np.uint8)
        pix1 = 255
        pix0 = 0
        D = 0
        Q = 0
        X = 0

        for i in range(height):
            for j in range(width):
                red = int(imgArray1[j][i][0]) + int(val)
                green = int(imgArray1[j][i][1]) + int(val)
                blue = int(imgArray1[j][i][2]) + int(val)
                if Q < max([red, green, blue]):
                    Q = max([red, green, blue])
        if Q > 255:
            D = Q - 255
            X = (D / 255)

        for i in range(height):
            for j in range(width):
                red = (imgArray1[j][i][0] - (imgArray1[j][i][0] * X)) + (val - (val * X))
                green = (imgArray1[j][i][1] - (imgArray1[j][i][1] * X)) + (val - (val * X))
                blue = (imgArray1[j][i][2] - (imgArray1[j][i][2] * X)) + (val - (val * X))
                ImgRew1[j][i][0] = math.ceil(red)
                ImgRew1[j][i][1] = math.ceil(green)
                ImgRew1[j][i][2] = math.ceil(blue)

                if pix1 > min([red, green, blue]):
                    pix1 = min([red, green, blue])
                if pix0 < max([red, green, blue]):
                    pix0 = max([red, green, blue])

        for i in range(height):
            for j in range(width):
                Normalizacja[j][i][0] = 255 * ((ImgRew1[j][i][0] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][1] = 255 * ((ImgRew1[j][i][1] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][2] = 255 * ((ImgRew1[j][i][2] - pix1) / (pix0 - pix1))

        Image.fromarray(imgArray1).show()
        Image.fromarray(ImgRew1).show()
        Image.fromarray(Normalizacja).show()

        im1 = Image.fromarray(ImgRew1)
        im1.convert('RGB')
        im1.save("przetworzone/zad3/221" + str(N) + ".png")
        im2 = Image.fromarray(Normalizacja)
        im2.convert('RGB')
        im2.save("przetworzone/zad3/222" + str(N) + ".png")


    def sumowanieObrazow(self, img1, img2, N):
        height = img1.height
        width = img1.width
        Array1 = np.array(img1)
        Array2 = np.array(img2)
        ImgRew1 = np.empty((height, width, 3), dtype=np.uint8)
        Normalizacja = np.empty((height, width, 3), dtype=np.uint8)
        Q = 0
        D = 0
        X = 0
        pix1 = 255
        pix0 = 0
        for i in range(height):
            for j in range(width):
                red = int(Array1[j][i][0]) + int(Array2[j][i][0])
                green = int(Array1[j][i][1]) + int(Array2[j][i][1])
                blue = int(Array1[j][i][2]) + int(Array2[j][i][2])
                if Q < max([red, green, blue]):
                    Q = max([red, green, blue])
        if Q > 255:
            D = Q - 255
            X = (D / 255)
        for i in range(height):
            for j in range(width):
                red = (Array1[j][i][0] - (Array1[j][i][0] * X)) + (
                            Array2[j][i][0] - (Array2[j][i][0] * X))
                green = (Array1[j][i][1] - (Array1[j][i][1] * X)) + (
                            Array2[j][i][1] - (Array2[j][i][1] * X))
                blue = (Array1[j][i][2] - (Array1[j][i][2] * X)) + (
                            Array2[j][i][2] - (Array2[j][i][2] * X))
                ImgRew1[j][i][0] = math.ceil(red)
                ImgRew1[j][i][1] = math.ceil(green)
                ImgRew1[j][i][2] = math.ceil(blue)
                if pix1 > min([red, green, blue]):
                    pix1 = min([red, green, blue])
                if pix0 < max([red, green, blue]):
                    pix0 = max([red, green, blue])
        for i in range(height):
            for j in range(width):
                Normalizacja[j][i][0] = 255 * ((ImgRew1[j][i][0] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][1] = 255 * ((ImgRew1[j][i][1] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][2] = 255 * ((ImgRew1[j][i][2] - pix1) / (pix0 - pix1))
            Image.fromarray(Array1).show()
            Image.fromarray(Array2).show()
            Image.fromarray(ImgRew1).show()
            Image.fromarray(Normalizacja).show()

        im1 = Image.fromarray(ImgRew1)
        im1.convert('RGB')
        im1.save("przetworzone/zad3/223" + str(N) + ".png")
        im2 = Image.fromarray(Normalizacja)
        im2.convert('RGB')
        im2.save("przetworzone/zad3/224" + str(N) + ".png")


    def obrazMnozenie(self, img1, val, N):


        height = img1.height
        width = img1.width
        Array1 = np.array(img1)
        ImgRew = np.empty((height, width, 3), dtype=np.uint8)
        Normalizacja = np.zeros((width, height, 3), dtype=np.uint8)
        pix1 = 255
        pix0 = 0
        for i in range(height):
            for j in range(width):
                red = int(Array1[j][i][0])
                green = int(Array1[j][i][1])
                blue = int(Array1[j][i][2])

                if red == 255:
                    red = val
                elif red == 0:
                    red = 0
                else:
                    red = (int(Array1[j][i][0]) * int(val)) / 255
                if green == 255:
                    green = val
                elif green == 0:
                    green = 0
                else:
                    green = (int(Array1[j][i][1]) * int(val)) / 255
                if blue == 255:
                    blue = val
                elif blue == 0:
                    blue = 0
                else:
                    blue = (int(Array1[j][i][2]) * int(val)) / 255
                ImgRew[j][i][0] = math.ceil(red)
                ImgRew[j][i][1] = math.ceil(green)
                ImgRew[j][i][2] = math.ceil(blue)

                if pix1 > min([red, green, blue]):
                    pix1 = min([red, green, blue])
                if pix0 < max([red, green, blue]):
                    pix0 = max([red, green, blue])
        for i in range(height):
            for j in range(width):
                Normalizacja[j][i][0] = 255 * ((ImgRew[j][i][0] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][1] = 255 * ((ImgRew[j][i][1] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][2] = 255 * ((ImgRew[j][i][2] - pix1) / (pix0 - pix1))
        Image.fromarray(Array1).show()
        Image.fromarray(ImgRew).show()
        Image.fromarray(Normalizacja).show()
        im1 = Image.fromarray(ImgRew)
        im1.convert('RGB')
        im1.save("przetworzone/zad3/225" + str(N) + ".png")
        im2 = Image.fromarray(Normalizacja)
        im2.convert('RGB')
        im2.save("przetworzone/zad3/226" + str(N) + ".png")

    def mnozenieObrazow(self, img1, img2, N):


        height = img1.height
        width = img1.width
        Array1 = np.array(img1)
        Array2 = np.array(img2)
        ImgRew = np.empty((height, width, 3), dtype=np.uint8)
        Normalizacja =  np.empty((height, width, 3), dtype=np.uint8)
        pix1 = 255
        pix0 = 0

        for i in range(height):
            for j in range(width):
                red = int(Array1[j][i][0])
                green = int(Array1[j][i][1])
                blue = int(Array1[j][i][2])
                if red == 255:
                    red = Array2[j][i][0]
                elif red == 0:
                    red = 0
                else:
                    red = (int(Array1[j][i][0]) * int(Array2[j][i][0])) / 255
                if green == 255:
                    green = Array2[j][i][1]
                elif green == 0:
                    green = 0
                else:
                    green = (int(Array1[j][i][1]) * int(Array2[j][i][1])) / 255
                if blue == 255:
                    blue = Array2[j][i][2]
                elif blue == 0:
                    blue = 0
                else:
                    blue = (int(Array1[j][i][2]) * int(Array2[j][i][2])) / 255

                ImgRew[j][i][0] = math.ceil(red)
                ImgRew[j][i][1] = math.ceil(green)
                ImgRew[j][i][2] = math.ceil(blue)
                if pix1 > min([red, green, blue]):
                    pix1 = min([red, green, blue])
                if pix0 < max([red, green, blue]):
                    pix0 = max([red, green, blue])
        for i in range(height):
            for j in range(width):
                Normalizacja[j][i][0] = 255 * ((ImgRew[j][i][0] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][1] = 255 * ((ImgRew[j][i][1] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][2] = 255 * ((ImgRew[j][i][2] - pix1) / (pix0 - pix1))
        Image.fromarray(Array1).show()
        Image.fromarray(Array2).show()
        Image.fromarray(ImgRew).show()
        Image.fromarray(Normalizacja).show()
        im1 = Image.fromarray(ImgRew)
        im1.convert('RGB')
        im1.save("przetworzone/zad3/227" + str(N) + ".png")
        im2 = Image.fromarray(Normalizacja)
        im2.convert('RGB')
        im2.save("przetworzone/zad3/228" + str(N) + ".png")

    def mieszanieObrazow(self, img1, img2, N):

        imgArray1 = np.array(img1)
        imgArray2 = np.array(img2)
        height = img1.height
        width = img1.width
        Normalizacja = np.zeros((width, height, 3), dtype=np.uint8)
        imgResult1 = np.empty((height, width, 3), dtype=np.uint8)
        pix1 = 255
        pix0 = 0
        val = 0.45

        for i in range(height):
            for j in range(width):
                red = float(imgArray1[j][i][0]) * val + (1 - val) * float(imgArray2[j][i][0])
                green = float(imgArray1[j][i][1]) * val + (1 - val) * float(imgArray2[j][i][1])
                blue = float(imgArray1[j][i][2]) * val + (1 - val) * float(imgArray2[j][i][2])
                imgResult1[j][i][0] = math.ceil(red)
                imgResult1[j][i][1] = math.ceil(green)
                imgResult1[j][i][2] = math.ceil(blue)
                if pix1 > min([red, green, blue]):
                    pix1 = min([red, green, blue])
                if pix0 < max([red, green, blue]):
                    pix0 = max([red, green, blue])
        for i in range(height):
            for j in range(width):
                Normalizacja[j][i][0] = 255 * ((imgResult1[j][i][0] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][1] = 255 * ((imgResult1[j][i][1] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][2] = 255 * ((imgResult1[j][i][2] - pix1) / (pix0 - pix1))
        Image.fromarray(imgArray1).show()
        Image.fromarray(imgArray2).show()
        Image.fromarray(imgResult1).show()
        Image.fromarray(Normalizacja).show()
        im1 = Image.fromarray(imgResult1)
        im1.convert('RGB')
        im1.save("przetworzone/zad3/229" + str(N) + ".png")
        im2 = Image.fromarray(Normalizacja)
        im2.convert('RGB')
        im2.save("przetworzone/zad3/230" + str(N) + ".png")


    def potegowanieObrazu(self, img1, val, N):
        Array = np.array(img1)
        height = img1.height
        width = img1.width
        ImgRew = np.empty((height, width, 3), dtype=np.uint8)
        Normalizacja = np.zeros((width, height, 3), dtype=np.uint8)
        pix1 = 255
        pix0 = 0
        pom = 0
        for i in range(height):
            for j in range(width):
                red = int(Array[j][i][0])
                green = int(Array[j][i][1])
                blue = int(Array[j][i][2])

                if pom < max([red, green, blue]):
                    pom = max([red, green, blue])
        for i in range(height):
            for j in range(width):
                red = int(Array[j][i][0])
                green = int(Array[j][i][1])
                blue = int(Array[j][i][2])
                if red == 0:
                    red = 0
                else:
                    red = 255 * (math.pow(int(Array[j][i][0]) / pom, val))
                if green == 0:
                    green = 0
                else:
                    green = 255 * (math.pow(int(Array[j][i][1]) / pom, val))
                if blue == 0:
                    blue = 0
                else:
                    blue = 255 * (math.pow(int(Array[j][i][2]) / pom, val))
                ImgRew[j][i][0] = math.ceil(red)
                ImgRew[j][i][1] = math.ceil(green)
                ImgRew[j][i][2] = math.ceil(blue)
                if pix1 > min([red, green, blue]):
                    pix1 = min([red, green, blue])
                if pix0 < max([red, green, blue]):
                    pix0 = max([red, green, blue])

        for i in range(height):
            for j in range(width):
                Normalizacja[j][i][0] = 255 * ((ImgRew[j][i][0] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][1] = 255 * ((ImgRew[j][i][1] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][2] = 255 * ((ImgRew[j][i][2] - pix1) / (pix0 - pix1))
        Image.fromarray(Array).show()
        Image.fromarray(ImgRew).show()
        Image.fromarray(Normalizacja).show()

        im1 = Image.fromarray(ImgRew)
        im1.convert('RGB')
        im1.save("przetworzone/zad3/231" + str(N) + ".png")
        im2 = Image.fromarray(Normalizacja)
        im2.convert('RGB')
        im2.save("przetworzone/zad3/232" + str(N) + ".png")

    def obrazDzielenie(self, img1, val, N):


        height = img1.height
        width = img1.width
        Array = np.array(img1)
        ImgRew = np.empty((height, width, 3), dtype=np.uint8)
        Normalizacja = np.zeros((width, height, 3), dtype=np.uint8)
        pix1 = 255
        pix0 = 0
        Q = 0
        for i in range(height):
            for j in range(width):
                red = int(Array[j][i][0]) + int(val)
                green = int(Array[j][i][1]) + int(val)
                blue = int(Array[j][i][2]) + int(val)
                if Q < max([red, green, blue]):
                    Q = max([red, green, blue])

        for i in range(height):
            for j in range(width):
                red = int(Array[j][i][0]) + int(val)
                green = int(Array[j][i][1]) + int(val)
                blue = int(Array[j][i][2]) + int(val)
                redQ = (red * 255) / Q
                greenQ = (green * 255) / Q
                blueQ = (blue * 255) / Q
                ImgRew[j][i][0] = math.ceil(redQ)
                ImgRew[j][i][1] = math.ceil(greenQ)
                ImgRew[j][i][2] = math.ceil(blueQ)
                if pix1 > min([redQ, greenQ, blueQ]):
                    pix1 = min([redQ, greenQ, blueQ])
                if pix0 < max([redQ, greenQ, blueQ]):
                    pix0 = max([redQ, greenQ, blueQ])
        for i in range(height):
            for j in range(width):
                Normalizacja[j][i][0] = 255 * ((ImgRew[j][i][0] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][1] = 255 * ((ImgRew[j][i][1] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][2] = 255 * ((ImgRew[j][i][2] - pix1) / (pix0 - pix1))
        Image.fromarray(Array).show()
        Image.fromarray(ImgRew).show()
        Image.fromarray(Normalizacja).show()
        im1 = Image.fromarray(ImgRew)
        im1.convert('RGB')
        im1.save("przetworzone/zad3/233" + str(N) + ".png")
        im2 = Image.fromarray(Normalizacja)
        im2.convert('RGB')
        im2.save("przetworzone/zad3/234" + str(N) + ".png")

    def dzielenieObrazow(self, img1, img2, N):

        Array1 = np.array(img1)
        Array2 = np.array(img2)
        height = img1.height
        width = img1.width
        ImgRew = np.empty((height, width, 3), dtype=np.uint8)
        Normalizacja = np.zeros((width, height, 3), dtype=np.uint8)
        pix1 = 255
        pix0 = 0
        Q = 0
        for i in range(height):
            for j in range(width):
                red = int(Array1[j][i][0]) + int(Array2[j][i][0])
                green = int(Array1[j][i][1]) + int(Array2[j][i][1])
                blue = int(Array1[j][i][2]) + int(Array2[j][i][2])
                if Q < max([red, green, blue]):
                    Q = max([red, green, blue])
        for i in range(height):
            for j in range(width):
                red = int(Array1[j][i][0]) + int(Array2[j][i][0])
                green = int(Array1[j][i][1]) + int(Array2[j][i][1])
                blue = int(Array1[j][i][2]) + int(Array2[j][i][2])
                redQ = (red * 255) / Q
                greenQ = (green * 255) / Q
                blueQ = (blue * 255) / Q
                ImgRew[j][i][0] = math.ceil(redQ)
                ImgRew[j][i][1] = math.ceil(greenQ)
                ImgRew[j][i][2] = math.ceil(blueQ)
                if pix1 > min([redQ, greenQ, blueQ]):
                    pix1 = min([redQ, greenQ, blueQ])
                if pix0 < max([redQ, greenQ, blueQ]):
                    pix0 = max([redQ, greenQ, blueQ])
        for i in range(height):
            for j in range(width):
                Normalizacja[j][i][0] = 255 * ((ImgRew[j][i][0] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][1] = 255 * ((ImgRew[j][i][1] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][2] = 255 * ((ImgRew[j][i][2] - pix1) / (pix0 - pix1))
        Image.fromarray(Array1).show()
        Image.fromarray(Array2).show()
        Image.fromarray(ImgRew).show()
        Image.fromarray(Normalizacja).show()
        im1 = Image.fromarray(ImgRew)
        im1.convert('RGB')
        im1.save("przetworzone/zad3/235" + str(N) + ".png")
        im2 = Image.fromarray(Normalizacja)
        im2.convert('RGB')
        im2.save("przetworzone/zad3/236" + str(N) + ".png")

    def pierwiastkowanieObrazu(self, img1, N):

        Array = np.array(img1)
        height = img1.height
        width = img1.width
        ImgRew = np.empty((height, width, 3), dtype=np.uint8)
        Normalizacja = np.zeros((width, height, 3), dtype=np.uint8)
        pix1 = 255
        pix0 = 0
        pom = 0
        V = 1 / 3
        for i in range(height):
            for j in range(width):
                red = int(Array[j][i][0])
                green = int(Array[j][i][1])
                blue = int(Array[j][i][2])
                if pom < max([red, green, blue]):
                    pom = max([red, green, blue])
        for i in range(height):
            for j in range(width):
                red = int(Array[j][i][0])
                green = int(Array[j][i][1])
                blue = int(Array[j][i][2])
                if red == 0:
                    red = 0
                else:
                    red = 255 * (math.pow(int(Array[j][i][0]) / pom, V))
                if green == 0:
                    green = 0
                else:
                    green = 255 * (math.pow(int(Array[j][i][1]) / pom, V))
                if blue == 0:
                    blue = 0
                else:
                    blue = 255 * (math.pow(int(Array[j][i][2]) / pom, V))
                ImgRew[j][i][0] = math.ceil(red)
                ImgRew[j][i][1] = math.ceil(green)
                ImgRew[j][i][2] = math.ceil(blue)

                if pix1 > min([red, green, blue]):
                    pix1 = min([red, green, blue])
                if pix0 < max([red, green, blue]):
                    pix0 = max([red, green, blue])
        for i in range(height):
            for j in range(width):
                Normalizacja[j][i][0] = 255 * ((ImgRew[j][i][0] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][1] = 255 * ((ImgRew[j][i][1] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][2] = 255 * ((ImgRew[j][i][2] - pix1) / (pix0 - pix1))

        Image.fromarray(Array).show()
        Image.fromarray(ImgRew).show()
        Image.fromarray(Normalizacja).show()

        im1 = Image.fromarray(ImgRew)
        im1.convert('RGB')
        im1.save("przetworzone/zad3/237" + str(N) + ".png")
        im2 = Image.fromarray(Normalizacja)
        im2.convert('RGB')
        im2.save("przetworzone/zad3/238" + str(N) + ".png")

    def logarytmowanieObrazu(self, img1, N):

        Array = np.array(img1)
        height = img1.height
        width = img1.width
        ImgRew = np.empty((height, width, 3), dtype=np.uint8)
        Normalizacja = np.zeros((width, height, 3), dtype=np.uint8)
        pix1 = 255
        pix0 = 0
        pom = 0
        for i in range(height):
            for j in range(width):
                red = int(Array[j][i][0])
                green = int(Array[j][i][1])
                blue = int(Array[j][i][2])
                if pom < max([red, green, blue]):
                    pom = max([red, green, blue])
        for i in range(height):
            for j in range(width):
                red = int(Array[j][i][0])
                green = int(Array[j][i][1])
                blue = int(Array[j][i][2])
                if red == 0:
                    red = 0
                else:
                    red = math.log(1 + int(Array[j][i][0])) / math.log(1 + int(pom)) * 255
                if green == 0:
                    green = 0
                else:
                    green = math.log(1 + int(Array[j][i][1])) / math.log(1 + int(pom)) * 255
                if blue == 0:
                    blue = 0
                else:
                    blue = math.log(1 + int(Array[j][i][2])) / math.log(1 + int(pom)) * 255
                ImgRew[j][i][0] = math.ceil(red)
                ImgRew[j][i][1] = math.ceil(green)
                ImgRew[j][i][2] = math.ceil(blue)
                if pix1 > min([red, green, blue]):
                    pix1 = min([red, green, blue])
                if pix0 < max([red, green, blue]):
                    pix0 = max([red, green, blue])
        for i in range(height):
            for j in range(width):
                Normalizacja[j][i][0] = 255 * ((ImgRew[j][i][0] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][1] = 255 * ((ImgRew[j][i][1] - pix1) / (pix0 - pix1))
                Normalizacja[j][i][2] = 255 * ((ImgRew[j][i][2] - pix1) / (pix0 - pix1))
        Image.fromarray(Array).show()
        Image.fromarray(ImgRew).show()
        Image.fromarray(Normalizacja).show()
        im1 = Image.fromarray(ImgRew)
        im1.convert('RGB')
        im1.save("przetworzone/zad3/239" + str(N) + ".png")
        im2 = Image.fromarray(Normalizacja)
        im2.convert('RGB')
        im2.save("przetworzone/zad3/240" + str(N) + ".png")