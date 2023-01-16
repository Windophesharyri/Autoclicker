#45JKL^&42Ds
from tkinter import *
from tkinter import messagebox
import keyboard
import pyautogui
from time import sleep



def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Вы хотите выйти из приложения?"):
        gui.destroy()

def on_closing_2():
    if messagebox.askokcancel("Выход из приложения", "Вы хотите выйти из приложения?"):
        gui.destroy()

if __name__ == "__main__":
    gui = Tk()

    gui.configure(background = "black")

    gui.title("Autoclicker v.1")

    gui.geometry("400x300")
    gui.protocol("WM_DELETE_WINDOW", on_closing_2)
    gui.maxsize(400,300)
    gui.minsize(400,300)

    #gui.iconphoto = (True, 'cursor.ico')
    def Greetings():
        text = "Добро пожаловать в автокликер."
        text2 = "Нажмите кнопку для перехода в основной интерфейс."
        greetings_frame = Frame(gui,background = "black", pady = 65)
        greetings_frame.pack()
        greetings_label = Label(greetings_frame, text=text, justify = "center", wraplength=300, background = "black", foreground = "white", font = "KacstDigital, 20")
        greetings_label.pack()
        greetings_label = Label(greetings_frame, text=text2, justify = "center", wraplength=300, background = "black", foreground = "white", font = "KacstDigital, 13")
        greetings_label.pack()
        greetings_button = Button(greetings_frame, text = "Переход в меню", font = "KacstDigital, 13", command = proccess_window, background = "black", foreground = "white", relief= "groove", bd = 4)
        greetings_button.pack(pady = 10)
    
    def proccess_window():

        def clicker():
            while True:
                if keyboard.is_pressed(user_entry_proc.get()):
                    pyautogui.tripleClick()     
                if keyboard.is_pressed(user_entry_proc_1.get()):
                    break

        gui.withdraw()
        proccess_frame = Toplevel(gui)
        proccess_frame.title("Autoclicker v.1")
        proccess_frame.geometry("450x350")
        proccess_frame.protocol("WM_DELETE_WINDOW", on_closing_2)
        proccess_frame.maxsize(400,350)
        proccess_frame.minsize(400,350)
        
        canvas_proc = Canvas(proccess_frame,width = "400", height = "300", highlightthickness=0, bg = "black")
        canvas_proc.pack(fill = BOTH, expand = True)

        frame_proc = Frame(canvas_proc, bg = "black", pady = 5)
        frame_proc.pack()
        text_proc = "Для начала работы нажмите на клавишу"
        text_proc1 = "так же вы можете поставить горячую клавишу"

        label_proc = Label(frame_proc, text = text_proc, justify = "center", wraplength=300, background = "black", foreground = "white", font = "KacstDigital, 16", padx = 20 )
        label_proc.pack()
        label_proc = Label(frame_proc, text = text_proc1, justify = "center", wraplength=300, background = "black", foreground = "white", font = "KacstDigital, 12" )
        label_proc.pack()
        button_proc = Button(frame_proc, text="Кликать!", font = "KacstDigital, 12", command = clicker, background = "black", foreground = "white", relief= "groove", bd = 4)
        button_proc.pack(pady = 5)
        user_label_proc = Label(frame_proc, text = "Поставить клавишу", justify = "center", wraplength=300, background = "black", foreground = "white", font = "KacstDigital, 12" )
        user_label_proc.pack()
        user_text = StringVar()
        user_label_entry = Label(frame_proc, text = "Поставить клавишу начала", justify = "center", wraplength=300, background = "black", foreground = "white", font = "KacstDigital, 10" )
        user_label_entry.pack()
        string = StringVar
        user_entry_proc = Entry(frame_proc, textvariable = string,bg = "white", fg = "black", font = "KacstDigital, 15", width = 2)
        user_entry_proc.pack(padx = 5, pady = 5)
        user_label_entry_1 = Label(frame_proc, text = "Поставить клавишу паузы", justify = "center", wraplength=300, background = "black", foreground = "white", font = "KacstDigital, 10" )
        user_label_entry_1.pack()
        string1 = StringVar
        user_entry_proc_1 = Entry(frame_proc, textvariable = string1 , bg = "white", fg = "black", font = "KacstDigital, 15", width = 2)
        user_entry_proc_1.pack(padx = 5, pady = 5)
        user_entry_button = Button(frame_proc, text="Поставить бинды", height = 3, font = "KacstDigital, 12", background = "black", foreground = "white", relief= "groove", bd = 4, pady = 3)
        user_entry_button.pack()
    Greetings()
    gui.mainloop()