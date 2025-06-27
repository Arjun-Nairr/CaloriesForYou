import tkinter as k
from tkinter import messagebox
window1=k.Tk()
window1.title("choose your option")


selected=k.IntVar()
option1=k.Radiobutton(window1,text="Kilos to Lbs",variable=selected,value=1)
option1.pack(pady=5)

option2=k.Radiobutton(window1,text="Maintenance Calorie checker",variable=selected,value=2)
option2.pack(pady=5)

option3=k.Radiobutton(window1,text="Calorie deficit checker",variable=selected,value=3)
option3.pack(pady=5)


def open_popup():
    choicesh=selected.get()
    if choicesh==1:
        window=k.Toplevel()
        window.title("Kilogram to Pound Converter")
        label=k.Label(window,text="Enter Kilograms in digits")
        label.pack(pady=6)
        inp=k.Entry(window)
        inp.pack(pady=6)
        def converter():
            try:
                kg=float(inp.get())
                pounds=kg*2.2
                messagebox.showinfo("Result",f"{pounds} pounds")
            except ValueError:
                print("Entered value is invalid")
        button=k.Button(window,text="convert",command=converter)
        button.pack(pady=12)

        window.mainloop()


    if choicesh==2:
        window2=k.Toplevel()
        window2.title("Maintenance Checker")

        label2=k.Label(window2,text="Enter your weight (in lbs)")
        label2.pack(pady=6)

        inp2=k.Entry(window2)
        inp2.pack(pady=6)

        label3=k.Label(window2,text="Enter your height (in cms)")
        label3.pack(pady=6)
        inp3=k.Entry(window2)
        inp3.pack(pady=6)

        label4=k.Label(window2,text="Enter age")
        label4.pack(pady=6)
        inp4=k.Entry(window2)
        inp4.pack(pady=6)

        

        
        label5=k.Label(window2,text="Enter daily activity")
        label5.pack(pady=6)
        selection=k.IntVar()
        exercise=k.Radiobutton(window2,text="1x a week",variable=selection,value=1)
        exercise.pack(pady=5)
        exercise2=k.Radiobutton(window2,text="2x a week",variable=selection,value=2)
        exercise2.pack(pady=5)
        exercise3=k.Radiobutton(window2,text="3x a week",variable=selection,value=3)
        exercise3.pack(pady=5)
        exercise4=k.Radiobutton(window2,text="4x a week",variable=selection,value=4)
        exercise4.pack(pady=5)
        exercise5=k.Radiobutton(window2,text="5x a week",variable=selection,value=5)
        exercise5.pack(pady=5)
        exercise6=k.Radiobutton(window2,text="6-7x a week",variable=selection,value=6)
        exercise6.pack(pady=5)
        

        def maintenance():
            weightnumber=float(inp2.get())
            height=float(inp3.get())
            activity=selection.get()
            age=float(inp4.get())

            bmr=66+6.23*weightnumber+6.25*height-5*age

            if activity==1:
                maintenance=bmr*1.25
                messagebox.showinfo("Results",f"Your maintenace calories is {maintenance}")

            if activity==2:
                maintenance=bmr*1.3
                messagebox.showinfo("Results",f"Your maintenace calories is {maintenance}")

            if activity==3:
                maintenance=bmr*1.35
                messagebox.showinfo("Results",f"Your maintenace calories is {maintenance}")

            if activity==4:
                maintenance=bmr*1.4
                messagebox.showinfo("Results",f"Your maintenace calories is {maintenance}")

            if activity==5:
                maintenance=bmr*1.45
                messagebox.showinfo("Results",f"Your maintenace calories is {maintenance}")

            if activity==6:
                maintenance=bmr*1.45
                messagebox.showinfo("Results",f"Your maintenace calories is {maintenance}")

                
        button2=k.Button(window2,text="calculate",command=maintenance)
        button2.pack(pady=12)

        window2.mainloop()


    if choicesh==3:
            window3=k.Toplevel()
            window3.title("Deficit Checker")

            lab1=k.Label(window3,text="Enter your weight (in lbs)")
            lab1.pack(pady=6)

            inpp=k.Entry(window3)
            inpp.pack(pady=6)

            lab2=k.Label(window3,text="Enter your height (in cms)")
            lab2.pack(pady=6)
            inpp2=k.Entry(window3)
            inpp2.pack(pady=6)

            lab3=k.Label(window3,text="Enter age")
            lab3.pack(pady=6)
            inpp3=k.Entry(window3)
            inpp3.pack(pady=6)

            

            
            lab4=k.Label(window3,text="Enter daily activity")
            lab4.pack(pady=6)
            selection1=k.IntVar()
            exercisez=k.Radiobutton(window3,text="1x a week",variable=selection1,value=1)
            exercisez.pack(pady=5)
            exercisez2=k.Radiobutton(window3,text="2x a week",variable=selection1,value=2)
            exercisez2.pack(pady=5)
            exercisez3=k.Radiobutton(window3,text="3x a week",variable=selection1,value=3)
            exercisez3.pack(pady=5)
            exercisez4=k.Radiobutton(window3,text="4x a week",variable=selection1,value=4)
            exercisez4.pack(pady=5)
            exercisez5=k.Radiobutton(window3,text="5x a week",variable=selection1,value=5)
            exercisez5.pack(pady=5)
            exercisez6=k.Radiobutton(window3,text="6-7x a week",variable=selection1,value=6)
            exercisez6.pack(pady=5)
            

            def deficit():
                weightnumberz=float(inpp.get())
                heightz=float(inpp2.get())
                activityz=selection1.get()
                agez=float(inpp3.get())

                bmr=66+6.23*weightnumberz+6.25*heightz-5*agez-500

                if activityz==1:
                    deficit=bmr*1.25
                    messagebox.showinfo("Results",f"Your deficit calories is {deficit}")

                if activityz==2:
                    deficit=bmr*1.3
                    messagebox.showinfo("Results",f"Your deficit calories is {deficit}")

                if activityz==3:
                    deficit=bmr*1.35
                    messagebox.showinfo("Results",f"Your deficit calories is {deficit}")

                if activityz==4:
                    deficit=bmr*1.4
                    messagebox.showinfo("Results",f"Your deficit calories is {deficit}")

                if activityz==5:
                    deficit=bmr*1.45
                    messagebox.showinfo("Results",f"Your deficit calories is {deficit}")

                if activityz==6:
                    deficit=bmr*1.45
                    messagebox.showinfo("Results",f"Your deficit calories is {deficit}")

                    
            button3=k.Button(window3,text="calculate",command=deficit)
            button3.pack(pady=12)

            window3.mainloop()
            

            


submit_btn = k.Button(window1, text="Submit", command=open_popup)
submit_btn.pack(pady=10)

window1.mainloop()
        


