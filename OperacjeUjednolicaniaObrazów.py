import numpy as np
from PIL import Image

class UjednolicenieObrazow:

    def Geometryczne(self, img1, img2, N):

        width1 = img1.width
        height1 = img1.height

        width2 = img2.width
        height2 = img2.height

        if(width1>width2):
            Max_Width = width1
        else:
            Max_Width = width2

        if(height1>height2):

            Max_Height = height1
        else:
            Max_Height = height2

        ImgArray1 = np.array(img1)
        if ImgArray1.shape.__len__() == 3:
            ImgArray1 = ImgArray1[:, :, 0]
        ImgArray2 = np.array(img2)
        if ImgArray2.shape.__len__() == 3:
            ImgArray2 = ImgArray2[:, :, 0]


        imgRew1 = np.ones((Max_Height, Max_Width), dtype=int)
        imgRew2 = np.ones((Max_Height, Max_Width), dtype=int)

        newImgWidth1=int(round((Max_Width - width1) /2))
        newImgHeight1=int(round((Max_Height - height1) /2))

        for i in range(0, height1):
            for j in range(0, width1):
                imgRew1[i+newImgHeight1,
                           j+newImgWidth1] = ImgArray1[i, j]

        for i in range(0, height2):
             for j in range(0, width2):
                 imgRew2[i, j] = ImgArray2[i, j]

        Image.fromarray((imgRew1)).show()
        Image.fromarray((imgRew2)).show()
        im = Image.fromarray(imgRew1*255)

        im.convert('RGB')
        im.save("przetworzone/zad1/1" + str(N) +".png")

    def Rozdzielczosciowe(self, img1, img2, N):

        img2.show()

        height1 = img1.height
        width1 = img1.width

        height2 = img2.height
        width2 = img2.width


        if (width1 > width2):
            Max_Width = width1
        else:
            Max_Width = width2

        if (height1 > height2):
            Max_Height = height1
        else:
            Max_Height = height2

        imgRew1 = np.zeros((Max_Height, Max_Width), dtype=np.int)
        imgRew2 = np.zeros((Max_Height, Max_Width), dtype=np.int)

        temp = np.zeros((height1, width1), dtype=np.uint8)
        w_width = width1 / width2
        h_height = height1 / height2
        Q = 0


        ImgArray1 = np.array(img1)
        if ImgArray1.shape.__len__() == 3:
            ImgArray1 = ImgArray1[:, :, 0]
        ImgArray2 = np.array(img2)
        if ImgArray2.shape.__len__() == 3:
            ImgArray2 = ImgArray2[:, :, 0]

        for i in range(height1):

            for j in range(width1):
                imgRew1[i, j] = ImgArray1[i, j]

        Image.fromarray((imgRew1)).show()

        for i in range(height2):
            for j in range(width2):
                if(Q == 0):
                    imgRew2[int(h_height*i),
                               int(round(w_width*j))+1] = ImgArray2[i,j]
                    Q = 1
                if(Q == 1):
                    imgRew2[int(round(h_height * i))+1,
                               int(w_width * j)] = ImgArray2[i, j]
                    Q = 0

        for i in range(Max_Height):
            for j in range(Max_Width):
                x = 0
                Value = 0
                temp[i, j] = imgRew2[i, j]
                if (imgRew2[i, j] < 1):
                    for y in range(-1, 2):
                        for z in range(-1, 2):
                            if ((i + y) > (height1 - 2)) | ((i + y) < 0):
                                oX = i
                            else:
                                oX = (i + y)


                            if ((j + z) > (width1 - 2)) | ((j + z) < 0):
                                oY = j
                            else:
                                oY = (j + z)


                            if imgRew2[oX, oY] > 0:
                                Value += imgRew2[oX, oY]
                                x += 1

                    temp[i, j] = Value / x
                    imgRew2[i, j] = temp[i, j]

        Image.fromarray((imgRew2)).show()
        im = Image.fromarray(imgRew2 * 255)
        im.convert('RGB')
        im.save("przetworzone/zad1/2" + str(N) + ".png")


    def GeometryczneRGB(self, img1, img2, N):

        imgArray1 = np.array(img1)
        imgArray2 = np.array(img2)
        imgArray1 = imgArray1[..., :3]
        imgArray2 = imgArray2[..., :3]

        height1 = img1.height
        width1 = img1.width
        height2 = img2.height
        width2 = img2.width

        if (width1 > width2):
            Max_Width = width1
        else:
            Max_Width = width2

        if (height1 > height2):
            Max_Height = height1
        else:
            Max_Height = height2

        img1X=int(round((Max_Width-width1)/2))
        img1Y=int(round((Max_Height-height1)/2))
        img2X = int(round((Max_Width-width2)/2))
        img2Y = int(round((Max_Height - height2) / 2))
        imgResult1=np.empty((Max_Height, Max_Width, 3), dtype=np.uint8)
        imgResult2=np.ones((Max_Height, Max_Width, 3), dtype=np.uint8)


        for i in range(0, Max_Height):
            for j in range(0, Max_Width):
                imgResult1[i,j]=(1, 1, 1)

        for i in range(0, height1):
            for j in range(0, width1):
                imgResult1[i+img1Y, j+img1X]=imgArray1[i,j]

        for i in range(0, Max_Height):
            for j in range(0, Max_Width):
                imgResult2[i, j] = (1, 1, 1)

        for i in range(0, height2):
            for j in range(0, width2):
                imgResult2[i + img2Y, j + img2X] = imgArray2[i, j]


        Image.fromarray((imgResult1)).show()
        Image.fromarray((imgResult2)).show()
        im = Image.fromarray(imgResult1)
        im.convert('RGB')
        im.save("przetworzone/zad1/3" + str(N) + ".png")

    def RozdzielczoscioweRGB(self, img1, img2, N):

        imgArray1 = np.array(img1)
        imgArray2 = np.array(img2)
        imgArray1 = imgArray1[..., :3]
        imgArray2 = imgArray2[..., :3]


        height1 = img1.height
        width1 = img1.width
        height2 = img2.height
        width2 = img2.width
        #maks wartosci
        if (width1 > width2):
            Max_Width = width1
        else:
            Max_Width = width2

        if (height1 > height2):
            Max_Height = height1
        else:
            Max_Height = height2

        img1X = width1 / width2
        img1Y = height1 / height2
        imgResult1=np.zeros((Max_Height, Max_Width, 3), dtype=np.uint8)
        imgResult2=np.zeros((Max_Height, Max_Width, 3), dtype=np.uint8)
        pom=np.zeros((Max_Height, Max_Width, 3), dtype=np.uint8)
        buff = 0

        for i in range(Max_Height):
            for j in range(Max_Width):
                imgResult1[i, j] = imgArray1[i, j]

        for i in range(height2):
            for j in range(width2):
                if buff == 0:
                    imgResult2[int(img1Y*i),
                               int(round(img1X * j)) +1]=imgArray2[i, j]
                    buff += 1
                if buff == 1:
                    imgResult2[int(round(img1Y * i))+1,
                               int(img1X * j)] = imgArray2[i, j]
                    buff = 0

        for i in range(Max_Height):
            for j in range(Max_Width):
                buff = 0
                red=0
                green=0
                blue=0
                pom[i, j]=imgResult2[i, j]

                if (imgResult2[i, j][0] < 1)\
                        & (imgResult2[i, j][1] < 1)\
                        & (imgResult2[i, j][2] < 1):
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            iValue = i if ((i + k) > (height1 - 2))\
                                          | ((i + k) < 0)\
                                else (i + k)
                            jValue = j if ((j + l) > (width1 - 2))\
                                          | ((j + l) < 0)\
                                else (j + l)
                            if (imgResult2[iValue, jValue][0] > 0)\
                                    | (imgResult2[iValue, jValue][1] > 0)\
                                    | (imgResult2[iValue, jValue][2] > 0):
                                red += imgResult2[iValue, jValue][0]
                                green += imgResult2[iValue, jValue][1]
                                blue += imgResult2[iValue, jValue][2]
                                buff += 1
                        pom[i, j] = (red / buff, green / buff, blue / buff)
                        imgResult2[i, j] = pom[i, j]
        Image.fromarray((imgArray2)).show()
        Image.fromarray((imgArray1)).show()
        Image.fromarray((imgResult2)).show()
        im = Image.fromarray(imgResult2)
        im.convert('RGB')
        im.save("przetworzone/zad1/4" + str(N) + ".png")