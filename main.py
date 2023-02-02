from tkinter import *
from tkinter import messagebox
import time
import random
import tkinter


# Setup Tkinter
root = Tk(className=" YouRType ")
root.title("Speed Typing Test")
root.geometry('800x600')
frame = tkinter.Frame(root)
root.configure(bg='#DFD3C3')
# Setup fonts
root.option_add('*Label.font', 'Helvetica 20')
root.option_add('*Button.font', 'Helvetica 20')

game_ended = False
game_started = False
time0 = time.time()
count = 60
labels = []

# User Entry Box
user_entry = Entry(root, width=40, bg='#F8EDE3', fg='black')
user_entry.place(relx=0.5, rely=0.5, anchor=CENTER)
user_entry.focus()
user_answer = user_entry.get()

# Label for typo
typo = Label(root, height='3', text="Please type what is written below", width='40', bg='#F8EDE3', fg='red')
# Words Amount Label
words_amount = len(user_answer)
words_written = Label(root, bg='#F8EDE3')

# Speed Label
time_label = Label(root, text="Remaining Time: 60", bg='#F8EDE3')
time_label.place(relx=0.1, rely=0.2, anchor=W)

# Reset Entry Box
def reset_entry():
    global labels, time0
    for label in labels:
        label.destroy()
    labels = []
    user_entry.delete(0, "end")




# Resetting New Texts
def reset_writing_labels():
    global line, time0, words
    text = Label(root, height='3', width='40', bg='#F8EDE3', fg='black')
    text.place(relx=0.5, rely=0.4, anchor=CENTER)
    with open("textfile.txt", "r") as possible_texts:
        possible_lines = possible_texts.readlines()
        random_words = random.choice(possible_lines).split(" ")
        words = random.choices(random_words, k=7)
        line = ' '.join(words)
        text.config(text=line)

reset_writing_labels()


def check_answer():
    global words_amount, words_written
    if line == user_entry.get():
        reset_entry()
        words_amount += 7
        words_written.config(text="Words written: " + str(words_amount))
        reset_writing_labels()
        typo.destroy()
    else:
        typo.place(relx=0.5, rely=0.3, anchor=CENTER)


def count_down_timer():
    global game_started
    game_started = True
    time1 = time.time()
    count = round(61 - (time1 - time0))
    if count > 0:
        words_written.place(relx=0.5, rely=0.2, anchor=W)
        words_written.config(text = "Words written: " + str(words_amount))
        time_label.config(text=F"Remaining time: {count}")
        root.after(1000, count_down_timer)
        root.update()
        time.sleep(1)
    elif count <= 0:
        end_game()




def end_game():
    global game_ended, game_started
    game_ended = True
    game_started = False
    time_label.destroy()
    words_written.destroy()
    messagebox.showinfo(title="TIME IS UP!", message=f"Test is over, you typed {words_amount} words in 60 seconds.")



#  Button to Check Texts
check_button = Button(root, text="CHECK ANSWER", bg='#F8EDE3', fg='black', command=check_answer, relief=RAISED)
check_button.place(relx=0.5, rely=0.7, anchor=CENTER)

#  Start Button
start_button = Button(root, text="START", bg='#F8EDE3', fg='black', command=count_down_timer)
start_button.place(relx=0.5, rely=0.6, anchor=CENTER)

# Reset Button
reset_button = Button(root, text="RESET", bg="#F8EDE3", font="Helvetica 20", command=reset_entry, relief=RAISED)
reset_button.place(relx=0.2, rely=0.7, anchor=W)



root.mainloop()

# Results Label
global result_label
result_label = Label(root, text=f"Words per Minute : {words_amount}", fg="blue")
result_label.place(relx=0.5, rely=0.4, anchor=CENTER)

# Restart button
restart_button = Button(root, text= f"Restart", command=restart)
restart_button.place(relx=0.5, rely=0.6, anchor=CENTER)

def restart():
# Destroying unwanted widgets
    restart_button.destroy()
    result_label.destroy()

# Re-place writing labels.
    reset_writing_labels()




root.mainloop()