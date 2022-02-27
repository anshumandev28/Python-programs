from tkinter import *
main_windows = Tk()

#Labels
Label(main_windows, text="Enter your name:").grid(row = 0 , column = 0 )

Label(main_windows, text="Enter your age:").grid(row = 1 , column = 0)

# Text Input
your_name = Entry(main_windows, width= 50 , borderwidth = 5).grid(row = 0 , column = 1)

your_age = Entry(main_windows, width= 50 , borderwidth = 5).grid(row = 1 , column = 1)

def on_click():
    print(f"your name is {your_name}, and , your age is {your_age}")

#Buttons
Button(main_windows, text="Click Me", command=on_click).grid(row = 2, column = 1)

main_windows.mainloop()