#import files for the project.---------------------------------------------------------------------------------------------
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter.font import Font
from PIL import Image as Im
from PIL import ImageTk
import Pmw
from tkinter import filedialog,simpledialog
import tkinter.messagebox
import shutil,os,pickle
import MySQLdb
from reportlab.pdfgen import canvas
from reportlab.platypus import Table,SimpleDocTemplate,TableStyle,Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
from PyPDF2 import PdfFileMerger
from datetime import datetime,date
#--------------------------------------------------------------------------------------------------------------------------
filex1=" "
filex2=" "
filex3=" "
filex4=" "
filex5=" "
filex6=" "
filex7=" "
filex8=" "
filex9=" "
filex10=" "
filex11=" "
filex12=" "
filename1="No Doc. Uploaded"
filename2="No Doc. Uploaded"
filename3="No Doc. Uploaded"
filename4="No Doc. Uploaded"
filename5="No Doc. Uploaded"
filename6="No Doc. Uploaded"
filename7="No Doc. Uploaded"
filename8="No Doc. Uploaded"
filename9="No Doc. Uploaded"
filename10="No Doc. Uploaded"
filename11="No Doc. Uploaded"
filename12="No Doc. Uploaded"
fullpath=" "
foldername="empinfo"
mycursor=" "
mydb=" "
folname=" "
loginus=" "
loginpa=" "


def signup():
    global ue
    global pe
    global name
    global foldername
    global fullpath
    global dname

    def create_folder():
        global name
        global foldername
        global fullpath
        name = filedialog.askdirectory()
        fullpath = str(name) + '/' + str(foldername)
        root1.deiconify()
        try:
            os.mkdir(fullpath)
        except OSError:
            tkinter.messagebox.showinfo('Folder Creation Error!!!!!!!!', 'Folder already exist.')
            root1.deiconify()

    def create_database():
        a = os.path.isfile(foldername + ".pickle")
        if a != True:
            global dname
            dname = simpledialog.askstring("Input", "Name of Your Database?")
            root1.deiconify()
            dictlog = {}
            dictlog[logusere.get()] = logpasse.get()
            arr = [ue.get(), pe.get(), dname, fullpath, he.get(), int(porte.get()), dictlog]
            pickle_out = open(str(foldername) + ".pickle", "wb")
            pickle.dump(arr, pickle_out)

            mydb = MySQLdb.connect(
                host=he.get(),
                port=int(porte.get()),
                user=ue.get(),
                password=pe.get()
            )
            try:
                mycursor = mydb.cursor()
                mycursor.execute("CREATE DATABASE " + str(dname))
                mycursor.execute("USE " + str(dname))
                mycursor.execute(
                    "CREATE TABLE TABLE1(EMPCODE varchar(20) unique primary key,FNAME varchar(50) not null,MNAME varchar(50) ,LNAME varchar(50),DOB date not null,RELIGION varchar(20),GENDER varchar(10),CASTE varchar(20),BLOODGROUP varchar(5),PREADDRESS varchar(200),PRECITY varchar(50),PRESTATE varchar(50),PREPIN numeric(10),PERADDRESS varchar(200),PERCITY varchar(50),PERSTATE varchar(50),PERPIN numeric(10),MOBILENO numeric(15) not null,ALTMOBILENO numeric(15),EMAIL varchar(70),PHOTOFILE varchar(50) not null,SIGNATUREFILE varchar(50) not null)")
                mycursor.execute(
                    "CREATE TABLE TABLE2(EMPCODE varchar(20),DEGREEOBT varchar(50) not null,DESCR varchar(50),UNIVER_BOARD varchar(70) not null,INSTITUTION varchar(100),YEAROFPASS date not null,MARKSINPERCENT decimal(5,2),REMARKS varchar(50),ACADEMICFILE varchar(50),primary key(EMPCODE,DEGREEOBT),foreign key(EMPCODE) references TABLE1(EMPCODE))")
                mycursor.execute(
                    "CREATE TABLE TABLE3(EMPCODE varchar(20),EXPTYPE varchar(50) not null,INST_COMP varchar(100) not null,ADDRESS varchar(200),DESIGNATION varchar(50),DATEOFJOIN date not null,DATEOFRELEASE date not null,SALARY numeric(10),REMARKS varchar(50),EXPERIENCEFILE varchar(50),foreign key(EMPCODE) references TABLE1(EMPCODE))")
                mycursor.execute(
                    "CREATE TABLE TABLE4(EMPCODE varchar(20),SLNO int auto_increment not null unique , SPECIALACV varchar(200) not null,SPECIALFILE varchar(50),foreign key(EMPCODE) references TABLE1(EMPCODE))")
                mycursor.execute(
                    "CREATE TABLE TABLE5(EMPCODE varchar(20),YOL numeric(10) not null,CL decimal(5,2),ML decimal(5,2),EL decimal(5,2),SL decimal(5,2),OD decimal(5,2),OTHER decimal(5,2),LEAVEFILE varchar(50),primary key(EMPCODE,YOL),foreign key(EMPCODE) references TABLE1(EMPCODE))")
                mycursor.execute(
                    "CREATE TABLE TABLE6(EMPCODE varchar(20),DORP date not null,DESCR varchar(100),REWARDFILE varchar(50),foreign key(EMPCODE) references TABLE1(EMPCODE))")
                mycursor.execute(
                    "CREATE TABLE TABLE7(EMPCODE varchar(20),DOPAY date not null,BASIC decimal(10,2) not null,DA decimal(10,2),HRA decimal(10,2),OTHER decimal(10,2),PAYSCALEFILE varchar(50),foreign key(EMPCODE) references TABLE1(EMPCODE))")
                mycursor.execute(
                    "CREATE TABLE TABLE8(EMPCODE varchar(20),SEM varchar(10) not null,PAPERCODE varchar(20),PAPERNAME varchar(70) not null,DEPARTMENT varchar(70) not null,YOA numeric(10) not null,SUBJECTALLOTFILE varchar(50),foreign key(EMPCODE) references TABLE1(EMPCODE))")
                mycursor.execute(
                    "CREATE TABLE TABLE9(EMPCODE varchar(20),FROMDATE date not null,TODATE date,DESCR varchar(200),ADDRESPFILE varchar(50),foreign key(EMPCODE) references TABLE1(EMPCODE))")
                mycursor.execute(
                    "CREATE TABLE TABLE10(EMPCODE varchar(20),DOCNAME varchar(20) not null,DOCIDNO varchar(20) not null,LEGALFILE varchar(50),foreign key(EMPCODE) references TABLE1(EMPCODE))")
                mycursor.execute(
                    "CREATE TABLE TABLE11(EMPCODE varchar(20),ACCOUNTNO varchar(50) not null,BANKNAME varchar(70) not null,BRANCHCODE varchar(20),IFSCCODE varchar(20),BANKFILE varchar(50),foreign key(EMPCODE) references TABLE1(EMPCODE))")
                mycursor.execute(
                    "CREATE TABLE TABLE12(EMPCODE varchar(20),COURSETYPE varchar(50) not null,DEPARTMENT varchar(70) not null,DESIGNATION varchar(70) not null,SUBSPECILIZE varchar(80) not null,DOJ date not null,JOININGFILE varchar(50),foreign key(EMPCODE) references TABLE1(EMPCODE))")
                mydb.commit()
                root1.destroy()
                tkinter.messagebox.showinfo('Confirmation!!', 'Database Created Successfully')
            except MySQLdb.DatabaseError:
                a = tkinter.messagebox.askyesno('Database creation error!!!', 'Database already exists. Use it???')
                if a == 1:
                    mycursor.execute("USE " + str(dname))
                    root1.destroy()
                    tkinter.messagebox.showinfo('Confirmation!!', 'Admin Setup Successful!!!')
                else:
                    pass

        else:
            tkinter.messagebox.showinfo('Security Prohibition',
                                        'Report to Administrator, User Donot have Permission!!!!')
            root1.destroy()

    root1 = Tk()
    root1.geometry("400x400")
    root1.title("ADMIN SETUP")
    root1.iconbitmap(r'diatmlogo.ico')
    h = Label(root1, text="Host/IP:")
    port = Label(root1, text="Port no.:")
    u = Label(root1, text="Database Username:")
    p = Label(root1, text="Database Password:")
    h.grid(row=0, column=0, padx=10, pady=10)
    port.grid(row=1, column=0, padx=10, pady=10)
    u.grid(row=2, column=0, padx=10, pady=10)
    p.grid(row=3, column=0, padx=10, pady=10)
    he = Entry(root1)
    he.grid(row=0, column=1, padx=10, pady=10)
    porte = Entry(root1)
    porte.grid(row=1, column=1, padx=10, pady=10)
    ue = Entry(root1)
    ue.grid(row=2, column=1, padx=10, pady=10)
    pe = Entry(root1, show="*")
    pe.grid(row=3, column=1, padx=10, pady=10)
    loguser = Label(root1, text="Login Username:")
    loguser.grid(row=4, column=0, padx=10, pady=10)
    logpass = Label(root1, text="Login Password")
    logpass.grid(row=5, column=0, padx=10, pady=10)
    logusere = Entry(root1)
    logusere.grid(row=4, column=1, padx=10, pady=10)
    logusere.insert(0, "admin")
    logusere.config(state="readonly")
    logpasse = Entry(root1, show="*")
    logpasse.grid(row=5, column=1, padx=10, pady=10)
    b1 = Button(root1, text="Create Folder", command=create_folder).grid(row=6, column=1, padx=10, pady=10)
    b2 = Button(root1, text="Create Database", command=create_database).grid(row=7, column=1, padx=10, pady=10)
    root1.mainloop()

def login_cred():
    global mycursor
    global mydb
    global username
    global password
    global databname
    global folname
    global hostname
    global loginpa
    global loginus
    try:
        pickle_in = open(str(foldername)+".pickle", "rb")
        data = pickle.load(pickle_in)
        username=data[0]
        password=data[1]
        databname= data[2]
        folname=data[3]
        hostname=data[4]
        portno=data[5]
        x=data[6]
        if use.get() in x:
            loginus=use.get()
            loginpa=x[loginus]
        else:
            loginus=" "
            loginpa=" "


        if use.get()==loginus and pae.get()==loginpa:
            try:
                mydb = MySQLdb.connect(
                    host=hostname,
                    port=portno,
                    user=username,
                    password=password,
                    database=databname
                )
                mycursor = mydb.cursor()
                tkinter.messagebox.showinfo('Welcome!','Hi! Friend you are logged in Continue working........')
                root2.destroy()
                # All the working functions.
                sig = 0
                title = " "

                def photo():
                    try:
                        global filename1
                        global filex1
                        file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"),))
                        filex1 = file1.name
                        f, ext = os.path.splitext(filex1)
                        if os.path.getsize(filex1) <= 55000:
                            del file1
                            a = E00.get() + '_photo'
                            filename1 = a + ext
                            EE3.delete(0, END)
                            EE3.insert(1, "Successful")
                        else:
                            tkinter.messagebox.showinfo('Uploading Error!!', 'Your Uploading Image must be below 50KB')
                            EE3.delete(0, END)
                            EE3.insert(0, "Failed")
                    except AttributeError:
                        tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')

                def sign():
                    try:
                        global filename2
                        global filex2
                        file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"),))
                        filex2 = file1.name
                        f, ext = os.path.splitext(filex2)
                        if os.path.getsize(filex2) <= 55000:
                            del file1
                            a = E00.get() + '_sign'
                            filename2 = a + ext
                            EE2.delete(0, END)
                            EE2.insert(0, "Successful")
                        else:
                            tkinter.messagebox.showinfo('Uploading Error!!', 'Your Uploading Image must be below 50KB')
                            EE2.delete(0, END)
                            EE2.insert(0, "Failed")
                    except AttributeError:
                        tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')

                def submit1():
                    global filename1
                    global filename2
                    if loginus == E00.get() or loginus == "admin":
                        try:
                            a = E4.get().split('-')
                            b = ''
                            b = a[-1] + '-' + a[-2] + '-' + a[-3]
                            c = " "
                            if gender.get() == 1:
                                c = "Male"
                            elif gender.get() == 2:
                                c = "Female"
                            else:
                                pass
                            d = ''
                            d = E6.get() + "," + E7.get() + "," + E8.get() + "," + E10.get()
                            if sig == 0:
                                pass
                                mycursor.execute(
                                    "INSERT INTO TABLE1(EMPCODE,FNAME,MNAME,LNAME,DOB,RELIGION,GENDER,CASTE,BLOODGROUP,PREADDRESS,PRECITY,PRESTATE,PREPIN,PERADDRESS,PERCITY,PERSTATE,PERPIN,MOBILENO,ALTMOBILENO,EMAIL,PHOTOFILE,SIGNATUREFILE) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                    (E00.get(), E1.get(), E2.get(), E3.get(), b, religion.get(), c, caste.get(), EE1.get(), d,
                                     E9.get(), state1.get(), int(E12.get()), d, E9.get(), state1.get(), int(E12.get()),
                                     int(E20.get()), int(E21.get()), EE4.get(), filename1, filename2,))
                                mydb.commit()
                                shutil.copy(filex1, folname + '/' + filename1)
                                shutil.copy(filex2, folname + '/' + filename2)
                                filename1 = "No Doc. Uploaded"
                                filename2 = "No Doc. Uploaded"
                                tkinter.messagebox.showinfo('Confirmation!!', 'Response Successfully Submitted!!')
                            elif sig == 1:
                                e = ''
                                e = E13.get() + "," + E14.get() + "," + E15.get() + "," + E17.get()
                                mycursor.execute(
                                    "INSERT INTO TABLE1(EMPCODE,FNAME,MNAME,LNAME,DOB,RELIGION,GENDER,CASTE,BLOODGROUP,PREADDRESS,PRECITY,PRESTATE,PREPIN,PERADDRESS,PERCITY,PERSTATE,PERPIN,MOBILENO,ALTMOBILENO,EMAIL,PHOTOFILE,SIGNATUREFILE) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                    (E00.get(), E1.get(), E2.get(), E3.get(), b, religion.get(), c, caste.get(), EE1.get(), d,
                                     E9.get(), state1.get(), int(E12.get()), e, E16.get(), state2.get(), int(E19.get()),
                                     int(E20.get()), int(E21.get()), EE4.get(), filename1, filename2,))
                                mydb.commit()
                                shutil.copy(filex1, folname + '/' + filename1)
                                shutil.copy(filex2, folname + '/' + filename2)
                                filename1 = "No Doc. Uploaded"
                                filename2 = "No Doc. Uploaded"
                                tkinter.messagebox.showinfo('Confirmation!!', 'Response Successfully Submitted!!')
                            else:
                                pass
                                tkinter.messagebox.showinfo('Error !!', 'Something went Wrong!!')
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Submitted without documents upload!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')

                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def submit10():
                    global filename11
                    if loginus == E00.get() or loginus == "admin":
                        try:
                            mycursor.execute(
                                "INSERT INTO TABLE10(EMPCODE,DOCNAME,DOCIDNO,LEGALFILE) VALUES (%s,%s,%s,%s)",
                                (E00.get(), docname.get(), str(EE5.get()), filename11))
                            mydb.commit()
                            text9.insert(2.0, "\n")
                            text9.insert(2.0, docname.get() + '|' + str(EE5.get()))
                            shutil.copy(filex11, folname + '/' + filename11)
                            filename11 = "No Doc. Uploaded"
                            tkinter.messagebox.showinfo('Confirmation!!', 'Response Successfully Submitted!!')

                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Submitted without Document upload / Insufficient data.!!')
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def legal_upload():
                    try:
                        global filename11
                        global filex11
                        file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                        filex11 = file1.name
                        f, ext = os.path.splitext(filex11)
                        if os.path.getsize(filex11) <= 55000:
                            del file1
                            a = E00.get() + '_' + docname.get()
                            filename11 = a + ext
                            tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')

                        else:
                            tkinter.messagebox.showinfo('Uploading Error!!', 'Your Uploading Image must be below 50KB')
                    except AttributeError:
                        tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')

                def addmore10():
                    docname.set('')
                    EE5.delete(0, END)

                def submit2():
                    global filename3
                    if loginus == E00.get() or loginus == "admin":
                        try:
                            aa = E25.get().split('-')
                            bb = ''
                            bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                            mycursor.execute(
                                "INSERT INTO TABLE2(EMPCODE,DEGREEOBT,DESCR,UNIVER_BOARD,INSTITUTION,YEAROFPASS,MARKSINPERCENT,REMARKS,ACADEMICFILE) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (
                                E00.get(), degree.get(), E22.get(), E23.get(), E24.get(), bb, int(E26.get()), E27.get(),
                                filename3))
                            mydb.commit()
                            text1.insert(2.0, '\n')
                            text1.insert(2.0,
                                         degree.get() + '|' + E22.get() + '|' + E23.get() + '|' + E24.get() + '|' + E25.get() + '|' + E26.get() + '|' + E27.get())
                            shutil.copy(filex3, folname + '/' + filename3)
                            filename3 = "No Doc. Uploaded"
                            tkinter.messagebox.showinfo('Confirmation!!', 'Response Successfully Submitted!!')
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Submitted without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def Academic_upload():
                    try:
                        global filename3
                        global filex3
                        file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                        filex3 = file1.name
                        f, ext = os.path.splitext(filex3)
                        if os.path.getsize(filex3) <= 55000:
                            del file1
                            a = E00.get() + '_' + degree.get() + '_' + E22.get()
                            filename3 = a + ext
                            tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')

                        else:
                            tkinter.messagebox.showinfo('Uploading Error!!', 'Your Uploading Image must be below 50KB')
                    except AttributeError:
                        tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')

                def addmore2():
                    E22.delete(0, END)
                    E23.delete(0, END)
                    E24.delete(0, END)
                    E25.delete(0, END)
                    E25.insert(0, 'DD-MM-YYYY')
                    E26.delete(0, END)
                    E27.delete(0, END)

                def submit3():
                    global filename4
                    if loginus == E00.get() or loginus == "admin":
                        try:
                            aaa = E32.get().split('-')
                            bbb = ''
                            bbb = aaa[-1] + '-' + aaa[-2] + '-' + aaa[-3]
                            aaaa = E33.get().split('-')
                            bbbb = ''
                            bbbb = aaaa[-1] + '-' + aaaa[-2] + '-' + aaaa[-3]
                            mycursor.execute(
                                "INSERT INTO TABLE3(EMPCODE,EXPTYPE,INST_COMP,ADDRESS,DESIGNATION,DATEOFJOIN,DATEOFRELEASE,SALARY,REMARKS,EXPERIENCEFILE) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (E00.get(), E28.get(), E29.get(), E30.get(), E31.get(), bbb, bbbb, int(E34.get()),
                                 E35.get(), filename4))
                            mydb.commit()
                            text2.insert(2.0, '\n')
                            text2.insert(2.0,
                                         E28.get() + '|' + E29.get() + '|' + E30.get() + '|' + E31.get() + '|' + E32.get() + '|' + E33.get() + '|' + E34.get() + '|' + E35.get())
                            shutil.copy(filex4, folname + '/' + filename4)
                            filename4 = "No Doc. Uploaded"
                            tkinter.messagebox.showinfo('Confirmation!!', 'Response Successfully Submitted!!')
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Submitted without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')

                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def Experience_upload():
                    try:
                        global filename4
                        global filex4
                        file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                        filex4 = file1.name
                        f, ext = os.path.splitext(filex4)
                        if os.path.getsize(filex4) <= 55000:
                            del file1
                            a = E00.get() + '_' + E32.get()
                            filename4 = a + ext
                            tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')
                        else:
                            tkinter.messagebox.showinfo('Uploading Error!!', 'Your Uploading Image must be below 50KB')
                    except AttributeError:
                        tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')

                def addmore3():
                    E28.delete(0, END)
                    E29.delete(0, END)
                    E30.delete(0, END)
                    E31.delete(0, END)
                    E32.delete(0, END)
                    E32.insert(0, 'DD-MM-YYYY')
                    E33.delete(0, END)
                    E33.insert(0, 'DD-MM-YYYY')
                    E34.delete(0, END)
                    E35.delete(0, END)

                def submit4():
                    global filename5
                    if loginus == E00.get() or loginus == "admin":

                        try:
                            mycursor.execute("INSERT INTO TABLE4(EMPCODE,SPECIALACV,SPECIALFILE) VALUES (%s,%s,%s)",
                                             (E00.get(), text3.get('1.0', END), filename5))
                            mydb.commit()
                            shutil.copy(filex5, folname + '/' + filename5)
                            filename5 = "No Doc. Uploaded"
                            tkinter.messagebox.showinfo('Confirmation!!', 'Response Successfully Submitted!!')
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Submitted without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')

                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def Special_upload():
                    try:
                        global filename5
                        global filex5
                        file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                        filex5 = file1.name
                        f, ext = os.path.splitext(filex5)
                        if os.path.getsize(filex5) <= 55000:
                            del file1
                            a = E00.get() + '_Special'
                            filename5 = a + ext
                            tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')

                        else:
                            tkinter.messagebox.showinfo('Uploading Error!!', 'Your Uploading Image must be below 50KB')
                    except AttributeError:
                        tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')

                def addmore4():
                    text3.delete(0.0, END)

                def k_func():
                    global sig
                    E13.config(state="normal")
                    E13.delete(0,END)
                    E14.config(state="normal")
                    E14.delete(0,END)
                    E15.config(state="normal")
                    E15.delete(0,END)
                    E16.config(state="normal")
                    E16.delete(0,END)
                    E17.config(state="normal")
                    E17.delete(0,END)
                    state2.set(" ")
                    E19.config(state="normal")
                    E19.delete(0,END)
                    E19.insert(0,0)
                    sig = 1

                def k_func_no():
                    global sig
                    E13.config(state="normal")
                    E13.delete(0, END)
                    E13.insert(0, E6.get())
                    E13.config(state="disabled")
                    E14.config(state="normal")
                    E14.delete(0, END)
                    E14.insert(0,E7.get())
                    E14.config(state="disabled")
                    E15.config(state="normal")
                    E15.delete(0, END)
                    E15.insert(0,E8.get())
                    E15.config(state="disabled")
                    E16.config(state="normal")
                    E16.delete(0, END)
                    E16.insert(0,E9.get())
                    E16.config(state="disabled")
                    E17.config(state="normal")
                    E17.delete(0, END)
                    E17.insert(0,E10.get())
                    E17.config(state="disabled")
                    state2.set(state1.get())
                    E19.config(state="normal")
                    E19.delete(0, END)
                    E19.insert(0,int(E12.get()))
                    E19.config(state="disabled")
                    sig = 0

                def submit5():
                    global filename6
                    if loginus == E00.get() or loginus == "admin":

                        try:
                            mycursor.execute(
                                "INSERT INTO TABLE5(EMPCODE,YOL,CL,ML,EL,SL,OD,OTHER,LEAVEFILE) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (E00.get(), leaveyear.get(), E36.get(), E37.get(), E38.get(), E39.get(), E40.get(),
                                 E41.get(), filename6))
                            mydb.commit()
                            text4.insert(2.0, "\n")
                            text4.insert(2.0,
                                         str(leaveyear.get()) + '|' + str(E36.get()) + '|' + str(E37.get()) + '|' + str(
                                             E38.get()) + '|' + str(E39.get()) + '|' + str(E40.get()) + '|' + str(
                                             E41.get()))
                            shutil.copy(filex6, folname + '/' + filename6)
                            filename6 = "No Doc. Uploaded"
                            tkinter.messagebox.showinfo('Confirmation!!', 'Response Successfully Submitted!!')
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Submitted without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def leave_upload():
                    try:
                        global filename6
                        global filex6
                        file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                        filex6 = file1.name
                        f, ext = os.path.splitext(filex6)
                        if os.path.getsize(filex6) <= 55000:
                            del file1
                            a = E00.get() + '_leaveallot' + '_' + str(leaveyear.get())
                            filename6 = a + ext
                            tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')

                        else:
                            tkinter.messagebox.showinfo('Uploading Error!!', 'Your Uploading Image must be below 50KB')
                    except AttributeError:
                        tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')

                def addmore5():
                    leaveyear.set(0)
                    E36.delete(0, END)
                    E37.delete(0, END)
                    E38.delete(0, END)
                    E39.delete(0, END)
                    E40.delete(0, END)
                    E41.delete(0, END)

                def submit6():
                    global filename7
                    if loginus == E00.get() or loginus == "admin":

                        try:
                            aaaaa = E42.get().split('-')
                            bbbbb = ''
                            bbbbb = aaaaa[-1] + '-' + aaaaa[-2] + '-' + aaaaa[-3]
                            mycursor.execute("INSERT INTO TABLE6(EMPCODE,DORP,DESCR,REWARDFILE) VALUES (%s,%s,%s,%s)",
                                             (E00.get(), bbbbb, E43.get(), filename7))
                            mydb.commit()
                            text5.insert(2.0, "\n")
                            text5.insert(2.0, E42.get() + '|' + E43.get())
                            shutil.copy(filex7, folname + '/' + filename7)
                            filename7 = "No Doc. Uploaded"
                            tkinter.messagebox.showinfo('Confirmation!!', 'Response Successfully Submitted!!')
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Submitted without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def reward_upload():
                    try:
                        global filename7
                        global filex7
                        file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                        filex7 = file1.name
                        f, ext = os.path.splitext(filex7)
                        if os.path.getsize(filex7) <= 55000:
                            del file1
                            a = E00.get() + '_reward_penalty' + '_' + E42.get()
                            filename7 = a + ext
                            tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')

                        else:
                            tkinter.messagebox.showinfo('Uploading Error!!', 'Your Uploading Image must be below 50KB')
                    except AttributeError:
                        tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')

                def addmore6():
                    E42.delete(0, END)
                    E42.insert(0, "DD-MM-YYYY")
                    E43.delete(0, END)

                def submit7():
                    global filename8
                    if loginus == E00.get() or loginus == "admin":

                        try:
                            aa = str(E003.get()).split('-')
                            bb = ''
                            bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                            mycursor.execute(
                                "INSERT INTO TABLE7(EMPCODE,DOPAY,BASIC,DA,HRA,OTHER,PAYSCALEFILE) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                                (E00.get(), bb, str(E44.get()), str(E45.get()), str(E46.get()),
                                 str(E47.get()), filename8))
                            mydb.commit()
                            text6.insert(2.0, "\n")
                            text6.insert(2.0, bb + '|' + str(E44.get()) + '|' + str(E45.get()) + '|' + str(E46.get()) + '|' + str(E47.get()))
                            shutil.copy(filex8, folname + '/' + filename8)
                            filename8 = "No Doc. Uploaded"
                            tkinter.messagebox.showinfo('Confirmation!!', 'Response Successfully Submitted!!')
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Submitted without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def pay_upload():
                    try:
                        global filename8
                        global filex8
                        file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                        filex8 = file1.name
                        f, ext = os.path.splitext(filex8)
                        if os.path.getsize(filex8) <= 55000:
                            del file1
                            a = E00.get() + '_pay' + '_' + str(E003.get())
                            filename8 = a + ext
                            tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')
                        else:
                            tkinter.messagebox.showinfo('Uploading Error!!', 'Your Uploading Image must be below 50KB')
                    except AttributeError:
                        tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')

                def addmore7():
                    E003.delete(0,END)
                    E003.insert(0,"DD-MM-YYYY")
                    E44.delete(0, END)
                    E44.insert(0,0)
                    E45.delete(0, END)
                    E45.insert(0,0)
                    E46.delete(0, END)
                    E46.insert(0,0)
                    E47.delete(0, END)
                    E47.insert(0,0)

                def submit8():
                    global filename9
                    if loginus == E00.get() or loginus == "admin":

                        try:
                            mycursor.execute(
                                "INSERT INTO TABLE8(EMPCODE,SEM,PAPERCODE,PAPERNAME,DEPARTMENT,YOA,SUBJECTALLOTFILE) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                                (E00.get(), sem.get(), E48.get(), E49.get(), dept2.get(), str(subyear.get()), filename9))
                            mydb.commit()
                            text7.insert(2.0, "\n")
                            text7.insert(2.0,
                                         sem.get() + '|' + E48.get() + '|' + E49.get() + '|' + dept2.get() + '|' + str(
                                             subyear.get()))
                            shutil.copy(filex9, folname + '/' + filename9)
                            filename9 = "No Doc. Uploaded"
                            tkinter.messagebox.showinfo('Confirmation!!', 'Response Successfully Submitted!!')
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Submitted without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def subjectallot_upload():
                    try:
                        global filename9
                        global filex9
                        file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                        filex9 = file1.name
                        f, ext = os.path.splitext(filex9)
                        if os.path.getsize(filex9) <= 55000:
                            del file1
                            a = E00.get() + '_subjectallot' + '_' + sem.get() + '_' + str(subyear.get())
                            filename9 = a + ext
                            tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')

                        else:
                            tkinter.messagebox.showinfo('Uploading Error!!', 'Your Uploading Image must be below 50KB')
                    except AttributeError:
                        tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')

                def addmore8():
                    sem.set('')
                    E48.delete(0, END)
                    E49.delete(0, END)
                    dept2.set(" ")
                    subyear.set(0)

                def submit9():
                    global filename10
                    if loginus == E00.get() or loginus == "admin":

                        try:
                            a1 = E001.get().split('-')
                            b1 = ''
                            b1 = a1[-1] + '-' + a1[-2] + '-' + a1[-3]
                            a2 = E002.get().split('-')
                            b2 = ''
                            b2 = a2[-1] + '-' + a2[-2] + '-' + a2[-3]
                            mycursor.execute(
                                "INSERT INTO TABLE9(EMPCODE,FROMDATE,TODATE,DESCR,ADDRESPFILE) VALUES (%s,%s,%s,%s,%s)",
                                (E00.get(), str(b1), str(b2), E51.get(), filename10))
                            mydb.commit()
                            text8.insert(2.0, "\n")
                            text8.insert(2.0, b1 + '|' + b2 + '|' + E51.get())
                            shutil.copy(filex10, folname + '/' + filename10)
                            filename10 = "No Doc. Uploaded"
                            tkinter.messagebox.showinfo('Confirmation!!', 'Response Successfully Submitted!!')
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Submitted without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def addresp_upload():
                    try:
                        global filename10
                        global filex10
                        file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                        filex10 = file1.name
                        f, ext = os.path.splitext(filex10)
                        if os.path.getsize(filex10) <= 55000:
                            del file1
                            a = E00.get() + '_addresp' + '_' + str(E001.get())
                            filename10 = a + ext
                            tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')
                        else:
                            tkinter.messagebox.showinfo('Uploading Error!!', 'Your Uploading Image must be below 50KB')
                    except AttributeError:
                        tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')

                def addmore9():
                    E001.delete(0, END)
                    E001.insert(0,"DD-MM-YYYY")
                    E002.delete(0, END)
                    E002.insert(0,"DD-MM-YYYY")
                    E51.delete(0, END)

                def submit11():
                    global filename11
                    if loginus == E00.get() or loginus == "admin":

                        try:
                            mycursor.execute(
                                "INSERT INTO TABLE11(EMPCODE,ACCOUNTNO,BANKNAME,BRANCHCODE,IFSCCODE,BANKFILE) VALUES (%s,%s,%s,%s,%s,%s)",
                                (E00.get(), EE6.get(), EE7.get(), EE8.get(), EE9.get(), filename11))
                            mydb.commit()
                            shutil.copy(filex11, folname + '/' + filename11)
                            filename11 = "No Doc. Uploaded"
                            tkinter.messagebox.showinfo('Confirmation!!', 'Response Successfully Submitted!!')
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Submitted without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def bank_upload():
                    try:
                        global filename11
                        global filex11
                        file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                        filex11 = file1.name
                        f, ext = os.path.splitext(filex11)
                        if os.path.getsize(filex11) <= 55000:
                            del file1
                            a = E00.get() + '_bankdetails'
                            filename11 = a + ext
                            tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')
                        else:
                            tkinter.messagebox.showinfo('Uploading Error!!', 'Your Uploading Image must be below 50KB')
                    except AttributeError:
                        tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')

                def submit12():
                    global filename12
                    if loginus == E00.get() or loginus == "admin":

                        try:
                            aaaaaa = EE12.get().split('-')
                            bbbbbb = ''
                            bbbbbb = aaaaaa[-1] + '-' + aaaaaa[-2] + '-' + aaaaaa[-3]
                            mycursor.execute(
                                "INSERT INTO TABLE12(EMPCODE,COURSETYPE,DEPARTMENT,DESIGNATION,SUBSPECILIZE,DOJ,JOININGFILE) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                                (E00.get(), coursetype.get(), dept1.get(), designation.get(), EE11.get(), bbbbbb,
                                 filename12))
                            mydb.commit()
                            text10.insert(2.0, "\n")
                            text10.insert(2.0,
                                          coursetype.get() + '|' + dept1.get() + '|' + designation.get() + '|' + EE11.get() + '|' + bbbbbb)
                            shutil.copy(filex12, folname + '/' + filename12)
                            filename12 = "No Doc. Uploaded"
                            tkinter.messagebox.showinfo('Confirmation!!', 'Response Successfully Submitted!!')
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Submitted without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def joining_upload():
                    try:
                        global filename12
                        global filex12
                        file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                        filex12 = file1.name
                        f, ext = os.path.splitext(filex12)
                        if os.path.getsize(filex12) <= 55000:
                            del file1
                            a = E00.get() + '_joining' + '_' + str(EE12.get())
                            filename12 = a + ext
                            tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')
                        else:
                            tkinter.messagebox.showinfo('Uploading Error!!', 'Your Uploading Image must be below 50KB')
                    except AttributeError:
                        tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')

                def addmore11():
                    coursetype.set("")
                    EE10.delete(0, END)
                    designation.set("")
                    EE11.delete(0, END)
                    EE12.delete(0, END)
                    EE12.insert(0, "DD-MM-YYYY")

                def edit1():
                    global filename1
                    global filename2
                    if loginus == E00.get() or loginus == "admin":
                        def photoedit():

                            try:
                                global filename1
                                global filex1
                                file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"),))
                                filex1 = file1.name
                                f, ext = os.path.splitext(filex1)
                                if os.path.getsize(filex1) <= 55000:
                                    del file1
                                    a = E00.get() + '_photo'
                                    filename1 = a + ext
                                    tkinter.messagebox.showinfo('Confirmation', 'New Image File Uploaded Successfully.')


                                else:
                                    tkinter.messagebox.showinfo('Uploading Error!!',
                                                                'Your Uploading Image must be below 50KB')

                                root1.deiconify()
                            except AttributeError:
                                tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')
                                root1.deiconify()

                        def signedit():

                            try:
                                global filename2
                                global filex2
                                file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"),))
                                filex2 = file1.name
                                f, ext = os.path.splitext(filex2)
                                if os.path.getsize(filex2) <= 55000:
                                    del file1
                                    a = E00.get() + '_sign'
                                    filename2 = a + ext
                                    tkinter.messagebox.showinfo('Confirmation', 'New Image File Uploaded Successfully.')

                                else:
                                    tkinter.messagebox.showinfo('Uploading Error!!',
                                                                'Your Uploading Image must be below 50KB')

                                root1.deiconify()
                            except AttributeError:
                                tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')
                                root1.deiconify()

                        def subedit1():
                            global filename1
                            global filename2
                            try:
                                aaaaaa = en4.get().split('-')
                                bbbbbb = ''
                                bbbbbb = aaaaaa[-1] + '-' + aaaaaa[-2] + '-' + aaaaaa[-3]
                                mycursor.execute(
                                    "UPDATE TABLE1 SET FNAME=%s,MNAME=%s,LNAME=%s,DOB=%s,RELIGION=%s,GENDER=%s,CASTE=%s,BLOODGROUP=%s,PREADDRESS=%s,PRECITY=%s,PRESTATE=%s,PREPIN=%s,PERADDRESS=%s,PERCITY=%s,PERSTATE=%s,PERPIN=%s,MOBILENO=%s,ALTMOBILENO=%s,EMAIL=%s,PHOTOFILE=%s,SIGNATUREFILE=%s WHERE EMPCODE=%s",
                                    (en1.get(), en2.get(), en3.get(), bbbbbb, Co1.get(), Co2.get(), Co3.get(), en5.get(), en6.get(), en7.get(),
                                     Co4.get(), en8.get(), en9.get(), en10.get(), Co5.get(), en11.get(), en12.get(), en13.get(),
                                     en14.get(), filename1, filename2, E00.get(),))
                                mydb.commit()
                                shutil.copy(filex1, folname + '/' + filename1)
                                shutil.copy(filex2, folname + '/' + filename2)
                                filename1 = "No Doc. Uploaded"
                                filename2 = "No Doc. Uploaded"
                                tkinter.messagebox.showinfo('Confirmation', 'New data successfully edited.')

                                root1.destroy()
                            except AttributeError:
                                tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                            except MySQLdb.IntegrityError:
                                tkinter.messagebox.showinfo('Connectivity Problem.',
                                                            'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                            except NameError:
                                tkinter.messagebox.showinfo('Error!!','Please Enter all the details and upload the file to submit')
                                root1.deiconify()
                            except FileNotFoundError:
                                tkinter.messagebox.showinfo('Confirmation!!',
                                                            'Response Successfully Edited without Document upload / Insufficient data.!!')
                            except MySQLdb._exceptions.OperationalError:
                                tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                                root1.deiconify()

                        try:
                            mycursor.execute("select * from table1 where EMPCODE=%s",(E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows

                            root1 = Tk()
                            rel=StringVar()
                            gen=StringVar()
                            cas=StringVar()
                            sta1=StringVar()
                            sta2=StringVar()
                            list1 = ["Hindu", "Islam", "Sikh", "Christian", "Judaism", "Buddhism", "Animism"]
                            list2 = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat","Haryana", "Himachal Pradesh", "Jammu & Kashmir", "Jharkhand", "Karnataka", "Kerala","Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha","Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh","Uttarakhand", "West Bengal"]
                            list3 = ["Male","Female"]
                            list4 = ["GENERAL", "SC", "ST", "OBC", "OTHERS"]
                            d = Font(family="Arial", size=13, weight="bold", slant="roman", underline=0)
                            root1.title('Edit')
                            root1.geometry('1500x1000')
                            root1.iconbitmap(r'diatmlogo.ico')
                            root1.configure(background='white')
                            lab1=Label(root1,text="First Name:",font=d).grid(row=0,column=0,padx=10,pady=10)
                            en1=Entry(root1)
                            en1.grid(row=0,column=1,padx=10,pady=10)
                            en1.insert(0,a[1])
                            lab2 = Label(root1, text="Middle Name:", font=d).grid(row=0, column=2, padx=10, pady=10)
                            en2 = Entry(root1)
                            en2.grid(row=0, column=3, padx=10, pady=10)
                            en2.insert(0, a[2])
                            lab3 = Label(root1, text="Last Name:", font=d).grid(row=0, column=4, padx=10, pady=10)
                            en3 = Entry(root1)
                            en3.grid(row=0, column=5, padx=10, pady=10)
                            en3.insert(0, a[3])
                            lab4 = Label(root1, text="Date of Birth:", font=d).grid(row=1, column=0, padx=10, pady=10)
                            en4 = Entry(root1)
                            en4.grid(row=1, column=1, padx=10, pady=10)
                            aa = str(a[4]).split('-')
                            bb = ''
                            bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                            en4.insert(0, bb)
                            lab5 = Label(root1, text="Religion:", font=d).grid(row=1, column=2, padx=10, pady=10)
                            Co1 = Combobox(root1, values=list1, height=4, textvariable=rel)
                            Co1.set(a[5])
                            Co1.grid(row=1, column=3, padx=10, pady=10)
                            rel.set(a[5])
                            lab6 = Label(root1, text="Gender:", font=d).grid(row=1, column=4, padx=10, pady=10)
                            Co2 = Combobox(root1, values=list3, height=2, textvariable=gen)
                            Co2.set(str(a[6]))
                            Co2.grid(row=1, column=5, padx=10,pady=10)
                            gen.set(a[6])
                            lab7 = Label(root1, text="Caste:", font=d).grid(row=1, column=6, padx=10, pady=10)
                            Co3 = Combobox(root1, values=list4, height=3, textvariable=cas)
                            Co3.set(str(a[7]))
                            Co3.grid(row=1, column=7, padx=10,pady=10)
                            cas.set(a[7])
                            lab8 = Label(root1, text="Blood Group:", font=d).grid(row=2, column=0, padx=10, pady=10)
                            en5 = Entry(root1)
                            en5.grid(row=2, column=1, padx=10, pady=10)
                            en5.insert(0, a[8])
                            lab9 = Label(root1, text="Present Address:", font=d).grid(row=3, column=0, padx=10, pady=10)
                            en6 = Entry(root1,width=80)
                            en6.grid(row=3, columnspan=5, padx=10, pady=20,sticky="e")
                            en6.insert(0, a[9])
                            lab10 = Label(root1, text="Present City:", font=d).grid(row=4, column=0, padx=10, pady=10)
                            en7 = Entry(root1)
                            en7.grid(row=4, column=1, padx=10, pady=10)
                            en7.insert(0, a[10])
                            lab11 = Label(root1, text="Present State:", font=d).grid(row=4, column=2, padx=10, pady=10)
                            Co4 = Combobox(root1, values=list2, height=4, textvariable=sta1)
                            Co4.set(str(a[11]))
                            Co4.grid(row=4, column=3, padx=10, pady=10)
                            sta1.set(a[11])
                            lab4 = Label(root1, text="Present PIN:", font=d).grid(row=4, column=4, padx=10, pady=10)
                            en8 = Entry(root1)
                            en8.grid(row=4, column=5, padx=10, pady=10)
                            en8.insert(0, a[12])
                            lab9 = Label(root1, text="Permanent Address:", font=d).grid(row=5, column=0, padx=10, pady=10)
                            en9 = Entry(root1, width=80)
                            en9.grid(row=5, columnspan=5, padx=10, pady=20,sticky="e")
                            en9.insert(0, a[13])
                            lab10 = Label(root1, text="Permanent City:", font=d).grid(row=6, column=0, padx=10, pady=10)
                            en10 = Entry(root1)
                            en10.grid(row=6, column=1, padx=10, pady=10)
                            en10.insert(0, a[14])
                            lab11 = Label(root1, text="Permanent State:", font=d).grid(row=6, column=2, padx=10, pady=10)
                            Co5 = Combobox(root1, values=list2, height=4, textvariable=sta2)
                            Co5.set(str(a[15]))
                            Co5.grid(row=6, column=3, padx=10,pady=10)
                            sta2.set(a[15])
                            lab12 = Label(root1, text="Permanent PIN:", font=d).grid(row=6, column=4, padx=10, pady=10)
                            en11 = Entry(root1)
                            en11.grid(row=6, column=5, padx=10, pady=10)
                            en11.insert(0, a[16])
                            lab13 = Label(root1, text="Mobile Number:", font=d).grid(row=7, column=0, padx=10, pady=10)
                            en12 = Entry(root1)
                            en12.grid(row=7, column=1, padx=10, pady=10)
                            en12.insert(0, a[17])
                            lab14 = Label(root1, text="Alternative Mobile Number:", font=d).grid(row=7, column=2, padx=10, pady=10)
                            en13 = Entry(root1)
                            en13.grid(row=7, column=3, padx=10, pady=10)
                            en13.insert(0, a[18])
                            lab15 = Label(root1, text="Email:", font=d).grid(row=7, column=4, padx=10,pady=10)
                            en14 = Entry(root1,width=40)
                            en14.grid(row=7, column=5, padx=10, pady=10)
                            en14.insert(0, a[19])
                            filename1=a[20]
                            filename2=a[21]
                            But1 = Button(root1,text="Edit Photo",command=photoedit).grid(row=8,column=1,padx=10,pady=10)
                            But2 = Button(root1, text="Edit Signature", command=signedit).grid(row=8, column=3, padx=10, pady=10)
                            But3 = Button(root1, text="Submit Changes", command=subedit1).grid(row=9, column=2, padx=10, pady=30)

                            root1.mainloop()
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.','Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!','Please Enter the EMPCODE')
                            root1.destroy()
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!','Response Successfully Edited without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                            root1.deiconify()

                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def edit2():
                    global filename11
                    global filex11
                    if loginus == E00.get() or loginus == "admin":
                        try:

                            def ok():
                                global filename11
                                x = listbox.get(ANCHOR)
                                listbox.delete(ANCHOR)
                                c = x.split("||")
                                Co1.config(state="normal")
                                Co1.set(" ")
                                Co1.set(c[0])
                                Co1.config(state="disable")
                                en1.delete(0, END)
                                en1.insert(0,c[1])
                                filename11=c[2]
                            def docupload1():
                                try:
                                    global filename11
                                    global filex11
                                    file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                                    filex11 = file1.name
                                    f, ext = os.path.splitext(filex11)
                                    if os.path.getsize(filex11) <= 55000:
                                        del file1
                                        a = E00.get() + '_' + Co1.get()
                                        filename11 = a + ext
                                        tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')
                                        root1.deiconify()

                                    else:
                                        tkinter.messagebox.showinfo('Uploading Error!!',
                                                                    'Your Uploading Image must be below 50KB')
                                        root1.deiconify()
                                except AttributeError:
                                    tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')
                                    root1.deiconify()
                            def subedit2():
                                global filename11
                                try:
                                    mycursor.execute("UPDATE TABLE10 SET DOCIDNO=%s,LEGALFILE=%s WHERE(EMPCODE=%s AND DOCNAME=%s) ",(str(en1.get()), filename11, E00.get(), Co1.get(),))
                                    mydb.commit()
                                    listbox.delete(0,END)
                                    mycursor.execute("select * from table10 where EMPCODE=%s", (E00.get(),))
                                    myresult = mycursor.fetchall()
                                    for rows in myresult:
                                        a = rows
                                        b = a[1] + '||' + a[2] + '||' + a[3]
                                        listbox.insert(END, b)
                                    shutil.copy(filex11, folname + '/' + filename11)
                                    filename11 = "No Doc. Uploaded"
                                    tkinter.messagebox.showinfo('Confirmation', 'New data successfully edited.')
                                    root1.deiconify()
                                except AttributeError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                                except MySQLdb.IntegrityError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.',
                                                                'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                                except NameError:
                                    tkinter.messagebox.showinfo('Error!!',
                                                                'Please Enter all the details and upload the file to submit')
                                    root1.deiconify()
                                except FileNotFoundError:
                                    tkinter.messagebox.showinfo('Confirmation!!','Response Edited Successfully')
                                    root1.deiconify()
                                except MySQLdb._exceptions.OperationalError:
                                    tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                                    root1.deiconify()

                            d = Font(family="Arial", size=13, weight="bold", slant="roman", underline=0)
                            root1 = Tk()
                            list1 = ["Epic_Voter ID Card", "Adhaar Card", "Passport", "PAN card", "Driving Licence"]
                            root1.geometry("1000x500")
                            root1.title("Edit")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=80)
                            listbox.grid(row=0,columnspan=4,padx=10,pady=10)

                            lab1=Label(root1,text="Document Name:",font=d).grid(row=4,column=0,padx=10,pady=10)
                            Co1 = Combobox(root1, values=list1, height=4)
                            Co1.grid(row=4, column=1, padx=10, pady=10)
                            Co1.config(state="disable")
                            lab2 = Label(root1, text="Document ID No.:", font=d).grid(row=4, column=2, padx=10, pady=10)
                            en1=Entry(root1,width=30)
                            en1.grid(row=4,column=3,padx=10,pady=10)
                            mycursor.execute("select * from table10 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                b = a[1] + '||' + a[2] + '||' + a[3]
                                listbox.insert(END, b)
                            bu1 = Button(root1, text="OK", command=ok)
                            bu1.grid(row=3, column=2, padx=10, pady=10)
                            bu2 = Button(root1, text="Edit Document Upload", command=docupload1)
                            bu2.grid(row=4, column=4, padx=10, pady=10)
                            bu3 = Button(root1, text="Submit Changes", command=subedit2)
                            bu3.grid(row=5, column=2, padx=10, pady=10)
                            root1.mainloop()
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.','Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!','Please Enter the EMPCODE')
                            root1.destroy()
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!','Response Successfully Edited without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                            root1.deiconify()

                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def edit3():
                    global filename11
                    global filex11
                    if loginus == E00.get() or loginus == "admin":
                        try:
                            def docupload():
                                global filex11
                                global filename11
                                try:
                                    global filename11
                                    global filex11
                                    file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                                    filex11 = file1.name
                                    f, ext = os.path.splitext(filex11)
                                    if os.path.getsize(filex11) <= 55000:
                                        del file1
                                        a = E00.get() + '_' +"bankdetails"
                                        filename11 = a + ext
                                        tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')
                                        root1.deiconify()

                                    else:
                                        tkinter.messagebox.showinfo('Uploading Error!!',
                                                                    'Your Uploading Image must be below 50KB')
                                        root1.deiconify()
                                except AttributeError:
                                    tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')
                                    root1.deiconify()
                            def subedit3():
                                global filename11
                                global filex11
                                try:
                                    mycursor.execute("UPDATE TABLE11 SET ACCOUNTNO=%s,BANKNAME=%s,BRANCHCODE=%s,IFSCCODE=%s,BANKFILE=%s WHERE EMPCODE=%s ",
                                        (en1.get(), en2.get(), en3.get(), en4.get(), filename11, E00.get(),))
                                    mydb.commit()
                                    shutil.copy(filex11, folname + '/' + filename11)
                                    filename11 = "No Doc. Uploaded"
                                    tkinter.messagebox.showinfo('Confirmation', 'New data successfully edited.')
                                    root1.destroy()

                                except AttributeError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                                except MySQLdb.IntegrityError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.','Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                                    root1.deiconify()
                                except NameError:
                                    tkinter.messagebox.showinfo('Error!!','Please Enter all the details and upload the file to submit')
                                except FileNotFoundError:
                                    tkinter.messagebox.showinfo('Confirmation!!', 'Response Edited Successfully')
                                    root1.destroy()
                                except MySQLdb._exceptions.OperationalError:
                                    tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                                    root1.deiconify()



                            mycursor.execute("select * from table11 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                            d = Font(family="Arial", size=13, weight="bold", slant="roman", underline=0)
                            root1 = Tk()
                            root1.geometry("1000x500")
                            root1.title("Edit")
                            root1.iconbitmap(r'diatmlogo.ico')
                            lab1=Label(root1,text="Bank Account No.",font=d).grid(row=0,column=0,padx=10,pady=10)
                            en1=Entry(root1)
                            en1.grid(row=1,column=0,padx=10,pady=10)
                            en1.insert(0,a[1])
                            lab2 = Label(root1, text="Name of Bank", font=d).grid(row=0, column=1, padx=10, pady=10)
                            en2 = Entry(root1)
                            en2.grid(row=1, column=1, padx=10, pady=10)
                            en2.insert(0, a[2])
                            lab3 = Label(root1, text="Branch Code", font=d).grid(row=0, column=2, padx=10, pady=10)
                            en3 = Entry(root1)
                            en3.grid(row=1, column=2, padx=10, pady=10)
                            en3.insert(0, a[3])
                            lab4 = Label(root1, text="IFSC Code", font=d).grid(row=0, column=3, padx=10, pady=10)
                            en4 = Entry(root1)
                            en4.grid(row=1, column=3, padx=10, pady=10)
                            en4.insert(0, a[4])
                            filename11=a[5]
                            but = Button(root1, text="Edit document upload", command=docupload).grid(row=1, column=4, padx=10,pady=10)
                            but=Button(root1,text="Submit Changes",command=subedit3).grid(row=2,column=3,padx=10,pady=10)
                            root1.mainloop()
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                            root1.deiconify()
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!','Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Edited without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                            root1.deiconify()
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')
                        root1.destroy()

                def edit4():
                    if loginus == E00.get() or loginus == "admin":
                        try:
                            def ok():
                                global filename11
                                x = listbox.get(ANCHOR)
                                listbox.delete(ANCHOR)
                                c = x.split("||")
                                Co1.set(" ")
                                Co1.set(c[0])
                                Co2.set(" ")
                                Co2.set(c[1])
                                Co3.set(" ")
                                Co3.set(c[2])
                                en1.delete(0, END)
                                en1.insert(0, c[3])
                                en2.delete(0, END)
                                en2.insert(0, c[4])
                                filename11 = c[5]
                            def docupload1():
                                try:
                                    global filename11
                                    global filex11
                                    file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                                    filex11 = file1.name
                                    f, ext = os.path.splitext(filex11)
                                    if os.path.getsize(filex11) <= 55000:
                                        del file1
                                        a = E00.get() + '_' +'joining'+'_'+ en2.get()
                                        filename11 = a + ext
                                        tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')
                                        root1.deiconify()

                                    else:
                                        tkinter.messagebox.showinfo('Uploading Error!!',
                                                                    'Your Uploading Image must be below 50KB')
                                        root1.deiconify()
                                except AttributeError:
                                    tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')
                                    root1.deiconify()
                            def subedit4():
                                global filex11
                                global filename11
                                try:

                                    aa = str(en2.get()).split('-')
                                    bb = ''
                                    bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                                    mycursor.execute(
                                        "UPDATE TABLE12 SET COURSETYPE=%s,DEPARTMENT=%s,DESIGNATION=%s,SUBSPECILIZE=%s,DOJ=%s,JOININGFILE=%s WHERE EMPCODE=%s",
                                        (Co1.get(), Co2.get(), Co3.get(), en1.get(),bb, filename11,
                                         E00.get(),))
                                    mydb.commit()
                                    listbox.delete(0, END)
                                    mycursor.execute("select * from table12 where EMPCODE=%s", (E00.get(),))
                                    myresult = mycursor.fetchall()
                                    for rows in myresult:
                                        a = rows
                                        aa = str(a[5]).split('-')
                                        bb = ''
                                        bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                                        b = a[1] + '||' + a[2] + '||' + a[3] + '||' + a[4] + '||' + bb + "||" + a[6]
                                        listbox.insert(END, b)
                                    shutil.copy(filex11, folname + '/' + filename11)
                                    filename11 = "No Doc. Uploaded"
                                    tkinter.messagebox.showinfo('Confirmation', 'New data successfully edited.')
                                    root1.deiconify()

                                except AttributeError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                                except MySQLdb.IntegrityError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.',
                                                                'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                                except NameError:
                                    tkinter.messagebox.showinfo('Error!!',
                                                                'Please Enter all the details and upload the file to submit')
                                    root1.deiconify()

                                except FileNotFoundError:
                                    tkinter.messagebox.showinfo('Confirmation!!', 'Response Edited Successfully')
                                    root1.deiconify()
                                except MySQLdb._exceptions.OperationalError:
                                    tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                                    root1.deiconify()

                            d = Font(family="Arial", size=13, weight="bold", slant="roman", underline=0)
                            root1 = Tk()
                            list1 = ["Under Graduate", "Post Graduate"]
                            list2 = ["Distinguished Professor", "Emeritus Professor", "Professor", "Associate Professor",
                                  "Assistant Professor", "Contractual Teacher", "Senior Technical Assistant",
                                  "Technical Assistant",
                                  "Others"]

                            list3 = ["CSE", "IT", "EE", "ME", "ECE", "CHE"]
                            root1.geometry("1000x500")
                            root1.title("Edit")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=100)
                            listbox.grid(row=0, columnspan=4, padx=10, pady=10)

                            lab1 = Label(root1, text="Course type:", font=d).grid(row=4, column=0, padx=10, pady=10)
                            Co1 = Combobox(root1, values=list1, height=4)
                            Co1.grid(row=4, column=1, padx=10, pady=10)
                            lab2 = Label(root1, text="Department:", font=d).grid(row=4, column=2, padx=10, pady=10)
                            Co2 = Combobox(root1, values=list3, height=4)
                            Co2.grid(row=4, column=3, padx=10, pady=10)
                            lab3 = Label(root1, text="Designation:", font=d).grid(row=4, column=4, padx=10, pady=10)
                            Co3 = Combobox(root1, values=list2, height=4)
                            Co3.grid(row=4, column=5, padx=10, pady=10)
                            lab4 = Label(root1, text="Subject Specialization:", font=d).grid(row=5, column=0, padx=10, pady=10)
                            en1=Entry(root1)
                            en1.grid(row=5, column=1, padx=10, pady=10)
                            lab5 = Label(root1, text="Date of joining:", font=d).grid(row=5, column=2, padx=10,pady=10)
                            en2 = Entry(root1)
                            en2.grid(row=5, column=3, padx=10, pady=10)
                            mycursor.execute("select * from table12 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                aa = str(a[5]).split('-')
                                bb = ''
                                bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                                b = a[1] + '||' + a[2] + '||' + a[3]+ '||' + a[4] + '||' + bb + "||" + a[6]
                                listbox.insert(END, b)
                            bu1 = Button(root1, text="OK", command=ok)
                            bu1.grid(row=3, column=2, padx=10, pady=10)
                            bu2 = Button(root1, text="Edit Document Upload", command=docupload1)
                            bu2.grid(row=5, column=4, padx=10, pady=10)
                            bu3 = Button(root1, text="Submit Changes", command=subedit4)
                            bu3.grid(row=6, column=2, padx=10, pady=10)
                            root1.mainloop()



                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!', 'Response Successfully Edited!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def edit5():
                    #
                    #mydb.commit()
                    if loginus == E00.get() or loginus == "admin":
                        try:
                            def ok():
                                global filename11
                                x = listbox.get(ANCHOR)
                                listbox.delete(ANCHOR)
                                c = x.split("||")
                                Co1.config(state="normal")
                                Co1.set(" ")
                                Co1.set(c[0])
                                Co1.config(state="disable")
                                en1.config(state="normal")
                                en1.delete(0,END)
                                en1.insert(0,c[1])
                                en1.config(state="disable")
                                en2.delete(0,END)
                                en2.insert(0,c[2])
                                en3.delete(0, END)
                                en3.insert(0, c[3])
                                en4.delete(0, END)
                                en4.insert(0, c[4])
                                en5.delete(0, END)
                                en5.insert(0,c[5])
                                en6.delete(0, END)
                                en6.insert(0,c[6])
                                filename11 = c[7]

                            def others():
                                if Co1.get()=="Others":
                                    en1.config(state="readonly")
                                else:
                                    en1.config(state="disable")
                                root1.after(100,others)

                            def docupload1():
                                try:
                                    global filename11
                                    global filex11
                                    file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                                    filex11 = file1.name
                                    f, ext = os.path.splitext(filex11)
                                    if os.path.getsize(filex11) <= 55000:
                                        del file1
                                        a = E00.get() + '_' +Co1.get()+'_'+ en1.get()
                                        filename11 = a + ext
                                        tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')
                                        root1.deiconify()

                                    else:
                                        tkinter.messagebox.showinfo('Uploading Error!!',
                                                                    'Your Uploading Image must be below 50KB')
                                        root1.deiconify()
                                except AttributeError:
                                    tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')
                                    root1.deiconify()

                            def subedit5():
                                global filex11
                                global filename11
                                try:

                                    aa = str(en4.get()).split('-')
                                    bb = ''
                                    bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                                    mycursor.execute("UPDATE TABLE2 SET DESCR=%s,UNIVER_BOARD=%s,INSTITUTION=%s,YEAROFPASS=%s,MARKSINPERCENT=%s,REMARKS=%s,ACADEMICFILE=%s WHERE (EMPCODE=%s AND DEGREEOBT=%s)",(en1.get(), en2.get(), en3.get(), bb, en5.get(),en6.get(),filename11, E00.get(),Co1.get(),))
                                    mydb.commit()
                                    listbox.delete(0, END)
                                    mycursor.execute("select * from table2 where EMPCODE=%s", (E00.get(),))
                                    myresult = mycursor.fetchall()
                                    for rows in myresult:
                                        a = rows
                                        aa = str(a[5]).split('-')
                                        bb = ''
                                        bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                                        b = a[1] + '||' + a[2] + '||' + a[3] + '||' + a[4] + '||' + bb + "||" + str(a[6]) + "||" + a[7] + "||" + a[8]
                                        listbox.insert(END, b)
                                    shutil.copy(filex11, folname + '/' + filename11)
                                    filename11 = "No Doc. Uploaded"
                                    tkinter.messagebox.showinfo('Confirmation', 'New data successfully edited.')
                                    root1.deiconify()

                                except AttributeError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                                except MySQLdb.IntegrityError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.',
                                                                'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                                except NameError:
                                    tkinter.messagebox.showinfo('Error!!',
                                                                'Please Enter all the details and upload the file to submit')
                                    root1.deiconify()

                                except FileNotFoundError:
                                    tkinter.messagebox.showinfo('Confirmation!!', 'Response Edited Successfully')
                                    root1.deiconify()
                                except MySQLdb._exceptions.OperationalError:
                                    tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                                    root1.deiconify()

                            d = Font(family="Arial", size=13, weight="bold", slant="roman", underline=0)
                            root1 = Tk()
                            list1 = ["CLASS X", "CLASS XII", "CLASS DIPLOMA", "ITI", "GRADUATION", "POST GRADUATION", "P.H.D","Others"]

                            root1.geometry("1100x500")
                            root1.title("Edit")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=100)
                            listbox.grid(row=0, columnspan=4, padx=10, pady=10)

                            lab1 = Label(root1, text="Degree Obtained:", font=d).grid(row=4, column=0, padx=10, pady=10)
                            Co1 = Combobox(root1, values=list1, height=4)
                            Co1.grid(row=5, column=0, padx=10, pady=10)
                            Co1.config(state="disable")
                            en1=Entry(root1)
                            en1.grid(row=6,column=0,padx=10,pady=10)
                            en1.config(state="disable")
                            root1.after(100,others)
                            lab2 = Label(root1, text="University/Board:", font=d).grid(row=4, column=1, padx=10, pady=10)
                            en2=Entry(root1)
                            en2.grid(row=5, column=1, padx=10, pady=10)
                            lab3 = Label(root1, text="Institution:", font=d).grid(row=4, column=2, padx=10, pady=10)
                            en3=Entry(root1,width=40)
                            en3.grid(row=5, column=2, padx=10, pady=10)
                            lab4 = Label(root1, text="Year of Passing:", font=d).grid(row=4, column=3, padx=10,pady=10)
                            en4 = Entry(root1)
                            en4.grid(row=5, column=3, padx=10, pady=10)
                            lab5 = Label(root1, text="Marks in percentage:", font=d).grid(row=4, column=4, padx=10, pady=10)
                            en5 = Entry(root1)
                            en5.grid(row=5, column=4, padx=10, pady=10)
                            lab6 = Label(root1, text="Remarks:", font=d).grid(row=4, column=5, padx=10,pady=10)
                            en6 = Entry(root1)
                            en6.grid(row=5, column=5, padx=10, pady=10)
                            mycursor.execute("select * from table2 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                aa = str(a[5]).split('-')
                                bb = ''
                                bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                                b = a[1] + '||' + a[2] + '||' + a[3] + '||' + a[4] + '||' + bb + "||" + str(a[6]) + "||" + a[7] + "||" + a[8]
                                listbox.insert(END, b)
                            bu1 = Button(root1, text="OK", command=ok)
                            bu1.grid(row=3, column=2, padx=10, pady=10)
                            bu2 = Button(root1, text="Edit Document Upload", command=docupload1)
                            bu2.grid(row=6, column=5, padx=10, pady=10)
                            bu3 = Button(root1, text="Submit Changes", command=subedit5)
                            bu3.grid(row=7, column=2, padx=10, pady=10)
                            root1.mainloop()
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Edited without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def edit6():

                    if loginus == E00.get() or loginus == "admin":
                        try:
                            def ok():
                                global filename11
                                x = listbox.get(ANCHOR)
                                listbox.delete(ANCHOR)
                                c = x.split("||")
                                en1.delete(0,END)
                                en1.insert(0,c[0])
                                en2.delete(0,END)
                                en2.insert(0,c[1])
                                en3.delete(0, END)
                                en3.insert(0, c[2])
                                en4.delete(0, END)
                                en4.insert(0, c[3])
                                en5.delete(0, END)
                                en5.insert(0,c[4])
                                en6.delete(0, END)
                                en6.insert(0,c[5])
                                en7.delete(0,END)
                                en7.insert(0,c[6])
                                en8.delete(0,END)
                                en8.insert(0,c[7])
                                filename11 = c[8]

                            def docupload1():
                                try:
                                    global filename11
                                    global filex11
                                    file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                                    filex11 = file1.name
                                    f, ext = os.path.splitext(filex11)
                                    if os.path.getsize(filex11) <= 55000:
                                        del file1
                                        a = E00.get() + '_' + en5.get()
                                        filename11 = a + ext
                                        tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')
                                        root1.deiconify()

                                    else:
                                        tkinter.messagebox.showinfo('Uploading Error!!',
                                                                    'Your Uploading Image must be below 50KB')
                                        root1.deiconify()
                                except AttributeError:
                                    tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')
                                    root1.deiconify()

                            def subedit6():
                                global filex11
                                global filename11
                                try:

                                    aa = str(en5.get()).split('-')
                                    bb = ''
                                    bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                                    aaa = str(en6.get()).split('-')
                                    bbb = ''
                                    bbb = aaa[-1] + '-' + aaa[-2] + '-' + aaa[-3]
                                    mycursor.execute(
                                        "UPDATE TABLE3 SET INST_COMP=%s,ADDRESS=%s,DESIGNATION=%s,DATEOFJOIN=%s,DATEOFRELEASE=%s,SALARY=%s,REMARKS=%s,EXPERIENCEFILE=%s WHERE(EMPCODE=%s AND EXPTYPE=%s) ",
                                        (en2.get(), en3.get(), en4.get(), bb, bbb, en7.get(), en8.get(),
                                         filename11, E00.get(),en1.get(),))
                                    mydb.commit()
                                    listbox.delete(0, END)
                                    mycursor.execute("select * from table3 where EMPCODE=%s", (E00.get(),))
                                    myresult = mycursor.fetchall()
                                    for rows in myresult:
                                        a = rows
                                        aa = str(a[5]).split('-')
                                        bb = ''
                                        bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                                        aaa = str(a[6]).split('-')
                                        bbb = ''
                                        bbb = aaa[-1] + '-' + aaa[-2] + '-' + aaa[-3]
                                        b = a[1] + '||' + a[2] + '||' + a[3] + '||' + a[
                                            4] + '||' + bb + "||" + bbb + "||" + str(a[7]) + "||" + a[8] + "||" + a[9]
                                        listbox.insert(END, b)
                                    shutil.copy(filex11, folname + '/' + filename11)
                                    filename11 = "No Doc. Uploaded"
                                    tkinter.messagebox.showinfo('Confirmation', 'New data successfully edited.')
                                    root1.deiconify()

                                except AttributeError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                                except MySQLdb.IntegrityError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.',
                                                                'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                                except NameError:
                                    tkinter.messagebox.showinfo('Error!!',
                                                                'Please Enter all the details and upload the file to submit')
                                    root1.deiconify()

                                except FileNotFoundError:
                                    tkinter.messagebox.showinfo('Confirmation!!', 'Response Edited Successfully')
                                    root1.deiconify()
                                except MySQLdb._exceptions.OperationalError:
                                    tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                                    root1.deiconify()

                            d = Font(family="Arial", size=13, weight="bold", slant="roman", underline=0)
                            root1 = Tk()
                            root1.geometry("1200x500")
                            root1.title("Edit")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=100)
                            listbox.grid(row=0, columnspan=4, padx=10, pady=10)

                            lab1 = Label(root1, text="Experience Type:", font=d).grid(row=4, column=0, padx=10, pady=10)
                            en1 = Entry(root1)
                            en1.grid(row=4, column=1, padx=10, pady=10)
                            lab2 = Label(root1, text="Institution/Company:", font=d).grid(row=4, column=2, padx=10,
                                                                                       pady=10)
                            en2 = Entry(root1)
                            en2.grid(row=4, column=3, padx=10, pady=10)
                            lab3 = Label(root1, text="Address:", font=d).grid(row=4, column=4, padx=10, pady=10)
                            en3 = Entry(root1)
                            en3.grid(row=4, column=5, padx=10, pady=10)
                            lab4 = Label(root1, text="Designation:", font=d).grid(row=4, column=6, padx=10, pady=10)
                            en4 = Entry(root1)
                            en4.grid(row=4, column=7, padx=10, pady=10)
                            lab5 = Label(root1, text="Date of Joining:", font=d).grid(row=5, column=0, padx=10,
                                                                                          pady=10)
                            en5 = Entry(root1)
                            en5.grid(row=5, column=1, padx=10, pady=10)
                            lab6 = Label(root1, text="Date of release:", font=d).grid(row=5, column=2, padx=10, pady=10)
                            en6 = Entry(root1)
                            en6.grid(row=5, column=3, padx=10, pady=10)
                            lab7 = Label(root1, text="Salary:", font=d).grid(row=5, column=4, padx=10, pady=10)
                            en7 = Entry(root1)
                            en7.grid(row=5, column=5, padx=10, pady=10)
                            lab8 = Label(root1, text="Remarks:", font=d).grid(row=5, column=6, padx=10, pady=10)
                            en8 = Entry(root1)
                            en8.grid(row=5, column=7, padx=10, pady=10)
                            mycursor.execute("select * from table3 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                aa = str(a[5]).split('-')
                                bb = ''
                                bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                                aaa = str(a[6]).split('-')
                                bbb = ''
                                bbb = aaa[-1] + '-' + aaa[-2] + '-' + aaa[-3]
                                b = a[1] + '||' + a[2] + '||' + a[3] + '||' + a[4] + '||' + bb + "||" + bbb + "||" + str(a[7]) + "||" + a[8] + "||" + a[9]
                                listbox.insert(END, b)
                            bu1 = Button(root1, text="OK", command=ok)
                            bu1.grid(row=3, column=2, padx=10, pady=10)
                            bu2 = Button(root1, text="Edit Document Upload", command=docupload1)
                            bu2.grid(row=6, column=6, padx=10, pady=10)
                            bu3 = Button(root1, text="Submit Changes", command=subedit6)
                            bu3.grid(row=7, column=2, padx=10, pady=10)
                            root1.mainloop()
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Edited without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def edit7():
                    if loginus == E00.get() or loginus == "admin":
                        try:
                            def ok():
                                global filename11
                                x = listbox.get(ANCHOR)
                                listbox.delete(ANCHOR)
                                c = x.split("||")
                                en1.config(state="normal")
                                en1.delete(0,END)
                                en1.insert(0,int(c[0]))
                                en1.config(state="readonly")
                                en2.delete(0,END)
                                en2.insert(0,float(c[1]))
                                en3.delete(0, END)
                                en3.insert(0, float(c[2]))
                                en4.delete(0, END)
                                en4.insert(0, float(c[3]))
                                en5.delete(0, END)
                                en5.insert(0,float(c[4]))
                                en6.delete(0, END)
                                en6.insert(0,float(c[5]))
                                en7.delete(0,END)
                                en7.insert(0,float(c[6]))
                                filename11 = c[7]

                            def docupload1():
                                try:
                                    global filename11
                                    global filex11
                                    file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                                    filex11 = file1.name
                                    f, ext = os.path.splitext(filex11)
                                    if os.path.getsize(filex11) <= 55000:
                                        del file1
                                        a = E00.get() + '_' +'leaveallot'+'_'+ str(en1.get())
                                        filename11 = a + ext
                                        tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')
                                        root1.deiconify()

                                    else:
                                        tkinter.messagebox.showinfo('Uploading Error!!',
                                                                    'Your Uploading Image must be below 50KB')
                                        root1.deiconify()
                                except AttributeError:
                                    tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')
                                    root1.deiconify()

                            def subedit7():
                                global filex11
                                global filename11
                                try:
                                    mycursor.execute("UPDATE TABLE5 SET CL=%s,ML=%s,EL=%s,SL=%s,OD=%s,OTHER=%s,LEAVEFILE=%s WHERE(EMPCODE=%s AND YOL=%s) ",(en2.get(),en3.get(),en4.get(),en5.get(),en6.get(),en7.get(),filename11, E00.get(),en1.get(),))
                                    mydb.commit()
                                    listbox.delete(0, END)
                                    mycursor.execute("select * from table5 where EMPCODE=%s", (E00.get(),))
                                    myresult = mycursor.fetchall()
                                    for rows in myresult:
                                        a = rows
                                        b = str(a[1]) + '||' + str(a[2]) + '||' + str(a[3]) + '||' + str(a[4]) + '||' + str(a[5]) + "||" + str(a[6]) + "||" + str(a[7]) + "||" + str(a[8])
                                        listbox.insert(END, b)
                                    shutil.copy(filex11, folname + '/' + filename11)
                                    filename11 = "No Doc. Uploaded"
                                    tkinter.messagebox.showinfo('Confirmation', 'New data successfully edited.')
                                    root1.deiconify()

                                except AttributeError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                                except MySQLdb.IntegrityError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.',
                                                                'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                                except NameError:
                                    tkinter.messagebox.showinfo('Error!!',
                                                                'Please Enter all the details and upload the file to submit')
                                    root1.deiconify()

                                except FileNotFoundError:
                                    tkinter.messagebox.showinfo('Confirmation!!', 'Response Edited Successfully')
                                    root1.deiconify()
                                except MySQLdb._exceptions.OperationalError:
                                    tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                                    root1.deiconify()
                            d = Font(family="Arial", size=13, weight="bold", slant="roman", underline=0)
                            root1 = Tk()
                            root1.geometry("1200x500")
                            root1.title("Edit")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=100)
                            listbox.grid(row=0, columnspan=4, padx=10, pady=10)

                            lab1 = Label(root1, text="Year:", font=d).grid(row=4, column=0, padx=10, pady=10)
                            en1 = Entry(root1)
                            en1.grid(row=4, column=1, padx=10, pady=10)
                            en1.config(state="readonly")
                            lab2 = Label(root1, text="CL:", font=d).grid(row=4, column=2, padx=10,pady=10)
                            en2 = Entry(root1)
                            en2.grid(row=4, column=3, padx=10, pady=10)
                            lab3 = Label(root1, text="ML:", font=d).grid(row=4, column=4, padx=10, pady=10)
                            en3 = Entry(root1)
                            en3.grid(row=4, column=5, padx=10, pady=10)
                            lab4 = Label(root1, text="EL:", font=d).grid(row=4, column=6, padx=10, pady=10)
                            en4 = Entry(root1)
                            en4.grid(row=4, column=7, padx=10, pady=10)
                            lab5 = Label(root1, text="SL:", font=d).grid(row=5, column=0, padx=10,pady=10)
                            en5 = Entry(root1)
                            en5.grid(row=5, column=1, padx=10, pady=10)
                            lab6 = Label(root1, text="OD:", font=d).grid(row=5, column=2, padx=10, pady=10)
                            en6 = Entry(root1)
                            en6.grid(row=5, column=3, padx=10, pady=10)
                            lab7 = Label(root1, text="Others:", font=d).grid(row=5, column=4, padx=10, pady=10)
                            en7 = Entry(root1)
                            en7.grid(row=5, column=5, padx=10, pady=10)

                            mycursor.execute("select * from table5 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                b = str(a[1]) + '||' + str(a[2]) + '||' + str(a[3]) + '||' + str(a[4]) + '||' + str(a[5]) + "||" + str(a[6]) + "||" + str(a[7]) + "||" + str(a[8])
                                listbox.insert(END, b)
                            bu1 = Button(root1, text="OK", command=ok)
                            bu1.grid(row=3, column=2, padx=10, pady=10)
                            bu2 = Button(root1, text="Edit Document Upload", command=docupload1)
                            bu2.grid(row=6, column=5, padx=10, pady=10)
                            bu3 = Button(root1, text="Submit Changes", command=subedit7)
                            bu3.grid(row=7, column=2, padx=10, pady=10)
                            root1.mainloop()

                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Edited without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def edit8():
                    if loginus == E00.get() or loginus == "admin":
                        try:
                            def ok():
                                global filename11
                                x = listbox.get(ANCHOR)
                                listbox.delete(ANCHOR)
                                c = x.split("||")
                                en1.config(state="normal")
                                en1.delete(0, END)
                                en1.insert(0, c[0])
                                en1.config(state="readonly")
                                en2.delete(0, END)
                                en2.insert(0, c[1])
                                filename11 = c[2]
                            def docupload1():
                                try:
                                    global filename11
                                    global filex11
                                    file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                                    filex11 = file1.name
                                    f, ext = os.path.splitext(filex11)
                                    if os.path.getsize(filex11) <= 55000:
                                        del file1
                                        a = E00.get() + '_' +'reward_penalty'+'_'+ str(en1.get())
                                        filename11 = a + ext
                                        tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')
                                        root1.deiconify()

                                    else:
                                        tkinter.messagebox.showinfo('Uploading Error!!',
                                                                    'Your Uploading Image must be below 50KB')
                                        root1.deiconify()
                                except AttributeError:
                                    tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')
                                    root1.deiconify()
                            def subedit7():
                                global filex11
                                global filename11
                                try:
                                    aa = str(en1.get()).split('-')
                                    bb = ''
                                    bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                                    mycursor.execute("UPDATE TABLE6 SET DESCR=%s,REWARDFILE=%s WHERE EMPCODE=%s AND DORP=%s ",(en2.get(), filename11, E00.get(), bb,))
                                    mydb.commit()
                                    listbox.delete(0, END)
                                    mycursor.execute("select * from table6 where EMPCODE=%s", (E00.get(),))
                                    myresult = mycursor.fetchall()
                                    for rows in myresult:
                                        a = rows
                                        aa = str(a[1]).split('-')
                                        bb = ''
                                        bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                                        b = bb + '||' + str(a[2]) + '||' + str(a[3])
                                        listbox.insert(END, b)
                                    shutil.copy(filex11, folname + '/' + filename11)
                                    filename11 = "No Doc. Uploaded"
                                    tkinter.messagebox.showinfo('Confirmation', 'New data successfully edited.')
                                    root1.deiconify()

                                except AttributeError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                                except MySQLdb.IntegrityError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.',
                                                                'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                                except NameError:
                                    tkinter.messagebox.showinfo('Error!!',
                                                                'Please Enter all the details and upload the file to submit')
                                    root1.deiconify()

                                except FileNotFoundError:
                                    tkinter.messagebox.showinfo('Confirmation!!', 'Response Edited Successfully')
                                    root1.deiconify()
                                except MySQLdb._exceptions.OperationalError:
                                    tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                                    root1.deiconify()

                            d = Font(family="Arial", size=13, weight="bold", slant="roman", underline=0)
                            root1 = Tk()
                            root1.geometry("1200x500")
                            root1.title("Edit")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=100)
                            listbox.grid(row=0, columnspan=4, padx=10, pady=10)

                            lab1 = Label(root1, text="Date:", font=d).grid(row=4, column=0, padx=10, pady=10)
                            en1 = Entry(root1)
                            en1.grid(row=4, column=1, padx=10, pady=10)
                            en1.config(state="readonly")
                            lab2 = Label(root1, text="Description:", font=d).grid(row=4, column=2, padx=10, pady=10)
                            en2 = Entry(root1,width=50)
                            en2.grid(row=4, column=3, padx=10, pady=10)

                            mycursor.execute("select * from table6 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                aa = str(a[1]).split('-')
                                bb = ''
                                bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                                b = bb + '||' + str(a[2]) + '||' + str(a[3])
                                listbox.insert(END, b)
                            bu1 = Button(root1, text="OK", command=ok)
                            bu1.grid(row=3, column=2, padx=10, pady=10)
                            bu2 = Button(root1, text="Edit Document Upload", command=docupload1)
                            bu2.grid(row=5, column=5, padx=10, pady=10)
                            bu3 = Button(root1, text="Submit Changes", command=subedit7)
                            bu3.grid(row=6, column=2, padx=10, pady=10)
                            root1.mainloop()

                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Edited without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def edit9():
                    #mycursor.execute("UPDATE TABLE7 SET BASIC=%s,DA=%s,HRA=%s,OTHER=%s,PAYSCALEFILE=%s WHERE EMPCODE=%s AND YOPAY=%s",(str(E44.get()), str(E45.get()), str(E46.get()), str(E47.get()), filename8, E00.get(),payyear.get(),))
                    if loginus == E00.get() or loginus == "admin":
                        try:
                            def ok():
                                global filename11
                                x = listbox.get(ANCHOR)
                                listbox.delete(ANCHOR)
                                c = x.split("||")
                                en1.config(state="normal")
                                en1.delete(0,END)
                                en1.insert(0,c[0])
                                en1.config(state="readonly")
                                en2.delete(0,END)
                                en2.insert(0,float(c[1]))
                                en3.delete(0, END)
                                en3.insert(0, float(c[2]))
                                en4.delete(0, END)
                                en4.insert(0, float(c[3]))
                                en5.delete(0, END)
                                en5.insert(0,float(c[4]))
                                filename11 = c[5]
                            def docupload1():
                                try:
                                    global filename11
                                    global filex11
                                    file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                                    filex11 = file1.name
                                    f, ext = os.path.splitext(filex11)
                                    if os.path.getsize(filex11) <= 55000:
                                        del file1
                                        a = E00.get() + '_' +'reward_penalty'+'_'+ str(en1.get())
                                        filename11 = a + ext
                                        tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')
                                        root1.deiconify()

                                    else:
                                        tkinter.messagebox.showinfo('Uploading Error!!',
                                                                    'Your Uploading Image must be below 50KB')
                                        root1.deiconify()
                                except AttributeError:
                                    tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')
                                    root1.deiconify()
                            def subedit7():
                                global filex11
                                global filename11
                                try:
                                    aa = str(en1.get()).split('-')
                                    bb = ''
                                    bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                                    mycursor.execute("UPDATE TABLE7 SET BASIC=%s,DA=%s,HRA=%s,OTHER=%s,PAYSCALEFILE=%s WHERE EMPCODE=%s AND DOPAY=%s",(str(en2.get()), str(en3.get()), str(en4.get()), str(en5.get()), filename11, E00.get(),bb,))
                                    mydb.commit()
                                    listbox.delete(0, END)
                                    mycursor.execute("select * from table7 where EMPCODE=%s", (E00.get(),))
                                    myresult = mycursor.fetchall()
                                    for rows in myresult:
                                        a = rows
                                        aa = str(a[1]).split('-')
                                        bb = ''
                                        bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                                        b = bb + '||' + str(a[2]) + '||' + str(a[3]) + '||' + str(a[4]) + '||' + str(a[5]) + "||" + str(a[6])
                                        listbox.insert(END, b)
                                    shutil.copy(filex11, folname + '/' + filename11)
                                    filename11 = "No Doc. Uploaded"
                                    tkinter.messagebox.showinfo('Confirmation', 'New data successfully edited.')
                                    root1.deiconify()

                                except AttributeError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                                except MySQLdb.IntegrityError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.','Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                                except NameError:
                                    tkinter.messagebox.showinfo('Error!!','Please Enter all the details and upload the file to submit')
                                    root1.deiconify()
                                except FileNotFoundError:
                                    tkinter.messagebox.showinfo('Confirmation!!', 'Response Edited Successfully')
                                    root1.deiconify()
                                except MySQLdb._exceptions.OperationalError:
                                    tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                                    root1.deiconify()

                            d = Font(family="Arial", size=13, weight="bold", slant="roman", underline=0)
                            root1 = Tk()
                            root1.geometry("1200x500")
                            root1.title("Edit")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=100)
                            listbox.grid(row=0, columnspan=4, padx=10, pady=10)

                            lab1 = Label(root1, text="Year of pay:", font=d).grid(row=4, column=0, padx=10, pady=10)
                            en1 = Entry(root1)
                            en1.grid(row=4, column=1, padx=10, pady=10)
                            en1.config(state="readonly")
                            lab2 = Label(root1, text="BASIC:", font=d).grid(row=4, column=2, padx=10, pady=10)
                            en2 = Entry(root1)
                            en2.grid(row=4, column=3, padx=10, pady=10)
                            lab3 = Label(root1, text="DA:", font=d).grid(row=4, column=4, padx=10, pady=10)
                            en3 = Entry(root1)
                            en3.grid(row=4, column=5, padx=10, pady=10)
                            lab4 = Label(root1, text="HRA:", font=d).grid(row=4, column=6, padx=10, pady=10)
                            en4 = Entry(root1)
                            en4.grid(row=4, column=7, padx=10, pady=10)
                            lab5 = Label(root1, text="OTHERS:", font=d).grid(row=5, column=0, padx=10, pady=10)
                            en5 = Entry(root1)
                            en5.grid(row=5, column=1, padx=10, pady=10)

                            mycursor.execute("select * from table7 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                aa = str(a[1]).split('-')
                                bb = ''
                                bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                                b = bb + '||' + str(a[2]) + '||' + str(a[3]) + '||' + str(a[4]) + '||' + str(a[5]) + "||"+ str(a[6])
                                listbox.insert(END, b)
                            bu1 = Button(root1, text="OK", command=ok)
                            bu1.grid(row=3, column=2, padx=10, pady=10)
                            bu2 = Button(root1, text="Edit Document Upload", command=docupload1)
                            bu2.grid(row=5, column=3, padx=10, pady=10)
                            bu3 = Button(root1, text="Submit Changes", command=subedit7)
                            bu3.grid(row=6, column=2, padx=10, pady=10)
                            root1.mainloop()

                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Edited without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def edit10():
                    if loginus == E00.get() or loginus == "admin":
                        try:
                            def ok():
                                global filename11
                                x = listbox.get(ANCHOR)
                                listbox.delete(ANCHOR)
                                c = x.split("||")
                                Co1.config(state="normal")
                                Co1.set(" ")
                                Co1.set(c[0])
                                Co1.config(state="disable")
                                en1.delete(0,END)
                                en1.insert(0,c[1])
                                en2.delete(0,END)
                                en2.insert(0,c[2])
                                Co2.set(" ")
                                Co2.set(c[3])
                                Co3.config(state="normal")
                                Co3.set(0)
                                Co3.set(int(c[4]))
                                Co3.config(state="disable")
                                filename11 = c[5]

                            def docupload1():
                                try:
                                    global filename11
                                    global filex11
                                    file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                                    filex11 = file1.name
                                    f, ext = os.path.splitext(filex11)
                                    if os.path.getsize(filex11) <= 55000:
                                        del file1
                                        a = E00.get() + '_' +'subjectallot'+'_'+ str(Co1.get()) +"_"+ str(Co3.get())
                                        filename11 = a + ext
                                        tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')
                                        root1.deiconify()

                                    else:
                                        tkinter.messagebox.showinfo('Uploading Error!!',
                                                                    'Your Uploading Image must be below 50KB')
                                        root1.deiconify()
                                except AttributeError:
                                    tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')
                                    root1.deiconify()

                            def subedit7():
                                global filex11
                                global filename11
                                try:
                                    mycursor.execute("UPDATE TABLE8 SET PAPERCODE=%s,PAPERNAME=%s,DEPARTMENT=%s,SUBJECTALLOTFILE=%s WHERE (EMPCODE=%s AND SEM=%s AND YOA=%s)  ",(en1.get(), en2.get(), Co2.get(), filename11, E00.get(), Co1.get(), Co3.get(),))
                                    mydb.commit()
                                    listbox.delete(0, END)
                                    mycursor.execute("select * from table8 where EMPCODE=%s", (E00.get(),))
                                    myresult = mycursor.fetchall()
                                    for rows in myresult:
                                        a = rows
                                        b = str(a[1]) + '||' + str(a[2]) + '||' + str(a[3]) + '||' + str(a[4]) + '||' + str(a[5]) + "||" + str(a[6])
                                        listbox.insert(END, b)
                                    shutil.copy(filex11, folname + '/' + filename11)
                                    filename11 = "No Doc. Uploaded"
                                    tkinter.messagebox.showinfo('Confirmation', 'New data successfully edited.')
                                    root1.deiconify()

                                except AttributeError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                                except MySQLdb.IntegrityError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.','Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                                except NameError:
                                    tkinter.messagebox.showinfo('Error!!','Please Enter all the details and upload the file to submit')
                                    root1.deiconify()
                                except FileNotFoundError:
                                    tkinter.messagebox.showinfo('Confirmation!!', 'Response Edited Successfully')
                                    root1.deiconify()
                                except MySQLdb._exceptions.OperationalError:
                                    tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                                    root1.deiconify()

                            d = Font(family="Arial", size=13, weight="bold", slant="roman", underline=0)
                            root1 = Tk()
                            list2 = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
                                  2015, 2016,
                                  2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030,
                                  2031, 2032,
                                  2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040]
                            list1 = ["1st Sem", "2nd Sem", "3rd Sem", "4th Sem", "5th Sem", "6th Sem", "7th Sem",
                                  "8th Sem"]
                            list3 = ["CSE", "IT", "EE", "ME", "ECE", "CHE"]
                            root1.geometry("1000x500")
                            root1.title("Edit")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=100)
                            listbox.grid(row=0, columnspan=4, padx=10, pady=10)

                            lab1 = Label(root1, text="Semester:", font=d).grid(row=4, column=0, padx=10, pady=10)
                            Co1 = Combobox(root1, values=list1, height=4)
                            Co1.grid(row=4, column=1, padx=10, pady=10)
                            Co1.config(state="disable")
                            lab2 = Label(root1, text="Paper Code:", font=d).grid(row=4, column=2, padx=10, pady=10)
                            en1=Entry(root1)
                            en1.grid(row=4, column=3, padx=10, pady=10)
                            lab3 = Label(root1, text="Paper name:", font=d).grid(row=4, column=4, padx=10, pady=10)
                            en2=Entry(root1)
                            en2.grid(row=4, column=5, padx=10, pady=10)
                            lab4 = Label(root1, text="Department:", font=d).grid(row=5, column=0, padx=10,pady=10)
                            Co2 = Combobox(root1, values=list3, height=4)
                            Co2.grid(row=5, column=1, padx=10, pady=10)
                            lab5 = Label(root1, text="Year:", font=d).grid(row=5, column=2, padx=10, pady=10)
                            Co3 = Combobox(root1, values=list2, height=4)
                            Co3.grid(row=5, column=3, padx=10, pady=10)
                            Co3.config(state="disable")
                            mycursor.execute("select * from table8 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                b = a[1] + '||' + a[2] + '||' + a[3] + '||' + a[4] + '||' + str(a[5]) + "||" + a[6]
                                listbox.insert(END, b)
                            bu1 = Button(root1, text="OK", command=ok)
                            bu1.grid(row=3, column=2, padx=10, pady=10)
                            bu2 = Button(root1, text="Edit Document Upload", command=docupload1)
                            bu2.grid(row=5, column=4, padx=10, pady=10)
                            bu3 = Button(root1, text="Submit Changes", command=subedit7)
                            bu3.grid(row=6, column=2, padx=10, pady=10)
                            root1.mainloop()

                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Edited without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def edit11():

                    if loginus == E00.get() or loginus == "admin":
                        try:
                            def ok():
                                global filename11
                                x = listbox.get(ANCHOR)
                                listbox.delete(ANCHOR)
                                c = x.split("||")
                                en1.config(state="normal")
                                en1.delete(0,END)
                                en1.insert(0,c[0])
                                en1.config(state="readonly")
                                en2.delete(0,END)
                                en2.insert(0,c[1])
                                en3.delete(0, END)
                                en3.insert(0, c[2])
                                filename11 = c[3]
                            def docupload1():
                                try:
                                    global filename11
                                    global filex11
                                    file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                                    filex11 = file1.name
                                    f, ext = os.path.splitext(filex11)
                                    if os.path.getsize(filex11) <= 55000:
                                        del file1
                                        a = E00.get() + '_' +'addresp'+'_'+ str(en1.get())
                                        filename11 = a + ext
                                        tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')
                                        root1.deiconify()

                                    else:
                                        tkinter.messagebox.showinfo('Uploading Error!!',
                                                                    'Your Uploading Image must be below 50KB')
                                        root1.deiconify()
                                except AttributeError:
                                    tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')
                                    root1.deiconify()

                            def subedit7():
                                global filex11
                                global filename11
                                try:
                                    aa = str(en1.get()).split('-')
                                    bb = ''
                                    bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                                    aaa = str(en2.get()).split('-')
                                    bbb = ''
                                    bbb = aaa[-1] + '-' + aaa[-2] + '-' + aaa[-3]
                                    mycursor.execute("UPDATE TABLE9 SET TODATE=%s,DESCR=%s,ADDRESPFILE=%s WHERE EMPCODE=%s AND FROMDATE=%s ",(bbb, en3.get(), filename11, E00.get(), bb,))
                                    mydb.commit()
                                    listbox.delete(0, END)
                                    mycursor.execute("select * from table9 where EMPCODE=%s", (E00.get(),))
                                    myresult = mycursor.fetchall()
                                    for rows in myresult:
                                        a = rows
                                        aa = str(a[1]).split('-')
                                        bb = ''
                                        bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                                        aaa = str(a[2]).split('-')
                                        bbb = ''
                                        bbb = aaa[-1] + '-' + aaa[-2] + '-' + aaa[-3]
                                        b = bb + '||' + bbb + '||' + str(a[3]) + '||' + str(a[4])
                                        listbox.insert(END, b)
                                    shutil.copy(filex11, folname + '/' + filename11)
                                    filename11 = "No Doc. Uploaded"
                                    tkinter.messagebox.showinfo('Confirmation', 'New data successfully edited.')
                                    root1.deiconify()

                                except AttributeError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                                except MySQLdb.IntegrityError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.','Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                                except NameError:
                                    tkinter.messagebox.showinfo('Error!!','Please Enter all the details and upload the file to submit')
                                    root1.deiconify()
                                except FileNotFoundError:
                                    tkinter.messagebox.showinfo('Confirmation!!', 'Response Edited Successfully')
                                    root1.deiconify()
                                except MySQLdb._exceptions.OperationalError:
                                    tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                                    root1.deiconify()
                            d = Font(family="Arial", size=13, weight="bold", slant="roman", underline=0)
                            root1 = Tk()
                            root1.geometry("1200x500")
                            root1.title("Edit")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=100)
                            listbox.grid(row=0, columnspan=4, padx=10, pady=10)

                            lab1 = Label(root1, text="From Date:", font=d).grid(row=4, column=0, padx=10, pady=10)
                            en1 = Entry(root1)
                            en1.grid(row=4, column=1, padx=10, pady=10)
                            en1.config(state="readonly")
                            lab2 = Label(root1, text="To Date:", font=d).grid(row=4, column=2, padx=10, pady=10)
                            en2 = Entry(root1)
                            en2.grid(row=4, column=3, padx=10, pady=10)
                            lab3 = Label(root1, text="Description:", font=d).grid(row=4, column=4, padx=10, pady=10)
                            en3 = Entry(root1,width=40)
                            en3.grid(row=4, column=5, padx=10, pady=10)


                            mycursor.execute("select * from table9 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                aa = str(a[1]).split('-')
                                bb = ''
                                bb = aa[-1] + '-' + aa[-2] + '-' + aa[-3]
                                aaa = str(a[2]).split('-')
                                bbb = ''
                                bbb = aaa[-1] + '-' + aaa[-2] + '-' + aaa[-3]
                                b = bb + '||' + bbb + '||' + str(a[3]) + '||' + str(a[4])
                                listbox.insert(END, b)
                            bu1 = Button(root1, text="OK", command=ok)
                            bu1.grid(row=3, column=2, padx=10, pady=10)
                            bu2 = Button(root1, text="Edit Document Upload", command=docupload1)
                            bu2.grid(row=5, column=3, padx=10, pady=10)
                            bu3 = Button(root1, text="Submit Changes", command=subedit7)
                            bu3.grid(row=6, column=2, padx=10, pady=10)
                            root1.mainloop()

                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Edited without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')

                def edit12():
                    if loginus == E00.get() or loginus == "admin":
                        slno=" "
                        try:
                            def ok():
                                global filename11
                                global slno
                                x = listbox.get(ANCHOR)
                                listbox.delete(ANCHOR)
                                c = x.split("||")
                                slno=str(c[0])
                                text1.insert(2.0, c[1])
                                filename11 = c[2]
                            def subedit7():
                                global slno
                                global filex11
                                global filename11
                                try:
                                    mycursor.execute("UPDATE TABLE4 SET SPECIALACV=%s,SPECIALFILE=%s where EMPCODE=%s and SLNO=%s",
                                                    (text1.get('2.0', END), filename11,E00.get(),slno,))
                                    mydb.commit()
                                    text1.delete(0.0, END)
                                    mycursor.execute("select * from table4 where EMPCODE=%s and SLNO=%s", (E00.get(),slno,))
                                    myresult = mycursor.fetchall()
                                    text1.insert(0.0, "---------Special Achievements----------\n")
                                    for rows in myresult:
                                        text1.insert(2.0,str(rows[2]))

                                    shutil.copy(filex11, folname + '/' + filename11)
                                    filename11 = "No Doc. Uploaded"
                                    tkinter.messagebox.showinfo('Confirmation', 'New data successfully edited.')
                                    root1.deiconify()

                                except AttributeError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                                except MySQLdb.IntegrityError:
                                    tkinter.messagebox.showinfo('Connectivity Problem.',
                                                            'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                                except NameError:
                                    tkinter.messagebox.showinfo('Error!!',
                                                            'Please Enter all the details and upload the file to submit')
                                    root1.deiconify()
                                except FileNotFoundError:
                                    tkinter.messagebox.showinfo('Confirmation!!', 'Response Edited Successfully')
                                    root1.deiconify()
                                except MySQLdb._exceptions.OperationalError:
                                    tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                                    root1.deiconify()

                            def docupload1():
                                try:
                                    global filename11
                                    global filex11
                                    file1 = filedialog.askopenfile(filetype=(("jpeg", "*.jpg"), ("pdf", "*.pdf")))
                                    filex11 = file1.name
                                    f, ext = os.path.splitext(filex11)
                                    if os.path.getsize(filex11) <= 55000:
                                        del file1
                                        a = E00.get() + '_' +'Special'
                                        filename11 = a + ext
                                        tkinter.messagebox.showinfo('Confirmation!!', 'File uploaded successfully')
                                        root1.deiconify()

                                    else:
                                        tkinter.messagebox.showinfo('Uploading Error!!',
                                                                    'Your Uploading Image must be below 50KB')
                                        root1.deiconify()
                                except AttributeError:
                                    tkinter.messagebox.showinfo('Uploading Error', 'No file Uploaded.')
                                    root1.deiconify()


                            d = Font(family="Arial", size=13, weight="bold", slant="roman", underline=0)
                            root1 = Tk()
                            root1.geometry("1200x500")
                            root1.title("Edit")
                            root1.iconbitmap(r'diatmlogo.ico')
                            lab1 = Label(root1, text="Please Update here and submit.", font=d).grid(row=0, column=0, padx=10, pady=10)
                            listbox = Listbox(root1, width=100)
                            listbox.grid(row=0, columnspan=4, padx=10, pady=10)
                            text1 = Text(root1, width=97, height=5, wrap=WORD, padx=10, pady=10, bd=1)
                            text1.grid(row=4, column=0, padx=10, pady=10, sticky='WN')
                            text1.insert(0.0, "---------Special Achievements----------\n")

                            mycursor.execute("select * from table4 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                b = str(a[1]) + '||' + a[2] + '||' +a[3]
                                listbox.insert(END, b)
                            bu1 = Button(root1, text="OK", command=ok)
                            bu1.grid(row=3, column=0, padx=10, pady=10)
                            bu2 = Button(root1, text="Edit Document Upload", command=docupload1)
                            bu2.grid(row=5, column=0, padx=20, pady=20)
                            bu3 = Button(root1, text="Submit Changes", command=subedit7)
                            bu3.grid(row=6, column=0, padx=20, pady=20)
                            root1.mainloop()
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')
                        except NameError:
                            tkinter.messagebox.showinfo('Error!!',
                                                        'Please Enter all the details and upload the file to submit')
                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Confirmation!!',
                                                        'Response Successfully Edited without Document upload / Insufficient data.!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')

                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')


                def header(canvas, doc):
                    styles = getSampleStyleSheet()
                    c1 = canvas
                    width, height = letter
                    nd = styles['Normal']
                    header = "<b><u>" + E00.get() + " " + title + "</u></b>"
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    footer = "Last updated :" + dt_string
                    p = Paragraph(header, nd)
                    p.wrapOn(c1, width, height)
                    p.drawOn(c1, 40, 780)
                    p = Paragraph(footer, nd)
                    p.wrapOn(c1, width, height)
                    p.drawOn(c1, 350, 30)

                def download_file1():
                    global foldername
                    if loginus == E00.get() or loginus == "admin":
                        try:
                            a = []
                            mycursor.execute("select * from table1 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                            filename = folname + '/' + "Report1.pdf"
                            c = canvas.Canvas(filename, pagesize=letter)
                            c.setFont('Helvetica', 22, leading=None)
                            c.drawString(160, 735, "Employee Information Report")
                            c.setFont('Helvetica', 12, leading=None)
                            c.drawString(45, 690, "Name:")
                            c.drawString(85, 690, a[1] + ' ' + a[2] + ' ' + a[3])
                            c.drawString(45, 660, "Date of Birth:")
                            b = str(a[4]).split('-')
                            bb = b[-1] + '-' + b[-2] + '-' + b[-3]
                            c.drawString(120, 660, bb)
                            c.drawString(45, 630, 'Religion:')
                            c.drawString(95, 630, a[5])
                            c.drawString(45, 600, 'Gender:')
                            c.drawString(95, 600, a[6])
                            c.drawString(45, 570, 'Caste:')
                            c.drawString(85, 570, a[7])
                            c.drawString(45, 540, 'Blood Group:')
                            c.drawString(120, 540, a[8])
                            c.setFont('Helvetica', 14, leading=None)
                            c.drawString(45, 500, "Present Address :-")
                            c.setFont('Helvetica', 12, leading=None)
                            c.drawString(45, 470, "Address:")
                            c.drawString(95, 470, a[9])
                            c.drawString(95, 440, a[10] + ' ' + a[11] + ' ' + str(a[12]))
                            c.setFont('Helvetica', 14, leading=None)
                            c.drawString(45, 400, "Permanent Address :-")
                            c.setFont('Helvetica', 12, leading=None)
                            c.drawString(45, 370, "Address:")
                            c.drawString(95, 370, a[13])
                            c.drawString(95, 340, a[14] + ' ' + a[15] + ' ' + str(a[16]))
                            c.setFont('Helvetica', 14, leading=None)
                            c.drawString(45, 300, "Contact Details :-")
                            c.setFont('Helvetica', 12, leading=None)
                            c.drawString(45, 270, "Mobile No.:")
                            c.drawString(110, 270, str(a[17]))
                            c.drawString(210, 270, "Alternative Mobile No.:")
                            c.drawString(340, 270, str(a[18]))
                            c.drawString(45, 240, "Email:")
                            c.drawString(85, 240, a[19])
                            photo1 = folname + '/' + a[20]
                            c.drawImage(photo1, 450, 610, width=100, height=100)
                            photo2 = folname + '/' + a[21]
                            c.drawImage(photo2, 450, 540, width=100, height=50)
                            c.setFont('Helvetica', 14, leading=None)
                            c.drawString(45, 200, "Banking details :-")
                            c.setFont('Helvetica', 12, leading=None)
                            mycursor.execute("select * from table11 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                if a[5]!="No Doc. Uploaded":
                                    c.drawString(45, 170, "Account No. :")
                                    c.drawString(120, 170, a[1])
                                    c.drawString(45, 140, "Bank Name:")
                                    c.drawString(120, 140, a[2])
                                    c.drawString(45, 110, "Branch Code:")
                                    c.drawString(120, 110, a[3])
                                    c.drawString(45, 80, "IFSC Code:")
                                    c.drawString(120, 80, a[4])
                                    b=(str(folname)+"/"+a[5])
                                    c.drawImage(b,450,140,width=100,height=120)
                                else:
                                    c.drawString(45, 170, "Account No. :")
                                    c.drawString(120, 170, a[1])
                                    c.drawString(45, 140, "Bank Name:")
                                    c.drawString(120, 140, a[2])
                                    c.drawString(45, 110, "Branch Code:")
                                    c.drawString(120, 110, a[3])
                                    c.drawString(45, 80, "IFSC Code:")
                                    c.drawString(120, 80, a[4])
                                    b = "NO BANK DOCUMENTS\nUPLOADED"
                                    c.drawString(450, 80, b)

                            c.save()
                            # -----------------------------------------------------------------------
                            global title
                            title = "Legal information Details"
                            elements = []
                            doc = SimpleDocTemplate(folname + '/' + "Report10.pdf")
                            data = [['                Document Name              ', '             Doucument ID            ','              Uploaded Doc.         ']]
                            mycursor.execute("select * from table10 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                if rows[3]!="No Doc. Uploaded":
                                    a=(str(folname)+"/"+rows[3])
                                    data2 = [rows[1], rows[2],Image(a,width=100,height=100)]
                                    data.append(data2)
                                else:
                                    a = "NO DOCUMENTS\nUPLOADED"
                                    data2 = [rows[1], rows[2], a]
                                    data.append(data2)
                            f = Table(data)
                            f.setStyle(TableStyle(
                                [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                 ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
                            elements.append(f)
                            doc.build(elements, onFirstPage=header)
                            # ------------------------------------------------------------------------
                            title = "Institution joining Details"
                            elements = []
                            doc = SimpleDocTemplate(folname + '/' + "Report11.pdf")
                            data = [['Course type', 'Department', 'Designation', 'Subject Specialization',
                                     'Date of joining','Uploaded Doc.']]
                            mycursor.execute("select * from table12 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                if rows[6]!="No Doc. Uploaded":
                                    a=(str(folname)+"/"+rows[6])
                                    b = str(rows[5]).split('-')
                                    bb = b[-1] + '-' + b[-2] + '-' + b[-3]
                                    data2 = [rows[1][:30] + '\n' + rows[1][30:],
                                             rows[2][:20] + '\n' + rows[2][20:40] + '\n' + rows[2][40:], rows[3],
                                             rows[4][:20] + '\n' + rows[4][20:40] + '\n' + rows[4][40:], bb,Image(a,width=100,height=100)]
                                    data.append(data2)
                                else:
                                    a = "NO DOCUMENTS\nUPLOADED"
                                    b = str(rows[5]).split('-')
                                    bb = b[-1] + '-' + b[-2] + '-' + b[-3]
                                    data2 = [rows[1][:30] + '\n' + rows[1][30:],
                                             rows[2][:20] + '\n' + rows[2][20:40] + '\n' + rows[2][40:], rows[3],
                                             rows[4][:20] + '\n' + rows[4][20:40] + '\n' + rows[4][40:], bb,a]
                                    data.append(data2)

                            f = Table(data)
                            f.setStyle(TableStyle(
                                [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                 ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
                            elements.append(f)
                            doc.build(elements, onFirstPage=header)

                            # ---------------------------------------------------------------------
                            title = "Academic Details"
                            elements = []
                            doc = SimpleDocTemplate(folname + '/' + "Report2.pdf")
                            data = [
                                ['Degree\nObtained', 'Description', 'University/Board', 'Institution', 'Year\nof\nPassout',
                                 'Marks\nin\npercent','Uploaded Doc.']]
                            mycursor.execute("select * from table2 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                if rows[8] != "No Doc. Uploaded":
                                    a = (str(folname) + "/" + rows[8])
                                    b = str(rows[5]).split('-')
                                    bb = b[-1] + '-' + b[-2] + '-' + b[-3]
                                    data2 = [rows[1], rows[2][:20] + '\n' + rows[2][20:40] + '\n' + rows[2][40:],
                                             rows[3][:20] + '\n' + rows[3][20:40] + '\n' + rows[3][40:],
                                             rows[4][:20] + '\n' + rows[4][20:40] + '\n' + rows[4][40:], bb, str(rows[6]),Image(a,width=100,height=100)]
                                    data.append(data2)
                                else:
                                    a = "NO DOCUMENTS\nUPLOADED"
                                    b = str(rows[5]).split('-')
                                    bb = b[-1] + '-' + b[-2] + '-' + b[-3]
                                    data2 = [rows[1], rows[2][:20] + '\n' + rows[2][20:40] + '\n' + rows[2][40:],
                                             rows[3][:20] + '\n' + rows[3][20:40] + '\n' + rows[3][40:],
                                             rows[4][:20] + '\n' + rows[4][20:40] + '\n' + rows[4][40:], bb,
                                             str(rows[6]), a]
                                    data.append(data2)
                            f = Table(data)
                            f.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                                   ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
                            elements.append(f)
                            doc.build(elements, onFirstPage=header)
                            # ----------------------------------------------------------------------
                            title = "Experience Details"
                            doc = SimpleDocTemplate(folname + '/' + "Report3.pdf")
                            data = [
                                ['Experience\ntype', 'Institute\n/Company', 'Address', 'Designation', 'Joining', 'Release',
                                 'Salary','Uploaded Doc.']]
                            mycursor.execute("select * from table3 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                if rows[9]!="No Doc. Uploaded":
                                    a = (str(folname) + "/" + rows[9])
                                    b = str(rows[5]).split('-')
                                    bb = b[-1] + '-' + b[-2] + '-' + b[-3]
                                    z = str(rows[6]).split('-')
                                    zz = z[-1] + '-' + z[-2] + '-' + z[-3]
                                    data2 = [rows[1][:12] + '\n' + rows[1][12:],
                                             rows[2][:20] + '\n' + rows[2][20:40] + '\n' + rows[2][40:],
                                             rows[3][:20] + '\n' + rows[3][20:40] + '\n' + rows[3][40:],
                                             rows[4][:12] + '\n' + rows[4][12:], bb, zz, str(rows[7]),Image(a,width=100,height=100)]
                                    data.append(data2)
                                else:
                                    a = "NO DOCUMENTS\nUPLOADED"
                                    b = str(rows[5]).split('-')
                                    bb = b[-1] + '-' + b[-2] + '-' + b[-3]
                                    z = str(rows[6]).split('-')
                                    zz = z[-1] + '-' + z[-2] + '-' + z[-3]
                                    data2 = [rows[1][:12] + '\n' + rows[1][12:],
                                             rows[2][:20] + '\n' + rows[2][20:40] + '\n' + rows[2][40:],
                                             rows[3][:20] + '\n' + rows[3][20:40] + '\n' + rows[3][40:],
                                             rows[4][:12] + '\n' + rows[4][12:], bb, zz, str(rows[7]),a]
                                    data.append(data2)
                            f = Table(data)
                            f.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                                   ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
                            elements.append(f)
                            doc.build(elements, onFirstPage=header)
                            # ------------------------------------------------------------------------
                            title = "Special Achievement Details"
                            doc = SimpleDocTemplate(folname + '/' + "Report4.pdf")
                            data = [['SL No.','Special Achievement','Uploaded Doc.']]
                            mycursor.execute("select * from table4 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                if rows[3]!="No Doc. Uploaded":
                                    a = (str(folname) + "/" + rows[2])
                                    data2 = [rows[1],rows[2],Image(a,width=100,height=100)]
                                    data.append(data2)
                                else:
                                    a = "NO DOCUMENTS\nUPLOADED"
                                    data2 = [rows[1],rows[2],a]
                                    data.append(data2)
                            f = Table(data)
                            f.setStyle(TableStyle(
                                [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                 ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
                            elements.append(f)
                            doc.build(elements, onFirstPage=header)
                            # ----------------------------------------------------------------------------
                            title = "Leave Details"
                            doc = SimpleDocTemplate(folname + '/' + "Report5.pdf")
                            data = [['Year of Leave', 'CL', 'ML', 'EL', 'SL', 'OD', 'Others','Uploaded Doc.']]
                            mycursor.execute("select * from table5 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                if rows[8]!="No Doc. Uploaded":
                                    a = (str(folname) + "/" + rows[8])
                                    data2 = [str(rows[1]), str(rows[2]), str(rows[3]), str(rows[4]), str(rows[5]),
                                             str(rows[6]), str(rows[7]),Image(a,width=100,height=100)]
                                    data.append(data2)
                                else:
                                    a = "NO DOCUMENTS\nUPLOADED"
                                    data2 = [str(rows[1]), str(rows[2]), str(rows[3]), str(rows[4]), str(rows[5]),
                                             str(rows[6]), str(rows[7]),a]
                                    data.append(data2)
                            f = Table(data)
                            f.setStyle(TableStyle(
                                [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                 ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
                            elements.append(f)
                            doc.build(elements, onFirstPage=header)
                            # ------------------------------------------------------------------------------
                            title = "Reward/Penalty Details"
                            doc = SimpleDocTemplate(folname + '/' + "Report6.pdf")
                            data = [['Date of Reward/Penalty', 'Description','Uploaded Doc.']]
                            mycursor.execute("select * from table6 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                if rows[3]!="No Doc. Uploaded":
                                    a = (str(folname) + "/" + rows[3])
                                    b = str(rows[1]).split('-')
                                    bb = b[-1] + '-' + b[-2] + '-' + b[-3]
                                    data2 = [bb, rows[2][:45] + '\n' + rows[2][45:80] + '\n' + rows[2][80:],Image(a,width=100,height=100)]
                                    data.append(data2)
                                else:
                                    a = "NO DOCUMENTS\nUPLOADED"
                                    b = str(rows[1]).split('-')
                                    bb = b[-1] + '-' + b[-2] + '-' + b[-3]
                                    data2 = [bb, rows[2][:20] + '\n' + rows[2][20:40] + '\n' + rows[2][40:],a]
                                    data.append(data2)
                            f = Table(data)
                            f.setStyle(TableStyle(
                                [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                 ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
                            elements.append(f)
                            doc.build(elements, onFirstPage=header)
                            # --------------------------------------------------------------------------------
                            title = "Pay Scale details"
                            doc = SimpleDocTemplate(folname + '/' + "Report7.pdf")
                            data = [['Year of Pay', 'Basic', 'DA', 'HRA', 'Others','Uploaded Doc.']]
                            mycursor.execute("select * from table7 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                if rows[6]!="No Doc. Uploaded":
                                    a = (str(folname) + "/" + rows[6])
                                    b = str(rows[1]).split('-')
                                    bb = b[-1] + '-' + b[-2] + '-' + b[-3]
                                    data2 = [bb, str(rows[2]), str(rows[3]), str(rows[4]), str(rows[5]),Image(a,width=100,height=100)]
                                    data.append(data2)
                                else:
                                    a = "NO DOCUMENTS\nUPLOADED"
                                    b = str(rows[1]).split('-')
                                    bb = b[-1] + '-' + b[-2] + '-' + b[-3]
                                    data2 = [bb, str(rows[2]), str(rows[3]), str(rows[4]), str(rows[5]),a]
                                    data.append(data2)
                            f = Table(data)
                            f.setStyle(TableStyle(
                                [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                 ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
                            elements.append(f)
                            doc.build(elements, onFirstPage=header)
                            # -------------------------------------------------------------------------------------
                            title = "Subject Allocation details"
                            doc = SimpleDocTemplate(folname + '/' + "Report8.pdf")
                            data = [['Semester', 'Paper code', 'Paper Name', 'Department', 'Year of Allocation','Uploaded Doc.']]
                            mycursor.execute("select * from table8 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                if rows[6]!="No Doc. Uploaded":
                                    a = (str(folname) + "/" + rows[6])
                                    data2 = [rows[1], rows[2], rows[3][:35] + '\n' + rows[3][35:],
                                             rows[4][:20] + '\n' + rows[4][20:40] + '\n' + rows[4][40:], str(rows[5]),Image(a,width=100,height=100)]
                                    data.append(data2)
                                else:
                                    a = "NO DOCUMENTS\nUPLOADED"
                                    data2 = [rows[1], rows[2], rows[3][:35] + '\n' + rows[3][35:],
                                             rows[4][:20] + '\n' + rows[4][20:40] + '\n' + rows[4][40:], str(rows[5]),a]
                                    data.append(data2)
                            f = Table(data)
                            f.setStyle(TableStyle(
                                [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                 ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
                            elements.append(f)
                            doc.build(elements, onFirstPage=header)
                            # --------------------------------------------------------------------------------------
                            title = "Additional Responsibility Details"
                            doc = SimpleDocTemplate(folname + '/' + "Report9.pdf")
                            data = [['From Date', 'To Date', 'Description','Uploaded Doc.']]
                            mycursor.execute("select * from table9 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                if rows[4]!="No Doc. Uploaded":
                                    a = (str(folname) + "/" + rows[4])
                                    b1 = str(rows[1]).split('-')
                                    bb1 = b1[-1] + '-' + b1[-2] + '-' + b1[-3]
                                    b2 = str(rows[2]).split('-')
                                    bb2 = b2[-1] + '-' + b2[-2] + '-' + b2[-3]
                                    data2 = [bb1, bb2, rows[3][:20] + '\n' + rows[3][20:40] + '\n' + rows[3][40:],Image(a,width=100,height=100)]
                                    data.append(data2)
                                else:
                                    a = "NO DOCUMENTS\nUPLOADED"
                                    b1 = str(rows[1]).split('-')
                                    bb1 = b1[-1] + '-' + b1[-2] + '-' + b1[-3]
                                    b2 = str(rows[2]).split('-')
                                    bb2 = b2[-1] + '-' + b2[-2] + '-' + b2[-3]
                                    data2 = [bb1, bb2, rows[3][:20] + '\n' + rows[3][20:40] + '\n' + rows[3][40:],a]
                                    data.append(data2)

                            f = Table(data)
                            f.setStyle(TableStyle(
                                [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                 ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
                            elements.append(f)
                            doc.build(elements, onFirstPage=header)
                            # ----------------------------------------------------------------------------------------
                            pdfs = ['Report1.pdf', 'Report10.pdf', 'Report2.pdf', 'Report3.pdf', 'Report4.pdf',
                                    'Report11.pdf', 'Report5.pdf', 'Report6.pdf', 'Report7.pdf', 'Report8.pdf',
                                    'Report9.pdf']
                            merger = PdfFileMerger()
                            path = folname + '/'
                            for pdf in pdfs:
                                merger.append(path + pdf)
                            merger.write(path + E00.get() + "_Final_report.pdf")
                            merger.close()
                            for i in range(1, 12, 1):
                                os.remove(path + "Report" + str(i) + ".pdf")

                            # ------------------------------------------------------------------------------------------------
                            os.startfile(path + E00.get() + "_Final_report.pdf")
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except MySQLdb.IntegrityError:
                            tkinter.messagebox.showinfo('Connectivity Problem.',
                                                        'Please Enter the EMPCODE which has primary information in database and re-enter details and upload...')

                        except FileNotFoundError:
                            tkinter.messagebox.showinfo('Message!!', 'File Not found!!')
                        except IndexError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the EMPCODE!!')
                        except MySQLdb._exceptions.OperationalError:
                            tkinter.messagebox.showinfo('Error!!', 'Please Enter the data in correct format.')
                        except OSError:
                            tkinter.messagebox.showinfo('Error!!', 'File not found!!!!!')
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + 'no other employee!!!')


                def query1():
                    if loginus == "admin":
                        def header(canvas, doc):
                            styles = getSampleStyleSheet()
                            c1 = canvas
                            width, height = letter
                            nd = styles['Normal']
                            header = "<b><u>" + "List of Employees working in the Institution"+ "</u></b>"
                            now = datetime.now()
                            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                            footer = "Last updated :" + dt_string
                            p = Paragraph(header, nd)
                            p.wrapOn(c1, width, height)
                            p.drawOn(c1, 40, 780)
                            p = Paragraph(footer, nd)
                            p.wrapOn(c1, width, height)
                            p.drawOn(c1, 350, 30)

                        elements=[]
                        doc = SimpleDocTemplate(folname + '/' + "query1.pdf")
                        data = [['Name','Academic\nQualification','Designation', 'Experience','Specialization','Photo']]
                        mycursor.execute("select FNAME,MNAME,LNAME,DESIGNATION,DOJ,SUBSPECILIZE,PHOTOFILE,table1.EMPCODE from table1,table12 where table1.EMPCODE=table12.EMPCODE")
                        myresult = mycursor.fetchall()
                        today=date.today()
                        d=today.strftime("%m/%d/%Y")
                        x=str(d).split('/')
                        y=x[-1]
                        l=[]
                        for rows in myresult:
                            if rows[7] not in l:
                                l.append(rows[7])
                                name=rows[0]+" "+rows[1]+" "+rows[2]
                                design=rows[3]
                                doj=rows[4]
                                v=str(doj).split('-')
                                w=v[0]
                                z=int(y)-int(w)
                                m=str(z)+" "+"year"
                                subs=rows[5]
                                photo=(str(folname) + "/" + rows[6])
                                mycursor.execute("select DEGREEOBT,DESCR from table2 where EMPCODE=%s",(str(rows[7]),))
                                myresult = mycursor.fetchall()
                                b=[]
                                for a in myresult:
                                    if a[0]!="Others":
                                        b.append(a[0])
                                    else:
                                        b.append(a[1])
                                degreeobt=" "
                                for i in range(len(b)):
                                    if i==0:
                                        degreeobt=b[i]
                                    else:
                                        degreeobt+=" , "
                                        degreeobt+=b[i]

                                data2 = [name,degreeobt[:20]+"\n"+degreeobt[20:40]+"\n"+degreeobt[40:80]+"\n"+degreeobt[80:],design,m,subs,Image(photo,width=100,height=100)]
                                b=[]
                                degreeobt=" "
                                data.append(data2)
                            else:
                                pass

                        f = Table(data)
                        f.setStyle(TableStyle(
                            [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                             ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
                        elements.append(f)
                        doc.build(elements, onFirstPage=header)
                        os.startfile(folname+ '/' + "query1.pdf")
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only ADMINISTRATOR!!!')

                def query2():
                    if loginus == "admin":
                        def header(canvas, doc):
                            styles = getSampleStyleSheet()
                            c1 = canvas
                            width, height = letter
                            nd = styles['Normal']
                            header = "<b><u>" + "List of Employees working for 5 years in the Institution" + "</u></b>"
                            now = datetime.now()
                            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                            footer = "Last updated :" + dt_string
                            p = Paragraph(header, nd)
                            p.wrapOn(c1, width, height)
                            p.drawOn(c1, 40, 780)
                            p = Paragraph(footer, nd)
                            p.wrapOn(c1, width, height)
                            p.drawOn(c1, 350, 30)

                        elements = []
                        doc = SimpleDocTemplate(folname + '/' + "query2.pdf")
                        data = [['Name', 'Academic\nQualification', 'Designation', 'Experience', 'Specialization', 'Photo']]
                        mycursor.execute(
                            "select FNAME,MNAME,LNAME,DESIGNATION,DOJ,SUBSPECILIZE,PHOTOFILE,table1.EMPCODE from table1,table12 where table1.EMPCODE=table12.EMPCODE")
                        myresult = mycursor.fetchall()
                        today = date.today()
                        d = today.strftime("%m/%d/%Y")
                        x = str(d).split('/')
                        y = x[-1]
                        l = []
                        for rows in myresult:
                            if rows[7] not in l:
                                l.append(rows[7])
                                name = rows[0] + " " + rows[1] + " " + rows[2]
                                design = rows[3]
                                doj = rows[4]
                                v = str(doj).split('-')
                                w = v[0]
                                z = int(y) - int(w)
                                m = str(z) + " " + "year"
                                subs = rows[5]
                                photo = (str(folname) + "/" + rows[6])
                                if z>=5:
                                    mycursor.execute("select DEGREEOBT,DESCR from table2 where EMPCODE=%s", (str(rows[7]),))
                                    myresult = mycursor.fetchall()
                                    b = []
                                    for a in myresult:
                                        if a[0] != "Others":
                                            b.append(a[0])
                                        else:
                                            b.append(a[1])
                                    degreeobt = " "
                                    for i in range(len(b)):
                                        if i == 0:
                                            degreeobt = b[i]
                                        else:
                                            degreeobt += " , "
                                            degreeobt += b[i]

                                    data2 = [name, degreeobt[:20] + "\n" + degreeobt[20:40] + "\n" + degreeobt[
                                                                                                     40:80] + "\n" + degreeobt[
                                                                                                                     80:],
                                             design, m, subs, Image(photo, width=100, height=100)]
                                    b = []
                                    degreeobt = " "
                                    data.append(data2)
                                else:
                                    pass
                            else:
                                pass

                        f = Table(data)
                        f.setStyle(TableStyle(
                            [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                             ('BOX', (0, 0), (-1, -1), 0.25, colors.black)]))
                        elements.append(f)
                        doc.build(elements, onFirstPage=header)
                        os.startfile(folname + '/' + "query2.pdf")
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only ADMINISTRATOR!!!')

                def Auth_update():
                    f1 = Font(family="Times New Roman", size=20)
                    if E00.get() == "":
                        Authority.config(text="Please Enter the EMP-CODE!!!", font=f1)
                        Authority1.config(text="Please Enter the EMP-CODE!!!", font=f1)
                        Authority2.config(text="Please Enter the EMP-CODE!!!", font=f1)
                        Authority3.config(text="Please Enter the EMP-CODE!!!", font=f1)
                        Authority4.config(text="Please Enter the EMP-CODE!!!", font=f1)
                        Authority5.config(text="Please Enter the EMP-CODE!!!", font=f1)
                        Authority6.config(text="Please Enter the EMP-CODE!!!", font=f1)
                        Authority7.config(text="Please Enter the EMP-CODE!!!", font=f1)
                    else:
                        Authority.config(text=E00.get(), font=f1)
                        Authority1.config(text=E00.get(), font=f1)
                        Authority2.config(text=E00.get(), font=f1)
                        Authority3.config(text=E00.get(), font=f1)
                        Authority4.config(text=E00.get(), font=f1)
                        Authority5.config(text=E00.get(), font=f1)
                        Authority6.config(text=E00.get(), font=f1)
                        Authority7.config(text=E00.get(), font=f1)
                    root.after(1000, Auth_update)

                def degree_update():
                    if degree.get() == "Others":
                        E22.config(state="normal")
                    else:
                        E22.delete(0, END)
                        E22.config(state="disabled")
                    root.after(100, degree_update)

                def title_update():
                    root.title(
                        "EMPLOYEE MANAGEMENT SYSTEM || Hello " + loginus.upper() + "!! You are successfully Logged In.")

                def deleteuser():
                    def submit():
                        if labpass.get() == loginpa and loginus == "admin":
                            pickle_in = open(str(foldername) + ".pickle", "rb")
                            data = pickle.load(pickle_in)
                            x = data[6]
                            del x[use.get()]
                            arr = [data[0], data[1], data[2], data[3], data[4], data[5], x]
                            pickle_out = open(str(foldername) + ".pickle", "wb")
                            pickle.dump(arr, pickle_out)
                            tkinter.messagebox.showinfo('Confirmation', 'User Deleted Successfully!!')
                            rootn1.destroy()
                        else:
                            tkinter.messagebox.showinfo('Permission error!!', 'Only Administrator can Delete user!!')

                    rootn1 = Tk()
                    rootn1.geometry("300x300")
                    rootn1.title("Admin Section")
                    rootn1.iconbitmap(r'diatmlogo.ico')
                    lab1 = Label(rootn1, text="Admin password:")
                    lab1.grid(row=1, column=0, padx=10, pady=10)
                    labpass = Entry(rootn1, show="*")
                    labpass.grid(row=1, column=1, padx=10, pady=10)
                    us = Label(rootn1, text="Username:")
                    us.grid(row=2, column=0, padx=10, pady=10)
                    use = Entry(rootn1)
                    use.grid(row=2, column=1, padx=10, pady=10)

                    but = Button(rootn1, text="DELETE USER", command=submit).grid(row=4, column=1, padx=10, pady=10)

                def adduser():
                    def submit():
                        if labpass.get() == loginpa and loginus == "admin":
                            pickle_in = open(str(foldername) + ".pickle", "rb")
                            data = pickle.load(pickle_in)
                            x = data[6]
                            x[use.get()] = pae.get()
                            arr = [data[0], data[1], data[2], data[3], data[4], data[5], x]
                            pickle_out = open(str(foldername) + ".pickle", "wb")
                            pickle.dump(arr, pickle_out)
                            tkinter.messagebox.showinfo('Confirmation', 'New user added Successfully!!')
                            rootn1.destroy()
                        else:
                            tkinter.messagebox.showinfo('Permission error!!', 'Only Administrator can add user!!')

                    rootn1 = Tk()
                    rootn1.geometry("300x300")
                    rootn1.title("Admin Section")
                    rootn1.iconbitmap(r'diatmlogo.ico')
                    lab1 = Label(rootn1, text="Admin password:")
                    lab1.grid(row=1, column=0, padx=10, pady=10)
                    labpass = Entry(rootn1, show="*")
                    labpass.grid(row=1, column=1, padx=10, pady=10)
                    us = Label(rootn1, text="New Username:")
                    us.grid(row=2, column=0, padx=10, pady=10)
                    use = Entry(rootn1)
                    use.grid(row=2, column=1, padx=10, pady=10)
                    pa = Label(rootn1, text="New Password:")
                    pa.grid(row=3, column=0, padx=10, pady=10)
                    pae = Entry(rootn1, show="*")
                    pae.grid(row=3, column=1, padx=10, pady=10)
                    but = Button(rootn1, text="ADD USER", command=submit).grid(row=4, column=1, padx=10, pady=10)

                    rootn1.mainloop()

                def changes():
                    def admin():
                        def submit():
                            if lab1e.get() == loginpa and loginus == "admin":
                                pickle_in = open(str(foldername) + ".pickle", "rb")
                                data = pickle.load(pickle_in)
                                x = data[6]
                                x[loginus] = lab2e.get()
                                arr = [data[0], data[1], data[2], data[3], data[4], data[5], x]
                                pickle_out = open(str(foldername) + ".pickle", "wb")
                                pickle.dump(arr, pickle_out)
                                tkinter.messagebox.showinfo('Confirmation', 'Password Changed Successfully!!')
                                rootn1.destroy()
                                rootn.destroy()
                            else:
                                tkinter.messagebox.showinfo('Permission error!!',
                                                            'Only Administrator can change password!!')

                        rootn1 = Tk()
                        rootn1.geometry("300x300")
                        rootn1.title("Admin Section")
                        rootn1.iconbitmap(r'diatmlogo.ico')
                        lab1 = Label(rootn1, text="Old Admin password:")
                        lab1.grid(row=0, column=0, padx=10, pady=10)
                        lab1e = Entry(rootn1, show="*")
                        lab1e.grid(row=0, column=1, padx=10, pady=10)
                        lab2 = Label(rootn1, text="New Admin password:")
                        lab2.grid(row=1, column=0, padx=10, pady=10)
                        lab2e = Entry(rootn1, show="*")
                        lab2e.grid(row=1, column=1, padx=10, pady=10)
                        But = Button(rootn1, text="CHANGE PASSWORD", command=submit).grid(row=3, column=1, padx=10,
                                                                                          pady=10)
                        rootn1.mainloop()

                    def user():
                        def submit():
                            if lab1e.get() == loginpa and loginus == labuse.get():
                                pickle_in = open(str(foldername) + ".pickle", "rb")
                                data = pickle.load(pickle_in)
                                x = data[6]
                                x[labuse.get()] = lab2e.get()
                                arr = [data[0], data[1], data[2], data[3], data[4], data[5], x]
                                pickle_out = open(str(foldername) + ".pickle", "wb")
                                pickle.dump(arr, pickle_out)
                                tkinter.messagebox.showinfo('Confirmation', 'Password Changed Successfully!!')
                                rootn1.destroy()
                                rootn.destroy()
                            else:
                                tkinter.messagebox.showinfo('Permission error!!',
                                                            'Only particular user can change password!!')

                        rootn1 = Tk()
                        rootn1.geometry("300x300")
                        rootn1.title("Admin Section")
                        rootn1.iconbitmap(r'diatmlogo.ico')
                        labus = Label(rootn1, text="User Name:")
                        labus.grid(row=0, column=0, padx=10, pady=10)
                        labuse = Entry(rootn1)
                        labuse.grid(row=0, column=1, padx=10, pady=10)
                        lab1 = Label(rootn1, text="Old password:")
                        lab1.grid(row=1, column=0, padx=10, pady=10)
                        lab1e = Entry(rootn1, show="*")
                        lab1e.grid(row=1, column=1, padx=10, pady=10)
                        lab2 = Label(rootn1, text="New password:")
                        lab2.grid(row=2, column=0, padx=10, pady=10)
                        lab2e = Entry(rootn1, show="*")
                        lab2e.grid(row=2, column=1, padx=10, pady=10)
                        But = Button(rootn1, text="CHANGE PASSWORD", command=submit).grid(row=3, column=1, padx=10,
                                                                                          pady=10)
                        rootn1.mainloop()

                    rootn = Tk()
                    rootn.geometry("300x100")
                    rootn.title("Change Credentials")
                    rootn.iconbitmap(r'diatmlogo.ico')
                    b1 = Button(rootn, text="Admin Section", command=admin).pack(pady=10)
                    b2 = Button(rootn, text="User Section", command=user).pack(pady=10)
                    rootn.mainloop()

                def delete_existing():
                    try:
                        a = tkinter.messagebox.askyesno('Confirmation', 'Do you really want to Delete?')
                        if a == 1:
                            mycursor.execute("DROP DATABASE " + str(databname))
                            pickle_in = open(str(foldername) + ".pickle", "rb")
                            data = pickle.load(pickle_in)
                            folname = data[3].rstrip()
                            shutil.rmtree(folname)
                            tkinter.messagebox.showinfo('Confirmation!!', 'Database & Folder Deleted Successfully')

                        else:
                            tkinter.messagebox.showinfo('Confirmation!!', 'Database Deletion Terminated!!')
                    except AttributeError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')

                def delete():
                    def del1():
                        try:
                            x = listbox.get(ANCHOR)
                            listbox.delete(ANCHOR)
                            c = x.split("||")
                            mycursor.execute("delete from table12 where EMPCODE =%s", (c[0],))
                            mycursor.execute("delete from table11 where EMPCODE =%s", (c[0],))
                            mycursor.execute("delete from table10 where EMPCODE =%s", (c[0],))
                            mycursor.execute("delete from table9 where EMPCODE =%s", (c[0],))
                            mycursor.execute("delete from table8 where EMPCODE =%s", (c[0],))
                            mycursor.execute("delete from table7 where EMPCODE =%s", (c[0],))
                            mycursor.execute("delete from table6 where EMPCODE =%s", (c[0],))
                            mycursor.execute("delete from table5 where EMPCODE =%s", (c[0],))
                            mycursor.execute("delete from table4 where EMPCODE =%s", (c[0],))
                            mycursor.execute("delete from table3 where EMPCODE =%s", (c[0],))
                            mycursor.execute("delete from table2 where EMPCODE =%s", (c[0],))
                            mycursor.execute("delete from table1 where EMPCODE =%s", (c[0],))
                            mydb.commit()
                        except IndexError:
                            tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                    try:
                        if loginus == "admin" or loginus == E00.get():
                            root1 = Tk()
                            root1.geometry("800x300")
                            root1.title("Delete")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=100)
                            listbox.pack()
                            bu1 = Button(root1, text="Delete", command=del1)
                            bu1.pack()
                            mycursor.execute(
                                "select EMPCODE,FNAME,MNAME,LNAME,DOB,MOBILENO from table1 where EMPCODE=%s",
                                (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                b = a[0] + '||' + a[1] + '||' + a[2] + '||' + a[3] + '||' + str(a[4]) + '||' + str(a[5])
                                listbox.insert(END, b)

                            root1.mainloop()
                        else:
                            tkinter.messagebox.showinfo('Permission error!!', 'Only respective user,Sorry!!')

                    except AttributeError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except NameError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except UnboundLocalError or IndexError:
                        tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                def delete2():
                    def del1():
                        try:
                            x = listbox.get(ANCHOR)
                            listbox.delete(ANCHOR)
                            c = x.split("||")
                            mycursor.execute("delete from table10 where EMPCODE =%s and DOCNAME=%s", (c[0], c[1],))
                            mydb.commit()
                        except IndexError:
                            tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                    try:
                        if loginus == "admin" or loginus == E00.get():
                            root1 = Tk()
                            root1.geometry("800x300")
                            root1.title("Delete")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=80)
                            listbox.pack()
                            bu1 = Button(root1, text="Delete", command=del1)
                            bu1.pack()
                            mycursor.execute("select * from table10 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                b = a[0] + '||' + a[1] + '||' + a[2] + '||' + a[3]
                                listbox.insert(END, b)

                            root1.mainloop()
                        else:
                            tkinter.messagebox.showinfo('Permission error!!', 'Only respective user,Sorry!!')

                    except AttributeError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except NameError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except UnboundLocalError or IndexError:
                        tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                def delete3():
                    def del1():
                        try:
                            x = listbox.get(ANCHOR)
                            listbox.delete(ANCHOR)
                            c = x.split("||")
                            mycursor.execute("delete from table11 where EMPCODE =%s and ACCOUNTNO=%s", (c[0], c[1],))
                            mydb.commit()
                        except IndexError:
                            tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                    try:
                        if loginus == "admin" or loginus == E00.get():
                            root1 = Tk()
                            root1.geometry("800x300")
                            root1.title("Delete")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=80)
                            listbox.pack()
                            bu1 = Button(root1, text="Delete", command=del1)
                            bu1.pack()
                            mycursor.execute("select * from table11 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                b = a[0] + '||' + a[1] + '||' + a[2] + '||' + a[3] + '||' + a[4] + '||' + a[5]
                                listbox.insert(END, b)

                            root1.mainloop()
                        else:
                            tkinter.messagebox.showinfo('Permission error!!', 'Only respective user,Sorry!!')

                    except AttributeError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except NameError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except UnboundLocalError or IndexError:
                        tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                def delete4():
                    def del1():
                        try:
                            x = listbox.get(ANCHOR)
                            listbox.delete(ANCHOR)
                            c = x.split("||")
                            mycursor.execute(
                                "delete from table12 where EMPCODE =%s and COURSETYPE=%s and DEPARTMENT=%s",
                                (c[0], c[1], c[2]))
                            mydb.commit()
                        except IndexError:
                            tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                    try:
                        if loginus == "admin" or loginus == E00.get():
                            root1 = Tk()
                            root1.geometry("800x300")
                            root1.title("Delete")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=100)
                            listbox.pack()
                            bu1 = Button(root1, text="Delete", command=del1)
                            bu1.pack()
                            mycursor.execute("select * from table12 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                b = a[0] + '||' + a[1] + '||' + a[2] + '||' + a[3] + '||' + a[4] + '||' + str(
                                    a[5]) + '||' + a[6]
                                listbox.insert(END, b)

                            root1.mainloop()
                        else:
                            tkinter.messagebox.showinfo('Permission error!!', 'Only respective user,Sorry!!')

                    except AttributeError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except NameError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except UnboundLocalError or IndexError:
                        tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                def delete5():
                    def del1():
                        try:
                            x = listbox.get(ANCHOR)
                            listbox.delete(ANCHOR)
                            c = x.split("||")
                            mycursor.execute("delete from table2 where EMPCODE =%s and DEGREEOBT=%s", (c[0], c[1],))
                            mydb.commit()
                        except IndexError:
                            tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                    try:
                        if loginus == "admin" or loginus == E00.get():
                            root1 = Tk()
                            root1.geometry("800x300")
                            root1.title("Delete")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=100)
                            listbox.pack()
                            bu1 = Button(root1, text="Delete", command=del1)
                            bu1.pack()
                            mycursor.execute("select * from table2 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                b = a[0] + '||' + a[1] + '||' + a[2] + '||' + a[3] + '||' + str(a[4]) + '||' + str(
                                    a[5]) + '||' + str(a[6]) + '||' + a[7] + '||' + a[8]
                                listbox.insert(END, b)

                            root1.mainloop()
                        else:
                            tkinter.messagebox.showinfo('Permission error!!', 'Only respective user,Sorry!!')

                    except AttributeError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except NameError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except UnboundLocalError or IndexError:
                        tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                def delete6():
                    def del1():
                        try:
                            x = listbox.get(ANCHOR)
                            listbox.delete(ANCHOR)
                            c = x.split("||")
                            mycursor.execute("delete from table3 where EMPCODE =%s and EXPTYPE=%s and INST_COMP=%s",
                                             (c[0], c[1], c[2],))
                            mydb.commit()
                        except IndexError:
                            tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                    try:
                        if loginus == "admin" or loginus == E00.get():
                            root1 = Tk()
                            root1.geometry("800x300")
                            root1.title("Delete")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=100)
                            listbox.pack()
                            bu1 = Button(root1, text="Delete", command=del1)
                            bu1.pack()
                            mycursor.execute("select * from table3 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                b = a[0] + '||' + a[1] + '||' + a[2] + '||' + a[3] + '||' + str(a[4]) + '||' + str(
                                    a[5]) + '||' + str(a[6]) + '||' + str(a[7]) + '||' + a[8] + '||' + a[9]
                                listbox.insert(END, b)

                            root1.mainloop()
                        else:
                            tkinter.messagebox.showinfo('Permission error!!', 'Only respective user,Sorry!!')

                    except AttributeError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except NameError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except UnboundLocalError or IndexError:
                        tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                def delete7():
                    def del1():
                        try:
                            x = listbox.get(ANCHOR)
                            listbox.delete(ANCHOR)
                            c = x.split("||")
                            mycursor.execute("delete from table4 where EMPCODE = %s and SPECIALACV = %s", (c[0], c[1],))
                            mydb.commit()
                        except IndexError:
                            tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                    try:
                        if loginus == "admin" or loginus == E00.get():
                            root1 = Tk()
                            root1.geometry("800x300")
                            root1.title("Delete")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=110)
                            listbox.pack()
                            bu1 = Button(root1, text="Delete", command=del1)
                            bu1.pack()
                            mycursor.execute("select * from table4 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                b = a[0] + '||' + a[1] + '||' + a[2]
                                listbox.insert(END, b)

                            root1.mainloop()
                        else:
                            tkinter.messagebox.showinfo('Permission error!!', 'Only respective user,Sorry!!')

                    except AttributeError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except NameError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except UnboundLocalError or IndexError:
                        tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                def delete8():
                    def del1():
                        try:
                            x = listbox.get(ANCHOR)
                            listbox.delete(ANCHOR)
                            c = x.split("||")
                            mycursor.execute("delete from table5 where EMPCODE = %s and YOL = %s", (c[0], c[1],))
                            mydb.commit()
                        except IndexError:
                            tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                    try:
                        if loginus == "admin" or loginus == E00.get():
                            root1 = Tk()
                            root1.geometry("800x300")
                            root1.title("Delete")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=100)
                            listbox.pack()
                            bu1 = Button(root1, text="Delete", command=del1)
                            bu1.pack()
                            mycursor.execute("select * from table5 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                b = str(a[0]) + '||' + str(a[1]) + '||' + str(a[2]) + '||' + str(a[3]) + '||' + str(
                                    a[4]) + '||' + str(a[5]) + '||' + str(a[6]) + '||' + str(a[7]) + '||' + a[8]
                                listbox.insert(END, b)

                            root1.mainloop()
                        else:
                            tkinter.messagebox.showinfo('Permission error!!', 'Only respective user,Sorry!!')

                    except AttributeError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except NameError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except UnboundLocalError or IndexError:
                        tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                def delete9():
                    def del1():
                        try:
                            x = listbox.get(ANCHOR)
                            listbox.delete(ANCHOR)
                            c = x.split("||")
                            mycursor.execute("delete from table6 where EMPCODE = %s and DORP = %s ", (c[0], c[1],))
                            mydb.commit()
                        except IndexError:
                            tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                    try:
                        if loginus == "admin" or loginus == E00.get():
                            root1 = Tk()
                            root1.geometry("800x300")
                            root1.title("Delete")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=100)
                            listbox.pack()
                            bu1 = Button(root1, text="Delete", command=del1)
                            bu1.pack()
                            mycursor.execute("select * from table6 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                b = str(a[0]) + '||' + str(a[1]) + '||' + str(a[2]) + '||' + str(a[3])
                                listbox.insert(END, b)

                            root1.mainloop()
                        else:
                            tkinter.messagebox.showinfo('Permission error!!', 'Only respective user,Sorry!!')

                    except AttributeError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except NameError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except UnboundLocalError or IndexError:
                        tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                def delete10():
                    def del1():
                        try:
                            x = listbox.get(ANCHOR)
                            listbox.delete(ANCHOR)
                            c = x.split("||")
                            mycursor.execute("delete from table7 where EMPCODE = %s and DOPAY = %s ", (c[0], c[1],))
                            mydb.commit()
                        except IndexError:
                            tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                    try:
                        if loginus == "admin" or loginus == E00.get():
                            root1 = Tk()
                            root1.geometry("800x300")
                            root1.title("Delete")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=100)
                            listbox.pack()
                            bu1 = Button(root1, text="Delete", command=del1)
                            bu1.pack()
                            mycursor.execute("select * from table7 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                b = str(a[0]) + '||' + str(a[1]) + '||' + str(a[2]) + '||' + str(a[3]) + '||' + str(
                                    a[4]) + '||' + str(a[5]) + '||' + str(a[6])
                                listbox.insert(END, b)

                            root1.mainloop()
                        else:
                            tkinter.messagebox.showinfo('Permission error!!', 'Only respective user,Sorry!!')

                    except AttributeError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except NameError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except UnboundLocalError or IndexError:
                        tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                def delete11():
                    def del1():
                        try:
                            x = listbox.get(ANCHOR)
                            listbox.delete(ANCHOR)
                            c = x.split("||")
                            mycursor.execute("delete from table8 where EMPCODE = %s and SEM = %s and PAPERCODE= %s ",
                                             (c[0], c[1], c[2],))
                            mydb.commit()
                        except IndexError:
                            tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                    try:
                        if loginus == "admin" or loginus == E00.get():
                            root1 = Tk()
                            root1.geometry("800x300")
                            root1.title("Delete")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=100)
                            listbox.pack()
                            bu1 = Button(root1, text="Delete", command=del1)
                            bu1.pack()
                            mycursor.execute("select * from table8 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                b = str(a[0]) + '||' + str(a[1]) + '||' + str(a[2]) + '||' + str(a[3]) + '||' + str(
                                    a[4]) + '||' + str(a[5]) + '||' + str(a[6])
                                listbox.insert(END, b)

                            root1.mainloop()
                        else:
                            tkinter.messagebox.showinfo('Permission error!!', 'Only respective user,Sorry!!')

                    except AttributeError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except NameError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except UnboundLocalError or IndexError:
                        tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                def delete12():
                    def del1():
                        try:
                            x = listbox.get(ANCHOR)
                            listbox.delete(ANCHOR)
                            c = x.split("||")
                            mycursor.execute("delete from table9 where EMPCODE = %s and FROMDATE = %s and DESCR= %s ",
                                             (c[0], c[1], c[3],))
                            mydb.commit()
                        except IndexError:
                            tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                    try:
                        if loginus == "admin" or loginus == E00.get():
                            root1 = Tk()
                            root1.geometry("800x300")
                            root1.title("Delete")
                            root1.iconbitmap(r'diatmlogo.ico')
                            listbox = Listbox(root1, width=100)
                            listbox.pack()
                            bu1 = Button(root1, text="Delete", command=del1)
                            bu1.pack()
                            mycursor.execute("select * from table9 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                b = str(a[0]) + '||' + str(a[1]) + '||' + str(a[2]) + '||' + str(a[3]) + '||' + str(
                                    a[4])
                                listbox.insert(END, b)

                            root1.mainloop()
                        else:
                            tkinter.messagebox.showinfo('Permission error!!', 'Only respective user,Sorry!!')

                    except AttributeError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except NameError:
                        tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        root1.destroy()
                    except UnboundLocalError or IndexError:
                        tkinter.messagebox.showinfo('Error!!', 'Nothing is Selected to Delete')

                def instruction():
                    root1 = Tk()
                    root1.geometry("1000x600")
                    root1.title("Instructions")
                    root1.iconbitmap(r'diatmlogo.ico')
                    lab1 = Label(root1, text="Read the instructions carefully before using:-", font=f)
                    lab1.grid(row=0, column=0, padx=10, pady=10)
                    lab = Label(root1,
                                text="1. Please do the setup by the administrator of the organisation at First.\n\n"
                                     "2. Administrator can add users, delete users,edit and display along with deletion of data.\n\n"
                                     "3. User name of administrator should always be 'admin' and password is user defined.\n\n"
                                     "4. User name of users should be their 'EMPCODE' and password user defined.\n\n"
                                     "5. Password of both administrator and user can be changed by them.\n\n"
                                     "6. You have to click on the tabs to switch in between them.\n\n"
                                     "7. With each and every click to submit will affect in the database.\n\n"
                                     "8. You can login to the software anytime at any point where you have left out,\n\n"
                                     "   the software is very dynamic and flexible.\n\n"
                                     "9. The upload and submission of photo and signature is mandatory.\n\n"
                                     "10. The file size of each and every document to be uploaded must be less than 50kb\n\n"
                                     "11. The photo and signature must be in jpeg format.\n\n"
                                     "12. The other documents can be in jpeg/pdf format.", font=f)
                    lab.grid(row=1, column=0, padx=20, pady=20)
                    root1.mainloop()

                def feedback():
                    def submit():
                        arr = [str(lab1e.get()), str(lab2e.get()), str(lab3e.get()), str(lab4e.get())]
                        pickle_out = open("feedback.pickle", "ab")
                        pickle.dump(arr, pickle_out)
                        tkinter.messagebox.showinfo('Confirmation!!', 'Feedback Successfully accepted. Thank you!!')
                        root1.destroy()

                    root1 = Tk()
                    root1.geometry("1000x400")
                    root1.title("User's feedback to Developer")
                    root1.iconbitmap(r'diatmlogo.ico')
                    lab1 = Label(root1, text="Score the Software out of 10.", font=f)
                    lab1.grid(row=0, column=0, padx=10, pady=10)
                    lab2 = Label(root1, text="Score the Design of Software out of 10.", font=f)
                    lab2.grid(row=1, column=0, padx=10, pady=10)
                    lab3 = Label(root1, text="Score the Software in terms of security out of 10.", font=f)
                    lab3.grid(row=2, column=0, padx=10, pady=10)
                    lab4 = Label(root1, text="Provide your valuable feedback to improve:", font=f)
                    lab4.grid(row=3, column=0, padx=10, pady=10)
                    lab1e = Entry(root1)
                    lab1e.grid(row=0, column=1, padx=10, pady=10, sticky='w')
                    lab2e = Entry(root1)
                    lab2e.grid(row=1, column=1, padx=10, pady=10, sticky='w')
                    lab3e = Entry(root1)
                    lab3e.grid(row=2, column=1, padx=10, pady=10, sticky='w')
                    lab4e = Entry(root1, width=60)
                    lab4e.grid(row=3, column=1, padx=10, pady=10, sticky='w')
                    button = Button(root1, text="SUBMIT", command=submit).grid(row=4, column=1, padx=10, pady=10)
                    root1.mainloop()

                def exit():
                    root.destroy()

                # =======================================================================================================================
                def display1():
                    if loginus == E00.get() or loginus == "admin":
                        def photo_show():
                            try:
                                pickle_in = open(str(foldername) + ".pickle", "rb")
                                data = pickle.load(pickle_in)
                                mycursor.execute("SELECT * FROM table1 WHERE EMPCODE=%s", (E00.get(),))
                                myresult = mycursor.fetchall()
                                a = myresult[0][-2]
                                os.startfile(data[3] + '/' + a)
                            except FileNotFoundError:
                                tkinter.messagebox.showinfo('Error',
                                                            'File doesnot exist, please upload/check connectivity')

                        def signature_show():
                            try:
                                pickle_in = open(str(foldername) + ".pickle", "rb")
                                data = pickle.load(pickle_in)
                                mycursor.execute("SELECT * FROM table1 WHERE EMPCODE=%s", (E00.get(),))
                                myresult = mycursor.fetchall()
                                a = myresult[0][-1]
                                os.startfile(data[3] + '/' + a)

                            except FileNotFoundError:
                                tkinter.messagebox.showinfo('Error',
                                                            'File doesnot exist, please upload/check connectivity')

                        rootdis = Tk()
                        rootdis.geometry("1300x600")
                        rootdis.iconbitmap(r'diatmlogo.ico')
                        rootdis.configure(background='white')
                        rootdis.title("Personal details")
                        label1 = Label(rootdis, text="NAME:", font=f)
                        label1.grid(row=0, column=0, padx=10, pady=10)
                        label2 = Label(rootdis, text=" ")
                        label2.grid(row=0, column=1, padx=10, pady=10)
                        label3 = Label(rootdis, text="DATE OF BIRTH:", font=f)
                        label3.grid(row=1, column=0, padx=10, pady=10)
                        label4 = Label(rootdis, text=" ")
                        label4.grid(row=1, column=1, padx=10, pady=10)
                        label5 = Label(rootdis, text="RELIGION:", font=f)
                        label5.grid(row=2, column=0, padx=10, pady=10)
                        label6 = Label(rootdis, text=" ")
                        label6.grid(row=2, column=1, padx=10, pady=10)
                        label7 = Label(rootdis, text="GENDER:", font=f)
                        label7.grid(row=2, column=2, padx=10, pady=10)
                        label8 = Label(rootdis, text=" ")
                        label8.grid(row=2, column=3, padx=10, pady=10)
                        label9 = Label(rootdis, text="CASTE:", font=f)
                        label9.grid(row=2, column=4, padx=10, pady=10)
                        label10 = Label(rootdis, text=" ")
                        label10.grid(row=2, column=5, padx=10, pady=10)
                        label11 = Label(rootdis, text="BLOOD GROUP:", font=f)
                        label11.grid(row=3, column=0, padx=10, pady=10)
                        label12 = Label(rootdis, text=" ")
                        label12.grid(row=3, column=1, padx=10, pady=10)
                        label13 = Label(rootdis, text="PRESENT ADDRESS:", font=f)
                        label13.grid(row=4, column=0, padx=10, pady=10)
                        label14 = Label(rootdis, text=" ")
                        label14.grid(row=4, column=1, padx=10, pady=10)
                        label15 = Label(rootdis, text="PRESENT CITY:", font=f)
                        label15.grid(row=5, column=0, padx=10, pady=10)
                        label16 = Label(rootdis, text=" ")
                        label16.grid(row=5, column=1, padx=10, pady=10)
                        label17 = Label(rootdis, text="PRESENT STATE:", font=f)
                        label17.grid(row=5, column=2, padx=10, pady=10)
                        label18 = Label(rootdis, text=" ")
                        label18.grid(row=5, column=3, padx=10, pady=10)
                        label19 = Label(rootdis, text="PRESENT PIN:", font=f)
                        label19.grid(row=5, column=4, padx=10, pady=10)
                        label20 = Label(rootdis, text=" ")
                        label20.grid(row=5, column=5, padx=10, pady=10)
                        label21 = Label(rootdis, text="PERMANENT ADDRESS:", font=f)
                        label21.grid(row=6, column=0, padx=10, pady=10)
                        label22 = Label(rootdis, text=" ")
                        label22.grid(row=6, column=1, padx=10, pady=10)
                        label23 = Label(rootdis, text="PERMANENT CITY:", font=f)
                        label23.grid(row=7, column=0, padx=10, pady=10)
                        label24 = Label(rootdis, text=" ")
                        label24.grid(row=7, column=1, padx=10, pady=10)
                        label25 = Label(rootdis, text="PERMANENT STATE:", font=f)
                        label25.grid(row=7, column=2, padx=10, pady=10)
                        label26 = Label(rootdis, text=" ")
                        label26.grid(row=7, column=3, padx=10, pady=10)
                        label27 = Label(rootdis, text="PERMANENT PIN:", font=f)
                        label27.grid(row=7, column=4, padx=10, pady=10)
                        label28 = Label(rootdis, text=" ")
                        label28.grid(row=7, column=5, padx=10, pady=10)
                        label29 = Label(rootdis, text="MOBILE NO.:", font=f)
                        label29.grid(row=8, column=0, padx=10, pady=10)
                        label30 = Label(rootdis, text=" ")
                        label30.grid(row=8, column=1, padx=10, pady=10)
                        label31 = Label(rootdis, text="ALTERNATIVE MOBLE NO.:", font=f)
                        label31.grid(row=8, column=2, padx=10, pady=10)
                        label32 = Label(rootdis, text=" ")
                        label32.grid(row=8, column=3, padx=10, pady=10)
                        label33 = Label(rootdis, text="EMAIL:", font=f)
                        label33.grid(row=8, column=4, padx=10, pady=10)
                        label34 = Label(rootdis, text=" ")
                        label34.grid(row=8, column=5, padx=10, pady=10)
                        photo = Button(rootdis, text="Show the Photo", command=photo_show)
                        photo.grid(row=10, column=1, padx=10, pady=20)
                        signature = Button(rootdis, text="Show the Signature", command=signature_show)
                        signature.grid(row=10, column=3, padx=10, pady=20)

                        try:
                            mycursor.execute("select * from table1 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                            aa = str(a[4]).split('-')
                            b = aa[-1] + "-" + aa[-2] + "-" + aa[-3]
                            label2.config(text=a[1] + " " + a[2] + " " + a[3])
                            label4.config(text=b)
                            label6.config(text=a[5])
                            label8.config(text=a[6])
                            label10.config(text=a[7])
                            label12.config(text=a[8])
                            label14.config(text=a[9])
                            label16.config(text=a[10])
                            label18.config(text=a[11])
                            label20.config(text=a[12])
                            label22.config(text=a[13])
                            label24.config(text=a[14])
                            label26.config(text=a[15])
                            label28.config(text=a[16])
                            label30.config(text=a[17])
                            label32.config(text=a[18])
                            label34.config(text=a[19])

                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except UnboundLocalError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Enter the EMPCODE...')

                        rootdis.mainloop()
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + ' no other employee!!!')

                def display2():
                    if loginus == E00.get() or loginus == "admin":
                        try:
                            rootdis1 = Tk()
                            rootdis1.geometry("1200x700")
                            rootdis1.iconbitmap(r'diatmlogo.ico')
                            rootdis1.title("Legal Details.")
                            text = Text(rootdis1, width=69, height=7, wrap=WORD, padx=10, pady=10, bd=1)
                            text.grid(row=1, column=0, padx=10, pady=10, sticky='WN')
                            text.insert(0.0, "Document Name || Document ID Number")
                            mycursor.execute("select * from table10 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                text.insert(2.0, "\n")
                                text.insert(2.0, a[1] + '|' + str(a[2]))
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except UnboundLocalError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Enter the EMPCODE...')

                        rootdis1.mainloop()
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + ' no other employee!!!')

                def display3():
                    if loginus == E00.get() or loginus == "admin":
                        rootdis2 = Tk()
                        rootdis2.geometry("1200x700")
                        rootdis2.title("Bank Details")
                        l1 = Label(rootdis2, text="Account No.:", font=f)
                        l1.grid(row=0, column=0, padx=10, pady=10)
                        l2 = Label(rootdis2, text=" ")
                        l2.grid(row=0, column=1, padx=10, pady=10)
                        l3 = Label(rootdis2, text="Bank Name:", font=f)
                        l3.grid(row=1, column=0, padx=10, pady=10)
                        l4 = Label(rootdis2, text=" ")
                        l4.grid(row=1, column=1, padx=10, pady=10)
                        l5 = Label(rootdis2, text="Branch Code", font=f)
                        l5.grid(row=2, column=0, padx=10, pady=10)
                        l6 = Label(rootdis2, text=" ")
                        l6.grid(row=2, column=1, padx=10, pady=10)
                        l7 = Label(rootdis2, text="IFSC Code", font=f)
                        l7.grid(row=3, column=0, padx=10, pady=10)
                        l8 = Label(rootdis2, text=" ")
                        l8.grid(row=3, column=1, padx=10, pady=10)
                        try:
                            mycursor.execute("select * from table11 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                            l2.config(text=a[1])
                            l4.config(text=a[2])
                            l6.config(text=a[3])
                            l8.config(text=a[4])

                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except UnboundLocalError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Enter the EMPCODE...')

                        rootdis2.mainloop()
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + ' no other employee!!!')

                def display4():
                    if loginus == E00.get() or loginus == "admin":
                        rootdis3 = Tk()
                        rootdis3.geometry("1200x700")
                        rootdis3.title("Joining Details.")
                        text = Text(rootdis3, width=90, height=5, wrap=WORD, padx=10, pady=10, bd=1)
                        text.grid(row=0, column=1, padx=10, pady=10, sticky='WN')
                        text.insert(0.0,
                                    "Course type || Department || Designation || Subject Specilization || Date of Joining")
                        try:
                            mycursor.execute("select * from table12 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                text.insert(2.0, "\n")
                                text.insert(2.0, a[1] + '|' + a[2] + '|' + a[3] + '|' + a[4] + '|' + str(a[5]))
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except UnboundLocalError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Enter the EMPCODE...')

                        rootdis3.mainloop()
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + ' no other employee!!!')

                def display5():
                    if loginus == E00.get() or loginus == "admin":
                        rootdis4 = Tk()
                        rootdis4.geometry("1200x700")
                        rootdis4.title("Academic Details.")
                        text = Text(rootdis4, width=95, height=7, wrap=WORD, padx=10, pady=10, bd=1)
                        text.grid(row=0, column=1, padx=10, pady=10, sticky='WN')
                        text.insert(0.0,
                                    "Degree obtained || Description || University/Board || Institution || Year of Passing || Percentage || Remarks")
                        try:
                            mycursor.execute("select * from table2 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                text.insert(2.0, '\n')
                                text.insert(2.0,
                                            a[1] + '|' + a[2] + '|' + a[3] + '|' + a[4] + '|' + str(a[5]) + '|' + str(
                                                a[6]) + '|' + a[7])
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except UnboundLocalError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Enter the EMPCODE...')

                        rootdis4.mainloop()
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + ' no other employee!!!')

                def display6():
                    if loginus == E00.get() or loginus == "admin":
                        rootdis5 = Tk()
                        rootdis5.geometry("1200x700")
                        rootdis5.title("Experience Details.")
                        text = Text(rootdis5, width=105, height=3, wrap=WORD, padx=10, pady=10, bd=1)
                        text.grid(row=0, column=1, padx=10, pady=10, sticky='WN')
                        text.insert(0.0,
                                    "Exp_Type || Institution || Address || Designation || Period_from || Period_to || Salary_drawn || Remarks")
                        try:
                            mycursor.execute("select * from table3 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                text.insert(2.0, '\n')
                                text.insert(2.0,
                                            a[1] + '|' + a[2] + '|' + a[3] + '|' + a[4] + '|' + str(a[5]) + '|' + str(
                                                a[6]) + '|' + str(a[7]) + '|' + a[8])
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except UnboundLocalError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Enter the EMPCODE...')

                        rootdis5.mainloop()
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + ' no other employee!!!')

                def display7():
                    if loginus == E00.get() or loginus == "admin":
                        rootdis6 = Tk()
                        rootdis6.geometry("1200x700")
                        rootdis6.title("Special Acievements Details.")
                        text = Text(rootdis6, width=70, height=5, wrap=WORD, padx=10, pady=10, bd=1)
                        text.grid(row=0, column=1, padx=10, pady=10, sticky='WN')
                        text.insert(0.0, "||Special achievement details||")
                        try:
                            mycursor.execute("select * from table4 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                text.insert(2.0, '\n')
                                text.insert(2.0, a[1])
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except UnboundLocalError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Enter the EMPCODE...')

                        rootdis6.mainloop()
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + ' no other employee!!!')

                def display8():
                    if loginus == E00.get() or loginus == "admin":
                        rootdis7 = Tk()
                        rootdis7.geometry("1200x700")
                        rootdis7.title("Leave Management Details")
                        text = Text(rootdis7, width=152, height=3, wrap=WORD, padx=10, pady=10, bd=1)
                        text.grid(row=0, column=1, padx=10, pady=10, sticky='WN')
                        text.insert(0.0, "Year || CL || ML || EL || SL || OD || Others")
                        try:
                            mycursor.execute("select * from table5 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                text.insert(2.0, "\n")
                                text.insert(2.0,
                                            str(a[1]) + '|' + str(a[2]) + '|' + str(a[3]) + '|' + str(a[4]) + '|' + str(
                                                a[5]) + '|' + str(a[6]) + '|' + str(a[7]))

                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except UnboundLocalError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Enter the EMPCODE...')

                        rootdis7.mainloop()
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + ' no other employee!!!')

                def display9():
                    if loginus == E00.get() or loginus == "admin":
                        rootdis8 = Tk()
                        rootdis8.geometry("1200x700")
                        rootdis8.title("Reward/Penalty Details")
                        text = Text(rootdis8, width=97, height=7, wrap=WORD, padx=10, pady=10, bd=1)
                        text.grid(row=0, column=1, padx=10, pady=10, sticky='WN')
                        text.insert(0.0, "Date || Description")
                        try:
                            mycursor.execute("select * from table6 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                text.insert(2.0, "\n")
                                text.insert(2.0, str(a[1]) + '|' + a[2])
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except UnboundLocalError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Enter the EMPCODE...')

                        rootdis8.mainloop()
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + ' no other employee!!!')

                def display10():
                    if loginus == E00.get() or loginus == "admin":
                        rootdis9 = Tk()
                        rootdis9.geometry("1200x700")
                        rootdis9.title("Pay Scale Details")
                        text = Text(rootdis9, width=116, height=5, wrap=WORD, padx=10, pady=10, bd=1)
                        text.grid(row=0, column=1, padx=10, pady=10, sticky='WN')
                        text.insert(0.0, "Date || Basic || DA || HRA || Others")
                        try:
                            mycursor.execute("select * from table7 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                text.insert(2.0, "\n")
                                text.insert(2.0, str(a[1]) + '|' + str(a[2]) + '|' + str(a[3]) + '|' + str(
                                    a[4]) + '|' + str(a[5]))
                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except UnboundLocalError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Enter the EMPCODE...')

                        rootdis9.mainloop()
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + ' no other employee!!!')

                def display11():
                    if loginus == E00.get() or loginus == "admin":
                        rootdis10 = Tk()
                        rootdis10.geometry("1200x700")
                        rootdis10.title("Subject Allocation Details")
                        text = Text(rootdis10, width=118, height=3, wrap=WORD, padx=10, pady=10, bd=1)
                        text.grid(row=0, column=1, padx=10, pady=10, sticky='WN')
                        text.insert(0.0, "Semester || Paper Code || Paper Name || Department || Year")
                        try:
                            mycursor.execute("select * from table8 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                text.insert(2.0, "\n")
                                text.insert(2.0, a[1] + '|' + a[2] + '|' + a[3] + '|' + a[4] + '|' + str(a[5]))

                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except UnboundLocalError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Enter the EMPCODE...')

                        rootdis10.mainloop()
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + ' no other employee!!!')

                def display12():
                    if loginus == E00.get() or loginus == "admin":
                        rootdis11 = Tk()
                        rootdis11.geometry("1200x700")
                        rootdis11.title("Additional Responsibility Details")
                        text = Text(rootdis11, width=98, height=3, wrap=WORD, padx=10, pady=10, bd=1)
                        text.grid(row=0, column=1, padx=10, pady=10, sticky='WN')
                        text.insert(0.0, "From date || To date || Description")
                        try:
                            mycursor.execute("select * from table9 where EMPCODE=%s", (E00.get(),))
                            myresult = mycursor.fetchall()
                            for rows in myresult:
                                a = rows
                                text.insert(2.0, "\n")
                                text.insert(2.0, str(a[1]) + '|' + str(a[2]) + '|' + a[3])

                        except AttributeError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Log In to Database...')
                        except UnboundLocalError:
                            tkinter.messagebox.showinfo('Connectivity Problem.', 'Please Enter the EMPCODE...')

                        rootdis11.mainloop()
                    else:
                        tkinter.messagebox.showinfo('Permission Error!!', 'Only' + loginus + ' no other employee!!!')

                def logout():
                    root.destroy()


                # ----------------------------------------------------------------------------------------------------------------------------
                class ScrolledFrame(Frame):

                    def __init__(self, parent, vertical=True, horizontal=True):
                        super().__init__(parent)

                        # canvas for inner frame
                        self._canvas = Canvas(self, width=1325, height=650)
                        self._canvas.grid(row=0, column=0, sticky='news')  # changed

                        # create right scrollbar and connect to canvas Y
                        self._vertical_bar = Scrollbar(self, orient='vertical', command=self._canvas.yview)
                        if vertical:
                            self._vertical_bar.grid(row=0, column=1, sticky='ns')
                        self._canvas.configure(yscrollcommand=self._vertical_bar.set)

                        # create bottom scrollbar and connect to canvas X
                        self._horizontal_bar = Scrollbar(self, orient='horizontal', command=self._canvas.xview)
                        if horizontal:
                            self._horizontal_bar.grid(row=1, column=0, sticky='we')
                        self._canvas.configure(xscrollcommand=self._horizontal_bar.set)

                        # inner frame for widgets
                        self.inner = Frame(self._canvas)
                        self._window = self._canvas.create_window((0, 0), window=self.inner, anchor='nw')

                        # autoresize inner frame
                        self.columnconfigure(0, weight=1)  # changed
                        self.rowconfigure(0, weight=1)  # changed

                        # resize when configure changed
                        self.inner.bind('<Configure>', self.resize)
                        self._canvas.bind('<Configure>', self.frame_width)

                    def frame_width(self, event):
                        # resize inner frame to canvas size
                        canvas_width = event.width
                        self._canvas.itemconfig(self._window, width=canvas_width)

                    def resize(self, event=None):
                        self._canvas.configure(scrollregion=self._canvas.bbox('all'))

                root = Tk()
                wwidth=root.winfo_screenwidth()
                wheight=root.winfo_screenheight()
                root.geometry("%dx%d+0+0" % (wwidth,wheight))

                root.title(
                    "EMPLOYEE MANAGEMENT SYSTEM || Hello " + loginus.upper() + "!! You are successfully Logged In.")
                root.iconbitmap(r'diatmlogo.ico')
                root.configure(background='white')
                window = ScrolledFrame(root)
                window.grid(row=2, column=7)
                # ---------------------------------------------------------------------------------------
                menubar = Menu(window.inner)
                filemenu = Menu(menubar, tearoff=0)
                filemenu.add_command(label="Change Credentials", command=changes)
                filemenu.add_command(label="Add User", command=adduser)
                filemenu.add_command(label="Delete User", command=deleteuser)
                filemenu.add_separator()
                filemenu.add_command(label="Delete existing Database", command=delete_existing)
                menubar.add_cascade(label="Edit credentials", menu=filemenu)
                filemenu2 = Menu(menubar, tearoff=0)
                filemenu2.add_command(label="Instructions", command=instruction)
                filemenu2.add_cascade(label="Feedback", command=feedback)
                filemenu2.add_separator()
                filemenu2.add_command(label="Logout", command=logout)
                filemenu2.add_command(label="Exit", command=exit)
                menubar.add_cascade(label="Help", menu=filemenu2)
                root.config(menu=menubar)

                # font for all the labels.
                f = Font(family="Times New Roman", size=12, weight="normal", slant="roman", underline=0)
                # font for emp.
                fe = Font(family="Arial", size=13, weight="bold", slant="roman", underline=1)

                # Creation of Tab
                tabcontrol = ttk.Notebook(window.inner, width=6000, height=1000)
                style = ttk.Style()
                style.configure("TNotebook", background='white', tabmargins=[2, 5, 2, 0])
                style.configure("TNotebook.Tab", padding=[1, 1], background='blue')
                style.map("TNotebook.Tab", foreground=[('selected', 'blue')], expand=[("selected", [1, 1, 1, 0])])
                style.configure("TNotebook.Tab", background='yellow', foreground='red')
                style.configure("TFrame", background="white")
                style.configure("TButton", font=('arial', 12, 'bold'), foreground='blue', background='red',
                                borderwidth='4')
                style.configure("TRadiobutton", background='cyan', foreground='black', font=("arial", 10, "bold"))
                style.configure("TLabel", foreground="black", background="cyan")
                style.configure("BW.TLabel", foreground="black", background="White")
                tabcontrol.grid(row=0, column=0, columnspan=50, rowspan=49, sticky='NESW')

                # Tab-1-----------------------------------------------------------------------------------------------------------------------
                tab1 = ttk.Frame(tabcontrol, style='TFrame')
                tabcontrol.add(tab1, text="Personal Details")

                # Grouping of blocks.----------------------------
                group1 = Pmw.Group(tab1, tag_text="INFORMATION")
                group1.grid(row=0, column=0, padx=20, pady=20, sticky='WN')

                gender = IntVar()
                caste = StringVar()
                leaveyear = IntVar()
                religion=StringVar()
                sem = StringVar()
                subyear = IntVar()
                docname = StringVar()
                coursetype = StringVar()
                designation = StringVar()
                degree = StringVar()
                state1 = StringVar()
                state2 = StringVar()
                dept1 = StringVar()
                dept2 = StringVar()
                l1 = ["GENERAL", "SC", "ST", "OBC", "OTHERS"]
                l2 = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016,
                      2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032,
                      2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040]
                l3 = ["1st Sem", "2nd Sem", "3rd Sem", "4th Sem", "5th Sem", "6th Sem", "7th Sem", "8th Sem"]
                l4 = ["Epic_Voter ID Card", "Adhaar Card", "Passport", "PAN card", "Driving Licence"]
                l5 = ["Under Graduate", "Post Graduate"]
                l6 = ["Distinguished Professor", "Emeritus Professor", "Professor", "Associate Professor",
                      "Assistant Professor", "Contractual Teacher", "Senior Technical Assistant", "Technical Assistant",
                      "Others"]
                l7 = ["CLASS X", "CLASS XII", "CLASS DIPLOMA", "ITI", "GRADUATION", "POST GRADUATION", "P.H.D","Others"]
                l8 = ["Hindu","Islam","Sikh","Christian","Judaism","Buddhism","Animism"]
                l9 = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu & Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]
                l10 = ["CSE","IT","EE","ME","ECE","CHE"]

                L1 = Label(group1.interior(), text="Employee Code", font=fe).grid(row=1, column=0, padx=10, pady=10,
                                                                                  sticky='e')
                E00 = Entry(group1.interior())
                E00.grid(row=1, column=1, padx=10, pady=10)
                Authority = Label(tab1, text="UnKnown Employee", font=f, style="BW.TLabel")
                Authority.grid(row=7, column=5)
                root.after(1, Auth_update)
                L3 = Label(group1.interior(), text="First Name:", font=f).grid(row=2, column=0, padx=10, pady=10)
                E1 = Entry(group1.interior())
                E1.grid(row=2, column=1, padx=10, pady=10)
                L4 = Label(group1.interior(), text="Middle Name:", font=f).grid(row=2, column=2, padx=10, pady=10,
                                                                                sticky='e')
                E2 = Entry(group1.interior())
                E2.grid(row=2, column=3, padx=10, pady=10)
                L5 = Label(group1.interior(), text="Last Name:", font=f).grid(row=2, column=4, padx=10, pady=10,
                                                                              sticky='e')
                E3 = Entry(group1.interior())
                E3.grid(row=2, column=5, padx=10, pady=10)
                L6 = Label(group1.interior(), text="Date of Birth:", font=f).grid(row=3, column=0, padx=10, pady=10)
                E4 = Entry(group1.interior())
                E4.grid(row=3, column=1, padx=10, pady=10)
                E4.insert(0, "DD-MM-YYYY")
                L6 = Label(group1.interior(), text="Religion:", font=f).grid(row=3, column=2, padx=10, pady=10)
                C3 = Combobox(group1.interior(), values=l8, height=4, textvariable=religion).grid(row=3, column=3, padx=10, pady=10)
                L7 = Label(group1.interior(), text="Gender:", font=f).grid(row=3, column=4, padx=10, pady=10)
                RD1 = Radiobutton(group1.interior(), text="Male", variable=gender, value=1, style='TRadiobutton')
                RD1.grid(row=3, column=5, padx=10, pady=10)
                RD2 = Radiobutton(group1.interior(), text="Female", variable=gender, value=2, style='TRadiobutton')
                RD2.grid(row=3, column=6, padx=10, pady=10)
                L8 = Label(group1.interior(), text="Caste:", font=f).grid(row=5, column=0, padx=10, pady=10)
                C = Combobox(group1.interior(), values=l1, height=2, textvariable=caste).grid(row=5, column=1, padx=10,
                                                                                              pady=10)
                LL1 = Label(group1.interior(), text="Blood Group:", font=f).grid(row=5, column=2, padx=10, pady=10)
                EE1 = Entry(group1.interior())
                EE1.grid(row=5, column=3, padx=10, pady=10)

                group2 = Pmw.Group(tab1, tag_text="PRESENT ADDRESS")
                group2.grid(row=7, column=0, padx=20, pady=20, sticky='WN')

                L10 = Label(group2.interior(), text="House No.:", font=f).grid(row=7, column=0, padx=10, pady=10)
                E6 = Entry(group2.interior())
                E6.grid(row=7, column=1, padx=10, pady=10)
                L11 = Label(group2.interior(), text="Street:", font=f).grid(row=7, column=2, padx=10, pady=10)
                E7 = Entry(group2.interior())
                E7.grid(row=7, column=3, padx=10, pady=10)
                L12 = Label(group2.interior(), text="Land Mark:", font=f).grid(row=7, column=4, padx=10, pady=10)
                E8 = Entry(group2.interior())
                E8.grid(row=7, column=5, padx=10, pady=10)
                L13 = Label(group2.interior(), text="City:", font=f).grid(row=8, column=0, padx=10, pady=10)
                E9 = Entry(group2.interior())
                E9.grid(row=8, column=1, padx=10, pady=10)
                L14 = Label(group2.interior(), text="District:", font=f).grid(row=8, column=2, padx=10, pady=10)
                E10 = Entry(group2.interior())
                E10.grid(row=8, column=3, padx=10, pady=10)
                L15 = Label(group2.interior(), text="State:", font=f).grid(row=8, column=4, padx=10, pady=10)
                C10 = Combobox(group2.interior(), values=l9, height=2, textvariable=state1).grid(row=8, column=5, padx=10, pady=10)
                L16 = Label(group2.interior(), text="Pin code:", font=f).grid(row=8, column=6, padx=10, pady=10)
                E12 = Entry(group2.interior())
                E12.grid(row=8, column=7, padx=10, pady=10)
                E12.insert(0, 0)

                L11 = Label(tab1, text="Do you have different permanent address? (Press the button to unlock)")
                L11.grid(row=8, column=0, padx=10, sticky='wn')
                BB1 = Button(tab1, text="Yes,I have.", command=k_func)
                BB1.grid(row=8, column=0)
                BB01 = Button(tab1, text="No,I don't", command=k_func_no)
                BB01.grid(row=8, column=0, sticky='ne')

                group3 = Pmw.Group(tab1, tag_text="PERMANENT ADDRESS")
                group3.grid(row=9, column=0, padx=20, pady=20, sticky='WN')

                L18 = Label(group3.interior(), text="House No.:", font=f).grid(row=11, column=0, padx=10, pady=10)
                E13 = Entry(group3.interior())
                E13.grid(row=11, column=1, padx=10, pady=10)
                E13.config(state="disabled")
                L19 = Label(group3.interior(), text="Street:", font=f).grid(row=11, column=2, padx=10, pady=10)
                E14 = Entry(group3.interior())
                E14.grid(row=11, column=3, padx=10, pady=10)
                E14.config(state="disabled")
                L20 = Label(group3.interior(), text="Land Mark:", font=f).grid(row=11, column=4, padx=10, pady=10)
                E15 = Entry(group3.interior())
                E15.grid(row=11, column=5, padx=10, pady=10)
                E15.config(state="disabled")
                L21 = Label(group3.interior(), text="City:", font=f).grid(row=12, column=0, padx=10, pady=10)
                E16 = Entry(group3.interior())
                E16.grid(row=12, column=1, padx=10, pady=10)
                E16.config(state="disabled")
                L22 = Label(group3.interior(), text="District:", font=f).grid(row=12, column=2, padx=10, pady=10)
                E17 = Entry(group3.interior())
                E17.grid(row=12, column=3, padx=10, pady=10)
                E17.config(state="disabled")
                L23 = Label(group3.interior(), text="State:", font=f).grid(row=12, column=4, padx=10, pady=10)
                C11 = Combobox(group3.interior(), values=l9, height=2, textvariable=state2).grid(row=12, column=5, padx=10, pady=10)

                L24 = Label(group3.interior(), text="Pin code:", font=f).grid(row=12, column=6, padx=10, pady=10)
                E19 = Entry(group3.interior())
                E19.grid(row=12, column=7, padx=10, pady=10)
                E19.insert(0, 0)
                E19.config(state="disabled")

                group4 = Pmw.Group(tab1, tag_text="CONTACT DETAILS")
                group4.grid(row=10, column=0, padx=20, pady=20, sticky='WN')

                L26 = Label(group4.interior(), text="Mobile No.:", font=f).grid(row=11, column=0, padx=10, pady=10)
                E20 = Entry(group4.interior())
                E20.grid(row=11, column=1, padx=10, pady=10)
                E20.insert(0, 0)
                L27 = Label(group4.interior(), text="Alternative Mobile No.:", font=f).grid(row=11, column=2, padx=10,
                                                                                            pady=10)
                E21 = Entry(group4.interior())
                E21.grid(row=11, column=3, padx=10, pady=10)
                E21.insert(0, 0)
                LL2 = Label(group4.interior(), text="Email:", font=f).grid(row=11, column=4, padx=10, pady=10)
                EE4 = Entry(group4.interior(), width=35)
                EE4.grid(row=11, column=5, padx=10, pady=10)

                group5 = Pmw.Group(tab1, tag_text="ORIGINALITY DETAILS")
                group5.grid(row=0, column=5, padx=20, pady=20, sticky='EN')
                Pmw.Color.changecolor(tab1, background='cyan', foreground="black")

                L28 = Label(group5.interior(), text="Signature:", font=f).grid(row=1, column=5, padx=10, pady=10)
                B1 = Button(group5.interior(), text="UPLOAD", command=sign).grid(row=1, column=6, padx=10, pady=10)
                EE2 = Entry(group5.interior())
                EE2.grid(row=1, column=7, padx=10, pady=10)
                L29 = Label(group5.interior(), text="Photo:", font=f).grid(row=2, column=5, padx=10, pady=10)
                B2 = Button(group5.interior(), text="UPLOAD", command=photo).grid(row=2, column=6, padx=10, pady=10)
                EE3 = Entry(group5.interior())
                EE3.grid(row=2, column=7, padx=10, pady=10)

                BB19 = Button(tab1, text="EDIT", command=edit1, style="TButton")
                BB19.grid(row=9, column=5, padx=10, pady=10)
                BB2 = Button(tab1, text="SUBMIT", command=submit1)
                BB2.grid(row=10, column=5)
                BB30 = Button(tab1, text="DELETE", command=delete)
                BB30.grid(row=11, column=5)
                Bdel1 = Button(tab1, text="DISPLAY", command=display1).grid(row=9, column=5, padx=10, pady=10,
                                                                            sticky='s')

                # Tab-9----------------------------------------------------------------------------------------------------------------------
                tab9 = ttk.Frame(tabcontrol)
                tabcontrol.add(tab9, text="Legal Verification and Joining Details")
                Authority1 = Label(tab9, text="UnKnown Employee", font=f, style="BW.TLabel")
                Authority1.grid(row=0, column=0, padx=20, pady=10, sticky='e')
                root.after(1, Auth_update)
                group14 = Pmw.Group(tab9, tag_text="Legal Documents Details")
                group14.grid(row=0, column=0, padx=10, pady=10, sticky='WN')
                LL6 = Label(group14.interior(), text="Document Name", font=f).grid(row=0, column=0, padx=10, pady=10)
                C7 = Combobox(group14.interior(), values=l4, height=3, textvariable=docname)
                C7.grid(row=1, column=0, padx=10, pady=10)
                LL7 = Label(group14.interior(), text="Document ID Number", font=f).grid(row=0, column=1, padx=10,
                                                                                        pady=10)
                EE5 = Entry(group14.interior(), width=30)
                EE5.grid(row=1, column=1, padx=10, pady=10)
                LL8 = Label(group14.interior(), text="Upload respective document", font=f).grid(row=0, column=2,
                                                                                                padx=10, pady=10)
                BB11 = Button(group14.interior(), text="UPLOAD", command=legal_upload)
                BB11.grid(row=1, column=2, padx=10, pady=10)
                BB20 = Button(group14.interior(), text="EDIT", command=edit2).grid(row=2, column=0, padx=10, pady=10)
                BB12 = Button(group14.interior(), text="SUBMIT", command=submit10).grid(row=2, column=1, padx=10,
                                                                                        pady=10)
                BB13 = Button(group14.interior(), text="ADD MORE", command=addmore10).grid(row=2, column=2, padx=10,
                                                                                           pady=10)
                Bdel2 = Button(group14.interior(), text="DISPLAY", command=display2).grid(row=2, column=3, padx=10,
                                                                                          pady=10)
                Bdele1 = Button(group14.interior(), text="DELETE", command=delete2).grid(row=2, column=4, padx=10,
                                                                                         pady=10)

                text9 = Text(tab9, width=69, height=3, wrap=WORD, padx=10, pady=10, bd=1)
                text9.grid(row=4, column=0, padx=10, pady=10, sticky='WN')
                text9.insert(0.0, "Document Name || Document ID Number")

                group15 = Pmw.Group(tab9, tag_text="Bank Account Details")
                group15.grid(row=6, column=0, padx=10, pady=10, sticky='WN')
                LL9 = Label(group15.interior(), text="Bank Account No. ", font=f).grid(row=6, column=0, padx=10,
                                                                                       pady=10)
                EE6 = Entry(group15.interior())
                EE6.grid(row=7, column=0, padx=10, pady=10)
                LL10 = Label(group15.interior(), text="Name of the Bank", font=f).grid(row=6, column=1, padx=10,
                                                                                       pady=10)
                EE7 = Entry(group15.interior())
                EE7.grid(row=7, column=1, padx=10, pady=10)
                LL11 = Label(group15.interior(), text="Branch Code", font=f).grid(row=6, column=2, padx=10, pady=10)
                EE8 = Entry(group15.interior())
                EE8.grid(row=7, column=2, padx=10, pady=10)
                LL12 = Label(group15.interior(), text="IFSC code", font=f).grid(row=6, column=3, padx=10, pady=10)
                EE9 = Entry(group15.interior())
                EE9.grid(row=7, column=3, padx=10, pady=10)
                LL19 = Label(group15.interior(), text="Upload Respective Document", font=f).grid(row=6, column=4,
                                                                                                 padx=10, pady=10)
                BB18 = Button(group15.interior(), text="UPLOAD", command=bank_upload)
                BB18.grid(row=7, column=4, padx=10, pady=10)
                BB14 = Button(group15.interior(), text="SUBMIT", command=submit11)
                BB14.grid(row=8, column=3, padx=10, pady=10)
                BB21 = Button(group15.interior(), text="EDIT", command=edit3).grid(row=8, column=4, padx=10, pady=10)
                Bdel3 = Button(group15.interior(), text="DISPLAY", command=display3).grid(row=8, column=5, padx=10,
                                                                                          pady=10)
                Bdele2 = Button(group15.interior(), text="DELETE", command=delete3).grid(row=8, column=6, padx=10,
                                                                                         pady=10)

                group16 = Pmw.Group(tab9, tag_text="Institution Joining Details")
                group16.grid(row=9, column=0, padx=10, pady=10, sticky='WN')
                LL13 = Label(group16.interior(), text="Course type", font=f).grid(row=9, column=0, padx=10, pady=10)
                C8 = Combobox(group16.interior(), values=l5, height=2, textvariable=coursetype)
                C8.grid(row=10, column=0, padx=10, pady=10)
                LL14 = Label(group16.interior(), text="Department", font=f).grid(row=9, column=1, padx=10, pady=10)
                C12 = Combobox(group16.interior(), values=l10, height=2, textvariable=dept1).grid(row=10, column=1, padx=10, pady=10)
                LL15 = Label(group16.interior(), text="Designation", font=f).grid(row=9, column=3, padx=10, pady=10)
                C9 = Combobox(group16.interior(), values=l6, height=3, textvariable=designation)
                C9.grid(row=10, column=3, padx=10, pady=10)
                LL16 = Label(group16.interior(), text="Subject Specilization", font=f).grid(row=9, column=4, padx=10,
                                                                                            pady=10)
                EE11 = Entry(group16.interior())
                EE11.grid(row=10, column=4, padx=10, pady=10)
                LL17 = Label(group16.interior(), text="Date of Joining", font=f).grid(row=9, column=5, padx=10, pady=10)
                EE12 = Entry(group16.interior())
                EE12.grid(row=10, column=5, padx=10, pady=10)
                EE12.insert(0, "DD-MM-YYYY")
                LL18 = Label(group16.interior(), text="Upload Respective Document", font=f).grid(row=9, column=6,
                                                                                                 padx=10, pady=10)
                BB15 = Button(group16.interior(), text="UPLOAD", command=joining_upload)
                BB15.grid(row=10, column=6, padx=10, pady=10)
                BB22 = Button(group16.interior(), text="EDIT", command=edit4).grid(row=11, column=4, padx=10, pady=10)
                BB16 = Button(group16.interior(), text="SUBMIT", command=submit12)
                BB16.grid(row=11, column=5, padx=10, pady=10)
                BB17 = Button(group16.interior(), text="ADD MORE", command=addmore11)
                BB17.grid(row=11, column=6, padx=10, pady=10)
                Bdel4 = Button(group16.interior(), text="DISPLAY", command=display4).grid(row=11, column=7, padx=10,
                                                                                          pady=10)
                Bdele3 = Button(group16.interior(), text="DELETE", command=delete4).grid(row=11, column=8, padx=10,
                                                                                         pady=10)
                text10 = Text(tab9, width=90, height=3, wrap=WORD, padx=10, pady=10, bd=1)
                text10.grid(row=12, column=0, padx=10, pady=10, sticky='WN')
                text10.insert(0.0,
                              "Course type || Department || Designation || Subject Specilization || Date of Joining")
                Pmw.Color.changecolor(tab9, background='cyan', foreground="black")

                # Tab-2----------------------------------------------------------------------------------------------------------------------
                tab2 = ttk.Frame(tabcontrol)
                tabcontrol.add(tab2, text="Academic Achievements")
                group6 = Pmw.Group(tab2, tag_text="ACADEMIC QUALIFICATIONS")
                group6.grid(row=0, column=0, padx=10, pady=10, sticky='WN')
                Authority2 = Label(tab2, text="UnKnown Employee", font=f, style="BW.TLabel")
                Authority2.grid(row=4, column=0, padx=100, sticky='e')
                root.after(1, Auth_update)

                L30 = Label(group6.interior(), text="Degree Obtained", font=f).grid(row=1, column=0, padx=10, pady=10)
                L31 = Label(group6.interior(), text="University/Board", font=f).grid(row=1, column=1, padx=10, pady=10)
                L32 = Label(group6.interior(), text="Institution", font=f).grid(row=1, column=2, padx=10, pady=10)
                L33 = Label(group6.interior(), text="Year of Passing", font=f).grid(row=1, column=3, padx=10, pady=10)
                L34 = Label(group6.interior(), text="Marks in Percentage", font=f).grid(row=1, column=4, padx=10,
                                                                                        pady=10)
                L35 = Label(group6.interior(), text="Remarks", font=f).grid(row=1, column=5, padx=10, pady=10)

                CC1 = Combobox(group6.interior(), values=l7, height=3, textvariable=degree)
                CC1.grid(row=2, column=0, padx=10, pady=10)
                E22 = Entry(group6.interior(), width=31)
                E22.grid(row=3, column=0, padx=10, pady=10)
                E22.config(state="disabled")
                E22.insert(0, " ")
                root.after(1, degree_update)
                E23 = Entry(group6.interior(), width=31)
                E23.grid(row=2, column=1, padx=10, pady=10)
                E24 = Entry(group6.interior(), width=31)
                E24.grid(row=2, column=2, padx=10, pady=10)
                E25 = Entry(group6.interior(), width=31)
                E25.grid(row=2, column=3, padx=10, pady=10)
                E25.insert(0, 'DD-MM-YYYY')
                E26 = Entry(group6.interior(), width=31)
                E26.grid(row=2, column=4, padx=10, pady=10)
                E26.insert(0, 0)
                E27 = Entry(group6.interior(), width=31)
                E27.grid(row=2, column=5, padx=10, pady=10)

                BB3 = Button(group6.interior(), text="Upload Document for each", command=Academic_upload).grid(row=3,
                                                                                                               column=2,
                                                                                                               padx=10,
                                                                                                               pady=10)
                BB23 = Button(group6.interior(), text="EDIT", command=edit5).grid(row=3, column=3, padx=10, pady=10)
                B4 = Button(group6.interior(), text="SUBMIT", command=submit2).grid(row=3, column=4, padx=10, pady=10)
                Bdel5 = Button(group6.interior(), text="DISPLAY", command=display5).grid(row=4, column=4, padx=10,
                                                                                         pady=10)
                B5 = Button(group6.interior(), text="ADD MORE", command=addmore2).grid(row=3, column=5, padx=10,
                                                                                       pady=10)
                Bdele4 = Button(group6.interior(), text="DELETE", command=delete5).grid(row=4, column=5, padx=10,
                                                                                        pady=10)

                text1 = Text(tab2, width=95, height=5, wrap=WORD, padx=10, pady=10, bd=1)
                text1.grid(row=4, column=0, padx=10, pady=10, sticky='WN')
                text1.insert(0.0,
                             "Degree obtained || University/Board || Institution || Year of Passing || Percentage || Remarks")

                group7 = Pmw.Group(tab2, tag_text="EXPERIENCE")
                group7.grid(row=5, column=0, padx=10, pady=10, sticky='WN')

                L36 = Label(group7.interior(), text="Experience Type(Teaching/Industry)", font=f).grid(row=6, column=0,
                                                                                                       padx=10, pady=10)
                L37 = Label(group7.interior(), text="Institution/Company", font=f).grid(row=6, column=1, padx=10,
                                                                                        pady=10)
                L38 = Label(group7.interior(), text="Address", font=f).grid(row=6, column=2, padx=10, pady=10)
                L39 = Label(group7.interior(), text="Designation", font=f).grid(row=6, column=3, padx=10, pady=10)
                L40 = Label(group7.interior(), text="Date of Join", font=f).grid(row=6, column=4, padx=10, pady=10)
                L41 = Label(group7.interior(), text="Date of Release", font=f).grid(row=6, column=5, padx=10, pady=10)
                L42 = Label(group7.interior(), text="Salary Drawn", font=f).grid(row=6, column=6, padx=10, pady=10)
                L43 = Label(group7.interior(), text="Remarks", font=f).grid(row=6, column=7, padx=10, pady=10)

                E28 = Entry(group7.interior(), width=30)
                E28.grid(row=7, column=0, padx=10, pady=10)
                E29 = Entry(group7.interior())
                E29.grid(row=7, column=1, padx=10, pady=10)
                E30 = Entry(group7.interior())
                E30.grid(row=7, column=2, padx=10, pady=10)
                E31 = Entry(group7.interior())
                E31.grid(row=7, column=3, padx=10, pady=10)
                E32 = Entry(group7.interior())
                E32.grid(row=7, column=4, padx=10, pady=10)
                E32.insert(0, 'DD-MM-YYYY')
                E33 = Entry(group7.interior())
                E33.grid(row=7, column=5, padx=10, pady=10)
                E33.insert(0, 'DD-MM-YYYY')
                E34 = Entry(group7.interior())
                E34.grid(row=7, column=6, padx=10, pady=10)
                E34.insert(0, 0)
                E35 = Entry(group7.interior())
                E35.grid(row=7, column=7, padx=10, pady=10)

                BB4 = Button(group7.interior(), text="Upload Document for each", command=Experience_upload).grid(row=8,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=10)
                BB24 = Button(group7.interior(), text="EDIT", command=edit6).grid(row=8, column=3, padx=10, pady=10)
                B6 = Button(group7.interior(), text="SUBMIT", command=submit3).grid(row=8, column=4, padx=10, pady=10)
                Bdel6 = Button(group7.interior(), text="DISPLAY", command=display6).grid(row=8, column=5, padx=10,
                                                                                         pady=10)
                B7 = Button(group7.interior(), text="ADD MORE", command=addmore3).grid(row=8, column=6, padx=10,
                                                                                       pady=10, sticky='e')
                Bdele5 = Button(group7.interior(), text="DELETE", command=delete6).grid(row=8, column=7, padx=10,
                                                                                        pady=10, sticky='e')

                text2 = Text(tab2, width=105, height=3, wrap=WORD, padx=10, pady=10, bd=1)
                text2.grid(row=9, column=0, padx=10, pady=10, sticky='WN')
                text2.insert(0.0,
                             "Exp_Type || Institution || Address || Designation || Period_from || Period_to || Salary_drawn || Remarks")

                group8 = Pmw.Group(tab2, tag_text="SPECIAL ACHIEVEMENTS")
                group8.grid(row=10, column=0, padx=10, pady=10, sticky='WN')
                text3 = Text(group8.interior(), width=90, height=2, wrap=WORD, padx=10, pady=10, bd=1)
                text3.grid(row=10, column=0, padx=10, pady=10, sticky='WN')
                BB5 = Button(group8.interior(), text="Upload Document for each", command=Special_upload).grid(row=10,
                                                                                                              column=1,
                                                                                                              padx=10,
                                                                                                              pady=10)
                BB6 = Button(group8.interior(), text="SUBMIT", command=submit4).grid(row=10, column=2, padx=10, pady=10)
                Bdel7 = Button(group8.interior(), text="DISPLAY", command=display7).grid(row=10, column=3, padx=10,
                                                                                         pady=10)
                BB7 = Button(group8.interior(), text="ADD MORE", command=addmore4).grid(row=11, column=2, padx=10,
                                                                                        pady=10)
                Bdele6 = Button(group8.interior(), text="DELETE", command=delete7).grid(row=11, column=3, padx=10,
                                                                                        pady=10)
                Bedit = Button(group8.interior(), text="EDIT", command=edit12).grid(row=11, column=1, padx=10,
                                                                                        pady=10)
                Pmw.Color.changecolor(tab2, background='cyan', foreground="black")

                # Tab-3-----------------------------------------------------------------------------------------------------------------------
                tab3 = ttk.Frame(tabcontrol)
                tabcontrol.add(tab3, text="Leave Management")
                group9 = Pmw.Group(tab3, tag_text="LEAVE MANAGEMENT")
                group9.grid(row=0, column=0, padx=10, pady=10, sticky='WN')

                Authority3 = Label(tab3, text="UnKnown Employee", font=f, style="BW.TLabel")
                Authority3.grid(row=6, column=0, padx=100, sticky='e')
                root.after(1, Auth_update)

                L44 = Label(group9.interior(), text="Year", font=f).grid(row=0, column=0, padx=10, pady=10)
                C2 = Combobox(group9.interior(), values=l2, height=5, textvariable=leaveyear).grid(row=1, column=0,
                                                                                                   padx=10, pady=10)
                L45 = Label(group9.interior(), text='CL', font=f).grid(row=0, column=1, padx=10, pady=10)
                E36 = Entry(group9.interior())
                E36.grid(row=1, column=1, padx=10, pady=10)
                E36.insert(0, 0)
                L46 = Label(group9.interior(), text='ML', font=f).grid(row=0, column=2, padx=10, pady=10)
                E37 = Entry(group9.interior())
                E37.grid(row=1, column=2, padx=10, pady=10)
                E37.insert(0, 0)
                L47 = Label(group9.interior(), text='EL', font=f).grid(row=0, column=3, padx=10, pady=10)
                E38 = Entry(group9.interior())
                E38.grid(row=1, column=3, padx=10, pady=10)
                E38.insert(0, 0)
                L48 = Label(group9.interior(), text='SL', font=f).grid(row=0, column=4, padx=10, pady=10)
                E39 = Entry(group9.interior())
                E39.grid(row=1, column=4, padx=10, pady=10)
                E39.insert(0, 0)
                L49 = Label(group9.interior(), text='OD', font=f).grid(row=0, column=5, padx=10, pady=10)
                E40 = Entry(group9.interior())
                E40.grid(row=1, column=5, padx=10, pady=10)
                E40.insert(0, 0)
                L50 = Label(group9.interior(), text='Others', font=f).grid(row=0, column=6, padx=10, pady=10)
                E41 = Entry(group9.interior())
                E41.grid(row=1, column=6, padx=10, pady=10)
                E41.insert(0, 0)
                LL3 = Label(group9.interior(), text='Upload respective document', font=f).grid(row=0, column=7, padx=10,
                                                                                               pady=10)
                BB8 = Button(group9.interior(), text="UPLOAD", command=leave_upload).grid(row=1, column=7, padx=10,
                                                                                          pady=10)
                BB25 = Button(group9.interior(), text="EDIT", command=edit7).grid(row=2, column=4, padx=10, pady=10)
                B8 = Button(group9.interior(), text="SUBMIT", command=submit5).grid(row=2, column=5, padx=10, pady=10)
                Bdel8 = Button(group9.interior(), text="DISPLAY", command=display8).grid(row=2, column=6, padx=10,
                                                                                         pady=10, sticky='s')
                B9 = Button(group9.interior(), text="ADD MORE", command=addmore5).grid(row=2, column=7, padx=10,
                                                                                       pady=10)
                Bdele7 = Button(group9.interior(), text="DELETE", command=delete8).grid(row=3, column=6, padx=10,
                                                                                        pady=10, sticky='s')
                text4 = Text(tab3, width=152, height=3, wrap=WORD, padx=10, pady=10, bd=1)
                text4.grid(row=4, column=0, padx=10, pady=10, sticky='WN')
                text4.insert(0.0, "Year || CL || ML || EL || SL || OD || Others")
                Pmw.Color.changecolor(tab3, background='cyan', foreground="black")

                # Tab-4----------------------------------------------------------------------------------------------------------------------
                tab4 = ttk.Frame(tabcontrol)
                tabcontrol.add(tab4, text="Rewards/Penalty")
                group10 = Pmw.Group(tab4, tag_text="Rewards/Penalty Information")
                group10.grid(row=0, column=0, padx=10, pady=10, sticky='WN')
                Authority4 = Label(tab4, text="UnKnown Employee", font=f, style="BW.TLabel")
                Authority4.grid(row=7, column=5, padx=50, sticky='e')
                root.after(1, Auth_update)
                L51 = Label(group10.interior(), text="Date", font=f).grid(row=0, column=0, padx=10, pady=10)
                E42 = Entry(group10.interior())
                E42.grid(row=1, column=0, padx=10, pady=10)
                E42.insert(0, "DD-MM-YYYY")
                L52 = Label(group10.interior(), text="Description", font=f).grid(row=0, column=1, padx=10, pady=10)
                E43 = Entry(group10.interior(), width=70)
                E43.grid(row=1, column=1, padx=10, pady=10)
                L53 = Label(group10.interior(), text="Upload Respective document", font=f).grid(row=0, column=2,
                                                                                                padx=10, pady=10)
                B10 = Button(group10.interior(), text="UPLOAD", command=reward_upload).grid(row=1, column=2, padx=10,
                                                                                            pady=10)
                BB26 = Button(group10.interior(), text="EDIT", command=edit8).grid(row=2, column=1, padx=10, pady=10,
                                                                                   sticky='w')
                B11 = Button(group10.interior(), text="SUBMIT", command=submit6).grid(row=2, column=1, padx=10, pady=10)
                Bdel9 = Button(group10.interior(), text="DISPLAY", command=display9).grid(row=2, column=1, padx=10,
                                                                                          pady=10, sticky='e')
                B12 = Button(group10.interior(), text="ADD MORE", command=addmore6).grid(row=2, column=2, padx=10,
                                                                                         pady=10)
                Bdele8 = Button(group10.interior(), text="DELETE", command=delete9).grid(row=2, column=3, padx=10,
                                                                                         pady=10)
                text5 = Text(tab4, width=97, height=3, wrap=WORD, padx=10, pady=10, bd=1)
                text5.grid(row=4, column=0, padx=10, pady=10, sticky='WN')
                text5.insert(0.0, "Date || Description")
                Pmw.Color.changecolor(tab4, background='cyan', foreground="black")

                # Tab-5----------------------------------------------------------------------------------------------------------------------
                tab5 = ttk.Frame(tabcontrol)
                tabcontrol.add(tab5, text="Pay Scale details")
                group11 = Pmw.Group(tab5, tag_text="Pay Scale")
                group11.grid(row=0, column=0, padx=10, pady=10, sticky='WN')
                Authority5 = Label(tab5, text="UnKnown Employee", font=f, style="BW.TLabel")
                Authority5.grid(row=7, column=5, padx=10, sticky='e')
                root.after(1, Auth_update)
                L54 = Label(group11.interior(), text="Date of Pay", font=f).grid(row=0, column=0, padx=10, pady=10)
                E003=Entry(group11.interior())
                E003.grid(row=1, column=0,padx=10, pady=10)
                E003.insert(0,"DD-MM-YYYY")
                L55 = Label(group11.interior(), text='BASIC', font=f).grid(row=0, column=1, padx=10, pady=10)
                E44 = Entry(group11.interior())
                E44.grid(row=1, column=1, padx=10, pady=10)
                E44.insert(0, 0)
                L56 = Label(group11.interior(), text='DA', font=f).grid(row=0, column=2, padx=10, pady=10)
                E45 = Entry(group11.interior())
                E45.grid(row=1, column=2, padx=10, pady=10)
                E45.insert(0, 0)
                L57 = Label(group11.interior(), text='HRA', font=f).grid(row=0, column=3, padx=10, pady=10)
                E46 = Entry(group11.interior())
                E46.grid(row=1, column=3, padx=10, pady=10)
                E46.insert(0, 0)
                L58 = Label(group11.interior(), text='Others', font=f).grid(row=0, column=4, padx=10, pady=10)
                E47 = Entry(group11.interior())
                E47.grid(row=1, column=4, padx=10, pady=10)
                E47.insert(0, 0)
                LL4 = Label(group11.interior(), text='Upload respective document', font=f).grid(row=0, column=5,
                                                                                                padx=10, pady=10)
                BB9 = Button(group11.interior(), text="UPLOAD", command=pay_upload).grid(row=1, column=5, padx=10,
                                                                                         pady=10)
                BB27 = Button(group11.interior(), text="EDIT", command=edit9).grid(row=2, column=2, padx=10, pady=10)
                B13 = Button(group11.interior(), text="SUBMIT", command=submit7).grid(row=2, column=3, padx=10, pady=10,
                                                                                      sticky='ne')
                Bdel0 = Button(group11.interior(), text="DISPLAY", command=display10).grid(row=2, column=4, padx=10,
                                                                                           pady=10)
                B14 = Button(group11.interior(), text="ADD MORE", command=addmore7).grid(row=2, column=5, padx=10,
                                                                                         pady=10)
                Bdele9 = Button(group11.interior(), text="DELETE", command=delete10).grid(row=3, column=4, padx=10,
                                                                                          pady=10)
                text6 = Text(tab5, width=116, height=3, wrap=WORD, padx=10, pady=10, bd=1)
                text6.grid(row=4, column=0, padx=10, pady=10, sticky='WN')
                text6.insert(0.0, "Date || Basic || DA || HRA || Others")
                Pmw.Color.changecolor(tab5, background='cyan', foreground="black")

                # Tab-6---------------------------------------------------------------------------------------------------------------------
                tab6 = ttk.Frame(tabcontrol)
                tabcontrol.add(tab6, text="Subject Allocation")
                group12 = Pmw.Group(tab6, tag_text="Subject Allocation")
                group12.grid(row=0, column=0, padx=10, pady=10, sticky='WN')
                Authority6 = Label(tab6, text="UnKnown Employee", font=f, style="BW.TLabel")
                Authority6.grid(row=7, column=5, padx=10, sticky='e')
                root.after(1, Auth_update)
                L59 = Label(group12.interior(), text="Semester", font=f).grid(row=0, column=0, padx=10, pady=10)
                C4 = Combobox(group12.interior(), values=l3, height=4, textvariable=sem).grid(row=1, column=0, padx=10,
                                                                                              pady=10)
                L60 = Label(group12.interior(), text='Paper Code', font=f).grid(row=0, column=1, padx=10, pady=10)
                E48 = Entry(group12.interior())
                E48.grid(row=1, column=1, padx=10, pady=10)
                L61 = Label(group12.interior(), text='Paper Name', font=f).grid(row=0, column=2, padx=10, pady=10)
                E49 = Entry(group12.interior())
                E49.grid(row=1, column=2, padx=10, pady=10)
                L62 = Label(group12.interior(), text='Department', font=f).grid(row=0, column=3, padx=10, pady=10)
                C13 = Combobox(group12.interior(), values=l10, height=2, textvariable=dept2).grid(row=1, column=3, padx=10, pady=10)
                L63 = Label(group12.interior(), text='Year', font=f).grid(row=0, column=4, padx=10, pady=10)
                C5 = Combobox(group12.interior(), values=l2, height=4, textvariable=subyear).grid(row=1, column=4,
                                                                                                  padx=10, pady=10)
                LL5 = Label(group12.interior(), text='Upload respective document', font=f).grid(row=0, column=5,
                                                                                                padx=10, pady=10)
                BB10 = Button(group12.interior(), text="UPLOAD", command=subjectallot_upload).grid(row=1, column=5,
                                                                                                   padx=10, pady=10)
                BB28 = Button(group12.interior(), text="EDIT", command=edit10).grid(row=2, column=2, padx=10, pady=10)
                B15 = Button(group12.interior(), text="SUBMIT", command=submit8).grid(row=2, column=3, padx=10, pady=10,
                                                                                      sticky='ne')
                Bdel11 = Button(group12.interior(), text="DISPLAY", command=display11).grid(row=2, column=4, padx=10,
                                                                                            pady=10)
                B16 = Button(group12.interior(), text="ADD MORE", command=addmore8).grid(row=2, column=5, padx=10,
                                                                                         pady=10)
                Bdele10 = Button(group12.interior(), text="DELETE", command=delete11).grid(row=3, column=4, padx=10,
                                                                                           pady=10)
                text7 = Text(tab6, width=118, height=3, wrap=WORD, padx=10, pady=10, bd=1)
                text7.grid(row=4, column=0, padx=10, pady=10, sticky='WN')
                text7.insert(0.0, "Semester || Paper Code || Paper Name || Department || Year")
                Pmw.Color.changecolor(tab6, background='cyan', foreground="black")

                # Tab-7----------------------------------------------------------------------------------------------------------------------
                tab7 = ttk.Frame(tabcontrol)
                tabcontrol.add(tab7, text="Additional Responsibilities")
                group13 = Pmw.Group(tab7, tag_text="Additional Responsibilities")
                group13.grid(row=0, column=0, padx=10, pady=10, sticky='WN')
                Authority7 = Label(tab7, text="UnKnown Employee", font=f, style="BW.TLabel")
                Authority7.grid(row=7, column=5, padx=10, sticky='e')
                root.after(1, Auth_update)
                L64 = Label(group13.interior(), text='From Date', font=f).grid(row=0, column=0, padx=10, pady=10)
                E001 = Entry(group13.interior())
                E001.grid(row=1, column=0, padx=10, pady=10)
                E001.insert(0, "DD-MM-YYYY")
                L664 = Label(group13.interior(), text='To Date', font=f).grid(row=0, column=1, padx=10, pady=10)
                E002 = Entry(group13.interior())
                E002.grid(row=1, column=1, padx=10, pady=10)
                E002.insert(0, "DD-MM-YYYY")
                L65 = Label(group13.interior(), text="Description", font=f).grid(row=0, column=2, padx=10, pady=10)
                E51 = Entry(group13.interior(), width=70)
                E51.grid(row=1, column=2, padx=10, pady=10)
                L66 = Label(group13.interior(), text='Upload respective document', font=f).grid(row=0, column=3,
                                                                                                padx=10, pady=10)
                B17 = Button(group13.interior(), text="UPLOAD", command=addresp_upload).grid(row=1, column=3, padx=10,
                                                                                             pady=10)
                BB29 = Button(group13.interior(), text="EDIT", command=edit11).grid(row=2, column=2, padx=10, pady=10,
                                                                                    sticky='w')
                B18 = Button(group13.interior(), text="SUBMIT", command=submit9).grid(row=2, column=2, padx=10, pady=10)
                Bdel2 = Button(group13.interior(), text="DISPLAY", command=display12).grid(row=2, column=2, padx=10,
                                                                                           pady=10, sticky='e')
                B19 = Button(group13.interior(), text="ADD MORE", command=addmore9).grid(row=2, column=3, padx=10,
                                                                                         pady=10)
                Bdele11 = Button(group13.interior(), text="DELETE", command=delete12).grid(row=3, column=2, padx=10,
                                                                                           pady=10, sticky='e')
                text8 = Text(tab7, width=98, height=3, wrap=WORD, padx=10, pady=10, bd=1)
                text8.grid(row=4, column=0, padx=10, pady=10, sticky='WN')
                text8.insert(0.0, "From Date|| To Date || Description")
                Pmw.Color.changecolor(tab7, background='cyan', foreground="black")

                # Tab-8-----------------------------------------------------------------------------------------------------------------------
                tab8 = ttk.Frame(tabcontrol)
                tabcontrol.add(tab8, text="Updated Report")
                L67 = Label(tab8, text='GENERATE UPDATED REPORTS', font=f)
                L67.grid(row=0, column=3, padx=440, pady=20)
                B20 = Button(tab8, text="Details of a particular employee.", command=download_file1)
                B20.grid(row=1, column=3, padx=440, pady=20)
                B21 = Button(tab8, text="List of all employees in the institution.", command=query1)
                B21.grid(row=2, column=3, padx=440, pady=20)
                B22 = Button(tab8, text="List of employees working for more than 5 years.", command=query2)
                B22.grid(row=3, column=3, padx=440, pady=20)
                Pmw.Color.changecolor(tab8, background='cyan', foreground="black")

                # ------------------------------------------------------------------------------------------------------------------------------
                root.mainloop()
            except OSError:
                tkinter.messagebox.showinfo('Something went wrong!!!','Please read the instructions!!')
        else:
            tkinter.messagebox.showinfo('Warning!!','Please enter correct user id and password!!!')
    except MySQLdb.ProgrammingError:
        tkinter.messagebox.showinfo('Warning!!', 'Database doesnot exist!!!')
    except UnboundLocalError:
        tkinter.messagebox.showinfo('Warning!!', 'Please enter correct user id and password!!!')
    except FileNotFoundError:
        tkinter.messagebox.showinfo('Warning!!', 'Please do the Admin setup!!!')








    #--------------------------------------------------------------------------------------------------------------------------

def Exit():
    root2.destroy()
global use
global pae
root2=Tk()
e = Font(family="Arial", size=18, weight="bold", slant="roman", underline=1)
d = Font(family="Arial", size=13, weight="bold", slant="roman", underline=0)
root2.overrideredirect(1)
root2.title('Login!!')
root2.geometry('6000x2000')
root2.iconbitmap(r'diatmlogo.ico')
root2.configure(background='cyan')
path ="diatm-home-1024x444.jpg"
path2=Im.open(path)
pathcopy=path2.copy()
x=pathcopy.resize((1000,300))
img = ImageTk.PhotoImage(x)
panel = Label(root2, image = img)
head=Label(root2,text="WELCOME TO EMPLOYEE MANAGEMENT SYSTEM.",font=e,background="cyan",foreground="blue")
head.grid(row=0,column=0,padx=400,pady=20)
panel.grid(row=1,columnspan=1)
us=Label(root2,text="Username :",background="cyan",font=d).grid(row=2,column=0,padx=400,pady=10)
pa=Label(root2,text="Password :",background="cyan",font=d).grid(row=4,column=0,padx=400,pady=10)
use=Entry(root2,width=30)
use.grid(row=3,column=0,padx=400,pady=10)
pae=Entry(root2,show="*",width=30)
pae.grid(row=5,column=0,padx=400,pady=10)
style=ttk.Style()
style.configure("TButton", font=('arial', 12, 'bold'), foreground='red', background='red',borderwidth='4',width=20)
b1=Button(root2,text="LOGIN",command=login_cred).grid(row=6,column=0,padx=400,pady=10)
b2=Button(root2,text="ADMIN SETUP",command=signup).grid(row=7,column=0,padx=400,pady=10)
b3=Button(root2,text="Exit",command=Exit).grid(row=8,column=0,padx=400,pady=10)
root2.mainloop()
