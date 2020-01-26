from tkinter import *
import os
# from PIL import Image, ImageTk
def save_info():
    firstname_info = firstname.get()
    #   lastname_info = lastname.get()
    #   age_info = age.get()
    #   age_info = str(age_info)
    # print(firstname_info)
    
    file = open("user.txt", "w")
    file.write(firstname_info)
    #   file.write(lastname_info)
    #   file.write(age_info)
    file.close()
    print(" User ", firstname_info, " has been registered successfully")
    
    firstname_entry.delete(0, END)
    os.system("Python display.py")
    # global root
    # import display
    screen.quit()
   
screen = Tk()
screen.geometry("750x750")
screen.title("Result")
heading = Label(text = "Result", bg = "grey", fg = "black", width = "500", height = "3")
heading.pack()
photo= PhotoImage(file="IIIT-N.png")
label1=Label(screen,image=photo)#.place(x=100,y=100)
label1.place(x=250,y=50)
screen.wm_iconbitmap('IIIT-N.ico')
firstname_text = Label(text = "Enrolment Number: * ",)
# lastname_text = Label(text = "Lastname * ",)
# age_text = Label(text = "Age * ",)
firstname_text.place(x = 330, y = 330)
# lastname_text.place(x = 15, y = 140)
# age_text.place(x = 15, y = 210)
 
 
firstname = StringVar()
# lastname = StringVar()
# age = IntVar()
 
firstname_entry = Entry(textvariable = firstname, width = "30")
# lastname_entry = Entry(textvariable = lastname, width = "30")
# age_entry = Entry(textvariable = age, width = "30")
 
firstname_entry.place(x = 300, y = 400)
# lastname_entry.place(x = 15, y = 180)
# age_entry.place(x = 15, y = 240)
 
register = Button(screen,text = "Submit", width = "15", height = "2", command = save_info, bg = "grey")
register.place(x = 330, y = 470)
mainloop()
screen.quit()
# import sys
# sys.exit()
