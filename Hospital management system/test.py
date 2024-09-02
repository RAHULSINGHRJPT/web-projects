from tkinter import * 
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector 

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()
        


        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        #===========================Data Frames===================================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Prescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        #============================== buttons frame===============================
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        #============================== Details frame================================
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        #===============================Dataframeleft=========================================
        lblNameTable = Label(DataframeLeft, text="Name of Table", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblNameTable.grid(row=0, column=0, sticky=W)

        comNametablet = ttk.Combobox(DataframeLeft, textvariable=self.Nameoftablets,state="readonly",
                                                            font=("times new roman", 12, "bold"), width=33)
        comNametablet["values"] = ("Nice", "Corona", "Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0, column=1)

        lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="Reference No:", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.ref, width=35)
        txtref.grid(row=1, column=1)

        lbDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=4)
        lbDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.Dose, width=35)
        txtDose.grid(row=2, column=1)

        lblNoOftablets = Label(DataframeLeft, font=("arial", 12, "bold"), text="No of tablets:", padx=2, pady=6)
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.NumberofTablets, width=35)
        txtNoOftablets.grid(row=3, column=1)

        lblLot = Label(DataframeLeft, font=("arial", 12, "bold"), text="Lot No:", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.Lot,width=35)
        txtLot.grid(row=4, column=1)

        lblissueDate = Label(DataframeLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.Issuedate,width=35)
        txtissueDate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft, font=("arial", 12, "bold"), text="Expiry Date:", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.ExpDate, width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=4)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(DataframeLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.sideEffect,width=35)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherinfo = Label(DataframeLeft, font=("arial", 12, "bold"), text="Further Information:", padx=2)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)
        txtFurtherinfo = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.FurtherInformation,width=35)
        txtFurtherinfo.grid(row=0, column=3)

        lblBloodPressure = Label(DataframeLeft, font=("arial", 12, "bold"), text="Blood Pressure:", padx=2, pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.DrivingUsingMachine,width=35)
        txtBloodPressure.grid(row=1, column=3)

        lblStorage = Label(DataframeLeft, font=("arial", 12, "bold"), text="Storage Advice:", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.StorageAdvice,width=35)
        txtStorage.grid(row=2, column=3)

        lblMedicine = Label(DataframeLeft, font=("arial", 12, "bold"), text="Medicine:", padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.HowToUseMedication ,width=35)
        txtMedicine.grid(row=3, column=3)

        lblPatientId = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Id:", padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(DataframeLeft, font=("arial", 12, "bold"), text="NHS Number:", padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientName = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Name:", padx=2, pady=6)
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.PatientName, width=35)
        txtPatientName.grid(row=6, column=3)

        lblDateOfBirth = Label(DataframeLeft, font=("arial", 12, "bold"), text="Date of Birth:", padx=2, pady=6)
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.DateOfBirth, width=35)
        txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Address:", padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.PatientAddress, width=35)
        txtPatientAddress.grid(row=8, column=3)

        #=============================================DataframeRight=============================================
        self.txtPrescription = Text(DataframeRight, font=("arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        #=============================================Buttons========================================================
        btnPrescription = Button(Buttonframe, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"), width=23)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"), width=23)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe,command=self.update_data ,text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=23)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Delete", command=self.idelete,bg="green", fg="white", font=("arial", 12, "bold"), width=23)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, command=self.clear,text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=23)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, command=self.iExit,text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=23)
        btnExit.grid(row=0, column=5)

        #====================================================Table================================================
        #==========================Scrollbar============================================
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(
            Detailsframe,
            columns=(
                "nameoftablets", "ref", "dose", "nooftablets", "lot", 
                "issuedate", "expdate", "dailydose", "storage", 
                "nhsnumber", "pname", "dob", "address"
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablets", text="Name Of Tablets")
        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill=BOTH, expand=1)

        # Add more headings for other columns if necessary
        self.hospital_table.heading("ref", text="Reference No")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot No")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Expiry Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="Date of Birth")
        self.hospital_table.heading("address", text="Address")


        self.hospital_table["show"]="headings"

        self.hospital_table.pack(fill=BOTH,expand=1)


        # Set column widths
        self.hospital_table.column("nameoftablets", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=150)
 
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)


        self.fatch_data()
      #===================================functionality declare=============================================



    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error", "Please fill all fields")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                        self.Nameoftablets.get(),
                                                                                                        self.ref.get(),
                                                                                                        self.Dose.get(),
                                                                                                        self.NumberofTablets.get(),
                                                                                                        self.Lot.get(),
                                                                                                        self.Issuedate.get(),
                                                                                                        self.ExpDate.get(),
                                                                                                        self.DailyDose.get(),
                                                                                                        self.StorageAdvice.get(),
                                                                                                        self.nhsNumber.get(),
                                                                                                        self.PatientName.get(),
                                                                                                        self.DateOfBirth.get(),
                                                                                                        self.PatientAddress.get()

                                                                                                     ))    
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been saved")


            def update(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("Update hospital set Nameoftablets=%s,Dose=%s,No_of_Tablets=%s,Lot=%s,Issue_Date=%s,Exp_Data=%s,Daily_date=%s,Storage=%s,NHSNumber=%s,Patient_name=%s,DOB=%s,Address=%s where Refrence_No=%s" (

                                                                                                            self.Nameoftablets.get(),
                                                                                                            self.Dose.get(),
                                                                                                            self.NumberofTablets.get(),
                                                                                                            self.Lot.get(),
                                                                                                            self.Issuedate.get(),
                                                                                                            self.ExpDate.get(),
                                                                                                            self.DailyDose.get(),
                                                                                                            self.StorageAdvice.get(),
                                                                                                            self.nhsNumber.get(),
                                                                                                            self.PatientName.get(),
                                                                                                            self.DateOfBirth.get(),
                                                                                                            self.PatientAddress.get(),
                                                                                                            self.ref.get()

                                                                                                            
                                                                                                                ))



            def fatch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
                mmy_cursor=conn.cursor()
                my_cursor.execute("select * from hospital")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.hospital_table.delete(*self.hospital_table.get_children())
                    for row in rows:
                        self.hospital_table.insert('',END,values=row)
                        conn.comit()
                        conn.close()


            def get_cursor(self,event=""):
                cursor_row=self.hospital_table.focus()
                content=self.hospital_table.item(cursor_row)
                row=content["values"]
                self.Nameoftablets.set(row[0])
                self.ref.set(row[1])
                self.Dose.set(row[2])
                self.NumberofTablets.set(row[3])
                self.Lot.set(row[4])
                self.Issuedate.set(row[5])
                self.ExpDate.set(row[6])
                self.DailyDose.set(row[7])
                self.StorageAdvice.set(row[8])
                self.nhsNumber.set(row[9])
                self.PatientName.set(row[10])
                self.DateOfBirth.set(row[11])
                self.PatientAddress.set(row[12])
                self.Entry.delete(0,END)


            def iPrescription(self):
                self.txtPrescription.insert(END,"Name of Tablets: \t\t\t" + self.Nameoftablets.get() + "\n")
                self.txtPrescription.insert(END,"Reference Number: \t\t\t" + self.ref.get() + "\n")
                self.txtPrescription.insert(END,"Dose: \t\t\t\t" + self.Dose.get() + "\n")
                self.txtPrescription.insert(END,"Number of Tablets: \t\t\t" + self.Numberoftablets.get() + "\n")
                self.txtPrescription.insert(END,"Lot: \t\t\t\t" + self.Lot.get() + "\n")
                self.txtPrescription.insert(END,"Issued Date: \t\t\t" + self.Issuedate.get() + "\n")
                self.txtPrescription.insert(END,"Expiry Date: \t\t\t" + self.ExpDate.get() + "\n")
                self.txtPrescription.insert(END,"Daily Dose: \t\t\t" + self.DailyDose.get() + "\n")
                self.txtPrescription.insert(END,"Storage Advice: \t\t\t" + self.StorageAdvice.get() + "\n")
                self.txtPrescription.insert(END,"NHS Number: \t\t\t" + self.DrivingUsingMachine.get() + "\n")
                self.txtPrescription.insert(END,"Patient Name: \t\t\t" + self.PatientName.get() + "\n")
                self.txtPrescription.insert(END,"Date of Birth: \t\t\t" + self.DateofBirth.get() + "\n")
                self.txtPrescription.insert(END,"Patient Address: \t\t\t" + self.PatientAddress.get() + "\n")
                self.txtPrescription.insert(END,"Prescribed By: \t\t\t" + self.nhsNumber.get() + "\n")
                self.txtPrescription.insert(END,"Prescription ID: \t\t\t" + self.PatientName.get() + "\n")
                self.txtPrescription.insert(END,"Prescription ID: \t\t\t" + self.DateofBirth.get() + "\n")
                self.txtPrescription.insert(END,"Prescription ID: \t\t\t" + self.sideEffect.get() + "\n")



            def idelete(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
                my_cursor=conn.cursor()
                query="delete from hospital where Refrence_No=%s"
                value=(self.ref.get(),)
                my_cursor.execute(query,value)



                conn.comit()
                conn.close()
                self.fatch_data()
                messagebox.showinfo("Delete","Patient has been deleted successfully")


            def clear(self):
                self.Nameoftablets.set("")
                self.ref.set("")
                self.Dose.set("")
                self.Numberoftablets.set("")
                self.Lot.set("")
                self.Issuedate.set("")
                self.ExpDate.set("")
                self.DailyDose.set("")
                self.StorageAdvice.set("")
                self.DrivingUsingMachine.set("")
                self.PatientName.set("")
                self.DateofBirth.set("")
                self.PatientAddress.set("")
                self.nhsNumber.set("")
                self.PatientName.set("")
                self.DateofBirth.set("")
                self.sideEffect.set("")
                self.txtPrescription.delete('1.0',END)
            

            def iExit(self):
                iExit=messagebox.askyesno("Hospital management systeem","Confirm you want to exit")
                if iExit > 0:
                    root.destroy()
                    return





root = Tk()
ob = Hospital(root)
root.mainloop()
