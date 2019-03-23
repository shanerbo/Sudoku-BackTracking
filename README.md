# Sudoku-BackTracking
Use Back Tracking to solve Sudoku.

### What is the purpose of this project?
Sudoku game was asked in one interview and I was unfimilar with the game itself and its implementation. This project aims to create a routine to resolve the problem and find the solution.

### How to implement it?
  1. Before assigning numbers, check if the number is valid to assign, the available numnbers are ranged from 1 to 9. 
  2. Assign numbers to empty cells. 
  3. Check if the number is not present in current row, column and 3x3 square([sudoku rule](http://www.counton.org/sudoku/rules-of-sudoku.php)). 
  4. If the number is good, recursively check if this assignment will lead to solution to Sudoku. 
  5. One problem that exits in Sudoku game is one can have more than one solutions.
  
### Big-O?
O(n^m) where n is row/column size of Sudoku (i.e.in classic Sudoku game, n is 9), m is the number of blank cells. 
  
### How to test it?
A simple UI is created for this problem using Tkinter. 0's represent for empty cells, you can type the corresponding numbers of an Sudoku question into that grid. After entering all data, you can just simply hit *solve* button to generate a solution for the Sudoku question.

### Any improvement?
Using dancing links with algorithm X to solve Sudoku will be faster than backtracking. It is hard to generate a sudoku question. Solving Sudoku is easier than generating one. Since when you create a new Sudoku grid, you need to check whether the grid is valid by finding a potential solution. If there is a solution exists, then the Sudoku is valid and solvable. 

## Sudoku Image Processing
Program can take an image of Sudoku as input and extract digits on the image and convert them to strings.
  
### Does it works?
It is too hard to make it work.
  * Bottleneck:
  1. Different resolution may vary the result.
  2. For different fonts, the accuracy changes. So far, the best score I have hit is 86% percent for a certain font.
  3. After getting binary clipped images, I need to feed them to the model I trained and convert back at the end, which has a high time complexity.


#### TODO:
  Make an iOS app that can solve Sudoku game.
  1. App can generate questions.(if it is hard to generate, we can store question on cloud)
  2. App can solve problems.
  3. App can cast image into grid(OCR) so that user do not need to manually type in problem(ARKit).
