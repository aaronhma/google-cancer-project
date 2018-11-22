import cv2
import os
import sys

height_of_images=[]
width_of_images=[]

def find_avg_dim(folder):
    	for filename in os.listdir(folder):
		img = cv2.imread(os.path.join(folder,filename),0)
		if img is not None:
			height, width = img.shape			
			height_of_images.append(height)		
			width_of_images.append(width)


avg_height=sum(height_of_images)/len(height_of_images)
avg_width=sum(width_of_images)/len(width_of_images)


def resize(folder): 
	for filename in os.listdir(folder):
		img = cv2.imread(os.path.join(folder,filename),0)
		if img is not None:
			resized = cv2.resize(img, (avg_width, avg_height), interpolation = cv2.INTER_AREA)
			cv2.imwrite(os.path.join(folder,filename),resized)