#!/usr/bin/env python

import cv2
import os
from PIL import Image
import Image
import ImageOps
import sys
import random

a = os.path.expanduser('~') +'/research_environment/round2/good'
b = os.path.expanduser('~') +'/research_environment/round2/good_2'
c = os.path.expanduser('~') +'/research_environment/round2/bad'

d = os.listdir(a)
e= os.listdir(b)
f = os.listdir(c)

x = sorted(d)
y = sorted(e)
z = sorted(f)

print len(x)
print len(y)
print len(z)

pth = '/home/allani/research_environment/round2/'

#im = cv2.imread('good_border' +'/' + str(i))

print 'processing.......'

for i in range(len(x)):

	lst = [pth + 'good/'+ str(x[i]),pth + 'good_2/'+ str(y[i]),pth + 'bad/'+ str(z[i])]
	random.shuffle(lst)
	images = map(Image.open,lst)
	widths,heights = zip(*(i.size for i in images))
	total_width = sum(widths)
	max_height = max(heights)
	new_im = Image.new('RGB',(total_width,max_height))
	x_offset = 0

	for im in images:
		new_im.paste(im,(x_offset,0))
		x_offset += im.size[0]

	new_im.save(str(i)+'.jpg')

print 'done!'
#c = sorted(b)
#print c
#os.chdir(a)
'''
lst =[i for i in range(len(c)) if i%2 == 1]
j=1
print 'processing......'
for i in lst:
	images = map(Image.open,[c[i-1],c[i]])
	widths,heights = zip(*(i.size for i in images))
	total_width = sum(widths)
	max_heigth = max(heights)
	new_im = Image.new('RGB',)
	x_offset = 0

	for im in images:
		new_im.paste(im,(x_offset,0))
		x_offset += im.size[0]


	new_im.save(str(j)+'.jpg')
	j+=1
print 'done'
	#print c[i-1],c[i]
'''
'''
for i in b:
	print i

	x = Image.open(i)
	y = ImageOps.expand(x,border=5,fill=190)
	y.save(str(i))

print 'done'
'''


'''



for i in b:
	image = cv2.imread(i)
	cropped = image[100:1000,350:1400]
	print cropped.shape
	print i
	cv2.imwrite(i,cropped)
	#print image.shape
	#cv2.imshow('ori',image)
	#cv2.waitKey(0)

'''

'''
image = cv2.imread('1110-s.png')
cv2.imshow('original',image)
#cv2.waitKey(0)
print image.shape
#(1080, 1920, 3)

#r = 1000/image.shape[1]
#dim = (1000, int(image.shape[0]*r))
#resized = cv2.resize(image,dim,interpolation = cv2.INTER_AREA)
#cv2.imshow('resized',resized)
#
#
'''
'''
image = cv2.imread('1-1-1.png')
print 'image',image.shape
cropped = image[200:1000,350:1500]
cv2.imshow('cropped',cropped)
print 'cropped',cropped.shape
cv2.waitKey(0)
cv2.imwrite('example.png',cropped)

#(927, 1237, 3)
'''
