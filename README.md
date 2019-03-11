# Sudoku-BackTracking
## Use Back Tracking to solve Sudoku.
### Why?
  I was asked to implement a Sudoku game in a interview. I was unfimiliar with the Sudoku game and the implementation of it. This project aims to create a routine that solves Sudoku games. I believe there are lessons to be learned in implementing a Sudoku solver.
### How does it work?
  - Assign numbers to empty cells. 
  - Before assigning numbers, check if the number is valid to assign. 
  - Check if the number is not present in current row, column and 3x3 square([sudoku rule](http://www.counton.org/sudoku/rules-of-sudoku.php)). 
  - If the number is good, recursively check if this assignment will lead to correct result. 
  - One problem worth mentioning is that each Sudoku game may have multiple solutions.
### Big-O?
  O(n^m) where n is size of Sudoku (i.e.in classic Sudoku game, n is 9), m is blank cells. Also solving sudoku is NP-Hard problem.
### How to test it?
  I create a simple UI for this program using Tkinter. 0's for empty cells, you can type any Sudoku question into that grid. After entering all data, you can just simply hit solve button, it will generate a solution for you Sudoku question.
### Any improvement?
  Using dancing links with algorithm X to solve Sudoku will be much more faster than backtracking. Also it is hard to generate a sudoku question. Solving is easy, generating is hard. You need create a full sudoku grid, and check if it is valid.

## Sudoku Image Processing
  Program can take an image of sudoku as input. It could extract digits on image and convert them to string.
### How it works?
  God damn it. It is too hard to have it worked.
  * Bottleneck:
  1. Different resulotion may make result vary.
  2. For different fonts, the accuracy changes. So far, the best score I have hit is 86% percent for a certain font.
  3. After I got binary clipped images, I need to feed them to model I trained. The problem is I need to convert them into binary format again. Time complexity is high AF.


#### TODO:
  Make an iOS app that can solve Sudoku game.
  1. App can generate questions.(if it is hard to generate, we can store question on cloud)
  2. App can solve problems.
  3. App can cast image into grid(OCR) so that user do not need to manually type in problem(ARKit).
