# Sudoku-BackTracking
## Use Back Tracking to solve Sudoku.
### What is the purpose of this project?
  I was asked to implement a Sudoku game in a interview. I was unfimiliar with the Sudoku game and the implementation of it. This project aims to create a routine that solves Sudoku games. One can learn a lot by implementing a Sudoku solver.
### How to implement it?
  1. Before assigning numbers, check if the number is valid to assign. 
  2. Assign numbers to empty cells. 
  3. Check if the number is not present in current row, column and 3x3 square([sudoku rule](http://www.counton.org/sudoku/rules-of-sudoku.php)). 
  4. If the number is good, recursively check if this assignment will lead to correct result. 
  5. One problem worth mentioning is that each Sudoku game may have multiple solutions.
### Big-O?
  O(n^m) where n is size of Sudoku (i.e.in classic Sudoku game, n is 9), m is the number of blank cells. Also solving sudoku is NP-Hard problem.
### How to test it?
  I created a simple UI for this program using Tkinter. 0's for empty cells, you can type any Sudoku question into that grid. After entering all data, you can just simply hit solve button, it will generate a solution for your Sudoku question.
### Any improvement?
  Using dancing links with algorithm X to solve Sudoku will be faster than backtracking. Also it is hard to generate a sudoku question. Solving is easy, generating is hard. You need to create a full sudoku grid, and check if it is valid.

## Sudoku Image Processing
  Program can take an image of sudoku as input. It could extract digits on image and convert them to strings.
### Does it works?
  GODDAMNIT. It is too hard to make it work.
  * Bottleneck:
  1. Different resolution may vary the result.
  2. For different fonts, the accuracy changes. So far, the best score I have hit is 86% percent for a certain font.
  3. After getting binary clipped images, I need to feed them to the model I trained and convert back at the end, which has a high time complexity.


#### TODO:
  Make an iOS app that can solve Sudoku game.
  1. App can generate questions.(if it is hard to generate, we can store question on cloud)
  2. App can solve problems.
  3. App can cast image into grid(OCR) so that user do not need to manually type in problem(ARKit).
