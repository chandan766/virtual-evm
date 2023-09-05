from tkinter import *
from tkinter import messagebox,ttk
import time

def clear_windows():
	for widget in windows.winfo_children():
		widget.destroy()

def clock_counter():
		global second 
		counter_lbl.config(text= str(second))
		second -= 1
		counter_lbl.after(1000,clock_counter)
		
# ==========================================================================================
# signup / first windows ===V
# ==========================================================================================
def evm_setting1():
	# title 1st
	windows.title("Welcome to the EVM Software")
	# icon
	icon = PhotoImage(file = "img\\evmicon.png")
	windows.iconphoto(False,icon)
	windows.geometry("480x360+400+150")
	windows.resizable(width=False,height=False)
	windows.config(bg="#AA55FF")

	# frame in first/sign up window -----------------------------------
	global frame_input1
	frame_input1 = Frame(windows,bg="#AAFFFF",width=400,height=280,highlightbackground="black",highlightthickness=3)
	frame_input1.place(x=50,y=50,width=400,height=280)

	# sign up label on frame ---------------------------------------------
	av1 = Label(frame_input1,text="Sign Up",bg="red",borderwidth=2,fg="#ffff00",font=("times new roman",15,"bold"))
	av1.place(x=0,y=10,width=394)

	# username label ----------------------------------------------------
	av4 = Label(frame_input1,text="Username",borderwidth=2,bg="lightgray",fg="brown",font=("times new roman",12,"bold"))
	av4.place(x=70,y=70,width=120)

	# username entry ----------------------------------------------------
	av4_entry= Entry(frame_input1,bg="white",textvariable=u,fg="brown",font=("times new roman",12))
	av4_entry.place(x=200,y=70,width=120,height=25)
	av4_entry.focus() # use for cursor position on starting program

	# password label ----------------------------------------------------------
	av5 = Label(frame_input1,text="Password",borderwidth=2,bg="lightgray",fg="brown",font=("times new roman",12,"bold"))
	av5.place(x=70,y=100,width=120)

	# password entry ----------------------------------------------------------
	global av5_entry
	av5_entry= Entry(frame_input1,bg="white",textvariable=p,fg="brown",font=("times new roman",12),show="*")
	av5_entry.place(x=200,y=100,width=120,height=25)

	# confirm password label -------------------------------------------------- 
	conf_av5 = Label(frame_input1,text="Confirm Password",borderwidth=2,bg="lightgray",fg="brown",font=("times new roman",12,"bold"))
	conf_av5.place(x=70,y=130,width=120)

	# confirm password entry ---------------------------------------------------
	global conf_av5_entry
	conf_av5_entry= Entry(frame_input1,bg="white",textvariable=cp,fg="brown",font=("times new roman",12),show="*")
	conf_av5_entry.place(x=200,y=130,width=120,height=25)

	#show password
	global show_password
	show_password = Checkbutton(frame_input1,text="Show Password",variable=show_pass,bg="#AAFFFF",activebackground="#AAFFFF",onvalue=1,offvalue=0)
	show_password.place(x=200,y=160)
	show_password.bind("<Button-1>",on_enter_showPassword)
	
	# note label ----------------------------------------------------------------
	av6 = Label(frame_input1,text="* Username and Password are required to see\nthe result of election.",bg="#AAFFFF",fg="red",font=("goudy old style",10))
	av6.place(x=70,y=180)

	# next button of sign up/ first window ----------------------------------------- 
	global av7
	av7 = Button(frame_input1,activebackground="cyan",text="Next",borderwidth=2,bg="#55007F",fg="white",font=("times new roman",10,"bold"),command=next_)
	av7.place(x=160,y=220,width=60)
	windows.bind("<Return>",click)
	av7.bind("<Enter>",on_enter_next)
	av7.bind("<Leave>",on_leave_next)

	# contact us button ------------------------------------------------------------
	global av8
	av8 = Button(frame_input1,text="Contact us",borderwidth=0,bg="#AAFFFF",fg="brown",font=("times new roman",10,"bold"),command=contact_us)
	av8.place(x=20,y=248)
	av8.bind("<Enter>",on_enter_contact)
	av8.bind("<Leave>",on_leave_contact)

	# about button -----------------------------------------------------------------
	global av9
	av9 = Button(frame_input1,text="About",borderwidth=0,bg="#AAFFFF",fg="brown",font=("times new roman",10,"bold"),command=about)
	av9.place(x=340,y=248)
	av9.bind("<Enter>",on_enter_about)
	av9.bind("<Leave>",on_leave_about)

# ========================================================================================
# buttons and actions fuctions for sign up / first window
# next button on sign up / first windows ,for working with enter key press on keyboard----------------
def on_enter_showPassword(e):
	if show_pass.get()==0:
		av5_entry.config(show='')
		conf_av5_entry.config(show='')
	else:
		av5_entry.config(show='*')
		conf_av5_entry.config(show='*')
		

def next_():
	if u.get()=="" or p.get()=="" or cp.get()=="" :
		messagebox.showerror("Error","All fields are required!")
	elif p.get() != cp.get():
		messagebox.showerror("Error","Password and confirm password should be same!")
	else:
		frame_input1.destroy()
		evm_setting2()
   
# next button configuration
def on_enter_next(e):
	av7['bg'] = "red"
	av7['fg'] = "black"
	av7.config(font=("times new roman",12,"bold"))

def on_leave_next(e):
	av7['bg']= "#55007F"
	av7['fg'] = "white"
	av7.config(font=("times new roman",10))

# click binding with enter key on keyboard to hit next button-----------------------
def click(event):
	next_()

# about button ------------------------------------------------------------------
def about():
	av9.unbind("<Leave>")
	av9['fg'] = "red"
	av9.config(font=("times new roman",11,"bold"))
	global about_
	about_ = Toplevel(windows,bg="#DAF1F1",highlightbackground="black",highlightthickness=1)
	about_.overrideredirect(True)
	about_.geometry("380x100+600+505")
	about_.resizable(width=False,height=False)
	label_about = Label(about_,text="Hi,\nMy name is Chandan Maurya.I am a student of B.Tech(Cs).\nCurrently I working on python gui and many projects on it.\nIf you have interest to do some projects with me.",font=("times new roman",10,"bold"),bg="#DAF1F1",fg="blue")
	label_about.pack()
	btn_about1 = Button(about_,text="Click here",font=("times new roman",8,"bold"),bd=0,bg="#DAF1F1",fg="#120949",activebackground="#DAF1F1",command=click_here)
	btn_about1.place(x=315,y=45)
	btn_about = Button(about_,text="Ok",command=ok_btn)
	btn_about.pack()

def ok_btn():
	av9['fg']= "brown"
	av9.config(font=("times new roman",10))
	av9.bind("<Leave>",on_leave_about)
	about_.destroy()

def click_here():
	ok_btn()
	contact_us()
# about button configuration
def on_enter_about(e):
	av9['fg'] = "red"
	av9.config(font=("times new roman",11,"bold"))
def on_leave_about(e):
	av9['fg']= "brown"
	av9.config(font=("times new roman",10))

# contact us button --------------------------------------------------------------
def contact_us():
	av8.unbind("<Leave>")
	av8['fg'] = "red"
	av8.config(font=("times new roman",11,"bold"))
	global contact_
	contact_ = Toplevel(windows,bg="white",highlightbackground="black",highlightthickness=1)
	contact_.overrideredirect(True)
	contact_.geometry("340x100+400+505")
	contact_.resizable(width=False,height=False)
	label_contact = Label(contact_,text="For any feedback or copyright of resources(images) \nplease contact me...\nEmail: cr3992@gmail.com\nWhatsapp no: +919140026966",font=("times new roman",10,"bold"),bg="white",fg="blue")
	label_contact.pack()
	btn_contact = Button(contact_,text="Ok",command=ok_contact)
	btn_contact.pack()

def ok_contact():
	av8.bind("<Leave>",on_leave_contact)
	av8['fg']= "brown"
	av8.config(font=("times new roman",10))
	contact_.destroy()
# contact us button configuration
def on_enter_contact(e):
	av8['fg'] = "red"
	av8.config(font=("times new roman",11,"bold"))
	
def on_leave_contact(e):
	av8['fg']= "brown"
	av8.config(font=("times new roman",10))

# ==================================================================================
# second window V
# ================================================================================
def evm_setting2():
	# title 2nd 
	windows.title("Name setup")
	icon = PhotoImage(file = "img\\evmicon.png")
	windows.iconphoto(False,icon)
	windows.geometry("750x600+200+100")
	windows.resizable(width=False,height=False)
	windows.config(bg="#AA55FF")

	global frame_input
	frame_input = Frame(windows,bg="red",highlightbackground="red",highlightthickness=2)
	frame_input.place(x=300,y=50,width=400,height=30)

	 # names display label ------------------------------------------
	ab1 = Label(frame_input,text="Name of Candidates/Parties",font=("times new roman",15,"bold"),bg="#00FF00",fg="brown",justify=CENTER)
	ab1.place(x=0,y=2,width=394)

	# frame for adding name and add button------------------------------
	global frame_input2
	frame_input2 = Frame(windows,bg="red",highlightbackground="red",highlightthickness=3)
	frame_input2.place(x=20,y=200,width=255,height=80)
	# label for entry names----------------------------------------

	ab = Label(frame_input2,text="Enter the Name of Candidates/Parties",font=("times new roman",11,"bold"),bg="cyan",fg="brown",justify=CENTER,highlightbackground="green",highlightthickness=2)
	ab.place(x=0,y=2,width=247)

	# entry of names-------------------------------------------
	ab_entry = Entry(frame_input2,textvariable=name,font=("times new roman",11),bg="lightgray",fg="black",justify=CENTER)
	ab_entry.place(x=0,y=30,width=247)
	ab_entry.focus()

	# add button----------------------------------------
	global ab2
	ab2 = Button(frame_input2,activebackground="cyan",text="Add",font=("times new roman",10),bg="orange",fg="white",command=add)
	ab2.place(x=100,y=55,height=20)
	# ab2.bind("<Return>",on_press_enter)
	ab2.bind("<Enter>",on_enter_add)
	ab2.bind("<Leave>",on_leave_add)
	
	# frame for display names+++++++++++++++++++++++++++++++++++
	global frame_input3
	frame_input3 = Frame(windows,bg="white",highlightbackground="red",highlightthickness=3)
	frame_input3.place(x=300,y=80,width=400,height=370)
	wrapper1 = LabelFrame(frame_input3)

	global mycanvas
	mycanvas = Canvas(wrapper1)
	mycanvas.pack(side=LEFT,fill="both",expand="yes")
	yscrollbar = ttk.Scrollbar(wrapper1,orient="vertical",command=mycanvas.yview)
	yscrollbar.pack(side=RIGHT,fill='both')
	mycanvas.configure(yscrollcommand=yscrollbar.set)
	mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

	global myframe
	myframe = Frame(mycanvas,bg="white",width=380,height=840)
	mycanvas.create_window((0,0),window=myframe,anchor="nw")
	wrapper1.pack(fill="both",expand="yes")
	lst_name = Label(frame_input3,text="No.              Name                   Symbol",fg="black",bg="white",font=("times new roman",14,'bold'))
	lst_name.place(x=50,y=2)

	# next1 button -------------------------------------------------
	global frame_button
	frame_button = Frame(windows,bg='yellow',highlightbackground="red",highlightthickness=3)
	frame_button.place(x=300,y=448,width=400,height=48)
	global ab4
	ab4 = Button(frame_button,activebackground="cyan",text="Next",font=("times new roman",10),bg="#55007F",fg="white",command=next1)
	ab4.place(x=250,y=4)
	ab4.bind("<Enter>",on_enter_next1)
	ab4.bind("<Leave>",on_leave_next1)

	# clear button ------------------------------------------------
	global ab5
	ab5 = Button(frame_button,activebackground="cyan",text="Clear",font=("times new roman",10),bg="gray",fg="white",command=clear_)
	ab5.place(x=200,y=4)
	ab5.bind("<Enter>",on_enter_clear)
	ab5.bind("<Leave>",on_leave_clear)

	# go back-----------------------------------------------------
	global ab6
	ab6 = Button(frame_button,activebackground="cyan",text="Back",font=("times new roman",10),bg="black",fg="white",command=back2)
	ab6.place(x=150,y=4)
	ab6.bind("<Enter>",on_enter_back2)
	ab6.bind("<Leave>",on_leave_back2)

# ================================================================================
# functions of buttons of second window
# ================================================================================
def back2():
	bbb=messagebox.askyesno("Back","Do you want to go back?")
	if bbb==True:
		logout()

# add button ----------------------------------------------
def add():
		global a 
		global display
		global display1
		if name.get()!="":
			if len(list_name)>16:
				pass
			else: 
				if name.get().upper() not in list_name:
					a += 1
					high = a*50
					if a>16:
						messagebox.showwarning("Warning","EVM Machine can take maximum 16 Candidates/Parties at once")            
					else:
							if 11>a>6:
								mycanvas.yview_moveto('0.3')
							elif a>11:
								mycanvas.yview_moveto('0.6')

							name_ele = name.get().upper()

							display_count = Label(myframe,text=str(a)+".",fg="darkblue",bg="white",font=("times new roman",15,"bold"))
							display_count.place(x=55,y=high)
							display = Label(myframe,text=name_ele,cursor="arrow",state="normal",font=("times new roman",12,"bold"),justify=CENTER)
							display.place(x=120,y=high,height=30,width=150)
							display['bg']="#7CFC00"
							display['fg']="darkblue"
							display.config(bd=1)
							display1 = Label(myframe,image=pic[a-1],bg="#AAFFFF")
							display1.photo = pic[a-1]
							display1.place(x=300,y=high,width=35,height=30)
							list_name.append(name.get().upper())
							name.set("")  
				else:
					messagebox.showwarning("Warning",f"{name.get().upper()} is already exist!") 

# add button configuration
def on_enter_add(e):
	ab2['bg']="yellow"
	ab2['fg'] ="black"
	ab2.config(font=("times new roman",11,"bold"))

def on_leave_add(e):
	ab2['fg'] ="white"
	ab2['bg']="orange"
	ab2.config(font=("times new roman",10))

def on_press_enter(e):
	add()
		 
# clear button ----------------------------------------------------------------
def clear_():
	global a
	a = 0
	ques = messagebox.askyesno("Clear","Do you want to clear all?")
	if ques == True:
		name.set("")
		list_name.clear()
		frame_input.destroy()
		frame_input2.destroy()
		frame_input3.destroy()
		mycanvas.destroy()
		frame_button.destroy()
		next_()

# clear button configuration
def on_enter_clear(e):
	ab5['bg']="lightgray"
	ab5['fg']="black"
	ab5.config(font=("times new roman",11,"bold"))

def on_leave_clear(e):
	ab5['bg']="gray"
	ab5['fg']="white"
	ab5.config(font=("times new roman",10))

# next1 button --------------------------------------------------------------------
def next1():
	if len(list_name) != 1 and len(list_name) != 0:
		voter_id()
		d=1
		for ele in voterId_list:
			if len(voterId_list) != 0:
						high1 = d*50
						display_count = Label(myframe1,text=str(d)+".",fg="darkblue",bg="white",font=("times new roman",15,"bold"))
						display_count.place(x=55,y=high1)
						display = Label(myframe1,text=ele,cursor="arrow",font=("times new roman",15,"bold"),justify=CENTER)
						display.place(x=140,y=high1,height=30,width=150)
						display['bg']="lightgray"
						display['fg']="purple"
						display.config(bd=0)
						voterId.set("")
						d += 1
	
	elif len(list_name) == 1:
		messagebox.showwarning("Warning","Minimum 2 candidates are required")

	else:
		messagebox.showerror("Error","Please Enter the name of candidates")

# next1 button configuration  
def on_enter_next1(e):
	 ab4['bg'] = "red"
	 ab4['fg'] = "black"
	 ab4.config(font=("times new roman",12,"bold"))

def on_leave_next1(e):
	 ab4['fg'] = "white"
	 ab4['bg'] = "#55007F"
	 ab4.config(font=("times new roman",10))

def on_enter_back2(e):
	 ab6['bg'] = "lightgray"
	 ab6['fg'] = "black"
	 ab6.config(font=("times new roman",11,"bold"))

def on_leave_back2(e):
	 ab6['fg'] = "white"
	 ab6['bg'] = "black"
	 ab6.config(font=("times new roman",10))

# ================================================================================
# voters id entry
# ================================================================================
def voter_id():
	windows.title("Voter id")
	icon = PhotoImage(file = "img\\evmicon.png")
	windows.iconphoto(False,icon)
	windows.geometry("750x600+200+100")
	windows.resizable(width=False,height=False)
	windows.config(bg="#AA55FF")

	global frame_input4
	frame_input4 = Frame(windows,bg="red",highlightbackground="red",highlightthickness=2)
	frame_input4.place(x=300,y=50,width=400,height=30)

	# names display label ------------------------------------------
	ab1 = Label(frame_input4,text="Voter Id",font=("times new roman",15,"bold"),bg="#00FF00",fg="brown",justify=CENTER)
	ab1.place(x=0,y=2,width=394)

	# frame for adding id and add button------------------------------
	global frame_input5
	frame_input5 = Frame(windows,bg="cyan",highlightbackground="red",highlightthickness=3)
	frame_input5.place(x=20,y=200,width=255,height=80)
	# label for entry names----------------------------------------

	ab = Label(frame_input5,text="Enter the id of Voters",font=("times new roman",11,"bold"),bg="cyan",fg="brown",justify=CENTER,highlightbackground="green",highlightthickness=2)
	ab.place(x=0,y=2,width=247)
	# entry of id-------------------------------------------

	ab_entry = Entry(frame_input5,textvariable=voterId,font=("times new roman",11),bg="lightgray",fg="black",justify=CENTER)
	ab_entry.place(x=0,y=30,width=247)
	ab_entry.focus()

	# add button----------------------------------------
	global ab2
	ab2 = Button(frame_input5,activebackground="green",text="Add",font=("times new roman",10),bg="orange",fg="white",command=add1)
	ab2.place(x=100,y=55,height=20)
	ab2.bind("<Enter>",on_enter_add1)
	ab2.bind("<Leave>",on_leave_add1)
	
	# frame for display id+++++++++++++++++++++++++++++++++++
	global frame_input6
	frame_input6 = Frame(windows,bg="white",highlightbackground="red",highlightthickness=3)
	frame_input6.place(x=300,y=80,width=400,height=370)
	wrapper1 = LabelFrame(frame_input6)

	global mycanvas2
	mycanvas2 = Canvas(wrapper1)
	mycanvas2.pack(side=LEFT,fill="both",expand="yes")
	yscrollbar = ttk.Scrollbar(wrapper1,orient="vertical",command=mycanvas2.yview)
	yscrollbar.pack(side=RIGHT,fill='both')
	mycanvas2.configure(yscrollcommand=yscrollbar.set)
	mycanvas2.bind('<Configure>',lambda e: mycanvas2.configure(scrollregion=mycanvas2.bbox('all')))

	global myframe1
	myframe1 = Frame(mycanvas2,bg="white",width=380,height=50000)
	mycanvas2.create_window((0,0),window=myframe1,anchor="nw") 
	wrapper1.pack(fill="both",expand="yes")
	lst_name = Label(frame_input6,text=" No.                         ID                     ",fg="black",bg="white",font=("times new roman",16,'bold'))
	lst_name.place(x=50,y=2)

	# enter button -------------------------------------------------
	global frame_button1
	frame_button1 = Frame(windows,bg='yellow',highlightbackground="red",highlightthickness=3)
	frame_button1.place(x=300,y=448,width=400,height=48)

	global ab_bk
	ab_bk = Button(frame_button1,relief="raised",activebackground="cyan",text="Back",font=("times new roman",10),bg="black",fg="white",command=back)
	ab_bk.place(x=150,y=4)
	ab_bk.bind("<Enter>",on_enter_bk)
	ab_bk.bind("<Leave>",on_leave_bk)

	global ab4
	ab4 = Button(frame_button1,activebackground="cyan",text="Enter",font=("times new roman",10),bg="#55007F",fg="white",command=enter)
	ab4.place(x=250,y=4)
	ab4.bind("<Enter>",on_enter_enter)
	ab4.bind("<Leave>",on_leave_enter)

	# clear button for id------------------------------------------------
	global ab5
	ab5 = Button(frame_button1,activebackground="cyan",text="Clear",font=("times new roman",10),bg="gray",fg="white",command=clear1)
	ab5.place(x=200,y=4)
	ab5.bind("<Enter>",on_enter_clear1)
	ab5.bind("<Leave>",on_leave_clear1)

# ===============================================================================
# buttons
# ===============================================================================
def add1():
		global c 
		global display
		if voterId.get()!="":
			if voterId.get() not in voterId_list:
					c += 1
					high1 = c*50
					name_id = voterId.get()
					display_count = Label(myframe1,text=str(c)+".",fg="darkblue",bg="white",font=("times new roman",15,"bold"))
					display_count.place(x=55,y=high1)
					display = Label(myframe1,text=name_id,cursor="arrow",font=("times new roman",15,"bold"),justify=CENTER)
					display.place(x=140,y=high1,height=30,width=150)
					display['bg']="lightgray"
					display['fg']="purple"
					display.config(bd=0)
					voterId_list.append(voterId.get())
					voterId.set("")
			else:
				messagebox.showwarning("Warning",f"{voterId.get()} is already exist!")   
					
# add button configuration
def on_enter_add1(e):
	ab2['bg']="yellow"
	ab2['fg'] ="black"
	ab2.config(font=("times new roman",11,"bold"))

def on_leave_add1(e):
	ab2['fg'] ="white"
	ab2['bg']="orange"
	ab2.config(font=("times new roman",10))

# clear button ----------------------------------------------------------------
def clear1():
	global c
	c = 0
	ques = messagebox.askyesno("Clear","Do you want to clear all?")
	if ques == True:
		voterId.set("")
		voterId_list.clear()
		frame_input.destroy()
		frame_input2.destroy()
		frame_input3.destroy()
		mycanvas.destroy()
		frame_button.destroy()
		next1()
def on_enter_clear1(e):
	ab5['bg']="lightgray"
	ab5['fg']="black"
	ab5.config(font=("times new roman",11,"bold"))

def on_leave_clear1(e):
	ab5['bg']="gray"
	ab5['fg']="white"
	ab5.config(font=("times new roman",10))

def enter():
		if len(voterId_list) != 0:
			pos = [30,70,109,149,188,228,267,307,347,386,426,465,505,544,583,623]
			frame_input2.destroy()
			frame_input3.destroy()
			evm_machine()
			n= len(list_name)
			for i in range(0,n):
				disp5 = Label(frame_evm,text=list_name[i],font=("times new roman",10,"bold"),fg="black",bg="#F1E9F1")
				disp5.place(x=50,y=pos[i])
				disp6 = Label(frame_evm,image=pic[i])
				disp6.photo = pic[i]
				disp6.place(x=180,y=pos[i],width=35,height=25)
			popId()
		else:
			messagebox.showerror("Error","Please provide the ID")
	
def on_enter_enter(e):
	ab4['bg'] = "red"
	ab4['fg'] = "black"
	ab4.config(font=("times new roman",12,"bold"))

def on_leave_enter(e):
	ab4['bg']= "#55007F"
	ab4['fg'] = "white"
	ab4.config(font=("times new roman",10))  

def back():
	ans2=messagebox.askquestion("Back","Do you want to go back?\n")
	if ans2 == 'yes':
		frame_input.destroy()
		frame_input2.destroy()
		frame_input3.destroy()
		mycanvas.destroy()
		myframe.destroy()
		frame_button.destroy()
		evm_setting2()
		b = 1
		for ele in list_name:
			high = b*50
			if 11>b>6:
				mycanvas.yview_moveto('0.3')
			elif b>11:
				mycanvas.yview_moveto('0.6')
			display_count = Label(myframe,text=str(b)+".",fg="darkblue",bg="white",font=("times new roman",15,"bold"))
			display_count.place(x=55,y=high)
			display = Label(myframe,cursor="arrow",text=ele,font=("times new roman",12,"bold"),bd=0,justify=CENTER)
			display.place(x=120,y=high,height=30,width=150)
			display['bg']="#7CFC00"
			display['fg']="darkblue"
			display1 = Label(myframe,image=pic[b-1],bg="#AAFFFF")
			display1.photo = pic[b-1]
			display1.place(x=300,y=high,width=35,height=30)  
			b += 1

# configure back navigation button
def on_enter_bk(e):
	ab_bk.config(font=("times new roman",12,"bold"))
	ab_bk['bg'] = "lightgray"
	ab_bk['fg'] = "black"
def on_leave_bk(e):
	ab_bk.config(font=("times new roman",10,"bold"))
	ab_bk['bg'] = "black"
	ab_bk['fg'] = "white"
# =================================================================================
# third window / virtual evm
# =================================================================================
def evm_machine():
	# title 3rd
	windows.title("EVM Machine")
	icon = PhotoImage(file = "img\\evmicon.png")
	windows.iconphoto(False,icon)
	windows.geometry("400x720+250+10")
	windows.resizable(width=False,height=False)

	# Frame of evm ----------------------------------------------------------
	global frame_evm
	frame_evm = Frame(windows,bg="white")
	frame_evm.place(x=1,y=40,width=400,height=680)

	# background image of evm  
	global bg
	bg = PhotoImage(file = "img\\evm.png")
	bg_img = Label(frame_evm,image=bg).place(x=0,y=0)
	
	# # top frame of control buttons ++++++++++++++++++++++++++++++++++++++++++++++
	global frame_evm1
	frame_evm1 = Frame(windows,bg="cyan",highlightbackground="red",highlightthickness=1)
	frame_evm1.place(x=0,y=0,width=400,height=40)

	# # evm label on center -------------------------------------------------------
	global disp1_
	disp1 = Label(frame_evm1,text="EVM",justify=CENTER,font=("arial black",15,"bold"),bd=5,bg="orange",fg="#F8F8FF")
	disp1.place(x=160,y=4,width=80,height=30)
	disp1_ = Label(frame_evm1,text="off",justify=CENTER,font=("dungeon",12,"bold"),bd=5,bg="red",fg="white")
	disp1_.place(x=300,y=4,width=50,height=30)

	# =====*******Buttons defining **********==============
	global btn1
	global btn2
	global btn3
	global btn4
	global btn5
	global btn6
	global btn7
	global btn8
	global btn9
	global btn10
	global btn11
	global btn12
	global btn13
	global btn14
	global btn15
	global btn16
	
	# voting buttons
	btn1 = Button(frame_evm,bd=0,bg="#3C7D9B",state="disabled",activebackground="#7ABEDE",command=vote_btn1)
	btn1.place(x=320,y=30,width=48,height=23)
	
	btn2 = Button(frame_evm,bd=0,bg="#3C7D9B",state="disabled",activebackground="#7ABEDE",command=vote_btn2)
	btn2.place(x=320,y=70,width=48,height=23)
	btn3 = Button(frame_evm,bd=0,bg="#3C7D9B",state="disabled",activebackground="#7ABEDE",command=vote_btn3)
	btn3.place(x=320,y=109,width=48,height=23)
	btn4 = Button(frame_evm,bd=0,bg="#3C7D9B",state="disabled",activebackground="#7ABEDE",command=vote_btn4)
	btn4.place(x=320,y=149,width=48,height=23)
	btn5 = Button(frame_evm,bd=0,bg="#3C7D9B",state="disabled",activebackground="#7ABEDE",command=vote_btn5)
	btn5.place(x=320,y=188,width=48,height=23)
	btn6 = Button(frame_evm,bd=0,bg="#3C7D9B",state="disabled",activebackground="#7ABEDE",command=vote_btn6)
	btn6.place(x=320,y=228,width=48,height=23)
	btn7 = Button(frame_evm,bd=0,bg="#3C7D9B",state="disabled",activebackground="#7ABEDE",command=vote_btn7)
	btn7.place(x=320,y=267,width=48,height=23)
	btn8 = Button(frame_evm,bd=0,bg="#3C7D9B",state="disabled",activebackground="#7ABEDE",command=vote_btn8)
	btn8.place(x=320,y=307,width=48,height=23)
	btn9 = Button(frame_evm,bd=0,bg="#3C7D9B",state="disabled",activebackground="#7ABEDE",command=vote_btn9)
	btn9.place(x=320,y=347,width=48,height=23)
	btn10 = Button(frame_evm,bd=0,bg="#3C7D9B",state="disabled",activebackground="#7ABEDE",command=vote_btn10)
	btn10.place(x=320,y=386,width=48,height=23)
	btn11 = Button(frame_evm,bd=0,bg="#3C7D9B",state="disabled",activebackground="#7ABEDE",command=vote_btn11)
	btn11.place(x=320,y=426,width=48,height=23)
	btn12 = Button(frame_evm,bd=0,bg="#3C7D9B",state="disabled",activebackground="#7ABEDE",command=vote_btn12)
	btn12.place(x=320,y=465,width=48,height=23)
	btn13 = Button(frame_evm,bd=0,bg="#3C7D9B",state="disabled",activebackground="#7ABEDE",command=vote_btn13)
	btn13.place(x=320,y=505,width=48,height=23)
	btn14 = Button(frame_evm,bd=0,bg="#3C7D9B",state="disabled",activebackground="#7ABEDE",command=vote_btn14)
	btn14.place(x=320,y=544,width=48,height=23)
	btn15 = Button(frame_evm,bd=0,bg="#3C7D9B",state="disabled",activebackground="#7ABEDE",command=vote_btn15)
	btn15.place(x=320,y=583,width=48,height=23)
	btn16 = Button(frame_evm,bd=0,bg="#3C7D9B",state="disabled",activebackground="#7ABEDE",command=vote_btn16)
	btn16.place(x=320,y=623,width=48,height=23)
	
	global ind
	ind = PhotoImage(file = "img\\indic.png")
	global indc
	# indc = Label(frame_evm,image=ind,bd=-1,bg="#F1E9F1")
	# indc.photo = ind
	indc = Label(frame_evm,text="◄",fg="red",bd=0,font=("times new roman",13,"bold"))

def on_enter_lock(e):
	global label_info
	label_info = Label(popId1,text="Click to Unlock/lock all \ncontrol buttons of this panel/move this panel",height=2,font=("times new roman",10,"bold"),bg="lightgray",fg="black")
	label_info.place(x=180,y=60)

def on_leave_lock(e):
	label_info.destroy()

def dragwin(event):
	x = popId1.winfo_pointerx()-popId1._offsetx
	y = popId1.winfo_pointery()-popId1._offsety
	popId1.geometry('+{x}+{y}'.format(x=x,y=y))

def clickwin(event):
	popId1._offsetx= event.x
	popId1._offsety= event.y

def popId():
	global disp_pp
	global popId1
	_offsetx=0
	_offsety = 0
	popId1 = Toplevel(windows,bg="#FFFDD0",highlightbackground="red",highlightthickness=3)
	popId1.overrideredirect(True)
	popId1.title("ID")
	popId1.geometry("450x400+800+150")
	popId1.resizable(width=False,height=False)

	label = Label(popId1,text="Control Unit",height=2,font=("times new roman",15,"bold"),bg="red",fg="white")
	label.pack(fill=X,pady=10)

	# display for counting total votes ------------------------------------------ 
	global disp
	disp = Label(popId1,text=votes,justify=CENTER,font=("dungeon",15),bd=2,bg="#98817B",fg="black")
	disp.place(x=150,y=80,width=180,height=60)
	disp.bind("<Enter>",on_enter_disp)
	disp.bind("<Leave>",on_leave_disp)

	# backword navigation button ------------------------------------------------
	global disp3 
	disp3 = Button(popId1,activebackground="cyan",relief="raised",state="disabled",text="Back",font=("times new roman",15,"bold"),fg="orange",bg="blue",command=back1)
	disp3.place(x=90,y=150,width=60,height=60)
	disp3.bind("<Enter>",on_enter_bk1)
	disp3.bind("<Leave>",on_leave_bk1)

	# On off button of evm ------------------------------------------------------
	disp_pp = Label(popId1,text="Off",font=("times new roman",12,"bold"),bd=2,fg="white",bg="red")
	disp_pp.place(x=220,y=160,width=50,height=30)
	lambda task=0: pause_play(task)
   
	# lock unlock button of evm -----------------------------------------------------
	global disp4
	global lock
	global unlock
	lock = PhotoImage(file = "img\\lock.png")
	unlock = PhotoImage(file = "img\\unlock.png")
	disp4 = Button(popId1,image=lock)
	disp4.place(x=370,y=25,width=22,height=22)
	disp4.photo=lock
	disp4.bind("<Button-1>",on_click_lock)
	disp4.bind("<Enter>",on_enter_lock)
	disp4.bind("<Leave>",on_leave_lock)
	
	# reset button -------------------------------------------------------------
	global disp_reset
	disp_reset = Button(popId1,activebackground="cyan",state="disabled",text="Reset",font=("times new roman",15,"bold"),fg="orange",bg="white",command=reset)
	disp_reset.place(x=330,y=150,width=60,height=60)
	disp_reset.bind("<Enter>",on_enter_reset)
	disp_reset.bind("<Leave>",on_leave_reset)

	# result button -----------------------------------------------------------
	global disp2
	disp2 = Button(popId1,activebackground="cyan",state="disabled",text="Result",font=("times new roman",12,"bold"),fg="white",bg="green",command=result)
	disp2.place(x=210,y=220,width=60,height=40)
	disp2.bind("<Enter>",on_enter_result)
	disp2.bind("<Leave>",on_leave_result)

	label = Label(popId1,text="Enter ID",font=("times new roman",12,"bold"),bg="#FFFDD0",fg="blue")
	label.place(x=90,y=300)
	global id_entry
	id_entry = Entry(popId1,textvariable=ele_id,font=("times new roman",12,"bold"),bg="lightgray",fg="brown",justify=CENTER)
	id_entry.place(x=90,y=320)
	id_entry.focus()
	global verify_btn
	verify_btn = Button(popId1,text="Verify",font=("times new roman",10,"bold"),bg="darkblue",fg="white",command=verify )
	verify_btn.place(x=270,y=320)
	verify_btn.bind("<Enter>",on_enter_verifyBtn)
	verify_btn.bind("<Leave>",on_leave_verifyBtn)
	popId1.mainloop()

def on_enter_verifyBtn(e):
		verify_btn['bg']="blue"
		verify_btn['fg']="black"
def on_leave_verifyBtn(e):
		verify_btn['bg']="darkblue"
		verify_btn['fg']="white"
	
def verify():
		if len(voterId_list) != 0:
			for vid in range(0,len(voterId_list)):
				if ele_id.get() == voterId_list[vid]:
					disp_pp['text']="On"
					disp_pp['bg']="#7CFC00"
					disp1_['text']="On"
					disp1_['bg']="#7CFC00"
					btn_enable()
					break 
			if ele_id.get() not in voterId_list:
				   messagebox.showerror("Error","*Id is already used or not found!")
	
		else:
			messagebox.showerror("Error","No more id available!")

# ================initilizing the buttons=======================
def btn_enable():
			n = len(list_name)
			for i in range(1,n+1):
				
				if i == 1:
					btn1.config(state='normal')
				elif i == 2:
					btn2.config(state='normal')
				elif i==3:
					btn3.config(state='normal')
				elif i==4:
					btn4.config(state='normal')
				elif i==5:
					btn5.config(state='normal')
				elif i==6:
					btn6.config(state='normal')
				elif i==7:
					btn7.config(state='normal')
				elif i==8:
					btn8.config(state='normal')
				elif i==9:
					btn9.config(state='normal')
				elif i==10:
					btn10.config(state='normal')
				elif i==11:
					btn11.config(state='normal')
				elif i==12:
					btn12.config(state='normal')
				elif i==13:
					btn13.config(state='normal')
				elif i==14:
					btn14.config(state='normal')
				elif i==15:
					btn15.config(state='normal')
				elif i==16:
					btn16.config(state='normal')
	   
def vote_view():
	global view
	view = Toplevel(windows,bg="purple",highlightbackground="red",highlightthickness=3)
	view.geometry("360x200+530+250")
	view.resizable(width=False,height=False)
	view.overrideredirect(True)
	global label_view
	i = len(votes_count)
	n = votes_count[i-1]
	label_view = Label(view,text="Successfully voted to "+ list_name[n-1] ,font=("times new roman",12,"bold"),bg="white",fg="blue")
	label_view.pack(pady=20)
	label_view1 = Label(view,image=pic[n-1],bg="white",width=80,height=80)
	label_view1.pack()
	disp_pp['text']="Off"
	disp_pp['bg']="red"
	disp1_['text']="Off"
	disp1_['bg']="red"
	lambda task=1: pause_play(task)
	global counter_lbl
	counter_lbl = Label(view,text="",font=("Helvetica",12,"bold"),fg="black",bg="purple")
	counter_lbl.pack(pady=2)
	clock_counter()
	view.after(10000,pause_play,0)
	view.mainloop()
	
# ======*****defining vote buttons*********=========

def vote_btn1():
	global votes
	votes = votes + 1
	disp['text']=votes
	votes_count.append(1)
	if len(voterId_list) != 0:
		for i in range(0, len(voterId_list)):
			if ele_id.get() == voterId_list[i]:
				voterId_list.remove(ele_id.get())
				ele_id.set("")
				break
		# indc.place(x=240,y=pos[0]+2)
		indc.place(x=240,y=pos[0]+2)
		vote_view()  
	 
def vote_btn2():
	global votes
	votes = votes + 1
	disp['text']=votes
	votes_count.append(2)
	if len(voterId_list) != 0:
		for i in range(0, len(voterId_list)):
			if ele_id.get() == voterId_list[i]:
				voterId_list.remove(ele_id.get())
				ele_id.set("")
				break
		indc.place(x=240,y=pos[1]+2)
		vote_view()

def vote_btn3():
	global votes
	votes = votes + 1
	disp['text']=votes
	votes_count.append(3)
	if len(voterId_list) != 0:
		for i in range(0, len(voterId_list)):
			if ele_id.get() == voterId_list[i]:
				voterId_list.remove(ele_id.get())
				ele_id.set("")
				break
		indc.place(x=240,y=pos[2]+2)
		vote_view()

def vote_btn4():
	global votes
	votes = votes + 1
	disp['text']=votes
	votes_count.append(4)
	if len(voterId_list) != 0:
		for i in range(0, len(voterId_list)):
			if ele_id.get() == voterId_list[i]:
				voterId_list.remove(ele_id.get())
				ele_id.set("")
				break
		indc.place(x=240,y=pos[3]+2)
		vote_view()

def vote_btn5():
	global votes
	votes = votes + 1
	disp['text']=votes
	votes_count.append(5)
	if len(voterId_list) != 0:
		for i in range(0, len(voterId_list)):
			if ele_id.get() == voterId_list[i]:
				voterId_list.remove(ele_id.get())
				ele_id.set("")
				break
		indc.place(x=240,y=pos[4]+2)
		vote_view()

def vote_btn6():
	global votes
	votes = votes + 1
	disp['text']=votes
	votes_count.append(6)
	if len(voterId_list) != 0:
		for i in range(0, len(voterId_list)):
			if ele_id.get() == voterId_list[i]:
				voterId_list.remove(ele_id.get())
				ele_id.set("")
				break
		indc.place(x=240,y=pos[5]+2)
		vote_view()

def vote_btn7():
	global votes
	votes = votes + 1
	disp['text']=votes
	votes_count.append(7)
	if len(voterId_list) != 0:
		for i in range(0, len(voterId_list)):
			if ele_id.get() == voterId_list[i]:
				voterId_list.remove(ele_id.get())
				ele_id.set("")
				break
		indc.place(x=240,y=pos[6]+2)
		vote_view()
 
def vote_btn8():
	global votes
	votes = votes + 1
	disp['text']=votes
	votes_count.append(8)
	if len(voterId_list) != 0:
		for i in range(0, len(voterId_list)):
			if ele_id.get() == voterId_list[i]:
				voterId_list.remove(ele_id.get())
				ele_id.set("")
				break
		indc.place(x=240,y=pos[7]+2)
		vote_view()
 
def vote_btn9():
	global votes
	votes = votes + 1
	disp['text']=votes
	votes_count.append(9)
	if len(voterId_list) != 0:
		for i in range(0, len(voterId_list)):
			if ele_id.get() == voterId_list[i]:
				voterId_list.remove(ele_id.get())
				ele_id.set("")
				break
		indc.place(x=240,y=pos[8]+2)
		vote_view()

def vote_btn10():
	global votes
	votes = votes + 1
	disp['text']=votes
	votes_count.append(10)
	if len(voterId_list) != 0:
		for i in range(0, len(voterId_list)):
			if ele_id.get() == voterId_list[i]:
				voterId_list.remove(ele_id.get())
				ele_id.set("")
				break
		indc.place(x=240,y=pos[9]+2)
		vote_view()
  
def vote_btn11():
	global votes
	votes = votes + 1
	disp['text']=votes
	votes_count.append(11)
	if len(voterId_list) != 0:
		for i in range(0, len(voterId_list)):
			if ele_id.get() == voterId_list[i]:
				voterId_list.remove(ele_id.get())
				ele_id.set("")
				break
		indc.place(x=240,y=pos[10]+2)
		vote_view()
 
def vote_btn12():
	global votes
	votes = votes + 1
	disp['text']=votes
	votes_count.append(12)
	if len(voterId_list) != 0:
		for i in range(0, len(voterId_list)):
			if ele_id.get() == voterId_list[i]:
				voterId_list.remove(ele_id.get())
				ele_id.set("")
				break
		indc.place(x=240,y=pos[11]+2)
		vote_view()
 
def vote_btn13():
	global votes
	votes = votes + 1
	disp['text']=votes
	votes_count.append(13)
	if len(voterId_list) != 0:
		for i in range(0, len(voterId_list)):
			if ele_id.get() == voterId_list[i]:
				voterId_list.remove(ele_id.get())
				ele_id.set("")
				break
		indc.place(x=240,y=pos[12]+2)
		vote_view()
 
def vote_btn14():
	global votes
	votes = votes + 1
	disp['text']=votes
	votes_count.append(14)
	if len(voterId_list) != 0:
		for i in range(0, len(voterId_list)):
			if ele_id.get() == voterId_list[i]:
				voterId_list.remove(ele_id.get())
				ele_id.set("")
				break
		indc.place(x=240,y=pos[13]+2)
		vote_view()
 
def vote_btn15():
	global votes
	votes = votes + 1
	disp['text']=votes
	votes_count.append(15)
	if len(voterId_list) != 0:
		for i in range(0, len(voterId_list)):
			if ele_id.get() == voterId_list[i]:
				voterId_list.remove(ele_id.get())
				ele_id.set("")
				break
		indc.place(x=240,y=pos[14]+2)
		vote_view()
 
def vote_btn16():
	global votes
	votes = votes + 1
	disp['text']=votes
	votes_count.append(16)
	if len(voterId_list) != 0:
		for i in range(0, len(voterId_list)):
			if ele_id.get() == voterId_list[i]:
				voterId_list.remove(ele_id.get())
				ele_id.set("")
				break
		indc.place(x=240,y=pos[15]+2)
		vote_view()

# configure the counter display -----------------------------------------
def on_enter_disp(e):
	disp.config(font=("dungeon",20,"bold"),width=100,height=50)
	disp['bg']="#C5C6D0"
def on_leave_disp(e):
	disp.config(font=("dungeon",15,"bold"),width=80,height=30)
	disp['bg']="#98817B"

# on off button --------------------------------------------------------
def pause_play(task):
		global second
		second = 10
		if task==0:
			indc.place_forget()
			view.destroy()
			disp_pp['text']="Off"
			disp_pp['bg']="red"
			disp1_['text']="Off"
			disp1_['bg']="red"
			lambda task=1: pause_play(task)
			btn1.config(state="disabled")
			btn2.config(state="disabled")
			btn3.config(state="disabled")
			btn4.config(state="disabled")
			btn5.config(state="disabled")
			btn6.config(state="disabled")
			btn7.config(state="disabled")
			btn8.config(state="disabled")
			btn9.config(state="disabled")
			btn10.config(state="disabled")
			btn11.config(state="disabled")
			btn12.config(state="disabled")
			btn13.config(state="disabled")
			btn14.config(state="disabled")
			btn15.config(state="disabled")
			btn16.config(state="disabled")
			if len(voterId_list) != 0:
					id_entry.focus()

		elif len(voterId_list) == 0:
			messagebox.showinfo("ID","Voting are already done, No more id are available!")
			pause_play(0)             
		else:
			disp_pp['text']="On"
			disp_pp['bg']="#7CFC00"
			disp1_['text']="On"
			disp1_['bg']="#7CFC00"
			lambda task=0: pause_play(task)
			btn_enable()

# back navigation button ---------------------------------------------------------- 
def back1():
	clear_windows()
	next1()
def on_enter_bk1(e):
	disp3['bg']="lightgray"
	disp3['fg']="black"
		
def on_leave_bk1(e):
	disp3['bg']="blue"
	disp3['fg']="white"

def exit_passw():
	passw.destroy()
				  
def unlock_pass():
	global passw
	passw = Toplevel(windows,bg="cyan",highlightbackground="purple",highlightthickness=2)
	passw.geometry("300x100+700+50")
	passw.resizable(width=False,height=False)
	passw.overrideredirect(True)
	global label_passw
	global passw_entry
	label_passw = Label(passw,text="Password" ,font=("times new roman",12,"bold"),bg="white",fg="red")
	label_passw.pack(pady=2,fill=X)
	passw_entry = Entry(passw,show="*",textvariable=unlock_passw,font=("times new roman",12,"bold"),bg="white",fg="blue",justify=CENTER)
	passw_entry.pack(pady=5)
	passw_entry.focus()
	passw_entry.bind("<Leave>",on_leave_passw)
	global btn_passw
	btn_passw = Button(passw,text="Unlock",bg="green",fg="white",command=unlock_verify)
	btn_passw.place(x=100,y=60)
	btn_passw.bind("<Enter>",on_enter_passw)
	btn_passw1 = Button(passw,text="Exit",bg="gray",fg="white",command=exit_passw)
	btn_passw1.place(x=150,y=60)

def on_enter_passw(e):
	global value
	if unlock_passw.get() == p.get():
	   value=1

def on_leave_passw(e):
	global value
	if unlock_passw.get() == p.get():
	   value=1

def on_click_lock(e):
			global value
			disp4.configure(image=lock)
			disp4.photo = lock
			disp2.config(state="disabled")
			disp_reset.config(state="disabled")
			disp3.config(state="disabled")
			popId1.unbind("<Button-1>")
			popId1.unbind("<B1-Motion>")
			unlock_pass()
			
def unlock_verify():
	global value
	if value != 1:
		messagebox.showerror("Error","Invalid password!")
	else:
			exit_passw()
			disp4.configure(image=unlock)
			disp4.photo = unlock
			disp2.config(state="normal")
			disp_reset.config(state="normal")
			disp3.config(state="normal")
			popId1.bind("<Button-1>",clickwin)
			popId1.bind("<B1-Motion>",dragwin)
			value = 0
			unlock_passw.set("")

# reset button ---------------------------------------------------------
def reset():
	global votes 
	votes = 0
	disp['text']="0"
	votes_count.clear()

# configure reset button
def on_enter_reset(e):
		disp_reset.config(font=("times new roman",16,"bold"))
		disp_reset['bg'] = "orange"
		disp_reset['fg'] = "white"

def on_leave_reset(e):
		disp_reset.config(font=("times new roman",15,"bold"))
		disp_reset['fg'] = "orange"
		disp_reset['bg'] = "white"

# result button
def result():
	sign()

# result button configure
def on_enter_result(e):
	disp2.config(font=("times new roman",13,"bold"))
	disp2['bg']="#7CFC00"
	disp2['fg']="#DE5D83"

def on_leave_result(e):
	disp2.config(font=("times new roman",12,"bold"))
	disp2['bg']="green"
	disp2['fg']="white"

# ===========================================================================
# sign in window
# ===========================================================================
def sign():
	clear_windows()
	windows.title("Sign In")
	icon = PhotoImage(file = "img\\evmicon.png")
	windows.iconphoto(False,icon)
	windows.geometry("360x360")
	windows.resizable(width=False,height=False)
	windows.config(bg="#AA55FF")
	 
	# frame ----------------------------------------------------------
	global frame_sign
	frame_sign = Frame(windows,bg="cyan",highlightbackground="red",highlightthickness=3)
	frame_sign.place(x=10,y=30,width=340,height=320)

	# sign label ---------------------------------------------------
	abc1 = Label(frame_sign,text="Sign In",bg="red",borderwidth=2,fg="#ffff00",font=("times new roman",15,"bold"))
	abc1.place(x=0,y=10,width=334)
	
	# username label -----------------------------------------------
	abc2 = Label(frame_sign,text="Username",borderwidth=2,bg="lightgray",fg="brown",font=("times new roman",12,"bold"))
	abc2.place(x=50,y=70,width=120)
	
	# username entry -----------------------------------------------
	abc2_entry= Entry(frame_sign,bg="white",textvariable=u1,fg="brown",font=("times new roman",12))
	abc2_entry.place(x=180,y=70,width=120,height=25)
	abc2_entry.focus()

	# password label -----------------------------------------------
	abc3 = Label(frame_sign,text="Password",borderwidth=2,bg="lightgray",fg="brown",font=("times new roman",12,"bold"))
	abc3.place(x=50,y=100,width=120)

	# password entry -----------------------------------------------
	global abc3_entry
	abc3_entry= Entry(frame_sign,bg="white",textvariable=p1,fg="brown",font=("times new roman",12),show="*")
	abc3_entry.place(x=180,y=100,width=120,height=25)
	
	# show password checkbutton from evmsetting1
	global show_password
	show_password = Checkbutton(frame_sign,text="Show Password",variable=show_pass1,bg="cyan",activebackground="cyan",onvalue=1,offvalue=0)
	show_password.place(x=180,y=140)
	show_password.bind("<Button-1>",on_enter_showPassword1)
	
	# sign in button label-----------------------------------------------
	global abc4
	abc4 = Button(frame_sign,activebackground="cyan",text="Sign In",borderwidth=2,bg="#55007F",fg="white",font=("times new roman",10,"bold"),command=sign_in)
	abc4.place(x=140,y=220,width=60)
	abc4.bind("<Return>",click_sign)
	abc4.bind("<Enter>",on_enter_sign)
	abc4.bind("<Leave>",on_leave_sign)

# sign in button
def on_enter_showPassword1(e):
	if show_pass1.get()==0:
		abc3_entry.config(show='')
	else:
		abc3_entry.config(show='*')

def sign_in():
	if u1.get()=="" or p1.get()=="":
		messagebox.showerror("Error","All fields are required!")
	elif u.get() == u1.get() and p.get()==p1.get():
		frame_button.destroy()
		result_window()
		b = 1
		high = 10
		for ele in list_name:
			if b==1:
				disp_count = Label(myframe1,text=str(b)+".",fg="black",bg="white",font=("times new roman",12,"bold"))
				disp_count.place(x=40,y=high)
				display_result_name = Entry(myframe1,cursor="arrow",state="normal",font=("times new roman",10,"bold"),bd=0,justify=CENTER)
				display_result_name.place(x=70,y=high,height=30,width=150)
				display_result_name.insert(END,ele)
				display1_result = Label(myframe1,image=pic[b-1],bg="#AAFFFF")
				display1_result.photo = pic[b-1]
				display1_result.place(x=240,y=high,width=35,height=30)  
				display_result_name.config(state="disabled")
				result_count = Label(myframe1,text=str(votes_count.count(b)),justify=CENTER,font=("goudy old style",15,"bold"),bg="lightgray",fg="blue")
				result_count.place(x=310,y=high,width=60,height=30)
				b += 1
			elif b ==2:
				high = b*30
				disp_count = Label(myframe1,text=str(b)+".",fg="black",bg="white",font=("times new roman",12,"bold"))
				disp_count.place(x=40,y=high)
				display_result_name = Entry(myframe1,cursor="arrow",state="normal",font=("times new roman",10,"bold"),bd=0,justify=CENTER)
				display_result_name.place(x=70,y=high,height=30,width=150)
				display_result_name.insert(END,ele)
				display1_result = Label(myframe1,image=pic[b-1],bg="#AAFFFF")
				display1_result.photo = pic[b-1]
				display1_result.place(x=240,y=high,width=35,height=30)  
				display_result_name.config(state="disabled")
				result_count = Label(myframe1,text=str(votes_count.count(b)),justify=CENTER,font=("goudy old style",15,"bold"),bg="lightgray",fg="blue")
				result_count.place(x=310,y=high,width=60,height=30)
				b += 1
				
				high += 50
			else:
				
				disp_count = Label(myframe1,text=str(b)+".",fg="black",bg="white",font=("times new roman",12,"bold"))
				disp_count.place(x=40,y=high)
				display_result_name = Entry(myframe1,cursor="arrow",state="normal",font=("times new roman",10,"bold"),bd=0,justify=CENTER)
				display_result_name.place(x=70,y=high,height=30,width=150)
				display_result_name.insert(END,ele)
				display1_result = Label(myframe1,image=pic[b-1],bg="#AAFFFF")
				display1_result.photo = pic[b-1]
				display1_result.place(x=240,y=high,width=35,height=30)  
				display_result_name.config(state="disabled")
				result_count = Label(myframe1,text=str(votes_count.count(b)),justify=CENTER,font=("goudy old style",15,"bold"),bg="lightgray",fg="blue")
				result_count.place(x=310,y=high,width=60,height=30)
				high += 50
				b += 1
					  
	else:
		messagebox.showerror("Error","Invalid Username or Password!")

# sign in button configure
def click_sign(e):
	sign_in()

def on_enter_sign(e):
	abc4.config(font=("times new roman",12,"bold"))
	abc4['bg']="red"
	abc4['fg']="black"
def on_leave_sign(e):
	abc4.config(font=("times new roman", 10, "bold"))
	abc4['bg'] = "#55007F"
	abc4['fg'] = "white"

# ================================================================================
# result window 
# ================================================================================
def result_window():
	windows.title("Result")
	icon = PhotoImage(file = "img\\evmicon.png")
	windows.iconphoto(False,icon)
	windows.geometry("420x700")
	windows.resizable(width=False,height=False)
	windows.config(bg="#AA55FF")

	# frame---------------------------------------------------------------------
	global frame_result
	frame_result = Frame(windows,bg="white",highlightbackground="blue",highlightthickness=3)
	frame_result.place(x=10,y=20,width=400,height=90)
	# result label --------------------------------------------------------------
	abb = Label(frame_result,text="Result",bg="orange",borderwidth=2,fg="#ffff00",font=("times new roman",15,"bold"))
	abb.place(x=2,y=2,width=340)
	abb1 = Button(frame_result,text="LogOut",bg="orange",borderwidth=0,fg="black",font=("times new roman",10,"bold"),command=logout)
	abb1.place(x=342,y=2,width=48,height=29)

	lst_result = Label(frame_result,text="        No.              Name                   Symbol         Votes",fg="black",bg="white",font=("times new roman",12,'bold'))
	lst_result.place(x=2,y=32)
	
	global frame_result1
	frame_result1 = Frame(windows,bg="white",highlightbackground="blue",highlightthickness=3)
	frame_result1.place(x=10,y=80,width=400,height=610)
	wrapper2 = LabelFrame(frame_result1)
	
	global mycanvas1
	mycanvas1 = Canvas(wrapper2)
	mycanvas1.pack(side=LEFT,fill="both",expand="yes")
	yscrollbar = ttk.Scrollbar(wrapper2,orient="vertical",command=mycanvas1.yview)
	yscrollbar.pack(side=RIGHT,fill='both')
	mycanvas1.configure(yscrollcommand=yscrollbar.set)
	mycanvas1.bind('<Configure>',lambda e: mycanvas1.configure(scrollregion=mycanvas1.bbox('all')))
	global myframe1
	myframe1 = Frame(mycanvas1,bg="white",width=380,height=840)
	mycanvas1.create_window((0,0),window=myframe1,anchor="nw")
	wrapper2.pack(fill="both",expand="yes")

def logout():
	clear_windows()
	name.set("")
	unlock_passw.set("")
	u1.set("")
	p1.set("")
	ele_id.set("")
	global a 
	global c
	global votes
	a = 0 
	c = 0
	votes = 0
	# clear_
	list_name.clear()
	frame_input.destroy()
	frame_input2.destroy()
	frame_input3.destroy()
	mycanvas.destroy()
	frame_button.destroy()
	# clear1
	voterId.set("")
	voterId_list.clear()
	frame_input.destroy()
	frame_input2.destroy()
	frame_input3.destroy()
	mycanvas.destroy()
	frame_button.destroy()

	votes_count.clear()
	evm_setting1() 
	u.set("") 
	p.set("")
	cp.set("") 
	  
# *******************************************************************************
# ===============================================================================
# ======================>>>>>>>>PROGRAM START HERE<<<<<<<<<======================
# ===============================================================================
# *******************************************************************************
windows = Tk()
votes = 0
a = 0
c=0
b=0
second = 10
value = 0

# =================inserting symbols pic================
pos = [30,70,109,149,188,228,267,307,347,386,426,465,505,544,583,623]
pic  = []
pic1 = PhotoImage(file = "img\\evm1.png")
pic2 = PhotoImage(file = "img\\evm2.png")
pic3 = PhotoImage(file = "img\\evm3.png")
pic4 = PhotoImage(file = "img\\evm4.png")
pic5 = PhotoImage(file = "img\\evm5.png")
pic6 = PhotoImage(file = "img\\evm6.png")
pic7 = PhotoImage(file = "img\\evm7.png")
pic8 = PhotoImage(file = "img\\evm8.png")
pic9 = PhotoImage(file = "img\\evm9.png")
pic10 = PhotoImage(file = "img\\evm10.png")
pic11 = PhotoImage(file = "img\\evm11.png")
pic12 = PhotoImage(file = "img\\evm12.png")
pic13 = PhotoImage(file = "img\\evm13.png")
pic14 = PhotoImage(file = "img\\evm14.png")
pic15 = PhotoImage(file = "img\\evm15.png")
pic16 = PhotoImage(file = "img\\evm16.png")

pic.append(pic1)
pic.append(pic2)
pic.append(pic3)
pic.append(pic4)
pic.append(pic5)
pic.append(pic6)
pic.append(pic7)
pic.append(pic8)
pic.append(pic9)
pic.append(pic10)
pic.append(pic11)
pic.append(pic12)
pic.append(pic13)
pic.append(pic14)
pic.append(pic15)
pic.append(pic16)

voterId_list = []
list_name = []
votes_count = []

show_pass = IntVar(value=0)
show_pass1 = IntVar(value=0)
voterId = StringVar()
ele_id = StringVar()
unlock_passw=StringVar()
u1 = StringVar()
p1 = StringVar()
u = StringVar()
p = StringVar()
cp = StringVar()
name = StringVar()

evm_setting1()


windows.mainloop()