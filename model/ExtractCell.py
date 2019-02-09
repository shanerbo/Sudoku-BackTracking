#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import pylab as pl
import numpy as np
import math

class Image2Sudoku:
    
    def __init__(self, imagePath):
        self.imagePath = imagePath
    
    def cropImage(self):
        gray_image = cv2.imread(self.imagePath, cv2.IMREAD_GRAYSCALE )
        '''This part of code is used for photo'''
        gray = cv2.GaussianBlur(gray_image,(1,1),8)
        #smooth the contours
        thresh = cv2.adaptiveThreshold(gray,225,1,1,11,8)
        temp, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        '''This part of code is used for photo'''
        area = []
        for i in contours:
            area.append(cv2.contourArea(i))
        index = area.index(max(area))
        axis_x = contours[index][:, 0, 0]
        axis_y = contours[index][:, 0, 1]
        corners = np.asarray([[[min(axis_x), min(axis_y)], 
                               [min(axis_x), max(axis_y)], 
                               [max(axis_x), max(axis_y)], 
                               [max(axis_x), min(axis_y)]]])
        # extract for corner points

        return gray[min(axis_y):max(axis_y), min(axis_x):max(axis_x)]
        
    def getCells(self):
        ret,black = cv2.threshold(self.cropImage(),100,255,cv2.THRESH_BINARY_INV)# binary black or white
        # black = cv2.bitwise_not(cropped) # for photo

        height, width = black.shape
        cellHeight = height//9
        cellWidth = width//9
        rows = []
        startHeight = 0
        for i in range(1, 10):
            rows.append(black[startHeight:i*cellHeight, 0:width])
            startHeight += cellHeight
        cells = {}
        counter = 0
        for i in rows:
            startWidth = 0
            for j in range(9):
                cell = i[0:cellHeight, startWidth: cellWidth+startWidth]
                cells[str(counter)] = self.cleanNoise(cell, cellWidth, cellHeight)
                startWidth += cellWidth
                counter += 1
        return cells
        
    def cleanNoise(self, cell, cellWidth, cellHeight):
        for i in range(cell.shape[0]):
            for j in range(cell.shape[1]):
                dist_center = np.sqrt(np.square(cellWidth // 2 - i) + np.square(cellHeight // 2 - j))
                if dist_center > cellWidth // 2 - (cellWidth + cellHeight)**(1./3.):
                    cell[i, j] = 0
        if np.sum(cell) == 0:
            return None        
        #return cv2.resize(cell[topMost: botMost, leftMost: rightMost], (50,50))
        active_px = np.argwhere(cell!=0)
        active_px = active_px[:,[1,0]]
        x,y,w,h = cv2.boundingRect(active_px)
        return cell[y:y+h, x:x+w]


