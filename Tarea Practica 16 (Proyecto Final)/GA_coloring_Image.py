import matplotlib.image as image
import numpy as npy

azul = [39, 219, 211]
amarillo = [219, 183, 18]
rosa = [219, 48, 189]


# < Crom: [98, 51, 201] Apt: 0.013 Gen: 6 >
# [Cerebro, Fondo, Tumor] Orden Vec Gen: 6
segmentacion = [azul, amarillo, rosa]
vec = [98, 51, 201]


# < Crom: [125, 183, 34] Apt: 0.013 Gen: 10 >
# [Cerebro, Tumor, Fondo] Orden Vec Gen: 10
# segmentacion = [azul, rosa, amarillo]
# vec = [125, 183, 34]


# < Crom: [201, 49, 99] Apt: 0.013 Gen: 13 >
# [Tumor, Fondo, Cerebro] Orden Vec Gen: 13
# segmentacion = [rosa, amarillo, azul]
# vec = [201, 49, 99]


ruta_Original = "Imagenes_Originales/"
nombre_Original = "Y254"
formato_Original = ".jpg"

ruta_Nueva = "Imagenes_Segmentadas/"
nombre_Nueva = nombre_Original + "_Segment"
version = "_01"
formato_Nueva = ".png"

ruta_Completa_Original = ruta_Original + nombre_Original + formato_Original
ruta_Completa_Nueva = ruta_Nueva + nombre_Nueva + version + formato_Nueva

imagen_Original = image.imread(ruta_Completa_Original)

w, h = imagen_Original.shape[:2]


imagen_Nueva = npy.zeros([w, h, 3])


def minkowsky(x, y):
    return abs(int(x) - int(y))


for i in range(w):
    for j in range(h):
        dist_pixel = []
        dist_pixel.append(minkowsky(imagen_Original[i][j][0], vec[0]))
        dist_pixel.append(minkowsky(imagen_Original[i][j][0], vec[1]))
        dist_pixel.append(minkowsky(imagen_Original[i][j][0], vec[2]))

        seg_index = dist_pixel.index(min(dist_pixel))

        if seg_index == 0:
            imagen_Nueva[i][j][0] = float(segmentacion[0][0] / 255.0)
            imagen_Nueva[i][j][1] = float(segmentacion[0][1] / 255.0)
            imagen_Nueva[i][j][2] = float(segmentacion[0][2] / 255.0)
        elif seg_index == 1:
            imagen_Nueva[i][j][0] = float(segmentacion[1][0] / 255.0)
            imagen_Nueva[i][j][1] = float(segmentacion[1][1] / 255.0)
            imagen_Nueva[i][j][2] = float(segmentacion[1][2] / 255.0)
        elif seg_index == 2:
            imagen_Nueva[i][j][0] = float(segmentacion[2][0] / 255.0)
            imagen_Nueva[i][j][1] = float(segmentacion[2][1] / 255.0)
            imagen_Nueva[i][j][2] = float(segmentacion[2][2] / 255.0)


image.imsave(ruta_Completa_Nueva, imagen_Nueva)
