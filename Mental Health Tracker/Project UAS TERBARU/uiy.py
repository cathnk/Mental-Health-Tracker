from tkinter import *
from tkinter.messagebox import showinfo
from pygame import mixer 
import datetime 
import textwrap
from PIL import ImageTk, Image
import webbrowser
from customtkinter import *
import random



class project:
    NILAI = 0
    
    def __init__ (self, window):
        self.window = window 
        window.title("Mental Health Tracker")
        window.configure(bg="#c1f2df")
        window.state("zoomed")
        self.ukw = self.window.winfo_screenwidth
        self.ukh = self.window.winfo_screenheight
        self.mainframe=Frame(self.window,bg='red')
        self.mainframe.place(x=0, y= 0)
        self.main_page_first = Image.open("C:/Project UAS TERBARU/Tampilan Awal.png")
        self.resize = self.main_page_first.resize((self.window.winfo_screenwidth(), self.window.winfo_screenheight()), Image.LANCZOS)
        self.main_page_first_read = ImageTk.PhotoImage(self.resize)
        self.label_main_page_first = Label(self.window, image=self.main_page_first_read)
        self.label_main_page_first.place(x=0, y=0, relwidth=1, relheight=1)
        window.iconbitmap("C:/Project UAS TERBARU/Icon.ico")
        self.imgn = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Arrow Right.png"))
        self.bttn = Button(self.label_main_page_first,image=self.imgn, command=self.wlcm, bg="#98bffa", fg="white", border=0, font=("Sitka Small Semibold",25), activebackground="#98bffa")
        self.bttn.place(relwidth=0.1, relheight=0.1, relx = 0.85, rely=0.85)
        self.soald = open("C:/Project UAS TERBARU/data_soald.txt", "r").read().split("\n")
        self.i = 0
        self.soalk = open("C:/Project UAS TERBARU/data_soalk.txt", "r").read().split("\n")
        self.j = 0
        self.soals = open("C:/Project UAS TERBARU/data_soals.txt", "r").read().split("\n")
        self.k = 0

        self.quotes = [
    "Masalah kesehatan mental tidak\nmenentukan siapa Anda.", 
    "Kepercayaan akan diri sendiri\nadalah rahasia utama untuk\nsukses.",
    "Kesehatan mental dan psikologis\nsangat mahal harganya.",
    "Menangislah jika itu membuatmu\ntenang. ",
    "Kamu tidak berbeda \nkamu hanya spesial.",
    "Ketika hidup memiliki ribuan\nalasan untuk menangis, kamu\nharus memiliki setidaknya satu\nalasan untuk tersenyum.",
    "Banggalah pada \ndirimu sendiri." ]

    def back(self):
         self.usn.destroy()
         self.login()
        
    def back1(self):
         self.usn.destroy()
         self.register()

    def register(self):
        def cek():
            def cek2():
                 a = self.el11.get()
                 akun_pw = data_akun_text.split('\n')
                 for akun in akun_pw:
                        if akun == '':
                            continue
                        ap = akun.split(',')
                        if ap[0] == a:
                            self.l.destroy()
                            self.wrusn.destroy()
                            used = Label(self.usn, text="Username is used",font=("Sitka Small Semibold",25, 'bold'), fg="red",bg="#4592bf")
                            used.place(x=230,y=200)
                            self.el11 = StringVar()
                            self.el1 = Entry(self.usn, border=0, text=self.el11, bg="white", fg="navy", font=("Sitka Small Semibold",22, 'bold'), justify=CENTER)
                            self.el1.place(x= 185, y =298)
                            self.el1.insert(0, "(..@nesa.com)")
                            self.el1.bind("<FocusIn>", lambda e: self.el1.delete(0,"end"))
                            self.imgb = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Arrow Left.png"))
                            Button(self.usn, image=self.imgb, command=self.back, bg="#38b6ff", border=0, fg="white", font=("Sitka Small Semibold",20, 'bold'), activebackground="#38b6ff").place(x=67, y=725)
    
                            return False
                 return True
                    
            global a
            a = self.el11.get()
            if a[-1:-10:-1][::-1] != '@nesa.com':
                    self.l.destroy()
                    self.wrusn = Label(self.usn,text="Username is incorrect",font=("Sitka Small Semibold",25, 'bold'), fg="red",bg="#4592bf")
                    self.wrusn.place(x=190,y=200)
                    self.el11 = StringVar()
                    self.el1 = Entry(self.usn, border=0, text=self.el11, bg="white", fg="navy", font=("Sitka Small Semibold",22, 'bold'), justify=CENTER)
                    self.el1.place(x= 185, y =298)
                    self.el1.insert(0, "(..@nesa.com)")
                    self.el1.bind("<FocusIn>", lambda e: self.el1.delete(0,"end"))
                    self.imgb = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Arrow Left.png"))
                    Button(self.usn, image=self.imgb, command=self.back, bg="#38b6ff", border=0, fg="white", font=("Sitka Small Semibold",20, 'bold'), activebackground="#38b6ff").place(x=67, y=725)
    
                    c = False
            else : c = cek2()

            def cekpw():
                x = self.el22.get()
                if len(x)<6 :
                    self.l2.destroy()
                    wrpw = Label(self.usn,text="Password is incorrect    ", font=("Sitka Small Semibold",25, 'bold'), fg="red",bg="#4592bf")
                    wrpw.place(x=185, y=180)
                    self.el22 = Entry(self.usn, bg="white", fg="navy", border=0,font=("Sitka Small Semibold",22, 'bold'), justify=CENTER )
                    self.el22.place(x= 185, y =298)
                    self.el22.insert(0, "Try Again")
                    self.el22.bind("<FocusIn>", lambda e: self.el22.delete(0,"end"))
                    self.imgb = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Arrow Left.png"))
                    Button(self.usn, image=self.imgb, command=self.back1, bg="#38b6ff", border=0, fg="white", font=("Sitka Small Semibold",20, 'bold'), activebackground="#38b6ff").place(x=67, y=725)
    

                else:
                    self.data_akun.write(f"{a},{x}\n")
                    self.data_akun.close()
                    self.usn.destroy()
                    self.login()


            if c == True :

                self.l2 = Label(self.usn, text="Make New Account", fg="white", bg="#4592bf", font=("Sitka Small Semibold",30, 'bold'))
                self.l2.place(x= 185, y= 180)
                self.el22 = Entry(self.usn, bg="white", fg="navy", border=0,font=("Sitka Small Semibold",22, 'bold'), justify=CENTER )
                self.el22.place(x= 185, y =298)
                self.el22.insert(0, "Sign Password")
                self.el22.bind("<FocusIn>", lambda e: self.el22.delete(0,"end"))

                self.bttn2 = Button(self.usn, text="OK",border=0, bg="#d9d9d9", fg="navy", command=cekpw, font=("Sitka Small Semibold",13, 'bold'))
                self.bttn2.place(x=367, y= 400)


                self.imgb = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Arrow Left.png"))
                Button(self.usn, image=self.imgb, command=self.back1, bg="#38b6ff", border=0, fg="white", font=("Sitka Small Semibold",20, 'bold'), activebackground="#38b6ff").place(x=67, y=725)
    
        self.frm2.destroy()
        self.frm1=Frame(bg='red')
        self.frm1.pack(ipadx = 640, ipady = 360, expand = True)
        img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Register.png"))
        self.usn = Label(self.frm1, image=img)
        self.usn.image = img
        self.usn.pack(ipadx=1200, ipady=864)
        
        self.data_akun = open("C:/Project UAS TERBARU/data_akun.txt",'a+')
        self.data_akun_r = open("C:/Project UAS TERBARU/data_akun.txt", 'r')
        data_akun_text = self.data_akun_r.read()

        self.l = Label(self.usn, text="Make New Account", fg="white", bg="#4592bf", font=("Sitka Small Semibold",30, 'bold'))
        self.l.place(x= 185, y= 180)
        self.el11 = StringVar()
        self.el1 = Entry(self.usn, border=0, text=self.el11, bg="white", fg="navy", font=("Sitka Small Semibold",22, 'bold'), justify=CENTER)
        self.el1.place(x= 185, y =298)
        self.el1.insert(0, "(..@nesa.com)")
        self.el1.bind("<FocusIn>", lambda e: self.el1.delete(0,"end"))

        self.bttn = Button(self.usn, text="OK", border=0, bg="#d9d9d9", fg="navy", command=cek,font=("Sitka Small Semibold",13, 'bold'), activebackground="#d9d9d9")
        self.bttn.place(x=367, y= 400)
        self.imgb = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Arrow Left.png"))
        Button(self.usn, image=self.imgb, command=self.back, bg="#38b6ff", border=0, fg="white", font=("Sitka Small Semibold",20, 'bold'), activebackground="#38b6ff").place(x=67, y=725)
    

    def login(self):
        def masuk():
             def checkin(usr, pws):
                data_akun = open("C:/Project UAS TERBARU/data_akun.txt",'r').read().split('\n')
                a = 0
                for akun in data_akun:
                    if akun == '':
                        continue
                    acpw = akun.split(',')
                    ac = acpw[0]
                    pwd = acpw[1]
                    if (usr==ac and pws==pwd):
                        a += 1
                        self.wlcm()
                        break
                    else:
                        pass
                if a == 0 :
                    showinfo(title="Info", message="Wrong Ussername Or Password")
                    
             self.masuk= masuk
             usr = self.lbl2.get()
             pws = self.lbl3.get()
             checkin(usr, pws) 

        self.label_main_page_first.destroy()
        self.mainframe=Frame(self.window,bg='red')
        self.mainframe.place(x=0, y= 0)
        self.main_page_first = Image.open("C:/Project UAS TERBARU/Project UAS TERBARU/Login.png")
        self.resize = self.main_page_first.resize((self.window.winfo_screenwidth(), self.window.winfo_screenheight()), Image.LANCZOS)
        self.main_page_first_read = ImageTk.PhotoImage(self.resize)
        self.label_main_page_first = Label(self.window, image=self.main_page_first_read)
        self.label_main_page_first.place(x=0, y=0, relwidth=1, relheight=1)
        usrnm = StringVar()
        self.lbl2 = Entry(self.label_main_page_first,justify=CENTER, text=usrnm, border=0, bg="#40a1d8", font=("Sitka Small Semibold",22, 'bold'), fg="white")
        self.lbl2.place(relwidth=0.17, relheight=0.1, relx=0.68, rely=0.41)
        self.lbl2.insert(0, "inop@nesa.com")
        self.lbl2.bind("<FocusIn>", lambda e: self.lbl2.delete(0,"end"))

        pw = StringVar()
        self.lbl3 = Entry(self.label_main_page_first, justify=CENTER, text=pw, border=0, bg="#40a1d8", font=("Sitka Small Semibold",22, 'bold'), fg="white")
        self.lbl3.place(relwidth=0.17, relheight=0.1, relx=0.68, rely=0.57)
        self.lbl3.insert(0, "inop123")
        self.lbl3.bind("<FocusIn>", lambda e: self.lbl3.delete(0,"end"))


        self.lgnbutton = Button(self.label_main_page_first, text="LOGIN",bg="#baf5ff", border=0, fg="black", command=masuk, font=("Sitka Small Semibold",20, 'bold'), activebackground="#baf5ff").place(relwidth=0.17, relheight=0.1, relx=0.68, rely=0.7)
        self.lbl4 = Label(self.label_main_page_first, text="New User ?", bg="#baf5ff", fg="salmon", font=("Sitka Small Semibold",15, 'bold')).place(relwidth=0.17, relheight=0.1, relx=0.61, rely=0.86)

        self.rgstrbttn = Button(self.label_main_page_first, text="Create an Account.", bg="#baf5ff", command=self.register, border=0, fg="navy", font=("Sitka Small Semibold",15, 'bold'), activebackground="#baf5ff")
        self.rgstrbttn.place(relwidth=0.17, relheight=0.1, relx=0.74, rely=0.86)


        def button_show():
            if self.lbl3['show'] == '*':
                self.lbl3['show'] = ''
                toggle_btn.config(image=self.imgs)
            else:
                self.lbl3['show'] = '*'
                toggle_btn.config(image=self.imgh)

        self.imgs = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/show.png"))
        self.imgh = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/hide.png"))
        toggle_btn = Button(self.label_main_page_first, command=button_show,  bg="#c6f6ff", border=0, fg="black", font=("Sitka Small Semibold",22, 'bold'), activebackground="#c6f6ff") 
        toggle_btn.config(image=self.imgh)
        toggle_btn.place(relwidth=0.08, relheight=0.08, relx=0.88, rely=0.58)

    def wlcm(self):
        self.label_main_page_first.destroy()
        self.mainframe=Frame(self.window,bg='red')
        self.mainframe.place(x=0, y= 0)
        self.main_page_first = Image.open("C:/Project UAS TERBARU/Username.png")
        self.resize = self.main_page_first.resize((self.window.winfo_screenwidth(), self.window.winfo_screenheight()), Image.LANCZOS)
        self.main_page_first_read = ImageTk.PhotoImage(self.resize)
        self.label_main_page_first = Label(self.window, image=self.main_page_first_read)
        self.label_main_page_first.place(x=0, y=0, relwidth=1, relheight=1)                                                                                                                                                                                                                                                                                                                                                  
        self.l1 = Label(self.label_main_page_first, text="Input Nickname", bg="#4592bf", fg="white", font=("Sitka Small Semibold",30, 'bold'))
        self.l1.place(relwidth=0.25, relheight=0.1, relx=0.58, rely=0.28)
        self.l1s = StringVar()
        self.l1e = Entry(self.label_main_page_first, text=self.l1s, border=0, bg="red", fg="salmon", justify=CENTER, font=("Sitka Small Semibold",22, 'bold'))
        self.l1e.place(relwidth=0.14, relheight=0.09, relx=0.64, rely=0.42)
        self.bttn = Button(self.label_main_page_first, text="Next", bg="red", fg="salmon",activebackground="#d9d9d9", command=self.cn,  font=("Sitka Small Semibold",13, 'bold'), border=0, activeforeground="salmon")
        self.bttn.place(relwidth=0.047, relheight=0.048, relx=0.685, rely=0.570)

    def cn(self):
        nick = self.l1e.get()
        if nick != "":
            self.mainmenu()
            pass
        else :
            showinfo(title="Info", message="Invalid Nickname")

    def change_quote(self):
        index = random.randint(0, len(self.quotes)-1)  
        return self.quotes[index]
                    

    def mainmenu(self):
        self.label_main_page_first.destroy()
        self.mainframe=Frame(self.window,bg='red')
        self.mainframe.place(x=0, y= 0)
        self.main_page_first = Image.open("C:\Project UAS TERBARU\Project UAS TERBARU\Main Menu.png")
        self.resize = self.main_page_first.resize((self.window.winfo_screenwidth(), self.window.winfo_screenheight()), Image.LANCZOS)
        self.main_page_first_read = ImageTk.PhotoImage(self.resize)
        self.label_main_page_first = Label(self.window, image=self.main_page_first_read)
        self.label_main_page_first.place(x=0, y=0, relwidth=1, relheight=1)
        self.frame_l = Frame(self.label_main_page_first, bg="#c1f6fe")
        self.frame_l.place(relwidth=0.35, relheight=0.11, relx=0.23, rely=0.09)
        self.frame_m = Frame(self.label_main_page_first, bg="white")
        self.frame_m.place(relwidth=0.2, relheight=0.05, relx=0.327, rely=0.257)
        self.frame_m1 = Frame(self.label_main_page_first, bg="white")
        self.frame_m1.place(x= 1100, y= 203, width=300, height=50)
        self.frame_m2 = Frame(self.label_main_page_first, bg="white")
        self.frame_m2.place(x= 403, y= 536, width=380, height=70)
        self.frame_m3 = Frame(self.label_main_page_first, bg="#145da0")
        self.frame_m3.place(x= 395, y= 695, width=630, height=80)
        self.frame_m4 = Frame(self.label_main_page_first, bg="white")
        self.frame_m4.place(x= 1084, y= 688, width=370, height=90)
        self.frame_m5 = Frame(self.label_main_page_first, bg="#123f7b")
        self.frame_m5.place(x= 830, y= 516, width=650, height=110)
        self.frame_m6 = Frame(self.label_main_page_first, bg="#38b6ff")
        self.frame_m6.place(x= 405, y= 260, width=500, height=200)
        self.frame_m7 = Frame(self.label_main_page_first, bg="#c1f3ff")
        self.frame_m7.place(x=10, y= 170, width=330, height=600)
        self.frame_m8 = Frame(self.label_main_page_first, bg="#537bb8")
        self.frame_m8.place(x= 995, y= 264, width=500, height=200)
       
        self.fm2 = Frame(self.label_main_page_first, bg="red")
        self.fm2.place(relwidth=1, relheight=0.07) 

        self.imgl = PhotoImage(file="C:/Project UAS TERBARU/Gambar Jurnal.png")
        self.ljurnal = Label(self.frame_m8, image=self.imgl, bg="#537bb8", justify=CENTER)
        self.ljurnal.place(x=20, y=20)
        self.q2 = "You're not alone.\tIt's okay to ask for\tsupport when you\tneed it."
        self.q22 = textwrap.wrap(text=self.q2, width=25)
        self.q222 = '\n'.join(self.q22)
        self.q12 = Label(self.frame_m8,justify=CENTER, text=self.q222, bg="#537bb8", fg="snow", font=("Sitka Small Semibold",15, 'bold'))
        self.q12.place(x= 275, y=40)
        self.imgd = PhotoImage(file="C:/Project UAS TERBARU/Doctor Main Menu.png")
        self.l11234 = Label(self.frame_m7, image=self.imgd, bg="#c1f3ff", justify=CENTER)
        self.l11234.place(x=30, y=0)
        self.quote_text = self.change_quote()
        self.q = Label(self.frame_m6,justify=LEFT, text=self.quote_text, bg="#38b6ff", fg="snow", font=("Sitka Small Semibold",17, 'bold'))
        self.q.place(x=40, y=20)
        self.l11 = Label(self.fm2, text="Mental Health",bg="#473a5f", font=("Sitka Small Semibold",20, 'bold'), fg="white" )
        self.l11.place(relwidth=0.13, relheight=0.5, relx=0.75, rely=0.26)
        self.l112 = Label(self.fm2, text="Tracker",bg="#473a5f", font=("Sitka Small Semibold",20, 'bold'), fg="aqua" )
        self.l112.place(relwidth=0.08, relheight=0.5, relx=0.89, rely=0.26)
        self.imgic = PhotoImage(file="C:/Project UAS TERBARU/Icon.png") 
        self.l1123 = Label(self.fm2, image=self.imgic, bg="#473a5f")
        self.l1123.place(relwidth=0.03, relheight=0.7, relx=0.7, rely=0.17)
        self.imgmrh4 = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Emoji 1.png"))
        self.bttn = Button(self.frame_m5,image=self.imgmrh4, bg="#123f7b",  border=0, activebackground="#123f7b", command=self.marah4)
        self.bttn.place(x=520, y=0)
        self.imgmrh3 = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Emoji 2.png"))
        self.bttn = Button(self.frame_m5,image=self.imgmrh3, bg="#123f7b",  border=0, activebackground="#123f7b", command=self.marah3)
        self.bttn.place(x=390, y=0)
        self.imgmrh2 = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Emoji 3.png"))
        self.bttn = Button(self.frame_m5,image=self.imgmrh2, bg="#123f7b",  border=0, activebackground="#123f7b", command=self.marah2)
        self.bttn.place(x=260, y=0)
        self.imgmrh1 = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Emoji 4.png"))
        self.bttn = Button(self.frame_m5,image=self.imgmrh1, bg="#123f7b",  border=0, activebackground="#123f7b", command=self.marah1)
        self.bttn.place(x=130, y=0)
        self.imgmrh = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Emoji 5.png"))
        self.bttn = Button(self.frame_m5,image=self.imgmrh, bg="#123f7b",  border=0, activebackground="#123f7b", command=self.marah)
        self.bttn.place(x=-2, y=0)
        self.bttn = Button(self.frame_m4, border=0,text="Test Mental Health", bg="white", fg="black",command=self.test, font=("Sitka Small Semibold",25, 'bold'), activebackground="white", activeforeground="lightgrey" )
        self.bttn.place(x= 0, y=0, width=370, height=90)
        self.l6 = Label(self.frame_m3, text="Know yourself better, cause mental health is\na journey of self-discovery and growth", bg="#145da0", fg="white",justify=CENTER, font=("Sitka Small Semibold",19, 'bold'))
        self.l6.place(x= 6, y=-3)
        self.l5 = Label(self.frame_m2, text="Your Mood Today", bg="white", fg="black", font=("Sitka Small Semibold",30, 'bold'))
        self.l5.place(x= 3, y=-3)
        self.l3 = Label(self.frame_m, text="Daily Motivation", bg="white", fg="black", font=("Sitka Small Semibold",25, 'bold'))
        self.l3.place(x= 3, y=-6)
        self.l4 = Button(self.frame_m1,activebackground="white",command=self.journal,  text="Journaling",border=0, bg="white", fg="black", font=("Sitka Small Semibold",30, 'bold'), justify=CENTER)
        self.l4.place(x= 26, y=-30)
       
        
        
        self.l1 = Label(self.frame_l, text=f"Haii  {self.l1s.get()}", bg="#c1f6fe", fg="black", font=("Sitka Small Semibold",30, 'bold'))
        self.l1.place(relwidth=0.5, relheight=0.4, rely=0)
        self.l2 = Label(self.frame_l, text="Welcome, Happy To See You", bg="#c1f6fe", fg="black", font=("Sitka Small Semibold",25, 'bold'))
        self.l2.place(relwidth=1, relheight=0.53, relx=-0.03, rely=0.4) 
        self.imgt = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Option.png"))
        self.bttnsl = Button(self.fm2, image=self.imgt, bg="#473a5f",border=0, fg="salmon", command=self.nextf, activebackground="#473a5f")
        self.bttnsl.place(x= 10, y=7)
        self.fr1 = Frame(self.label_main_page_first,bg="#67d4ff")  
        self.fr1.place(x=-320, y =0, width=320, height= 864)
        self.imgbtest = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon Test.png"))
        self.bttnt = Button(self.fr1,  image=self.imgbtest, border=0, bg="#67d4ff",activebackground="#67d4ff", activeforeground="snow", fg="salmon",command=self.test, font=("Sitka Small Semibold",25, 'bold'))
        self.bttnt.place(x=-80, y=150, width=400, height=85)
        self.imghstry = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon History.png"))
        self.bttnh = Button(self.fr1, image=self.imghstry,border=0, bg="#67d4ff",activebackground="#67d4ff", activeforeground="snow", fg="salmon", command=self.history, font=("Sitka Small Semibold",25, 'bold'))
        self.bttnh.place(x= -57, y=250, width=400, height=85)
        self.imgmn = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon Home.png"))
        self.bttnm = Button(self.fr1, image=self.imgmn, border=0, bg="snow", activebackground="snow", activeforeground="snow", fg="silver", font=("Sitka Small Semibold",25, 'bold'))
        self.bttnm.place(x= -68, y=50, width=400, height=85)
        self.imgjrnl = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon Jurnal.png"))
        self.bttnj = Button(self.fr1, image=self.imgjrnl, border=0, bg="#67d4ff", activebackground="#67d4ff", activeforeground="snow", fg="salmon",command=self.journal, font=("Sitka Small Semibold",25, 'bold'))
        self.bttnj.place(x= -65, y=350, width=400, height=85)
        self.logout = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon Logout.png"))
        self.bttnl = Button(self.fr1, image=self.logout, border=0, bg="#67d4ff", activebackground="snow", activeforeground="snow", fg="salmon", command=self.exit, font=("Sitka Small Semibold",25, 'bold'))
        self.bttnl.place(x= -58, y=650, width=400, height=85)
        self.imgbt= ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Slide Left.png"))
        self.btnslb= Button(self.fr1, image=self.imgbt, bg="#67d4ff", fg="black", command=self.prevf, activebackground="#67d4ff", border=0).place(x=265, y=437)
        

        self.a = -320 
        self.window.after(10000, self.update_quote)
    
    def update_quote(self):
        self.quote_text = self.change_quote()
        self.q.config(text=self.quote_text)
        

    
     
    def marah(self):
        webbrowser.open("https://www.crazygames.co.id/game/funny-kitty-care")

    def marah1(self):
        webbrowser.open("https://www.crazygames.co.id/game/capybara-clicker-2")

    def marah2(self):
        webbrowser.open("https://www.crazygames.co.id/game/animal-shopping-supermarket")

    def marah3(self):
        webbrowser.open("https://www.crazygames.co.id/game/funny-angela-haircut")

    def marah4(self):
       webbrowser.open("https://www.crazygames.co.id/game/squishy-fruits")

    def nextf(self):
        self.a += 10
        if self.a > 0:
            return self.a
        else: 
            self.window.after(10, self.nextf)
            self.fr1.place_configure(x=self.a)

    def prevf(self):
        self.a -= 10
        if self.a < -320:
            return self.a
        else: 
            self.window.after(10, self.prevf)
            self.fr1.place_configure(x=self.a)
        
    

    def journal(self):
        self.fm1.destroy()
        img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Tampilan Jurnal.png"))
        self.fj = Label(image=img)
        self.fj.image = img
        self.fj.pack(ipadx=1200, ipady=864)
        self.fj2 = Frame(bg="#07a4ff")
        self.fj2.place(x= 690, y=78, width=470, height=85)
        self.fj1 = Frame(bg="#f3f5f6")
        self.fj1.place(x= 460, y=300, width=940, height=380)
        self.fj3 = Frame(bg="#004aad")
        self.fj3.place(x= 1193, y=687, width=170, height=45)
        self.fj4 = Frame(bg="#c1f7ff")
        self.fj4.place(x=10, y= 170, width=330, height=600)
        self.imgdc = PhotoImage(file="C:/Project UAS TERBARU/Doctor Jurnal.png")
        self.ldc = Label(self.fj4, image=self.imgdc, bg="#c1f7ff", justify=CENTER)
        self.ldc.place(x=70, y=0)
        self.l2e = Label(self.fj2, text=f"{self.l1s.get()} Yuk Curhat", font=("Sitka Small Semibold",30, 'bold'), bg="#07a4ff", fg="snow")
        self.l2e.place(x=3, y=1)
        self.l1e = Text(self.fj1, border=0, bg="#f3f5f6", fg="salmon", font=("Sitka Small Semibold",25, 'bold'))
        self.l1e.place(x=40, y=20)
        self.l1e.insert("1.0", "   Bagaimana perasaanmu hari ini ?")
        self.l1e.bind("<FocusIn>", lambda e: self.l1e.delete('1.0',"end"))
        self.bttn = Button(self.fj3, border=0, activebackground="#004aad", text="Kirim", bg="#004aad", fg="white", command=self.cekj, font=("Sitka Small Semibold",20, 'bold'))
        self.bttn.place(x= 0, y=0, width=170, height=45 )   
        self.imgt = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Option.png"))
        self.fm2 = Frame(bg="#473a5f")
        self.fm2.place(x=0, y=0, width=1536, height=50)
        self.l11 = Label(self.fm2, text="Mental Health",bg="#473a5f", font=("Sitka Small Semibold",20, 'bold'), fg="white" )
        self.l11.place(x= 1150, y=1 )
        self.l112 = Label(self.fm2, text="Tracker",bg="#473a5f", font=("Sitka Small Semibold",20, 'bold'), fg="aqua" )
        self.l112.place(x= 1360, y=1 )
        self.imgic = PhotoImage(file="C:/Project UAS TERBARU/Icon.png")
        self.l1123 = Label(self.fm2, image=self.imgic, bg="#473a5f")
        self.l1123.place(x=1100, y=1)
        self.bttnsl = Button(self.fm2, image=self.imgt, bg="#473a5f",border=0, fg="salmon", command=self.nextf, activebackground="#473a5f")
        self.bttnsl.place(x= 10, y=7)
        self.fr1 = Frame(bg="#67d4ff")
        self.fr1.place(x=-320, y =0, width=320, height= 864)
        self.imgbtest = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon Test.png"))
        self.bttnt = Button(self.fr1,  image=self.imgbtest, border=0, bg="#67d4ff",activebackground="#67d4ff", activeforeground="snow", fg="salmon",command=self.backt1, font=("Sitka Small Semibold",25, 'bold'))
        self.bttnt.place(x=-80, y=150, width=400, height=85)
        self.imghstry = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon History.png"))
        self.bttnh = Button(self.fr1, image=self.imghstry,border=0, bg="#67d4ff",activebackground="#67d4ff", activeforeground="snow", fg="salmon", command=self.backh1, font=("Sitka Small Semibold",25, 'bold'))
        self.bttnh.place(x= -57, y=250, width=400, height=85)
        self.imgmn = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon Home.png"))
        self.bttnm = Button(self.fr1, image=self.imgmn, border=0, bg="#67d4ff", activebackground="#67d4ff", activeforeground="snow", fg="silver", font=("Sitka Small Semibold",25, 'bold'), command=self.backm1)
        self.bttnm.place(x= -68, y=50, width=400, height=85)
        self.imgjrnl = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon Jurnal.png"))
        self.bttnj = Button(self.fr1, image=self.imgjrnl, border=0, bg="snow", activebackground="snow", activeforeground="snow", fg="salmon", font=("Sitka Small Semibold",25, 'bold'))
        self.bttnj.place(x= -65, y=350, width=400, height=85)
        self.logout = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon Logout.png"))
        self.bttnl = Button(self.fr1, image=self.logout, border=0, bg="#67d4ff", activebackground="snow", activeforeground="snow", fg="salmon", command=self.exit3, font=("Sitka Small Semibold",25, 'bold'))
        self.bttnl.place(x= -58, y=650, width=400, height=85)
        self.imgbt= ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Slide Left.png"))
        self.btnslb= Button(self.fr1, image=self.imgbt, bg="#67d4ff", fg="black", command=self.prevf, activebackground="#67d4ff", border=0).place(x=265, y=437)
       

        self.a = -320


    def cekj(self):
        b = self.l1s.get()
        a = self.l1e.get('1.0', END)
        perasaan_negatif = ["sedih", "marah", "bingung", "ragu", "takut", "kecewa"]
        perasaan_positif = ["senang", "bahagia", "gembira", "puas", "lega", "semangat", "bangga", "antusias"]
        self.perasaan = ""
        self.penyebab = ""

        for i in perasaan_positif :
            if i in a :
               self.perasaan = "Positif"
               if "nilai" in a :
                   self.penyebab = "Nilai"
               elif "keluarga" in a :
                   self.penyebab = "Keluarga"
               elif "pacar" in a :
                   self.penyebab = "Pacar"
               elif "teman" in a :
                   self.penyebab = "Teman"
               elif "kerja" in a :
                   self.penyebab = "Kerja"

        for i in perasaan_negatif :
           if i in a :
               self.perasaan = "Negatif"
               if "nilai" in a :
                   self.penyebab = "Nilai"
               elif "keluarga" in a :
                   self.penyebab = "Keluarga"
               elif "pacar" in a :
                   self.penyebab = "Pacar"
               elif "teman" in a :
                   self.penyebab = "Teman"
               elif "kerja" in a :
                   self.penyebab = "Kerja"

        a = b + ',  ' + self.berikan_saran(self.perasaan, self.penyebab)
        a = textwrap.wrap(a, width= 70)
        a = '\n'.join(a)
        self.l1e.destroy()
        
        self.fj5 = Frame(bg="#f3f5f6")
        self.fj5.place(x= 477, y=687, width=270, height=60)
        self.rsj = Label(self.fj1, border=0, text=a, justify=LEFT, bg="#f3f5f6", fg="salmon", font=("Sitka Small Semibold",15, 'bold'))
        self.rsj.place(x=20, y=20, width=905)
        self.bttnj1 = Button(self.fj3, text="Terimakasih\nSaranya",border=0, activebackground="#004aad", bg="#004aad", fg="white", command=self.resetj, font=("Sitka Small Semibold",13, 'bold'))
        self.bttnj1.place(x= 0, y=0, width=170, height=45)
        self.bttnj2 = Button(self.fj5, text="Hubungi Psikolog",border=0, activebackground="#f3f5f6", bg="#f3f5f6", fg="blue", command=self.openlink, font=("Sitka Small Semibold",15, 'bold'), justify=LEFT)
        self.bttnj2.place(x = 0, y=0,width=270, height=60 )

    def openlink(self):
        webbrowser.open("wa.me/62895365021551")


    def berikan_saran(self, perasaan, penyebab):

        if perasaan == "Negatif":
            if penyebab == "Nilai":
                return "Mendapat nilai yang tidak sesuai dengan yang kita harapkan pastinya membuat perasaan kita sedih bahkan kecewa dengan diri kita sendiri. Perasaan ini kadang disebabkan karena kita takut mengecewakan orang tua ataupun takut diejek oleh teman kita. Dalam fase ini, STOP SALAHKAN DIRI SENDIRI! Karena kamu sudah lakukan yang terbaik. Satu hal yang harus diingat bahwa nilai bukanlah segalanya meskipun segalanya butuh nilai, namun proseslah yang terpenting. Nelson Mandela pernah berkata ” Jangan menilai saya dari kesuksesan, tetapi nilai saya dari seberapa sering saya jatuh dan berhasil bangkit kembali.”. So cheer up, life must go on and you must better than before."
            elif penyebab == "Keluarga":
                return "Kesuksesan dan harta, bukanlah jaminan bisa membuat keluarga bahagia. Akan tetapi rasa cinta, waktu, dan kepedulian itu yang menjadi fondasi dalam keluarga. Permasalahan, perdebatan, kesalahpahaman tentu saja bisa terjadi dan tidak bisa dihindari, hal ini dapat disebabkan oleh miss komunikasi, kurangnya waktu bersama dan masih banyak lainnya. Namun ingat komunikasi selalu menjadi penyelesaian terbaik dalam segala hal. Kita memang tidak bisa memilih dilahirkan dikeluarga seperti apa, namun apapun yang terjadi keluarga tetap yang terutama di hidup kita. Sejauh apapun kakimu melangkah, keluarga adalah tempat ternyaman yang selalu dirindukan untuk pulang."
            elif penyebab == "Pacar":
                return "Hubungan yang baik adalah hubungan yang berjalan dua arah. Kamu menerima dan juga memberi. Hubungan dimana kamu merasa nyaman dan semakin bertumbuh menjadi pribadi yang lebih baik. Dalam hubungan senang, sedih dan segala situasi harus dihadapi bersama, tak jarang juga ada permasalahan yang membuat kita merasa sendiri dan ingin berpisah dari pasangan kita. Hal itu adalah hal yang wajar, karena menyatukan 2 insan yang berbeda latar belakang dan kepribadian bukanlah hal yang mudah. Apabila hubungan yang kamu jalani telah membuat kamu merasa sakit dan membuat kamu tidak menjadi dirimu sendiri, maka lebih baik kamu mempertimbangkan untuk putus karena tanpa kamu sadari kamu sudah masuk ke hubungan yang toxic. You deserve the best!"
            elif penyebab == "Teman":
                return "Kita sebagai manusia sosial, tidak bisa menghindari fakta bahwa kita membutuhkan teman dalam kehidupan kita sehari-hari. Kita membutuhkan teman untuk selalu menemani dan selalu support yang kita lakukan. Namun sayangnya kita tidak bisa langsung akrab dengan semua orang, bahkan terkadang ada beberapa sifat yang tidak kita sukai dari mereka, yang membuat adanya pertengkaran ataupun permasalahan antar teman. Ada pepatah mengatakan Persahabatan tidak perlu saling mengerti, karena sahabat akan saling menerima hal yang tak bisa dimengerti. Jadi kita harus berusaha saling mengerti dan bersikap terbuka satu sama lain."
            elif penyebab == "Kerja":
                return "Semangat buat kamu, kamu pasti capek, ngerasa sendiri, ngerasa banyak beban. Kerjaan memang penting tapi jangan lupa kesehatan kamu juga harus dijaga. Kadang hasil dari yang kita kerjakan emang gak sesuai sama ekspetasi kita, tapi yang penting kamu udah berusaha. Kamu udah lakuin yang terbaik jadi jangan kecewa sama diri sendiri ya. Enjoy prosesnya, Steve Jobs pernah berkata Satu-satunya cara untuk melakukan pekerjaan hebat yaitu dengan mencintai apa yang sedang kamu lakukan."
            
        elif perasaan == "Positif":
            if penyebab == "Nilai":
                return "Wihh, selamat yaa usaha kamu selama ini gak sia-sia. I'm so proud of you. Tapi inget jangan sampai kamu terlalu puas dengan pencapaian kamu sekarang dan jadi males untuk belajar. Persiapkan hari ini sebaik-baiknya untuk menghadapi hari esok yang baru. Goodluck! I know you can do better."
            elif penyebab == "Keluarga":
                return "Happy to hear that. Brad Henry pernah berkata ""Keluarga adalah kompas yang memandu arah kita. Ia adalah inspirasi untuk mencapai puncak, yang menghibur saat kita goyah"". Kita harus memiliki hubungan yang baik, saling support dan saling menyayangi dalam keluarga karena kemanapun kita pergi keluarga memang menjadi rumah terbaik untuk pulang. Hope you always happy and remember to go home."
            elif penyebab == "Pacar":
                return "Cie... ikut seneng deh kalau kamu akur sama pasanganmu. Kamu harus tau kalau kamu beruntung punya pasangan yang selalu support dan selalu ada buat kamu. Always happy and longlast yaa!"
            elif penyebab == "Teman":
                return "Hebat! Jaga baik-baik hubunganmu dengan teman. Salam persahabatan! Seneng kamu akur sama temen kamu, dijaga baik-baik ya hubungannya. Jangan lupa selalu saling memahami dan support satu sama lain. "
            elif penyebab == "Kerja":
                return "kamu keren banget!!! Hebatt sekali!! Semangat terus dalam bekerja. Tapi  Jangan lupa istirahat juga yaaa!"
        
        else :
            return  "Maaf\nKata yang anda inputkan tidak dapat dipahami, silahkan input ulang"
            
       

    def resetj(self):
        self.fj.destroy()
        self.journal()

    def exit(self):
        self.fm1.destroy()
        self.frame_l.destroy()
        mixer.music.stop()
        self.login()
    
    def exit1(self):
        self.ft.destroy()
        mixer.music.stop()
        self.login()

    def exit2(self):
        self.fh.destroy()
        mixer.music.stop()
        self.login()

    def exit3(self):
        self.fj.destroy()
        mixer.music.stop()
        self.login()




    
    def history(self):
        
        self.fm1.destroy()
        img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Tampilan History.png"))
        self.fh = Label(image=img)
        self.fh.image = img
        self.fh.pack(ipadx=768, ipady=432)
        self.frc = CTkScrollableFrame( self.window, orientation=VERTICAL, fg_color="white", width=350, height=480)
        self.frc.place(x=120, y=180)

        self.frc1 = CTkScrollableFrame( self.window, orientation=VERTICAL, fg_color="white", width=350, height=480)
        self.frc1.place(x=560, y=180)

        self.frc2 = CTkScrollableFrame( self.window, orientation=VERTICAL, fg_color="white", width=350, height=480)
        self.frc2.place(x=1030, y=180)

        self.fhh = Frame(bg="white")
        self.fhh.place(x=10, y=7, width= 51, height=36)
        # self.fh1 = Frame(bg="red")

        self.fh2 = Frame(bg="#07a4ff")
        self.fh2.place(x= 500, y=54, width= 500, height=50)

        self.fh21 = Frame(bg="white")
        self.fh21.place(x=150, y=120, width=300, height=70)

        self.fh22 = Frame(bg="white")
        self.fh22.place(x=600, y=120, width=300, height=70)

        self.fh33 = Frame(bg="white")
        self.fh33.place(x=1070, y=120, width=300, height=70)

        self.lbel12 = Label(self.fh21, justify=CENTER, bg="white", fg="salmon", text="Depresi", font=("Sitka Small Semibold",30, 'bold'))
        self.lbel12.place(x=70, y=-10)

        self.lbel123 = Label(self.fh22, justify=CENTER, bg="white", fg="salmon", text="Anxiety", font=("Sitka Small Semibold",30, 'bold'))
        self.lbel123.place(x=70, y=-10)

        self.lbel1234 = Label(self.fh33, justify=CENTER, bg="white", fg="salmon", text="Stress", font=("Sitka Small Semibold",30, 'bold'))
        self.lbel1234.place(x=70, y=-10)
        
        # self.fh1.place(x= 120, y=120, width= 1300, height=550)

       
        file = open("C:/Project UAS TERBARU/data_history2.txt","r")
        history_data = file.read().split("\n\n")
        file.close()
        for data2 in history_data:
            
        
            self.hry1 = Label(self.frc2,border=0,  text=data2+"\n", bg="white", justify=LEFT,  font=("Sitka Small Semibold",13, 'bold'))
            self.hry1.pack()
        


        file = open("C:/Project UAS TERBARU/data_history1.txt","r")
        history_data = file.read().split("\n\n")
        file.close()
        for data1 in history_data:
            
        
            self.hry1 = Label(self.frc1,border=0,  text=data1+"\n", bg="white", justify=LEFT,  font=("Sitka Small Semibold",13, 'bold'))
            self.hry1.pack()
        

        
        file = open("C:/Project UAS TERBARU/data_history.txt","r")
        history_data = file.read().split("\n\n")
        file.close()
        for data in history_data:
            
        
            self.hry = Label(self.frc,border=0,  text=data+"\n", bg="white", justify=LEFT, font=("Sitka Small Semibold",13, 'bold'))
            self.hry.pack()
        
        self.lbel1 = Label(self.fh2, justify=CENTER, bg="#07a4ff", fg="white", text="History", font=("Sitka Small Semibold",40, 'bold'))
        self.lbel1.place(x=150, y= -25)

        self.imgt = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Option.png"))
        self.bttnsl = Button(self.fhh, image=self.imgt, bg="#bcf4fe",border=0, fg="salmon", command=self.nextf, activebackground="#bcf4fe")
        self.bttnsl.place(x= 0, y=0)
        self.fr1 = Frame(bg="#67d4ff")
        self.fr1.place(x=-320, y =0, width=320, height= 864)
        self.imgbtest = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon Test.png"))
        self.bttnt = Button(self.fr1,  image=self.imgbtest, border=0, bg="#67d4ff",activebackground="#67d4ff", activeforeground="snow", fg="salmon",command=self.backt, font=("Sitka Small Semibold",25, 'bold'))
        self.bttnt.place(x=-80, y=150, width=400, height=85)
        self.imghstry = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon History.png"))
        self.bttnh = Button(self.fr1, image=self.imghstry,border=0, bg="snow",activebackground="snow", activeforeground="snow", fg="salmon", font=("Sitka Small Semibold",25, 'bold'))
        self.bttnh.place(x= -57, y=250, width=400, height=85)
        self.imgmn = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon Home.png"))
        self.bttnm = Button(self.fr1, image=self.imgmn, border=0, bg="#67d4ff", activebackground="#67d4ff", activeforeground="snow", fg="silver", font=("Sitka Small Semibold",25, 'bold'), command=self.backm3)
        self.bttnm.place(x= -68, y=50, width=400, height=85)
        self.imgjrnl = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon Jurnal.png"))
        self.bttnj = Button(self.fr1, image=self.imgjrnl, border=0, bg="#67d4ff", activebackground="#67d4ff", activeforeground="snow", fg="salmon", font=("Sitka Small Semibold",25, 'bold'), command=self.backj1)
        self.bttnj.place(x= -65, y=350, width=400, height=85)
        self.logout = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon Logout.png"))
        self.bttnl = Button(self.fr1, image=self.logout, border=0, bg="#67d4ff", activebackground="snow", activeforeground="snow", fg="salmon", command=self.exit2, font=("Sitka Small Semibold",25, 'bold'))
        self.bttnl.place(x= -58, y=650, width=400, height=85)
        self.imgbt= ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Slide Left.png"))
        self.btnslb= Button(self.fr1, image=self.imgbt, bg="#67d4ff", fg="black", command=self.prevf, activebackground="#67d4ff", border=0).place(x=265, y=437)
       

        self.a = -320
        
    def backm(self):
        self.ft.destroy()
        self.mainmenu()
    
    def backm1(self):
        self.fj.destroy()
        self.mainmenu()

    def backm2(self):
        self.fj.destroy()
        self.mainmenu()

    def backm3(self):
        self.fh.destroy()
        self.mainmenu()

    def backh(self):
        self.ft.destroy()
        self.history()

    def backh1(self):
        self.fj.destroy()
        self.history()

    def backt(self):
        self.fh.destroy()
        self.test()
    
    def backt1(self):
        self.fj.destroy()
        self.test()

    def backt2(self):
        project.NILAI = 0
        self.hst = self.l1['text']
        self.hst1 = self.l2['text']
        self.hasil = f"Tanggal :{datetime.datetime.now()}\n{self.hst}\n{self.hst1}\n"
        self.data_history.write(self.hasil+'\n')
        self.data_history.close()
        self.fts.destroy()
        self.test()

    def backt21(self):
        project.NILAI = 0
        self.hst = self.l1['text']
        self.hst1 = self.l2['text']
        self.hasil = f"Tanggal :{datetime.datetime.now()}\n{self.hst}\n{self.hst1}\n"
        self.data_history1.write(self.hasil+'\n')
        self.data_history1.close()
        self.fts.destroy()
        self.test()
    
    def backt22(self):
        project.NILAI = 0
        self.hst = self.l1['text']
        self.hst1 = self.l2['text']
        self.hasil = f"Tanggal :{datetime.datetime.now()}\n{self.hst}\n{self.hst1}\n"
        self.data_history2.write(self.hasil+'\n')
        self.data_history2.close()
        self.fts.destroy()
        self.test()

    def backj(self):
        self.ft.destroy()
        self.journal()
    
    def backj1(self):
        self.fh.destroy()
        self.journal()


    def test(self):  
        
        self.fm1.destroy()
        img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Tampilan Tes Mental Health.png"))
        self.ft = Label(image=img)
        self.ft.image = img
        self.ft.pack(ipadx=1200, ipady=864)
        
        self.frame_1t = Frame(bg="#473a5f")
        self.frame_1t.place(x= 82, y= 593, width=400,height=100)
        self.frame_2t = Frame(bg="#473a5f")
        self.frame_2t.place(x= 563, y= 593, width=400,height=100)
        self.frame_3t = Frame(bg="#473a5f")
        self.frame_3t.place(x= 1048, y= 593, width=400,height=100)
        self.frame_4t = Frame(bg="#c6f6ff")
        self.frame_4t.place(x= 422.5, y= 60, width=900,height=50)
        self.t1 = Label(self.frame_4t, bg="#c1f3ff", fg="black", text=f"Haii {self.l1s.get()} Yuk Test Mental Health", font=("Sitka Small Semibold",30, 'bold'))
        self.t1.place(x=15, y=0 )
        self.button = Button(self.frame_3t, text="Mulai Tes Depresi", bg="#473a5f", fg="snow", command=lambda : self.soal(self.i), border=0, activebackground="#473a5f", font=("Sitka Small Semibold",31, 'bold'), activeforeground="snow")
        self.button.place(x= -7, y=-3)
        self.button = Button(self.frame_2t, text="Mulai Tes Anxiety", bg="#473a5f", fg="snow", command=lambda : self.soal1(self.j), border=0, activebackground="#473a5f",activeforeground="snow", font=("Sitka Small Semibold",31, 'bold'))
        self.button.place(x=-8, y=-3)
        self.button = Button(self.frame_1t, text="Mulai Tes Stress", bg="#473a5f", fg="snow", command=lambda : self.soal2(self.k), border=0, activebackground="#473a5f", font=("Sitka Small Semibold",31, 'bold'), activeforeground="snow")
        self.button.place(x=0, y=-3)
       

        self.imgt = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Option.png"))
        self.fm2 = Frame(bg="#473a5f")
        self.fm2.place(x=0, y=0, width=1536, height=50)
        self.l11 = Label(self.fm2, text="Mental Health",bg="#473a5f", font=("Sitka Small Semibold",20, 'bold'), fg="white" )
        self.l11.place(x= 1150, y=1 )
        self.l112 = Label(self.fm2, text="Tracker",bg="#473a5f", font=("Sitka Small Semibold",20, 'bold'), fg="aqua" )
        self.l112.place(x= 1360, y=1 )
        self.imgic = PhotoImage(file="C:/Project UAS TERBARU/Icon.png")
        self.l1123 = Label(self.fm2, image=self.imgic, bg="#473a5f")
        self.l1123.place(x=1100, y=1)
        self.bttnsl = Button(self.fm2, image=self.imgt, bg="#473a5f",border=0, fg="salmon", command=self.nextf, activebackground="#473a5f")
        self.bttnsl.place(x= 10, y=7)
        self.fr1 = Frame(bg="#67d4ff")
        self.fr1.place(x=-320, y =0, width=320, height= 864)
        self.imgbtest = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon Test.png"))
        self.bttnt = Button(self.fr1,  image=self.imgbtest, border=0, bg="snow",activebackground="snow", activeforeground="snow", fg="salmon",font=("Sitka Small Semibold",25, 'bold'))
        self.bttnt.place(x=-80, y=150, width=400, height=85)
        self.imghstry = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon History.png"))
        self.bttnh = Button(self.fr1, image=self.imghstry,border=0, bg="#67d4ff",activebackground="#67d4ff", activeforeground="snow", fg="salmon", command=self.backh, font=("Sitka Small Semibold",25, 'bold'))
        self.bttnh.place(x= -57, y=250, width=400, height=85)
        self.imgmn = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon Home.png"))
        self.bttnm = Button(self.fr1, image=self.imgmn, border=0, bg="#67d4ff", activebackground="#67d4ff", activeforeground="snow", fg="silver", font=("Sitka Small Semibold",25, 'bold'), command=self.backm)
        self.bttnm.place(x= -68, y=50, width=400, height=85)
        self.imgjrnl = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon Jurnal.png"))
        self.bttnj = Button(self.fr1, image=self.imgjrnl, border=0, bg="#67d4ff", activebackground="#67d4ff", activeforeground="snow", fg="salmon", font=("Sitka Small Semibold",25, 'bold'), command=self.backj)
        self.bttnj.place(x= -65, y=350, width=400, height=85)
        self.logout = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Icon Logout.png"))
        self.bttnl = Button(self.fr1, image=self.logout, border=0, bg="#67d4ff", activebackground="snow", activeforeground="snow", fg="salmon", command=self.exit1, font=("Sitka Small Semibold",25, 'bold'))
        self.bttnl.place(x= -58, y=650, width=400, height=85)
        self.imgbt= ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Slide Left.png"))
        self.btnslb= Button(self.fr1, image=self.imgbt, bg="#67d4ff", fg="black", command=self.prevf, activebackground="#67d4ff", border=0).place(x=265, y=437)
       


        self.a = -320

    def soal(self, i):
        try:
            self.ft.destroy()
        except:
            pass
        if i >= len(self.soald):
            self.i = 0
            self.result()
            pass
        else:
            self.soald1 = textwrap.wrap(text=self.soald[i], width=50)
            self.w = '\n'.join(self.soald1)
            self.tst(soal=self.w)

    def soal1(self, j):
        try:
            self.ft.destroy()
        except:
            pass
        if j >= len(self.soalk):
            self.j = 0
            self.result1()
            pass
        else:
            self.soalk1 = textwrap.wrap(text=self.soalk[j], width=50)
            self.w = '\n'.join(self.soalk1)
            self.tst1(soal=self.w)

    def soal2(self, k):
        try:
            self.ft.destroy()
        except:
            pass
        if k >= len(self.soals):
            self.k = 0
            self.result2()
            pass
        else:
            self.soals1 = textwrap.wrap(text=self.soals[k], width=50)
            self.w = '\n'.join(self.soals1)
            self.tst2(soal=self.w)

    def result(self):
        self.fts.destroy()
  
        self.data_history = open("C:/Project UAS TERBARU/data_history.txt", "a")
        # self.data_history_r = open("C:/Project UAS TERBARU/data_history.txt", 'r')
        # self.data_history_text = self.data_history_r.read()

        self.fts = Frame(bg="salmon")
        self.fts.pack(ipadx=500, ipady=168, expand=True, padx=50, pady=50)
        n = project.NILAI
        if 0<=n<=9 : 
            self.fts.destroy()
            img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Hasil Tes (1).png"))
            self.fts = Label(image=img)
            self.fts.image = img
            self.fts.pack(ipadx=1200, ipady=864)
            self.imgo = PhotoImage(file= "C:/Project UAS TERBARU/Simbol Hati.png")
            self.l1p = Label(self.fts, image=self.imgo, bg="#38b6ff")
            self.l1p.place(x=640, y=100)
            self.l1 = Label(self.fts, text=f"Skor Kamu : {project.NILAI}", font=("Sitka Small Semibold",40, 'bold'), bg="#004aad", fg="snow")
            self.l1.place(x=100, y= 105 )
            self.l2 = Label(self.fts, text=f"Tingkat Depresi Normal", font=("Sitka Small Semibold",40, 'bold'), bg="#38b6ff", fg="snow")
            self.l2.place(x=760, y= 110 )
            self.wrd = "Tingkat depresi kamu normal, sebaiknya kamu meluangkan waktu untuk diri sendiri seperti      me time, self reward dll. Dan juga jangan terlalu mencemaskan hal-hal secara berlebihan"
            self.wrd1 = textwrap.wrap(text=self.wrd, width=50)
            self.wrd11 = '\n'.join(self.wrd1)
            self.l3 = Label(self.fts, justify=LEFT, text=self.wrd11, font=("Sitka Small Semibold",20, 'bold'), bg="white", fg="salmon")
            self.l3.place(x=120, y= 300 )
        elif 10<=n<=13:
            self.fts.destroy() 
            img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Hasil Tes (2).png"))
            self.fts = Label(image=img)
            self.fts.image = img
            self.fts.pack(ipadx=1200, ipady=864)
            self.imgo = PhotoImage(file= "C:/Project UAS TERBARU/Simbol Hati.png")
            self.l1p = Label(self.fts, image=self.imgo, bg="#38b6ff")
            self.l1p.place(x=640, y=100)
            self.l1 = Label(self.fts, text=f"Skor Kamu : {project.NILAI}", font=("Sitka Small Semibold",40, 'bold'), bg="#004aad", fg="snow")
            self.l1.place(x=100, y= 105 )
            self.l2 = Label(self.fts, text=f"Tingkat Depresi Ringan", font=("Sitka Small Semibold",40, 'bold'), bg="#38b6ff", fg="snow")
            self.l2.place(x=760, y= 110 )
            self.wrd = "Tingkat depresi kamu ringan sebaiknya kamu beristirahat dengan cukup, berolahraga secara teratur, relaksasi diri,melakukan hobi atau aktivitas menyenangkan, dan mengelola waktu        dengan baik"
            self.wrd1 = textwrap.wrap(text=self.wrd, width=50)
            self.wrd11 = '\n'.join(self.wrd1)
            self.l3 = Label(self.fts, justify=LEFT, text=self.wrd11, font=("Sitka Small Semibold",20, 'bold'), bg="white", fg="salmon")
            self.l3.place(x=120, y= 300 )
        elif 14<=n<=20:  
            self.fts.destroy()
            img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Hasil Tes (3).png"))
            self.fts = Label(image=img)
            self.fts.image = img
            self.fts.pack(ipadx=1200, ipady=864)
            self.imgo = PhotoImage(file= "C:/Project UAS TERBARU/Simbol Hati.png")
            self.l1p = Label(self.fts, image=self.imgo, bg="#38b6ff")
            self.l1p.place(x=640, y=100)
            self.l1 = Label(self.fts, text=f"Skor Kamu : {project.NILAI}", font=("Sitka Small Semibold",40, 'bold'), bg="#004aad", fg="snow")
            self.l1.place(x=100, y= 105 )
            self.l2 = Label(self.fts, text=f"Tingkat Depresi Sedang", font=("Sitka Small Semibold",40, 'bold'), bg="#38b6ff", fg="snow")
            self.l2.place(x=760, y= 110 )
            self.wrd = "Tingkat depresi kamu sedang sebaiknya kamu beristirahat dengan cukup, relaksasi diri, melakukan hobi atau aktivitas menyenangkan, batasi penggunaan media sosial yang dapat memicu stress dan komunikasikan pada orang yang kamu percayai"
            self.wrd1 = textwrap.wrap(text=self.wrd, width=50)
            self.wrd11 = '\n'.join(self.wrd1)
            self.l3 = Label(self.fts, justify=LEFT, text=self.wrd11, font=("Sitka Small Semibold",20, 'bold'), bg="white", fg="salmon")
            self.l3.place(x=120, y= 300 )
        elif 23<=n<=27 : 
            self.fts.destroy()
            img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Hasil Tes (4).png"))
            self.fts = Label(image=img)
            self.fts.image = img
            self.fts.pack(ipadx=1200, ipady=864)
            self.imgo = PhotoImage(file= "C:/Project UAS TERBARU/Simbol Hati.png")
            self.l1p = Label(self.fts, image=self.imgo, bg="#38b6ff")
            self.l1p.place(x=640, y=100)
            self.l1 = Label(self.fts, text=f"Skor Kamu : {project.NILAI}", font=("Sitka Small Semibold",40, 'bold'), bg="#004aad", fg="snow")
            self.l1.place(x=100, y= 105 )
            self.l2 = Label(self.fts, text=f"Tingkat Depresi Parah", font=("Sitka Small Semibold",40, 'bold'), bg="#38b6ff", fg="snow")
            self.l2.place(x=760, y= 110 )
            self.wrd = "Tingkat depresi kamu parah, sebaiknya kamu melakukan meditasi, relaksasi diri, melakukan olahraga secara teratur, bercerita pada orang terdekat, mandi dengan air hangat, liburan dan melakukan hal-hal yang dapat membuat mu bahagia"
            self.wrd1 = textwrap.wrap(text=self.wrd, width=50)
            self.wrd11 = '\n'.join(self.wrd1)
            self.l3 = Label(self.fts, justify=LEFT, text=self.wrd11, font=("Sitka Small Semibold",20, 'bold'), bg="white", fg="salmon")
            self.l3.place(x=120, y= 300 )
        else  : 
            self.fts.destroy()
            img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Hasil Tes (5).png"))
            self.fts = Label(image=img)
            self.fts.image = img
            self.fts.pack(ipadx=1200, ipady=864)
            self.imgo = PhotoImage(file= "C:/Project UAS TERBARU/Simbol Hati.png")
            self.l1p = Label(self.fts, image=self.imgo, bg="#38b6ff")
            self.l1p.place(x=640, y=100)
            self.l1 = Label(self.fts, text=f"Skor Kamu : {project.NILAI}", font=("Sitka Small Semibold",40, 'bold'), bg="#004aad", fg="snow")
            self.l1.place(x=100, y= 105 )
            self.l2 = Label(self.fts, text=f"Tingkat Depresi Sangat Parah", font=("Sitka Small Semibold",30, 'bold'), bg="#38b6ff", fg="snow")
            self.l2.place(x=760, y= 110 )
            self.wrd = "Tingkat depresi kamu sangat parah, sebaiknya hubungi dokter,psikiater atau psikolog supaya bisa mendapatkan penanganan yang tepat."
            self.wrd1 = textwrap.wrap(text=self.wrd, width=50)
            self.wrd11 = '\n'.join(self.wrd1)
            self.l3 = Label(self.fts, justify=LEFT, text=self.wrd11, font=("Sitka Small Semibold",20, 'bold'), bg="white", fg="salmon")
            self.l3.place(x=120, y= 300 )

        self.bttnbck = Button(self.fts,activebackground="white", border=0, fg="hotpink", bg="white", text="OK", command=self.backt2, font=("Sitka Small Semibold",15, 'bold'), )
        self.bttnbck.place(x= 750, y=600, width=50)


    def result1(self):
        self.fts.destroy()
        # global data_history_text
        self.data_history1 = open("C:/Project UAS TERBARU/data_history1.txt", "a")
        # self.data_history_r = open("C:/Project UAS TERBARU/data_history1.txt", 'r')
        # data_history_text = self.data_history_r.read()

        self.fts = Frame(bg="salmon")
        self.fts.pack(ipadx=500, ipady=168, expand=True, padx=50, pady=50)
        n = project.NILAI 
        if 0<=n<=9 :
            self.fts.destroy()
            img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Hasil Tes (1).png"))
            self.fts = Label(image=img)
            self.fts.image = img
            self.fts.pack(ipadx=1200, ipady=864)
            self.imgo = PhotoImage(file= "C:/Project UAS TERBARU/Simbol Hati.png")
            self.l1p = Label(self.fts, image=self.imgo, bg="#38b6ff")
            self.l1p.place(x=640, y=100)
            self.l1 = Label(self.fts, text=f"Skor Kamu : {project.NILAI}", font=("Sitka Small Semibold",40, 'bold'), bg="#004aad", fg="snow")
            self.l1.place(x=100, y= 105 )
            self.l2 = Label(self.fts, text=f"Tingkat Kecemasan Normal", font=("Sitka Small Semibold",30, 'bold'), bg="#38b6ff", fg="snow")
            self.l2.place(x=760, y= 110 )
            self.wrd = "Tingkat kecemasan kamu normal, sebaiknya kamu meluangkan waktu untuk diri sendiri seperti      me time, self reward dll. Dan juga jangan terlalu mencemaskan hal-hal secara berlebihan"
            self.wrd1 = textwrap.wrap(text=self.wrd, width=50)
            self.wrd11 = '\n'.join(self.wrd1)
            self.l3 = Label(self.fts, justify=LEFT, text=self.wrd11, font=("Sitka Small Semibold",20, 'bold'), bg="white", fg="salmon")
            self.l3.place(x=120, y= 300 )
        elif 10<=n<=13:
            self.fts.destroy()
            img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Hasil Tes (2).png"))
            self.fts = Label(image=img)
            self.fts.image = img
            self.fts.pack(ipadx=1200, ipady=864)
            self.imgo = PhotoImage(file= "C:/Project UAS TERBARU/Simbol Hati.png")
            self.l1p = Label(self.fts, image=self.imgo, bg="#38b6ff")
            self.l1p.place(x=640, y=100)
            self.l1 = Label(self.fts, text=f"Skor Kamu : {project.NILAI}", font=("Sitka Small Semibold",40, 'bold'), bg="#004aad", fg="snow")
            self.l1.place(x=100, y= 105 )
            self.l2 = Label(self.fts, text=f"Tingkat Kecemasan Ringan", font=("Sitka Small Semibold",30, 'bold'), bg="#38b6ff", fg="snow")
            self.l2.place(x=760, y= 110 )
            self.wrd = "Tingkat kecemasan kamu ringan sebaiknya kamu beristirahat dengan cukup, berolahraga secara teratur, relaksasi diri,melakukan hobi atau aktivitas menyenangkan, dan mengelola waktu        dengan baik"
            self.wrd1 = textwrap.wrap(text=self.wrd, width=50)
            self.wrd11 = '\n'.join(self.wrd1)
            self.l3 = Label(self.fts, justify=LEFT, text=self.wrd11, font=("Sitka Small Semibold",20, 'bold'), bg="white", fg="salmon")
            self.l3.place(x=120, y= 300 )
        elif 14<=n<=20:
            self.fts.destroy()
            img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Hasil Tes (3).png"))
            self.fts = Label(image=img)
            self.fts.image = img
            self.fts.pack(ipadx=1200, ipady=864)
            self.imgo = PhotoImage(file= "C:/Project UAS TERBARU/Simbol Hati.png")
            self.l1p = Label(self.fts, image=self.imgo, bg="#38b6ff")
            self.l1p.place(x=640, y=100)
            self.l1 = Label(self.fts, text=f"Skor Kamu : {project.NILAI}", font=("Sitka Small Semibold",40, 'bold'), bg="#004aad", fg="snow")
            self.l1.place(x=100, y= 105 )
            self.l2 = Label(self.fts, text=f"Tingkat Kecemasan Sedang", font=("Sitka Small Semibold",30, 'bold'), bg="#38b6ff", fg="snow")
            self.l2.place(x=760, y= 110 )
            self.wrd = "Tingkat kecemasan kamu sedang sebaiknya kamu beristirahat dengan cukup, relaksasi diri, melakukan hobi atau aktivitas menyenangkan, batasi penggunaan media sosial yang dapat memicu stress dan komunikasikan pada orang yang kamu percayai"
            self.wrd1 = textwrap.wrap(text=self.wrd, width=50)
            self.wrd11 = '\n'.join(self.wrd1)
            self.l3 = Label(self.fts, justify=LEFT, text=self.wrd11, font=("Sitka Small Semibold",20, 'bold'), bg="white", fg="salmon")
            self.l3.place(x=120, y= 300 )
        elif 23<=n<=27 :
            self.fts.destroy()
            img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Hasil Tes (4).png"))
            self.fts = Label(image=img)
            self.fts.image = img
            self.fts.pack(ipadx=1200, ipady=864)
            self.imgo = PhotoImage(file= "C:/Project UAS TERBARU/Simbol Hati.png")
            self.l1p = Label(self.fts, image=self.imgo, bg="#38b6ff")
            self.l1p.place(x=640, y=100)
            self.l1 = Label(self.fts, text=f"Skor Kamu : {project.NILAI}", font=("Sitka Small Semibold",40, 'bold'), bg="#004aad", fg="snow")
            self.l1.place(x=100, y= 105 )
            self.l2 = Label(self.fts, text=f"Tingkat Kecemasan Parah", font=("Sitka Small Semibold",30, 'bold'), bg="#38b6ff", fg="snow")
            self.l2.place(x=760, y= 110 )
            self.wrd = "Tingkat kecemasan kamu parah, sebaiknya kamu melakukan meditasi, relaksasi diri, melakukan olahraga secara teratur, bercerita pada orang terdekat, mandi dengan air hangat, liburan dan melakukan hal-hal yang dapat membuat mu bahagia"
            self.wrd1 = textwrap.wrap(text=self.wrd, width=50)
            self.wrd11 = '\n'.join(self.wrd1)
            self.l3 = Label(self.fts, justify=LEFT, text=self.wrd11, font=("Sitka Small Semibold",20, 'bold'), bg="white", fg="salmon")
            self.l3.place(x=120, y= 300 )
        else  :
            self.fts.destroy()
            img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Hasil Tes (5).png"))
            self.fts = Label(image=img)
            self.fts.image = img
            self.fts.pack(ipadx=1200, ipady=864)
            self.imgo = PhotoImage(file= "C:/Project UAS TERBARU/Simbol Hati.png")
            self.l1p = Label(self.fts, image=self.imgo, bg="#38b6ff")
            self.l1p.place(x=640, y=100)
            self.l1 = Label(self.fts, text=f"Skor Kamu : {project.NILAI}", font=("Sitka Small Semibold",40, 'bold'), bg="#004aad", fg="snow")
            self.l1.place(x=100, y= 105 )
            self.l2 = Label(self.fts, text=f"Tingkat kecemasan Sangat Parah", font=("Sitka Small Semibold",30, 'bold'), bg="#38b6ff", fg="snow")
            self.l2.place(x=750, y= 110 )
            self.wrd = "Tingkat kecemasan kamu sangat parah, sebaiknya hubungi dokter,psikiater atau psikolog supaya bisa mendapatkan penanganan yang tepat."
            self.wrd1 = textwrap.wrap(text=self.wrd, width=50)
            self.wrd11 = '\n'.join(self.wrd1)
            self.l3 = Label(self.fts, justify=LEFT, text=self.wrd11, font=("Sitka Small Semibold",20, 'bold'), bg="white", fg="salmon")
            self.l3.place(x=120, y= 300 )

        self.bttnbck = Button(self.fts,activebackground="white", border=0, fg="hotpink", bg="white", text="OK", command=self.backt21, font=("Sitka Small Semibold",15, 'bold'), )
        self.bttnbck.place(x= 750, y=600, width=50)

    def result2(self):
        self.fts.destroy()
        # global data_history_text
        self.data_history2 = open("C:/Project UAS TERBARU/data_history2.txt", "a")
        # self.data_history_r = open("C:/Project UAS TERBARU/data_history2.txt", 'r')
        # data_history_text = self.data_history_r.read()

        self.fts = Frame(bg="salmon")
        self.fts.pack(ipadx=500, ipady=168, expand=True, padx=50, pady=50)
        n = project.NILAI 
        if 0<=n<=9 :
            self.fts.destroy()
            img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Hasil Tes (1).png"))
            self.fts = Label(image=img)
            self.fts.image = img
            self.fts.pack(ipadx=1200, ipady=864)
            self.imgo = PhotoImage(file= "C:/Project UAS TERBARU/Simbol Hati.png")
            self.l1p = Label(self.fts, image=self.imgo, bg="#38b6ff")
            self.l1p.place(x=640, y=100)
            self.l1 = Label(self.fts, text=f"Skor Kamu : {project.NILAI}", font=("Sitka Small Semibold",40, 'bold'), bg="#004aad", fg="snow")
            self.l1.place(x=100, y= 105 )
            self.l2 = Label(self.fts, text=f"Tingkat Stress Normal", font=("Sitka Small Semibold",40, 'bold'), bg="#38b6ff", fg="snow")
            self.l2.place(x=760, y= 110 )
            self.wrd = "Tingkat stress kamu normal, sebaiknya kamu meluangkan waktu untuk diri sendiri seperti      me time, self reward dll. Dan juga jangan terlalu mencemaskan hal-hal secara berlebihan"
            self.wrd1 = textwrap.wrap(text=self.wrd, width=50)
            self.wrd11 = '\n'.join(self.wrd1)
            self.l3 = Label(self.fts, justify=LEFT, text=self.wrd11, font=("Sitka Small Semibold",20, 'bold'), bg="white", fg="salmon")
            self.l3.place(x=120, y= 300 )
        elif 10<=n<=13:
            self.fts.destroy()
            img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Hasil Tes (2).png"))
            self.fts = Label(image=img)
            self.fts.image = img
            self.fts.pack(ipadx=1200, ipady=864)
            self.imgo = PhotoImage(file= "C:/Project UAS TERBARU/Simbol Hati.png")
            self.l1p = Label(self.fts, image=self.imgo, bg="#38b6ff")
            self.l1p.place(x=640, y=100)
            self.l1 = Label(self.fts, text=f"Skor Kamu : {project.NILAI}", font=("Sitka Small Semibold",40, 'bold'), bg="#004aad", fg="snow")
            self.l1.place(x=100, y= 105 )
            self.l2 = Label(self.fts, text=f"Tingkat Stress Ringan", font=("Sitka Small Semibold",40, 'bold'), bg="#38b6ff", fg="snow")
            self.l2.place(x=760, y= 110 )
            self.wrd = "Tingkat Stress kamu ringan sebaiknya kamu beristirahat dengan cukup, berolahraga secara teratur, relaksasi diri,melakukan hobi atau aktivitas menyenangkan, dan mengelola waktu        dengan baik"
            self.wrd1 = textwrap.wrap(text=self.wrd, width=50)
            self.wrd11 = '\n'.join(self.wrd1)
            self.l3 = Label(self.fts, justify=LEFT, text=self.wrd11, font=("Sitka Small Semibold",20, 'bold'), bg="white", fg="salmon")
            self.l3.place(x=120, y= 300 )
        elif 14<=n<=20:
            self.fts.destroy()
            img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Hasil Tes (3).png"))
            self.fts = Label(image=img)
            self.fts.image = img
            self.fts.pack(ipadx=1200, ipady=864)
            self.imgo = PhotoImage(file= "C:/Project UAS TERBARU/Simbol Hati.png")
            self.l1p = Label(self.fts, image=self.imgo, bg="#38b6ff")
            self.l1p.place(x=640, y=100)
            self.l1 = Label(self.fts, text=f"Skor Kamu : {project.NILAI}", font=("Sitka Small Semibold",40, 'bold'), bg="#004aad", fg="snow")
            self.l1.place(x=100, y= 105 )
            self.l2 = Label(self.fts, text=f"Tingkat Stress Sedang", font=("Sitka Small Semibold",40, 'bold'), bg="#38b6ff", fg="snow")
            self.l2.place(x=760, y= 110 )
            self.wrd = "Tingkat stress kamu sedang sebaiknya kamu beristirahat dengan cukup, relaksasi diri, melakukan hobi atau aktivitas menyenangkan, batasi penggunaan media sosial yang dapat memicu stress dan komunikasikan pada orang yang kamu percayai"
            self.wrd1 = textwrap.wrap(text=self.wrd, width=50)
            self.wrd11 = '\n'.join(self.wrd1)
            self.l3 = Label(self.fts, justify=LEFT, text=self.wrd11, font=("Sitka Small Semibold",20, 'bold'), bg="white", fg="salmon")
            self.l3.place(x=120, y= 300 )
        elif 23<=n<=27 :
            self.fts.destroy()
            img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Hasil Tes (4).png"))
            self.fts = Label(image=img)
            self.fts.image = img
            self.fts.pack(ipadx=1200, ipady=864)
            self.imgo = PhotoImage(file= "C:/Project UAS TERBARU/Simbol Hati.png")
            self.l1p = Label(self.fts, image=self.imgo, bg="#38b6ff")
            self.l1p.place(x=640, y=100)
            self.l1 = Label(self.fts, text=f"Skor Kamu : {project.NILAI}", font=("Sitka Small Semibold",40, 'bold'), bg="#004aad", fg="snow")
            self.l1.place(x=100, y= 105 )
            self.l2 = Label(self.fts, text=f"Tingkat Stress Parah", font=("Sitka Small Semibold",40, 'bold'), bg="#38b6ff", fg="snow")
            self.l2.place(x=760, y= 110 )
            self.wrd = "Tingkat Stress kamu parah, sebaiknya kamu melakukan meditasi, relaksasi diri, melakukan olahraga secara teratur, bercerita pada orang terdekat, mandi dengan air hangat, liburan dan melakukan hal-hal yang dapat membuat mu bahagia"
            self.wrd1 = textwrap.wrap(text=self.wrd, width=50)
            self.wrd11 = '\n'.join(self.wrd1)
            self.l3 = Label(self.fts, justify=LEFT, text=self.wrd11, font=("Sitka Small Semibold",20, 'bold'), bg="white", fg="salmon")
            self.l3.place(x=120, y= 300 )
        else  :
            self.fts.destroy()
            img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Hasil Tes (5).png"))
            self.fts = Label(image=img)
            self.fts.image = img
            self.fts.pack(ipadx=1200, ipady=864)
            self.imgo = PhotoImage(file= "C:/Project UAS TERBARU/Simbol Hati.png")
            self.l1p = Label(self.fts, image=self.imgo, bg="#38b6ff")
            self.l1p.place(x=640, y=100)
            self.l1 = Label(self.fts, text=f"Skor Kamu : {project.NILAI}", font=("Sitka Small Semibold",40, 'bold'), bg="#004aad", fg="snow")
            self.l1.place(x=100, y= 105 )
            self.l2 = Label(self.fts, text=f"Tingkat Stress Sangat Parah", font=("Sitka Small Semibold",30, 'bold'), bg="#38b6ff", fg="snow")
            self.l2.place(x=760, y= 110 )
            self.wrd = "Tingkat stress kamu sangat parah, sebaiknya hubungi dokter,psikiater atau psikolog supaya bisa mendapatkan penanganan yang tepat."
            self.wrd1 = textwrap.wrap(text=self.wrd, width=50)
            self.wrd11 = '\n'.join(self.wrd1)
            self.l3 = Label(self.fts, justify=LEFT, text=self.wrd11, font=("Sitka Small Semibold",20, 'bold'), bg="white", fg="salmon")
            self.l3.place(x=120, y= 300 )

        self.bttnbck = Button(self.fts,activebackground="white", border=0, fg="hotpink", bg="white", text="OK", command=self.backt22, font=("Sitka Small Semibold",15, 'bold'), )
        self.bttnbck.place(x= 750, y=600, width=50)



    def tst(self,soal):
        img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Tampilan Soal Test.png"))
        self.fts = Label(image=img)
        self.fts.image = img
        self.fts.pack(ipadx=1200, ipady=864)
        self.imgo = PhotoImage(file="C:/Project UAS TERBARU/Gambar Soal Tes.png")
        self.l1123 = Label(self.fts, image=self.imgo, bg="#c1f3ff")
        self.l1123.place(x=675, y=678)
        self.nilai = IntVar()
        self.nilai.set(0)
        self.lts1 = Label(self.fts, justify=LEFT, text=soal, bg="#c1f3ff",fg="#473a5f", font=("Sitka Small Semibold",30, 'bold'))
        self.lts1.place(x=165, y= 270)
        self.rt = Radiobutton(self.fts, text="Tidak ada atau tidak pernah", bg="#38b6ff",fg="snow", font=("Sitka Small Semibold",25, 'bold'), variable=self.nilai, value=0, command=self.results, relief=FLAT, activebackground="#38b6ff", activeforeground="snow")
        self.rt.place(x=165, y= 430, width=570)
        self.rt1 = Radiobutton(self.fts, text="Kadang-Kadang", bg="#38b6ff",fg="snow", font=("Sitka Small Semibold",25, 'bold'), variable=self.nilai, value=1, command=self.results, relief=FLAT, activebackground="#38b6ff", activeforeground="snow")
        self.rt1.place(x=800, y= 430 , width=570)
        self.rt2 = Radiobutton(self.fts, text="Sering", bg="#38b6ff",fg="snow", font=("Sitka Small Semibold",25, 'bold'), variable=self.nilai, value=2, command=self.results, relief=FLAT, activebackground="#38b6ff", activeforeground="snow")
        self.rt2.place(x=165, y= 580 , width=570)
        self.rt3 = Radiobutton(self.fts, text="Hampir Setiap Saat", bg="#38b6ff",fg="snow", font=("Sitka Small Semibold",25, 'bold'), variable=self.nilai, value=3, command=self.results, relief=FLAT, activebackground="#38b6ff", activeforeground="snow")
        self.rt3.place(x=800, y= 580, width=570)

    def tst1(self,soal):
        img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Tampilan Soal Test.png"))
        self.fts = Label(image=img)
        self.fts.image = img
        self.fts.pack(ipadx=1200, ipady=864)
        self.imgo = PhotoImage(file="C:/Project UAS TERBARU/Gambar Soal Tes.png")
        self.l1123 = Label(self.fts, image=self.imgo, bg="#c1f3ff")
        self.l1123.place(x=675, y=678)
        self.nilai = IntVar()
        self.nilai.set(0)
        self.lts1 = Label(self.fts, justify=LEFT, text=soal, bg="#c1f3ff",fg="#473a5f", font=("Sitka Small Semibold",30, 'bold'))
        self.lts1.place(x=165, y= 270)
        self.rt = Radiobutton(self.fts, text="Tidak ada atau tidak pernah", bg="#38b6ff",fg="snow", font=("Sitka Small Semibold",25, 'bold'), variable=self.nilai, value=0, command=self.results1, relief=FLAT, activebackground="#38b6ff", activeforeground="snow")
        self.rt.place(x=165, y= 430, width=570 )
        self.rt1 = Radiobutton(self.fts, text="Kadang-Kadang", bg="#38b6ff",fg="snow", font=("Sitka Small Semibold",25, 'bold'), variable=self.nilai, value=1, command=self.results1, relief=FLAT, activebackground="#38b6ff", activeforeground="snow")
        self.rt1.place(x=800, y= 430, width=570 )
        self.rt2 = Radiobutton(self.fts, text="Sering", bg="#38b6ff",fg="snow", font=("Sitka Small Semibold",25, 'bold'), variable=self.nilai, value=2, command=self.results1, relief=FLAT, activebackground="#38b6ff", activeforeground="snow")
        self.rt2.place(x=165, y= 580, width=570 )
        self.rt3 = Radiobutton(self.fts, text="Hampir Setiap Saat", bg="#38b6ff",fg="snow", font=("Sitka Small Semibold",25, 'bold'), variable=self.nilai, value=3, command=self.results1, relief=FLAT, activebackground="#38b6ff", activeforeground="snow")
        self.rt3.place(x=800, y= 580, width=570)

    def tst2(self,soal):
        img = ImageTk.PhotoImage(Image.open("C:/Project UAS TERBARU/Tampilan Soal Test.png"))
        self.fts = Label(image=img)
        self.fts.image = img
        self.fts.pack(ipadx=1200, ipady=864)
        self.imgo = PhotoImage(file="C:/Project UAS TERBARU/Gambar Soal Tes.png")
        self.l1123 = Label(self.fts, image=self.imgo, bg="#c1f3ff")
        self.l1123.place(x=675, y=678)
        self.nilai = IntVar()
        self.nilai.set(0)
        self.lts1 = Label(self.fts, justify=LEFT, text=soal, bg="#c1f3ff",fg="#473a5f", font=("Sitka Small Semibold",30, 'bold'))
        self.lts1.place(x=165, y= 270)
        self.rt = Radiobutton(self.fts, text="Tidak ada atau tidak pernah", bg="#38b6ff",fg="snow", font=("Sitka Small Semibold",25, 'bold'), variable=self.nilai, value=0, command=self.results2, relief=FLAT, activebackground="#38b6ff", activeforeground="snow")
        self.rt.place(x=165, y= 430, width=570)
        self.rt1 = Radiobutton(self.fts, text="Kadang-Kadang", bg="#38b6ff",fg="snow", font=("Sitka Small Semibold",25, 'bold'), variable=self.nilai, value=1, command=self.results2, relief=FLAT, activebackground="#38b6ff", activeforeground="snow")
        self.rt1.place(x=800, y= 430, width=570)
        self.rt2 = Radiobutton(self.fts, text="Sering", bg="#38b6ff",fg="snow", font=("Sitka Small Semibold",25, 'bold'), variable=self.nilai, value=2, command=self.results2, relief=FLAT, activebackground="#38b6ff", activeforeground="snow")
        self.rt2.place(x=165, y= 580,width=570)
        self.rt3 = Radiobutton(self.fts, justify=LEFT, text="Hampir Setiap Saat", bg="#38b6ff",fg="snow", font=("Sitka Small Semibold",25, 'bold'), variable=self.nilai, value=3, command=self.results2, relief=FLAT, activebackground="#38b6ff", activeforeground="snow")
        self.rt3.place(x=800, y= 580, width=570)

    
    def results(self):
        try:
            self.fts.destroy()
        except:
            pass

        project.NILAI += self.nilai.get()
        self.i += 1
        self.soal(self.i)

    def results1(self):
        try:
            self.fts.destroy()
        except:
            pass

        project.NILAI += self.nilai.get()
        self.j += 1
        self.soal1(self.j)

    def results2(self):
        try:
            self.fts.destroy()
        except:
            pass

        project.NILAI += self.nilai.get()
        self.k += 1
        self.soal2(self.k)
        



    
       
       
       

window = Tk()

print(window.winfo_screenwidth())
print(window.winfo_screenheight())
project(window)
window.mainloop()