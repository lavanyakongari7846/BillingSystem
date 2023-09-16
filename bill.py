from tkinter import * 
import math,random,os
from tkinter import messagebox
import MongoQueries as mq


mq.delete_db_in_mongo()

mq.create_db_in_mongo('Bill_System')

mq.create_table_in_mongo('Bills')

values = {}        

class Bill_App:
    def __init__(self,root):
          self.root=root
          self.root.geometry("1350x770+0+0")
          self.root.title("Billing System")
          bg_color="#074465"
          title=Label(self.root,text="Billing System",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
          ###-------------------variables------------------
          self.soap=IntVar()
          self.face_cream=IntVar()
          self.face_wash=IntVar()
          self.spray=IntVar()
          self.gel=IntVar()
          self.lotion=IntVar()

          self.rice=IntVar()
          self.food_oil=IntVar()
          self.daal=IntVar()
          self.wheat=IntVar()
          self.sugar=IntVar()
          self.tea=IntVar()

          self.maza=IntVar()
          self.cock=IntVar()
          self.frooti=IntVar()
          self.thumbs_up=IntVar()
          self.limca=IntVar()
          self.sprite=IntVar()

          self.cosmetic_price=StringVar()
          self.grocery_price=StringVar()
          self.cold_drinks_price=StringVar()

          self.cosmetic_tax=StringVar()
          self.grocery_tax=StringVar()
          self.cold_drinks_tax=StringVar()

          self.c_name=StringVar()
          self.c_phone=StringVar()
          self.bill_number=StringVar()
          self.c_id=IntVar()
          x=random.randint(1000,9999)
          self.bill_number.set(str(x))         
          self.search_bill=StringVar()
          


          F1=LabelFrame(self.root,bd=2,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
          F1.place(x=0,y=80,relwidth=1)

          cname_label=Label(F1,text="Customer Name:",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
          cname_text=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)
         
          cphone_label=Label(F1,text="Phone Number:",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
          cphone_text=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

          cid_label=Label(F1,text="C_iD:",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
          cid_text=Entry(F1,width=15,textvariable=self.c_id,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)


          cbill_label=Label(F1,text="Bill No:",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=6,padx=20,pady=5)
          cbill_text=Entry(F1,width=15,textvariable=self.bill_number,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=8,padx=10,pady=5)
       
          #bill_button=Button(F1,text="Serach",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)

          #=========1st frame ==========

          F2=LabelFrame(self.root,bd=2,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
          F2.place(x=5,y=180,width=325,height=380)

          bath_label=Label(F2,text="Bath Soap:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
          bath_text=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

          face_cream_label=Label(F2,text="Face Cream:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
          face_cream_text=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

          face_wash_label=Label(F2,text="Face Wash:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
          face_wash_text=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

          hair_spray_label=Label(F2,text="Hair Spray:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
          hair_spray_text=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

          hair_gel_label=Label(F2,text="Hair Gel:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
          hair_gel_text=Entry(F2,width=10,textvariable=self.gel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

          body_lotion_label=Label(F2,text="Body Lotion:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
          body_lotion_text=Entry(F2,width=10,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


           #=========2nd frame ==========

          F3=LabelFrame(self.root,bd=2,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
          F3.place(x=340,y=180,width=325,height=380)

          rice_label=Label(F3,text="Rice:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
          rice_text=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

          food_oil_cream_label=Label(F3,text="Food Oil:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
          food_oil_cream_text=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

          daal_label=Label(F3,text="Daal:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
          daal_text=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

          wheat_label=Label(F3,text="Wheat:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
          wheat_spray_text=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

          sugar_label=Label(F3,text="Sugar:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
          hsugar_text=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

          tea_label=Label(F3,text="Tea:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
          tea_text=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


          #=========3rd frame ==========

          F4=LabelFrame(self.root,bd=2,relief=GROOVE,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
          F4.place(x=670,y=180,width=325,height=380)

          maza_label=Label(F4,text="Maza:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
          maza_text=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

          cock_label=Label(F4,text="Cock:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
          cock_text=Entry(F4,width=10,textvariable=self.cock,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

          frooti_label=Label(F4,text="Frooti:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
          frooti_text=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

          thumbs_up_label=Label(F4,text="Thumbs Up:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
          thumbs_up_text=Entry(F4,width=10,textvariable=self.thumbs_up,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

          limca_label=Label(F4,text="Limca:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
          limca_text=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

          sprite_label=Label(F4,text="Sprite:",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
          sprite_text=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


          #=============4th frame ==================
          F5=LabelFrame(self.root,bd=10,relief=GROOVE)
          F5.place(x=1010,y=180,width=330,height=380)

          bill_title=Label(F5,text="Bill Area",font="arial 15 ",bd=7,relief=GROOVE).pack(fill=X)
          scrol_y=Scrollbar(F5,orient=VERTICAL)
          self.textarea=Text(F5,yscrollcommand=scrol_y.set)
          scrol_y.pack(side=RIGHT,fill=Y)
          scrol_y.config(command=self.textarea.yview)
          self.textarea.pack(fill=BOTH,expand=1)

          


          F6=LabelFrame(self.root,bd=2,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
          F6.place(x=0,y=560,relwidth=1,height=220)

          m1_label=Label(F6,text="Total Cosmetic Price:",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
          m1_text=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1,sticky="w")

          m2_label=Label(F6,text="Total Grocery Price:",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
          m2_text=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1,sticky="w")

          m3_label=Label(F6,text="Total Cold Drinks Price:",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
          m3_text=Entry(F6,width=18,textvariable=self.cold_drinks_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1,sticky="w")



          c1_label=Label(F6,text="Cosmetic Tax:",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
          c1_text=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1,sticky="w")

          c2_label=Label(F6,text="Grocery Tax:",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
          c2_text=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1,sticky="w")

          c3_label=Label(F6,text="Cold Drinks Tax:",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
          c3_text=Entry(F6,width=18,textvariable=self.cold_drinks_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1,sticky="w")


          btn_frame=Frame(F6,bd=7,relief=GROOVE)
          btn_frame.place(x=760,width=580,height=190)
          


          total_button=Button(btn_frame,command=self.total,text="Total",bg="lightblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
          dis_button=Button(btn_frame,command=self.disp_one,text="Display",bg="lightblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=1,column=0,padx=5,pady=5)
          

          gerenate_bill_button=Button(btn_frame,command=self.bill_area,text="Generate Bill",bg="lightblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
          update_button=Button(btn_frame,command=self.update,text="Update",bg="lightblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=1,column=1,padx=5,pady=5)
          

          clear_button=Button(btn_frame,text="Clear",command=self.clear_data,bg="lightblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
          delete_button=Button(btn_frame,text="Delete",command=self.delete,bg="lightblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=1,column=2,padx=5,pady=5)

          exit_button=Button(btn_frame,text="Exit",command=self.exit_app,bg="lightblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
          sm_button=Button(btn_frame,text="DisplayAll",command=self.disp,bg="lightblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=1,column=3,padx=5,pady=5)
          self.welcome_bill()

          #=============5th frame ==================
            
          

          
    def total(self):
        global values
        self.c1_s_p=self.soap.get()*40
        self.c2_s_p=self.face_cream.get()*120
        self.c3_s_p=self.face_wash.get()*60
        self.c4_s_p=self.spray.get()*180
        self.c5_s_p=self.gel.get()*140
        self.c6_s_p=self.lotion.get()*180
        
        values["soap"]			= self.c1_s_p
        values["face_cream"]	        = self.c2_s_p
        values["face_wash"]		= self.c3_s_p
        values["spray"]			= self.c4_s_p
        values["gel"]			= self.c5_s_p
        values["lotion"]		= self.c6_s_p
        
        self.total_cosmetic_price=float(
                                    self.c1_s_p+
                                    self.c2_s_p+
                                    self.c3_s_p+
                                    self.c4_s_p+
                                    self.c5_s_p+
                                    self.c6_s_p
                                )
        self.cosmetic_price.set("Rs."+str(self.total_cosmetic_price))         
        self.c_tax=self.total_cosmetic_price*0.1
        self.cosmetic_tax.set("Rs."+str(self.c_tax))

        values["cosmetic_price"]	= self.total_cosmetic_price
        values["c_tax"  ]	        = self.c_tax 
        
        
        self.g1_r_p=self.rice.get()*80
        self.g2_r_p=self.food_oil.get()*160
        self.g3_r_p=self.daal.get()*60
        self.g4_r_p=self.wheat.get()*240
        self.g5_r_p=self.sugar.get()*45
        self.g6_r_p=self.tea.get()*150
        
        values["rice"]		= self.g1_r_p	
        values["food_oil"]	= self.g2_r_p
        values["daal"]		= self.g3_r_p	
        values["wheat"]		= self.g4_r_p	
        values["sugar"]		= self.g5_r_p	
        values["tea"]		= self.g6_r_p
                
        self.total_grocery_price=float(
                                    self.g1_r_p+
                                    self.g2_r_p+
                                    self.g3_r_p+
                                    self.g4_r_p+
                                    self.g5_r_p+
                                    self.g6_r_p
                                )
        self.grocery_price.set("Rs."+str(self.total_grocery_price))
        self.g_tax=self.total_grocery_price*0.05
        self.grocery_tax.set("Rs."+str(self.g_tax))
        
        values["grocery_price"]	= self.total_grocery_price	
        values["g_tax"]		= self.g_tax        
        
        
        self.d1_m_p=self.maza.get()*60
        self.d2_m_p=self.cock.get()*60
        self.d3_m_p=self.frooti.get()*50
        self.d4_m_p=self.thumbs_up.get()*45
        self.d5_m_p=self.limca.get()*40
        self.d6_m_p=self.sprite.get()*60
        self.total_cold_drinks_price=float(
                                    self.d1_m_p+
                                    self.d2_m_p+
                                    self.d3_m_p+
                                    self.d4_m_p+
                                    self.d5_m_p+
                                    self.d6_m_p
                                )
        values["maza"] 		= self.d1_m_p
        values["cock"] 		= self.d2_m_p
        values["frooti"] 	= self.d3_m_p
        values["thumbs_up"]     = self.d4_m_p
        values["limca"] 	= self.d5_m_p
        values["sprite"]	= self.d6_m_p


        
        self.cold_drinks_price.set("Rs."+str(self.total_cold_drinks_price))
        self.d_tax=self.total_cold_drinks_price*0.1
        self.cold_drinks_tax.set("Rs."+str(self.d_tax))

        values["tot_cold_drinks_price"] = self.total_cold_drinks_price
        values["cold_drinks_tax"]   = self.d_tax

 
        self.total_bill=float(self.total_cosmetic_price+
                              self.total_grocery_price+
                              self.total_cold_drinks_price+
                              self.c_tax+
                              self.g_tax+
                              self.d_tax
                              )

        values["total_bill"] = self.total_bill

        return values
        
        
        
       # 9420343173
    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t Welcome WebCode Retail \n")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_number.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n====================================")
        self.textarea.insert(END,f"\nProducts\t\tQTY\t    Price")
        self.textarea.insert(END,f"\n====================================")
        
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details required")
        elif self.cosmetic_price.get()=="Rs.0.0" and self.grocery_price.get()=="Rs.0.0" and self.cold_drinks_price.get()=="Rs.0.0":
             messagebox.showerror("Error","No Product Selected ")
        else:
            self.disp_bill()
            if self.soap.get()!=0:
                self.textarea.insert(END,f"\nBath Soap\t\t{self.soap.get()}\t\t{self.c1_s_p}")
                
            if self.face_cream.get()!=0:
                self.textarea.insert(END,f"\n Face Cream \t\t{self.face_cream.get()}\t\t{self.c2_s_p}")
                
            if self.face_wash.get()!=0:
                self.textarea.insert(END,f"\n Face Wash \t\t{self.face_wash.get()}\t\t{self.c3_s_p}")
                
            if self.spray.get()!=0:
                self.textarea.insert(END,f"\n Spray  \t\t{self.spray.get()}\t\t{self.c4_s_p}")
                
            if self.gel.get()!=0:
                self.textarea.insert(END,f"\n Hair Gel \t\t{self.gel.get()}\t\t{self.c5_s_p}")
                
            if self.lotion.get()!=0:
                self.textarea.insert(END,f"\n Lotion \t\t{self.lotion.get()}\t\t{self.c6_s_p}")
                
                
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n Rice  \t\t{self.rice.get()}\t\t{self.g1_r_p}")
                
            if self.food_oil.get()!=0:
                self.textarea.insert(END,f"\n Food Oil \t\t{self.food_oil.get()}\t\t{self.g2_r_p}")
                
            if self.daal.get()!=0:
                self.textarea.insert(END,f"\n Daal \t\t{self.daal.get()}\t\t{self.g3_r_p}")
                
            if self.wheat.get()!=0:
                self.textarea.insert(END,f"\n Wheat  \t\t{self.wheat.get()}\t\t{self.g4_r_p}")
                
            if self.sugar.get()!=0:
                self.textarea.insert(END,f"\n Sugar \t\t{self.sugar.get()}\t\t{self.g5_r_p}")
                
            if self.tea.get()!=0:
                self.textarea.insert(END,f"\n Tea \t\t{self.tea.get()}\t\t{self.g6_r_p}")
            
                
            if self.maza.get()!=0:
                self.textarea.insert(END,f"\n Maza  \t\t{self.maza.get()}\t\t{self.d1_m_p}")
                
            if self.cock.get()!=0:
                self.textarea.insert(END,f"\n Cock  \t\t{self.cock.get()}\t\t{self.d2_m_p}")
                
            if self.frooti.get()!=0:
                self.textarea.insert(END,f"\n Frooti \t\t{self.frooti.get()}\t\t{self.d3_m_p}")
                
            if self.thumbs_up.get()!=0:
                self.textarea.insert(END,f"\n Thumbs Up  \t\t{self.thumbs_up.get()}\t\t{self.d4_m_p}")
                
            if self.limca.get()!=0:
                self.textarea.insert(END,f"\n Limca \t\t{self.limca.get()}\t\t{self.d5_m_p}")
                
            if self.sprite.get()!=0:
                self.textarea.insert(END,f"\n Sprite \t\t{self.sprite.get()}\t\t{self.d6_m_p}")
                
                
            self.textarea.insert(END,f"\n------------------------------------------------------------------------")
            if self.cosmetic_tax.get()!="Rs.0.0":
                self.textarea.insert(END,f"\nCosmetic Tax  \t\t\t  {self.cosmetic_tax.get()}")
                
            if self.grocery_tax.get()!="Rs.0.0":
                self.textarea.insert(END,f"\nGrocery Tax  \t\t\t  {self.grocery_tax.get()} ")
                
            if self.cold_drinks_tax.get()!="Rs.0.0":
                self.textarea.insert(END,f"\nCold Drink Tax  \t\t\t  {self.cold_drinks_tax.get()} ")
            
            self.textarea.insert(END,f"\nTotal Bill    \t\t\t  Rs. {(self.total_bill)} ")
            self.textarea.insert(END,f"\n------------------------------------------------------------------------")

            values["C_Name"]  = self.c_name.get()
            values["C_Phone"] = self.c_phone.get()
            values["Bill_no"]    = self.bill_number.get()

           
            self.save_bill() 
            
            
    def save_bill(self):
       op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
       if op>0:
           '''self.bill_data=self.textarea.get('1.0',END)
           f1=open("billsprint/"+str(self.bill_number.get())+".txt","w")
           f1.write(self.bill_data)
           f1.close()'''
           #print("jjjjjjj",values)
           bill = {}
           mq.writ_rcd_to_mongo(values)
           messagebox.showinfo("Saved",f"Bill Number.:{self.bill_number.get()}Saved Successfully")
           values.clear()
           mq.read_rcd_to_mongo()
       else:
           return
      
#    def find_bill(self):
#        present="no"
#        for i in os.listdir("billsprint/"):
#            if i.split('.')[0]==self.search_bill.get():
#                f1=open(f"billsprint/{i}","r")
#                self.textarea.delete('1.0',END)
#                for d in f1:
#                    self.textarea.insert(END,d)
#                fq.close()
#                present="yes"
#        if present=="no":
#            messagebox.showinfo("Error","invalid bill number")
        
       
    def disp(self):
        recall=mq.read_rcd_to_mongo()
        self.textarea.delete('1.0',END)
        for x in recall:
            self.textarea.insert(END,"\t Welcome WebCode Retail \n")
            self.textarea.insert(END,f"\n ID:{recall[x]['iD']}")        
            self.textarea.insert(END,f"\n Bill Number:{recall[x]['Bill_no']}")
            self.textarea.insert(END,f"\n====================================")

    def getValues(self):
        
        global values
        
        values["soap"]		= self.soap.get()		
        values["face_cream"]    = self.face_cream.get()	
        values["face_wash"]	= self.face_wash.get()	
        values["spray"]		= self.spray.get()	
        values["gel"]		= self.gel.get()		
        values["lotion"]	= self.lotion.get()

        values["cosmetic_price"]= self.cosmetic_price.get()
        values["c_tax"  ]	= self.cosmetic_tax.get()

        values["rice"]		 =self.rice.get()
        values["food_oil"]	 =self.food_oil.get()
        values["daal"]		 =self.daal.get()
        values["wheat"]		 =self.wheat.get()
        values["sugar"]		 =self.sugar.get()
        values["tea"]		 =self.tea.get()

        values["grocery_price"]	= self.grocery_price.get()	
        values["g_tax"]		= self.grocery_tax.get()

        values["maza"] 		=self.maza.get()
        values["cock"] 		=self.cock.get()
        values["frooti"] 	=self.frooti.get()
        values["thumbs_up"]     =self.thumbs_up.get()
        values["limca"] 	=self.limca.get()
        values["sprite"]	=self.sprite.get()

        values["tot_cold_drinks_price"] = self.cold_drinks_price.get()
        values["cold_drinks_tax"]   = self.cold_drinks_tax.get()

        return values

    def disp_bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details required")
        elif self.cosmetic_price.get()=="Rs.0.0" and self.grocery_price.get()=="Rs.0.0" and self.cold_drinks_price.get()=="Rs.0.0":
             messagebox.showerror("Error","No Product Selected ")
        else:
            self.disp_bill()
            vals={}
            vals = self.getValues()
            print("Vals",vals)
            if self.soap.get()!=0:
                self.textarea.insert(END,f"\nBath Soap\t\t\t{vals['soap']}")
                
            if self.face_cream.get()!=0:
                self.textarea.insert(END,f"\n Face Cream \t\t\t{vals['face_cream']}")
                
            if self.face_wash.get()!=0:
                self.textarea.insert(END,f"\n Face Wash \t\t\t{vals['face_wash']}")
                
            if self.spray.get()!=0:
                self.textarea.insert(END,f"\n Spray  \t\t\t{vals['spray']}")
                
            if self.gel.get()!=0:
                self.textarea.insert(END,f"\n Hair Gel \t\t\t{vals['gel']}")
                
            if self.lotion.get()!=0:
                self.textarea.insert(END,f"\n Lotion \t\t\t{vals['lotion']}")
                
                
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n Rice  \t\t\t{vals['rice']}")
                
            if self.food_oil.get()!=0:
                self.textarea.insert(END,f"\n Food Oil \t\t\t{vals['food_oil']}")
                
            if self.daal.get()!=0:
                self.textarea.insert(END,f"\n Daal \t\t\t{vals['daal']}")
                
            if self.wheat.get()!=0:
                self.textarea.insert(END,f"\n Wheat  \t\t\t{vals['wheat']}")
                
            if self.sugar.get()!=0:
                self.textarea.insert(END,f"\n Sugar \t\t\t{vals['sugar']}")
                
            if self.tea.get()!=0:
                self.textarea.insert(END,f"\n Tea \t\t\t{vals['tea']}")
            
                
            if self.maza.get()!=0:
                self.textarea.insert(END,f"\n Maza  \t\t\t{vals['maza']}")
                
            if self.cock.get()!=0:
                self.textarea.insert(END,f"\n Cock  \t\t\t{vals['cock']}")
                
            if self.frooti.get()!=0:
                self.textarea.insert(END,f"\n Frooti \t\t\t{vals['frooti']}")
                
            if self.thumbs_up.get()!=0:
                self.textarea.insert(END,f"\n Thumbs Up  \t\t\t{vals['thumbs_up']}")
                
            if self.limca.get()!=0:
                self.textarea.insert(END,f"\n Limca \t\t\t{vals['limca']}")
                
            if self.sprite.get()!=0:
                self.textarea.insert(END,f"\n Sprite \t\t\t{vals['sprite']}")
                
                
            self.textarea.insert(END,f"\n------------------------------------------------------------------------")
            if self.cosmetic_tax.get()!="Rs.0.0":
                self.textarea.insert(END,f"\nCosmetic Tax  \t\t\t  {vals['c_tax']}")
                
            if self.grocery_tax.get()!="Rs.0.0":
                self.textarea.insert(END,f"\nGrocery Tax  \t\t\t {vals['g_tax']} ")
                
            if self.cold_drinks_tax.get()!="Rs.0.0":
                self.textarea.insert(END,f"\nCold Drink Tax  \t\t\t  {vals['cold_drinks_tax']} ")

            tot = int(vals['cosmetic_price']+vals['grocery_price']+vals['grocery_price'])
            self.textarea.insert(END,f"\nTotal Bill    \t\t\t  Rs. {tot} ")
            self.textarea.insert(END,f"\n------------------------------------------------------------------------")

            values["C_Name"]  = self.c_name.get()
            values["C_Phone"] = self.c_phone.get()
           
    def disp_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t Welcome WebCode Retail \n")
        self.textarea.insert(END,f"\n ID:{self.c_id.get()}")        
        self.textarea.insert(END,f"\n Bill Number:{self.bill_number.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n====================================")
        self.textarea.insert(END,f"\nProducts\t\t\t Price")
        self.textarea.insert(END,f"\n====================================")
        

    def disp_one(self):
        print(self.c_id.get())    
        rec= mq.read_one_rcd_mongo(self.c_id.get())
        print("sopap",rec)
        self.soap.set(rec['soap'])
        self.face_cream.set(rec['face_cream'])
        self.face_wash.set(rec['face_wash'])
        self.spray.set(rec['spray'])
        self.gel.set(rec['gel'])
        self.lotion.set(rec['lotion'])

        self.rice.set(rec['rice'])
        self.food_oil.set(rec['food_oil'])
        self.daal.set(rec['daal'])
        self.wheat.set(rec['wheat'])
        self.sugar.set(rec['sugar'])
        self.tea.set(rec['tea'])
    
        self.maza.set(rec['maza'])
        self.cock.set(rec['cock'])
        self.frooti.set(rec['frooti'])
        self.thumbs_up.set(rec['thumbs_up'])
        self.limca.set(rec['limca'])
        self.sprite.set(rec['sprite'])
    
        self.cosmetic_price.set(rec['cosmetic_price'])
        self.grocery_price.set(rec['grocery_price'])
        self.cold_drinks_price.set(rec['tot_cold_drinks_price'])
    
        self.cosmetic_tax.set(rec['c_tax'])
        self.grocery_tax.set(rec['g_tax'])
        self.cold_drinks_tax.set(rec['cold_drinks_tax'])
    
        self.c_name.set(rec['C_Name'])
        self.c_phone.set(rec['C_Phone'])
        self.bill_number.set(rec['Bill_no'])
        self.disp_bill_area()
        return rec

    def update(self):

        #self.total()
        rec = self.getValues()
        mq.upd_tb_rec(self.c_id.get(),rec)
        messagebox.showinfo("Updated !",f" Record:{self.c_id.get()} Updated Successfully")

    def delete(self):
        mq.del_tb_rec(self.c_id.get())
        messagebox.showinfo("Deleted !",f" Record:{self.c_id.get()} Deleted Successfully")
        
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to clear?")
        if op>0:
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gel.set(0)
            self.lotion.set(0)
    
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
    
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbs_up.set(0)
            self.limca.set(0)
            self.sprite.set(0)
    
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")
    
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")
    
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_number.set("")
            self.c_id.set(0)
            x=random.randint(1000,9999)
            self.bill_number.set(str(x))         
            self.search_bill.set("")
            self.welcome_bill()
        
    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()
                   
root=Tk()
obj=Bill_App(root)
root.mainloop()
