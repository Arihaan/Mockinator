from tkinter import *

window = Tk()
window.title("Mockinator by @R!")
window.geometry('600x350')
window['bg'] = 'peachpuff2'

lbl = Label(window, text="Welcome to MoCkInAtOr", font=("Courier", 20), bg="peachpuff2", pady=15)
lbl.grid(column=18, row=22, columnspan=1, rowspan=20)

lbl2 = Label(window, text="Enter normal text:", bg="peachpuff2", font=("Calibri", 12))
lbl2.grid(column=4, row=300)

txt = Entry(window, width=60)
txt.grid(column=5, row=300, columnspan=500, rowspan=1, pady=10)
txt.focus()

out = ''

user_out = Entry(window, width=60)
user_out.grid(column=5, row=500, columnspan=500, rowspan=1, pady=20)


def clicked():
    global out
    user_out.delete(0, 'end')
    user_in = txt.get()
    input_arr = list(user_in)

    for i in range(len(input_arr)):
        if i % 2 == 0:
            input_arr[i] = input_arr[i].upper()

    out = ''.join(input_arr)
    user_out.insert(END, out)


btn = Button(window, text="Wreak havoc", command=clicked)
btn.grid(column=18, row=400, pady=15)

lbl3 = Label(window, text="MoCkInG TeXt:", bg="peachpuff2", font=("Calibri", 12))
lbl3.grid(column=4, row=500, pady=5)

lbl4 = Label(window, text="(Ctrl/Cmd + C to copy)", bg="peachpuff2", font=("Calibri", 9))
lbl4.grid(column=18, row=700)

lbl5 = Label(window, text="V1.1 Developed by @R! in Feb '21  <3", bg="peachpuff2", font=("Courier", 8))
lbl5.grid(column=18, row=3000, columnspan=1, pady=70)

window.mainloop()
