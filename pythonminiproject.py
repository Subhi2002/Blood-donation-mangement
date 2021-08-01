#from re import L
from tkinter import *
from PIL import ImageTk,Image
import pymysql
import mysql.connector
import speech_recognition as sr
import smtplib
import pyttsx3
from email.message import EmailMessage
from tkinter import messagebox
root=Tk()
gh="hi"
listener = sr.Recognizer()
engine= pyttsx3.init('sapi5')
engine.setProperty("rate",170)
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
emaillist={"subhi":"pssubhiksha@gmail.com","surabhi":"pssubhiksha@gmail.com"} 
# Use female voice
engine.setProperty('voice', voice_id)

mypass="subhi@sql2002"
mydb =mysql.connector.connect(host='localhost',user='root',password=mypass,database="pythonmp")


root.title("blood donation")

#root.minsize(width=1000,height=800)
mycanvas = Canvas(root,width=1000,height=800)
bgn = Image.open("bg1.jpeg")
newbgn=ImageTk.PhotoImage(bgn)

mycanvas.create_image(0,0,image=newbgn,anchor="nw")
mycanvas.pack()

"""def resize(e):
       global resized_bg,newbg
       global  bg1 
       bg1 = Image.open("bg1.jpeg")
       resized_bg = bg1.resize((e.width,e.height),Image.ANTIALIAS)
       newbg=ImageTk.PhotoImage(resized_bg)
       mycanvas.create_image(0,0,image=newbg,anchor="nw")
       mycanvas.pack()

root.bind('<Configure>',resize)
headingFrame1 = Frame(root,bg="white",bd=4)
headingFrame1.place(relx=0.15,rely=0.05,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome!!", bg='#eb2828', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
#mycanvas.create_text(200,150,text="WELCOME!!",font=("Helvetica",30),fill="white",bg="#eb2828")"""

v=Label(root,text="WELCOME!!",fg="white",bg="#eb2828",padx=120,pady=30,font=("Helvetica",20))
button23_window=mycanvas.create_window(300,100,window=v)


def open():
    
    donate_window = Toplevel()
    donate_window.title("DONORS")
    donate_window.minsize(width=700,height=800)
    donate_window['bg']="#77D2EE"

    
    a= Label(donate_window,text="Donate and save lives!!!",font=("Helvetica",30),bg="#77D2EE")
    a.grid(row=0,column =0,columnspan=2,padx=120)
   
    mypass="subhi@sql2002"
    mydb =mysql.connector.connect(host='localhost',user='root',password=mypass,database="bloodmanagement")
    mycursor = mydb.cursor()

    def clearfields():
        namebox.delete(0,END)
        mobbox.delete(0,END)
        emailbox.delete(0,END)
        bldbox.delete(0,END)
        placebox.delete(0,END)
    def submiti():
        sqlcommand = "INSERT INTO donors (name,mobilenumber,emailid,place,bloodgroup) VALUES (%s,%s,%s,%s,%s)"
        values =(namebox.get(),mobbox.get(),emailbox.get(),placebox.get(),bldbox.get())
        mycursor.execute(sqlcommand,values)
        mydb.commit()
        clearfields()
    name=Label(donate_window,text="Enter name",font=("Helvetica",20),bg="#77D2EE")
    name.grid(row=1,column=0,sticky=W,padx=20,pady=15,)
    mob=Label(donate_window,text="Enter mobile number",font=("Helvetica",20),bg="#77D2EE")
    mob.grid(row=2,column=0,sticky=W,padx=20,pady=15)
    email =Label(donate_window,text="Enter emailid",font=("Helvetica",20),bg="#77D2EE")
    email.grid(row=3,column=0,sticky=W,padx=20,pady=15)
    bld=Label(donate_window,text="Enter blood group",font=("Helvetica",20),bg="#77D2EE")
    bld.grid(row=4,column=0,sticky=W,padx=20,pady=15)
    place=Label(donate_window,text="Enter your place",font=("Helvetica",20),bg="#77D2EE")
    place.grid(row=5,column=0,sticky=W,padx=20,pady=15)

    namebox = Entry(donate_window,width=25,font=("Helvetica",15))
    namebox.grid(row=1,column=1)
    mobbox = Entry(donate_window,width=25,font=("Helvetica",15))
    mobbox.grid(row=2,column=1)
    emailbox = Entry(donate_window,width=25,font=("Helvetica",15))
    emailbox.grid(row=3,column=1)
    bldbox = Entry(donate_window,width=25,font=("Helvetica",15))
    bldbox.grid(row=4,column=1)
    placebox = Entry(donate_window,width=25,font=("Helvetica",15))
    placebox.grid(row=5,column=1)

    a=Label(donate_window,text=" ",bg="#77D2EE").grid(row=6,column=0)
    submit =Button(donate_window,text="SUBMIT",font=("Helvetica",15),relief="raised",bg="white",command=submiti,width=12)
    submit.grid(row=7,column=0)
    z = Button(donate_window,text="CLEAR",font=("Helvetica",15),relief="raised",bg="white",command=clearfields,width=12)
    z.grid(row=7,column=1)

    mycursor.execute("SELECT * FROM donors")
    x = mycursor.fetchall()
    for i in x:
        print(i)
        emaillist[i[0]]=i[2]

def opennew():
    needers_window= Toplevel()
    needers_window.title("NEEDERS")
    needers_window.minsize(width=700,height=800)
    needers_window['bg']="#77D2EE"

    a= Label(needers_window,text="Stay Calm!!",font=("Helvetica",30),bg="#77D2EE")
    a.grid(row=0,column =0,columnspan=2,padx=120)
   
    mypass="subhi@sql2002"
    mydb =mysql.connector.connect(host='localhost',user='root',password=mypass,database="bloodmanagement")
    mycursor = mydb.cursor()

    def clearfields():
        namebox.delete(0,END)
        mobbox.delete(0,END)
        emailbox.delete(0,END)
        bldbox.delete(0,END)
        placebox.delete(0,END)

    def displaying():
      
        mycursor.execute("SELECT * FROM donors")
        x = mycursor.fetchall()
        gh=bldbox.get()
        print(gh)
        

        for index,i in enumerate(x):

            if gh==i[4]:
                    
                index=index+11
                xlabel=Label(needers_window,text=i[0],font=("Helvetica",13),bg="#77D2EE")
                xlabel.grid(row=index,column=0)
                xlabel=Label(needers_window,text=i[4],font=("Helvetica",13),bg="#77D2EE")
                xlabel.grid(row=index,column=1)
                xlabel=Label(needers_window,text=i[3],font=("Helvetica",13),bg="#77D2EE")
                xlabel.grid(row=index,column=2)
                
            else:
                continue
                    

            

    
    def submiti():
        sqlcommand = "INSERT INTO needers (name,mobilenumber,emailid,place,bloodgroup) VALUES (%s,%s,%s,%s,%s)"
        values =(namebox.get(),mobbox.get(),emailbox.get(),placebox.get(),bldbox.get())
        mycursor.execute(sqlcommand,values)
        mydb.commit()
        gty=Label(needers_window,text=" ",bg="#77D2EE").grid(row=9,column=0)
        namelabel=Label(needers_window,text="NAME",font=("Helvetica",15),bg="#77D2EE")
        namelabel.grid(row=10,column=0)
        bloodlabel=Label(needers_window,text="BLD GRP",font=("Helvetica",15),bg="#77D2EE")
        bloodlabel.grid(row=10,column=1)
        placelabel=Label(needers_window,text="PLACE",font=("Helvetica",15),bg="#77D2EE")
        placelabel.grid(row=10,column=2)
        displaying()
        clearfields()


    def emailing():
        print(emaillist)
        listener = sr.Recognizer()
        engine= pyttsx3.init('sapi5')
        engine.setProperty("rate",170)
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        # Use female voice
        engine.setProperty('voice', voice_id)
        
        def get_info():
            try:
                with sr.Microphone() as source:
                    print("listening...")
                    voice =listener.listen(source)
                    info = listener.recognize_google(voice)
                    print(info)
                    return info
            except:
                    print("not responding")   

        def talk(text) :
            engine.say(text)
            engine.runAndWait()            

        def send_email(receiver,subject):  
                server =smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login('pssubhiksha@gmail.com','rrwptimsrxqqwuny')
                email = EmailMessage()
                email['From'] ="pssubhiksha@gmail.com"
                email['To'] = receiver
                email['Subject']=subject
                message="it is urgent and the patient needs your blood...kindly help !!!"
                email.set_content(message)
                server.send_message(email)
                print('sent')   

        def getemailinfo():
            talk("to whom do you want to send email")
            name = get_info()
            if name in emaillist:
                receiver = emaillist[name]
            else:
                talk("email id not recognised")   
                return; 
            print(receiver)
            talk("what is the subject of the mail")
            subject = get_info()
            send_email(receiver,subject)
            talk("your email is sent succesfully")
            
            
        getemailinfo()    

    
    
    name=Label(needers_window,text="Enter name",font=("Helvetica",20),bg="#77D2EE")
    name.grid(row=1,column=0,sticky=W,padx=20,pady=15,)
    mob=Label(needers_window,text="Enter mobile number",font=("Helvetica",20),bg="#77D2EE")
    mob.grid(row=2,column=0,sticky=W,padx=20,pady=15)
    email =Label(needers_window,text="Enter emailid",font=("Helvetica",20),bg="#77D2EE")
    email.grid(row=3,column=0,sticky=W,padx=20,pady=15)
    bld=Label(needers_window,text="Enter blood group",font=("Helvetica",20),bg="#77D2EE")
    bld.grid(row=4,column=0,sticky=W,padx=20,pady=15)
    place=Label(needers_window,text="Enter your place",font=("Helvetica",20),bg="#77D2EE")
    place.grid(row=5,column=0,sticky=W,padx=20,pady=15)

    namebox = Entry(needers_window,width=25,font=("Helvetica",15))
    namebox.grid(row=1,column=1)
    mobbox = Entry(needers_window,width=25,font=("Helvetica",15))
    mobbox.grid(row=2,column=1)
    emailbox = Entry(needers_window,width=25,font=("Helvetica",15))
    emailbox.grid(row=3,column=1)
    bldbox = Entry(needers_window,width=25,font=("Helvetica",15))
    bldbox.grid(row=4,column=1)
    placebox = Entry(needers_window,width=25,font=("Helvetica",15))
    placebox.grid(row=5,column=1)
    
    
    a=Label(needers_window,text=" ",bg="#77D2EE").grid(row=6,column=0)
    submit =Button(needers_window,text="SUBMIT",font=("Helvetica",15),relief="raised",bg="white",command=submiti,width=12)
    submit.grid(row=7,column=0)
    z = Button(needers_window,text="SEND EMAIL",font=("Helvetica",15),relief="raised",bg="white",command=emailing,width=12)
    z.grid(row=7,column=1)

 
button2 = Button(root,text="NEED BLOOD!!",fg="white",bg="#eb2828",font=("Helvetica",15),padx=75,pady=20,command=opennew)
button2_window=mycanvas.create_window(300,230,window=button2)
button1 = Button(root,text="DONATE BLOOD!!",fg="white",bg="#eb2828",padx=63,pady=20,font=("Helvetica",15),command=open)
button1_window=mycanvas.create_window(300,330,window=button1)

mainloop()