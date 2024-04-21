from tkinter import *
import math
from pygame import mixer
import speech_recognition as sr

mixer.init()

def click(value):
    ex = entry_field.get()
    answer = ""

    try:
        if value == "C":
            ex = ex[0:len(ex)-1]
            entry_field.delete(0, END)
            entry_field.insert(0, ex)
            return
        elif value == "CE":
            entry_field.delete(0, END)
        elif value == "√":
            answer = math.sqrt(eval(ex))
        elif value == "π":
            answer = math.pi
        elif value == "cosθ":
            answer = math.cos(math.radians(eval(ex)))
        elif value == "sinθ":
            answer = math.sin(math.radians(eval(ex)))
        elif value == "tanθ":
            answer = math.tan(math.radians(eval(ex)))
        elif value == "2π":
            answer = 2 * math.pi
        elif value == "cosh":
            answer = math.cosh(eval(ex))
        elif value == "sinh":
            answer = math.sinh(eval(ex))
        elif value == "tanh":
            answer = math.tanh(eval(ex))
        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)
        elif value == "x\u02b8":
            entry_field.insert(END, "")
            return
        elif value == "x\u00B3":
            answer = eval(ex) ** 3
        elif value == "x\u00B2":
            answer = eval(ex) ** 2
        elif value == "ln":
            answer = math.log(eval(ex))
        elif value == "deg":
            answer = math.degrees(eval(ex))
        elif value == "rad":
            answer = math.radians(eval(ex))
        elif value == "e":
            answer = math.e
        elif value == "log₁₀":
            answer = math.log10(eval(ex))
        elif value == "x!":
            answer = math.factorial(ex)
        elif value == chr(247):
            entry_field.insert(END, "/")
            return
        elif value == "=":
            answer = eval(ex)
        else:
            entry_field.insert(END, value)
            return

        entry_field.delete(0, END)
        entry_field.insert(0, answer)
    except SyntaxError:
        pass

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def lcm(a, b):
    return math.lcm(a, b)

def hcf(a, b):
    return math.gcd(a, b)

operations = {'ADD': add, 'ADDITION': add, 'SUM': add, 'PLUS': add,
              'SUBTRACTION': sub, 'DIFFERENCE': sub, 'MINUS': sub, 'SUBTRACT': sub,
              'PRODUCT': mul, 'MULTIPLICATION': mul, 'MULTIPLY': mul,
              'DIVISION': div, 'DIV': div, 'DIVIDE': div,
              'LCM': lcm, 'HCF': hcf, 'MOD': mod, 'REMAINDER': mod, 'MODULUS': mod}

def findNumbers(t):
    l = []
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l

def audio():
    mixer.music.load("music2.mp3")
    mixer.music.play()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio_text = r.listen(source)
        try:
            print("Recognizing...")
            text = r.recognize_google(audio_text)
            print("You said:", text)
            entry_field.delete(0, END)
            entry_field.insert(0, text)
            text_list = text.split()
            for word in text_list:
                if word.upper() in operations.keys():
                    l = findNumbers(text_list)
                    result = operations[word.upper()](l[0], l[1])
                    entry_field.delete(0, END)
                    entry_field.insert(END, result)
                else:
                    pass
        except Exception as e:
            print("Error:", e)


root = Tk()
root.title("SADIA_Calculator")
root.config(bg="orchid")
root.geometry("680x486+100+100")

logoImage = PhotoImage(file="logo.png")
logoLabel =Label(root,image=logoImage,bg="orchid")
logoLabel.grid(row=0,column=0)

entry_field = Entry(root, font=("Arial", 20, "bold"), bg="Black", fg="white", bd=10, relief=SUNKEN, width=30)
entry_field.grid(row=0, column=0, columnspan=8)

micImage = PhotoImage(file="microphone.png")
mic_button =Button(root,image=micImage,bd=0,bg="orchid", command=audio)
mic_button.grid(row=0,column=7)


button_text_list = [
    "C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"
]
row_value = 1
column_value = 0
for i in button_text_list:
    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg="purple",
                    fg="white", font=("Arial", 18, "bold"), command=lambda button=i: click(button))
    button.grid(row=row_value, column=column_value, pady=1)
    column_value += 1
    if column_value > 7:
        row_value += 1
        column_value = 0

root.mainloop()