from tkinter import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("600x600+700+200")

        self.button_input = ""
        self.calculated_result = ""

        def button_click(num):
            self.button_input += str(num)
            self.display.config(text=self.button_input)

        def compute_result():
            self.calculated_result = str(eval(self.button_input))
            self.display.config(text=self.calculated_result)
            self.button_input = self.calculated_result

        def clear_display():
            self.button_input = ""
            self.display.config(text=self.button_input)

        self.display = Label(self.root, text="", width=30, height=2, font=("consolas", 20), bd=5, bg="white")
        self.display.pack()

        self.button_frame = Frame(self.root)
        self.button_frame.pack()
        
        self.button1 = Button(self.button_frame, text=1, height=6, width=9, command=lambda: button_click(1))
        self.button1.grid(row=0, column=0)
        self.button2 = Button(self.button_frame, text=2, height=6, width=9, command=lambda: button_click(2))
        self.button2.grid(row=0, column=1)
        self.button3 = Button(self.button_frame, text=3, height=6, width=9, command=lambda: button_click(3))
        self.button3.grid(row=0, column=2)
        self.add = Button(self.button_frame, text='+', height=6, width=9, command=lambda: button_click('+'))
        self.add.grid(row=0, column=3)

        self.button4 = Button(self.button_frame, text=4, height=6, width=9, command=lambda: button_click(4))
        self.button4.grid(row=1, column=0)
        self.button5 = Button(self.button_frame, text=5, height=6, width=9, command=lambda: button_click(5))
        self.button5.grid(row=1, column=1)
        self.button6 = Button(self.button_frame, text=6, height=6, width=9, command=lambda: button_click(6))
        self.button6.grid(row=1, column=2)
        self.minus = Button(self.button_frame, text='-', height=6, width=9, command=lambda: button_click('-'))
        self.minus.grid(row=1, column=3)

        self.button7 = Button(self.button_frame, text=7, height=6, width=9, command=lambda: button_click(7))
        self.button7.grid(row=2, column=0)
        self.button8 = Button(self.button_frame, text=8, height=6, width=9, command=lambda: button_click(8))
        self.button8.grid(row=2, column=1)
        self.button9 = Button(self.button_frame, text=9, height=6, width=9, command=lambda: button_click(9))
        self.button9.grid(row=2, column=2)
        self.multiply = Button(self.button_frame, text='*', height=6, width=9, command=lambda: button_click('*'))
        self.multiply.grid(row=2, column=3)

        self.button0 = Button(self.button_frame, text=0, height=6, width=9, command=lambda: button_click(0))
        self.button0.grid(row=3, column=0)
        self.decimal = Button(self.button_frame, text='.', height=6, width=9, command=lambda: button_click('.'))
        self.decimal.grid(row=3, column=1)
        self.equals = Button(self.button_frame, text='=', height=6, width=9, command=compute_result) 
        self.equals.grid(row=3, column=2)
        self.divide = Button(self.button_frame, text='/', height=6, width=9, command=lambda: button_click('/'))
        self.divide.grid(row=3, column=3)

        self.clear = Button(self.root, text='clear', height=6, width=18, command=clear_display)
        self.clear.pack()


def main():
    root = Tk()
    classInstance = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()