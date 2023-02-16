import tkinter as tk
import keyboard
import time


def shutdownall():

    # for i in range(10):
    keyboard.send("win")
    time.sleep(0.5)
    keyboard.send("Tab")
    # keyboard.send("alt + f4")
    for i in range(4):
        time.sleep(0.2)
        keyboard.press_and_release("DOWN")
    # keyboard.press_and_release("enter")


numm = ""
strr = []


def ocan():
    try:
        strr.pop()
        label["text"] = strr
    except IndexError:
        oclear()


def oclear():
    while strr:
        strr.pop()
    label["text"] = strr


def o1():
    strr.append('1')
    label["text"] = strr


def o2():
    strr.append('2')
    label["text"] = strr


def o3():
    strr.append('3')
    label["text"] = strr


def o4():
    strr.append('4')
    label["text"] = strr


def o5():
    strr.append('5')
    label["text"] = strr


def o6():
    strr.append('6')
    label["text"] = strr


def o7():
    strr.append('7')
    label["text"] = strr


def o8():
    strr.append('8')
    label["text"] = strr


def o9():
    strr.append('9')
    label["text"] = strr


def o0():
    strr.append('0')
    label["text"] = strr


def oplus():
    strr.append('+')
    label["text"] = strr


def ominus():
    strr.append('-')
    label["text"] = strr


def ostar():
    strr.append('*')
    label["text"] = strr


def odivide():
    strr.append('/')
    label["text"] = strr


def oequal():
    neww = ''
    for i in strr:
        neww = neww + i
    try:
        oe = eval(neww)
        label["text"] += "="
        time.sleep(0.1)
        label["text"] = oe
        while strr:
            strr.pop()
        strr.append(str(oe))
    except SyntaxError:
        print("")
        label["text"] = "Error"
    except ZeroDivisionError:
        label["font"] = "Calibri 25 bold"
        time.sleep(1)
        label["text"] = "Zero Cannot be divided by zero"
        time.sleep(1)
        label["font"] = "Calibri 50 bold"


t = tk.Tk()
t.title("Calculator")
hheight = 700
wwidth = 700
t.iconbitmap("C:\\Users\\Piyush\\Downloads\\g.ico")
swidth = t.winfo_screenmmwidth()
sheight = t.winfo_screenheight()

cx = int(swidth/2-wwidth/2)
cy = int(sheight/2-hheight/2)
canvas = tk.Canvas(t, height=hheight, width=wwidth, bg="purple")
canvas.pack()
t.resizable(False, False)
t.attributes('-alpha', 1)
# t.iconbitmap('.pathname')
# t.geometry('60x70+50+50')
frame = tk.Frame(t, bg="white")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)
message = tk.Label(frame, text="HI")
message.pack()
# boe=tk.Label(t, text="0", font="Caligraphy 22").place(anchor="s", relx=0.5, rely=0.5)
label = tk.Label(t, text="   ", bg="white", font='Calibri 50 bold')
label.place(anchor="s", relx=0.5, rely=0.5)
# while label["relx"] >= frame["relx"]:
#    iiii = 50
#    label["text"] = f"Calibri {iiii-1} bold"
a1 = tk.Button(t, text="1", padx=8, pady=9, fg="white", bg="black", activebackground="purple", activeforeground="red", command= o1)
a1.place(relheight=0.1, relwidth=0.2, relx=0.1, rely=0.5)
a2 = tk.Button(t, text="2", padx=8, pady=9, fg="white", bg="black", activebackground="purple", activeforeground="red", command=o2)
a2.place(relheight=0.1, relwidth=0.2, relx=0.3, rely=0.5)
a3 = tk.Button(t, text="3", padx=8, pady=9, fg="white", bg="black", activebackground="purple", activeforeground="red", command= o3)
a3.place(relheight=0.1, relwidth=0.2, relx=0.5, rely=0.5)
a4 = tk.Button(t, text="4", padx=8, pady=9, fg="white", bg="black", activebackground="purple", activeforeground="red", command=o4)
a4.place(relheight=0.1, relwidth=0.2, relx=0.7, rely=0.5)
a5 = tk.Button(t, text="5", padx=8, pady=9, fg="white", bg="black", activebackground="purple", activeforeground="red", command= o5)
a5.place(relheight=0.1, relwidth=0.2, relx=0.1, rely=0.6)
a6 = tk.Button(t, text="6", padx=8, pady=9, fg="white", bg="black", activebackground="purple", activeforeground="red", command=o6)
a6.place(relheight=0.1, relwidth=0.2, relx=0.3, rely=0.6)
a7 = tk.Button(t, text="7", padx=8, pady=9, fg="white", bg="black", activebackground="purple", activeforeground="red", command= o7)
a7.place(relheight=0.1, relwidth=0.2, relx=0.5, rely=0.6)
a8 = tk.Button(t, text="8", padx=8, pady=9, fg="white", bg="black", activebackground="purple", activeforeground="red", command=o8)
a8.place(relheight=0.1, relwidth=0.2, relx=0.7, rely=0.6)
a9 = tk.Button(t, text="9", padx=8, pady=9, fg="white", bg="black", activebackground="purple", activeforeground="red", command= o9)
a9.place(relheight=0.1, relwidth=0.2, relx=0.1, rely=0.7)
a0 = tk.Button(t, text="0", padx=8, pady=9, fg="white", bg="black", activebackground="purple", activeforeground="red", command=o0)
a0.place(relheight=0.1, relwidth=0.2, relx=0.3, rely=0.7)
apl = tk.Button(t, text="+", padx=8, pady=9, fg="white", bg="black", activebackground="purple", activeforeground="red", command=oplus)
apl.place(relheight=0.1, relwidth=0.2, relx=0.5, rely=0.7)
ami = tk.Button(t, text="-", padx=8, pady=9, fg="white", bg="black", activebackground="purple", activeforeground="red", command=ominus)
ami.place(relheight=0.1, relwidth=0.2, relx=0.7, rely=0.7)
amu = tk.Button(t, text="x", padx=8, pady=9, fg="white", bg="black", activebackground="purple", activeforeground="red", command=ostar)
amu.place(relheight=0.1, relwidth=0.2, relx=0.5, rely=0.8)
adi = tk.Button(t, text="/", padx=8, pady=9, fg="white", bg="black", activebackground="purple", activeforeground="red", command=odivide)
adi.place(relheight=0.1, relwidth=0.2, relx=0.7, rely=0.8)
aeq = tk.Button(t, text="=", padx=8, pady=9, fg="white", bg="black", activebackground="purple", activeforeground="red", command=oequal)
aeq.place(relheight=0.1, relwidth=0.2, relx=0.1, rely=0.8)
acl = tk.Button(t, text="Clear", padx=8, pady=9, fg="white", bg="black", activebackground="purple", activeforeground="red", command=oclear)
acl.place(relheight=0.1, relwidth=0.2, relx=0.3, rely=0.8)
acan = tk.Button(t, text="X", padx=8, pady=9, fg="white", bg="black", activebackground="purple", activeforeground="red", command=ocan)
acan.place(relheight=0.1, relwidth=0.8, relx=0.1, rely=0.9)
aaa = tk.Button(t, text="SHUTDOWN", padx=8, pady=9, fg="white", bg="black", activebackground="purple", activeforeground="red", command=shutdownall)
aaa.place(relheight=0.1, relwidth=0.8, relx=0.1, rely=0.1)
t.mainloop()