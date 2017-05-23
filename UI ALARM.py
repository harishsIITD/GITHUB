# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

from subprocess import check_output
#print(check_output(["ls", "../input"]).decode("utf8"))

# Any results you write to the current directory are saved as output.

from tkinter import *
from tkinter import ttk
import numpy as np
import pandas as pd
import tkinter.filedialog
import tkinter.messagebox
import webbrowser
import os
import win32com.client
from xlsxwriter.utility import xl_rowcol_to_cell

from PIL import ImageTk,Image




TITLE_FONT = ("Helvetica", 18, "bold")
global stroot1,stroot2,check3

global filename,df,check1,check2,button1,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,t1,t2,t3,t4,t5,t6,t7,f,lis,df,checka,t8,i11,i12,i13
global scale1,spinbox1,scale2,spinbox2,scale3,spinbox3,scale4,spinbox4,scale5,spinbox5,scale6,spinbox6,scale7,spinbox7,scale8,spinbox8,scale9,spinbox9,scale10,spinbox10,scale11,spinbox11,scale12,spinbox12,scale14,spinbox14
global par1,par2,par3,par4,par5,par6,par7,par8,par9,par10,par11,par12,par14,spinval1
global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14,explis
global a1,a2,a3,a4,a5,a6,a7,f,lis1,lisv1,df1,checka,t8,check2,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,alis,u
global buttonps1,buttonps2,buttonps3,buttonpa1,buttonpa2,buttonpa3,h1,h2,h3,paras,parac,portstatus,selpara,wtpara

u=1
h1=0
h2=0
h3=0

r1=0
r2=0
r3=0
r4=0
r5=0
r6=0
r7=0
r8=0
r9=0
r10=0
r11=0
r12=0
r14=0

y1=0
y2=0
y3=0
y4=0
y5=0


a1=1
a2=1
a3=1
a4=1
a5=1

lisv1=[]
lis1=[]
alis=[]
DBDlist=[]
ORlis=[]
CDlis=[]
ISQlis=[]
glis=[]
selpara=[]
wtpara=[]


global box2_dict 
box2_dict = {}
y1=0
y2=0
y3=0
y4=0
y5=0
y6=0
y7=0
y8=0

scale1=0
scale2=0
scale3=0
scale4=0
scale5=0
scale6=0
scale7=0
scale8=0
scale9=0
scale10=0
scale11=0
scale12=0
scale14=0
par1=0
par2=0
par3=0
par4=0
par5=0
par6=0
par7=0
par8=0
par9=0
par10=0
par11=0
par12=0
par14=0



p1=0
p2=0
p3=0
p4=0
p5=0
p6=0
p7=0
p8=0
p9=0
p10=0
p11=0
p12=0
p13=0
p14=0

lisv=[]
lis=[]
llis=[]
llis2=[]
llis3=[]
llis4=[]
llis5=[]
llis6=[]
llis7=[]
llis8=[]





def change_icon2(event,i):
    global box2_dict,f,lis1,df1,lisv1
    lis1.append(box2_dict[i].get())
    
    lisv1.append(alis[i])
               
    #print("The user selected value now is:")
    #print("This is selection",lis)
    df1 = pd.DataFrame({'col1':lisv1,'col2':lis1})
    print("Data Frame",df1)

def updateValue(event):
    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
    global scale1,spinbox1,scale2,spinbox2,scale3,spinbox3,scale4,spinbox4,scale5,spinbox5,scale6,spinbox6,scale7,spinbox7,scale8,spinbox8,scale9,spinbox9,scale10,spinbox10,scale11,spinbox11,scale12,spinbox12,scale14,spinbox14
    
    if p1%2==1 or p13%2==1:
        r1=scale1.get()
        
    if p2%2==1 or p13%2==1:
        r2=scale2.get()
    if p3%2==1 or p13%2==1:
        r3=scale3.get()    
    if p4%2==1 or p13%2==1:
        r4=scale4.get()
    if p5%2==1 or p13%2==1:
        r5=scale5.get()
    if p6%2==1 or p13%2==1:
        r6=scale6.get()
    if p7%2==1 or p13%2==1:
        r7=scale7.get()
    if p8%2==1 or p13%2==1:
        r8=scale8.get()
    if p9%2==1 or p13%2==1:
        r9=scale9.get()
    if p10%2==1 or p13%2==1:
        r10=scale10.get()
    if p11%2==1 or p13%2==1:
        r11=scale11.get()
    if p12%2==1 or p13%2==1:
        r12=scale12.get()
    if p14%2==1 or p13%2==1:
        r14=scale14.get()

#def calp():
#    global scale1,spinbox1,scale2,spinbox2,scale3,spinbox3,scale4,spinbox4,scale5,spinbox5,scale6,spinbox6,scale7,spinbox7,scale8,spinbox8,scale9,spinbox9,scale10,spinbox10,scale11,spinbox11,scale12,spinbox12
#    global par1,par2,par3,par4,par5,par6,par7,par8,par9,par10,par11,par12,stroot2
#    v1=0
#    v2=0
#    v3=0
#    v4=0
#    v5=0
#    v6=0
#    v7=0
#    v8=0
#    v9=0
#    v10=0
#    v11=0
#    v12=0
#    if p1%2==1 or p13%2==1:
#        v1=scale1.get()
#    if p2%2==1 or p13%2==1:
#        v2=scale2.get()
#    if p3%2==1 or p13%2==1:
#        v3=scale3.get()
#    if p4%2==1 or p13%2==1:
#        v4=scale4.get()
#    if p5%2==1 or p13%2==1:
#        v5=scale5.get()
#    if p6%2==1 or p13%2==1:
#        v6=scale6.get()
#    if p7%2==1 or p13%2==1:
#        v7=scale7.get()
#    if p8%2==1 or p13%2==1:
#        v8=scale8.get()
#    if p9%2==1 or p13%2==1:
#        v9=scale9.get()
#    if p10%2==1 or p13%2==1:
#        v10=scale10.get()
#    if p11%2==1 or p13%2==1:
#        v11=scale11.get()
#    if p12%2==1 or p13%2==1:
#        v12=scale12.get()
#    
#    
#    
#       
#    if p1%2==1 or p13%2==1:
#        global stroot2
#
#        
#        par1= v1/(v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12)
#        par1=round(par1,1)
#        pec1=round((par1*100))
#        
#        perc1=ttk.Label(stroot2,text=pec1,font="Verdana 18 bold")
#        perc1.grid(row=0,column=7,sticky=W)
#    if p2%2==1 or p13%2==1:
#        
#        par2=v2/(v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12)
#        par2=round(par2,1)
#        pec2=round((par2*100))
#        
#        perc2=ttk.Label(stroot2,text=pec2,font="Verdana 18 bold")
#        perc2.grid(row=1,column=7,sticky=W)
#    if p3%2==1 or p13%2==1:
#        
#        par3=v3/(v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12)
#        par3=round(par3,1)
#        pec3=round((par3*100))
#        
#        perc3=ttk.Label(stroot2,text=pec3,font="Verdana 18 bold")
#        perc3.grid(row=2,column=7,sticky=W)
#    if p4%2==1 or p13%2==1:
#        
#        par4=v4/(v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12)
#        par4=round(par4,1)
#        pec4=round((par4*100))
#        
#        perc4=ttk.Label(stroot2,text=pec4,font="Verdana 18 bold")
#        perc4.grid(row=3,column=7,sticky=W)
#    if p5%2==1 or p13%2==1:
#        
#        par5=v5/(v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12)
#        par5=round(par5,2)
#    if p6%2==1 or p13%2==1:
#       
#        par6=v6/(v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12)
#        par6=round(par6,2)
#    if p7%2==1 or p13%2==1:
#       
#        par7=v7/(v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12)
#        par7=round(par7,2)
#    if p8%2==1 or p13%2==1:
#        
#        par8=v8/(v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12)
#        par8=round(par8,2)
#    if p9%2==1 or p13%2==1:
#        
#        par9=v9/(v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12)
#        par9=round(par9,2)
#    if p10%2==1 or p13%2==1:
#       
#        par10=v10/(v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12)
#        par10=round(par10,2)
#    if p11%2==1 or p13%2==1:
#        
#        par11=v11/(v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12)
#        par11=round(par11,2)
#    if p12%2==1 or p13%2==1:
#       
#        par12=v12/(v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12)
#        par12=round(par12,2)
#        
#    print(par1,par2,par3,par4,par5,par6,par7,par8,par9,par10,par11,par12)
    
    
    
    

    





def inp1():
    global p1
    p1=p1+1
    global stroot2,scale1,spinbox1,spinval1
    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
    
    spinval1 = IntVar()
    def accept_whole_number_only1(e=None):
        global scale1,spinbox1
        value1 = scale1.get()
        if int(value1) != value1:
            scale1.set(round(value1))
            

    def update1(e=None):
        global scale1,spinbox1
    
        scale1.set(spinbox1.get())
    if p1%2==1 and (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))>0:
        global scale1,spinbox1
       
        scale1 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                variable=spinval1,
                                command=accept_whole_number_only1)
        scale1.bind("<ButtonRelease-1>", updateValue)
        scale1.grid(row=0,column=1,sticky=W)
    
    
        spinbox1 = Spinbox(stroot2,from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                textvariable=spinval1,
                                command=update1,
                                width=10)
        spinbox1.bind("<ButtonRelease-1>", updateValue)
        spinbox1.grid(row=0,column=3,sticky=W)
    elif p1%2==0 or (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))<=0:
        
        scale1.grid_forget()
        spinbox1.grid_forget()
        
    
    
    
   
    print(p1)
    
def inp2():
    global p2    
    p2=p2+1
    
    global stroot2,scale2,spinbox2,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
    
    spinval2 = IntVar()
    def accept_whole_number_only2(e=None):
        value2 = scale2.get()
        if int(value2) != value2:
            scale2.set(round(value2))

    def update2(e=None):
    
        scale2.set(spinbox2.get())
    if p2%2==1 and (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))>0:
        

        scale2 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                variable=spinval2,
                                command=accept_whole_number_only2)
        scale2.bind("<ButtonRelease-1>", updateValue)
        scale2.grid(row=1,column=1,sticky=W)
    
    
        spinbox2 = Spinbox(stroot2,from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                textvariable=spinval2,
                                command=update2,
                                width=10)
        spinbox2.bind("<ButtonRelease-1>", updateValue)
        spinbox2.grid(row=1,column=3,sticky=W)
    elif p2%2==0 or (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))<=0:
        
        scale2.grid_forget()
        spinbox2.grid_forget()

def inp3():
    global p3    
    p3=p3+1
    
    global stroot2,scale3,spinbox3
    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
    
    spinval3 = IntVar()
    def accept_whole_number_only3(e=None):
        value3 = scale3.get()
        if int(value3) != value3:
            scale3.set(round(value3))

    def update3(e=None):
    
        scale3.set(spinbox3.get())
    if p3%2==1 and (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))>0:
       

        scale3 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                variable=spinval3,
                                command=accept_whole_number_only3)
        scale3.bind("<ButtonRelease-1>", updateValue)
        scale3.grid(row=2,column=1,sticky=W)
    
    
        spinbox3 = Spinbox(stroot2,from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                textvariable=spinval3,
                                command=update3,
                                width=10)
        spinbox3.bind("<ButtonRelease-1>", updateValue)
        spinbox3.grid(row=2,column=3,sticky=W)
    elif p3%2==0 or (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))<=0:
        
        scale3.grid_forget()
        spinbox3.grid_forget()
    
def inp4():
    global p4    
    p4=p4+1
    print(p4)
    global stroot2,scale4,spinbox4
    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
    
    spinval4 = IntVar()
    def accept_whole_number_only4(e=None):
        value4 = scale4.get()
        if int(value4) != value4:
            scale4.set(round(value4))

    def update4(e=None):
    
        scale4.set(spinbox4.get())
    if p4%2==1 and (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))>0:
        

        scale4 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                variable=spinval4,
                                command=accept_whole_number_only4)
        scale4.bind("<ButtonRelease-1>", updateValue)
        scale4.grid(row=3,column=1,sticky=W)
    
    
        spinbox4 = Spinbox(stroot2,from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                textvariable=spinval4,
                                command=update4,
                                width=10)
        spinbox4.bind("<ButtonRelease-1>", updateValue)
        spinbox4.grid(row=3,column=3,sticky=W)
    elif p4%2==0 or (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))<=0:
        
        scale4.grid_forget()
        spinbox4.grid_forget()
        
def inp5():
    global p5    
    p5=p5+1
    print(p5)
    global stroot2,scale5,spinbox5
    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
    
    spinval5 = IntVar()
    def accept_whole_number_only5(e=None):
        value5 = scale5.get()
        if int(value5) != value5:
            scale5.set(round(value5))

    def update5(e=None):
    
        scale5.set(spinbox5.get())
    if p5%2==1 and (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))>0:
        
        scale5 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                variable=spinval5,
                                command=accept_whole_number_only5)
        scale5.bind("<ButtonRelease-1>", updateValue)
        scale5.grid(row=4,column=1,sticky=W)
    
    
        spinbox5 = Spinbox(stroot2,from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                textvariable=spinval5,
                                command=update5,
                                width=10)
        spinbox5.bind("<ButtonRelease-1>", updateValue)
        spinbox5.grid(row=4,column=3,sticky=W)
    elif p5%2==0 or (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))<=0:
        
        scale5.grid_forget()
        spinbox5.grid_forget()
def inp6():
    global p6    
    p6=p6+1
    print(p6)
    global stroot2,scale6,spinbox6
    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
    
    spinval6 = IntVar()
    def accept_whole_number_only6(e=None):
        value6 = scale6.get()
        if int(value6) != value6:
            scale6.set(round(value6))

    def update6(e=None):
    
        scale6.set(spinbox6.get())
    if p6%2==1 and (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))>0:
       

        scale6 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                variable=spinval6,
                                command=accept_whole_number_only6)
        scale6.bind("<ButtonRelease-1>", updateValue)
        scale6.grid(row=5,column=1,sticky=W)
    
    
        spinbox6 = Spinbox(stroot2,from_=1, to=100,
                                textvariable=spinval6,
                                command=update6,
                                width=10)
        spinbox6.bind("<ButtonRelease-1>", updateValue)
        spinbox6.grid(row=5,column=3,sticky=W)
    elif p6%2==0 or (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))<=0:
        
        scale6.grid_forget()
        spinbox6.grid_forget()
def inp7():
    global p7    
    p7=p7+1
    print(p7)
    global stroot2,scale7,spinbox7
    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
    
    spinval7 = IntVar()
    def accept_whole_number_only7(e=None):
        value7 = scale7.get()
        if int(value7) != value7:
            scale7.set(round(value7))

    def update7(e=None):
    
        scale7.set(spinbox7.get())
    if p7%2==1 and (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))>0:
       

        scale7 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                variable=spinval7,
                                command=accept_whole_number_only7)
        scale7.bind("<ButtonRelease-1>", updateValue)
        scale7.grid(row=6,column=1,sticky=W)
    
    
        spinbox7 = Spinbox(stroot2,from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                textvariable=spinval7,
                                command=update7,
                                width=10)
        spinbox7.bind("<ButtonRelease-1>", updateValue)
        spinbox7.grid(row=6,column=3,sticky=W)
    elif p7%2==0 or (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))<=0:
        
        scale7.grid_forget()
        spinbox7.grid_forget()
def inp8():
    global p8    
    p8=p8+1
    print(p8)
    global stroot2,scale8,spinbox8
    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
    
    spinval8 = IntVar()
    def accept_whole_number_only8(e=None):
        value8 = scale8.get()
        if int(value8) != value8:
            scale8.set(round(value8))

    def update8(e=None):
    
        scale8.set(spinbox8.get())
    if p8%2==1 and (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))>0:
        

        scale8 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                variable=spinval8,
                                command=accept_whole_number_only8)
        scale8.bind("<ButtonRelease-1>", updateValue)
        scale8.grid(row=7,column=1,sticky=W)
    
    
        spinbox8 = Spinbox(stroot2,from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                textvariable=spinval8,
                                command=update8,
                                width=10)
        spinbox8.bind("<ButtonRelease-1>", updateValue)
        spinbox8.grid(row=7,column=3,sticky=W)
    elif p8%2==0 or (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))<=0:
        
        scale8.grid_forget()
        spinbox8.grid_forget()
def inp9():
    global p9    
    p9=p9+1
    print(p9)
    global stroot2,scale9,spinbox9
    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
    
    spinval9 = IntVar()
    def accept_whole_number_only9(e=None):
        value9 = scale9.get()
        if int(value9) != value9:
            scale9.set(round(value9))

    def update9(e=None):
    
        scale9.set(spinbox9.get())
    if p9%2==1 and (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))>0:
       

        scale9 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                variable=spinval9,
                                command=accept_whole_number_only9)
        scale9.bind("<ButtonRelease-1>", updateValue)
        scale9.grid(row=8,column=1,sticky=W)
    
    
        spinbox9 = Spinbox(stroot2,from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                textvariable=spinval9,
                                command=update9,
                                width=10)
        spinbox9.bind("<ButtonRelease-1>", updateValue)
        spinbox9.grid(row=8,column=3,sticky=W)
    elif p9%2==0 or (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))<=0:
        
        scale9.grid_forget()
        spinbox9.grid_forget()
def inp10():
    global p10    
    p10=p10+1
    print(p10)
    global stroot2,scale10,spinbox10
    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
    
    spinval10 = IntVar()
    def accept_whole_number_only10(e=None):
        value10 = scale10.get()
        if int(value10) != value10:
            scale10.set(round(value10))

    def update10(e=None):
    
        scale10.set(spinbox10.get())
    if p10%2==1 and (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))>0:
       

        scale10 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                variable=spinval10,
                                command=accept_whole_number_only10)
        scale10.bind("<ButtonRelease-1>", updateValue)
        scale10.grid(row=9,column=1,sticky=W)
    
    
        spinbox10 = Spinbox(stroot2,from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                textvariable=spinval10,
                                command=update10,
                                width=10)
        spinbox10.bind("<ButtonRelease-1>", updateValue)
        spinbox10.grid(row=9,column=3,sticky=W)
    elif p10%2==0 or (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))<=0:
        
        scale10.grid_forget()
        spinbox10.grid_forget()
def inp11():
    global p11    
    p11=p11+1
    print(p11)
    global stroot2,scale11,spinbox11
    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
    
    spinval11 = IntVar()
    def accept_whole_number_only11(e=None):
        value11 = scale11.get()
        if int(value11) != value11:
            scale11.set(round(value11))

    def update11(e=None):
    
        scale11.set(spinbox11.get())
    if p11%2==1 and (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))>0:
        
        scale11 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                variable=spinval11,
                                command=accept_whole_number_only11)
        scale11.bind("<ButtonRelease-1>", updateValue)
        scale11.grid(row=10,column=1,sticky=W)
    
    
        spinbox11 = Spinbox(stroot2,from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                textvariable=spinval11,
                                command=update11,
                                width=10)
        spinbox11.bind("<ButtonRelease-1>", updateValue)
        spinbox11.grid(row=10,column=3,sticky=W)
    elif p11%2==0 or (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))<=0:
        
        scale11.grid_forget()
        spinbox11.grid_forget()
def inp12():
    global p12    
    p12=p12+1
    print(p12)
    global stroot2,scale12,spinbox12  
    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
    spinval12 = IntVar()    
    def accept_whole_number_only12(e=None):
        value12 = scale12.get()
        if int(value12) != value12:
            scale12.set(round(value12))

    def update12(e=None):
    
        scale12.set(spinbox12.get())
    if p12%2==1 and (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))>0:
        

        scale12 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                variable=spinval12,
                                command=accept_whole_number_only12)
        scale12.bind("<ButtonRelease-1>", updateValue)
        scale12.grid(row=11,column=1,sticky=W)
    
    
        spinbox12 = Spinbox(stroot2,from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                textvariable=spinval12,
                                command=update12,
                                width=10)
        spinbox12.bind("<ButtonRelease-1>", updateValue)
        spinbox12.grid(row=11,column=3,sticky=W)
    elif p12%2==0 or (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))<=0:
        
        scale12.grid_forget()
        spinbox12.grid_forget()

def inp14():
    global p14    
    p14=p14+1
    print(p14)
    global stroot2,scale14,spinbox14  
    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
    spinval14 = IntVar()    
    def accept_whole_number_only14(e=None):
        value14 = scale14.get()
        if int(value14) != value14:
            scale14.set(round(value14))

    def update14(e=None):
    
        scale14.set(spinbox14.get())
    if p14%2==1 and (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))>0:
        

        scale14 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                variable=spinval14,
                                command=accept_whole_number_only14)
        scale14.bind("<ButtonRelease-1>", updateValue)
        scale14.grid(row=12,column=1,sticky=W)
    
    
        spinbox14 = Spinbox(stroot2,from_=1, to=(100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14)),
                                textvariable=spinval14,
                                command=update14,
                                width=10)
        spinbox14.bind("<ButtonRelease-1>", updateValue)
        spinbox14.grid(row=12,column=3,sticky=W)
    elif p14%2==0 or (100-(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r14))<=0:
        
        scale14.grid_forget()
        spinbox14.grid_forget()


def inp13():
    global p13
    p13=p13+1
    global stroot2,scale1,spinbox1,scale2,spinbox2,scale3,spinbox3,scale4,spinbox4,scale5,spinbox5,scale6,spinbox6,scale7,spinbox7,scale8,spinbox8,scale9,spinbox9,scale10,spinbox10,scale11,spinbox11,scale12,spinbox12,scale14,spinbox14
    spinval1 = IntVar()
    spinval2 = IntVar()
    spinval3 = IntVar()
    spinval4 = IntVar()
    spinval5 = IntVar()
    spinval6 = IntVar()
    spinval7 = IntVar()
    spinval8 = IntVar()
    spinval9 = IntVar()
    spinval10 = IntVar()
    spinval11 = IntVar()
    spinval12 = IntVar()
    spinval14 = IntVar()
    def accept_whole_number_only(e=None):
        value1 = scale1.get()
        value2 = scale2.get()
        value3 = scale3.get()
        value4 = scale4.get()
        value5 = scale5.get()
        value6 = scale6.get()
        value7 = scale7.get()
        value8 = scale8.get()
        value9 = scale9.get()
        value10 = scale10.get()
        value11 = scale11.get()
        value12 = scale12.get()
        value14 = scale14.get()
        if int(value1) != value1:
            scale1.set(round(value1))
        if int(value2) != value2:
            scale2.set(round(value2))
        if int(value3) != value3:
            scale3.set(round(value3))
        if int(value4) != value4:
            scale4.set(round(value4))
        if int(value5) != value5:
            scale5.set(round(value5))
        if int(value6) != value6:
            scale6.set(round(value6))
        if int(value7) != value7:
            scale7.set(round(value7))
        if int(value8) != value8:
            scale8.set(round(value8))
        if int(value9) != value9:
            scale9.set(round(value9))
        if int(value10) != value10:
            scale10.set(round(value10))
        if int(value11) != value11:
            scale11.set(round(value11))
        if int(value12) != value12:
            scale12.set(round(value12))
        if int(value14) != value14:
            scale14.set(round(value14))
    def update(e=None):
        scale1.set(spinbox1.get())
        scale2.set(spinbox2.get())
        scale3.set(spinbox3.get())
        scale4.set(spinbox4.get())
        scale5.set(spinbox5.get())
        scale6.set(spinbox6.get())
        scale7.set(spinbox7.get())
        scale8.set(spinbox8.get())
        scale9.set(spinbox9.get())
        scale10.set(spinbox10.get())
        scale11.set(spinbox11.get())
        scale12.set(spinbox12.get())
        scale14.set(spinbox14.get())        
        
    if p13%2==1:
        
        scale1 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=100,
                                variable=spinval1,
                                command=accept_whole_number_only)
        scale1.grid(row=0,column=1,sticky=W)
    
    
        spinbox1 = Spinbox(stroot2,from_=1, to=100,
                                textvariable=spinval1,
                                command=update,
                                width=10)
        spinbox1.grid(row=0,column=3,sticky=W)
        

        scale2 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=100,
                                variable=spinval2,
                                command=accept_whole_number_only)
        scale2.grid(row=1,column=1,sticky=W)
    
    
        spinbox2 = Spinbox(stroot2,from_=1, to=100,
                                textvariable=spinval2,
                                command=update,
                                width=10)
        spinbox2.grid(row=1,column=3,sticky=W)
        
        scale3 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=100,
                                variable=spinval3,
                                command=accept_whole_number_only)
        scale3.grid(row=2,column=1,sticky=W)
    
    
        spinbox3 = Spinbox(stroot2,from_=1, to=100,
                                textvariable=spinval3,
                                command=update,
                                width=10)
        spinbox3.grid(row=2,column=3,sticky=W)

        scale4 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=100,
                                variable=spinval4,
                                command=accept_whole_number_only)
        scale4.grid(row=3,column=1,sticky=W)
    
    
        spinbox4 = Spinbox(stroot2,from_=1, to=100,
                                textvariable=spinval4,
                                command=update,
                                width=10)
        spinbox4.grid(row=3,column=3,sticky=W)
        
        scale5 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=100,
                                variable=spinval5,
                                command=accept_whole_number_only)
        scale5.grid(row=4,column=1,sticky=W)
    
    
        spinbox5 = Spinbox(stroot2,from_=1, to=100,
                                textvariable=spinval5,
                                command=update,
                                width=10)
        spinbox5.grid(row=4,column=3,sticky=W)  
        
         
        scale6 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=100,
                                variable=spinval6,
                                command=accept_whole_number_only)
        scale6.grid(row=5,column=1,sticky=W)
    
    
        spinbox6 = Spinbox(stroot2,from_=1, to=100,
                                textvariable=spinval6,
                                command=update,
                                width=10)
        spinbox6.grid(row=5,column=3,sticky=W)  
        
         
        scale7 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=100,
                                variable=spinval7,
                                command=accept_whole_number_only)
        scale7.grid(row=6,column=1,sticky=W)
    
    
        spinbox7 = Spinbox(stroot2,from_=1, to=100,
                                textvariable=spinval7,
                                command=update,
                                width=10)
        spinbox7.grid(row=6,column=3,sticky=W)  
        
        scale8 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=100,
                                variable=spinval8,
                                command=accept_whole_number_only)
        scale8.grid(row=7,column=1,sticky=W)
    
    
        spinbox8 = Spinbox(stroot2,from_=1, to=100,
                                textvariable=spinval8,
                                command=update,
                                width=10)
        spinbox8.grid(row=7,column=3,sticky=W)  
        scale9 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=100,
                                variable=spinval9,
                                command=accept_whole_number_only)
        scale9.grid(row=8,column=1,sticky=W)
    
    
        spinbox9 = Spinbox(stroot2,from_=1, to=100,
                                textvariable=spinval9,
                                command=update,
                                width=10)
        spinbox9.grid(row=8,column=3,sticky=W)  
       
        scale10 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=100,
                                variable=spinval10,
                                command=accept_whole_number_only)
        scale10.grid(row=9,column=1,sticky=W)
    
    
        spinbox10 = Spinbox(stroot2,from_=1, to=100,
                                textvariable=spinval10,
                                command=update,
                                width=10)
        spinbox10.grid(row=9,column=3,sticky=W) 
        
        scale11 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=100,
                                variable=spinval11,
                                command=accept_whole_number_only)
        scale11.grid(row=10,column=1,sticky=W)
    
    
        spinbox11 = Spinbox(stroot2,from_=1, to=100,
                                textvariable=spinval11,
                                command=update,
                                width=10)
        spinbox11.grid(row=10,column=3,sticky=W)  
        
        scale12 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=100,
                                variable=spinval12,
                                command=accept_whole_number_only)
        scale12.grid(row=11,column=1,sticky=W)
    
    
        spinbox12 = Spinbox(stroot2,from_=1, to=100,
                                textvariable=spinval12,
                                command=update,
                                width=10)
        spinbox12.grid(row=11,column=3,sticky=W)  
        
        scale14 = ttk.Scale(stroot2,orient=HORIZONTAL,
                                length=200,
                                from_=1, to=100,
                                variable=spinval14,
                                command=accept_whole_number_only)
        scale14.grid(row=11,column=1,sticky=W)
    
    
        spinbox14 = Spinbox(stroot2,from_=1, to=100,
                                textvariable=spinval14,
                                command=update,
                                width=10)
        spinbox14.grid(row=11,column=3,sticky=W)          
            
        
        
        
        
        
        
        
        
        
    elif p13%2==0: 
        scale1.grid_forget()
        spinbox1.grid_forget()
        scale2.grid_forget()
        spinbox2.grid_forget()
        scale3.grid_forget()
        spinbox3.grid_forget()
        scale4.grid_forget()
        spinbox4.grid_forget()
        scale5.grid_forget()
        spinbox5.grid_forget()
        scale6.grid_forget()
        spinbox6.grid_forget()
        scale7.grid_forget()
        spinbox7.grid_forget()
        scale2.grid_forget()
        spinbox8.grid_forget()
        scale8.grid_forget()
        spinbox9.grid_forget()
        scale9.grid_forget()
        spinbox10.grid_forget()
        scale10.grid_forget()
        spinbox11.grid_forget()
        scale11.grid_forget()
        spinbox12.grid_forget()
        scale12.grid_forget()
        spinbox14.grid_forget()
        scale14.grid_forget()
        
def upload():
   global filename,button1,i11,i12,i13
     
   
   filename=filedialog.askopenfilename()
   print(filename)
   
   if not filename:
       messagebox.showinfo("Window Title","File not Selected!! Please select the file")
         
   else:
       messagebox.showinfo("Window Title","Data Uploaded Successfully")
       




#def populate(roots):
#    '''Put in some fake data'''
#    for row in range(100):
#        Label(roots, text="%s" % row, width=3, borderwidth="1", 
#                 relief="solid").grid(row=row, column=0)
#        t="this is the second column for row %s" %row
#        Label(roots, text=t).grid(row=row, column=1)


       
   
 




def dypar():
    
            root=Tk()
            root.title("Parameter Selection")
            #root.geometry("760x760")
            w, h = root.winfo_screenwidth(), root.winfo_screenheight()
            root.geometry("%dx%d+0+0" % (w, h))
            
           # canvas = Canvas(root, borderwidth=0,width=850, height=400)
           
            roots = Frame(root)            
            
          
            

            

            
            
            
            
            
            
           

                      
            notebook = ttk.Notebook(roots)
            notebooka = ttk.Notebook(roots)

    
            global p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,Entry_1,dropDownBox21,Entry_2,dropDownBox22,Entry_3,dropDownBox23,i11,i12,i13
            global dropDownBox22,dropDownBox23,dropDownBox31,dropDownBox32,dropDownBox33,dropDownBox41,dropDownBox42
            global dropDownBox51,dropDownBox52,dropDownBox53,dropDownBox54,dropDownBox55,dropDownBox56,dropDownBox57,dropDownBox58,dropDownBox59
            global dropDownBox61,dropDownBox62,dropDownBox63,dropDownBox64,dropDownBox65,dropDownBox66,dropDownBox67,dropDownBox68,dropDownBox69
            global dropDownBox91,dropDownBox92,dropDownBox93,dropDownBox94,dropDownBox95,dropDownBox96,dropDownBox97,dropDownBox98,dropDownBox99,dropDownBox910,dropDownBox911,dropDownBox912,dropDownBox913,dropDownBox914,dropDownBox915,dropDownBox916,dropDownBox917,dropDownBox918,dropDownBox919,dropDownBox920,dropDownBox921,dropDownBox922,dropDownBox923,dropDownBox924
            global dropDownBox101,dropDownBox102,dropDownBox103,dropDownBox104,dropDownBox105,dropDownBox106,dropDownBox107,dropDownBox108,dropDownBox109,dropDownBox1010,dropDownBox1011,dropDownBox1012,dropDownBox1013,dropDownBox1014
            global a1,a2,a3,a4,a5,a6,a7,f,lis1,lisv1,df1,checka,t8,check2,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,alis,u
            global portstatus
            global selpara,wtpara
            global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14,y1,y2,y3,y4,y5
            
            selpara=[]
            wtpara=[]
            
            
            label = Label(roots, text="Assumptions", font="Verdana 24 bold",bg="black",fg="white")
            label.grid(row=0,column=0,columnspan=50)
            if p1%2==1 or p13%2==1:  
                global i11,i12,i13
                
            
            listItems=['Highly Liquid','Moderately Liquid','Less Liquid','Illiquid']
            
            def resize(event):
   
                pixelX=root.winfo_width()
                pixelY=root.winfo_height()/3
                notebook["width"]=int(round(pixelX))
                notebook["height"]=int(round(pixelY))
                notebooka["width"]=int(round(pixelX)) 
                notebooka["height"]=int(round(pixelY))
            
            
#      
            def para():
                       
                global filename,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p14,p12,i11,i12,i13,Entry_1,dropDownBox21,check3
                global Entry_2,dropDownBox22,Entry_3,dropDownBox23,dropDownBox31,dropDownBox32,dropDownBox33,dropDownBox41,dropDownBox42
                global dropDownBox51,dropDownBox52,dropDownBox53,dropDownBox54,dropDownBox55,dropDownBox56,dropDownBox57,dropDownBox58,dropDownBox59
                global dropDownBox61,dropDownBox62,dropDownBox63,dropDownBox64,dropDownBox65,dropDownBox66,dropDownBox67,dropDownBox68,dropDownBox69
                global dropDownBox91,dropDownBox92,dropDownBox93,dropDownBox94,dropDownBox95,dropDownBox96,dropDownBox97,dropDownBox98,dropDownBox99,dropDownBox910,dropDownBox911,dropDownBox912,dropDownBox913,dropDownBox914,dropDownBox915,dropDownBox916,dropDownBox917,dropDownBox918,dropDownBox919,dropDownBox920,dropDownBox921,dropDownBox922,dropDownBox923,dropDownBox924
                global dropDownBox101,dropDownBox102,dropDownBox103,dropDownBox104,dropDownBox105,dropDownBox106,dropDownBox107,dropDownBox108,dropDownBox109,dropDownBox1010,dropDownBox1011,dropDownBox1012,dropDownBox1013,dropDownBox1014,df1
                global selpara,wtpara
                global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
                result=[]                
                result=check3.copy()
                #print("Result",check3)
                
                
                if p1%2==1 or p13%2==1: 
                    global i11,i12,i13
                    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
                    
                    val11=int(i11.get())
                    val12=int(i12.get()) 
                    val13=int(i13.get())
                    br = []
                    br1=[]
                    for row in result['No._of_broker_dealers']:                   
                        if row >= val11:
                            br.append('Highly Liquid')
                            br1.append(4)
                            
                        elif row <val11 and row >=val12:
                            br.append('Moderately Liquid')
                            br1.append(3)
                        elif row <val12 and row >=val13:
                            br.append('Less Liquid')
                            br1.append(2)
                        elif row <val13:
                            br.append('Illiquid')
                            br1.append(1)
                            
                        
                    result['Brokers Rating'] = br
                    selpara.append("No._of_broker_dealers")
                    wtpara.append(r1)
                     
                        
                        
                        
                if p7%2==1 or p13%2==1:
                    global i71,i72,i73
                    #global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
                    val71=round(float(i71.get()))
                    val72=round(float(i72.get())) 
                    val73=round(float(i73.get()))
                    cr = []
                    cr1 = []
                    ds1=result.ix[:,['Portfolio','Ticker','Security age & time to maturity1']]
                    ds1=ds1.dropna()
                    
                    for row in ds1['Security age & time to maturity1']:
                        
                        if row=="NM":
                            cr.append(' ')
                            
                                     
                        elif row <= val71:
                            cr.append('Highly Liquid')
                            cr1.append(4)
                        elif row >val71 and row <=val72:
                            cr.append('Moderately Liquid')
                            cr1.append(3)
                        elif row >val72 and row <=val73:
                            cr.append('Less Liquid')
                            cr1.append(2)
                        elif row >val73:
                            cr.append('Illiquid')
                            cr1.append(1)
                    
                    ds1 = ds1.drop('Security age & time to maturity1', 1)                   
                        
                    ds1['Security age & time to maturity Rating'] = cr 
                    print(cr)
                    result=pd.merge(result,ds1, on=['Portfolio','Ticker'],how="left")
                    selpara.append("Security age & time to maturity")
                    wtpara.append(r7)
                    
                if p8%2==1 or p13%2==1:
                    global i81,i82,i83
#                    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
                    val81=float(i81.get())
                    val82=float(i82.get()) 
                    val83=float(i83.get())
                    
                    dr = []
                    for row in result['Bid-Ask Spread rates (%)']:
                 
                        if row=="NM":
                            dr.append(' ')                       
                        
                        elif row <= val81:
                           dr.append('Highly Liquid')    
                        elif row >val81 and row <=val82:
                           dr.append('Moderately Liquid')
                        elif row >val82 and row <=val83:
                            dr.append('Less Liquid')
                        elif row >val83:
                            dr.append('Illiquid')
                        
                    result['Difference between Bid/Ask rating'] = dr
                    selpara.append("Bid-Ask Spread rates (%)")
                    wtpara.append(r8)
                    
                    
                
                if p2%2==1 or p13%2==1:
#                    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
#                    value21=dropDownBox21.get()
#                    value22=dropDownBox22.get()
#                    value23=dropDownBox23.get()
                    df2=df1
                    df2.columns=["Diversity_of_broker_dealers","Diversity of broker dealers Rating"]
                    
                    #df2 = pd.DataFrame({'Diversity of broker dealers': ['Discount Broker','Prime Broker','Online Broker'], 'Diversity of broker dealers Rating': [ value21, value22, value23]})
                    result=pd.merge(result,df2, on='Diversity_of_broker_dealers',how="left")
                    selpara.append("Diversity_of_broker_dealers")
                    wtpara.append(r2)
                if p3%2==1 or p13%2==1:
                    global dropDownBox31
#                    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
                    value31=dropDownBox31.get()
                    value32=dropDownBox32.get()
                    value33=dropDownBox33.get()
                    df3 = pd.DataFrame({'Exchange_structure': ['Standard Exchange','Electronic Platforms','OTC'], 'Exchange structure Rating': [ value31, value32, value33]})
                    result=pd.merge(result,df3, on='Exchange_structure',how="left")
                    selpara.append("Exchange_structure")
                    wtpara.append(r3)
                if p4%2==1 or p13%2==1:
#                    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
                    value41=dropDownBox41.get()
                    value42=dropDownBox42.get()
                    df4 = pd.DataFrame({'Central clearing requirements and capabilities': ['Y','N'], 'Central clearing requirements and capabilities Rating': [ value41, value42]})
                    result=pd.merge(result,df4, on='Central clearing requirements and capabilities',how="left")
                    selpara.append("Central clearing requirements and capabilities")
                    wtpara.append(r4)
                    
                if p5%2==1 or p13%2==1:
#                    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
#                    value51=dropDownBox51.get()
#                    value52=dropDownBox52.get()
#                    value53=dropDownBox53.get()
#                    value54=dropDownBox54.get()
#                    value55=dropDownBox55.get()
#                    value56=dropDownBox56.get()
#                    value57=dropDownBox57.get()
#                    value58=dropDownBox58.get()
#                    value59=dropDownBox59.get() 
                    df5=df1
                    df5.columns=["Overall riskiness","Overall riskiness Rating"]
                    #df5 = pd.DataFrame({'Overall riskiness': ['HY1','IG3','IG4','IG5','IG6','IG7','IG8','IG9','IG10'], 'Overall riskiness Rating': [ value51, value52, value53, value54, value55, value56, value57, value58, value59]})
                    result=pd.merge(result,df5, on='Overall riskiness',how="left")
                    selpara.append("Overall riskiness")
                    wtpara.append(r5)
                    
                if p6%2==1 or p13%2==1:
#                    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
#                    value61=dropDownBox61.get()
#                    value62=dropDownBox62.get()
#                    value63=dropDownBox63.get()
#                    value64=dropDownBox64.get()
#                    value65=dropDownBox65.get()
#                    value66=dropDownBox66.get()
#                    value67=dropDownBox67.get()
#                    value68=dropDownBox68.get()
#                    value69=dropDownBox69.get()
                    df6=df1
                    df6.columns=["Currency_denomination","Currency denomination Rating"]
                   # df6 = pd.DataFrame({'Currency denomination': ['CAD','CHF','DKK','EUR','GBp','HKD','JPY','SGD','USD'], 'Currency denomination Rating': [ value61, value62, value63, value64, value65, value66, value67, value68, value69]})
                    result=pd.merge(result,df6, on='Currency_denomination',how="left")
                    selpara.append("Currency_denomination")
                    wtpara.append(r6)
                    
                if p11%2==1 or p13%2==1:
#                    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
                    global i111,i112,i113
                    val111=float(i111.get())
                    val112=float(i112.get()) 
                    val113=float(i113.get())
                    er = []
                    for row in result['30 day Volatility index number']:
                   
                        if row >= val111:
                            er.append('Highly Liquid')    
                        elif row <val111 and row >=val112:
                            er.append('Moderately Liquid')
                        elif row <val112 and row >=val113:
                            er.append('Less Liquid')
                        elif row <val113:
                            er.append('Illiquid')
                        
                    result['30 day Volatility index number Rating'] = er
                    selpara.append("30 day Volatility index number Rating")
                    wtpara.append(r11)
                if p12%2==1 or p13%2==1: 
#                    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
                    global i121,i122,i123
                    val121=float(i121.get())
                    val122=float(i122.get()) 
                    val123=float(i123.get())
                    fr = []
                    for row in result['Position sizes (% Net)']:
                   
                        if row <= val121:
                            fr.append('Highly Liquid')    
                        elif row >val121 and row <=val122:
                            fr.append('Moderately Liquid')
                        elif row >val122 and row <=val123:
                            fr.append('Less Liquid')
                        elif row >val123:
                            fr.append('Illiquid')
                        
                    result['Position sizes (% Net) Rating'] = fr
                    selpara.append("Position sizes (% Net)")
                    wtpara.append(r12)
                
                
                if p14%2==1 or p13%2==1: 
#                    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
                    global i141,i142,i143
                    val141=float(i141.get())
                    val142=float(i142.get()) 
                    val143=float(i143.get())
                    gr = []
                    for row in result['Position as a % of Avg. Daily Volume']:
                   
                        if row <= val141:
                            gr.append('Highly Liquid')    
                        elif row >val141 and row <=val142:
                            gr.append('Moderately Liquid')
                        elif row >val142 and row <=val143:
                            gr.append('Less Liquid')
                        elif row >val143:
                            gr.append('Illiquid')
                        
                    result['Position as a % of Avg. Daily Volume Rating'] = gr
                    selpara.append("Position as a % of Avg. Daily Volume")
                    wtpara.append(r14)
                
                
                
                
                
                
                
                
                
                
                
                
                
                if p9%2==1 or p13%2==1: 
#                    global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
                
#                    value91=dropDownBox91.get()
#                    value92=dropDownBox92.get()
#                    value93=dropDownBox93.get()
#                    value94=dropDownBox94.get()
#                    value95=dropDownBox95.get()
#                    value96=dropDownBox96.get()
#                    value97=dropDownBox97.get()
#                    value98=dropDownBox98.get()
#                    value99=dropDownBox99.get()
#                    value910=dropDownBox910.get()
#                    value911=dropDownBox911.get()
#                    value912=dropDownBox912.get()
#                    value913=dropDownBox913.get()
#                    value914=dropDownBox914.get()
#                    value915=dropDownBox915.get()
#                    value916=dropDownBox916.get()
#                    value917=dropDownBox917.get()
#                    value918=dropDownBox918.get()
#                    value919=dropDownBox919.get()
#                    value920=dropDownBox920.get()
#                    value921=dropDownBox921.get()
#                    value922=dropDownBox922.get()
#                    value923=dropDownBox923.get()
#                    value924=dropDownBox924.get()
                    df9=df1
                    df9.columns=["Issue/issuer credit quality","Issue/issuer credit quality Rating"]
                    #df9 = pd.DataFrame({'Issue/issuer credit quality': ['AAA','AA+','AA','AA-','A+','A','A-','BBB+','BBB','BBB-','BB+','BB','BB-','B+','B','B-','CCC','CC','C','D','pr','Unsolicited','SD','NR'],'Issue/issuer credit quality Rating': [ value91, value92, value93, value94, value95, value96, value97, value98, value99,value910,value911,value912, value913, value914,value915, value916, value917, value918, value919,value920,value921,value922, value923, value924]})
                    result=pd.merge(result,df9, on='Issue/issuer credit quality',how="left")
                    selpara.append("Issue/issuer credit quality")
                    wtpara.append(r9)
                if p10%2==1 or p13%2==1:
#                    value101=dropDownBox91.get()
#                    value102=dropDownBox92.get()
#                    value103=dropDownBox93.get()
#                    value104=dropDownBox94.get()
#                    value105=dropDownBox95.get()
#                    value106=dropDownBox96.get()
#                    value107=dropDownBox97.get()
#                    value108=dropDownBox98.get()
#                    value109=dropDownBox99.get() 
#                    value1010=dropDownBox910.get()
#                    value1011=dropDownBox911.get()
#                    value1012=dropDownBox912.get()
#                    value1013=dropDownBox913.get()
#                    value1014=dropDownBox914.get()
                    df10=df1
                    df10.columns=["Geography_Country","Geography Rating"]
                    #df10 = pd.DataFrame({'Geography / Country': ['CA','CH','DE','FR','GB','GE','HK','IR','IT','JN','LX','NE','SZ','US'],'Geography Rating': [ value101, value102, value103, value104, value105, value106, value107, value108, value109,value1010,value1011,value1012, value1013, value1014]})
                    result=pd.merge(result,df10, on='Geography_Country',how="left")
                    selpara.append("Geography_Country")
                    wtpara.append(r10)
              
                
                
                result1=result.ix[:,["Sector","Security Type","Security","Ticker","Brokers Rating","Security age & time to maturity Rating","Difference between Bid/Ask rating","Diversity of broker dealers Rating","Exchange structure Rating","Central clearing requirements and capabilities Rating","Overall riskiness Rating","Currency denomination Rating","30 day Volatility index number Rating","Position sizes (% Net) Rating","Issue/issuer credit quality Rating","Geography Rating","Position as a % of Avg. Daily Volume Rating"]]
                
               
                result1=result1.as_matrix()
                
                [r,c]=result1.shape
                for j in range(0,c):
                    for i in range(0,r):
                        if result1[i,j]=="Highly Liquid":
                            result1[i,j]=4
                        elif result1[i,j]=="Moderately Liquid":
                            result1[i,j]=3
                        elif result1[i,j]=="Less Liquid":
                            result1[i,j]=2
                        elif result1[i,j]=="Illiquid":
                            result1[i,j]=1
                        else:
                            result1[i,j]=0
                
                            
                result1=pd.DataFrame(result1)
                result1.columns=["Sector","Security Type","Security","Ticker","Brokers Rating","Security age & time to maturity Rating","Difference between Bid/Ask rating","Diversity of broker dealers Rating","Exchange structure Rating","Central clearing requirements and capabilities Rating","Overall riskiness Rating","Currency denomination Rating","30 day Volatility index number Rating","Position sizes (% Net) Rating","Issue/issuer credit quality Rating","Geography Rating","Position as a % of Avg. Daily Volume Rating"]
                
                q=[]
#                global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
                result1["Asset-wise Score"]=((r1*result1["Brokers Rating"]/100)+(r7*result1["Security age & time to maturity Rating"]/100)+(r8*result1["Difference between Bid/Ask rating"]/100)+(r2*result1["Diversity of broker dealers Rating"]/100)+(r3*result1["Exchange structure Rating"]/100)+(r4*result1["Central clearing requirements and capabilities Rating"]/100)+(r5*result1["Overall riskiness Rating"]/100)+(r6*result1["Currency denomination Rating"]/100)+(r11*result1["30 day Volatility index number Rating"]/100)+(r12*result1["Position sizes (% Net) Rating"]/100)+(r9*result1["Issue/issuer credit quality Rating"]/100)+(r14*result1["Position as a % of Avg. Daily Volume Rating"]/100)+(r10*result1["Geography Rating"]/100))
         
               # print("asset",result1["Asset-wise Score"])
              #  Portfolio_rating=result1[["Asset-wise Score"]].mean()
                
                sc=[]
                for row in result1["Asset-wise Score"]: 
                   
                    if row >= 3:
                        sc.append('Highly Liquid')                        
                        
                    elif row <3 and row >=2:
                        sc.append('Moderately Liquid')
                       
                    elif row <2 and row >=1:
                        sc.append('Less Liquid')
                        
                    elif row <1:
                        sc.append('Illiquid')
                       
                            
                        
                result['Asset_wise_Rating'] = sc
                result['Assets']=1
                global u
                
                
                global buttonps1,buttonps2,buttonps3,buttonpa1,buttonpa2,buttonpa3,h1,h2,h3,stroot
                tick=PhotoImage(file="D:/python/ALARM IMAGES/tick.gif")
                
                if h1==1:
                    
                                
                    buttonps1 = ttk.Button(stroot,image=tick)
                    buttonps1.image=tick
                    buttonps1.grid(row=3,column=5,columnspan=1,sticky=E+W,padx=50)
                    
                    
                    buttonpa1 = ttk.Button(stroot,image=tick)
                    buttonpa1.image=tick
                    buttonpa1.grid(row=3,column=9,columnspan=1,sticky=E+W,padx=50)
                if h2==1:
                    
                    buttonps2 = ttk.Button(stroot,image=tick)
                    buttonps2.image=tick
                    buttonps2.grid(row=5,column=5,columnspan=2,sticky=E+W,padx=50)
                    
                    
                    buttonpa2 = ttk.Button(stroot, image=tick)
                    buttonpa2.image=tick
                    buttonpa2.grid(row=5,column=9,columnspan=2,sticky=E+W,padx=50)
                if h3==1:
                    
                    buttonps3 = ttk.Button(stroot,image=tick)
                    buttonps3.image=tick
                    buttonps3.grid(row=7,column=5,columnspan=2,sticky=E+W,padx=50)
                    
                    
                    buttonpa3 = ttk.Button(stroot, image=tick)
                    buttonpa3.image=tick
                    buttonpa3.grid(row=7,column=9,columnspan=2,sticky=E+W,padx=50)
                global portstatus
                
                
                    
                
                if u==1:
#                    global portstatus,selpara,wtpara
                
                
                    result1.to_csv("D:/python/resultansSc1.csv")
                    result.to_csv("D:/Alarm/resultSc1.csv")
                    result.to_excel("D:/Alarm/resultSc1.xlsx")
                   # result.to_html("D:/python/resultSc1.html")
                    webbrowser.open('http://localhost:8000/Alarm/Alarm Mod1.html')
                    psl1 = pd.DataFrame({'Parameter Selected':selpara,'Weightage %':wtpara})
                    psl1.to_csv("D:/Alarm/psl1.csv")
                    del selpara,wtpara
                    u=u+1
                    status1=pd.read_excel("D:/Alarm/resultSc1.xlsx")
                    portstatus=status1.ix[:,["Portfolio","Ticker","Weightage","Assets","Asset_wise_Rating"]]
                    portstatus.rename(columns={'Asset_wise_Rating': 'Scenario1_Rating'}, inplace=True)
                    portstatus.to_csv('D:/Alarm/portstatus.csv')
                    
                    root.destroy()
                    
                    
                    
                    
                elif u==2:
#                    global portstatus
                    
                    result1.to_csv('resultansSc2.csv')
                    result.to_csv('D:/Alarm/resultSc2.csv')
                    result.to_excel("D:/Alarm/resultSc2.xlsx")
              #      result.to_html("resultSc2.html")
                    webbrowser.open('http://localhost:8000/Alarm/Alarm Mod2.html')
                    psl2 = pd.DataFrame({'Parameter Selected':selpara,'Weightage %':wtpara})
                    psl2.to_csv("D:/Alarm/psl2.csv")
                    del selpara,wtpara
                    
                    u=u+1
                    status2=pd.read_excel("D:/Alarm/resultSc2.xlsx")
                    
                    portstatus["Scenario2_Rating"]=status2.ix[:,["Asset_wise_Rating"]]
                    portstatus.to_csv('D:/Alarm/portstatus.csv')
                    
                    root.destroy()
                    
                elif u==3:
#                    global portstatus
                    
                    result1.to_csv('resultansSc3.csv')
                    result.to_csv('D:/Alarm/resultSc3.csv')
                    result.to_excel("D:/Alarm/resultSc3.xlsx")
                 #   result.to_html("resultSc3.html")
                    webbrowser.open('http://localhost:8000/Alarm/Alarm Mod3.html')
                    psl3 = pd.DataFrame({'Parameter Selected':selpara,'Weightage %':wtpara})
                    psl3.to_csv("D:/Alarm/psl3.csv")
                    status3=pd.read_excel("D:/Alarm/resultSc3.xlsx")
                    portstatus["Scenario3_Rating"]=status3.ix[:,["Asset_wise_Rating"]]
                    portstatus.to_csv('D:/Alarm/portstatus.csv')
                    webbrowser.open('http://localhost:8000/Alarm/Alarm Scenario DB.html')
                   
                    
                    
                    u=u+1
                    del u
                    root.destroy()
            
                
            
                
                
                
                
                
                
               
                
            
                    
                                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
               
                
                
            
            
            
             
            
            if p1%2==1 or p13%2==1:
                
                root1=ttk.Frame(notebook)
                
                notebook.add(root1, text="No of Brokers")
                

                
                
               
               # root1.grid(row=1,column=0,sticky="NW")
                global i11,i12,i13
               
                i11=StringVar(root1)
                i12=StringVar(root1)
                i13=StringVar(root1)
               
                
                label_En11=ttk.Label(root1, text="Highly Liquid",style="BW.TLabel")
                label_En12=ttk.Label(root1, text="Medium Liquid",style="BW.TLabel")
                label_En13=ttk.Label(root1, text="Low Liquid",style="BW.TLabel")
                Entry_1=ttk.Entry(root1,textvariable=i11).grid(row=2, column=1)
                Entry_2=ttk.Entry(root1,textvariable=i12).grid(row=3, column=1)
                Entry_3=ttk.Entry(root1,textvariable=i13).grid(row=4, column=1)
                button1=ttk.Button(roots,text="Submit",command=para)
                button1.grid(row=4, column=0,sticky="E")   
                
                label_Met1=ttk.Label(root1,text="No of Brokers")
                label_rat1=ttk.Label(root1,text="Liquidity Rating")
                label_Met1.grid(row=1, column=1,columnspan=2)
                label_rat1.grid(row=1)
                label_En11.grid(row=2)
                label_En12.grid(row=3)
                label_En13.grid(row=4)
           
                
            #Second Shell
            
            
             
           
            if p2%2==1 or p13%2==1:
                root2=ttk.Frame(notebook)
                notebook.add(root2, text="Type of broker dealers") 
                
                label_Met2=ttk.Label(root2,text="Liquidity Rating")
                label_rat2=ttk.Label(root2,text="Type of broker dealers")
                label_Met2.grid(row=0, column=1)
                label_rat2.grid(row=0) 
                  
                
                DBDlist=check3["Diversity_of_broker_dealers"].unique()
                y1=len(DBDlist)
                alis=list(DBDlist)
                #print(alis)
                
                #print(y1)
                for i in range(0,y1):
                    label1=ttk.Label(root2,text=alis[i])
                    label1.grid(row=a1)
                    
                    box1 = ttk.Combobox(root2,values=listItems)
                    box1["values"] = listItems
                    box1.grid(row=a1, column=1, pady=1, padx=1, sticky=E+W+N+S)
                    box2_dict[i] =box1
                    box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon2(event,i))
                #    print(box1["values"][i])
                
                    a1=a1+1
                
            #third Shell
            
            
            if p3%2==1 or p13%2==1:
                root3=ttk.Frame(notebook)
           
                
                notebook.add(root3, text="Types of Exchange Structure") 
        #        root3.grid(row=1,column=1,sticky="E")
                label_En31=ttk.Label(root3, text="Standard Exchange")
                label_En32=ttk.Label(root3, text="Electronic Platforms")
                label_En33=ttk.Label(root3, text="OTC")
                label_En31.grid(row=2)
                label_En32.grid(row=3)
                label_En33.grid(row=4)
                
                label_Met3=ttk.Label(root3,text="Liquidity Rating")
                label_rat3=ttk.Label(root3,text="Types of Exchange Structure")
                label_Met3.grid(row=1, column=1,columnspan=2)
                label_rat3.grid(row=1)
                dropDownBox31 = ttk.Combobox(root3,values=listItems)                                              
                dropDownBox31.grid(row=2,column=1)                             #display dropdown
                
                
                dropDownBox32 = ttk.Combobox(root3,values=listItems)                                               
                dropDownBox32.grid(row=3,column=1)   
                
                
                dropDownBox33 = ttk.Combobox(root3,values=listItems)                                                
                
                dropDownBox33.grid(row=4,column=1)
                
            
            #Fourth Shell
            
            if p4%2==1 or p13%2==1:
                
                root4=ttk.Frame(notebook)
                
                
                
                notebook.add(root4, text="Central clearing requirements and capabilities") 
        #        root4.grid(row=1,column=1,sticky="NE")
                label_En41=ttk.Label(root4, text="Yes")
                label_En42=ttk.Label(root4, text="No")
                label_En41.grid(row=2)
                label_En42.grid(row=3)
                
                label_Met4=ttk.Label(root4,text="Liquidity Rating")
                label_rat4=ttk.Label(root4,text="Central clearing requirements and capabilities")
                label_Met4.grid(row=1, column=1,columnspan=2)
                label_rat4.grid(row=1)
                dropDownBox41 = ttk.Combobox(root4,values=listItems)                                            
                dropDownBox41.grid(row=2,column=1)                             #display dropdown
                dropDownBox42 = ttk.Combobox(root4,values=listItems)                                               
                dropDownBox42.grid(row=3,column=1)   
                
            
            #Fifth Shell
           
            if p5%2==1 or p13%2==1:
                
                root5=ttk.Frame(notebook)
                notebook.add(root5, text="Overall Risk Rating") 
                
                label_Met5=ttk.Label(root5,text="Liquidity Rating")
                label_rat5=ttk.Label(root5,text="Overall Risk Rating")
                label_Met5.grid(row=0, column=1,columnspan=2)
                label_rat5.grid(row=0) 
               
                
                ORlis=check3["Overall riskiness"].unique()
                y2=len(ORlis)
                ORlis=list(set(ORlis))
               # print(y2)
                alis=alis + ORlis
                l1=1
                l2=1
                l3=1
                l4=1
                for i in range(y1,y1+y2) :
                    if a2<=13:  
                        
                        label1=ttk.Label(root5,text=alis[i])
                        label1.grid(row=l1,column=0)
                        box1 = ttk.Combobox(root5,values=listItems)
                        box1["values"] = listItems
                        box1.grid(row=l1, column=1, pady=1, padx=1, sticky=E+W+N+S)
                        box2_dict[i] =box1
                        box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon2(event,i))
                        l1=l1+1
                #    print(box1["values"][i])
                    elif a2 < 26 :
                        label_Met6=ttk.Label(root5,text="Liquidity Rating")
                        label_rat6=ttk.Label(root5,text="Overall Risk Rating")
                        label_Met6.grid(row=0, column=3,columnspan=2)
                        label_rat6.grid(row=0,column=2)
                
                       
                        label1=ttk.Label(root5,text=alis[i])
                        label1.grid(row=l2,column=2)
                        box1 = ttk.Combobox(root5,values=listItems)
                        box1["values"] = listItems
                        box1.grid(row=l2, column=3, pady=1, padx=1, sticky=E+W+N+S)
                        box2_dict[i] =box1
                        box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon2(event,i))
                        l2=l2+1
                    elif a2 < 39 :
                        #print(a3)
                        label_Met6=ttk.Label(root5,text="Liquidity Rating")
                        label_rat6=ttk.Label(root5,text="Overall Risk Rating")
                        label_Met6.grid(row=0, column=7,columnspan=2)
                        label_rat6.grid(row=0,column=6)
                
                       
                        label1=ttk.Label(root5,text=alis[i])
                        label1.grid(row=l3,column=6)
                        box1 = ttk.Combobox(root5,values=listItems)
                        box1["values"] = listItems
                        box1.grid(row=l3, column=7, pady=1, padx=1, sticky=E+W+N+S)
                        box2_dict[i] =box1
                        box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon2(event,i))
                        l3=l3+1
                    elif a2 < 52 :
                        #print(a2)
                        label_Met6=ttk.Label(root5,text="Liquidity Rating")
                        label_rat6=ttk.Label(root5,text="Overall Risk Rating")
                        label_Met6.grid(row=0, column=10,columnspan=2)
                        label_rat6.grid(row=0,column=9)
                
                       
                        label1=ttk.Label(root5,text=alis[i])
                        label1.grid(row=l4,column=9)
                        box1 = ttk.Combobox(root5,values=listItems)
                        box1["values"] = listItems
                        box1.grid(row=l4, column=10, pady=1, padx=1, sticky=E+W+N+S)
                        box2_dict[i] =box1
                        box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon2(event,i))
                        l4=l4+1
                    
                    a2=a2+1  
            
            
            #Sixth Shell
            
            if p6%2==1 or p13%2==1:
                
                root6=ttk.Frame(notebook)
                notebook.add(root6, text="Currency denomination") 
                
                label_Met6=ttk.Label(root6,text="Liquidity Rating")
                label_rat6=ttk.Label(root6,text="Currency denomination Rating")
                label_Met6.grid(row=0, column=1,columnspan=1)
                label_rat6.grid(row=0)
                
                CDlis=check3["Currency_denomination"].unique()
                y3=len(CDlis)
                CDlis=list(set(CDlis))
                
                alis=alis + CDlis
                #print(alis)
                
                l1=1
                l2=1
                l3=1
                l4=1
                for i in range(y1+y2,y1+y2+y3) :
                    if a3<=13:  
                        
                        label1=ttk.Label(root6,text=alis[i])
                        label1.grid(row=l1,column=0)
                        box1 = ttk.Combobox(root6,values=listItems)
                        box1["values"] = listItems
                        box1.grid(row=l1, column=1, pady=1, padx=1, sticky=E+W+N+S)
                        box2_dict[i] =box1
                        box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon2(event,i))
                        l1=l1+1
                #    print(box1["values"][i])
                    elif a3 < 26 :
                        label_Met6=ttk.Label(root6,text="Liquidity Rating")
                        label_rat6=ttk.Label(root6,text="Currency denomination Rating")
                        label_Met6.grid(row=0, column=3,columnspan=2)
                        label_rat6.grid(row=0,column=2)
                
                       
                        label1=ttk.Label(root6,text=alis[i])
                        label1.grid(row=l2,column=2)
                        box1 = ttk.Combobox(root6,values=listItems)
                        box1["values"] = listItems
                        box1.grid(row=l2, column=3, pady=1, padx=1, sticky=E+W+N+S)
                        box2_dict[i] =box1
                        box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon2(event,i))
                        l2=l2+1
                    elif a3 < 39 :
                        #print(a3)
                        label_Met6=ttk.Label(root6,text="Liquidity Rating")
                        label_rat6=ttk.Label(root6,text="Currency denomination Rating")
                        label_Met6.grid(row=0, column=7,columnspan=2)
                        label_rat6.grid(row=0,column=6)
                
                       
                        label1=ttk.Label(root6,text=alis[i])
                        label1.grid(row=l3,column=6)
                        box1 = ttk.Combobox(root6,values=listItems)
                        box1["values"] = listItems
                        box1.grid(row=l3, column=7, pady=1, padx=1, sticky=E+W+N+S)
                        box2_dict[i] =box1
                        box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon2(event,i))
                        l3=l3+1
                    elif a3 < 52 :
                        print(a3)
                        label_Met6=ttk.Label(root6,text="Liquidity Rating")
                        label_rat6=ttk.Label(root6,text="Currency denomination Rating")
                        label_Met6.grid(row=0, column=10,columnspan=2)
                        label_rat6.grid(row=0,column=9)
                
                       
                        label1=ttk.Label(root6,text=alis[i])
                        label1.grid(row=l4,column=9)
                        box1 = ttk.Combobox(root6,values=listItems)
                        box1["values"] = listItems
                        box1.grid(row=l4, column=10, pady=1, padx=1, sticky=E+W+N+S)
                        box2_dict[i] =box1
                        box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon2(event,i))
                        l4=l4+1
                    
                    a3=a3+1
            
            if p7%2==1 or p13%2==1: 
                
                
                root7=ttk.Frame(notebook)
           
                
                notebook.add(root7, text="Security age & time to maturity")
                global i71,i72,i73
                i71=StringVar(root7)
                i72=StringVar(root7)
                i73=StringVar(root7)
              #  root7.grid(row=2,column=1,sticky="NE")
                label_En71=ttk.Label(root7, text="Highly Liquid")
                label_En72=ttk.Label(root7, text="Medium Liquid")
                label_En73=ttk.Label(root7, text="Low Liquid")
                Entry_71=ttk.Entry(root7,textvariable=i71).grid(row=2, column=1)
                Entry_72=ttk.Entry(root7,textvariable=i72).grid(row=3, column=1)
                Entry_73=ttk.Entry(root7,textvariable=i73).grid(row=4, column=1)
                label_Met7=ttk.Label(root7,text="Security age & time to maturity")
                label_rat7=ttk.Label(root7,text="Liquidity Rating")
                label_Met7.grid(row=1, column=1)
                label_rat7.grid(row=1)
                label_En71.grid(row=2)
                label_En72.grid(row=3)
                label_En73.grid(row=4)
            
            ##Eigth Shell
            
            
            if p8%2==1 or p13%2==1:
                
                root8=ttk.Frame(notebook)
                
                notebook.add(root8, text="Bid-Ask % Difference")
                global i81,i82,i83
                i81=StringVar(root8)
                i82=StringVar(root8)
                i83=StringVar(root8) 
             #   root8.grid(row=2,column=1,sticky="NE")
                label_En81=ttk.Label(root8, text="Highly Liquid")
                label_En82=ttk.Label(root8, text="Medium Liquid")
                label_En83=ttk.Label(root8, text="Low Liquid")
                Entry_81=ttk.Entry(root8,textvariable=i81).grid(row=2, column=1)
                Entry_82=ttk.Entry(root8,textvariable=i82).grid(row=3, column=1)
                Entry_83=ttk.Entry(root8,textvariable=i83).grid(row=4, column=1)
                label_Met8=ttk.Label(root8,text="Bid-Ask % Difference")
                label_rat8=ttk.Label(root8,text="Liquidity Rating")
                label_Met8.grid(row=1, column=1)
                label_rat8.grid(row=1)
                label_En81.grid(row=2)
                label_En82.grid(row=3)
                label_En83.grid(row=4)
            
            
           
            
            if p9%2==1 or p13%2==1:
                root9=ttk.Frame(notebooka)
                notebooka.add(root9, text="Issue/issuer credit quality")
                label_Met9=Label(root9,text="Liquidity Rating")
                label_rat9=Label(root9,text="Issue/issuer credit quality")
                
                label_Met9.grid(row=0, column=1,columnspan=2)
                label_rat9.grid(row=0)
                ISQlis=check3["Issue/issuer credit quality"].unique()
                y4=len(ISQlis)
                ISQlis=list(set(ISQlis))
                
                alis=alis + ISQlis
                print(alis)
                
                l1=1
                l2=1
                l3=1
                l4=1
                for i in range(y1+y2+y3,y1+y2+y3+y4) :
                    if a4<=13:  
                        
                        label1=ttk.Label(root9,text=alis[i])
                        label1.grid(row=l1,column=0)
                        box1 = ttk.Combobox(root9,values=listItems)
                        box1["values"] = listItems
                        box1.grid(row=l1, column=1, pady=1, padx=1, sticky=E+W+N+S)
                        box2_dict[i] =box1
                        box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon2(event,i))
                        l1=l1+1
                #    print(box1["values"][i])
                    elif a4 < 26 :
                        label_Met9=ttk.Label(root6,text="Liquidity Rating")
                        label_rat9=ttk.Label(root6,text="Issue/issuer credit quality")
                        label_Met9.grid(row=0, column=3,columnspan=2)
                        label_rat9.grid(row=0,column=2)
                
                       
                        label1=ttk.Label(root9,text=alis[i])
                        label1.grid(row=l2,column=2)
                        box1 = ttk.Combobox(root9,values=listItems)
                        box1["values"] = listItems
                        box1.grid(row=l2, column=3, pady=1, padx=1, sticky=E+W+N+S)
                        box2_dict[i] =box1
                        box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon2(event,i))
                        l2=l2+1
                    elif a4< 39 :
                        print(a3)
                        label_Met9=ttk.Label(root9,text="Liquidity Rating")
                        label_rat9=ttk.Label(root9,text="Issue/issuer credit quality")
                        label_Met9.grid(row=0, column=7,columnspan=2)
                        label_rat9.grid(row=0,column=6)
                
                       
                        label1=ttk.Label(root9,text=alis[i])
                        label1.grid(row=l3,column=6)
                        box1 = ttk.Combobox(root9,values=listItems)
                        box1["values"] = listItems
                        box1.grid(row=l3, column=7, pady=1, padx=1, sticky=E+W+N+S)
                        box2_dict[i] =box1
                        box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon2(event,i))
                        l3=l3+1
                    elif a4< 52 :
                        print(a3)
                        label_Met9=ttk.Label(root9,text="Liquidity Rating")
                        label_rat9=ttk.Label(root9,text="Issue/issuer credit quality")
                        label_Met9.grid(row=0, column=10,columnspan=2)
                        label_rat9.grid(row=0,column=9)
                
                       
                        label1=ttk.Label(root9,text=alis[i])
                        label1.grid(row=l4,column=9)
                        box1 = ttk.Combobox(root9,values=listItems)
                        box1["values"] = listItems
                        box1.grid(row=l4, column=10, pady=1, padx=1, sticky=E+W+N+S)
                        box2_dict[i] =box1
                        box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon2(event,i))
                        l4=l4+1
                    
                    a4=a4+1
            
            ##Ninth Shell
            
            if p10%2==1 or p13%2==1:
                
                root10=ttk.Frame(notebooka)
                notebooka.add(root10, text="Geography")
                label_Met10=Label(root10,text="Liquidity Rating")
                label_rat10=Label(root10,text="Geography / Country")
                
                label_Met10.grid(row=0, column=1,columnspan=1)
                label_rat10.grid(row=0)
                glis=check3["Geography_Country"].unique()
                y5=len(glis)
                glis=list(set(glis))
                
                alis=alis + glis
               # print(alis)
                
                l1=1
                l2=1
                l3=1
                l4=1
                for i in range(y1+y2+y3+y4,y1+y2+y3+y4+y5) :
                    if a5<=13:  
                        
                        label1=ttk.Label(root10,text=alis[i])
                        label1.grid(row=l1,column=0)
                        box1 = ttk.Combobox(root10,values=listItems)
                        box1["values"] = listItems
                        box1.grid(row=l1, column=1, pady=1, padx=1, sticky=E+W+N+S)
                        box2_dict[i] =box1
                        box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon2(event,i))
                        l1=l1+1
                #    print(box1["values"][i])
                    elif a5 < 26 :
                        label_Met10=ttk.Label(root10,text="Liquidity Rating")
                        label_rat10=ttk.Label(root10,text="Geography / Country")
                        label_Met10.grid(row=0, column=3,columnspan=2)
                        label_rat10.grid(row=0,column=2)
                
                       
                        label1=ttk.Label(root10,text=alis[i])
                        label1.grid(row=l2,column=2)
                        box1 = ttk.Combobox(root10,values=listItems)
                        box1["values"] = listItems
                        box1.grid(row=l2, column=3, pady=1, padx=1, sticky=E+W+N+S)
                        box2_dict[i] =box1
                        box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon2(event,i))
                        l2=l2+1
                    elif a5< 39 :
                        print(a3)
                        label_Met10=ttk.Label(root10,text="Liquidity Rating")
                        label_rat10=ttk.Label(root10,text="Geography / Country")
                        label_Met10.grid(row=0, column=7,columnspan=2)
                        label_rat10.grid(row=0,column=6)
                
                       
                        label1=ttk.Label(root10,text=alis[i])
                        label1.grid(row=l3,column=6)
                        box1 = ttk.Combobox(root10,values=listItems)
                        box1["values"] = listItems
                        box1.grid(row=l3, column=7, pady=1, padx=1, sticky=E+W+N+S)
                        box2_dict[i] =box1
                        box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon2(event,i))
                        l3=l3+1
                    elif a5< 52 :
                        print(a3)
                        label_Met10=ttk.Label(root10,text="Liquidity Rating")
                        label_rat10=ttk.Label(root10,text="Geography / Country")
                        label_Met10.grid(row=0, column=10,columnspan=2)
                        label_rat10.grid(row=0,column=9)
                
                       
                        label1=ttk.Label(root10,text=alis[i])
                        label1.grid(row=l4,column=9)
                        box1 = ttk.Combobox(root10,values=listItems)
                        box1["values"] = listItems
                        box1.grid(row=l4, column=10, pady=1, padx=1, sticky=E+W+N+S)
                        box2_dict[i] =box1
                        box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon2(event,i))
                        l4=l4+1
                    
                    a5=a5+1   
            
            
            
            
            
            
            
            
            
            
            
                 
                 
                 
                 
                 ### Eleven Shell
             
            if p11%2==1 or p13%2==1:
                root11=ttk.Frame(notebooka)  
                
                notebooka.add(root11, text="30 day Volatility index number")
                global i111,i112,i113
                i111=StringVar(root11)
                i112=StringVar(root11)
                i113=StringVar(root11)
                label_En111=Label(root11, text="Highly Liquid")
                label_En112=Label(root11, text="Medium Liquid")
                label_En113=Label(root11, text="Low Liquid")
        #        button1=Button(self,text="Submit",command=para,fg="red").grid(row=10, column=1,sticky="SE")
                Entry_111=Entry(root11,textvariable=i111).grid(row=1, column=1)
                Entry_112=Entry(root11,textvariable=i112).grid(row=2, column=1)
                Entry_113=Entry(root11,textvariable=i113).grid(row=3, column=1)
                label_Met11=Label(root11,text="30 day Volatility index number")
                label_rat11=Label(root11,text="Liquidity Rating")
                label_Met11.grid(row=0, column=1)
                label_rat11.grid(row=0)
                label_En111.grid(row=1)
                label_En112.grid(row=2)
                label_En113.grid(row=3)
            #
            #
            ### Twelve Shell
            
            if p12%2==1 or p13%2==1:
                
                root12=ttk.Frame(notebooka)
                
                notebooka.add(root12, text="Position size as a   % of Total O/s")
                global i121,i122,i123
                i121=StringVar(root12)
                i122=StringVar(root12)
                i123=StringVar(root12)
                label_En121=Label(root12, text="Highly Liquid")
                label_En122=Label(root12, text="Medium Liquid")
                label_En123=Label(root12, text="Low Liquid")
                Entry_121=Entry(root12,textvariable=i121).grid(row=2, column=1)
                Entry_122=Entry(root12,textvariable=i122).grid(row=3, column=1)
                Entry_123=Entry(root12,textvariable=i123).grid(row=4, column=1)
                label_Met12=Label(root12,text="Position size as a   % of Total O/s")
                label_rat12=Label(root12,text="Liquidity Rating")
                label_Met12.grid(row=1, column=1)
                label_rat12.grid(row=1)
                label_En121.grid(row=2)
                label_En122.grid(row=3)
                label_En123.grid(row=4)        
            if p14%2==1 or p13%2==1:
                
                root14=ttk.Frame(notebooka)
                
                notebooka.add(root14, text="Position as a % of Avg. Daily Volume")
                global i141,i142,i143
                i141=StringVar(root14)
                i142=StringVar(root14)
                i143=StringVar(root14)
                label_En141=Label(root14, text="Highly Liquid")
                label_En142=Label(root14, text="Medium Liquid")
                label_En143=Label(root14, text="Low Liquid")
                Entry_141=Entry(root14,textvariable=i141).grid(row=2, column=1)
                Entry_142=Entry(root14,textvariable=i142).grid(row=3, column=1)
                Entry_143=Entry(root14,textvariable=i143).grid(row=4, column=1)
                label_Met14=Label(root14,text="Position as a % of Avg. Daily Volume")
                label_rat14=Label(root14,text="Liquidity Rating")
                label_Met14.grid(row=1, column=1)
                label_rat14.grid(row=1)
                label_En141.grid(row=2)
                label_En142.grid(row=3)
                label_En143.grid(row=4)
        
        
        
        
        
        
        
        
            notebook.grid(row=1,column=0,sticky="W")
            
            separator = Frame(roots,height=2, bd=1, relief=SUNKEN)
            separator.grid(columnspan=10,sticky=N+S+E+W)
    #        label = Label(roots, text="Assumptions", font="Verdana 24 bold",bg="black",fg="white")
    #        label.grid(columnspan=500)
            notebooka.grid(row=3,column=0,sticky="W")
            notebook.update()
            notebooka.update()
            
            button1=ttk.Button(roots,text="Submit",command=para)
            button1.grid(row=4, column=0,sticky="E")
            roots.grid(row=0,column=0,sticky=N+E+W+S)
#            vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
#            canvas.configure(yscrollcommand=vsb.set)
#            canvas.config(scrollregion=(0, 0, 10000, 10000))
#            vsb.grid(row=0,column=5,rowspan=10,sticky=N+E+S)            
#            canvas.grid(row=0,column=0,rowspan=10,sticky=N+E+W+S)
#            #canvas.create_window((10,10),window=roots, anchor="center")
#            canvas.create_rectangle(0,0,10,10)
            root.bind("<Configure>", resize)
            
            
            
            
            
            
            
            
            

#            populate(roots)
            

            
            
            
         
    
#            button = Button(root, text="Go to the start page",
#                                           command=lambda: controller.show_frame("StartPage"))
#            button.grid(row=10,column=0,sticky="W")


 
def ps():
    
        global stroot2,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14
        global r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r14
        rootp=Tk()
        stroot2=Frame(rootp)
        stroot2.grid()
        
        
        c1 = ttk.Checkbutton(stroot2, text="No of Brokers",command=inp1)
        p1=0
        r1=0
        c1.grid(row=0,column=0,sticky=W)
        c2 = ttk.Checkbutton(stroot2, text="Type of broker dealers",command=inp2)
        p2=0
        r2=0
        c2.grid(row=1,column=0,sticky=W)
        
        c3 = ttk.Checkbutton(stroot2, text="Types of Exchange Structure",command=inp3)
        p3=0
        r3=0
        c3.grid(row=2,column=0,sticky=W)
        c4 = ttk.Checkbutton(stroot2, text="Central clearing requirements and capabilities",command=inp4)
        p4=0
        r4=0
        c4.grid(row=3,column=0,sticky=W)
        c5 = ttk.Checkbutton(stroot2, text="Overall Risk Rating",command=inp5)
        p5=0
        r5=0
        c5.grid(row=4,column=0,sticky=W)
        c6 = ttk.Checkbutton(stroot2, text="Currency denomination",command=inp6)
        p6=0
        r6=0
        c6.grid(row=5,column=0,sticky=W)
        c7 = ttk.Checkbutton(stroot2, text="Security age & time to maturity",command=inp7)
        p7=0
        r7=0
        c7.grid(row=6,column=0,sticky=W)
        c8 = ttk.Checkbutton(stroot2, text="Bid-Ask % Difference",command=inp8)
        p8=0
        r8=0
        c8.grid(row=7,column=0,sticky=W)
        c9 = ttk.Checkbutton(stroot2, text="Issue/issuer credit quality",command=inp9)
        p9=0
        r9=0
        c9.grid(row=8,column=0,sticky=W)
        c10 = ttk.Checkbutton(stroot2, text="Geography",command=inp10)
        p10=0
        r10=0
        c10.grid(row=9,column=0,sticky=W)
        c11= ttk.Checkbutton(stroot2, text="30 day Volatility index number",command=inp11)
        p11=0
        r11=0
        c11.grid(row=10,column=0,sticky=W)
        c12= ttk.Checkbutton(stroot2, text="Position size as a   % of Total O/s",command=inp12)
        p12=0
        r12=0
        c12.grid(row=11,column=0,sticky=W)
        
        
        c14= ttk.Checkbutton(stroot2, text="Position as a % of Avg. Daily Volume",command=inp14)
        p14=0
        r14=0
        c14.grid(row=12,column=0,sticky=W)
        
        c13= ttk.Checkbutton(stroot2, text="Choose Everything",command=inp13)
        p13=0
        c13.grid(row=13,column=0,sticky=W)
        
        
        buttonp1 = ttk.Button(stroot2,text="Submit Parameters",command=rootp.destroy)
        
        buttonp1.grid(row=20,column=3,sticky=S)
        buttonp2 = ttk.Button(stroot2,text="Cancel",command=rootp.destroy)
        
        buttonp2.grid(row=20,column=4,sticky=S)
        
        separator = Frame(stroot2,height=2, bd=1, relief=SUNKEN)
        separator.grid(row=30,column=0,rowspan=300,columnspan=2000,sticky=N+S+E+W)
        
        labelr1=Label(stroot2, text="**Highly Liquid : 4")
        labelr1.grid(column=0,sticky=W)
        
        labelr2=Label(stroot2, text="**Medium Liquid : 3")
        labelr2.grid(column=0,sticky=W)
       
        labelr3=Label(stroot2, text="**Low Liquid : 2")
        labelr3.grid(column=0,sticky=W)
       
        labelr4=Label(stroot2, text="**Illiquid Liquid : 1")
        labelr4.grid(column=0,sticky=W)
       
        
       
        
    
  

   
def missingdata():
    global filename
    global check1,mcolor,co,check2,check3,stroot
    co=0
    
    
    check1=pd.read_excel(filename)
    check1[["No._of_broker_dealers","Diversity_of_broker_dealers","Exchange_structure","Overall riskiness Status","Issue/issuer credit quality","Industry","Currency_denomination","Geography_Country","Security age & time to maturity1 Status","30 day Volatility index number","Position sizes (% Net)","Amount Outstanding","average daily trading volume of the asset","Position as a % of Avg. Daily Volume"]]=check1[["No._of_broker_dealers","Diversity_of_broker_dealers","Exchange_structure","Overall riskiness Status","Issue/issuer credit quality","Industry","Currency_denomination","Geography_Country","Security age & time to maturity1 Status","30 day Volatility index number","Position sizes (% Net)","Amount Outstanding","average daily trading volume of the asset","Position as a % of Avg. Daily Volume"]].fillna(value="Mandatory")
    k=len(check1["Exchange_structure"])
    check1["Central clearing requirements and capabilities"]=check1["Central clearing requirements and capabilities"].fillna(value="False")
    for row in range(0,k):    
        if check1["Exchange_structure"][row]=="OTC":    
            if check1["Central clearing requirements and capabilities"][row]=="False":
                check1["Central clearing requirements and capabilities"][row]="Mandatory"
        elif check1["Central clearing requirements and capabilities"][row]=="False":
            check1["Central clearing requirements and capabilities"][row]="NM"
    check1["Overall riskiness"]=check1["Overall riskiness"].fillna(value="False")
    for row in range(0,k):    
   
        if check1["Overall riskiness Status"][row]!="N":
            if check1["Overall riskiness"][row]=="False":
                check1["Overall riskiness"][row]="Mandatory"
            
        elif check1["Overall riskiness"][row]=="False":
                check1["Overall riskiness"][row]="NM"
                
    #print(check1["Overall riskiness"])
    check1["Security age & time to maturity1"]=check1["Security age & time to maturity1"].fillna(value="False")
    for row in range(0,k):    
   
        if check1["Security age & time to maturity1 Status"][row]=="Y":
            if check1["Security age & time to maturity1"][row]=="False":
                check1["Security age & time to maturity1"][row]="Mandatory"
            
        elif check1["Security age & time to maturity1"][row]=="False":
                check1["Security age & time to maturity1"][row]="NM"
    check1["Bid-Ask Spread rates (%)"]=check1["Bid-Ask Spread rates (%)"].fillna(value="False")
    
    for row in range(0,k):    
   
        if check1["Bid-Ask Spread rates Status"][row]=="Y":
            if check1["Bid-Ask Spread rates (%)"][row]=="False":
                check1["Bid-Ask Spread rates (%)"][row]="Mandatory"
            
        elif check1["Bid-Ask Spread rates (%)"][row]=="False":
                check1["Bid-Ask Spread rates (%)"][row]="NM"
                
   # print(check1["Security age & time to maturity1"])
    #for row in range(0,k):         
    #if  any(check1["Central clearing requirements and capabilities"][row],check1["No. of broker dealers"],check1["Issue/issuer credit quality"],check1["Industry"],check1["Currency denomination"],check1["Geography / Country"],check1["Overall riskiness"],check1["Diversity of broker dealers"],check1["Exchange structure"],check1["Bid rates"],check1["Ask rates"],check1["30 day Volatility index number"],check1["Position sizes (% Net)"]]=="Mandatory"):
    check2=check1.as_matrix()
    [r,c]=check2.shape
    for j in range(0,c):
        for i in range(0,r):
            if check2[i,j]=="Mandatory":
                co=co+1
   
    
        
    msg="You have %d missing value"%(co)    
    tkinter.messagebox.showinfo("Window Title",msg)
    check2=pd.DataFrame(check2)
    check2.columns = ["Portfolio","Sector","Security Type","Security","Ticker","No._of_broker_dealers","Diversity_of_broker_dealers","Exchange_structure","Central clearing requirements and capabilities","Overall riskiness Status","Overall riskiness","Issue/issuer credit quality","Industry","Currency_denomination","Geography_Country","Security age & time to maturity1 Status","Security age & time to maturity1","Bid-Ask Spread rates Status","Bid-Ask Spread rates (%)","Type of security","Description","30 day Volatility index number","Position sizes","Position sizes (% Net)","Amount Outstanding","average daily trading volume of the asset","Position as a % of Avg. Daily Volume","Weightage"]
    check3=check2.copy()
    if (co>0):
        down = PhotoImage(file="D:\python\ALARM IMAGES\Download.gif")
        button5 = Button(stroot,text="Download Missing Data-Point",command=mdcheck,bg="red",image=down)
        button5.image_names=down
        button5.grid(row=1,column=9,columnspan=1,sticky=E+W,padx=50)
       
def accpr():
    global t1,t2,t3,t4,t5,t6,t7,f,lis,df,checka,t8,check2,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,rootm
    t1=1
    t2=1
    t3=1
    t4=1
    t5=1
    t6=1
    t7=1
    t8=1
    
    lisv=[]
    lis=[]
    llis=[]
    llis2=[]
    llis3=[]
    llis4=[]
    llis5=[]
    llis6=[]
    llis7=[]
    llis8=[]
    
    global box1_dict 
    box1_dict = {}
    r1=0
    r2=0
    r3=0
    r4=0
    r5=0
    r6=0
    r7=0
    r8=0
    def change_icon(event,i):
        global box_dict,f,lis,df,lisv
        lis.append(box1_dict[i].get())
        
        lisv.append(llis[i])
                   
        #print("The user selected value now is:")
        #print("This is selection",lis)
        df = pd.DataFrame({'col1':lisv,'col2':lis})
       # print("Data Frame",df)
    def savedf():
        global df,check2,check3,rootm
        
        tkinter.messagebox.showinfo("Window Title","Data Replaced")
        
        rootm.destroy()
        
        df.to_csv("df.csv")
        repl=pd.read_csv("df.csv")
    
        repl=repl.as_matrix()
        [r1,c1]=repl.shape  
        
       
        check3=check2.as_matrix()
        [r2,c2]=check3.shape
        
        for z in range(0,r1):
            rep=StringVar()
            mat=StringVar()
            rep=repl[z,2]
            mat=repl[z,1]
    #            if rep.isnumeric():
    #                rep=float(rep)
    #            
    #           
    #            if mat.isnumeric():
    #                mat=float(mat)
    #           
            
            for j in range(0,c2):
                for i in range(0,r2):
                    if (check3[i,j]== mat):
                        
                        check3[i,j] = rep
                        
                       
    
        check3=pd.DataFrame(check3)
        check3.columns = ["Portfolio","Sector","Security Type","Security","Ticker","No._of_broker_dealers","Diversity_of_broker_dealers","Exchange_structure","Central clearing requirements and capabilities","Overall riskiness Status","Overall riskiness","Issue/issuer credit quality","Industry","Currency_denomination","Geography_Country","Security age & time to maturity1 Status","Security age & time to maturity1","Bid-Ask Spread rates Status","Bid-Ask Spread rates (%)","Type of security","Description","30 day Volatility index number","Position sizes","Position sizes (% Net)","Amount Outstanding","average daily trading volume of the asset","Position as a % of Avg. Daily Volume","Weightage"]
        check3.to_excel("checkacc.xlsx")
    
    
       
        
        
        
    
    rootm = Tk()
    global explis,check2
    
    explis=pd.read_csv("D:/python/Exception list.csv")
    exp1=explis["Diversity of broker dealers"]
    exp1=exp1.dropna()
    exp1=list(exp1)
    exp1=sorted(exp1, key=str.lower)
    
    exp2=explis["Exchange structure"]
    exp2=exp2.dropna()
    exp2=list(exp2)
    exp2=sorted(exp2, key=str.lower)
    
    exp3=explis["Overall riskiness"]
    exp3=exp3.dropna()
    exp3=list(exp3)
    exp3=sorted(exp3, key=str.lower)
    
    exp4=explis["Issue/issuer credit quality"]
    exp4=exp4.dropna()
    exp4=list(exp4)
    exp4=sorted(exp4, key=str.lower)
    
    exp5=explis["Currency denomination"]
    exp5=exp5.dropna()
    exp5=list(exp5)
    exp5=sorted(exp5, key=str.lower)
    
    
    exp6=explis["Geography / Country"]
    exp6=exp6.dropna()
    exp6=list(exp6)
    exp6=sorted(exp6, key=str.lower)
    
    
     
    checka=check2
    notebook = ttk.Notebook(rootm)
    
    #    check1=pd.read_excel(filename)
    
    ##1(Diversity of broker dealers)
       # if p2%2==1 or p13%2==1:
    root1=ttk.Frame(notebook)
    notebook.add(root1, text="Diversity of broker dealers") 
    
    
    
    for row1 in checka["Diversity_of_broker_dealers"]:
        if row1 not in exp1:
            llis.append(row1)
    llis=list(set(llis))
    r1=len(llis)
    if (r1 > 0):
            labelh1=ttk.Label(root1,text="DBD Error")
            labelh1.grid(row=0)
            labelhr1=ttk.Label(root1,text="DBD Value")
            labelhr1.grid(row=0,column=1)
            
            for i in range(r1):
                label1=ttk.Label(root1,text=llis[i])
                label1.grid(row=t1)
                
                
                
                box1 = ttk.Combobox(root1,values=exp1.sort)
                box1["values"] = exp1
                box1.grid(row=t1, column=1, pady=1, padx=1, sticky=E+W+N+S)
                box1_dict[i] =box1
                box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon(event,i))
            #    print(box1["values"][i])
            
                t1=t1+1
    ##2(Exchange structure)
    #if p3%2==1 or p13%2==1:
    root2=ttk.Frame(notebook)
    notebook.add(root2, text="Exchange structure") 
    for row2 in checka["Exchange_structure"]:
        if row2 not in exp2:
            llis2.append(row2)
    llis2=list(set(llis2))
    llis=llis+llis2
    r2=len(llis2)
   # print(llis,r1,r2)
    if (r2 > 0):
        labelh1=ttk.Label(root2,text="ES Error")
        labelh1.grid(row=0,column=2)
        labelhr1=ttk.Label(root2,text="ES Value")
        labelhr1.grid(row=0,column=3)
        
            
        for i in range(r1,r1+r2) :
            label1=ttk.Label(root2,text=llis[i])
            label1.grid(row=t2,column=2)
            box1 = ttk.Combobox(root2,values=exp2.sort)
            box1["values"] = exp2
            box1.grid(row=t2, column=3, pady=1, padx=1, sticky=E+W+N+S)
            box1_dict[i] =box1
            box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon(event,i))
        #    print(box1["values"][i])
            t2=t2+1
    
    ##3(Central clearing requirements and capabilities)
     #   if p4%2==1 or p13%2==1:
    root3=ttk.Frame(notebook)
    notebook.add(root3, text="Central clearing requirements and capabilities") 
    for row3 in checka["Central clearing requirements and capabilities"]:
        if row3 not in {"Y","N","Mandatory","NM"}:
            llis3.append(row3)
    llis3=list(set(llis3))
    llis=llis+llis3
    r3=len(llis3)
    if (r3 > 0):
        labelh1=ttk.Label(root3,text="CCC Error")
        labelh1.grid(row=0,column=4)
        labelhr1=ttk.Label(root3,text="CCC Value")
        labelhr1.grid(row=0,column=5)
        for i in range(r1+r2,r1+r2+r3):
            label1=ttk.Label(root3,text=llis[i])
            label1.grid(row=t3,column=4)
            box1 = ttk.Combobox(root3,values=("Y","N","Mandatory"))
            box1["values"] = ("Y","N","Mandatory")
            box1.grid(row=t3, column=5, pady=1, padx=1, sticky=E+W+N+S)
            box1_dict[i] =box1
            box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon(event,i))
            #print(box1["values"][i])
            t3=t3+1
       # if p5%2==1 or p13%2==1:
    root4=ttk.Frame(notebook)
    notebook.add(root4, text="Overall riskiness")
    for row4 in checka["Overall riskiness"]:
        if row4 not in exp3:
            llis4.append(row4)
    llis4=list(set(llis4))
    llis=llis+llis4
    r4=len(llis4)
    #        print(llis)
    if (r4 > 0):
        labelh1=ttk.Label(root4,text="OR Error")
        labelh1.grid(row=0,column=6)
        labelhr1=ttk.Label(root4,text="OR Value")
        labelhr1.grid(row=0,column=7)
        for i in range(r1+r2+r3,r1+r2+r3+r4):
            label1=ttk.Label(root4,text=llis[i])
            label1.grid(row=t4,column=6)
            box1 = ttk.Combobox(root4,values=exp3)
            box1["values"] = exp3
            box1.grid(row=t4, column=7, pady=1, padx=1, sticky=E+W+N+S)
            box1_dict[i] =box1
            box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon(event,i))
            #print(box1["values"][i])
            t4=t4+1
      #  if p9%2==1 or p13%2==1:
    root5=ttk.Frame(notebook)
    notebook.add(root5, text="Issue/issuer credit quality")
            
    
    for row5 in checka["Issue/issuer credit quality"]:
        if row5 not in exp4:
            llis5.append(row5)
    llis5=list(set(llis5))
    llis=llis+llis5
    r5=len(llis5)
    #print(llis5,r5)
    if (r5 > 0):
        labelh1=ttk.Label(root5,text="ISQ Error")
        labelh1.grid(row=0,column=8)
        labelhr1=ttk.Label(root5,text="ISQ Value")
        labelhr1.grid(row=0,column=9)
        for i in range(r1+r2+r3+r4,r1+r2+r3+r4+r5):
            label1=ttk.Label(root5,text=llis[i])
            label1.grid(row=t5,column=8)
            box1 = ttk.Combobox(root5,values=exp4)
            box1["values"] = exp4
            box1.grid(row=t5, column=9, pady=1, padx=1, sticky=E+W+N+S)
            box1_dict[i] =box1
            box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon(event,i))
            #print(box1["values"][i])
            t5=t5+1
     #   if p6%2==1 or p13%2==1:
    root6=ttk.Frame(notebook)
    notebook.add(root6, text="Currency denomination")
    for row6 in checka["Currency_denomination"]:
        if row6 not in exp5:
            llis6.append(row6)
    llis6=list(set(llis6))
    llis=llis+llis6
    r6=len(llis6)
            
    #        print(llis)
    if (r6 > 0):
        labelh1=ttk.Label(root6,text="CD Error")
        labelh1.grid(row=0,column=10)
        labelhr1=ttk.Label(root6,text="CD Value")
        labelhr1.grid(row=0,column=11)
        for i in range(r1+r2+r3+r4+r5,r1+r2+r3+r4+r5+r6):
            label1=ttk.Label(root6,text=llis[i])
            label1.grid(row=t6,column=10)
            box1 = ttk.Combobox(root6,values=exp5)
            box1["values"] = exp5
            box1.grid(row=t6, column=11, pady=1, padx=1, sticky=E+W+N+S)
            box1_dict[i] =box1
            box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon(event,i))
            #print(box1["values"][i])
            t6=t6+1
    
      #  if p10%2==1 or p13%2==1:        
    root7=ttk.Frame(notebook)
    notebook.add(root7, text="Geography / Country")
    for row7 in checka["Geography_Country"]:
        if row7 not in exp6:
            llis7.append(row7)
    llis7=list(set(llis7))
    llis=llis+llis7
    r7=len(llis7)
    #        print(llis)
    if (r7 > 0):
        labelh1=ttk.Label(root7,text="G/C Error")
        labelh1.grid(row=0,column=12)
        labelhr1=ttk.Label(root7,text="G/C Value")
        labelhr1.grid(row=0,column=13)
        for i in range(r1+r2+r3+r4+r5+r6,r1+r2+r3+r4+r5+r6+r7):
            label1=ttk.Label(root7,text=llis[i])
            label1.grid(row=t7,column=12)
            box1 = ttk.Combobox(root7,values=exp6)
            box1["values"] = exp6
            box1.grid(row=t7, column=13, pady=1, padx=1, sticky=E+W+N+S)
            box1_dict[i] =box1
            box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon(event,i))
            #print(box1["values"][i])
            t7=t7+1
      #  if p1%2==1 or p13%2==1:
    root8=ttk.Frame(notebook)
    notebook.add(root8, text="No. of broker dealers")
    for row8 in checka["No._of_broker_dealers"]:
        if row8 not in range(0,999):
            llis8.append(row8)
    llis8=list(set(llis8))
    llis=llis+llis8
    r8=len(llis8)
   # print(r8)
    if (r8 > 0):
        labelh1=ttk.Label(root8,text="NB Error")
        labelh1.grid(row=0,column=1)
        labelhr1=ttk.Label(root8,text="NB Value")
        labelhr1.grid(row=0,column=2)
        for i in range(r1+r2+r3+r4+r5+r6+r7,r1+r2+r3+r4+r5+r6+r7+r8):
            label1=ttk.Label(root8,text=llis[i])
            label1.grid(row=t8,column=1)
            nums=range(0,999)
            box1 = ttk.Combobox(root8,values=list(nums))
            box1["values"] = list(nums)
            box1.grid(row=t8, column=2, pady=1, padx=1, sticky=E+W+N+S)
            box1_dict[i] =box1
            
            box1.bind("<<ComboboxSelected>>",lambda event, i=i:change_icon(event,i))
            #print(box1["values"][i])
            t8=t8+1
            
      
            
            
    
    notebook.grid()
    
    
    
    
    
    
    button = ttk.Button(rootm,text="Replace",command=savedf)
    button.grid(sticky=S+E)
            
       
    
    #rootb.grid(row=5000,column=0,sticky=S+W)
    separator = Frame(rootm,height=2, bd=1, relief=SUNKEN)
    separator.grid(row=300,columnspan=2000,sticky=N+S+E+W)
    labeln=ttk.Label(rootm,text="*DBD=Diversity of broker dealers")
    labeln.grid(sticky=N+S+E+W)
    
    labeln=ttk.Label(rootm,text="*ES=Exchange Structure")
    labeln.grid(sticky=N+S+E+W)
    labeln=ttk.Label(rootm,text="*CCC=Central clearing requirements and capabilities")
    labeln.grid(sticky=N+S+E+W)
    labeln=ttk.Label(rootm,text="*OR=Overall riskiness")
    labeln.grid(sticky=N+S+E+W)
    labeln=ttk.Label(rootm,text="*ISQ=Issue/issuer credit quality")
    labeln.grid(sticky=N+S+E+W)
    labeln=ttk.Label(rootm,text="*CD=Currency denomination")
    labeln.grid(sticky=N+S+E+W)
    labeln=ttk.Label(rootm,text="*G/C=Geography / Country")
    labeln.grid(sticky=N+S+E+W)
    labeln=ttk.Label(rootm,text="*NB=No of Brokers")
    labeln.grid(sticky=N+S+E+W)
        
        
        
        
         
def mdcheck():
    global check2
    
    
    check2.to_excel("check1.xlsx")
    df=pd.read_excel("check1.xlsx")
    writer = pd.ExcelWriter('missind data.xlsx', engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='report')
    workbook = writer.book
    worksheet = writer.sheets['report']
    format1 = workbook.add_format({'bold': True, 'italic': 1,'bg_color': '#FF0000',})
    worksheet.conditional_format('A1:AH2000', {'type': 'text',
                                           'criteria': "containing",
                                           'value': "Mandatory",
                                           'format': format1})
    writer.save()
    tkinter.messagebox.showinfo("Window Title","File saved in D drive python folder as missind data.xlsx")
    stroot.destroy()
    
    
    
    
#class SampleApp(Tk):
#    def __init__(self, *args, **kwargs):
#        Tk.__init__(self, *args, **kwargs)
#        
def dispy1():
    global h1,buttonps1,buttonpa1,paras,parac,arrow,arrow2
    h1=h1+1
    if h1==1:
        arrow_label = Label(stroot,image=arrow)
        arrow_label.grid(row=3,column=3)            
        arrow_label.image = arrow
        buttonps1 = ttk.Button(stroot,text="Parameter Selection",command=ps,image=paras)
        buttonps1.image=paras
        buttonps1.grid(row=3,column=5,columnspan=1,sticky=E+W,padx=50)
        
        arrow_label = Label(stroot,image=arrow)
        arrow_label.grid(row=3,column=7)            
        arrow_label.image = arrow
        buttonpa1 = ttk.Button(stroot, text="Parameter Assumption",
                            command=dypar,image=parac)
        buttonpa1.image=parac
        buttonpa1.grid(row=3,column=9,columnspan=1,sticky=E+W,padx=50)
    
    
def dispy2():
    global h2,buttonps2,buttonpa2,paras,parac,arrow,arrow2
    h2=h2+1
    if h2==1:
        
        arrow_label = Label(stroot,image=arrow)
        arrow_label.grid(row=5,column=3)            
        arrow_label.image = arrow
        buttonps2 = ttk.Button(stroot,text="Parameter Selection",command=ps,image=paras)
        buttonps2.image=paras
        buttonps2.grid(row=5,column=5,columnspan=2,sticky=E+W,padx=50)
        
        arrow_label = Label(stroot,image=arrow)
        arrow_label.grid(row=5,column=7)            
        arrow_label.image = arrow
        buttonpa2 = ttk.Button(stroot, text="Parameter Assumption",
                            command=dypar,image=parac)
        buttonpa2.image=parac
        buttonpa2.grid(row=5,column=9,columnspan=2,sticky=E+W,padx=50)
    

def dispy3():
    global h3,buttonps3,buttonpa3,paras,parac,arrow,arrow2
    h3=h3+1
    if h3==1:
        
        arrow_label = Label(stroot,image=arrow)
        arrow_label.grid(row=7,column=3)            
        arrow_label.image = arrow
        buttonps3 = ttk.Button(stroot,text="Parameter Selection",command=ps,image=paras)
        buttonps3.image=paras
        buttonps3.grid(row=7,column=5,columnspan=2,sticky=E+W,padx=50)
        
        arrow_label = Label(stroot,image=arrow)
        arrow_label.grid(row=7,column=7)            
        arrow_label.image = arrow
        buttonpa3 = ttk.Button(stroot, text="Parameter Assumption",
                            command=dypar,image=parac)
        buttonpa3.image=parac
        buttonpa3.grid(row=7,column=9,columnspan=2,sticky=E+W,padx=50)
    


stroot=Tk()

stroot.configure(background="black")

stroot.title("Crisil Alarm Tool")
global i11,i12,i13,colr
global portstatus
w, h = stroot.winfo_screenwidth(), stroot.winfo_screenheight()
stroot.geometry("%dx%d+0+0" % (w, h))
#stroot.geometry('1366x768')
#stroot.overrideredirect(True)

#stroot.grid(row=0,column=0,sticky=N)


#        path = "Crisil.png"
#        img = ImageTk.PhotoImage(Image.open("Crisil.png"))
#
##The Label widget is a standard Tkinter widget used to display a text or image on the screen.
#        #panel = tk.Label(window, image = img)
#
##The Pack geometry manager packs widgets in rows or columns.
#        panel.grid(row=0,column=0,sticky=N)

#label = Label(stroot, text="Crisil Ltd", font="Verdana 24 bold",bg="black",fg="white")
#label.pack(side="top", fill="x", pady=10)
#label.grid(row=0,column=0,sticky=N)
#        strootI2=Frame(stroot)
#        strootI2.grid(row=0,column=0,rowspan=40)
        
#        strootI1=Frame(stroot)
#        strootI1.grid(row=0,column=0,columnspan=4)

#        strootI4=Frame(stroot)
#        strootI4.configure(background="Bisque")
#        strootI4.grid(row=0,column=2,rowspan=40)
   
    
global paras,parac,arrow,arrow2 


photo = PhotoImage(file="D:\python\ALARM IMAGES\wALL.png")
#alarmI=PhotoImage(file="D:\python\ALARM IMAGES\wALL.gif")
uploadI = PhotoImage(file="D:\python\ALARM IMAGES\Final Upload.gif")
missingD = PhotoImage(file="D:\python\ALARM IMAGES\Missing data Final.gif")
accprange = PhotoImage(file="D:\python\ALARM IMAGES\Acceptable ranges Final.gif")
sc1 = PhotoImage(file="D:\python\ALARM IMAGES\Scenario1Final.gif")
sc2 = PhotoImage(file="D:\python\ALARM IMAGES\Scenario2 Final.gif")
sc3 = PhotoImage(file="D:\python\ALARM IMAGES\Scenario3 Final.gif")
paras = PhotoImage(file="D:\python\ALARM IMAGES\Parameter Selection Final.gif")
parac = PhotoImage(file="D:\python\ALARM IMAGES\Parameter assumption.gif")
arrow = PhotoImage(file="D:\python\ALARM IMAGES\sarrow.gif")
arrow2= PhotoImage(file="D:\python\ALARM IMAGES\sarrow2.gif")
#photo=photo.subsample(w,h)
photo_label = Label(stroot,image=photo)
#photo_label.place(x=0, y=0, relwidth=1, relheight=1)
photo_label.grid(row=0,column=0,rowspan=w,columnspan=h,sticky=N+E+W+S)            
photo_label.image = photo
photo_label.columnconfigure(1, weight=1) 
photo_label.rowconfigure(1, weight=1)

#        Alarm_label = Label(stroot1,image=alarmI)
#        Alarm_label.grid(row=0,column=0,sticky=N+E+W+S)            
#        Alarm_label.image = alarmI

##        

global button1,i11,i12,i13,stroot1,colr

colr="White"
i11=StringVar(stroot,value="ok")
    
#stroot1=Frame(stroot)
#stroot1.configure(highlightbackground="Blue",background=colr)
#stroot1.grid(row=0,column=0,sticky=S)
#        separator = Frame(stroot1,height=2, bd=1, relief=SUNKEN)
#        separator.grid(columnspan=2000,sticky=N+S+E+W)
#photo_label = Label(stroot1,image=photo)
#photo_label.grid(row=1,column=0,rowspan=1000,columnspan=900,sticky=N+E+W+S)            
#photo_label.image = photo 
button1 = ttk.Button(stroot, text="Upload File",
                   command=upload,image=uploadI)



   # uploadI=uploadI.subsample(6000,600)
button1.image=uploadI
                    


button1.grid(row=1,column=1,columnspan=1,sticky=E+W,padx=50,pady=50)

arrow_label = Label(stroot,image=arrow)
arrow_label.grid(row=1,column=3)            
arrow_label.image = arrow


   

      

button3 = ttk.Button(stroot, text="Check for Missing Data-Point",
                    command=missingdata,image=missingD)
button3.image=missingD
button3.grid(row=1,column=5,columnspan=1,sticky=E+W,padx=50)

arrow_label = Label(stroot,image=arrow)
arrow_label.grid(row=1,column=7)            
arrow_label.image = arrow





button4 = ttk.Button(stroot,text="Acceptable Ranges",command=accpr,image=accprange)
button4.image=accprange
button4.grid(row=1,column=9,columnspan=1,sticky=E+W,padx=50)

arrow2_label = Label(stroot,image=arrow2)
arrow2_label.grid(row=2,column=5)            
arrow2_label.image = arrow2

buttonsc1 = ttk.Button(stroot, text="Scenario 1",command=dispy1,image=sc1)

buttonsc1.image=sc1
                    
buttonsc1.grid(row=3,column=1,columnspan=1,sticky=E+W,padx=50)
arrow2_label = Label(stroot,image=arrow2)
arrow2_label.grid(row=4,column=5)            
arrow2_label.image = arrow2

buttonsc2 = ttk.Button(stroot, text="Scenario 2",command=dispy2,image=sc2)
buttonsc2.image=sc2
                    
buttonsc2.grid(row=5,column=1,columnspan=1,sticky=E+W,padx=50)
arrow2_label = Label(stroot,image=arrow2)
arrow2_label.grid(row=6,column=5)            
arrow2_label.image = arrow2

buttonsc3 = ttk.Button(stroot, text="Scenario 3",command=dispy3,image=sc3)

buttonsc3.image=sc3
                    
buttonsc3.grid(row=7,column=1,columnspan=1,sticky=E+W,padx=50)



#        separator = Frame(stroot1,height=2, bd=1, relief=SUNKEN)
#        separator.configure(background=colr)
#        separator.grid(row=4,rowspan=300,columnspan=2000,sticky=N+S+E+W)
#photoI=photo.subsample(4,4)
#   
#labeln=ttk.Label(stroot,text="Step 1: Upload the input file",background=colr,compound = CENTER)
#labeln.grid(row=5,column=0,columnspan=25,sticky=E+W,)
#
#labeln=ttk.Label(stroot,text="Step 2: Run checks for missing data",background=colr,compound = CENTER)
#labeln.grid(row=6,column=0,columnspan=25,sticky=E+W)
#labeln=ttk.Label(stroot,text="Step 3: If you have missing values then download the Missing data file",background=colr,compound = LEFT)
#labeln.grid(row=7,column=0,columnspan=25,sticky=E+W)
#labeln=ttk.Label(stroot,text="Step 4: Check for acceptable ranges if errors exist, replace them all",background=colr,compound = CENTER)
#labeln.grid(row=8,column=0,columnspan=25,sticky=E+W)
#labeln=ttk.Label(stroot,text="Step 5: Enter assumptions",background=colr,compound = CENTER)
#labeln.grid(row=9,column=0,columnspan=25,sticky=E+W)
#stroot.lift()
#stroot.wm_attributes("-topmost", True)
#stroot.wm_attributes("-disabled", True)
stroot.wm_attributes("-transparentcolor", "Blue")
stroot.attributes("-alpha", 1)
stroot.grid()
stroot.mainloop()

    
                            
            


#if __name__ == "__main__":
#    app = SampleApp()
#    photo = PhotoImage(file="D:\python\ALARM IMAGES\wALL.gif")
#    photo_label = Label(app,image=photo)
#    photo_label.grid(row=1,column=0,rowspan=1000,columnspan=1000,sticky=W)            
#    photo_label.image = photo 
#    app.configure(background="White")
#    app.title("Crisil Alarm Tool")
#    global i11,i12,i13,colr
#    
#    
#    #app.filename=filedialog.askopenfilename(filetypes=(("howCode files","*.hc"),("All files","*")))
#    app.geometry('1200x800')    
#    app.mainloop()

