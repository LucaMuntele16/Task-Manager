import _tkinter
import random
import tkinter
from plyer import notification
import threading
import time

# Numele fișierului pentru stocare
FILENAME = "tasks.txt"


#Root Window
root = tkinter.Tk()

#Schimbam background-color la root - culoarea luata de pe palletes.shecodes.io/palettes/1225
root.configure(bg="#2c5d63")

#Schimbam titlul
root.title("Task-Manager w Reminders")

# Obține dimensiunile ecranului
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculează dimensiunile relative (de exemplu, 50% din lățime și 40% din înălțime)
relative_width = int(screen_width * 0.18)  # 18% din lățimea ecranului
relative_height = int(screen_height * 0.25)  # 25% din înălțimea ecranului

# Calculează poziția pentru centrare
x_position = (screen_width - relative_width) // 2
y_position = (screen_height - relative_height) // 2

# Setează dimensiunea și poziția ferestrei
root.geometry(f"{relative_width}x{relative_height}+{x_position}+{y_position}")

#Cream o lista goala
tasks = []



#Functii
def save_tasks():
    """Salvează lista de task-uri într-un fișier text."""
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")  # Scrie fiecare task pe o linie

def load_tasks():
    """Încarcă lista de task-uri dintr-un fișier text, dacă există."""
    global tasks
    try:
        with open(FILENAME, "r") as file:
            tasks = [line.strip() for line in file]  # Elimină spațiile goale
    except FileNotFoundError:
        # Dacă fișierul nu există, inițializăm cu o listă goală
        tasks = []

def set_reminder():
    """Setează un reminder pentru task-ul selectat."""
    task = lb_tasks.get("active")
    if not task:
        show_message("Selectează un task pentru reminder")
        return
    
    def reminder_notification():
        time.sleep(1 * 3)  # Așteaptă 3 secunde (1 * 3 secunde)
        notification.notify(
            title="Reminder Task",
            message=f"Nu uita să: {task}",
            timeout=10  # Afișează notificarea timp de 10 secunde
        )
    
    # Pornim un thread pentru reminder
    threading.Thread(target=reminder_notification, daemon=True).start()
    show_message(f"Reminder setat.")


def show_message(message):
    lbl_display["text"] = message
    lbl_display.grid()  # Afișează eticheta

def clear_message():
    lbl_display.grid_remove()  # Ascunde eticheta

def update_listbox():
    #Stergem lista curenta
    lbl_display["text"] = ""
    clear_listbox()
    #Populam listbox-ul
    for task in tasks:
        lb_tasks.insert("end",task)  #"end" il adauga la finalul cutiei de insert



def clear_listbox():
    lb_tasks.delete(0,"end") #sterge task-urile pe care le aveam deja trecute in variabila "tasks" ca sa nu se adauge de mai multe ori, de la 0 pana la final

def add_task():
    #Luam task-ul pe care il adaugam
    task = txt_input.get() #.get va lua ceea ce este scris in input
    #Adaugam task-ul
    if task != "":
        tasks.append(task)
        #Update
        update_listbox()
        save_tasks()
        clear_message()
    else:
        show_message("Te rog introduce un task.")
    txt_input.delete(0,"end") #Stergem ca sa nu ramana scrisa in continuarea eroarea
    
        
def del_all():
    #Lista trebuie schimbata din locala in globala
    global tasks
    #Stergem lista de taskuri
    tasks=[]
    #Update
    update_listbox()
    clear_message()
    save_tasks()

def del_one():
    #Luam text-ul de la task-ul selectat
    task = lb_tasks.get("active")
    #Confirmam ca este in lista
    if task in tasks:
        tasks.remove(task)
    #Update
    update_listbox()
    save_tasks()

def sort_asc():
    #Sortam ascendent
    tasks.sort()
    #Update
    update_listbox()

def sort_desc():
    #Sortam ascendent
    tasks.sort()
    #Inversam lista
    tasks.reverse()
    #Update
    update_listbox()
    

def show_number_of_tasks():
    #Luam numarul de task-uri - len = lungimea vectorului
    number_of_tasks = len(tasks)
    #Cream un mesaj
    msg = "Numarul de Task-uri: %s" %number_of_tasks
    #Afisam mesajul
    show_message(msg)  



lbl_title = tkinter.Label(root, text="Task-Manager", fg="#e0e0e0",bg="#283739")
lbl_title.grid(row=0,column=0,padx = 25)

lbl_display = tkinter.Label(root, text="", fg="#e0e0e0",bg="#283739")
lbl_display.grid(row=0,column=1,padx = 25)
lbl_display.grid_remove()

txt_input = tkinter.Entry(root, width=15,bg="#e0e0e0" )
txt_input.grid(row=1,column=1,padx = 25)

btn_add_task = tkinter.Button(root, text="Adauga Task", fg="#e0e0e0",bg="#283739", command=add_task)
btn_add_task.grid(row=1,column=0,padx = 25)

btn_del_all = tkinter.Button(root, text="Sterge Taskurile", fg="#e0e0e0",bg="#283739", command=del_all)
btn_del_all.grid(row=2,column=0,padx = 25)

btn_del_one = tkinter.Button(root, text="Sterge",fg="#e0e0e0",bg="#283739",  command=del_one)
btn_del_one.grid(row=3,column=0,padx = 25)

btn_sort_asc = tkinter.Button(root, text="Sorteaza Ascendent",fg="#e0e0e0",bg="#283739",  command=sort_asc)
btn_sort_asc.grid(row=4,column=0,padx = 25)

btn_sort_desc = tkinter.Button(root, text="Sorteaza Descendent",fg="#e0e0e0",bg="#283739",  command=sort_desc)
btn_sort_desc.grid(row=5,column=0,padx = 25)

btn_numbers_of_tasks = tkinter.Button(root, text="Numarul de Task-uri",fg="#e0e0e0",bg="#283739",  command=show_number_of_tasks)
btn_numbers_of_tasks.grid(row=6,column=0,padx = 25)

btn_exit = tkinter.Button(root, text="Iesire",fg="#e0e0e0",bg="#283739",  command=exit)
btn_exit.grid(row=8,column=0,padx = 25)

btn_reminder = tkinter.Button(root, text="Reminder", fg="#e0e0e0", bg="#283739", command=set_reminder)
btn_reminder.grid(row=7, column=0)


#List Box
lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=2, column=1, rowspan=7,padx=25)

load_tasks()
update_listbox()

root.mainloop()
