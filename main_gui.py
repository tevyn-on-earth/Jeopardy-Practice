from tkinter import *
from tkinter.ttk import *
from create_cluedeck import *

# main window of application
main = Tk()

# creates the main window
main.title('Jeopardy! Practice')
main.geometry('1000x750')
main.minsize(1000, 750)
main['background']='#16208a'

# creates a deck of the specified number of clues
deck_size = 60
cluedeck = create_cluedeck(deck_size)

# initial index of the question
q_num = 0

# create style object and style objects
style = Style()
style.configure('TButton', font=('times new roman', 20, 'bold'))
style.configure('c.Label', font=('times new roman', 50, 'bold'), foreground='white', background='#16208a')
style.configure('qa.Label', font=('times new roman', 20, 'bold'), foreground='white', background='#16208a')

# category label shown at top of main window
c_sv = StringVar()
c_sv.set(cluedeck[q_num][0])
c_lbl = Label(main, textvariable=c_sv, style='c.Label', wraplength=1000, justify='center')
c_lbl.place(relx=0.5, rely=0.1, anchor='center')

# question label shown on main window
q_sv = StringVar()
q_sv.set(cluedeck[q_num][1])
q_lbl = Label(main, textvariable=q_sv, style='qa.Label', wraplength=1000, justify='center')
q_lbl.place(relx=0.5, rely=0.3, anchor='center')

# answer label shown on main window
a_sv = StringVar()
a_sv.set(cluedeck[q_num][2])
a_lbl = Label(main, textvariable=a_sv, style='qa.Label', wraplength=1000, justify='center')
a_lbl.place_forget()

# stores question count in a variable
def show_answer():
    a_lbl.place(relx=0.5, rely=0.45, anchor='center')

# shows the next question
def show_next():
    global q_num
    q_num += 1
    # hides the answer when entering the next question
    a_lbl.place_forget()
    # updates the labels for the category, question, and answer
    c_sv.set(cluedeck[q_num][0])
    q_sv.set(cluedeck[q_num][1])
    a_sv.set(cluedeck[q_num][2])

    # exits program once all clues are exhausted
    if q_num > deck_size:
        main.destroy()

# button to show the answer
answer_btn = Button(main, text='Show Answer', style='TButton', command=show_answer)
answer_btn.place(relx=0.4, rely=0.6, anchor='center')

# button to see next question
next_btn = Button(main, text='Next', style='TButton', command=show_next)
next_btn.place(relx=0.6, rely=0.6, anchor='center')

# run the gui
main.mainloop()
