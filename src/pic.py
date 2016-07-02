#!/usr/bin/env python

import cv2
import os
from PIL import Image
import Image
import ImageOps
import sys
import random

a = os.path.expanduser('~') +'/bad_pix/good_combined'
b = os.path.expanduser('~') +'/bad_pix/bad_combined'
#c = os.path.expanduser('~') +'/research_environment/round2/bad'

d = os.listdir(a)
d_s = sorted(d)
e= os.listdir(b)
e_s = sorted(e)
os.chdir(b)

#print d_s
#print e_s
#f = os.listdir(c)
'''
x = sorted(d)
y = sorted(e)
z = sorted(f)

print len(x)
print len(y)
print len(z)
'''
pth = '/home/allani/bad_pix/'

#im = cv2.imread('good_border' +'/' + str(i))
'''
#this loop is for combining images
print 'processing.......'

for i in range(len(d)):

	lst = [pth + 'good_cropped/'+ str(d_s[i]),pth + 'good_cropped/'+ str(d_s[i])]
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
'''
#c = sorted(b)
#print c
'''
#this loop is for combining consequitive images
lst =[i for i in range(len(d_s)) if i%2 == 1]
j=1
print 'processing......'
for i in lst:
	images = map(Image.open,[e_s[i-1],e_s[i]])
	widths,heights = zip(*(i.size for i in images))
	total_width = sum(widths)
	max_height = max(heights)
	new_im = Image.new('RGB',(total_width,max_height))
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

#this loop is add borders to images
for i in e_s:
	print i

	x = Image.open(i)
	y = ImageOps.expand(x,border=5,fill=190)
	y.save(str(i))

print 'done'

'''

'''

# this loop is for cropping images

for i in range(len(e_s)):
	image = cv2.imread(e_s[i])
	cropped = image[100:1000,350:1400]
	print cropped.shape
	print i
	cv2.imwrite(str(e_s[i]),cropped)
	#print image.shape
	#cv2.imshow('crop',cropped)
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
