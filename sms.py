from  tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import requests
import bs4
import socket
import json
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import pandas as pd

def f1():
	root.withdraw()
	adst.deiconify()

def f2():
	adst.withdraw()
	root.deiconify()


def f3():
	root.withdraw()
	vist.deiconify()
	vist_stData.delete(1.0, END)
	con = None
	try:
                con = connect("gva.db")
                cursor = con.cursor()
                sql = "select * from student";
                cursor.execute(sql)
                data = cursor.fetchall()
                info = ""
                for d in data:
                        info = info + "rno =" + str(d[0]) + " name  = " + str(d[1]) + " " + "marks = " + str(d[2]) + "\n"
                vist_stData.insert(INSERT, info)
	except Exception as e:
                showerror("failure",e)
	finally:
                if con is not None:
                        con.close()

def f4():
	vist.withdraw()
	root.deiconify()

def f5():
	root.withdraw()
	upst.deiconify()

def f6():
	upst.withdraw()
	root.deiconify()

def f7():
	root.withdraw()
	delst.deiconify()

def f8():
	delst.withdraw()
	root.deiconify()

def f9():
	con = None
	x = 0
	error = False
	try:
		con = connect("gva.db")
		cursor = con.cursor()
		sql = "insert into student values('%d', '%s','%d')"
		
		
		try:
			x = int(adst_entRno.get())

		except Exception as es:
			showwarning("try again","please enter a roll number")
			print("LOG\t: Enter number")
			error = True
	
		print("LOG\t:start")
		if x < 0:
			print("LOG\t:Enter positive roll no")
			showwarning("try again","please enter a positive roll no")
			error = True
		elif x == 0 and not error:
			showwarning("try again","rollno cannot be zero")
			error = True
		else:
			rno = x
			print("LOG\t:rno is assigned")

		print("LOG\t:end")
		print("LOG\t:Exiting One")      
		y = 0
		try:
			y = adst_entName.get()
			print("LOG\t:started Second")
			if len(y) == 0:
				print("LOG\t:Enter name")
				showwarning("try again","please enter a name")
				error=True			
			elif len(y) < 2 or not y.isalpha():
				print("LOG\t:name les than 2")
				showwarning("try again","name should be minimum of two alphabets and only alphabets")
				error = True
			else:
				name = y
		except Exception as e1:
			showwarning("Exception :"+e)
			print("LOG\t: Error:\t "+e)
		
		print("LOG\t:ended Second")
		
		z=0
		
		try:
			z = int(adst_entMarks.get())
			print("LOG\t:started Third")
		except Exception as e3:
                        showwarning("try again","please enter  marks")
                        print("LOG\t:Marks not entered")
                        error = True
		
		if z < 0:
			showwarning("try again","Marks cannot be less than 0")
			print("LOG\t: MArks less than 0")
			error = True	
		elif z > 100:
			showwarning("try again","marks cannot be greater than 100")
			print("LOG\t: Marks greater than 100")
			error = True
		else:
			print("LOG\t: Marks assigned")
			marks = int(z)
		if not error:
			print("Executing..")
			args = (rno, name, marks)
			cursor.execute(sql % args)
			con.commit()
			showinfo("success","record inserted")

	except Exception as e:
		print("LOG\t: Exception")
		showerror("failure" ,e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
	
def f10():
	con = None
	error = False
	try:
		con = connect("gva.db")
		print("connected")
		
		b=0
		try:
			b = int(upst_entRno.get())
		
		except Exception as es:	
                        showwarning("try again","please enter a roll number")
                        error=True
		print("LOG\t:start")
		if b < 0:
			print("LOG\t:Enter positive roll no")
			showwarning("try again","please enter a positive roll no")
			error=True
		elif b == 0 and not error:
			showwarning("try again","rollno cannot be zero")
			error=True
		else:
			rno = b
			print("LOG\t:rno is assigned")
		print("LOG\t:end")
		print("LOG\t:Exiting One")
		try:
			c = upst_entName.get()
			print("LOG\t: started second")
			if len(c) == 0:
				print("LOF\t:Enter name")
				showwarning("try again","please enter a name")
				error = True
			elif len(c) < 2 or not c.isalpha():
				showwarning("try again","name should be minimum of two alphabets and must contain only alphabets")
				error = True
			else:
                        	name = c
		except Exception as e2:
			showwarning("Exception :" +e)
			print("LOG\t: Error:\t " +e)
		
		print("LOG\t:ended second")
		
		d = 0
		try:
			d = int(upst_entMarks.get())
		except Exception as es:
                        showwarning("try again","please enter marks")
                        error=True
		print("LOG\t:started Third")
		if d < 0:
			showwarning("try again","Marks cannot be less than 0")
			print("LOG\t: Marks less than 0")
			error = True
		elif d > 100:
			showwarning("try again","marks cannot be greater than 100")
			print("LOG\t: Marks greater than 100")
			error = True
		else:
			print("LOG\t: Marks assigned")
			marks = int(d)
		if not error:
			args =(name, marks, rno)
			cursor = con.cursor()
			sql = "update student set name = '%s', marks= '%d'  where rno = '%d' "
			cursor.execute(sql % args)
			if cursor.rowcount >= 1:
				con.commit()
				info = str(cursor.rowcount) + "record updated"
				showinfo("success", "record updated")
			else:
				showwarning("failed", "rno does not exists")
				
	
	except Exception as e:
		showerror("failure",e)
		con.rollback()	

	finally :
		if con is not None:
			con.close()
		

def f11():
	con = None
	a = 0
	error = False
	try:

		con = connect("gva.db")
		print("connected")
		try:
			a = int(delst_entRno.get())
		except Exception as e4:
                        showwarning("try again","please enter a roll number")
                        error=True
		if a == 0 and not error:
			showwarning("try again","rollno cannot be zero")
			error=True
		elif int(a) < 0:
			showwarning("try again","Roll no cannot be negative")
			error=True
		else:
			rno = int(a)
		if not error:
			args =(rno)
			cursor = con.cursor()
			sql = "delete from student where rno = '%d' "
			cursor.execute(sql % args)
			if cursor.rowcount >= 1:
				con.commit()
				info = str(cursor.rowcount) + "record deleted"
				showinfo("deleted", "record deleted")
			else:
				showwarning("Sorry", "rno not found")
				delst_entRno.delete(0,END)
				delst_entRno.focus()
	except Exception as e:
		showerror("failure",e)
		con.rollback()	

	finally :
		if con is not None :
			con.close()

def f12():
    con = sqlite3.connect("gva.db")
    cursor = con.cursor()
    st_query="Select * from student ORDER by marks DESC"
    cursor.execute(st_query)

    result=cursor.fetchmany(5)
    rno = []
    name = []
    marks = []

    for row in result:
        rno.append(row[0])
        str(name.append(row[1]))
        marks.append(row[2])
    
    barlist = plt.bar(name,marks)

    barlist[0].set_color('r')
    barlist[1].set_color('b')
    barlist[2].set_color('g')
    barlist[3].set_color('r')
    barlist[4].set_color('b')
    plt.title("Batch Information!")
    plt.ylabel("Marks")
    plt.xlabel("Students")
    plt.show()
    con.close()

    




res = requests.get("https://www.brainyquote.com/quote_of_the_day")
#print(res)

soup = bs4.BeautifulSoup(res.text, "lxml")
#print(soup)


data = soup.find("img", {"class" :"p-qotd"})
#print(data)


text = data['alt']
#print(text)


img_url = "https://www.brainyquote.com" + data["data-img-url"]
#print(img_url)


#res = requests.get(img_url)
#f = open("iml.jpg", "wb")
#f.write(res.content)
#f.close()

socket.create_connection( ("www.google.com", 80) )
#print("u r connected ")
res = requests.get("https://ipinfo.io")
#print(res)
data = res.json() # res into dict ==> key & value
#print(data)
city = data['city']
#print(city)
loc = data['loc']
#print(loc)
info = loc.split(",")
#print("lat = ", info[0])
#print("lon = ", info[1])
socket.create_connection( ("www.google.com", 80))
#city = input("enter location name")
	
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
# City Name CITY = "Hyderabad"
API_KEY = "ce7a0ad0ee042bbbd798eaa8e19bb887"
# updating the URL
URL = BASE_URL + "q=" + city + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)
# checking the status code of the request

# getting data in the json format
data = response.json()
# getting the main dict block
main = data['main']
# getting temperature
temperature = main['temp']
temp = temperature - 273.15
# getting the humidity
humidity = main['humidity']
# getting the pressure
pressure = main['pressure']
   # weather report
report = data['weather']
#print(f"{CITY:-^30}")
#print(f"Temperature: {temperature}")
#print(f"Humidity: {humidity}")
#print(f"Pressure: {pressure}")
#print(f"Weather Report: {report[0]['description']}")

	


root = Tk()
root.title("S. M. S. ")
root.geometry("650x800+300+0")
root.configure(bg='DarkSeaGreen1')
btnAdd = Button(root, text="Add", width = 10, font=("courier", 18, "bold"), command = f1)
btnView = Button(root, text="View", width = 10, font=("courier", 18, "bold"), command = f3)
btnUpdate = Button(root, text="Update", width = 10, font=("courier", 18, "bold"), command = f5)
btnDelete = Button(root, text="Delete", width = 10, font=("courier", 18, "bold"), command = f7)
btnCharts = Button(root, text="Charts", width = 10, font=("courier", 18, "bold"),command = f12)
frame2 = Frame(root)
frame2.pack()
upperframe = Frame(root,highlightbackground="black",highlightthickness=2,bg='DarkSeaGreen1')

upper_location = Label(upperframe, text = " Location: " + str(city) + "        " + "Temp: " + str(temp) +" " +".C", font=("courier",18),bg='DarkSeaGreen1',width=500,anchor=W,wraplength=685)



frame1 = Frame(root)
frame1.pack()
bottomframe = Frame(root,highlightbackground="black",highlightthickness=1,bg='DarkSeaGreen1')

bottom_location = Label(bottomframe, text = " QOTD: " + str(text), font=("courier",18),bg='DarkSeaGreen1',width=500,anchor=W,wraplength=685)



btnAdd.pack(pady=20)
btnView.pack(pady=20)
btnUpdate.pack(pady=20)
btnDelete.pack(pady=20)
btnCharts.pack(pady=20)
upperframe.pack()
upper_location.pack(pady=20)
bottomframe.pack()
bottom_location.pack(pady=20)

adst = Toplevel(root)
adst.title("Add st.")
adst.geometry("500x500+400+100")
adst.configure(bg='SlateGray1')
adst_lblRno = Label(adst, text = "enter rno ", font=("courier",18, "bold"))
adst_entRno = Entry(adst, bd=5, font=("courier",18, "bold"))
adst_lblName = Label(adst, text = "enter name ", font=("courier",18, "bold"))
adst_entName = Entry(adst, bd = 5, font=("courier",18, "bold"))
adst_lblMarks = Label(adst, text = "enter marks", font=("courier",18, "bold"))
adst_entMarks = Entry(adst, bd = 5, font=("courier",18, "bold"))
adst_btnSave = Button(adst, text = "Save ", font=("courier",18, "bold"),command=f9)
adst_btnBack = Button(adst, text = "Back ", font=("courier",18, "bold"), command=f2)


adst_lblRno.pack(pady=10)
adst_entRno.pack(pady=10)
adst_lblName.pack(pady=10)
adst_entName.pack(pady=10)
adst_lblMarks.pack(pady=10)
adst_entMarks.pack(pady=10)
adst_btnSave.pack(pady=10)
adst_btnBack.pack(pady=10)
adst.withdraw()


vist = Toplevel(root)
vist.title("View st. ")
vist.geometry("500x500+400+100")
vist.configure(bg='khaki1')

vist_stData = ScrolledText(vist, width=30, height=4, font=("courier", 18, "bold"))
vist_btnBack = Button(vist, text="Back", font=("courier", 18, "bold"), command=f4)


vist_stData.pack(pady=10)
vist_btnBack.pack(pady=10)
vist.withdraw()


upst = Toplevel(root)
upst.title("Update st.")
upst.geometry("500x500+400+100")
upst.configure(bg='PeachPuff2')
upst_lblRno = Label(upst, text = "enter rno ", font=("courier",18, "bold"))
upst_entRno = Entry(upst, bd=5, font=("courier",18, "bold"))
upst_lblName = Label(upst, text = "enter name ", font=("courier",18, "bold"))
upst_entName = Entry(upst, bd = 5, font=("courier",18, "bold"))
upst_lblMarks = Label(upst, text = "enter marks", font=("courier",18, "bold"))
upst_entMarks = Entry(upst, bd = 5, font=("courier",18, "bold"))
upst_btnSave = Button(upst, text = "Save ", font=("courier",18, "bold"),command=f10)
upst_btnBack = Button(upst, text = "Back ", font=("courier",18, "bold"),command=f6)


upst_lblRno.pack(pady=10)
upst_entRno.pack(pady=10)
upst_lblName.pack(pady=10)
upst_entName.pack(pady=10)
upst_lblMarks.pack(pady=10)
upst_entMarks.pack(pady=10)
upst_btnSave.pack(pady=10)
upst_btnBack.pack(pady=10)
upst.withdraw()

delst = Toplevel(root)
delst.title("Delete st.")
delst.geometry("500x500+400+100")
delst.configure(bg='LightBlue1')
delst_lblRno = Label(delst, text = "enter rno ", font=("courier",18, "bold"))
delst_entRno = Entry(delst, bd=5, font=("courier",18, "bold"))
delst_btnSave = Button(delst, text = "Save ", font=("courier",18, "bold"),command=f11)
delst_btnBack = Button(delst, text = "Back ", font=("courier",18, "bold"),command=f8)


delst_lblRno.pack(pady=10)
delst_entRno.pack(pady=10)
delst_btnSave.pack(pady=10)
delst_btnBack.pack(pady=10)
delst.withdraw()

root.mainloop()
