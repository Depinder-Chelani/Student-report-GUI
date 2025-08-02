import tkinter as tk
from tkinter import messagebox
import datetime

def clear_fields():
   text_input1.delete(0,tk.END)
   text_input2.delete(0,tk.END)
   text_input3.delete(0,tk.END)
   text_input4.delete(0,tk.END)
   text_input5.delete(0,tk.END)
   label9.config(text= "")
   text_input1.focus_set()

def generate_report():
    
    name = text_input1.get()
    rollno = text_input2.get()
    english = text_input3.get()
    science = text_input4.get()
    math = text_input5.get()

    if not name or not rollno or not english or not science or not math:  
        messagebox.showerror("Error", "Field cannot be empty!")
        label9.config(text="Field is empty")
        return
    
    try:

      english1 = float(english)
      science1 = float(science)
      math1 = float(math)
      if (english1 >= 0 and english1 <= 100) and (science1 >= 0 and science1<= 100) and (math1 >= 0 and math1 <= 100) :
        total = english1 + science1 +math1
           
        percentage = total /3
        if percentage >= 90:
           grade = "A"
        elif percentage >= 75:
           grade = "B"
        elif percentage >= 60:
           grade = "C"
        elif percentage >= 40:
           grade = "D"
        else:
           grade = "F"
      
        current_time = datetime.datetime.now()
        formatted_timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        with open("report_card.txt","a") as file:
            file.write("\n")
            file.write("Timestamp:"+formatted_timestamp+"\n")
            file.write("Name:"+name+"\n")
            file.write("Roll No:"+rollno+"\n")
            file.write("Total:"+str(total)+"\n")
            file.write("Percentage:"+str(percentage)+"\n")
            file.write("Grade:"+grade+"\n")
            file.write("--------------------------------------------")
        
        label9.config(text="Report generated in report_card.txt")

        
      else:
         messagebox.showerror("Error", "Marks should be between 0 - 100!")
         label9.config(text="Marks should be between 1 - 100")
         return
    except ValueError:
       messagebox.showerror("Error", "Marks should be numeric")
       label9.config(text="Marks should be numeric")
       return

      
       

root = tk.Tk()
root.geometry("500x500")
root.title("Student Report Card")

label1 = tk.Label(root,text="----------------------------------------------------------------")
label1.pack()
label2 = tk.Label(root,text="|                            STUDENT REPORT CARD                                |")
label2.pack()
label3 = tk.Label(root,text="----------------------------------------------------------------")
label3.pack()

form_frame = tk.Frame(root)
form_frame.pack(padx=10,pady=10)

label4 = tk.Label(form_frame,text="STUDENT NAME:",font=("Arial",10,"bold"))
label4.grid(row=0,column=0)
text_input1 = tk.Entry(form_frame)
text_input1.grid(row=0 , column=1)
label5 = tk.Label(form_frame,text="ROLL NUMBER  :",font=("Arial",10,"bold"))
label5.grid(row=1,column=0)
text_input2 = tk.Entry(form_frame)
text_input2.grid(row=1 , column=1)
marks_frame = tk.Frame(root)
marks_frame.pack(padx= 10,pady=10)
label6 = tk.Label(marks_frame,text="ENGLISH MARKS:",font=("Arial",10,"bold"))
label6.grid(row=0,column=0)
text_input3 = tk.Entry(marks_frame)
text_input3.grid(row=0 , column=1)
label7 = tk.Label(marks_frame,text="SCIENCE MARKS:",font=("Arial",10,"bold"))
label7.grid(row=1,column=0)
text_input4 = tk.Entry(marks_frame)
text_input4.grid(row=1 , column=1)
label8 = tk.Label(marks_frame,text="MATH MARKS   :",font=("Arial",10,"bold"))
label8.grid(row=2,column=0)
text_input5 = tk.Entry(marks_frame)
text_input5.grid(row=2 , column=1)
button_frame = tk.Frame(root)
button_frame.pack(padx=10,pady= 10)
button1 = tk.Button(button_frame,text="Generate report",font=("Arial",10,"bold"),command=generate_report)
button1.grid(row=0,column=1,padx= 30)
button2 = tk.Button(button_frame,text="Clear",font=("Arial",10,"bold"),command=clear_fields)
button2.grid(row=0,column=2,padx= 30)
report_frame = tk.Frame(root)
report_frame.pack(padx=10,pady=10)
label9 = tk.Label(report_frame)
label9.pack()





root.mainloop()