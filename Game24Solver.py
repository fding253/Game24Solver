# =============================================================================
#  Name:            Game24Solver
#  Purpose:         Determine whether a game of 24 is solveable.
#   
#  Author:          Winnie
#  Date Created:    Sun Jun  7 15:19:29 2020
# =============================================================================
import tkinter as tk
import itertools as it

class ReversePolishCalculator(object):
     """
     Calculate a postfix expression.
     """

     def __init__(self):
          pass


class Game24Solver(tk.Tk):
     """
     """
     def __init__(self):
          tk.Tk.__init__(self)

          # Create a label frame for user input
          self.entry_frame = tk.LabelFrame(self, text='Enter 4 numbers', bd=5)

          # Create four entry boxes
          self.e1 = tk.Entry(self.entry_frame)
          self.e4 = tk.Entry(self.entry_frame)
          self.e2 = tk.Entry(self.entry_frame)
          self.e3 = tk.Entry(self.entry_frame)

          # Place the entry boxes in the frame
          self.e1.grid(row=0, column=0)
          self.e2.grid(row=0, column=1)
          self.e3.grid(row=0, column=2)
          self.e4.grid(row=0, column=3)
          self.entry_frame.pack()

          # Add button to window
          self.b_run = tk.Button(text='Run', command=self.button_run)
          self.b_run.pack()


     def button_run(self):
          n1 = int(self.e1.get())
          n2 = int(self.e2.get())
          n3 = int(self.e3.get())
          n4 = int(self.e4.get())

          self.numbers = (n1, n2, n3, n4)

          self.solution = self.solver()
          print(self.solution)

          # Print message to window
          self.answer_box = tk.Text(self)
          self.answer_box.pack()
          if self.solution:
               self.answer_box.insert(tk.END, "Solution exists!\n")

               # Add button to show solutions
               self.b_soln = tk.Button(text="Show solutions?", command=self.display_solutions)
               self.b_soln.pack()

          return self.solution

     def display_solutions(self):
          """
          print solutions to window
          :return:
          """
          for s in self.solution:
               self.answer_box.insert(tk.END, s)
               self.answer_box.insert(tk.END, '\n')

     def solver(self):
          """

          :param numbers:
          :return:
          """
          return self.numbers


def tester(a, b, c, d):
     return a + b + c + d


if __name__ == "__main__":
     app = Game24Solver()
     app.mainloop()

     print(tester(1, 2, 1, 2))

