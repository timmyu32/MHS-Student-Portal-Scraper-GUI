'''
 * @author Timothy Uzoegbu
 * Program Name: GradeGetter
 * 
 * Description:  Graphs grades for Medway High School Students 
                 Displays graded assignments
                 Displays classs averages
                 Displays individual class progress overtime as well as cumulative avergae on the same or seperate graphs
    Recent Fixes:
                Fixed the Display in Depth Classess so that the info displayed in column2 is accurate
                Added winsound fx to alert user that login is complete

    Things to consider:
                Logging in for other people still writes over my saved data in the .txt files sinceI have yet to find a way to scrape and
                save guest data after the change from the previous grading portal to the new one as of 8/18.
                Right now, this part of the progam is not functional 

                Look into how to create a text area with vertical scrollbar to consolodate graded assignments into one page/class


 * Date: 12/24/18
 * Programmer: TU
 * 
'''

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
from selenium.webdriver.common.action_chains import ActionChains


from functools import reduce as reducer

from datetime import date as date

from PIL import Image, ImageTk

import time

import threading 
from queue import Queue

import csv

import winsound


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
global uname_for_pop_up_trans
global pass_for_pop_up_trans
una = Figure(figsize = (10,5), dpi=100)
f = Figure(figsize = (10,5), dpi=100)
g = Figure(figsize = (5,5), dpi=100)
zed = Figure(figsize= (10,5), dpi=100)
bary = Figure(figsize= (5,5), dpi=100)
unatated = una.add_subplot(111)
a = f.add_subplot(111)
baro = bary.add_subplot(111)

class reassign1(object):
    #This class stores the integer number of the player's value once they abstain at any point
    #reassign_pv will be used to compare compturn vlue to player value and return a string 
    def __init__(self, pvalue= 0):
        self.pvalue = pvalue

    def reassign_user(self):
        #This class holds the value of the player's value outside of playerturn()
        return self.pvalue

class reassign2(object):
    #This class stores the integer number of the player's value once they abstain at any point
    #reassign_pv will be used to compare compturn vlue to player value and return a string 
    def __init__(self, pvalue= 0):
        self.pvalue = pvalue

    def reassign_pass(self):
        #This class holds the value of the player's value outside of playerturn()
        return self.pvalue

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
        
        for F in (StartPage, PageOne, PageTwo, Homework, Login, AdminPage, DisplayInDepth1, ClassOne, ClassTwo, ClassThree, ClassFour, ClassFive, ClassSix, ClassSeven, UnannotatedGraph, BarGraph, Average, DisplayInDepth2,  DisplayInDepth3, DisplayInDepth4):
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
        self.label1 = tk.Label(self, text= "Enter your name, then click Verifiy and NEXT.", bg="#95c8f4", font = Largest_Font)
        self.label1.place(x=400, y= 200)
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
        
        def rgb_2_hex():
            import random
            
            hex_keys = {10: 'A',
                        11: 'B',
                        12: 'C',
                        13: 'D',
                        14: 'E',
                        15: 'F'}
            
            end_result = []

            for i in range(1):
                num = random.randint(0,256)
                x = num // 16
                y = num % 16

                if x > 9:
                    x = hex_keys[x]
                if y > 9:
                    y = hex_keys[y]

                value = str(x) + str(y)
                end_result.append(value)
                
            
            return end_result


        if a == "gui":
            tim = True
            timnoget = False
            tk.Label(self, text= 'Welcome Back Tim!', font= Largest_Font, bg= '#95c8f4').place(x=600, y=310)
            random_color = '#'+rgb_2_hex()[0] + rgb_2_hex()[0] + rgb_2_hex()[0]
            self.label1.config(fg= random_color )
            print(random_color)
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
        self.label4.config(text= 'Please Wait...', fg= 'black')
        uname_for_pop_up = reassign1(self.u1.get())
        #print(uname_for_pop_up.reassign_user())
        uname_for_pop_up_trans = uname_for_pop_up
        

        pass_for_pop_up = reassign2(self.p1.get())
        pass_for_pop_up.reassign_pass()
        pass_for_pop_up_trans = pass_for_pop_up
        if tim:
            def gc_get():
                
                if len(self.gc_p.get()) > 1:
                    gc_password = self.gc_p.get()
                    configurer = webdriver.ChromeOptions()
                    configurer.add_argument("-headless")
                    #browser = webdriver.Chrome("C:\\Users\\inspiron\\Downloads\\chromedriver_win32\\chromedriver", chrome_options=configurer)
                    browser = webdriver.Chrome()

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
                driver = webdriver.Chrome("C:\\Users\\inspiron\\Downloads\\chromedriver_win32\\chromedriver", chrome_options=options)
                #driver = webdriver.Chrome("C:\\Users\\inspiron\\Downloads\\chromedriver_win32\\chromedriver")
                driver.get('https://medway.crportals.studentinformation.systems/')
                uname = driver.find_element_by_name('Email')
                password = driver.find_element_by_name('Password')
                login_btn = driver.find_element_by_id('loginBtn')

                uname.clear()
                uname.send_keys(u)
                password.send_keys(p)
                login_btn.click()

                try:
                    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='field-validation-error text-danger']")))
                    error_msg = driver.find_element_by_xpath("//span[@class='field-validation-error text-danger']").text
                    if type(error_msg) != None:
                        data_file = open("temp3.txt", 'w')
                        data_file.write(error_msg)
                        data_file.close()
                        self.label4.config(text=error_msg, fg='red')
                           
                except:
                    data_file = open("temp3.txt", 'w')
                    data_file.write("No errors")
                    data_file.close()


                timeout = 10
                try:
                    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//ul[@class='student-info-list']")))
                except:
                    driver.close()

                at_a_glance = driver.find_elements_by_xpath("//span[@class='tile-anchor-label']")[5]
                at_a_glance.click()

                try:
                    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='k-link']")))
                except:
                    driver.close()

                alphabetizer = driver.find_elements_by_xpath("//a[@class='k-link']")[0]
                alphabetizer.click()

                grade_table = driver.find_elements_by_xpath("//tbody[@role='rowgroup']")[0]

                
                class_names = []
                class_grades = []

                for row in grade_table.find_elements_by_tag_name('tr'):
                    grade = row.find_elements_by_tag_name('td')
                    for thingy in grade:
                        try:
                            class_names.append(float(thingy.text.split('\n')[0]))
                        except:
                            class_names.append(str(thingy.text.split('\n')[0]))
                
               
                print(class_names)
                

                for item in class_names:
                    if type(item) == float or type(item) == int or item == 'No Grade':
                        class_names.remove(item)
                        class_grades.append(item)
                
                #this segment is still under development and may be needed when there is a transition from term to term... not sure- 11/15/18
                '''
                class_name_holder = ''
                for items in class_names:
                    print(items+'\n')
                    print(class_name_holder)
                    class_name_holder = items
                    if items == class_name_holder:
                        class_names.remove(items)
                

                print(class_grades)
                print(class_names)
                input('sadfad')

                guideLine = len(class_names) + 1
                appropriateNumberOfGrades = ( len(class_grades) + 1 ) / guideLine
                counter = 0
                class_grades2 = []
                for items in class_grades:
                    if counter % appropriateNumberOfGrades != 0:
                        class_grades2.append(items)
                    
                    counter += 1

                print(class_grades2)
                print(class_names)
                input('sadfad')
                '''
                
                today = str(date.today())

                global denominator
                denominator = []
                global pie_chart_indicator

                
                pie_chart_indicator = []

                data_file = open('temp10.csv', 'w')
                
                class_name_csv = csv.writer(data_file)
                class_name_csv.writerow(class_names)

                data_file.close()

                try:
                    class1_name = class_names[0]
                except:
                    pass
                try:
                    class2_name = class_names[1]
                except:
                    pass
                try:
                    class3_name = class_names[2]
                except:
                    pass
                try:
                    class4_name = class_names[3]
                except:
                    pass
                try:
                    class5_name = class_names[4]
                except:
                    pass
                try:
                    class6_name = class_names[5]
                except:
                    pass
                try:
                    class7_name = class_names[6]
                except:
                    pass
                try:
                    class8_name = class_names[7]
                except:
                    pass
                
                
                    


                driver.get('https://medway.crportals.studentinformation.systems/')
                uname = driver.find_element_by_name('Email')
                password = driver.find_element_by_name('Password')
                login_btn = driver.find_element_by_id('loginBtn')

                uname.clear()
                uname.send_keys(u)
                password.send_keys(p)
                login_btn.click()

                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='col-md-6 tile-wrapper']")))
                assignments_tab = driver.find_elements_by_xpath("//div[@class='col-md-6 tile-wrapper']")[1]
                assignments_tab.click()

                time.sleep(4)

                class_name = driver.find_elements_by_xpath("//h3[@class='panel-title']")[1].text


                ids = []
                id_descriptors = []
                grdr = []
                grdr2 = []
                grdr3 = []

                try:
                    looper = 5

                    for links in range(       len(driver.find_elements_by_xpath("//li[@role= 'presentation']"))):
                        try:
                            driver.switch_to.parent_frame()
                        except:
                            print('no element')

                        links = driver.find_elements_by_xpath("//li[@role= 'presentation']")[looper]
                        links.click()
                        progress_report = driver.find_elements_by_xpath("//button[@class='btn btn-link']")[looper]
                        progress_report.click()

                        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//iframe[@id= 'courseProgressReportFrame']")))
                        driver.switch_to.frame(driver.find_elements_by_xpath("//iframe[@id= 'courseProgressReportFrame']")[0])

                        
                        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id= 'ctl00_ContentPlaceHolder1_ReportViewer1ReportFrame']"))
                        class_identifiers = [x.text for x in driver.find_elements_by_xpath("//div[@class='HtmlTextBox2 s22-']")]
                        class_identifiers2 = [x.text for x in driver.find_elements_by_xpath("//div[@class='HtmlTextBox2 s25-']")]
                                        
                        if len(class_identifiers) > 0:
                            ids.append(class_identifiers)
                            descriptor = [x.text.replace('\n',  ' ') for x in driver.find_elements_by_xpath("//div[@class='TextBox41 s28-']") ]
                            if len(descriptor) > 0:
                                id_descriptors.append([('***{}***').format( driver.find_element_by_xpath("//div[@class='TextBox5 s5-']").text[0:-2])])
                                id_descriptors.append(descriptor)
                                grdr.append(['{}{} Assignments'.format(  len( driver.find_elements_by_xpath("//div[@class='TextBox46 s29-']"))-1, '4465' )])
                                grdr2.append([driver.find_element_by_xpath("//div[@class='TextBox16 s13-']").text + '4465'])
                                grdr3.append([' '])
                                grd1 = [x.text for x in driver.find_elements_by_xpath("//div[@class='TextBox46 s29-']") ]
                                grd2 = [x.text for x in driver.find_elements_by_xpath("//div[@class='TextBox27 s28-']") ]
                                grd3 = [x.text.replace(",", "-") for x in driver.find_elements_by_xpath("//div[@class= 'TextBox42 s28-']") ] 
                                if len(grd1) > 0:
                                    grdr.append(grd1)
                                    grdr2.append(grd2)
                                    grdr3.append(grd3)
                                driver.switch_to.parent_frame()
                                driver.refresh()
                                

                                looper += -1
                            else:
                                looper += -1
                                driver.switch_to.parent_frame()
                                driver.refresh()
                            
                        else:
                            looper += -1
                            driver.switch_to.parent_frame()
                            driver.refresh()
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
                except:
                    looper = 4

                    for links in range(       len(driver.find_elements_by_xpath("//li[@role= 'presentation']"))):
                        try:
                            driver.switch_to.parent_frame()
                        except:
                            print('no element')

                        links = driver.find_elements_by_xpath("//li[@role= 'presentation']")[looper]
                        links.click()
                        progress_report = driver.find_elements_by_xpath("//button[@class='btn btn-link']")[looper]
                        progress_report.click()

                        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//iframe[@id= 'courseProgressReportFrame']")))
                        driver.switch_to.frame(driver.find_elements_by_xpath("//iframe[@id= 'courseProgressReportFrame']")[0])

                        
                        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id= 'ctl00_ContentPlaceHolder1_ReportViewer1ReportFrame']"))
                        class_identifiers = [x.text for x in driver.find_elements_by_xpath("//div[@class='HtmlTextBox2 s22-']")]
                        class_identifiers2 = [x.text for x in driver.find_elements_by_xpath("//div[@class='HtmlTextBox2 s25-']")]
                                        
                        if len(class_identifiers) > 0:
                            ids.append(class_identifiers)
                            descriptor = [x.text.replace('\n',  ' ') for x in driver.find_elements_by_xpath("//div[@class='TextBox41 s28-']") ]
                            if len(descriptor) > 0:
                                id_descriptors.append([('***{}***').format( driver.find_element_by_xpath("//div[@class='TextBox5 s5-']").text[0:-2])])
                                id_descriptors.append(descriptor)
                                grdr.append(['{}{} Assignments'.format(  len( driver.find_elements_by_xpath("//div[@class='TextBox46 s29-']"))-1, '4465' )])
                                grdr2.append([driver.find_element_by_xpath("//div[@class='TextBox16 s13-']").text + '4465'])
                                grdr3.append([' '])
                                grd1 = [x.text for x in driver.find_elements_by_xpath("//div[@class='TextBox46 s29-']") ]
                                grd2 = [x.text for x in driver.find_elements_by_xpath("//div[@class='TextBox27 s28-']") ]
                                grd3 = [x.text.replace(",", "-") for x in driver.find_elements_by_xpath("//div[@class= 'TextBox42 s28-']") ] 
                                if len(grd1) > 0:
                                    grdr.append(grd1)
                                    grdr2.append(grd2)
                                    grdr3.append(grd3)
                                driver.switch_to.parent_frame()
                                driver.refresh()
                                

                                looper += -1
                            else:
                                looper += -1
                                driver.switch_to.parent_frame()
                                driver.refresh()
                            
                        else:
                            looper += -1
                            driver.switch_to.parent_frame()
                            driver.refresh()

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


                    try:
                        class1_grade = float(class_grades[0])
                    except:
                        class1_grade = int(class_grades[0])
                    
                    denominator.append(class1_grade)
                    pie_chart_indicator.append(str(class1_name) + '(' + str(class1_grade) + ')')
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
                    try:
                        class2_grade = float(class_grades[1])
                    except:
                        class2_grade = int(class_grades[1])
                    denominator.append(class2_grade)
                    pie_chart_indicator.append(str(class2_name) +'(' + str(class2_grade) + ')')
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
                    try:
                        class3_grade = float(class_grades[2])
                    except:
                        class3_grade = int(class_grades[2])

                    denominator.append(class3_grade) 
                    pie_chart_indicator.append(str(class3_name) + '(' + str(class3_grade) + ')')
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
                    try:
                        class4_grade = float(class_grades[3])
                    except:
                        class4_grade = int(class_grades[3])

                    denominator.append(class4_grade) 
                    pie_chart_indicator.append(str(class4_name) +'(' + str(class4_grade) + ')')
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
                    try:
                        class5_grade = float(class_grades[4])
                    except:
                        class5_grade = int(class_grades[4])

                    denominator.append(class5_grade)
                    pie_chart_indicator.append(str(class5_name) +'(' + str(class5_grade) + ')')  
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
                    try:
                        class6_grade = float(class_grades[5])
                    except:
                        class6_grade = int(class_grades[5])  

                    denominator.append(class6_grade) 
                    pie_chart_indicator.append(str(class6_name) + '(' + str(class6_grade) + ')') 
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
                    try:
                        class7_grade = float(class_grades[6])
                    except:
                        class7_grade = int(class_grades[6])

                    denominator.append(class7_grade)
                    pie_chart_indicator.append(str(class7_name) + '(' + str(class7_grade) + ')')
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
            
                d = len(denominator)
                n = reducer(lambda x,y: x+y, denominator)

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
                try:
                    a.plot(data66x, data66y, "#FF8CEC", label= class6_name, data= class6_name, marker= '.')
                    unatated.plot(data66x, data66y, "#FF8CEC", label= class6_name, data= class6_name, marker= '.')
                except:
                    pass
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
                    print("Class {} is not avaliable for bar graph".format('dood'))
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
                try:
                    for xy in zip(data66x, data66y):
                        a.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
                    for xy in zip(data77x, data77y):
                        a.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
                except:
                    pass
                temporal_lobe = open('temp3.txt', 'r')
                occipital = temporal_lobe.read()
                if occipital.startswith('N'):
                    self.label4.config(text='Click NEXT', fg= 'black' )
                    self.button3.place(x=460, y=330)
                else:
                    self.label4.config(text='An ERROR has occured, try correcting your user and password.', fg= 'red')

                winsound.MessageBeep()

                
            threading.Thread(target = get_grades).start()
            threading.Thread(target = gc_get).start() 

        else:
            nono = True
            timestamps = ['Quarter 1', 'Quarter 2', 'Quarter 3', 'Current']
            u = self.u1.get()
            p = self.p1.get()
            goog = self.gc_p.get()
            
            
    

            def get_grades2():
                
                options = webdriver.ChromeOptions()

                options.add_argument("-headless")
                driver = webdriver.Chrome(chrome_options=options)
                #driver = webdriver.Chrome("C:\\Users\\inspiron\\Downloads\\chromedriver_win32\\chromedriver")

                driver.get('https://medway.crportals.studentinformation.systems/')
                uname = driver.find_element_by_name('Email')
                password = driver.find_element_by_name('Password')
                login_btn = driver.find_element_by_id('loginBtn')

                uname.clear()
                password.clear()
                uname.send_keys(u)
                password.send_keys(p)
                login_btn.click()
                time.sleep(1)

                try:
                    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='field-validation-error text-danger']")))
                    error_msg = driver.find_element_by_xpath("//span[@class='field-validation-error text-danger']").text
                    if type(error_msg) != None:
                        data_file = open("temp3.txt", 'w')
                        data_file.write(error_msg)
                        data_file.close()        
                except:
                    pass


                timeout = 4.6
                try:
                    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//ul[@class='student-info-list']")))
                except:
                    self.label4.config(text='An Error has occured, please use correct username and password', fg='red')
                    driver.close()

                at_a_glance = driver.find_elements_by_xpath("//span[@class='tile-anchor-label']")[5]
                at_a_glance.click()

                try:
                    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='k-link']")))
                except:
                    driver.close()


                alphabetizer = driver.find_elements_by_xpath("//a[@class='k-link']")[0]
                alphabetizer.click()

                grade_table = driver.find_elements_by_xpath("//tbody[@role='rowgroup']")[0]

                
                class_names = []
                class_grades = []

                for row in grade_table.find_elements_by_tag_name('tr'):
                    grade = row.find_elements_by_tag_name('td')
                    for thingy in grade:
                        print(thingy.text.split('\n'))
                        class_names.append(thingy.text.split('\n')[0])
                        class_grades.append(thingy.text.split('\n')[1])

                for item in class_names:
                    if type(item) == float or type(item) == int or item == 'No Grade':
                        transfer = item
                        class_names.remove(item)
                        class_grades.append(item)

             
                try:
                    class1_name = class_names[0]
                except:
                    pass
                try:
                    class2_name = class_names[1]
                except:
                    pass
                try:
                    class3_name = class_names[2]
                except:
                    pass
                try:
                    class4_name = class_names[3]
                except:
                    pass
                try:
                    class5_name = class_names[4]
                except:
                    pass
                try:
                    class6_name = class_names[5]
                except:
                    pass
                try:
                    class7_name = class_names[6]
                except:
                    pass
                try:
                    class8_name = class_names[7]
                except:
                    pass
               
                global denominator
                denominator = []
                
                driver.get('https://medway.crportals.studentinformation.systems/')
                uname = driver.find_element_by_name('Email')
                password = driver.find_element_by_name('Password')
                login_btn = driver.find_element_by_id('loginBtn')

                uname.clear()
                uname.send_keys(u)
                password.send_keys(p)
                login_btn.click()

                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='col-md-6 tile-wrapper']")))
                assignments_tab = driver.find_elements_by_xpath("//div[@class='col-md-6 tile-wrapper']")[1]
                assignments_tab.click()

                time.sleep(4)

                class_name = driver.find_elements_by_xpath("//h3[@class='panel-title']")[1].text


                ids = []
                id_descriptors = []
                grdr = []
                grdr2 = []
                grdr3 = []


                looper = 5

                for links in range(       len(driver.find_elements_by_xpath("//li[@role= 'presentation']"))):
                    try:
                        driver.switch_to.parent_frame()
                    except:
                        print('no element')

                    print('9')
                    print(looper)
                    links = driver.find_elements_by_xpath("//li[@role= 'presentation']")[looper]
                    links.click()
                    print('10')
                    progress_report = driver.find_elements_by_xpath("//button[@class='btn btn-link']")[looper]
                    progress_report.click()

                    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//iframe[@id= 'courseProgressReportFrame']")))
                    driver.switch_to.frame(driver.find_elements_by_xpath("//iframe[@id= 'courseProgressReportFrame']")[0])

                    
                    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id= 'ctl00_ContentPlaceHolder1_ReportViewer1ReportFrame']"))
                    class_identifiers = [x.text for x in driver.find_elements_by_xpath("//div[@class='HtmlTextBox2 s22-']")]
                    class_identifiers2 = [x.text for x in driver.find_elements_by_xpath("//div[@class='HtmlTextBox2 s25-']")]
                                    
                    if len(class_identifiers) > 0:
                        ids.append(class_identifiers)
                        descriptor = [x.text.replace('\n',  ' ') for x in driver.find_elements_by_xpath("//div[@class='TextBox41 s28-']") ]
                        if len(descriptor) > 0:
                            id_descriptors.append([('***{}***').format( driver.find_element_by_xpath("//div[@class='TextBox5 s5-']").text[0:-2])])
                            id_descriptors.append(descriptor)
                            grdr.append(['{}{} Assignments'.format(  len( driver.find_elements_by_xpath("//div[@class='TextBox46 s29-']"))-1, '4465' )])
                            grdr2.append([driver.find_element_by_xpath("//div[@class='TextBox16 s13-']").text + '4465'])
                            grdr3.append([' '])
                            grd1 = [x.text for x in driver.find_elements_by_xpath("//div[@class='TextBox46 s29-']") ]
                            grd2 = [x.text for x in driver.find_elements_by_xpath("//div[@class='TextBox27 s28-']") ]
                            grd3 = [x.text.replace(",", "-") for x in driver.find_elements_by_xpath("//div[@class= 'TextBox42 s28-']") ] 
                            if len(grd1) > 0:
                                grdr.append(grd1)
                                grdr2.append(grd2)
                                grdr3.append(grd3)
                            driver.switch_to.parent_frame()
                            driver.refresh()
                            

                            looper += -1
                        else:
                            looper += -1
                            driver.switch_to.parent_frame()
                            driver.refresh()
                        
                    else:
                        looper += -1
                        driver.switch_to.parent_frame()
                        driver.refresh()

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
                    try:
                        class1_grade = float(class_grades[0])
                    except:
                        class1_grade = int(class_grades[0])
                    

                    denominator.append(class1_grade)
                except:
                    class1_grade = 0
                try:
                    try:
                        class2_grade = float(class_grades[1])
                    except:
                        class2_grade = int(class_grades[1])
                    

                    denominator.append(class2_grade)         
                except:
                    class2_grade = 0
                try:
                    try:
                        class3_grade = float(class_grades[2])
                    except:
                        class3_grade = int(class_grades[2])
                    

                    denominator.append(class3_grade)   
                except:
                    class3_grade = 0
                try:
                    try:
                        class4_grade = float(class_grades[3])
                    except:
                        class4_grade = int(class_grades[3])
                    

                    denominator.append(class4_grade)   
                except:
                    class4_grade = 0
                try:
                    try:
                        class5_grade = float(class_grades[4])
                    except:
                        class5_grade = int(class_grades[4])
                    

                    denominator.append(class5_grade)   
                except:
                    class5_grade = 0
                try:
                    try:
                        class6_grade = float(class_grades[5])
                    except:
                        class6_grade = int(class_grades[5])
                    

                    denominator.append(class6_grade)  
                except:
                    class6_grade = 0
                try:
                    try:
                        class7_grade = float(class_grades[6])
                    except:
                        class7_grade = int(class_grades[6])
                    

                    denominator.append(class7_grade)   
                except:
                    class7_grade = 0
                try:
                    try:
                        class8_grade = float(class_grades[0])
                    except:
                        class8_grade = int(class_grades[0])
                    

                    denominator.append(class8_grade)  
                except:
                    class8_grade = 0



                try:        
                    d = len(denominator)
                    n = functools.reduce(lambda x,y: x+y, denominator)
                except:
                    pass

                try:
                    current_q_average = round(n/d, 2)
                except:
                    pass


                class1s =[]
                class2s = []
                class3s = []
                class4s = []
                class5s= []
                class6s =[]
                class7s = []


                class1_namer = class_name_coullumn[0]
                class2_namer = class_name_coullumn[1]
                class3_namer = class_name_coullumn[2]
                class4_namer = class_name_coullumn[3]
                class5_namer = class_name_coullumn[4]
                class6_namer = class_name_coullumn[5]
                class7_namer = class_name_coullumn[6]

                


                class1_gradeq1 = grade_collumn1[0]
                class1s.append(class1_gradeq1)

                class2_gradeq1 = grade_collumn1[1]
                class2s.append(class2_gradeq1)

                class3_gradeq1 = grade_collumn1[2]
                class3s.append(class3_gradeq1)

                class4_gradeq1 = grade_collumn1[3]
                class4s.append(class4_gradeq1)

                class5_gradeq1 = grade_collumn1[4]
                class5s.append(class5_gradeq1)

                class6_gradeq1 = grade_collumn1[5]
                class6s.append(class6_gradeq1)

                class7_gradeq1 = grade_collumn1[6]
                class7s.append(class7_gradeq1)
            

                class1_gradeq2 = grade_collumn2[0]
                class1s.append(class1_gradeq2)

                class2_gradeq2 = grade_collumn2[1]
                class2s.append(class2_gradeq2)

                class3_gradeq2 = grade_collumn2[2]
                class3s.append(class3_gradeq2)

                class4_gradeq2 = grade_collumn2[3]
                class4s.append(class4_gradeq2)

                class5_gradeq2 = grade_collumn2[4]
                class5s.append(class5_gradeq2)

                class6_gradeq2 = grade_collumn2[5]
                class6s.append(class6_gradeq2)

                class7_gradeq2 = grade_collumn2[6]
                class7s.append(class7_gradeq2)

                class1_gradeq3 = grade_collumn3[0]
                class1s.append(class1_gradeq3)

                class2_gradeq3 = grade_collumn3[1]
                class2s.append(class2_gradeq3)

                class3_gradeq3 = grade_collumn3[2]
                class3s.append(class3_gradeq3)

                class4_gradeq3 = grade_collumn3[3]
                class4s.append(class4_gradeq3)

                class5_gradeq3 = grade_collumn3[4]
                class5s.append(class5_gradeq3)

                class6_gradeq3 = grade_collumn3[5]
                class6s.append(class6_gradeq3)

                class7_gradeq3 = grade_collumn3[6]
                class7s.append(class7_gradeq3)

                class1s.append(class1_grade)
                class2s.append(class2_grade)
                class3s.append(class3_grade)
                class4s.append(class4_grade)
                class5s.append(class5_grade)
                class6s.append(class6_grade)
                class7s.append(class7_grade)

                timestamps = ['Quatyer 1', 'Quarter 2', 'Quarter 3', 'Current']

                data_file = open("temp.txt", "w")
                g=','
                
                data_file.write(class1_namer+g+class2_namer+g+class3_namer+g+class4_namer+g+class5_namer+g+class6_namer+g+class7_namer+'***')
                
                for grade in class1s:
                    if grade == None:
                        pass
                    else:
                        data_file.write(str(grade)+ ',')
                data_file.write('/')

                for grade in class2s:
                    if grade == None:
                        pass
                    else:
                        data_file.write(str(grade)+ ',')
                data_file.write('/')

                for grade in class3s:
                    if grade == None:
                        pass
                    else:
                        data_file.write(str(grade)+ ',')
                data_file.write('/')

                for grade in class4s:
                    if grade == None:
                        pass
                    else:
                        data_file.write(str(grade)+ ',')
                data_file.write('/')

                for grade in class5s:
                    if grade == None:
                        pass
                    else:
                        data_file.write(str(grade)+ ',')
                data_file.write('/')

                for grade in class6s:
                    if grade == None:
                        pass
                    else:
                        data_file.write(str(grade)+ ',')
                data_file.write('/')

                for grade in class7s:
                    if grade == None:
                        pass
                    else:
                        data_file.write(str(grade)+ ',')
                
                code_grade.sort()
                ampersand = '&'
                data_file = open("temp2.txt", "w")
                data_file.write( code_grade[0].split('4465')[1] + ampersand +
                                code_grade[1].split('4465')[1] + ampersand +
                                code_grade[2].split('4465')[1] + ampersand +
                                code_grade[3].split('4465')[1] + ampersand +
                                code_grade[4].split('4465')[1] + ampersand +
                                code_grade[5].split('4465')[1] + ampersand +
                                code_grade[6].split('4465')[1]
                                                                            )  
                data_file.close()
                data_file.close()



                data_file = open("temp3.txt", 'w')
                data_file.write('No ERRORS, click NEXT')
                data_file.close()
                self.label4.config(text='Click NEXT', fg= 'black' )
                self.button3.place(x=460, y=330)
            
                
           
                

                
                

            def gc_get2():
                try:
                    
                    if len(goog) > 0:
                        gc_password = goog
                        configurer = webdriver.ChromeOptions()
                        configurer.add_argument("-headless")
                        #browser = webdriver.Chrome(chrome_options=configurer)
                        browser = webdriver.Chrome("C:\\Users\\inspiron\\Downloads\\chromedriver_win32\\chromedriver")
                        #browser.set_window_size(0, 0)

                        browser.get("https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&followup=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
                        WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, "//input[@class='whsOnd zHQkBf']")))
                        #time.sleep(4)
                        gc_uname = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
                        next_btn = browser.find_element_by_xpath("//div[@id='identifierNext']")
                        email_adress = u.lower() + '@student.medwayschools.org'
                        gc_uname.send_keys(email_adress)
                        next_btn.click()
                        time.sleep(2)
                        gc_password_box = browser.find_element_by_xpath("//input[@name='password']")
                        gc_password_box.send_keys(gc_password)
                        next_btn2 = browser.find_element_by_xpath("//span[@class='RveJvd snByac']")
                        next_btn2.click()
                        WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, "//h2[@class='oBSRLe']")))


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
                        return True

                    else:
                        pass
                    

                
                except:
                    pass
     
                


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
            
            threading.Thread(target = get_grades2).start()
            threading.Thread(target = gc_get2).start()

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
        #label.grid(row=7, column=2, columnspan= 2, sticky= tk.W)
        #The HOMEWORK page is no longer functional, code will be left in as it may still be useable


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
        driver = webdriver.Chrome("C:\\Users\\inspiron\\Downloads\\chromedriver_win32\\chromedriver")
        driver.get('https://medway.crportals.studentinformation.systems/')
        
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
        try:
            self.button9 = ttk.Button(self, text = " ", command= lambda: controller.show_frame(ClassSix))
        except:
            pass
        #self.button10 = ttk.Button(self, text = " ", command= lambda: controller.show_frame(ClassSeven))
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
            #self.button10.config(text='7')
            #self.button10.place(x=360,y=0)
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
        self.label = tk.Label(self, text=' ', bg= '#95c8f4', font= Large_Font)
        button1 = ttk.Button(self, text= 'Go back to graph', command= lambda: controller.show_frame(PageOne))
        button2 = ttk.Button(self,  text= 'Update Graph',  command= lambda: self.refresh2())
        self.label.pack()
        button1.pack()
        button2.pack()

    def refresh2(self):


        data_file = open("temp10.csv", 'r' )

        csv_reader = csv.reader(data_file)


        class_names = []
        for row in csv_reader:
            for item in row:
                class_names.append(item)

        graph_title = class_names[0]

        data_file.close()

        self.label.config(text= graph_title)
        


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
        self.label = tk.Label(self, text=' ', bg= '#95c8f4', font= Large_Font)
        self.label.pack()
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

        data_file = open("temp10.csv", 'r' )

        csv_reader = csv.reader(data_file)


        class_names = []
        for row in csv_reader:
            for item in row:
                class_names.append(item)

        graph_title = class_names[1]

        data_file.close()

        self.label.config(text= graph_title)

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
        self.label = tk.Label(self, text=' ', bg= '#95c8f4', font= Large_Font)
        self.label.pack()
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

        data_file = open("temp10.csv", 'r' )

        csv_reader = csv.reader(data_file)


        class_names = []
        for row in csv_reader:
            for item in row:
                class_names.append(item)

        graph_title = class_names[2]

        data_file.close()

        self.label.config(text= graph_title)

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
        self.label = tk.Label(self, text=' ', bg= '#95c8f4', font= Large_Font)
        self.label.pack()
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


        data_file = open("temp10.csv", 'r' )

        csv_reader = csv.reader(data_file)


        class_names = []
        for row in csv_reader:
            for item in row:
                class_names.append(item)

        graph_title = class_names[3]

        data_file.close()

        self.label.config(text= graph_title)

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

        button1 = ttk.Button(self, text= 'Go back to graph',  command= lambda: controller.show_frame(PageOne))
        button2 = ttk.Button(self,  text= 'Update Graph',  command= lambda: self.refresh2())
        self.label = tk.Label(self, text=' ',bg= '#95c8f4', font= Large_Font)
        self.label.pack()
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

        data_file = open("temp10.csv", 'r' )

        csv_reader = csv.reader(data_file)


        class_names = []
        for row in csv_reader:
            for item in row:
                class_names.append(item)

        graph_title = class_names[4]

        data_file.close()

        self.label.config(text= graph_title)


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

        button1 = ttk.Button(self, text= 'Go back to graph',command= lambda: controller.show_frame(PageOne))
        button2 = ttk.Button(self,  text= 'Update Graph',  command= lambda: self.refresh2())
        self.label = tk.Label(self, text=' ',bg= '#95c8f4', font= Large_Font)
        self.label.pack()
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

        data_file = open("temp10.csv", 'r' )

        csv_reader = csv.reader(data_file)


        class_names = []
        for row in csv_reader:
            for item in row:
                class_names.append(item)

        graph_title = class_names[5]

        data_file.close()

        self.label.config(text= graph_title)

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
        self.page_counter = 1
        button4 = ttk.Button(self, text= 'NEXT', command= lambda:  controller.show_frame(DisplayInDepth2) )
        button4.grid(row=1, column=4)
        '''
        button5 = ttk.Button(self, text= 'BACK', command= lambda: self.ticker_down())
        button5.grid(row=1, column=5)
        '''

    def shower(self):
        data_file = open("temp5.txt", 'r')
        loadedData1 = data_file.read()
        loadedData11 = loadedData1.split(',')
        data_file.close()
        loadedData = []
        for i in loadedData11:
            if len(i) > 1:
                loadedData.append(i)
            

        looper = 1
        loadedData111 = []
        for items in loadedData11:
            if len(items) > 1:
                loadedData111.append(items)

        for items in loadedData111[0:21]:
            #displays the assignments and the name of the classes
            looper += 1
            if "***" in items:
                tk.Label(self, text= items, bg= '#f9ee68', font= Large_Font).grid(column= 1, row=looper, sticky=  tk.E + tk.W)
            else:
                tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 1, row=looper, sticky=  tk.E + tk.W)
    
        data_file = open("temp8.txt", 'r')
        loadedData4 = data_file.read()
        loadedData44 = loadedData4.split(',')
        data_file.close() 

        looper = 1
        loadedData444 = []
        for items in loadedData44:
            loadedData444.append(items)

        for items in loadedData444[0:21]:
            looper += 1
            tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 2, row=looper, sticky=  tk.W)

        
        data_file = open("temp6.txt", 'r')
        loadedData2 = data_file.read()
        loadedData22 = loadedData2.split(',')
        data_file.close() 

        looper = 1
        loadedData222 = []
        for items in loadedData22:
            if len(items) > 0:
                loadedData222.append(items)

        for items in loadedData222[0:21]:
            if len(items)  > 0:
                looper += 1
                if "4465" in items:
                    tk.Label(self, text= '({})'.format( items.replace('4465', '') ), bg= '#f9ee68', font= Large_Font).grid(column= 3, row=looper, sticky=  tk.E + tk.W)
                else:
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 3, row=looper, sticky=  tk.E + tk.W)
        
        
        data_file = open("temp7.txt", 'r')
        loadedData3 = data_file.read()
        loadedData33 = loadedData3.split(',')
        data_file.close() 

        loadedData333 = []
        for items in loadedData33:
            if len(items) > 0:
                loadedData333.append(items)

        looper = 1
        for items in loadedData333[0:21]:
            if len(items)  > 0:
                looper += 1
                if "4465" in items:
                    tk.Label(self, text= '({})'.format( items.replace('4465', '') ), bg= '#f9ee68', font= Large_Font).grid(column= 4, row=looper, sticky=  tk.E + tk.W)
                else:
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 4, row=looper, sticky=  tk.E + tk.W)
        
        
        looper = 1
        numerator = [x.replace(" /", '0') for x in loadedData222[0:21] ]
                
        for num, denom in zip(numerator, loadedData333[0:21]):
            looper += 1
            try:
                ave = round( (float(num) / float(denom)) * 100, 2 )


                green = 100 # if grade is 100 it will be pure red
                yellow = 90 # grades at 90 will be pure yellow
                red = 85 #    grades below 85 will show as red


                if (ave < green) and (ave > yellow):

                    redValue = int( str(round( 255 * (100-ave) / 10, 0)).split('.')[0] )
                    greenValue = 255
                    blueValue = 0 

                elif (ave < yellow) and (ave > red):

                    redValue = 255
                    greenValue = int( str( round(255 - 255 * (90 - ave) / 5, 0)).split('.')[0] )
                    blueValue = 0


                elif ave == 100:
                    
                    redValue = 0
                    greenValue = 255
                    blueValue = 0
                
                elif ave == 90:
                    
                    redValue = 255
                    greenValue = 255
                    blueValue = 0

                else:

                    redValue = 255
                    greenValue = 0
                    blueValue = 0

                def rgb_2_hex(red, green, blue):
                    rgb = []
                    hexColor = []

                    rgb.append(red)
                    rgb.append(green)
                    rgb.append(blue)

                    hex_keys = {10: 'A',
                                11: 'B',
                                12: 'C',
                                13: 'D',
                                14: 'E',
                                15: 'F'}
                    
                    

                    for i in rgb:
                        x = i // 16
                        y = i % 16

                        if x > 9:
                            x = hex_keys[x]
                        if y > 9:
                            y = hex_keys[y]

                        value = str(x) + str(y)
                        hexColor.append(value)
                        
                    
                    return hexColor

                hexColor = rgb_2_hex(redValue, greenValue, blueValue)
                hexColor = "#" + hexColor[0] + hexColor[1] + hexColor[2]

                
                
                tk.Label(self, text= "({}%)".format(ave), bg= '#696969', fg= hexColor , font= Large_Font).grid(column= 5, row=looper, sticky=  tk.E + tk.W)
    
            
            except:
                tk.Label(self, text= " ", bg= '#696969', font= Large_Font).grid(column= 5, row=looper, sticky=  tk.E + tk.W)

        tk.Label(self, text= '{} Assignment(s)'.format(len(loadedData44)), font= Large_Font, bg= '#95c8f4').grid(row=1,column=1)
    
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
        self.button5.grid(row=1,column=5)
        

    def shower(self):
        data_file = open("temp5.txt", 'r')
        loadedData1 = data_file.read()
        loadedData11 = loadedData1.split(',')
        data_file.close()
        looper = 1
        loadedData111 = []
        for items in loadedData11:
            if len(items) > 0:
                loadedData111.append(items)
        if len(loadedData111) < 50:
            for items in loadedData111[21:-1]:
                looper += 1
                if "***" in items:
                    tk.Label(self, text= items, bg= '#f9ee68', font= Large_Font).grid(column= 1, row=looper, sticky=  tk.E + tk.W)
                else:
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 1, row=looper, sticky=  tk.E + tk.W)
        

            data_file = open("temp8.txt", 'r')
            loadedData4 = data_file.read()
            loadedData44 = loadedData4.split(',')
            data_file.close() 
            looper = 2
            loadedData444 = []
            for items in loadedData44:
                loadedData444.append(items)
        

            for items in loadedData444[21:-1]:
                looper += 1
                tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 2, row=looper, sticky=  tk.W)

            
            data_file = open("temp6.txt", 'r')
            loadedData2 = data_file.read()
            loadedData22 = loadedData2.split(',')
            data_file.close() 

            looper = 1
            loadedData222 = []
            for items in loadedData22:
                if len(items) > 0:
                    loadedData222.append(items)

            for items in loadedData222[21:-1]:
                if len(items)  > 0:
                    looper += 1
                    if "4465" in items:
                        tk.Label(self, text='({})'.format( items.replace('4465', '') ), bg= '#f9ee68', font= Large_Font).grid(column= 3, row=looper, sticky=  tk.E + tk.W)
                    else:
                        tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 3, row=looper, sticky=  tk.E + tk.W)
            
            
            data_file = open("temp7.txt", 'r')
            loadedData3 = data_file.read()
            loadedData33 = loadedData3.split(',')
            data_file.close() 

            loadedData333 = []
            for items in loadedData33:
                if len(items) > 0:
                    loadedData333.append(items)

            looper = 1
            for items in loadedData333[21:-1]:
                if len(items)  > 0:
                    looper += 1
                    if "4465" in items:
                        tk.Label(self, text= '({})'.format( items.replace('4465', '') ), bg= '#f9ee68', font= Large_Font).grid(column= 4, row=looper, sticky=  tk.E + tk.W)
                    else:
                        tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 4, row=looper, sticky=  tk.E + tk.W)
            
        
            looper = 1
            numerator = [x.replace(" /", '0') for x in loadedData222[21:-1] ]
                    
            for num, denom in zip(numerator, loadedData333[21:-1]):
                looper += 1
                try:
                    ave = round( (float(num) / float(denom)) * 100, 2 )


                    green = 100 # if grade is 100 it will be pure red
                    yellow = 90 # grades at 90 will be pure yellow
                    red = 85 #    grades below 85 will show as red


                    if (ave < green) and (ave > yellow):

                        redValue = int( str(round( 255 * (100-ave) / 10, 0)).split('.')[0] )
                        greenValue = 255
                        blueValue = 0 

                    elif (ave < yellow) and (ave > red):

                        redValue = 255
                        greenValue = int( str( round(255 - 255 * (90 - ave) / 5, 0)).split('.')[0] )
                        blueValue = 0


                    elif ave == 100:
                        
                        redValue = 0
                        greenValue = 255
                        blueValue = 0
                    
                    elif ave == 90:
                        
                        redValue = 255
                        greenValue = 255
                        blueValue = 0

                    else:

                        redValue = 255
                        greenValue = 0
                        blueValue = 0

                    def rgb_2_hex(red, green, blue):
                        rgb = []
                        hexColor = []

                        rgb.append(red)
                        rgb.append(green)
                        rgb.append(blue)

                        hex_keys = {10: 'A',
                                    11: 'B',
                                    12: 'C',
                                    13: 'D',
                                    14: 'E',
                                    15: 'F'}
                        
                        

                        for i in rgb:
                            x = i // 16
                            y = i % 16

                            if x > 9:
                                x = hex_keys[x]
                            if y > 9:
                                y = hex_keys[y]

                            value = str(x) + str(y)
                            hexColor.append(value)
                            
                        
                        return hexColor

                    hexColor = rgb_2_hex(redValue, greenValue, blueValue)
                    hexColor = "#" + hexColor[0] + hexColor[1] + hexColor[2]

                    
                    
                    tk.Label(self, text= "({}%)".format(ave), bg='#696969', fg= hexColor , font= Large_Font).grid(column= 5, row=looper, sticky=  tk.E + tk.W)
                except:
                        tk.Label(self, text= " ", bg= '#696969', font= Large_Font).grid(column= 5, row=looper, sticky=  tk.E + tk.W)        
        else:
            self.button5.grid(row=1, column= 5)
            data_file = open("temp5.txt", 'r')
            loadedData1 = data_file.read()
            loadedData11 = loadedData1.split(',')
            data_file.close()
            looper = 1
            loadedData444 = []

            for items in loadedData11:
                if len(items) > 0:
                    loadedData444.append(items)
            
            
            for items in loadedData444[21:41]:
                looper += 1
                if "***" in items:
                        tk.Label(self, text= items, bg= '#f9ee68', font= Large_Font).grid(column= 1, row=looper, sticky=  tk.E + tk.W)
                else:
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 1, row=looper, sticky=  tk.E + tk.W)
        
            
            data_file = open("temp6.txt", 'r')
            loadedData2 = data_file.read()
            loadedData22 = loadedData2.split(',')
            data_file.close() 

            looper = 1
            loadedData222 = []
            for items in loadedData22:
                if len(items) > 0:
                    loadedData222.append(items)

            for items in loadedData222[21:41]:
                if len(items)  > 0:
                    looper += 1
                    if "4465" in items:
                        tk.Label(self, text= '({})'.format( items.replace('4465', '') ), bg= '#f9ee68', font= Large_Font).grid(column= 3, row=looper, sticky=  tk.E + tk.W)
                    else:
                        tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 3, row=looper, sticky=  tk.E + tk.W)
            
            
            data_file = open("temp7.txt", 'r')
            loadedData3 = data_file.read()
            loadedData33 = loadedData3.split(',')
            data_file.close() 

            loadedData333 = []
            for items in loadedData33:
                if len(items) > 0:
                    loadedData333.append(items)

            looper = 1
            for items in loadedData333[21:41]:
                if len(items)  > 0:
                    looper += 1
                    if "4465" in items:
                        tk.Label(self, text= '({})'.format( items.replace('4465', '') ), bg= '#f9ee68', font= Large_Font).grid(column= 4, row=looper, sticky=  tk.E + tk.W)
                    else:
                        tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 4, row=looper, sticky=  tk.E + tk.W)
            

            data_file = open("temp8.txt", 'r')
            loadedData5 = data_file.read()
            loadedData55 = loadedData5.split(',')
            data_file.close() 

            loadedData555 = []
            for items in loadedData55:
                loadedData555.append(items)


            #changed looper to be equal to 2, might fix ghe problem of discriptions being 1 row to high ... 12/24/18
            looper = 2
            for items in loadedData555[21:41]:
                if len(items)  > 0:
                    looper += 1
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 2, row=looper, sticky=  tk.E + tk.W)
        



            looper = 1
            numerator = [x.replace(" /", '0') for x in loadedData222[21:41] ]
                    
            for num, denom in zip(numerator, loadedData333[21:41]):
                looper += 1
                try:
                    ave = round( (float(num) / float(denom)) * 100, 2 )


                    green = 100 # if grade is 100 it will be pure red
                    yellow = 90 # grades at 90 will be pure yellow
                    red = 85 #    grades below 85 will show as red


                    if (ave < green) and (ave > yellow):

                        redValue = int( str(round( 255 * (100-ave) / 10, 0)).split('.')[0] )
                        greenValue = 255
                        blueValue = 0 

                    elif (ave < yellow) and (ave > red):

                        redValue = 255
                        greenValue = int( str( round(255 - 255 * (90 - ave) / 5, 0)).split('.')[0] )
                        blueValue = 0


                    elif ave == 100:
                        
                        redValue = 0
                        greenValue = 255
                        blueValue = 0
                    
                    elif ave == 90:
                        
                        redValue = 255
                        greenValue = 255
                        blueValue = 0

                    else:

                        redValue = 255
                        greenValue = 0
                        blueValue = 0

                    def rgb_2_hex(red, green, blue):
                        rgb = []
                        hexColor = []

                        rgb.append(red)
                        rgb.append(green)
                        rgb.append(blue)

                        hex_keys = {10: 'A',
                                    11: 'B',
                                    12: 'C',
                                    13: 'D',
                                    14: 'E',
                                    15: 'F'}
                        
                        

                        for i in rgb:
                            x = i // 16
                            y = i % 16

                            if x > 9:
                                x = hex_keys[x]
                            if y > 9:
                                y = hex_keys[y]

                            value = str(x) + str(y)
                            hexColor.append(value)
                            
                        
                        return hexColor

                    hexColor = rgb_2_hex(redValue, greenValue, blueValue)
                    hexColor = "#" + hexColor[0] + hexColor[1] + hexColor[2]

                    
                    
                    tk.Label(self, text= "({}%)".format(ave), bg='#696969', fg= hexColor , font= Large_Font).grid(column= 5, row=looper, sticky=  tk.E + tk.W)
                        
                except:
                    tk.Label(self, text= " ", bg= '#696969', font= Large_Font).grid(column= 5, row=looper, sticky=  tk.E + tk.W)

class  DisplayInDepth3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)   
        button1 = ttk.Button(self, text='Go back to HOME PAGE',  command= lambda: controller.show_frame(StartPage) )
        button3 = ttk.Button(self, text= 'Show Avaliable Data', command= lambda: self.shower())
        button1.grid(row= 1, column= 2)
        button3.grid(row= 1, column= 3)
        button4 = ttk.Button(self, text= 'BACK', command= lambda: controller.show_frame(DisplayInDepth2))     
        button4.grid(row=1, column=4)
        button4 = ttk.Button(self, text= 'NEXT', command= lambda: controller.show_frame(DisplayInDepth4))     
        button4.grid(row=1, column=5)

    def shower(self):
        data_file = open("temp5.txt", 'r')
        loadedData1 = data_file.read()
        loadedData11 = loadedData1.split(',')
        data_file.close()
        looper = 1
        loadedData111 = []
        for items in loadedData11:
            if len(items) > 0:
                loadedData111.append(items)

        for items in loadedData111[41:61]:
            looper += 1
            if "***" in items:
                tk.Label(self, text= items, bg= '#f9ee68', font= Large_Font).grid(column= 1, row=looper, sticky=  tk.E + tk.W)
            else:
                tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 1, row=looper, sticky=  tk.E + tk.W)
    
        data_file = open("temp8.txt", 'r')
        loadedData4 = data_file.read()
        loadedData44 = loadedData4.split(',')
        data_file.close() 
        looper = 2
        loadedData444 = []
        for items in loadedData44:
            loadedData444.append(items)
        

        for items in loadedData444[41:61]:
            looper += 1
            tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 2, row=looper, sticky=  tk.W)

        
        data_file = open("temp6.txt", 'r')
        loadedData2 = data_file.read()
        loadedData22 = loadedData2.split(',')
        data_file.close() 

        looper = 1
        loadedData222 = []
        for items in loadedData22:
            if len(items) > 0:
                loadedData222.append(items)

        for items in loadedData222[41:61]:
            if len(items)  > 0:
                looper += 1
                if "4465" in items:
                    tk.Label(self, text= '({})'.format( items.replace('4465', '') ), bg= '#f9ee68', font= Large_Font).grid(column= 3, row=looper, sticky=  tk.E + tk.W)
                else:
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 3, row=looper, sticky=  tk.E + tk.W)
        
        
        data_file = open("temp7.txt", 'r')
        loadedData3 = data_file.read()
        loadedData33 = loadedData3.split(',')
        data_file.close() 

        loadedData333 = []
        for items in loadedData33:
            if len(items) > 0:
                loadedData333.append(items)

        looper = 1
        for items in loadedData333[41:61]:
            if len(items)  > 0:
                looper += 1
                if "4465" in items:
                    tk.Label(self, text= '({})'.format( items.replace('4465', '') ), bg= '#f9ee68', font= Large_Font).grid(column= 4, row=looper, sticky=  tk.E + tk.W)
                else:
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 4, row=looper, sticky=  tk.E + tk.W)
        
    
        looper = 1
        numerator = [x.replace(" /", '0') for x in loadedData222[41:61] ]
                
        for num, denom in zip(numerator, loadedData333[41:61]):
            looper += 1
            try:
                ave = round( (float(num) / float(denom)) * 100, 2 )


                green = 100 # if grade is 100 it will be pure red
                yellow = 90 # grades at 90 will be pure yellow
                red = 85 #    grades below 85 will show as red


                if (ave < green) and (ave > yellow):

                    redValue = int( str(round( 255 * (100-ave) / 10, 0)).split('.')[0] )
                    greenValue = 255
                    blueValue = 0 

                elif (ave < yellow) and (ave > red):

                    redValue = 255
                    greenValue = int( str( round(255 - 255 * (90 - ave) / 5, 0)).split('.')[0] )
                    blueValue = 0


                elif ave == 100:
                    
                    redValue = 0
                    greenValue = 255
                    blueValue = 0
                
                elif ave == 90:
                    
                    redValue = 255
                    greenValue = 255
                    blueValue = 0

                else:

                    redValue = 255
                    greenValue = 0
                    blueValue = 0

                def rgb_2_hex(red, green, blue):
                    rgb = []
                    hexColor = []

                    rgb.append(red)
                    rgb.append(green)
                    rgb.append(blue)

                    hex_keys = {10: 'A',
                                11: 'B',
                                12: 'C',
                                13: 'D',
                                14: 'E',
                                15: 'F'}
                    
                    

                    for i in rgb:
                        x = i // 16
                        y = i % 16

                        if x > 9:
                            x = hex_keys[x]
                        if y > 9:
                            y = hex_keys[y]

                        value = str(x) + str(y)
                        hexColor.append(value)
                        
                    
                    return hexColor

                hexColor = rgb_2_hex(redValue, greenValue, blueValue)
                hexColor = "#" + hexColor[0] + hexColor[1] + hexColor[2]

                
                
                tk.Label(self, text= "({}%)".format(ave), bg='#696969', fg= hexColor , font= Large_Font).grid(column= 5, row=looper, sticky=  tk.E + tk.W)

            except:
                tk.Label(self, text= " ", bg= '#696969', font= Large_Font).grid(column= 5, row=looper, sticky=  tk.E + tk.W)

class DisplayInDepth4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button1 = ttk.Button(self, text='Go back to HOME PAGE',  command= lambda: controller.show_frame(StartPage) )
        button3 = ttk.Button(self, text= 'Show Avaliable Data', command= lambda: self.shower())
        button1.grid(row= 1, column= 2)
        button3.grid(row= 1, column= 3)
        button4 = ttk.Button(self, text= 'BACK', command= lambda: controller.show_frame(DisplayInDepth3))     
        button4.grid(row=1, column=4)

    def shower(self):
        data_file = open("temp5.txt", 'r')
        loadedData1 = data_file.read()
        loadedData11 = loadedData1.split(',')
        data_file.close()
        looper = 1
        loadedData111 = []
        for items in loadedData11:
            if len(items) > 0:
                loadedData111.append(items)

        for items in loadedData111[61:81]:
            looper += 1
            if "***" in items:
                tk.Label(self, text= items, bg= '#f9ee68', font= Large_Font).grid(column= 1, row=looper, sticky=  tk.E + tk.W)
            else:
                tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 1, row=looper, sticky=  tk.E + tk.W)
    
        data_file = open("temp8.txt", 'r')
        loadedData4 = data_file.read()
        loadedData44 = loadedData4.split(',')
        data_file.close() 
        looper = 2
        loadedData444 = []
        for items in loadedData44:
            loadedData444.append(items)
        

        for items in loadedData444[61:81]:
            looper += 1
            tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 2, row=looper, sticky=  tk.W)

        
        data_file = open("temp6.txt", 'r')
        loadedData2 = data_file.read()
        loadedData22 = loadedData2.split(',')
        data_file.close() 

        looper = 1
        loadedData222 = []
        for items in loadedData22:
            if len(items) > 0:
                loadedData222.append(items)

        for items in loadedData222[61:81]:
            if len(items)  > 0:
                looper += 1
                if "4465" in items:
                    tk.Label(self, text= '({})'.format( items.replace('4465', '') ), bg= '#f9ee68', font= Large_Font).grid(column= 3, row=looper, sticky=  tk.E + tk.W)
                else:
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 3, row=looper, sticky=  tk.E + tk.W)
        
        
        data_file = open("temp7.txt", 'r')
        loadedData3 = data_file.read()
        loadedData33 = loadedData3.split(',')
        data_file.close() 

        loadedData333 = []
        for items in loadedData33:
            if len(items) > 0:
                loadedData333.append(items)

        looper = 1
        for items in loadedData333[61:81]:
            if len(items)  > 0:
                looper += 1
                if "4465" in items:
                    tk.Label(self, text= '({})'.format( items.replace('4465', '') ), bg= '#f9ee68', font= Large_Font).grid(column= 4, row=looper, sticky=  tk.E + tk.W)
                else:
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 4, row=looper, sticky=  tk.E + tk.W)
        
    
        looper = 1
        numerator = [x.replace(" /", '0') for x in loadedData222[61:81] ]
                
        for num, denom in zip(numerator, loadedData333[61:81]):
            looper += 1
            try:
                ave = round( (float(num) / float(denom)) * 100, 2 )


                green = 100 # if grade is 100 it will be pure red
                yellow = 90 # grades at 90 will be pure yellow
                red = 85 #    grades below 85 will show as red


                if (ave < green) and (ave > yellow):

                    redValue = int( str(round( 255 * (100-ave) / 10, 0)).split('.')[0] )
                    greenValue = 255
                    blueValue = 0 

                elif (ave < yellow) and (ave > red):

                    redValue = 255
                    greenValue = int( str( round(255 - 255 * (90 - ave) / 5, 0)).split('.')[0] )
                    blueValue = 0


                elif ave == 100:
                    
                    redValue = 0
                    greenValue = 255
                    blueValue = 0
                
                elif ave == 90:
                    
                    redValue = 255
                    greenValue = 255
                    blueValue = 0

                else:

                    redValue = 255
                    greenValue = 0
                    blueValue = 0

                def rgb_2_hex(red, green, blue):
                    rgb = []
                    hexColor = []

                    rgb.append(red)
                    rgb.append(green)
                    rgb.append(blue)

                    hex_keys = {10: 'A',
                                11: 'B',
                                12: 'C',
                                13: 'D',
                                14: 'E',
                                15: 'F'}
                    
                    

                    for i in rgb:
                        x = i // 16
                        y = i % 16

                        if x > 9:
                            x = hex_keys[x]
                        if y > 9:
                            y = hex_keys[y]

                        value = str(x) + str(y)
                        hexColor.append(value)
                        
                    
                    return hexColor

                hexColor = rgb_2_hex(redValue, greenValue, blueValue)
                hexColor = "#" + hexColor[0] + hexColor[1] + hexColor[2]

                
                
                tk.Label(self, text= "({}%)".format(ave), bg='#696969', fg= hexColor , font= Large_Font).grid(column= 5, row=looper, sticky=  tk.E + tk.W)  
            except:
                tk.Label(self, text= " ", bg= '#696969', font= Large_Font).grid(column= 5, row=looper, sticky=  tk.E + tk.W)

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
            loadedData1 = data_file.read()
            loadedData11 = loadedData1.split('***')
            dates = loadedData11[0].split(',')
            hws = loadedData11[1].split('^^')
            data_file.close()

            looper = 1
            for items in dates:
                looper += 1
                tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 1, row=looper, sticky=  tk.E + tk.W)
            
            looper = 1 
            for items in hws:
                looper += 1
                if len(items) < 50:
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 2, row=looper, sticky=  tk.W)
                else:
                    i = items[0:50] + '...'
                    tk.Label(self, text= items, bg= '#95c8f4', font= Large_Font).grid(column= 2, row=looper, sticky=  tk.W)
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
