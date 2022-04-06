from tkinter import *
import math

expression1 = ''
expression2 = ''
value1 = ''
value2 = ''
operation = 0


def press(num):
    global expression1
    # There can be only one zero at beginning and only one dot
    if num == 0 and expression1 == '0':
        pass
    elif num == '.' and expression1.find('.') != -1:
        pass
    # If ane number is pressed in range 1-9 and actual value is 0, replace 0 with number
    elif num != 0 and num != '.' and len(expression1) == 1 and expression1.find('0') != -1:
        expression1 = expression1[:-1]
        expression1 = expression1 + str(num)
        equation.set(expression1)

    # Normal digit input
    else:
        expression1 = expression1 + str(num)
        equation.set(expression1)


def symbol(symb):
    global expression1
    global expression2

    if expression1 == '':
        pass
    elif expression1 != '' and expression2 == '':
        expression2 = expression1 + symb
        expression1 = ''
        equation.set(expression1)
        labtxt.set(expression2)
    elif expression1 != '' and expression2 != '':
        tmp = expression2 + expression1
        total = str(eval(tmp))
        expression2 = total + symb
        expression1 = ''
        equation.set(expression1)
        labtxt.set(expression2)


def equalpress():

    global expression1
    global expression2

    try:
        tmp = expression2 + expression1
        total = str(eval(tmp))
        expression1 = total
        expression2 = ''
        equation.set(total)
        labtxt.set(expression2)
    except:
        equation.set(" error ")
        expression1 = ""


def pow():
    global expression1
    global expression2

    if expression1 == '':
        pass
    elif expression1 != '' and expression2 == '':
        expression2 = str(expression1) + '**'
        expression1 = ''
        equation.set(expression1)
        labtxt.set(expression2)
    elif expression1 != '' and expression2 != '':
        tmp = expression2 + expression1
        total = str(eval(tmp))
        expression2 = total + '**'
        expression1 = ''
        equation.set(expression1)
        labtxt.set(expression2)



def clear():
    global expression1
    expression1 = ""
    equation.set(expression1)


def clearall():
    global expression1
    global expression2
    expression1 = ""
    expression2 = ''
    equation.set(expression1)
    labtxt.set(expression2)


def delete():
    global expression1
    expression1 = expression1[:-1]
    equation.set(expression1)


def invers():
    global expression1
    expression1 = (1 / float(expression1))
    equation.set(str(expression1))


def sqr():
    global expression1
    expression1 = math.sqrt(float(expression1))
    equation.set(str(expression1))


#def down(event):
    #global m


if __name__ == "__main__":
    GUI = Tk()
    GUI.geometry('280x400')
    GUI.title('Kalkulator')
    GUI.configure(bg='dark gray')
    GUI.resizable(False, False)

    equation = StringVar()
    labtxt = StringVar()

    frame = Frame(GUI)
    frame.place(x=25, y=20, height=60, width=230)
    lab = Label(frame, font=("", 10), bg='Light gray', textvariable=labtxt, anchor=E)
    lab.place(x=0, y=0, height=20, width=230)
    disp = Label(frame, font=("", 16), bg='Light gray', textvariable=equation, anchor=E)
    disp.place(x=0, y=20, height=40, width=230)

    bclr = Button(GUI, bg='red', fg='yellow', text="C", font=("", 14), command=clear)
    bclr.place(x=25, y=90, width=50, height=35)

    bcle = Button(GUI, bg='red', fg='yellow', text="CE", font=("", 14), command=clearall)
    bcle.place(x=85, y=90, width=50, height=35)

    bdel = Button(GUI, bg='red', fg='yellow', text="\u2190", font=("", 14), command=delete)
    bdel.place(x=145, y=90, width=50, height=35)

    bx2 = Button(GUI, bg='purple', fg='yellow', text="\u1d6a\u02b8", font=("", 14), command=pow)
    bx2.place(x=25, y=135, width=50, height=35)

    bsqr = Button(GUI, bg='purple', fg='yellow', text="\u221a", font=("", 14), command=sqr)
    bsqr.place(x=85, y=135, width=50, height=35)

    brcp = Button(GUI, bg='purple', fg='yellow', text="1/x", font=("", 14), command=invers)
    brcp.place(x=145, y=135, width=50, height=35)

    badd = Button(GUI, bg='purple', fg='yellow', text="+", font=("", 14), command=lambda: symbol('+'))
    badd.place(x=205, y=135, width=50, height=35)

    b7 = Button(GUI, bg='light grey', text="7", font=("", 14), command=lambda: press(7))
    b7.place(x=25, y=180, width=50, height=35)

    b8 = Button(GUI, bg='light grey', text="8", font=("", 14), command=lambda: press(8))
    b8.place(x=85, y=180, width=50, height=35)

    b9 = Button(GUI, bg='light grey', text="9", font=("", 14), command=lambda: press(9))
    b9.place(x=145, y=180, width=50, height=35)

    bsub = Button(GUI, bg='purple', fg='yellow', text="-", font=("", 14), command=lambda: symbol('-'))
    bsub.place(x=205, y=180, width=50, height=35)

    b4 = Button(GUI, bg='light grey', text="4", font=("", 14), command=lambda: press(4))
    b4.place(x=25, y=225, width=50, height=35)

    b5 = Button(GUI, bg='light grey', text="5", font=("", 14), command=lambda: press(5))
    b5.place(x=85, y=225, width=50, height=35)

    b6 = Button(GUI, bg='light grey', text="6", font=("", 14), command=lambda: press(6))
    b6.place(x=145, y=225, width=50, height=35)

    bmul = Button(GUI, bg='purple', fg='yellow', text="*", font=("", 14), command=lambda: symbol('*'))
    bmul.place(x=205, y=225, width=50, height=35)

    b1 = Button(GUI, bg='light grey', text="1", font=("", 14), command=lambda: press(1))
    b1.place(x=25, y=270, width=50, height=35)

    b2 = Button(GUI, bg='light grey', text="2", font=("", 14), command=lambda: press(2))
    b2.place(x=85, y=270, width=50, height=35)

    b3 = Button(GUI, bg='light grey', text="3", font=("", 14), command=lambda: press(3))
    b3.place(x=145, y=270, width=50, height=35)

    bdiv = Button(GUI, bg='purple', fg='yellow', text="/", font=("", 14), command=lambda: symbol('/'))
    bdiv.place(x=205, y=270, width=50, height=35)

    b0 = Button(GUI, bg='light grey', text="0", font=("", 14), command=lambda: press(0))
    b0.place(x=25, y=315, width=110, height=35)

    bdot = Button(GUI, bg='light grey', text=".", font=("", 14), command=lambda: press("."))
    bdot.place(x=145, y=315, width=50, height=35)

    beq = Button(GUI, bg='purple', fg='yellow', text="=", font=("", 14), command=equalpress)
    beq.place(x=205, y=315, width=50, height=35)

    #GUI.bind('<KeyPress>', down)
    #GUI.bind('<KeyRelease>', up)

    GUI.mainloop()
