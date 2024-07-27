from tkinter import *
root=Tk()
root.title("Flight Details")
root.geometry("800x600+0+0")
#INTERFACE!!
##   X = label
##   E = entry
x1 = Label(root,text="Welcome to our Airlines",font=("Helvetica",24)).place(x=200,y=0)
x2 = Label(root,text="From",font=24).place(x=50,y=50)
E1 = Entry(root)
E1.place(x=50,y=80)
x3 = Label(root,text="To",font=24).place(x=50,y=120)
E2 =Entry(root)
E2.place(x=50,y=150)
x4 =Label(root,text="Departure",font=24).place(x=50,y=190)
E3 =Entry(root)
E3.place(x=50,y=220)
x5 =Label(root,text="Return",font=24).place(x=50,y=260)
E4 =Entry(root)
E4.place(x=50,y=290)

x6 =Label(root,text="select type",font=24).place(x=50,y=320)
R1=Radiobutton(root,text="Economy",value=1,font=24).place(x=50,y=350)
R2=Radiobutton(root,text="First Class",value=2,font=24).place(x=50,y=380)
R3=Radiobutton(root,text="Buisness Class",value=3,font=24).place(x=50,y=410)


def book_flight():
    global phone
    booking_window = Tk()
    booking_window.title("Booking Details")
    booking_window.geometry("600x600")

    name_label =Label(booking_window, text="Name : ",font=24).place(x=50,y=80)
    name_entry = Entry(booking_window)
    name_entry.place(x=50,y=115)
    name=name_entry.get()

    Age_label =Label(booking_window,text="Age : ",font=24).place(x=50,y=145)
    Age_entry = Entry(booking_window)
    Age_entry.place(x=50,y=175)
    address_label =Label(booking_window,text="Address : ",font=24).place(x=50,y=205)
    address_entry =Entry(booking_window)
    address_entry.place(x=50,y=235)
    phone_no_label = Label(booking_window,text="Phone No : ",font=24).place(x=50,y=265)
    phone_no_entry =Entry(booking_window)
    phone_no_entry.place(x=50,y=295)


    
    
    def FI():
            
            final_interface = Tk()
            final_interface.title("Your Details")
            final_interface.geometry("600x600")
            Label(final_interface,text="Name: "+name_entry.get(),font=48).place(x=50,y=80)
            Label(final_interface,text="Age: "+Age_entry.get(),font=48).place(x=50,y=120)
            Label(final_interface,text="Address: "+address_entry.get(),font=48).place(x=50,y=160)
            Label(final_interface,text="Phone Num: "+phone_no_entry.get(),font=48).place(x=50,y=200)
            Label(final_interface,text="From: "+E1.get(),font=48).place(x=50,y=240)
            Label(final_interface,text="To: "+E2.get(),font=48).place(x=50,y=280)
            Label(final_interface,text="Departure: "+E3.get(),font=48).place(x=50,y=320)
            Label(final_interface,text="Return: "+E4.get(),font=48).place(x=50,y=360)
            button = Button(final_interface,text="Submit",font=48,command=final_interface.destroy,padx=50,pady=20).place(x=250,y=400)
            TTk = Label(final_interface, text="Thank You For Choosing Us \n Hope You Have A Wonderful Experience", font=("Helvetica", 24))
            TTk.pack(side="bottom")



    done_button = Button(booking_window, text="Done", command=FI, padx=50, pady=20).place(x=250, y=400)


book_button =Button(root, text="Next", command=book_flight,padx=50,pady=20,font=30).place(x=300,y=500)


root.mainloop()
