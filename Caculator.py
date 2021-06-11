import tkinter

test = tkinter.Tk()

test.title("Calculator")
test.geometry("300x500")
test.resizable(False, False)
entry = tkinter.Entry(fg = "gray19", bg = "snow", width = 40)
entry.place(x = 10, y = 10)
test.mainloop()
