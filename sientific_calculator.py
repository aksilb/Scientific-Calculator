from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title('Scientific Calculator')
root.config(background='powder blue')
root.resizable(width=True, height=True)
root.geometry('960x585+0+0')

calc = Frame(root)
calc.grid()


class Calc:
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def clear(self):
        self.result = False
        self.current = '0'
        self.display(0)
        self.input_value = True

    def clear_all(self):
        self.clear()
        self.total = 0

    def valid_function(self):
        if self.op == 'add':
            self.total += self.current
        if self.op == 'mc':
            self.total -= self.current
        if self.op == 'mp':
            self.total *= self.current
        if self.op == 'dv':
            self.total /= self.current
        if self.op == 'mod':
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def opperation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def pi(self):
        self.current = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.current = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.current = False
        self.current = math.e
        self.display(self.current)

    def tan(self):
        self.current = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.current = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.current = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.current = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def asinh(self):
        self.current = False
        self.current = math.asinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cos(self):
        self.current = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.current = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def acosh(self):
        self.current = False
        self.current = math.acosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.current = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def log_10(self):
        self.current = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.current = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.current = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.current = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def expm1(self):
        self.current = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    def lgamma(self):
        self.current = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

    def sq(self):
        self.current = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def pow2(self):
        self.current = False
        self.current = math.pow(float(txtDisplay.get()))
        self.display(self.current)

    def neg(self):
        self.current = False
        self.current = - (float(txtDisplay.get()))
        self.display(self.current)


add_value = Calc()

# =================Entry================ #

txtDisplay = Entry(calc, font=('arial', 20, 'bold'), bg='powder blue', bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, '0')

lblDisplay = Label(calc, text='Scientific Calculator \n\t\t By: Benhaoui', font=('arial', 18, 'bold'), bg='powder blue',
                   bd=30, width=28, justify=CENTER)
lblDisplay.grid(row=0, column=4, columnspan=4)
# ============Buttons===========#
numberpad = '123456789'
i = 0
btns = []
for j in range(2, 5):
    for k in range(3):
        btns.append(Button(calc, width=6, height=2, font=('arial', 20, 'bold'), bd=4, text=numberpad[i]))
        btns[i].grid(row=j, column=k, pady=1)
        btns[i]['command'] = lambda x=numberpad[i]: add_value.numberEnter(x)
        i += 1

# ==========================Standard Calculator===========================#


btnClear = Button(calc, text=chr(67), width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                  bg='powder blue', command=add_value.clear).grid(row=1, column=0, pady=1)
btnClearALL = Button(calc, text=chr(67) + chr(69), width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                     bg='powder blue', command=add_value.clear_all).grid(row=1, column=1, pady=1)
btnSq = Button(calc, text='√', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
               bg='powder blue', command=add_value.sq).grid(row=1, column=3, pady=1)
btnAdd = Button(calc, text='+', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg='powder blue', command=lambda: add_value.opperation('add')).grid(row=1, column=2, pady=1)
btnMc = Button(calc, text='-', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
               bg='powder blue', command=lambda: add_value.opperation('mc')).grid(row=2, column=3, pady=1)
btnMp = Button(calc, text='*', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
               bg='powder blue', command=lambda: add_value.opperation('mp')).grid(row=3, column=3, pady=1)
btnDv = Button(calc, text=chr(247), width=6, height=2, font=('arial', 20, 'bold'), bd=4,
               bg='powder blue', command=lambda: add_value.opperation('dv')).grid(row=4, column=3, pady=1)
btnEqu = Button(calc, text='=', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg='powder blue', command=add_value.sum_of_total).grid(row=5, column=3, pady=1)
btnNeg = Button(calc, text=chr(177), width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg='powder blue', command=add_value.neg).grid(row=5, column=2, pady=1)
btnZero = Button(calc, text='0', width=6, height=2, font=('arial', 20, 'bold'), bd=4
                 , command=lambda: add_value.numberEnter(0)).grid(row=5, column=1, pady=1)
btnDot = Button(calc, text='.', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg='powder blue', command=lambda: add_value.numberEnter('.')).grid(row=5, column=0, pady=1)

# ==========================Scientific Calculator===========================#


btnPi = Button(calc, text=chr(960), width=6, height=2, font=('arial', 20, 'bold'), bd=4,
               bg='powder blue', command=add_value.pi).grid(row=1, column=4, pady=1)
btn2Pi = Button(calc, text='2' + chr(960), width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg='powder blue', command=add_value.tau).grid(row=2, column=4, pady=1)
btnLog = Button(calc, text='log', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg='powder blue', command=add_value.log).grid(row=4, column=4, pady=1)
btnLog2 = Button(calc, text='log2', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                 bg='powder blue', command=add_value.log2).grid(row=4, column=5, pady=1)
btnLog10 = Button(calc, text='log10', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                  bg='powder blue', command=add_value.log_10).grid(row=5, column=4, pady=1)
btnCos = Button(calc, text='cos', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg='powder blue', command=add_value.cos).grid(row=1, column=5, pady=1)
btnCosh = Button(calc, text='cos' + chr(175) + chr(185), width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                 bg='powder blue', command=add_value.cosh).grid(row=2, column=5, pady=1)
btnExp = Button(calc, text='Exp', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg='powder blue', command=add_value.exp).grid(row=4, column=6, pady=1)
btnDeg = Button(calc, text='Deg', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg='powder blue').grid(row=3, column=4, pady=1)
btnLog1p = Button(calc, text='log1p', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                  bg='powder blue', command=add_value.log1p).grid(row=5, column=5, pady=1)
btnTan = Button(calc, text='tan', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg='powder blue', command=add_value.tan).grid(row=1, column=6, pady=1)
btnTanh = Button(calc, text='tan' + chr(175) + chr(185), width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                 bg='powder blue', command=add_value.tanh).grid(row=2, column=6, pady=1)
btnMod = Button(calc, text='Mod', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg='powder blue', command=add_value.valid_function).grid(row=3, column=5, pady=1)
btnAcosh = Button(calc, text='acoch', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                  bg='powder blue', command=add_value.acosh).grid(row=3, column=6, pady=1)
btnExpm1 = Button(calc, text='expm1', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                  bg='powder blue', command=add_value.expm1).grid(row=5, column=6, pady=1)
btnSin = Button(calc, text='sin', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg='powder blue', command=add_value.sin).grid(row=1, column=7, pady=1)
btnSinh = Button(calc, text='sin' + chr(175) + chr(185), width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                 bg='powder blue', command=add_value.sinh).grid(row=2, column=7, pady=1)
btn_e_ = Button(calc, text='e', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg='powder blue', command=add_value.e).grid(row=4, column=7, pady=1)
btnAsinh = Button(calc, text='asinh', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                  bg='powder blue', command=add_value.asinh).grid(row=3, column=7, pady=1)
btnLgamma = Button(calc, text='lgamma', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                   bg='powder blue', command=add_value.lgamma).grid(row=5, column=7, pady=1)


# ====================Menu================== #

def iExit():
    iExit = tkinter.messagebox.askyesno('Scientific Calculator', 'Confirm if you want to exit')
    if iExit != 0:
        root.destroy()
        return


def sCientific():
    root.resizable(width=True, height=True)
    root.geometry('960x585+0+0')


def sTandard():
    root.resizable(width=True, height=True)
    root.geometry('480x585+0+0')


menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Fill', menu=filemenu)
filemenu.add_command(label='Standard', command=sTandard)
filemenu.add_command(label='Scientific', command=sCientific)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=iExit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_command(label='Past')

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='View Help')

root.config(menu=menubar)
root.mainloop()
