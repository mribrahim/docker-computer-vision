
import numpy as np
import collections
import cv2
import dlib
import math
import argparse


def shape_to_np(shape, dtype="int"):
	# initialize the list of (x, y)-coordinates
	coords = np.zeros((68, 2), dtype=dtype)
 
	# loop over the 68 facial landmarks and convert them
	# to a 2-tuple of (x, y)-coordinates
	for i in range(0, 68):
		coords[i] = (shape.part(i).x, shape.part(i).y)
 
	# return the list of (x, y)-coordinates
	return coords



FACIAL_LANDMARKS_IDXS = collections.OrderedDict([
	("mouth", (48, 68)),
	("right_eyebrow", (17, 22)),
	("left_eyebrow", (22, 27)),
#	("right_eye", (36, 42)),
#	("left_eye", (42, 48)),
	("nose", (27, 35)),
	("jaw", (0, 17))
])
    


parser = argparse.ArgumentParser()
parser.add_argument("-f","--file", help="input image filename",required=True)
args = vars(parser.parse_args())


img = cv2.imread(args["file"])
	
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

         
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 


faces = detector(gray, 1)

for (i, rect) in enumerate(faces):
	
	cv2.rectangle(img,(rect.left(),rect.top()),(rect.right(),rect.bottom()),(255,0,255),2)
	
	face_length = rect.top()-rect.bottom()
	shape = predictor(gray, rect)
	shape = shape_to_np(shape)
	
	for (x, y) in shape:
		cv2.circle(img, (x, y), 1, (0, 0, 255), -1)

	center_points = {}
	for (name, (i, j)) in FACIAL_LANDMARKS_IDXS.items():

		points = shape[i:j]
		
		if 'jaw' == name:
			minindex = np.argmax(points[:,1])
			centroid = points[minindex]
		else :
			x = [p[0] for p in points]
			y = [p[1] for p in points]
			centroid = (sum(x) / len(points), sum(y) / len(points))
		
		cv2.putText(img, name, (int(centroid[0]), int(centroid[1])), cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 0, 255), 2)
 
		center_points[name] = centroid
                         

result = args["file"][:-4] + '-processed.jpg'						 
print("result image: ", result  ) 
cv2.imwrite( result,img)
 
print("program ended...")   