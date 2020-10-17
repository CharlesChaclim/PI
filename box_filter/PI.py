import cv2
import numpy as np
from argparse import ArgumentParser
import math

parser = ArgumentParser()
parser.add_argument("-P", "--path", dest="path", default='../Imagens/Grayscale/67079.jpg', help="caminho da imagem")
parser.add_argument("-S", "--scale", dest="scale", default='2', help="valor da escala aplicada")
    
args = parser.parse_args()

path = args.path
image = cv2.imread(path, 1)
cv2.imshow("Imagem Original", image)

scale = int(args.scale)

lin = []
for i in range(0,image.shape[0],scale):
	for j in range(0,image.shape[1],scale):
		lin.append(int(image[i:scale+i,j:scale+j].mean()))

FImage = np.repeat(np.repeat(np.array(np.reshape(lin,(math.ceil(image.shape[0]/scale),math.ceil(image.shape[1]/scale))), dtype=np.uint8), scale, axis=1), scale, axis=0)

cv2.imshow('Box filter', FImage)
cv2.waitKey(0)
cv2.destroyAllWindows()