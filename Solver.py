
from tkinter import *
from tkinter import messagebox
import numpy as np
import cv2
import pylab as pl
import numpy as np

class Sudoku:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        
    def printGrid(self):
        for i in range(len(self.sudoku)):
            if i%3 == 0:
                print('.-----------------------.')
            for j in range(len((self.sudoku)[0])):
                if j%3 == 0:
                    print('|', end=' ')
                print(self.sudoku[i][j], end=' ')
                if j == 8:
                    print('|')
        print('.-----------------------.')
        
    def validCol(self, c, n):
        for i in range(len(self.sudoku)):
            if self.sudoku[i][c] == n:
                return False
        return True
    
    def validRow(self, r, n):
        for i in range(len(self.sudoku)):
            if self.sudoku[r][i] == n:
                return False
        return True
    
    def boxStartPoint(self, r, c):
        return (r//3)*3, (c//3)*3
    
    
    def validBox(self, r, c, n):
        boxRow, boxCol = self.boxStartPoint(r, c)
        for i in range(3):
            for j in range(3):
                if self.sudoku[boxRow+i][boxCol+j] == n:
                    return False
        return True
    
    def validEntry(self, r, c, n):
        if self.validCol(c, n) and self.validRow(r, n) and self.validBox(r, c, n):
            return True
        else:
            return False
        
    def findEntry(self, loc):
        for i in range(len(self.sudoku)):
            for j in range(len((self.sudoku)[0])):
                if self.sudoku[i][j] == 0:
                    loc[0] = i
                    loc[1] = j
                    return True
        return False

    def solver(self):
        loc = [0, 0]
        if not self.findEntry(loc):
            return True
        r = loc[0]
        c = loc[1]
        for i in range(1, 10):
            if self.validEntry(r, c, i):
                self.sudoku[r][c] = i
                if self.solver():
                    return True
                self.sudoku[r][c] = 0
        return False

    class gui:
    def __init__(self, grid):
        self.grid = grid
        main = Tk()
        main.geometry("270x300")
        entries = {}
        point = 0
        for a, i in zip(range(0, 270, 30), range(9)):
            for b, j in zip(range(0, 270, 30), range(9)):
                temp = Entry(main)
                temp.place(x=b, y=a, width=30, height=30)
                temp.insert(END, self.grid[i][j])
                entries[point] = temp
                point += 1
        def onPress():
            data = []
            for i, j in entries.items():
                entry = j.get()
                if (entry not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
                    messagebox.showinfo("Invalid Entry", "Entry cannot be" + entry)
                    return False
                data.append(int(j.get()))
            data = [data[i:i+9] for i in range(0, len(data),9)]
            answer = Sudoku(data)
            answer.solver()
            result = []
            for i in range(len(answer.sudoku)):
                for j in range(len(answer.sudoku)):
                    result.append(answer.sudoku[i][j])
            for i,j in entries.items():
                j.delete(0, END)
                j.insert(0,result[i])

        b = Button(main, text="Solve", command=onPress)
        b.pack(side=BOTTOM)
        main.mainloop()
if __name__ == '__main__':
    
    grid =  [[0,1,6,0,7,0,4,0,0], 
             [5,0,0,0,0,0,0,0,8], 
             [0,8,7,0,0,0,0,3,0], 
             [2,0,0,0,1,0,0,0,7], 
             [9,0,0,8,0,3,0,0,5], 
             [0,5,0,0,9,0,6,0,3], 
             [1,3,0,0,0,0,2,0,6], 
             [6,0,0,0,0,0,0,7,4], 
             [0,4,0,2,0,0,3,1,9]] 

    a = gui(grid)

	image = cv2.imread(r'C:\Users\e6ncbcy\Desktop\0.png')
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray_image,(1,1),5)
	#smooth the contours
	thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)
	temp, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

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
	#extract for corner points
	cv2.drawContours(image, [corners], 0, (0,255,0), 1)
	print(min(axis_y), max(axis_y), min(axis_x), max(axis_x))
	cropped = image[min(axis_y):max(axis_y), min(axis_x):max(axis_x)]

	# cv2.imshow('img',image)
	# cv2.waitKey(2000)
	# cv2.destroyAllWindows()
	# show boundary box
	black = cv2.bitwise_not(cropped) 
	cv2.imshow('img',black)
	cv2.waitKey(2000)
	cv2.destroyAllWindows()
	pl.imshow(black)
	height, width, channel = black.shape
	cellHeight = height//9
	cellWidth = width//9
	rows = []
	cols = []
	startHeight = 0
	for i in range(1, 10):
	    rows.append(black[startHeight:i*cellHeight, 0:width])
	    startHeight += cellHeight