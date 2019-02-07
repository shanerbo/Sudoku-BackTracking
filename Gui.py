from tkinter import *
from tkinter import messagebox
import Solver
class Gui:
    main = Tk()
    def __init__(self, grid):
        self.grid = grid
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
