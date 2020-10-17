import cv2
import numpy as np
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-P", "--path", dest="path", default='../Imagens/Grayscale/67079.jpg', help="caminho da imagem")
parser.add_argument("-S", "--scale", dest="scale", default='4', help="valor da escala aplicada")
    
args = parser.parse_args()

path = args.path
image = cv2.imread(path, 1)
cv2.imshow("Imagem Original", image)

cv2.waitKey(0)
cv2.destroyAllWindows()