from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random
from tkinter import messagebox


root=Tk()
root.title("Flash App")
root.geometry("810x550")
load = Image.open("C:/gui/india.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.image = render
img.place(x=2, y=2)
# alabel=Label(root,text="Created by"+ " Yash Mehta 1811024 " +"Nidhi Nair 1811028").grid(row=1,column=1,columnspan=3)


def math_random():
    # generate a random number
    global num_1
    global num_2
    num_1=randint(0,10)
    num_2=randint(0,10)

    global add_image1
    global add_image2
    card1="C:/gui/Flashcards/" + str(num_1) +".png"
    card2="C:/gui/Flashcards/" + str(num_2) +".png"
    add_image1=ImageTk.PhotoImage(Image.open(card1))
    add_image2=ImageTk.PhotoImage(Image.open(card2))
    
    # put flashcard on screen
    add_1.config(image=add_image1)
    add_2.config(image=add_image2)




# create addition answer function
def answer_sub():
    answer=num_1-num_2
    if sub_answer.get()=="":
        messagebox.showerror("Error","Write a value")
    elif int(sub_answer.get())==answer:
        response="Correct! "+str(num_1) +" - "+str(num_2)+" = "+str(answer)
        answer_message.config(text=response)
    else:
        response="Wrong! "+str(num_1) +" - "+str(num_2)+" = "+str(answer) +" Not "+sub_answer.get()
        answer_message.config(text=response)
    
    sub_answer.delete(0,END)
    math_random()






# create addition math flashcard function
def sub():
    hide_all_frames()
    sub_frame.pack(fill="both",expand=1)

    add_label=Label(sub_frame,text="Subtraction Flashcards",font=("Helvetica",18)).pack(pady=15)
    pic_frame=Frame(sub_frame,width=400,height=300)
    pic_frame.pack()

    # generate a random number
    global num_1
    global num_2
    num_1=randint(0,10)
    num_2=randint(0,10)

    # create 3 labels inside our pic frame
    global add_1
    global add_2
    add_1=Label(pic_frame)
    add_2=Label(pic_frame)
    math_sign=Label(pic_frame,text="-",font=("Helvetica",28))
    # grid labels
    add_1.grid(row=0,column=0)
    math_sign.grid(row=0,column=1)
    add_2.grid(row=0,column=2)

    global add_image1
    global add_image2
    card1="C:/gui/Flashcards/" + str(num_1) +".png"
    card2="C:/gui/Flashcards/" + str(num_2) +".png"
    add_image1=ImageTk.PhotoImage(Image.open(card1))
    add_image2=ImageTk.PhotoImage(Image.open(card2))
    
    # put flashcard on screen
    add_1.config(image=add_image1)
    add_2.config(image=add_image2)


    # create answer box and button
    global sub_answer
    sub_answer=Entry(sub_frame,font=("Helvetica",18))
    sub_answer.pack(pady=50)

    sub_answer_button=Button(sub_frame,text="Answer",command=answer_sub)
    sub_answer_button.pack()

    global answer_message
    answer_message =Label(sub_frame,text="",font=("Helvetica",18))
    answer_message.pack(pady=40)




# create addition answer function
def answer_add():
    answer=num_1+num_2
    if add_answer.get()=="":
        messagebox.showerror("Error","Write a value")
    elif int(add_answer.get())==answer:
        response="Correct! "+str(num_1) +" + "+str(num_2)+" = "+str(answer)
        answer_message.config(text=response)
    else:
        response="Wrong! "+str(num_1) +" + "+str(num_2)+" = "+str(answer) +" Not "+add_answer.get()
        answer_message.config(text=response)
    
    add_answer.delete(0,END)
    math_random()





# create addition math flashcard function
def add():
    hide_all_frames()
    add_frame.pack(fill="both",expand=1)

    add_label=Label(add_frame,text="Addition Flashcards",font=("Helvetica",18)).pack(pady=15)
    pic_frame=Frame(add_frame,width=400,height=300)
    pic_frame.pack()

    # generate a random number
    global num_1
    global num_2
    num_1=randint(0,10)
    num_2=randint(0,10)

    # create 3 labels inside our pic frame
    global add_1
    global add_2
    add_1=Label(pic_frame)
    add_2=Label(pic_frame)
    math_sign=Label(pic_frame,text="+",font=("Helvetica",28))
    # grid labels
    add_1.grid(row=0,column=0)
    math_sign.grid(row=0,column=1)
    add_2.grid(row=0,column=2)

    global add_image1
    global add_image2
    card1="C:/gui/Flashcards/" + str(num_1) +".png"
    card2="C:/gui/Flashcards/" + str(num_2) +".png"
    add_image1=ImageTk.PhotoImage(Image.open(card1))
    add_image2=ImageTk.PhotoImage(Image.open(card2))
    
    # put flashcard on screen
    add_1.config(image=add_image1)
    add_2.config(image=add_image2)


    # create answer box and button
    global add_answer
    add_answer=Entry(add_frame,font=("Helvetica",18))
    add_answer.pack(pady=50)

    add_answer_button=Button(add_frame,text="Answer",command=answer_add)
    add_answer_button.pack()

    global answer_message
    answer_message =Label(add_frame,text="",font=("Helvetica",18))
    answer_message.pack(pady=40)





# create randomizing state function 
def random_state():
    # create a list of our state names
    global our_states
    our_states=['andhrapradesh','arunachalpradesh','assam','bihar',
                'chattisgarh','goa','gujarat','haryana',
                'himachalpradesh','jharkhand','karnataka','kerala',
                'madhyapradesh','maharashtra','manipur','meghalaya',
                'mizoram','nagaland','odisha','punjab',
                'rajasthan','sikkim','tamilnadu','telangana',
                'tripura','uttarakhand','uttarpradesh','westbengal']

    # generate random number
    global rando
    rando=randint(0,len(our_states)-1)
    state1="C:/gui/states/" + our_states[rando] +".png"

    # create state images
    global state_img
    state_img=ImageTk.PhotoImage(Image.open(state1))
    show_state.config(image=state_img,bg="white")





# create state capital answers
def state_capital_answer():
    if capital_radio.get() == our_state_capitals[answer]:
        response = "Correct! "+our_state_capitals[answer].title()+" is the capital of "+answer.title()
    else:
        response="Incorrect! "+our_state_capitals[answer].title()+" is the capital of "+answer.title()

    answer_label_capitals.config(text=response)




# create answer function
def state_answer():
    answer=answer_input.get()
    answer=answer.replace("","")

    # determine if our answer is right or wrong
    if answer.lower()=="":
        messagebox.showerror("Error","Atleast give a miss!!")
    elif answer.lower()==our_states[rando]:
        response="correct " +our_states[rando].title()
        answer_label.config(text=response)
    else:
        response="Incorrect! "+our_states[rando].title()
        answer_label.config(text=response)    


    # answer_label.config(text=response)

    # clear the entry box
    answer_input.delete(0,END)


    random_state()







# create state flashcard function
def states():
    # hide previous frames
    hide_all_frames()
    state_frame.pack(fill="both",expand=1)

    global  show_state
    show_state=Label(state_frame)
    show_state.pack(pady=15)
    random_state()

    # create answer input box
    global answer_input
    answer_input=Entry(state_frame,font=("Helvetica",18),bd=2)
    answer_input.pack(pady=15)

    # create button to randomize images
    rando_btn=Button(state_frame,text="Next State",command=states)
    rando_btn.pack(pady=10)

    # create a button to ans the q 
    answer_button=Button(state_frame,text="Answer",command=state_answer)
    answer_button.pack(pady=5)

    # create a label to tell us if we got the right answer or not
    global answer_label
    answer_label=Label(state_frame,text="",font=("Helvetica",18),bg="white")
    answer_label.pack(pady=15)





# create state capital flashcard function
def state_capitals():
    hide_all_frames()
    state_capital_frame.pack(fill="both",expand=1)
    # my_label=Label(state_capital_frame,text="Capitals").pack()
    
    global  show_state
    show_state=Label(state_capital_frame)
    show_state.pack(pady=15)

    global our_states
    our_states=['andhrapradesh','arunachalpradesh','assam','bihar',
                'chattisgarh','goa','gujarat','haryana',
                'himachalpradesh','jharkhand','karnataka','kerala',
                'madhyapradesh','maharashtra','manipur','meghalaya',
                'mizoram','nagaland','odisha','punjab',
                'rajasthan','sikkim','tamilnadu','telangana',
                'tripura','uttarakhand','uttarpradesh','westbengal']

    global our_state_capitals
    our_state_capitals={
        'andhrapradesh':"hyderabad",
        'arunachalpradesh':"itanagar",
        'assam':"dispur",
        'bihar':"patna",
        'chattisgarh':"raipur",
        'goa':"panaji",
        'gujarat':"gandhinagar",
        'haryana':"chandigarh",
        'himachalpradesh':"shimla",
        'jharkhand':"ranchi",
        'karnataka':"bangalore",
        'kerala':"trivandrum",
        'madhyapradesh':"bhopal",
        'maharashtra':"mumbai",
        'manipur':"imphal",
        'meghalaya':"shillong",
        'mizoram':"aizawl",
        'nagaland':"kohima",
        'odisha':"bhubaneshwar",
        'punjab':"chandigarh",
        'rajasthan':"jaipur",
        'sikkim':"gangtok",
        'tamilnadu':"chennai",
        'telangana':"hyderabad",
        'tripura':"agartala",
        'uttarakhand':"dehradun",
        'uttarpradesh':"lucknow",
        'westbengal':"kolkata"
    }

    # create empty answer list and counter
    answer_list=[]
    count = 1
    global answer
    # generate 3 random capitals
    while count <4:
        rando=randint(0,len(our_states)-1)
        # if first selection,make it our answer
        if count==1:
            answer=our_states[rando]
            global state_img
            state="C:/gui/states/"+our_states[rando]+".png"
            state_img=ImageTk.PhotoImage(Image.open(state))
            show_state.config(image=state_img)

        # add our first selection to a new list
        answer_list.append(our_states[rando])

        # remove from old list
        our_states.remove(our_states[rando])

        # shuffle original list
        random.shuffle(our_states)

        count=count+1

    random.shuffle(answer_list)

    global capital_radio
    capital_radio=StringVar()
    capital_radio.set(our_state_capitals[answer_list[0]])

    capital_radio_button1=Radiobutton(state_capital_frame,text=our_state_capitals[answer_list[0]].title(),variable=capital_radio,value=our_state_capitals[answer_list[0]]).pack()
    capital_radio_button2=Radiobutton(state_capital_frame,text=our_state_capitals[answer_list[1]].title(),variable=capital_radio,value=our_state_capitals[answer_list[1]]).pack()
    capital_radio_button3=Radiobutton(state_capital_frame,text=our_state_capitals[answer_list[2]].title(),variable=capital_radio,value=our_state_capitals[answer_list[2]]).pack()

    # add a pass button
    pass_button=Button(state_capital_frame,text="Next",command=state_capitals)
    pass_button.pack(pady=15)

    # create a button to answer
    capital_answer_button=Button(state_capital_frame,text="Answer",command=state_capital_answer)
    capital_answer_button.pack(pady=15)

    # create an answer label
    global answer_label_capitals
    answer_label_capitals=Label(state_capital_frame,text="",font=("Helvetica",12)) 
    answer_label_capitals.pack(pady=15)





# hide all previous frames
def hide_all_frames():
    # loop through and destroy all children in previous frames
    for widget in  state_frame.winfo_children():
        widget.destroy()

    for widget in  state_capital_frame.winfo_children():
        widget.destroy()

    for widget in  add_frame.winfo_children():
        widget.destroy()  

    for widget in  sub_frame.winfo_children():
        widget.destroy()        

    sub_frame.pack_forget()
    add_frame.pack_forget()
    state_frame.pack_forget()
    state_capital_frame.pack_forget()



# create menu
my_menu=Menu(root)
root.config(menu=my_menu)

# geography menu items
states_menu=Menu(my_menu)
my_menu.add_cascade(label="Geography",menu=states_menu)
states_menu.add_command(label="states",command=states)
states_menu.add_command(label="states capitals",command=state_capitals)
states_menu.add_separator()
states_menu.add_command(label="Exit",command=root.quit)

# Math flashcard menu
math_menu=Menu(my_menu)
my_menu.add_cascade(label="Math",menu=math_menu)
math_menu.add_command(label="Addition",command=add)
math_menu.add_command(label="Subtraction",command=sub)
math_menu.add_separator()
math_menu.add_command(label="Exit",command=root.quit)


# create our frames
state_frame=Frame(root,width=500,height=500,bg="white")
state_capital_frame=Frame(root,width=500,height=500)
# addition and subtraction frames
add_frame=Frame(root,width=500,height=500)
sub_frame=Frame(root,width=500,height=500)

root.mainloop()