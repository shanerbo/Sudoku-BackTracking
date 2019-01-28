#!/usr/bin/env python
# coding: utf-8

# In[203]:


grid =  [[0,1,6,0,7,0,4,0,0], 
         [5,0,0,0,0,0,0,0,8], 
         [0,8,7,0,0,0,0,3,0], 
         [2,0,0,0,1,0,0,0,7], 
         [9,0,0,8,0,3,0,0,5], 
         [0,5,0,0,9,0,6,0,3], 
         [1,3,0,0,0,0,2,0,6], 
         [6,0,0,0,0,0,0,7,4], 
         [0,4,0,2,0,0,3,1,9]] 


# In[204]:


def printGrid(grid):
    for i in range(9):
        if i%3 == 0:
            print('.-----------------------.')
        for j in range(9):
            if j%3 == 0:
                print('|', end=' ')
            print(grid[i][j], end=' ')
            if j == 8:
                print('|')
    print('.-----------------------.')

def validCol(c, s, n):
    for i in range(9):
        if s[i][c] == n:
            return False
    return True

def validRow(r, s, n):
    for i in range(9):
        if s[r][i] == n:
            return False
    return True

def validBox(r, c, s, n):
    boxRow, boxCol = boxStartPoint(r, c)
    for i in range(3):
        for j in range(3):
            if s[boxRow+i][boxCol+j] == n:
                return False
    return True
    
def boxStartPoint(r, c):
    return (r//3)*3, (c//3)*3

def validEntry(r, c, s, n):
    if validCol(c, s, n) and validRow(r, s, n) and validBox(r, c, s, n):
        return True
    else:
        return False

def findEntry(grid, loc):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                loc[0] = i
                loc[1] = j
                return True
    return False

    


# In[205]:


def solver(grid):
    loc = [0, 0]
    if not findEntry(grid, loc):
        return True
    r = loc[0]
    c = loc[1]
    for i in range(1, 10):
        if validEntry(r, c, grid, i):
            grid[r][c] = i
            if solver(grid):
                return True
            grid[r][c] = 0
    return False


# In[198]:


solver(grid)


# In[206]:


printGrid(grid)


# In[207]:


from tkinter import *
from tkinter import messagebox
import numpy as np


# In[213]:


main = Tk()
main.geometry("270x300")
#grid = [['0' for i in range(9)] for i in range(9)]
entries = {}
point = 0
for a, i in zip(range(0, 270, 30), range(9)):
    for b, j in zip(range(0, 270, 30), range(9)):
        temp = Entry(main)
        temp.place(x=b, y=a, width=30, height=30)
        temp.insert(END, grid[i][j])
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
    solver(data)
    result = []
    for i in range(len(data)):
        for j in range(len(data)):
            result.append(data[i][j])
    for i,j in entries.items():
        j.delete(0, END)
        j.insert(0,result[i])

    
b = Button(main, text="Solve", command=onPress)
b.pack(side=BOTTOM)



main.mainloop()

