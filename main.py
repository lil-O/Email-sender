from tkinter import *
import smtplib, ssl

y = 0
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
context = ssl.create_default_context()

root = Tk()
root.geometry("1000x600+0+0")
root.title("Spam people with emails hehe")

Top = Frame(root, width=1000, height=300, bg="powder blue", relief=SUNKEN)
Top.pack(side=TOP)

bottom = Frame(root, width=1000, height=400, bg="powder blue", relief=SUNKEN)
bottom.pack(side=BOTTOM)

email = StringVar()
password = StringVar()
email2 = StringVar()
sender_email = ""
sender_password = ""
receiver_email = ""
message = StringVar()
message_mes = ""
time = StringVar()
time_t = ""





def submitData():
    global sender_email
    global sender_password
    global receiver_email
    global message_mes
    global time_te

    message_mes = message.get()
    time_t = time.get()
    sender_email = email.get()
    sender_password = password.get()
    receiver_email = email2.get()



def f():
    sendMail()

def sendMail():


    try:
        while True:
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, receiver_email, message_mes)
    except:
        print("bad credentials")


#############################################################################################
emailEntry = Entry(Top, font=('ariel', 15, "bold"), bd=10, bg="powder blue", textvariable=email)
emailEntry.grid(row=1, column=1)

emailLabel = Label(Top, font=('ariel', 15, "bold"), text='Your username', bg='powder blue')
emailLabel.grid(row=1, column=0)
#############################################################################################

PassEntry = Entry(Top, font=('ariel', 15, "bold"), bd=10, bg="powder blue", textvariable=password)
PassEntry.grid(row=2, column=1)

passLabel = Label(Top, font=('ariel', 15, "bold"), text='Your password', bg='powder blue')
passLabel.grid(row=2, column=0)

titleLable = Label(Top, font=('ariel', 15, "bold"), text='ENTER YOUR EMAIL AND PASSWORD:     ', bg='powder blue',
                   justify=CENTER)
titleLable.grid(row=0, column=0)

################################################################################################

submitPassEmail = Button(Top, font=('Roboto', 15, "bold"), text="SUBMIT  YOUR \n USERNAME AND PASSWORD",
                         bg='powder blue', bd=10, command=submitData)
submitPassEmail.grid(row=0, column=4)

subjectEntry = Entry(bottom, font=('ariel', 15, "bold"), bd=10, bg="powder blue", width=59)
subjectEntry.grid(row=0, column=1)
subjectLabel = Label(bottom, font=('ariel', 15, "bold"), text='Subject of your email', bg='powder blue')
subjectLabel.grid(row=0, column=0)

textEntry = Entry(bottom, font=('ariel', 15, "bold"), bd=10, bg="powder blue", width=59, textvariable=message)
textEntry.grid(row=1, column=1)
textLabel = Label(bottom, font=('ariel', 15, "bold"), text='Actual text inside your email', bg='powder blue', bd=30, )
textLabel.grid(row=1, column=0)

DurEntry = Entry(bottom, font=('ariel', 15, "bold"), bd=10, bg="powder blue", width=59, textvariable = time)
DurEntry.grid(row=2, column=1)
DurLabel = Label(bottom, font=('ariel', 15, "bold"), text='How many times do you want to send?', bg='powder blue',
                 bd=30, )
DurLabel.grid(row=2, column=0)

reEntry = Entry(bottom, font=('ariel', 15, "bold"), textvariable=email2, bd=10, bg="powder blue", width=59)
reEntry.grid(row=3, column=1)
reLabel = Label(bottom, font=('ariel', 15, "bold"), text='reciever email', bg='powder blue', bd=30)
reLabel.grid(row=3, column=0)

send = Button(bottom, font=('ariel', 15, "bold"), bd=10, bg="powder blue", text="Send", width=10, command=f)
send.grid(row=4, column=0)

root.mainloop()
