import cv2
import numpy as np
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--face", dest="face", default='1', help="face do cubo")
parser.add_argument("-i", dest="ies", default='0', help="i-ésima fatia")
    
args = parser.parse_args()

faceA = args.face
iesA = int(args.ies)

cube_dimension=255

if(faceA=='1'):
	face = [(j, i, 0) for i in range(255) for j in range(255)]
	ies  = [(j, i, 0+iesA) for i in range(255) for j in range(255)]
elif(faceA=='2'):
	face = [(i, 0, j) for i in range(255) for j in range(255)]
	ies  = [(i, 0+iesA, j) for i in range(255) for j in range(255)]
elif(faceA=='3'):
	face = [(255, j, i) for i in range(255) for j in range(255)]
	ies  = [(255-iesA, j, i) for i in range(255) for j in range(255)]
elif(faceA=='4'):
	face = [(i, 255, j) for i in range(255) for j in range(255)]
	ies  = [(i, 255-iesA, j) for i in range(255) for j in range(255)]
elif(faceA=='5'):
	face = [(0, j, i) for i in range(255) for j in range(255)]
	ies  = [(0+iesA, j, i) for i in range(255) for j in range(255)]
else:
	face = [(j, i, 255) for i in range(255) for j in range(255)]
	ies  = [(j, i, 255-iesA) for i in range(255) for j in range(255)]

FImage = np.array(np.reshape(face,(255,255,3)), dtype=np.uint8)
cv2.imshow("Face escolhida",FImage)

FImage = np.array(np.reshape(ies,(255,255,3)), dtype=np.uint8)
cv2.imshow("Face com Fatiamento",FImage)

cv2.waitKey(0)
cv2.destroyAllWindows()