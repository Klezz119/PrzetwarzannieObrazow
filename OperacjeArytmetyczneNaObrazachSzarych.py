import numpy as np
from PIL import Image
import math
class OperacjeArytmetyczneSzare:

    def sumowaniePrzezStala(self, img1, val, N):

        img = img1
        width = img.width
        height = img.height
        img = np.array(img)

        pix1 = 255
        pix0 = 0


        if img.shape.__len__() == 3:
            img = img[:, :, 0]


        Max = 0
        for i in range(height):
            for j in range(width):
                nVal = int(img[i][j]) + int(val)

                if Max < nVal:
                    Max = nVal

        if Max > 255:
            abov = Max - 255
            pom = (abov / 255)
        imgRew1 = np.ones((width, height), dtype=np.uint8)
        for i in range(height):
            for j in range(width):

                nVal = (img[j][i] - (img[j][i] * pom)) + (val - (val * pom))
                imgRew1[j][i] = math.ceil(nVal)
                if pix1 > nVal:
                    pix1 = nVal
                if pix0 < nVal:
                    pix0 = nVal

        Norm = np.zeros((width, height), dtype=np.uint8)
        for i in range(height):
            for j in range(width):

                Norm[j][i] = 255 * ((imgRew1[j][i] - pix1) / (pix0 - pix1))

        Image.fromarray((img)).show()
        Image.fromarray((imgRew1)).show()
        Image.fromarray((Norm)).show()

        im1 = Image.fromarray(imgRew1)
        im1.convert('RGB')
        im1.save("przetworzone/zad2/21" + str(N) + ".png")
        im2 = Image.fromarray(Norm)
        im2.convert('RGB')
        im2.save("przetworzone/zad2/22" + str(N) + ".png")

    def sumowanieObrazow (self, img1, img2, N):

        height = img1.height
        width = img1.width
        imgRew1 = np.zeros((width, height), dtype=np.uint8)
        pix1 = 255
        pix0 = 0
        Max = 0
        pom = 0
        tImg1 = np.array(img1)
        tImg2 = np.array(img2)

        if tImg1.shape.__len__() == 3:
            tImg1 = tImg1[:, :, 0]
        if tImg2.shape.__len__() == 3:
            tImg2 = tImg2[:, :, 0]

        for i in range(height):
            for j in range(width):
                nVal = int(tImg1[j][i]) + int(tImg2[j][i])
                if Max < nVal:
                    Max = nVal

        if Max > 255:
            abov = Max - 255
            pom = (abov / 255)

        for i in range(height):
            for j in range(width):
                nVal = (tImg1[j][i] - (tImg1[j][i] * pom)) + (
                        tImg2[j][i] - (tImg2[j][i] * pom))
                imgRew1[j][i] = math.ceil(nVal)
                if pix1 > nVal:
                    pix1 = nVal
                if pix0 < nVal:
                    pix0 = nVal

        Norm = np.zeros((width, height), dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                Norm[j][i] = 255 * ((imgRew1[j][i] - pix1) / (pix0 - pix1))

        Image.fromarray((tImg1)).show()
        Image.fromarray((tImg2)).show()
        Image.fromarray((imgRew1)).show()
        Image.fromarray((Norm)).show()
        im1 = Image.fromarray(imgRew1)
        im1.convert('RGB')
        im1.save("przetworzone/zad2/23" + str(N) + ".png")
        im2 = Image.fromarray(Norm)
        im2.convert('RGB')
        im2.save("przetworzone/zad2/24" + str(N) + ".png")

    def obrazMnozenie(self, img1, val, N):

        imgArray=np.array(img1)
        height = img1.height
        width = img1.width
        imgResult1 = np.zeros((width, height), dtype=np.uint8)
        Norm = np.zeros((width, height), dtype=np.uint8)
        pix1 = 255
        pix0 = 0

        for i in range(height):
            for j in range(width):
                nVal = int(imgArray[j][i])
                if nVal == 255:
                    nVal = val
                elif nVal == 0:
                    nVal = 0
                else:
                    nVal = (int(imgArray[j][i]) * val) / 255
                imgResult1[j][i] = math.ceil(nVal)
                if pix1 > nVal:
                    pix1 = nVal
                if pix0 < nVal:
                    pix0 = nVal

        for i in range(height):
            for j in range(width):
                Norm[j][i] = 255 * ((imgResult1[j][i] - pix1) / (pix0 - pix1))

        Image.fromarray(imgArray).show()
        Image.fromarray(imgResult1).show()
        Image.fromarray(Norm).show()

        im1 = Image.fromarray(imgResult1)
        im1.convert('RGB')
        im1.save("przetworzone/zad2/25" + str(N) + ".png")
        im2 = Image.fromarray(Norm)
        im2.convert('RGB')
        im2.save("przetworzone/zad2/26" + str(N) + ".png")


    def mnozenieObraz(self, img1, img2, N):

            imgArray1=np.array(img1)
            imgArray2=np.array(img2)
            height = img2.height
            width = img2.width
            imgResult1 = np.zeros((width, height), dtype=np.uint8)
            imgNorm = np.zeros((width, height), dtype=np.uint8)
            pix1 = 255
            pix0 = 0

            if imgArray1.shape.__len__() == 3:
                imgArray1 = imgArray1[:, :, 0]
            if imgArray2.shape.__len__() == 3:
                imgArray2 = imgArray2[:, :, 0]

            for i in range(height):
                for j in range(width):
                    nVal = int(imgArray1[j][i])
                    if nVal == 255:
                        nVal = imgArray2[j][i]
                    elif nVal == 0:
                        nVal = 0
                    else:
                        nVal = (int(imgArray1[j][i]) * int(imgArray2[j][i])) / 255
                    imgResult1[j][i] = math.ceil(nVal)
                    if pix1 > nVal:
                        pix1 = nVal
                    if pix0 < nVal:
                        pix0 = nVal

            for i in range(height):
                for j in range(width):
                    imgNorm[j][i] = 255 * ((imgResult1[j][i] - pix1) / (pix0 - pix1))

            Image.fromarray(imgArray1).show()
            Image.fromarray(imgArray2).show()
            Image.fromarray(imgResult1).show()
            Image.fromarray(imgNorm).show()

            im1 = Image.fromarray(imgResult1)
            im1.convert('RGB')
            im1.save("przetworzone/zad2/27" + str(N) + ".png")
            im2 = Image.fromarray(imgNorm)
            im2.convert('RGB')
            im2.save("przetworzone/zad2/28" + str(N) + ".png")

    def mieszanieObrazow(self,img1, img2, N):

            val = 0.45
            height = img1.height
            width = img1.width
            imgArray1=np.array(img1)
            imgArray2=np.array(img2)
            imgResult1 = np.zeros((width, height), dtype=np.uint8)
            Norm = np.zeros((width, height), dtype=np.uint8)
            pix1 = 255
            pix0 = 0

            if imgArray1.shape.__len__() == 3:
                imgArray1 = imgArray1[:, :, 0]
            if imgArray2.shape.__len__() == 3:
                imgArray2 = imgArray2[:, :, 0]

            for i in range(height):
                for j in range(width):
                    nVal = float(imgArray1[j][i]) * val + (1 - val) * float(imgArray2[j][i])
                    imgResult1[j][i] = math.ceil(nVal)
                    if pix1 > nVal:
                        pix1 = nVal
                    if pix0 < nVal:
                        pix0 = nVal

            for i in range(height):
                for j in range(width):
                    Norm[j][i] = 255 * ((imgResult1[j][i] - pix1) / (pix0 - pix1))

            Image.fromarray(imgArray1).show()
            Image.fromarray(imgArray2).show()
            Image.fromarray(imgResult1).show()
            Image.fromarray(Norm).show()

            im1 = Image.fromarray(imgResult1)
            im1.convert('RGB')
            im1.save("przetworzone/zad2/29" + str(N) + ".png")
            im2 = Image.fromarray(Norm)
            im2.convert('RGB')
            im2.save("przetworzone/zad2/210" + str(N) + ".png")

    def potegowanieObrazow(self, img1, val, N):

        hight = img1.height
        width = img1.width
        imgResult1 = np.zeros((width, hight), dtype=np.uint8)
        Norm = np.zeros((width, hight), dtype=np.uint8)
        imgArray1 = np.array(img1)
        pix1 = 255
        pix0 = 0
        Max = 0

        if imgArray1.shape.__len__() == 3:
            imgArray1 = imgArray1[:, :, 0]

        for i in range(hight):
            for j in range(width):
                pom = int(imgArray1[j][i])
                if Max < pom:
                    Max = pom

        for i in range(hight):
            for j in range(width):
                pom = int(imgArray1[j][i])
                if pom == 255:
                    pom = 255
                elif pom == 0:
                    pom = 0
                else:
                    pom = math.pow(int(imgArray1[j][i]) / Max, val) * 255

                imgResult1[j][i] = math.ceil(pom)
                if pix1 > pom:
                    pix1 = pom
                if pix0 < pom:
                    pix0 = pom

        for i in range(hight):
            for j in range(width):
                Norm[j][i] = 255 * ((imgResult1[j][i] - pix1) / (pix0 - pix1))

        Image.fromarray(imgArray1).show()
        Image.fromarray(imgResult1).show()
        Image.fromarray(Norm).show()

        im1 = Image.fromarray(imgResult1)
        im1.convert('RGB')
        im1.save("przetworzone/zad2/211" + str(N) + ".png")
        im2 = Image.fromarray(Norm)
        im2.convert('RGB')
        im2.save("przetworzone/zad2/212" + str(N) + ".png")

    def dzielenieObrazu(self, img1, val, N):

        imgArray1=np.array(img1)
        height = img1.height
        width = img1.width
        imgResult1 = np.zeros((width, height), dtype=np.uint8)
        Normalizacja = np.zeros((width, height), dtype=np.uint8)
        pix1 = 255
        pix0 = 0
        Max = 0
        Dzielenie = 0
        for i in range(height):
            for j in range(width):
                pom = int(imgArray1[j][i]) + int(val)
                if Max < pom:
                    Max = pom

        for i in range(height):
            for j in range(width):
                pom = int(imgArray1[j][i]) + int(val)
                Dzielenie = (pom * 255) / Max

                imgResult1[j][i] = math.ceil(Dzielenie)
                if pix1 > Dzielenie:
                    pix1 = Dzielenie
                if pix0 < Dzielenie:
                    pix0 = Dzielenie

        for i in range(height):
            for j in range(width):
                Normalizacja[j][i] = 255 * ((imgResult1[j][i] - pix1) / (pix0 - pix1))

        Image.fromarray(imgArray1).show()
        Image.fromarray(imgResult1).show()
        Image.fromarray(Normalizacja).show()

        im1 = Image.fromarray(imgResult1)
        im1.convert('RGB')
        im1.save("przetworzone/zad2/213" + str(N) + ".png")
        im2 = Image.fromarray(Normalizacja)
        im2.convert('RGB')
        im2.save("przetworzone/zad2/214" + str(N) + ".png")

    def dzielenieObrazObraz(self, img1, img2, N):

        imgArray1=np.array(img1)
        imgArray2=np.array(img2)
        height = img1.height
        width = img1.width
        imgResult1 = np.zeros((width, height), dtype=np.uint8)
        Normalizacja = np.zeros((width, height), dtype=np.uint8)
        pix1 = 255
        pix0 = 0
        max = 0
        Dzielenie = 0

        if imgArray1.shape.__len__() == 3:
            imgArray1 = imgArray1[:, :, 0]
        if imgArray2.shape.__len__() == 3:
            imgArray2 = imgArray2[:, :, 0]

        for i in range(height):
            for j in range(width):
                # Obliczanie sumy
                pom = int(imgArray1[j][i]) + int(imgArray2[j][i])
                if max < pom:
                    max = pom

        for i in range(height):
            for j in range(width):
                pom = int(imgArray1[j][i]) + int(imgArray2[j][i])
                Dzielenie = (pom * 255) / max
                imgResult1[j][i] = math.ceil(Dzielenie)
                if pix1 > Dzielenie:
                    pix1 = Dzielenie
                if pix0 < Dzielenie:
                    pix0 = Dzielenie

        for i in range(height):
            for j in range(width):
                Normalizacja[j][i] = 255 * ((imgResult1[j][i] - pix1) / (pix0 - pix1))

        Image.fromarray(imgArray1).show()
        Image.fromarray(imgArray2).show()
        Image.fromarray(imgResult1).show()
        Image.fromarray(Normalizacja).show()

        im1 = Image.fromarray(imgResult1)
        im1.convert('RGB')
        im1.save("przetworzone/zad2/215" + str(N) + ".png")
        im2 = Image.fromarray(Normalizacja)
        im2.convert('RGB')
        im2.save("przetworzone/zad2/216" + str(N) + ".png")

    def pierwiastkowanieObrazow(self, img1, N):

        val = 2
        imgArray1 = np.array(img1)
        height = img1.height
        width = img1.width
        imgResult1 = np.zeros((width, height), dtype=np.uint8)
        Normalizacja = np.zeros((width, height), dtype=np.uint8)
        pix1 = 255
        pix0 = 0
        Max = 0
        A = 1 / val

        for i in range(height):
            for j in range(width):
                pom = int(imgArray1[j][i])
                if Max < pom:
                    Max = pom

        for i in range(height):
            for j in range(width):
                pom = int(imgArray1[j][i])
                if pom == 255:
                    pom = 255
                elif pom == 0:
                    pom = 0
                else:
                    pom = math.pow(int(imgArray1[j][i]) / Max, A) * 255
                imgResult1[j][i] = math.ceil(pom)
                if pix1 > pom:
                    pix1 = pom
                if pix0 < pom:
                    pix0 = pom

        for i in range(height):
            for j in range(width):
                Normalizacja[j][i] = 255 * ((imgResult1[j][i] - pix1) / (pix0 - pix1))

        Image.fromarray(imgArray1).show()
        Image.fromarray(imgResult1).show()
        Image.fromarray(Normalizacja).show()

        im1 = Image.fromarray(imgResult1)
        im1.convert('RGB')
        im1.save("przetworzone/zad2/217" + str(N) + ".png")
        im2 = Image.fromarray(Normalizacja)
        im2.convert('RGB')
        im2.save("przetworzone/zad2/218" + str(N) + ".png")

    def logarytmowanieObrazu(self, img1, N):

        imgArray1 = np.array(img1)
        height = img1.height
        width = img1.width
        imgResult1 = np.empty((width, height), dtype=np.uint8)
        Normalizacja = np.zeros((width, height), dtype=np.uint8)
        pix1 = 255
        pix0 = 0
        Max = 0

        if imgArray1.shape.__len__() == 3:
            imgArray1 = imgArray1[:, :, 0]

        for i in range(height):
            for j in range(width):
                pom = int(imgArray1[j][i])
                if Max < pom:
                    Max = pom

        for i in range(height):
            for j in range(width):
                pom = int(imgArray1[j][i])
                if pom == 0:
                    pom = 0
                else:
                    pom = (math.log(1 + pom) / math.log(1 + Max)) * 255
                imgResult1[j][i] = math.ceil(pom)
                if pix1 > pom:
                    pix1 = pom
                if pix0 < pom:
                    pix0 = pom

        for i in range(height):
            for j in range(width):
                Normalizacja[j][i] = 255 * ((imgResult1[j][i] - pix1) / (pix0 - pix1))

        Image.fromarray(imgArray1).show()
        Image.fromarray(imgResult1).show()
        Image.fromarray(Normalizacja).show()

        im1 = Image.fromarray(imgResult1)
        im1.convert('RGB')
        im1.save("przetworzone/zad2/219" + str(N) + ".png")
        im2 = Image.fromarray(Normalizacja)
        im2.convert('RGB')
        im2.save("przetworzone/zad2/220" + str(N) + ".png")
