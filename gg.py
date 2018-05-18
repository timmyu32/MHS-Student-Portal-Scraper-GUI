from individual_class_data import alternate as alter
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style
from matplotlib import pyplot

import tkinter as tk
from tkinter import ttk

from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from functools import reduce as reducer
from datetime import date as date

from PIL import Image, ImageTk

import time

import threading 
from queue import Queue


Largest_Font = ("Times New Roman", "16")
Large_Font = ("Times New Roman", "12")
smaller_font = ("Times New Roman", "9")
smallest_font = ("Times New Roman", "7")
style.use("ggplot")

global a
global f
global g
global zed
global una
global bary
una = Figure(figsize = (10,5), dpi=100)
f = Figure(figsize = (10,5), dpi=100)
g = Figure(figsize = (5,5), dpi=100)
zed = Figure(figsize= (10,5), dpi=100)
bary = Figure(figsize= (5,5), dpi=100)
unatated = una.add_subplot(111)
a = f.add_subplot(111)
baro = bary.add_subplot(111)


class GradeGetterApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="gradealert2.ico")
        tk.Tk.wm_title(self, "Tim Uzoegbu's Grade Graphers")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand="true")
        container.grid_rowconfigure(0, weight= 1)
        container.grid_columnconfigure(0, weight= 1)

        self.frames = {}
        
        for F in (StartPage, PageOne, PageTwo, Homework, Login, AdminPage, DisplayInDepth1, ClassOne, ClassTwo, ClassThree, ClassFour, ClassFive, ClassSix, ClassSeven, UnannotatedGraph, BarGraph, Average, DisplayInDepth2,  DisplayInDepth3):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.configure(background= "#95c8f4")

        self.show_frame(AdminPage)

    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()

class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text= "Enter your name, then click Verifiy and NEXT.", bg="#95c8f4", font = Largest_Font)
        label1.place(x=400, y= 200)
        self.enter = tk.Entry(self, show='*')
        self.enter.place(x=400, y=250)
        button1 = ttk.Button(self, text="Verify", command= lambda: self.go_login())
        button2 = ttk.Button(self, text= 'NEXT', command=  lambda: controller.show_frame(Login))
        button1.place(x=570, y=250)
        button2.place(x=690, y=250)

    def go_login(self):
        a = self.enter.get()
        global tim
        global timnoget
        if a == "gui":
            tim = True
            timnoget = False
            tk.Label(self, text= 'Welcome Back Tim!', font= Largest_Font, bg= '#95c8f4').place(x=600, y=310)
        elif a == "gui/noget":
            timnoget = True
            tk.Label(self, text= 'Welcome Back Tim!', font= Largest_Font, bg= '#95c8f4').place(x=600, y=310)
            tim = True
        else:
            tim = False
            tk.Label(self, text= 'Welcome {}!'.format(a), font= Largest_Font, bg= '#95c8f4').place(x=600, y=310)
           
class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text= "Please log into MHS Studnt Portal Account", bg="#95c8f4", font = Large_Font)
        label1.place(x=350, y= 200)
        label2 = tk.Label(self, text= "USERNAME", bg= "#95c8f4", font= smaller_font)
        label3 = tk.Label(self, text= "PASSWORD", bg= '#95c8f4', font= smaller_font)
        self.label4 = tk.Label(self, text= '', bg= '#95c8f4', font= smaller_font, fg= 'red')
        label2.place(x= 350, y=220)
        label3.place(x= 350, y= 240)
        self.u1 = ttk.Entry(self)
        self.p1 = ttk.Entry(self, show='*')
        self.u1.place(x=430, y=220)
        self.p1.place(x=430, y=240)
        button1 = ttk.Button(self, text="Login", command= lambda: self.go_login())
        button2 = ttk.Button(self, text ='Quit', command= quit)
        self.button3 = ttk.Button(self, text= 'NEXT', command= lambda:  controller.show_frame(StartPage))
        self.button3.configure(state= 'DISABLED')
        button1.place(x=460, y=270)
        button2.place(x=460, y=300)
        self.label4.place(x=350, y=370)
        self.label = tk.Label(self)
        checker = tk.Checkbutton(self, text= 'Do want to see HW due soon from GOOGLE CLASSROM', bg= '#95c8f4', command= lambda: self.show_pbox())
        checker.place(x=630, y=220)
        self.gc_p = ttk.Entry(self)


    def show_pbox(self):
        self.gc_p.place(x=630, y=240)
        self.label4.config(text= 'Enter GOOGLE CLASSROOM password')

        
    def go_login(self):
        goog = self.gc_p.get()
        if tim:
            def gc_get():
                
                if len(self.gc_p.get()) > 1:
                    gc_password = self.gc_p.get()
                    configurer = webdriver.ChromeOptions()
                    configurer.add_argument("-headless")
                    browser = webdriver.Chrome(chrome_options=configurer)
                    #browser = webdriver.Chrome()

                    browser.get("https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&followup=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
                    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@class='whsOnd zHQkBf']")))
                    gc_uname = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
                    next_btn = browser.find_element_by_xpath("//div[@id='identifierNext']")
                    email_adress = self.u1.get().lower() + '@student.medwayschools.org'
                    gc_uname.send_keys(email_adress)
                    next_btn.click()
                    time.sleep(2)
                    gc_password_box = browser.find_element_by_xpath("//input[@name='password']")
                    gc_password_box.send_keys(gc_password)
                    next_btn2 = browser.find_element_by_xpath("//span[@class='RveJvd snByac']")
                    next_btn2.click()
                    WebDriverWait(browser, 7).until(EC.visibility_of_element_located((By.XPATH, "//h2[@class='oBSRLe']")))


                    assignments_date = [x.text for x in browser.find_elements_by_xpath("//h2[@class='oBSRLe']")]
                    assignments = [x.text for x in browser.find_elements_by_xpath("//div[@class='hrUpcomingAssignmentGroup']")]

                    new_temp = open("temp9.txt", "w")
                    for items in assignments_date:
                        new_temp.write(items +',')
                    new_temp.close()
                    new_temp = open("temp9.txt", 'a')
                    new_temp.write("***")
                    for items in assignments:
                        new_temp.write(items+'^^')

                    browser.close()
                    new_temp.close()

                else:
                    new_temp = open('temp9.txt', 'w')
                    new_temp.write('')
                    new_temp.close()
                    

            def get_grades():
                u = self.u1.get()
                p = self.p1.get()
                goog = self.gc_p.get()
    
                options = webdriver.ChromeOptions()
                
                
                options.add_argument("-headless")
                driver = webdriver.Chrome(chrome_options=options)
                #driver = webdriver.Chrome()
                driver.get('https://www.mms669.org/MMSGB45/default.aspx?ReturnUrl=%2fMMSGB45%2fstudent')
                uname = driver.find_element_by_name('LoginControl1$txtUsername')
                password = driver.find_element_by_name('LoginControl1$txtPassword')
                login_btn = driver.find_element_by_name('LoginControl1$btnLogin')

                uname.clear()
                uname.send_keys(u)
                password.send_keys(p)
                login_btn.click()

                try:
                    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//span[@id='LoginControl1_lblErrMsg']")))
                    error_msg = driver.find_element_by_xpath("//span[@id='LoginControl1_lblErrMsg']").text
                    if type(error_msg) != None:
                        data_file = open("temp3.txt", 'w')
                        data_file.write(error_msg)
                        data_file.close()
                        self.label4.config(text=error_msg)
                           
                except:
                    data_file = open("temp3.txt", 'w')
                    data_file.write("No errors")
                    data_file.close()


                timeout = 10
                try:
                    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='rgMasterTable rgClipCells']")))
                except:
                    driver.close()

                class_names1 = driver.find_elements_by_xpath("//tr[@class='rgRow']")
                evens = [x.text for x in class_names1]

                class_names2 = driver.find_elements_by_xpath("//tr[@class='rgAltRow']")
                odds = [x.text for x in class_names2]

                all_class_codes = driver.find_elements_by_xpath("//td[@style='background-color:White;width:95px;']")
                class_codes = [x.text for x in all_class_codes]


                today = str(date.today())

                global denominator
                denominator = []
                global pie_chart_indicator
                pie_chart_indicator = []

                ids = []
                id_descriptors = []
                grdr = []
                grdr2 = []
                grdr3 = []


                numero = len(driver.find_elements_by_xpath("//td[@style= 'background-color:White;width:145px;']"))

                for links in driver.find_elements_by_xpath("//td[@style= 'background-color:White;width:145px;']"):
                    try:
                        links.click()
                        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id= 'ctl00_ContentPlaceHolder1_ReportViewer1ReportFrame']"))
                        class_identifiers = [x.text for x in driver.find_elements_by_xpath("//div[@class='HtmlTextBox2 s22-']")]
                        if len(class_identifiers) > 0:
                            ids.append(class_identifiers)
                            descriptor = [x.text.replace('\n',  ' ') for x in driver.find_elements_by_xpath("//div[@class='TextBox41 s28-']") ]
                            if len(descriptor) > 0:
                                id_descriptors.append([('***{}***').format( driver.find_element_by_xpath("//div[@class='TextBox5 s5-']").text[0:-2])])
                                id_descriptors.append(descriptor)
                                grdr.append([' '])
                                grdr2.append([' '])
                                grdr3.append([' '])
                                grd1 = [x.text for x in driver.find_elements_by_xpath("//div[@class='TextBox46 s29-']") ]
                                grd2 = [x.text for x in driver.find_elements_by_xpath("//div[@class='TextBox27 s28-']") ]
                                grd3 = [x.text.replace(",", "-") for x in driver.find_elements_by_xpath("//div[@class= 'TextBox42 s28-']") ] 
                            if len(grd1) > 0:
                                grdr.append(grd1)
                                grdr2.append(grd2)
                                grdr3.append(grd3)
                            driver.switch_to.parent_frame()
                            driver.find_elements_by_xpath("//a[@class= 'rmLink rmRootLink']")[4].click()
                            numero += -1
                        else:
                            driver.switch_to.parent_frame()
                            driver.find_elements_by_xpath("//a[@class= 'rmLink rmRootLink']")[4].click()
                            numero += -1

                    except:
                        links = driver.find_elements_by_xpath("//td[@style= 'background-color:White;width:145px;']")[numero]
                        links.click()
                        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id= 'ctl00_ContentPlaceHolder1_ReportViewer1ReportFrame']"))
                        class_identifiers = [x.text for x in driver.find_elements_by_xpath("//div[@class='HtmlTextBox2 s22-']")]
                        if len(class_identifiers) > 0:
                            ids.append(class_identifiers)
                            descriptor = [x.text.replace('\n',  ' ') for x in driver.find_elements_by_xpath("//div[@class='TextBox41 s28-']") ]
                            if len(descriptor) >0:
                                id_descriptors.append([('***{}***').format( driver.find_element_by_xpath("//div[@class='TextBox5 s5-']").text[0:-2])])
                                id_descriptors.append(descriptor)
                                grdr.append([' '])
                                grdr2.append([' '])
                                grdr3.append([' '])
                                grd1 = [x.text for x in driver.find_elements_by_xpath("//div[@class='TextBox46 s29-']") ]
                                grd2 = [x.text for x in driver.find_elements_by_xpath("//div[@class='TextBox27 s28-']") ]
                                grd3 = [x.text.replace(",", "-") for x in driver.find_elements_by_xpath("//div[@class= 'TextBox42 s28-']") ]
                            if len(grd1) > 0:
                                grdr.append(grd1)
                                grdr2.append(grd2)
                                grdr3.append(grd3)
                            driver.switch_to.parent_frame()
                            driver.find_elements_by_xpath("//a[@class= 'rmLink rmRootLink']")[4].click()
                            numero += -1

                        else:
                            driver.switch_to.parent_frame()
                            driver.find_elements_by_xpath("//a[@class= 'rmLink rmRootLink']")[4].click()
                            numero += -1

                driver.close()

                data_file = open("temp5.txt", 'w')
                for items in id_descriptors:
                    for item in items:
                        data_file.write(str(item)+',')
                data_file.close()
                data_file = open("temp6.txt", 'w')
                for items in grdr:
                    for item in items:
                        data_file.write(str(item)+',')
                data_file.close()
                data_file = open("temp7.txt", 'w')
                for items in grdr2:
                    for item in items:
                        data_file.write(str(item)+',')
                data_file.close()
                data_file = open("temp8.txt", 'w')
                for items in grdr3:
                    for item in items:
                        data_file.write(str(item)+',')
                data_file.close()            
                
                try:
                    class1_code = class_codes[0]
                    class1_name = evens[0].split(class1_code)[0]
                except:
                    pass
                try:
                    class2_code = class_codes[1]
                    class2_name = odds[0].split(class2_code)[0]
                except:
                    pass
                try:
                    class3_code = class_codes[2]
                    class3_name = evens[1].split(class3_code)[0]
                except:
                    pass
                try:
                    class4_code = class_codes[3]
                    class4_name = odds[1].split(class4_code)[0]
                except:
                    pass
                try:
                    class5_code = class_codes[4]
                    class5_name = evens[2].split(class5_code)[0]
                except:
                    pass
                try:
                    class6_code = class_codes[5]
                    class6_name = odds[2].split(class6_code)[0]
                except:
                    pass
                try:
                    class7_code = class_codes[6]
                    class7_name = evens[3].split(class7_code)[0]
                except:
                    pass
                try:
                    class8_code = class_codes[7]
                    class8_name = odds[3].split(class8_code)[0]
                except:
                    pass
                try:
                    class9_code = class_code[8]
                    class9_name = evens[4].split(class9_code)[0]
                except:
                    pass
                try:
                    class10_code = class_codes[9]
                    class10_name = odds[4].split(class10_code)[0]
                except:
                    pass

                

                try:
                    class1 = evens[0]
                    class1_g = class1.split(",")
                    class1_grade = float(class1_g[1].split(')')[0].split('(')[1]) 
                    denominator.append(class1_grade)
                    pie_chart_indicator.append(str(class1_name) + str(class1_grade))
                    if timnoget == False:
                        data_file = open("one.txt", "r")
                        last_grade = data_file.read().split(',')[-2].split('@')[0]
                        tempy1 = str(class1_grade) +'@'+today+','
                        
                        if tempy1 not in data_file.read():
                            try:
                                data_file.close()
                                if float(last_grade) != float(class1_grade):
                                    data_file = open("one.txt", "a")
                                    data_file.write(str(class1_grade) +'@'+today +',')
                            except:
                                print('writing has failed')
                        else:
                            print("Class {}'s grade of {} is already in one.txt".format(class1_name, class1_grade))
                        data_file.close() 
                    else:
                        print('Tim No get is false')   
                except:
                    class1_grade = None
                try:
                    class2 = odds[0]
                    class2_g = class2.split(",")
                    class2_grade = float(class2_g[1].split(')')[0].split('(')[1])
                    denominator.append(class2_grade)
                    pie_chart_indicator.append(str(class2_name) + str(class2_grade))
                    if timnoget == False:
                        data_file = open("two.txt", "r")
                        last_grade = data_file.read().split(',')[-2].split('@')[0]
                        tempy1 = str(class2_grade) +'@'+today+','
                        
                        if tempy1 not in data_file.read():
                            try:
                                data_file.close()
                                if float(last_grade) != float(class2_grade):
                                    data_file = open("two.txt", "a")
                                    data_file.write(str(class2_grade) +'@'+today +',')
                            except:
                                print('writing has failed')
                        else:
                            print("Class {}'s grade of {} is already in two.txt".format(class2_name, class2_grade))
                        data_file.close() 
                    else:
                        print('Tim No get is false')          
                except:
                    class2_grade = None
                try:
                    class3 = evens[1]
                    class3_g = class3.split(",")
                    class3_grade = float(class3_g[1].split(')')[0].split('(')[1])    
                    denominator.append(class3_grade) 
                    pie_chart_indicator.append(str(class3_name) + str(class3_grade))
                    if timnoget == False:
                        data_file = open("three.txt", "r")
                        last_grade = data_file.read().split(',')[-2].split('@')[0]
                        tempy1 = str(class3_grade) +'@'+today+','
                        
                        if tempy1 not in data_file.read():
                            try:
                                data_file.close()
                                if float(last_grade) != float(class3_grade):
                                    data_file = open("three.txt", "a")
                                    data_file.write(str(class3_grade) +'@'+today +',')
                            except:
                                print('writing has failed')
                        else:
                            print("Class {}'s grade of {} is already in three.txt".format(class3_name, class3_grade))
                        data_file.close() 
                    else:
                        print('Tim No get is false')  
                except:
                    class3_grade = None
                try:
                    class4 = odds[1]
                    class4_g = class4.split(",")
                    class4_grade = float(class4_g[1].split(')')[0].split('(')[1])    
                    denominator.append(class4_grade) 
                    pie_chart_indicator.append(str(class4_name) + str(class4_grade))
                    if timnoget == False:
                        data_file = open("four.txt", "r")
                        last_grade = data_file.read().split(',')[-2].split('@')[0]
                        tempy1 = str(class4_grade) +'@'+today+','
                        
                        if tempy1 not in data_file.read():
                            try:
                                data_file.close()
                                if float(last_grade) != float(class4_grade):
                                    data_file = open("four.txt", "a")
                                    data_file.write(str(class4_grade) +'@'+today +',')
                            except:
                                print('writing has failed')
                        else:
                            print("Class {}'s grade of {} is already in four.txt".format(class4_name, class4_grade))
                        data_file.close() 
                    else:
                        print('Tim No get is false')  
                except:
                    class4_grade = None
                try:
                    class5 = evens[2]
                    class5_g = class5.split(",")
                    class5_grade = float(class5_g[1].split(')')[0].split('(')[1])    
                    denominator.append(class5_grade)
                    pie_chart_indicator.append(str(class5_name) + str(class5_grade))  
                    if timnoget == False:
                        data_file = open("five.txt", "r")
                        last_grade = data_file.read().split(',')[-2].split('@')[0]
                        tempy1 = str(class5_grade) +'@'+today+','
                        
                        if tempy1 not in data_file.read():
                            try:
                                data_file.close()
                                if float(last_grade) != float(class5_grade):
                                    data_file = open("five.txt", "a")
                                    data_file.write(str(class5_grade) +'@'+today +',')
                            except:
                                print('writing has failed')
                        else:
                            print("Class {}'s grade of {} is already in five.txt".format(class5_name, class5_grade))
                        data_file.close() 
                    else:
                        print('Tim No get is false') 
                except:
                    class5_grade = None
                try:
                    class6 = odds[2]
                    class6_g = class6.split(",")
                    class6_grade = float(class6_g[1].split(')')[0].split('(')[1])    
                    denominator.append(class6_grade) 
                    pie_chart_indicator.append(str(class6_name) + str(class6_grade)) 
                    if timnoget == False:
                        data_file = open("six.txt", "r")
                        last_grade = data_file.read().split(',')[-2].split('@')[0]
                        tempy1 = str(class6_grade) +'@'+today+','
                        
                        if tempy1 not in data_file.read():
                            try:
                                data_file.close()
                                if float(last_grade) != float(class6_grade):
                                    data_file = open("six.txt", "a")
                                    data_file.write(str(class6_grade) +'@'+today +',')
                            except:
                                print('writing has failed')
                        else:
                            print("Class {}'s grade of {} is already in six.txt".format(class6_name, class6_grade))
                        data_file.close() 
                    else:
                        print('Tim No get is false')
                except:
                    class6_grade = None
                try:
                    class7 = evens[3]
                    class7_g = class7.split(",")
                    class7_grade = float(class7_g[1].split(')')[0].split('(')[1])    
                    denominator.append(class7_grade)
                    pie_chart_indicator.append(str(class7_name) + str(class7_grade))
                    if timnoget == False:
                        data_file = open("seven.txt", "r")
                        last_grade = data_file.read().split(',')[-2].split('@')[0]
                        tempy1 = str(class7_grade) +'@'+today+','
                        
                        if tempy1 not in data_file.read():
                            try:
                                data_file.close()
                                if float(last_grade) != float(class7_grade):
                                    data_file = open("seven.txt", "a")
                                    data_file.write(str(class7_grade) +'@'+today +',')
                            except:
                                print('writing has failed')
                        else:
                            print("Class {}'s grade of {} is already in seven.txt".format(class7_name, class7_grade))
                        data_file.close() 
                    else:
                        print('Tim No get is false') 
                except:
                    class7_grade = None
                try:
                    class8 = odds[3]
                    class8_g = class8.split(",")
                    class8_grade = float(class8_g[1].split(')')[0].split('(')[1])   
                    denominator.append(class8_grade)
                    pie_chart_indicator.append(str(class8_name) + str(class8_grade)) 
                except:
                    class8_grade = None
                try:
                    class9 = evens[4]
                    class9_g = class9.split(",")
                    class9_grade = float(class9_g[1].split(')')[0].split('(')[1])    
                    denominator.append(class9_grade) 
                    pie_chart_indicator.append(class9_name) 
                except:
                    class9_grade = None
                try:
                    class10 = odds[4]
                    class10_g = class10.split(",")
                    class10_grade = float(class10_g[1].split(')')[0].split('(')[1])  
                    denominator.append(class10_grade)  
                except:
                    class10_grade = None


                try:        
                    d = len(denominator)
                    n = reducer(lambda x,y: x+y, denominator)
                except:
                    pass

                try:
                    average = round(n/d, 2)
                except:
                    pass

            


                try:
                    data_1 = open("one.txt", "r")
                    data11 = data_1.read().split(',')
                    data_1.close()

                    data11y = []
                    data11x = []

                    for items in data11:
                        y_valuer = items.split('@')[0]
                        if len(y_valuer) > 1:
                            y_value = float(y_valuer)
                            data11y.append(y_value)
                        x_valuer = items.split('@')[-1]
                        if len(x_valuer) > 1:
                            data11x.append(x_valuer)
                except:
                    pass

                try:
                    data_2 = open("two.txt", "r")
                    data22 = data_2.read().split(',')
                    data_2.close()

                    data22y = []
                    data22x = []

                    for items in data22:
                        y_valuer = items.split('@')[0]
                        if len(y_valuer) > 1:
                            y_value = float(y_valuer)
                            data22y.append(y_value)
                        x_valuer = items.split('@')[-1]
                        if len(x_valuer) > 1:
                            data22x.append(x_valuer)
                except:
                    pass

                try:
                    data_3 = open("three.txt", "r")
                    data33 = data_3.read().split(',')
                    data_3.close()

                    data33y = []
                    data33x = []

                    for items in data33:
                        y_valuer = items.split('@')[0]
                        if len(y_valuer) > 1:
                            y_value = float(y_valuer)
                            data33y.append(y_value)
                        x_valuer = items.split('@')[-1]
                        if len(x_valuer) > 1:
                            data33x.append(x_valuer)
                except:
                    pass

                try:
                    data_4 = open("four.txt", "r")
                    data44 = data_4.read().split(',')
                    data_4.close()

                    data44y = []
                    data44x = []

                    for items in data44:
                        y_valuer = items.split('@')[0]
                        if len(y_valuer) > 1:
                            y_value = float(y_valuer)
                            data44y.append(y_value)
                        x_valuer = items.split('@')[-1]
                        if len(x_valuer) > 1:
                            data44x.append(x_valuer)
                except:
                    pass
                try:    
                    data_5 = open("five.txt", "r")
                    data55 = data_5.read().split(',')
                    data_5.close()

                    data55y = []
                    data55x = []

                    for items in data55:
                        y_valuer = items.split('@')[0]
                        if len(y_valuer) > 1:
                            y_value = float(y_valuer)
                            data55y.append(y_value)
                        x_valuer = items.split('@')[-1]
                        if len(x_valuer) > 1:
                            data55x.append(x_valuer)
                    
                except:
                    pass

                try:  
                    data_6 = open("six.txt", "r")
                    data66 = data_6.read().split(',')
                    data_6.close()

                    data66y = []
                    data66x = []

                    for items in data66:
                        y_valuer = items.split('@')[0]
                        if len(y_valuer) > 1:
                            y_value = float(y_valuer)
                            data66y.append(y_value)
                        x_valuer = items.split('@')[-1]
                        if len(x_valuer) > 1:
                            data66x.append(x_valuer)
                except:
                    pass

                try:
                    data_7 = open("seven.txt", "r")
                    data77 = data_7.read().split(',')
                    data_7.close()

                    data77y = []
                    data77x = []

                    for items in data77:
                        y_valuer = items.split('@')[0]
                        if len(y_valuer) > 1:
                            y_value = float(y_valuer)
                            data77y.append(y_value)
                        x_valuer = items.split('@')[-1]
                        if len(x_valuer) > 1:
                            data77x.append(x_valuer)
                except:
                    pass

                if timnoget == False:
                    data_file = open("avg.txt", "r")
                    tempy1 = str(average) +'@'+today+','
                    
                    if tempy1 not in data_file.read():
                        try:
                            data_file.close()
                            data_file = open("avg.txt", "a")
                            data_file.write(str(average) +'@'+today +',')     
                        except:
                            print('writing has failed')
                    else:
                        print(" {} is already in avg.txt".format(average))
                    data_file.close() 
                else:
                    print('Tim No get is false')
                
                avg_data = open("avg.txt", "r")
                avg_data1 = avg_data.read().split(',')
                avg_data1y = []
                global avg_data1x
                avg_data1x = []

                for items in avg_data1:
                    y_valuer = items.split('@')[0]
                    if len(y_valuer) > 1:
                        y_value = float(y_valuer)
                        avg_data1y.append(y_value)
                    x_valuer = items.split('@')[-1]
                    if len(x_valuer) > 1:
                        avg_data1x.append(x_valuer)
                a.set_title("GRADES Graph\nCurrent Avg= "+str(average))

                a.plot(avg_data1x, avg_data1y, label= 'Average', ls= '--')
                unatated.plot(avg_data1x, avg_data1y, label= 'Average', ls= '--')
                a.plot(data11x, data11y, "#ED1F11", label= class1_name, data= class1_name, marker= '.')
                unatated.plot(data11x, data11y, "#ED1F11", label= class1_name, data= class1_name, marker= '.')
                a.plot(data22x, data22y, "#010101", label= class2_name, data= class2_name, marker= '.')
                unatated.plot(data22x, data22y, "#010101", label= class2_name, data= class2_name, marker= '.')
                a.plot(data33x, data33y, "#25bcb5", label= class3_name, data= class3_name, marker= '.')
                unatated.plot(data33x, data33y, "#25bcb5", label= class3_name, data= class3_name, marker= '.')
                a.plot(data44x, data44y, "#29A223", label= class4_name, data= class4_name, marker= '.')
                unatated.plot(data44x, data44y, "#29A223", label= class4_name, data= class4_name, marker= '.')
                a.plot(data55x, data55y, "#2E3ACA", label= class5_name, data= class5_name, marker= '.')
                unatated.plot(data55x, data55y, "#2E3ACA", label= class5_name, data= class5_name, marker= '.')
                a.plot(data66x, data66y, "#FF8CEC", label= class6_name, data= class6_name, marker= '.')
                unatated.plot(data66x, data66y, "#FF8CEC", label= class6_name, data= class6_name, marker= '.')
                a.plot(data77x, data77y, "#F5891C", label= class7_name, data= class7_name, marker= '.')
                unatated.plot(data77x, data77y, "#F5891C", label= class7_name, data= class7_name, marker= '.')
                a.legend()
                unatated.legend()
                try:
                    baro.bar(x=class1_name, height= class1_grade, color= "#ED1F11", lw = 0.35)
                except:
                    print("Class {} is not avaliable for bar graph".format(class1_name))
                try:
                    baro.bar(x=class2_name, height= class2_grade, color= "#010101", lw = 0.35)
                except:
                    print("Class {} is not avaliable for bar graph".format(class2_name))
                try:
                    baro.bar(x=class3_name, height= class3_grade, color= "#25bcb5", lw = 0.35)
                except:
                    print("Class {} is not avaliable for bar graph".format(class3_name))
                try:
                    baro.bar(x=class4_name, height= class4_grade, color= "#29A223", lw = 0.35)
                except:
                    print("Class {} is not avaliable for bar graph".format(class4_name))
                try:    
                    baro.bar(x=class5_name, height= class5_grade, color= "#2E3ACA", lw = 0.35)
                except:
                    print("Class {} is not avaliable for bar graph".format(class5_name))
                try:
                    baro.bar(x=class6_name, height= class6_grade, color= "#FF8CEC", lw = 0.35)
                except:
                    print("Class {} is not avaliable for bar graph".format(class6_name))
                try:
                    baro.bar(x=class7_name, height= class7_grade, color = "#F5891C")
                except:
                    print("Class {} is not avaliable for bar graph".format(class7_name))
                try:
                    baro.bar(x='Average', height= average, lw = 0.35)
                except:
                    print("Class {} is not avaliable for bar graph".format("average"))
            

                #for xy in zip(avg_data1x, avg_data1y):
                #    a.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
                for xy in zip(data11x, data11y):
                    a.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
                for xy in zip(data22x, data22y):
                    a.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
                for xy in zip(data33x, data33y):
                    a.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
                for xy in zip(data44x, data44y):
                    a.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
                for xy in zip(data55x, data55y):
                    a.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
                for xy in zip(data66x, data66y):
                    a.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
                for xy in zip(data77x, data77y):
                    a.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
                temporal_lobe = open('temp3.txt', 'r')
                occipital = temporal_lobe.read()
                if occipital.startswith('N'):
                    self.label4.config(text='Click NEXT', fg= 'black' )
                    self.button3.place(x=460, y=330)
                else:
                    self.label4.config(text='An ERROR has occured, try correcting your user and password.')

                
            threading.Thread(target = get_grades).start()
            threading.Thread(target = gc_get).start() 

        else:
            nono = True
            timestamps = ['Quarter 1', 'Quarter 2', 'Quarter 3', 'Current']
            u = self.u1.get()
            p = self.p1.get()
            goog = self.gc_p.get()
            
            
        
            if alter(u,p,goog):
                self.label4.config(text='Click NEXT', fg= 'black' )
                self.button3.place(x=460, y=330)
            else:
                data_file = open("temp3.txt", 'r')
                msg = data_file.read()
                data_file.close()
                self.label4.config(text=msg, fg= 'black' )

                
                


                data_file = open("temp.txt", 'r')
                temps = data_file.read()
                data_file.close()
                namers = temps.split('***')[0].split(',')
                n1 = namers[0]
                n2 = namers[1]
                n3 = namers[2]
                n4 = namers[3]
                n5 = namers[4]
                n6 = namers[5]
                n7 = namers[6]
                graders = temps.split('***')[1].split('/')
                g1 = [x.split(",") for x in graders[0]]

                try:
                    a111=int(graders[0].split(',')[0][::1])
                except:
                    a111=0
                try:
                    b111=int(graders[0].split(',')[1][::1])
                except:
                    b=0
                try:
                    c=int(graders[0].split(',')[2][::1])
                except:
                    c=0
                try:
                    d=int(graders[1].split(',')[0][::1])
                except:
                    d=0
                try:
                    e= int(graders[1].split(',')[1][::1])
                except:
                    e=0
                try:
                    f111= int(graders[1].split(',')[2][::1])
                except:
                    f111=0
                try:
                    g111=int(graders[2].split(',')[0][::1])
                except:
                    g111=0
                try:
                    h=int(graders[2].split(',')[1][::1])
                except:
                    h=0
                try:
                    i=int(graders[2].split(',')[2][::1])
                except:
                    i=0
                try:
                    j=int(graders[3].split(',')[0][::1])
                except:
                    j=0
                try:
                    k=int(graders[3].split(',')[1][::1])
                except:
                    k=0
                try:
                    l=int(graders[3].split(',')[2][::1]) 
                except:
                    l=0
                try:
                    m= int(graders[4].split(',')[0][::1])
                except:
                    m=0
                try:
                    n=int(graders[4].split(',')[1][::1])
                except:
                    n=0
                try:
                    o=int(graders[4].split(',')[2][::1])
                except:
                    o=0
                try:
                    p=int(graders[5].split(',')[0][::1])
                except:
                    p=0
                try:
                    q=int(graders[5].split(',')[1][::1])
                except:
                    q=0
                try:
                    r=int(graders[5].split(',')[2][::1])
                except:
                    r=0
                try:
                    s=int(graders[6].split(',')[0][::1])
                except:
                    s=0
                try:
                    t=int(graders[6].split(',')[1][::1])
                except:
                    t=0
                try:
                    u=int(graders[6].split(',')[2][::1])
                except:
                    u=0
                
                data_file = open("temp2.txt", 'r')
                cgz = data_file.read().split('&')
                data_file.close()

                try:
                    c1g = int(cgz[0])
                except:
                    c1g = float(cgz[0])
                try:
                    c2g = int(cgz[1])
                except:
                    c2g = float(cgz[1])
                try:
                    c3g = int(cgz[2])
                except:
                    c3g = float(cgz[2])
                try:
                    c4g = int(cgz[3])
                except:
                    c4g = float(cgz[3])
                try:
                    c5g = int(cgz[4])
                except:
                    c5g = float(cgz[4])
                try:
                    c6g = int(cgz[5])
                except:
                    c6g = float(cgz[5])
                try:
                    c7g = int(cgz[6])
                except:
                    c7g = float(cgz[6])


                g1 = [ a111,b111 ,c, c1g  ]  

                g2 = [ d,d,f111, c2g ]

                g3 = [g111,h ,i, c3g] 

                g4 = [ j,k,l, c4g ]  

                g5 = [m,n ,o, c5g  ]  

                g6 = [ p,q ,r,c6g  ]  

                g7 = [ s,t ,u ,c7g ]  

                        

                a.plot(timestamps, g1, "#ED1F11", label= n1, data=c1g, marker= '.')
                for xy in zip(timestamps, g1):
                    a.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
                a.plot(timestamps, g2, "#010101", label= n2, data= c2g, marker= '.')
                for xy in zip(timestamps, g2):
                    a.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
                a.plot(timestamps, g3, "#25bcb5", label= n3, data= c3g, marker= '.')
                for xy in zip(timestamps, g3):
                    a.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
                a.plot(timestamps, g4, "#29A223", label= n4, data= c4g, marker= '.')
                for xy in zip(timestamps, g4):
                    a.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
                a.plot(timestamps, g5, "#2E3ACA", label= n5, data= c5g, marker= '.')
                for xy in zip(timestamps, g5):
                    a.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
                a.plot(timestamps, g6, "#FF8CEC", label= n6, data= c6g, marker= '.')
                for xy in zip(timestamps, g6):
                    a.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
                a.plot(timestamps, g7, "#F5891C", label= n7, data= c7g, marker= '.')
                for xy in zip(timestamps, g7):
                    a.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
                a.legend()
                studentName = open("temp4.txt", "r")
                studentName1 = studentName.read()
                studentName.close()
                a.set_title('Graph of '+studentName1)
            
        
        
            
                data_file.close()

class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text= 'Welcome to the MHS Live Student Portal graph for data visualization created by Tim Uzoegbu.', font= Largest_Font, background= "#95c8f4")
        label1.grid(row=1, column=1, columnspan= 3, sticky= tk.W)
        label2 = tk.Label(self, text= 'This program can be used to plot the course of your courses over a month, semester, or even a year! Lets get started...', font= smaller_font, background= "#95c8f4")
        label2.grid(row= 2, column = 1, columnspan= 3, sticky= tk.W)
        button1 = ttk.Button(self, text= 'Go to Student Portal Class Data Graph', command= lambda: controller.show_frame(PageOne))
        button1.grid(row=3, column= 2, sticky= tk.W)
        tk.Label(self, bg= '#95c8f4',text= '(Program graphs up to 7 classes)').grid(row=3, column= 3, sticky= tk.W)
        button2 = ttk.Button(self, text= 'Go to Class Data Pie Chart', command= lambda: controller.show_frame(PageTwo))
        button5 = ttk.Button(self, text= 'Bar Graph Page', command= lambda: controller.show_frame(BarGraph))
        button2.grid(row= 5, column= 2, sticky= tk.W)
        button5.grid(row= 5, column= 3, sticky= tk.W)
        button3 = ttk.Button(self, text= "Quit App", command= quit,)
        button4 = ttk.Button(self, text= 'See Avaliable Class Data', command= lambda: controller.show_frame(DisplayInDepth1))
        button4.grid(row= 4, column= 2, columnspan= 2, sticky= tk.W)
        button3.grid(row= 8, column= 2, sticky= tk.W)
        self.showImg()
        button7  = ttk.Button(self, text= 'Go to Student Portal Web Page', command= lambda: self.mms())
        button7.grid(row= 6, column= 2, columnspan= 2, sticky= tk.W)
        label = ttk.Button(self, text= 'HOMEWORK', command= lambda: controller.show_frame(Homework))
        label.grid(row=7, column=2, columnspan= 2, sticky= tk.W)



    def showImg(self):
            
        load = Image.open("home_img.jpg")
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image= render)
        img.image = render
        img.grid(row=3, column= 1, rowspan= 6)

    def mms(self):
        options = webdriver.ChromeOptions()
        options.add_argument("-headless")
        #driver = webdriver.Chrome(chrome_options=options)
        driver = webdriver.Chrome()
        driver.get('https://www.mms669.org/MMSGB45/default.aspx?ReturnUrl=%2fMMSGB45%2fstudent')

class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  

        label1 = ttk.Label(self, text= "Annotated Graph Page", font= Large_Font, background= "#95c8f4")
        label1.pack()
        button1 = ttk.Button(self, text= 'Go back to HOME PAGE', command= lambda: controller.show_frame(StartPage))
        button1.pack()
        button3 = ttk.Button(self, text= 'Update Graph', command= lambda: self.refresh())
        button3.pack()
        self.button4 = ttk.Button(self, text = " ", command= lambda: controller.show_frame(ClassOne))
        self.button5 = ttk.Button(self, text = " ", command= lambda: controller.show_frame(ClassTwo))
        self.button6 = ttk.Button(self, text = " ", command= lambda: controller.show_frame(ClassThree))
        self.button7 = ttk.Button(self, text = " ", command= lambda: controller.show_frame(ClassFour))
        self.button8 = ttk.Button(self, text = " ", command= lambda: controller.show_frame(ClassFive))
        self.button9 = ttk.Button(self, text = " ", command= lambda: controller.show_frame(ClassSix))
        self.button10 = ttk.Button(self, text = " ", command= lambda: controller.show_frame(ClassSeven))
        self.button11 = ttk.Button(self, text= ' ',command= lambda: controller.show_frame(UnannotatedGraph) )
        self.button12 = ttk.Button(self, text= 'Go to Bar Graph Page', command= lambda: controller.show_frame(BarGraph))
        self.e = ttk.Entry(self)
        self.button13 = ttk.Button(self, text= 'Plot', command= lambda: self.refer())
        self.button14 = ttk.Button(self, text= 'AVERAGE', command= lambda: controller.show_frame(Average))
        self.label1 = tk.Label(self, text= 'Plot a referance line', font= smaller_font, bg ='#95c8f4' )
        
    def refer(self):
        
        
        y = self.e.get()
        if y == int or y== float:
            a.plot(avg_data1x, y)
        else:
            a.plot(0, 0)
        
        canvas = FigureCanvasTkAgg(f, self)
        
        canvas.draw()




    def refresh(self):
        if tim:
            self.button4.config(text= '1')
            self.button4.place(x=0,y=0)
            self.button5.config(text='2')
            self.button5.place(x=60,y=0)
            self.button6.config(text='3')
            self.button6.place(x=120,y=0)
            self.button7.config(text='4')
            self.button7.place(x=180,y=0)
            self.button8.config(text='5')
            self.button8.place(x=240,y=0)
            self.button9.config(text='6')
            self.button9.place(x=300,y=0)
            self.button10.config(text='7')
            self.button10.place(x=360,y=0)
            self.button14.place(x=440, y=0)
            self.button11.place(x=180,y=50)
            self.button11.config(text='Show Unannotated Graph')
            self.button12.place(x=390, y=50)
            #self.e.place(x=1000,y=30)
            #self.label1.place(x=1000,y=0)
            #self.button13.place(x=1150, y= 30)

            
        
     
        canvas = FigureCanvasTkAgg(f, self)
        
        canvas.draw()
        canvas.get_tk_widget().pack(side= tk.TOP, fill= tk.BOTH, expand= True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side= tk.TOP, fill= tk.BOTH, expand= True)

class BarGraph(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  

        button1 = ttk.Button(self, text= 'Go back to graph', command= lambda: controller.show_frame(PageOne))
        button2 = ttk.Button(self,  text= 'Update Graph',  command= lambda: self.refresh2())
        button1.pack()
        button2.pack()
    
    def refresh2(self):
        canvas = FigureCanvasTkAgg(bary, self)
        
        canvas.draw()
        canvas.get_tk_widget().pack(side= tk.TOP, fill= tk.BOTH, expand= True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side= tk.TOP, fill= tk.BOTH, expand= True)
                  
class ClassOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  

        button1 = ttk.Button(self, text= 'Go back to graph', command= lambda: controller.show_frame(PageOne))
        button2 = ttk.Button(self,  text= 'Update Graph',  command= lambda: self.refresh2())
        button1.pack()
        button2.pack()

    def refresh2(self):
        try:    
            data_1 = open("one.txt", "r")
            data11 = data_1.read().split(',')
            data_1.close()

            data11y = []
            data11x = []

            for items in data11:
                y_valuer = items.split('@')[0]
                if len(y_valuer) > 1:
                    y_value = float(y_valuer)
                    data11y.append(y_value)
                x_valuer = items.split('@')[-1]
                if len(x_valuer) > 1:
                    data11x.append(x_valuer)         
        except:
            pass   

        zed1 = zed.add_subplot(111)
        zed1.plot(data11x,data11y,"#ED1F11", marker= '.' )

        for xy in zip(data11x, data11y):
                    zed1.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')

        canvas = FigureCanvasTkAgg(zed, self)
        
        canvas.draw()
        canvas.get_tk_widget().pack(side= tk.TOP, fill= tk.BOTH, expand= True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side= tk.TOP, fill= tk.BOTH, expand= True)

class ClassTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  

        button1 = ttk.Button(self, text= 'Go back to graph', command= lambda: controller.show_frame(PageOne))
        button2 = ttk.Button(self,  text= 'Update Graph',  command= lambda: self.refresh2())
        button1.pack()
        button2.pack()

    def refresh2(self):
        try:    
            data_2 = open("two.txt", "r")
            data22 = data_2.read().split(',')
            data_2.close()

            data22y = []
            data22x = []

            for items in data22:
                y_valuer = items.split('@')[0]
                if len(y_valuer) > 1:
                    y_value = float(y_valuer)
                    data22y.append(y_value)
                x_valuer = items.split('@')[-1]
                if len(x_valuer) > 1:
                    data22x.append(x_valuer)         
        except:
            pass
        zed22 = Figure(figsize= (10,5), dpi=100)

        zed2 = zed22.add_subplot(111)
        zed2.plot(data22x,data22y,"#010101", marker='.' )

        for xy in zip(data22x, data22y):
                    zed2.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')

        canvas = FigureCanvasTkAgg(zed22, self)
        
        canvas.draw()
        canvas.get_tk_widget().pack(side= tk.TOP, fill= tk.BOTH, expand= True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side= tk.TOP, fill= tk.BOTH, expand= True)

class ClassThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  

        button1 = ttk.Button(self, text= 'Go back to graph', command= lambda: controller.show_frame(PageOne))
        button2 = ttk.Button(self,  text= 'Update Graph',  command= lambda: self.refresh2())
        button1.pack()
        button2.pack()

    def refresh2(self):
        try:    
            data_3 = open("three.txt", "r")
            data33 = data_3.read().split(',')
            data_3.close()

            data33y = []
            data33x = []

            for items in data33:
                y_valuer = items.split('@')[0]
                if len(y_valuer) > 1:
                    y_value = float(y_valuer)
                    data33y.append(y_value)
                x_valuer = items.split('@')[-1]
                if len(x_valuer) > 1:
                    data33x.append(x_valuer)         
        except:
            pass   
        zed33 = Figure(figsize= (10,5), dpi=100)


        zed3 = zed33.add_subplot(111)
        zed3.plot(data33x,data33y, "#25bcb5", marker='.' )

        for xy in zip(data33x, data33y):
                    zed3.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')

        canvas = FigureCanvasTkAgg(zed33, self)
        
        canvas.draw()
        canvas.get_tk_widget().pack(side= tk.TOP, fill= tk.BOTH, expand= True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side= tk.TOP, fill= tk.BOTH, expand= True)

class ClassFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  

        button1 = ttk.Button(self, text= 'Go back to graph', command= lambda: controller.show_frame(PageOne))
        button2 = ttk.Button(self,  text= 'Update Graph',  command= lambda: self.refresh2())
        button1.pack()
        button2.pack()

    def refresh2(self):
        try:    
            data_4 = open("four.txt", "r")
            data44 = data_4.read().split(',')
            data_4.close()

            data44y = []
            data44x = []

            for items in data44:
                y_valuer = items.split('@')[0]
                if len(y_valuer) > 1:
                    y_value = float(y_valuer)
                    data44y.append(y_value)
                x_valuer = items.split('@')[-1]
                if len(x_valuer) > 1:
                    data44x.append(x_valuer)         
        except:
            pass   
        zed44 = Figure(figsize= (10,5), dpi=100)


        zed4 = zed44.add_subplot(111)
        zed4.plot(data44x,data44y,"#29A223", marker='.')

        for xy in zip(data44x, data44y):
                    zed4.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')

        canvas = FigureCanvasTkAgg(zed44, self)
        
        canvas.draw()
        canvas.get_tk_widget().pack(side= tk.TOP, fill= tk.BOTH, expand= True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side= tk.TOP, fill= tk.BOTH, expand= True)

class ClassFive(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  

        button1 = ttk.Button(self, text= 'Go back to graph', command= lambda: controller.show_frame(PageOne))
        button2 = ttk.Button(self,  text= 'Update Graph',  command= lambda: self.refresh2())
        button1.pack()
        button2.pack()

    def refresh2(self):
        try:    
            data_5 = open("five.txt", "r")
            data55 = data_5.read().split(',')
            data_5.close()

            data55y = []
            data55x = []

            for items in data55:
                y_valuer = items.split('@')[0]
                if len(y_valuer) > 1:
                    y_value = float(y_valuer)
                    data55y.append(y_value)
                x_valuer = items.split('@')[-1]
                if len(x_valuer) > 1:
                    data55x.append(x_valuer)         
        except:
            pass   
        zed55 = Figure(figsize= (10,5), dpi=100)

        zed5 = zed55.add_subplot(111)
        zed5.plot(data55x,data55y,"#2E3ACA", marker='.')

        for xy in zip(data55x, data55y):
                    zed5.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')

        canvas = FigureCanvasTkAgg(zed55, self)
        
        canvas.draw()
        canvas.get_tk_widget().pack(side= tk.TOP, fill= tk.BOTH, expand= True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side= tk.TOP, fill= tk.BOTH, expand= True)

class ClassSix(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  

        button1 = ttk.Button(self, text= 'Go back to graph', command= lambda: controller.show_frame(PageOne))
        button2 = ttk.Button(self,  text= 'Update Graph',  command= lambda: self.refresh2())
        button1.pack()
        button2.pack()

    def refresh2(self):
        try:    
            data_6 = open("six.txt", "r")
            data66 = data_6.read().split(',')
            data_6.close()

            data66y = []
            data66x = []

            for items in data66:
                y_valuer = items.split('@')[0]
                if len(y_valuer) > 1:
                    y_value = float(y_valuer)
                    data66y.append(y_value)
                x_valuer = items.split('@')[-1]
                if len(x_valuer) > 1:
                    data66x.append(x_valuer)         
        except:
            pass   
        zed66 = Figure(figsize= (10,5), dpi=100)


        zed6 = zed66.add_subplot(111)
        zed6.plot(data66x,data66y,"#FF8CEC", marker='.')

        for xy in zip(data66x, data66y):
                    zed6.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')

        canvas = FigureCanvasTkAgg(zed66, self)
        
        canvas.draw()
        canvas.get_tk_widget().pack(side= tk.TOP, fill= tk.BOTH, expand= True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side= tk.TOP, fill= tk.BOTH, expand= True)

class ClassSeven(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  

        button1 = ttk.Button(self, text= 'Go back to graph', command= lambda: controller.show_frame(PageOne))
        button2 = ttk.Button(self,  text= 'Update Graph',  command= lambda: self.refresh2())
        button1.pack()
        button2.pack()

    def refresh2(self):
        try:    
            data_7 = open("seven.txt", "r")
            data77 = data_7.read().split(',')
            data_7.close()

            data77y = []
            data77x = []

            for items in data77:
                y_valuer = items.split('@')[0]
                if len(y_valuer) > 1:
                    y_value = float(y_valuer)
                    data77y.append(y_value)
                x_valuer = items.split('@')[-1]
                if len(x_valuer) > 1:
                    data77x.append(x_valuer)         
        except:
            pass   
        zed77 = Figure(figsize= (10,5), dpi=100)


        zed7 = zed77.add_subplot(111)
        zed7.plot(data77x,data77y,"#F5891C", marker='.')

        for xy in zip(data77x, data77y):
                    zed7.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')

        canvas = FigureCanvasTkAgg(zed77, self)
        
        canvas.draw()
        canvas.get_tk_widget().pack(side= tk.TOP, fill= tk.BOTH, expand= True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side= tk.TOP, fill= tk.BOTH, expand= True)

class Average(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  

        button1 = ttk.Button(self, text= 'Go back to graph', command= lambda: controller.show_frame(PageOne))
        button2 = ttk.Button(self,  text= 'Update Graph',  command= lambda: self.refresh2())
        button1.pack()
        button2.pack()

    def refresh2(self):
        try:    
            data_3 = open("avg.txt", "r")
            data33 = data_3.read().split(',')
            data_3.close()

            data33y = []
            data33x = []

            for items in data33:
                y_valuer = items.split('@')[0]
                if len(y_valuer) > 1:
                    y_value = float(y_valuer)
                    data33y.append(y_value)
                x_valuer = items.split('@')[-1]
                if len(x_valuer) > 1:
                    data33x.append(x_valuer)         
        except:
            pass   
        avg = Figure(figsize= (10,5), dpi=100)


        avg1 = avg.add_subplot(111)
        avg1.plot(data33x,data33y, marker='.', ls='--')

        for xy in zip(data33x, data33y):
                    avg1.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')

        canvas = FigureCanvasTkAgg(avg, self)
        
        canvas.draw()
        canvas.get_tk_widget().pack(side= tk.TOP, fill= tk.BOTH, expand= True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side= tk.TOP, fill= tk.BOTH, expand= True)

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  
        label1 = ttk.Label(self, text= "PIE CHART Page", font= Large_Font, background= "#95c8f4")
        label1.pack()
        button1 = ttk.Button(self, text= 'Go back to HOME PAGE', command= lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text= 'Go to Student Portal Class Data Graph', command= lambda: controller.show_frame(PageOne))
        button2.pack()
        button3 = ttk.Button(self, text= 'Update Graph', command= lambda: refresh())
        button3.pack()

        
        def refresh():
            canvas = FigureCanvasTkAgg(g, self)
            
            canvas.draw()
            canvas.get_tk_widget().pack(side= tk.TOP, fill= tk.BOTH, expand= True)

            toolbar = NavigationToolbar2TkAgg(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side= tk.TOP, fill= tk.BOTH, expand= True)
            g.add_subplot(111).pie(denominator, shadow=True, labels=pie_chart_indicator, autopct='%1.1f%%', startangle=90)
            g.legend()
            
class DisplayInDepth1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        button1 = ttk.Button(self, text='Go back to HOME PAGE',  command= lambda: controller.show_frame(StartPage) )
        button3 = ttk.Button(self, text= 'Show Avaliable Data', command= lambda: self.shower())
        button1.grid(row= 1, column= 2)
        button3.grid(row= 1, column= 3)
        button4 = ttk.Button(self, text= 'NEXT', command= lambda: controller.show_frame(DisplayInDepth2))
        button4.grid(row=1, column=4)

    

    def shower(self):
        data_file = open("temp5.txt", 'r')
        avadat1 = data_file.read()
        avadat11 = avadat1.split(',')
        data_file.close()
        avadat = []
        for i in avadat11:
            if len(i) > 1:
                avadat.append(i)
               
        
        if len(avadat) < 20:
            numero = 1
            for items in avadat11:
                if len(items) > 0:
                    numero += 1
                    if "***" in items:
                        tk.Label(self, text= items, bg= '#f9ee68', font= Large_Font).grid(column= 1, row=numero, sticky=  tk.E + tk.W)
                    else:
                        tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 1, row=numero, sticky=  tk.E + tk.W)
            
            data_file = open("temp8.txt", 'r')
            avadat4 = data_file.read()
            avadat44 = avadat4.split(',')
            data_file.close() 
            numero = 1
            tk.Label(self, text= '{} Assignment(s)'.format(len(avadat44)), font= Large_Font, bg= '#95c8f4').grid(row=1,column=1)
            for items in avadat44:
                numero += 1
                tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 2, row=numero, sticky=  tk.W)

            
            data_file = open("temp6.txt", 'r')
            avadat2 = data_file.read()
            avadat22 = avadat2.split(',')
            data_file.close() 
            numero = 1
            for items in avadat22:
                if len(items)  > 0:
                    numero += 1
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 3, row=numero,  sticky= tk.E + tk.W)
            data_file = open("temp7.txt", 'r')
            avadat3 = data_file.read()
            avadat33 = avadat3.split(',')
            data_file.close() 
            numero = 1
            for items in avadat33:
                if len(items)  > 0:
                    numero += 1
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 4, row=numero, sticky=  tk.E + tk.W)

            numero = 1
            numerator = []

            for nums in avadat22:
                nums.replace(" /", '0')
                numerator.append(nums)

       
            
            for num, denom in numerator, avadat33:
                numero += 1
                try:
                    ave = float(num) / float(denom)
                    tk.Label(self, text= "({})".format(ave), bg= '#95c8f4', font= Large_Font).grid(column= 5, row=numero, sticky=  tk.E + tk.W)
                except:
                    tk.Label(self, text= " ", bg= '#95c8f4', font= Large_Font).grid(column= 5, row=numero, sticky=  tk.E + tk.W)

            numero = 1
            numerator = [x.replace(" /", '0') for x in avadat22 ]
                    
            for num, denom in zip(numerator, avadat33):
                numero += 1
                try:
                    ave = round( (float(num) / float(denom)) * 100, 2 )
                    if ave < 90:
                        tk.Label(self, text= "({}%)".format(ave), bg= '#95c8f4', fg= "#d80f4f", font= Large_Font).grid(column= 5, row=numero, sticky=  tk.E + tk.W)
                    else:
                        tk.Label(self, text= "({}%)".format(ave), bg= '#95c8f4', fg= "#0bbf17", font= Large_Font).grid(column= 5, row=numero, sticky=  tk.E + tk.W)   
                except:
                    tk.Label(self, text= " ", bg= '#95c8f4', font= Large_Font).grid(column= 5, row=numero, sticky=  tk.E + tk.W)
      
            
            
        else:
           
            numero = 1
            avadat111 = []
            for items in avadat11:
                if len(items) > 1:
                    avadat111.append(items)

            for items in avadat111[0:21]:
                numero += 1
                if "***" in items:
                    tk.Label(self, text= items, bg= '#f9ee68', font= Large_Font).grid(column= 1, row=numero, sticky=  tk.E + tk.W)
                else:
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 1, row=numero, sticky=  tk.E + tk.W)
        
            data_file = open("temp8.txt", 'r')
            avadat4 = data_file.read()
            avadat44 = avadat4.split(',')
            data_file.close() 

            numero = 1
            avadat444 = []
            for items in avadat44:
                avadat444.append(items)

            for items in avadat444[0:21]:
                numero += 1
                tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 2, row=numero, sticky=  tk.W)

            
            data_file = open("temp6.txt", 'r')
            avadat2 = data_file.read()
            avadat22 = avadat2.split(',')
            data_file.close() 

            numero = 1
            avadat222 = []
            for items in avadat22:
                if len(items) > 0:
                    avadat222.append(items)

            for items in avadat222[0:21]:
                if len(items)  > 0:
                    numero += 1
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 3, row=numero,  sticky= tk.E + tk.W)
            
            data_file = open("temp7.txt", 'r')
            avadat3 = data_file.read()
            avadat33 = avadat3.split(',')
            data_file.close() 

            avadat333 = []
            for items in avadat33:
                if len(items) > 0:
                    avadat333.append(items)

            numero = 1
            for items in avadat333[0:21]:
                if len(items)  > 0:
                    numero += 1
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 4, row=numero, sticky=  tk.E + tk.W)
            
            numero = 1
            numerator = [x.replace(" /", '0') for x in avadat222[0:21] ]
                    
            for num, denom in zip(numerator, avadat333[0:21]):
                numero += 1
                try:
                    ave = round( (float(num) / float(denom)) * 100, 2 )
                    if ave < 90:
                        tk.Label(self, text= "({}%)".format(ave), bg= '#95c8f4', fg= "#d80f4f", font= Large_Font).grid(column= 5, row=numero, sticky=  tk.E + tk.W)
                    else:
                        tk.Label(self, text= "({}%)".format(ave), bg= '#95c8f4', fg= "#0bbf17", font= Large_Font).grid(column= 5, row=numero, sticky=  tk.E + tk.W)
                
                except:
                    tk.Label(self, text= " ", bg= '#95c8f4', font= Large_Font).grid(column= 5, row=numero, sticky=  tk.E + tk.W)

class  DisplayInDepth2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)     
        button1 = ttk.Button(self, text='Go back to HOME PAGE',  command= lambda: controller.show_frame(StartPage) )
        button3 = ttk.Button(self, text= 'Show Avaliable Data', command= lambda: self.shower())
        button1.grid(row= 1, column= 2)
        button3.grid(row= 1, column= 3)
        button4 = ttk.Button(self, text= 'BACK', command= lambda: controller.show_frame(DisplayInDepth1))     
        button4.grid(row=1, column=4)
        self.button5 = ttk.Button(self, text= 'NEXT', command= lambda: controller.show_frame(DisplayInDepth3))
        

    def shower(self):
        data_file = open("temp5.txt", 'r')
        avadat1 = data_file.read()
        avadat11 = avadat1.split(',')
        data_file.close()
        numero = 1
        avadat111 = []
        for items in avadat11:
            if len(items) > 0:
                avadat111.append(items)
        if len(avadat111) < 50:
            for items in avadat111[21:-1]:
                numero += 1
                if "***" in items:
                    tk.Label(self, text= items, bg= '#f9ee68', font= Large_Font).grid(column= 1, row=numero, sticky=  tk.E + tk.W)
                else:
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 1, row=numero, sticky=  tk.E + tk.W)
        

            data_file = open("temp8.txt", 'r')
            avadat4 = data_file.read()
            avadat44 = avadat4.split(',')
            data_file.close() 
            numero = 1
            avadat444 = []
            for items in avadat44:
                avadat444.append(items)
        

            for items in avadat444[21:-1]:
                numero += 1
                tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 2, row=numero, sticky=  tk.W)

            
            data_file = open("temp6.txt", 'r')
            avadat2 = data_file.read()
            avadat22 = avadat2.split(',')
            data_file.close() 

            numero = 1
            avadat222 = []
            for items in avadat22:
                if len(items) > 0:
                    avadat222.append(items)

            for items in avadat222[21:-1]:
                if len(items)  > 0:
                    numero += 1
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 3, row=numero,  sticky= tk.E + tk.W)
            
            data_file = open("temp7.txt", 'r')
            avadat3 = data_file.read()
            avadat33 = avadat3.split(',')
            data_file.close() 

            avadat333 = []
            for items in avadat33:
                if len(items) > 0:
                    avadat333.append(items)

            numero = 1
            for items in avadat333[21:-1]:
                if len(items)  > 0:
                    numero += 1
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 4, row=numero, sticky=  tk.E + tk.W)
        
            numero = 1
            numerator = [x.replace(" /", '0') for x in avadat222[21:-1] ]
                    
            for num, denom in zip(numerator, avadat333[21:-1]):
                numero += 1
                try:
                    ave = round((float(num) / float(denom)) * 100, 2)
                    if ave < 90:
                        tk.Label(self, text= "({}%)".format(ave), bg= '#95c8f4',fg= "#d80f4f", font= Large_Font).grid(column= 5, row=numero, sticky=  tk.E + tk.W)
                    else:
                        tk.Label(self, text= "({}%)".format(ave), bg= '#95c8f4',fg= "#0bbf17", font= Large_Font).grid(column= 5, row=numero, sticky=  tk.E + tk.W)                    
                except:
                    tk.Label(self, text= " ", bg= '#95c8f4', font= Large_Font).grid(column= 5, row=numero, sticky=  tk.E + tk.W)        
        else:
            self.button5.grid(row=1, column= 5)
            data_file = open("temp5.txt", 'r')
            avadat1 = data_file.read()
            avadat11 = avadat1.split(',')
            data_file.close()
            numero = 1
            avadat444 = []

            for items in avadat11:
                if len(items) > 0:
                    avadat444.append(items)
            
            
            for items in avadat444[21:41]:
                numero += 1
                if "***" in items:
                        tk.Label(self, text= items, bg= '#f9ee68', font= Large_Font).grid(column= 1, row=numero, sticky=  tk.E + tk.W)
                else:
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 1, row=numero, sticky=  tk.E + tk.W)
        
            
            data_file = open("temp6.txt", 'r')
            avadat2 = data_file.read()
            avadat22 = avadat2.split(',')
            data_file.close() 

            numero = 1
            avadat222 = []
            for items in avadat22:
                if len(items) > 0:
                    avadat222.append(items)

            for items in avadat222[21:41]:
                if len(items)  > 0:
                    numero += 1
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 3, row=numero,  sticky= tk.E + tk.W)
            
            data_file = open("temp7.txt", 'r')
            avadat3 = data_file.read()
            avadat33 = avadat3.split(',')
            data_file.close() 

            avadat333 = []
            for items in avadat33:
                if len(items) > 0:
                    avadat333.append(items)

            numero = 1
            for items in avadat333[21:41]:
                if len(items)  > 0:
                    numero += 1
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 4, row=numero, sticky=  tk.E + tk.W)

            data_file = open("temp8.txt", 'r')
            avadat5 = data_file.read()
            avadat55 = avadat5.split(',')
            data_file.close() 

            avadat555 = []
            for items in avadat55:
                avadat555.append(items)

            numero = 1
            for items in avadat555[21:41]:
                if len(items)  > 0:
                    numero += 1
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 2, row=numero, sticky=  tk.E + tk.W)
        



            numero = 1
            numerator = [x.replace(" /", '0') for x in avadat222[21:41] ]
                    
            for num, denom in zip(numerator, avadat333[21:41]):
                numero += 1
                try:
                    ave = round((float(num) / float(denom)) * 100, 2)
                    if ave < 90:
                        tk.Label(self, text= "({}%)".format(ave), bg= '#95c8f4',fg= "#d80f4f", font= Large_Font).grid(column= 5, row=numero, sticky=  tk.E + tk.W)
                    else:
                        tk.Label(self, text= "({}%)".format(ave), bg= '#95c8f4',fg= "#0bbf17", font= Large_Font).grid(column= 5, row=numero, sticky=  tk.E + tk.W)                    
                except:
                    tk.Label(self, text= " ", bg= '#95c8f4', font= Large_Font).grid(column= 5, row=numero, sticky=  tk.E + tk.W)

class  DisplayInDepth3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)   
        button1 = ttk.Button(self, text='Go back to HOME PAGE',  command= lambda: controller.show_frame(StartPage) )
        button3 = ttk.Button(self, text= 'Show Avaliable Data', command= lambda: self.shower())
        button1.grid(row= 1, column= 2)
        button3.grid(row= 1, column= 3)
        button4 = ttk.Button(self, text= 'BACK', command= lambda: controller.show_frame(DisplayInDepth2))     
        button4.grid(row=1, column=4)

    def shower(self):
        data_file = open("temp5.txt", 'r')
        avadat1 = data_file.read()
        avadat11 = avadat1.split(',')
        data_file.close()
        numero = 1
        avadat111 = []
        for items in avadat11:
            if len(items) > 0:
                avadat111.append(items)

        for items in avadat111[41:-1]:
            numero += 1
            if "***" in items:
                tk.Label(self, text= items, bg= '#f9ee68', font= Large_Font).grid(column= 1, row=numero, sticky=  tk.E + tk.W)
            else:
                tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 1, row=numero, sticky=  tk.E + tk.W)
    
        data_file = open("temp8.txt", 'r')
        avadat4 = data_file.read()
        avadat44 = avadat4.split(',')
        data_file.close() 
        numero = 1
        avadat444 = []
        for items in avadat44:
            avadat444.append(items)
        

        for items in avadat444[41:-1]:
            numero += 1
            tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 2, row=numero, sticky=  tk.W)

        
        data_file = open("temp6.txt", 'r')
        avadat2 = data_file.read()
        avadat22 = avadat2.split(',')
        data_file.close() 

        numero = 1
        avadat222 = []
        for items in avadat22:
            if len(items) > 0:
                avadat222.append(items)

        for items in avadat222[41:-1]:
            if len(items)  > 0:
                numero += 1
                tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 3, row=numero,  sticky= tk.E + tk.W)
        
        data_file = open("temp7.txt", 'r')
        avadat3 = data_file.read()
        avadat33 = avadat3.split(',')
        data_file.close() 

        avadat333 = []
        for items in avadat33:
            if len(items) > 0:
                avadat333.append(items)

        numero = 1
        for items in avadat333[41:-1]:
            if len(items)  > 0:
                numero += 1
                tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 4, row=numero, sticky=  tk.E + tk.W)
    
        numero = 1
        numerator = [x.replace(" /", '0') for x in avadat222[41:-1] ]
                
        for num, denom in zip(numerator, avadat333[41:-1]):
            numero += 1
            try:
                ave = round((float(num) / float(denom)) * 100, 2)
                if ave < 90:
                    tk.Label(self, text= "({}%)".format(ave), bg= '#95c8f4',fg= "#d80f4f", font= Large_Font).grid(column= 5, row=numero, sticky=  tk.E + tk.W)
                else:
                    tk.Label(self, text= "({}%)".format(ave), bg= '#95c8f4',fg= "#0bbf17", font= Large_Font).grid(column= 5, row=numero, sticky=  tk.E + tk.W)                    
            except:
                tk.Label(self, text= " ", bg= '#95c8f4', font= Large_Font).grid(column= 5, row=numero, sticky=  tk.E + tk.W)

class Homework(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button3 = ttk.Button(self, text= 'Show Avaliable Data', command= lambda: self.shower())
        button3.grid(row= 1, column= 3)
        button1 = ttk.Button(self, text='Go back to HOME PAGE',  command= lambda: controller.show_frame(StartPage) )
        button1.grid(row= 1, column= 2)
        
    def shower(self):
        try:
            data_file = open("temp9.txt", 'r')
            avadat1 = data_file.read()
            avadat11 = avadat1.split('***')
            dates = avadat11[0].split(',')
            hws = avadat11[1].split('^^')
            data_file.close()

            numero = 1
            for items in dates:
                numero += 1
                tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 1, row=numero, sticky=  tk.E + tk.W)
            
            numero = 1 
            for items in hws:
                numero += 1
                if len(items) < 50:
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 2, row=numero, sticky=  tk.W)
                else:
                    i = items[0:50] + '...'
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 2, row=numero, sticky=  tk.W)
        except:
            tk.Label(self, text= 'Homework from Google Classroom was not collected', bg= '#95c8f4', font= Large_Font).grid(column= 2, row=4, sticky=  tk.W)
            
class UnannotatedGraph(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label1 = tk.Label(self, text= 'Unannotated Graph Page',  bg= '#95c8f4', font= Large_Font).pack()
        button1 = ttk.Button(self, text= 'Go back to HOME PAGE', command= lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text= 'Go to Student Portal Class Data Graph', command= lambda: controller.show_frame(PageOne))
        button2.pack()
        button3 = ttk.Button(self, text= 'Update Graph', command= lambda: self.refresh())
        button3.pack()

    def refresh(self):
        canvas = FigureCanvasTkAgg(una, self)
        
        canvas.draw()
        canvas.get_tk_widget().pack(side= tk.TOP, fill= tk.BOTH, expand= True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side= tk.TOP, fill= tk.BOTH, expand= True)

app = GradeGetterApp()
app.mainloop()
