import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style

import tkinter as tk
from tkinter import ttk

from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from functools import reduce as reducer
from datetime import date as date

from PIL import Image, ImageTk


options = webdriver.ChromeOptions()

options.add_argument("-headless")
driver = webdriver.Chrome(chrome_options=options)



driver.get('https://www.mms669.org/MMSGB45/default.aspx?ReturnUrl=%2fMMSGB45%2fstudent')
uname = driver.find_element_by_name('LoginControl1$txtUsername')
password = driver.find_element_by_name('LoginControl1$txtPassword')
login_btn = driver.find_element_by_name('LoginControl1$btnLogin')


uname.send_keys(
            #username
                )
password.send_keys(
                #password
                    )
login_btn.click()


timeout = 10
WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='rgMasterTable rgClipCells']")))

class_names1 = driver.find_elements_by_xpath("//tr[@class='rgRow']")
evens = [x.text for x in class_names1]

class_names2 = driver.find_elements_by_xpath("//tr[@class='rgAltRow']")
odds = [x.text for x in class_names2]

all_class_codes = driver.find_elements_by_xpath("//td[@style='background-color:White;width:95px;']")
class_codes = [x.text for x in all_class_codes]

driver.close()

today = str(date.today())

denominator = []

try:
    class1 = evens[0]
    class1_g = class1.split(",")
    class1_grade = float(class1_g[1].split(')')[0].split('(')[1]) 
    denominator.append(class1_grade)
    data_file = open("C:\\Users\\click\\Downloads\\T\\one.txt", "a")
    data_file.write(str(class1_grade) +'@'+today +',')    
    data_file.close()    
except:
    class1_grade = None
try:
    class2 = odds[0]
    class2_g = class2.split(",")
    class2_grade = float(class2_g[1].split(')')[0].split('(')[1])
    denominator.append(class2_grade)
    data_file = open("C:\\Users\\click\\Downloads\\T\\two.txt", "a")
    data_file.write(str(class2_grade) +'@'+today +',')
    data_file.close()          
except:
    class2_grade = None
try:
    class3 = evens[1]
    class3_g = class3.split(",")
    class3_grade = float(class3_g[1].split(')')[0].split('(')[1])    
    denominator.append(class3_grade) 
    data_file = open("C:\\Users\\click\\Downloads\\T\\three.txt", "a")
    data_file.write(str(class3_grade) +'@'+today +',')
    data_file.close()  
except:
    class3_grade = None
try:
    class4 = odds[1]
    class4_g = class4.split(",")
    class4_grade = float(class4_g[1].split(')')[0].split('(')[1])    
    denominator.append(class4_grade) 
    data_file = open("C:\\Users\\click\\Downloads\\T\\four.txt", "a")
    data_file.write(str(class4_grade) +'@'+today +',')
    data_file.close()  
except:
    class4_grade = None
try:
    class5 = evens[2]
    class5_g = class5.split(",")
    class5_grade = float(class5_g[1].split(')')[0].split('(')[1])    
    denominator.append(class5_grade)  
    data_file = open("C:\\Users\\click\\Downloads\\T\\five.txt", "a")
    data_file.write(str(class5_grade) +'@'+today +',')
    data_file.close() 
except:
    class5_grade = None
try:
    class6 = odds[2]
    class6_g = class6.split(",")
    class6_grade = float(class6_g[1].split(')')[0].split('(')[1])    
    denominator.append(class6_grade)  
    data_file = open("C:\\Users\\click\\Downloads\\T\\six.txt", "a")
    data_file.write(str(class6_grade) +'@'+today +',')
    data_file.close() 
except:
    class6_grade = None
try:
    class7 = evens[3]
    class7_g = class7.split(",")
    class7_grade = float(class7_g[1].split(')')[0].split('(')[1])    
    denominator.append(class7_grade)  
    data_file = open("C:\\Users\\click\\Downloads\\T\\seven.txt", "a")
    data_file.write(str(class7_grade) +'@'+today +',')
    data_file.close() 
except:
    class7_grade = None
try:
    class8 = odds[3]
    class8_g = class8.split(",")
    class8_grade = float(class8_g[1].split(')')[0].split('(')[1])   
    denominator.append(class8_grade)  
except:
    class8_grade = None
try:
    class9 = evens[4]
    class9_g = class9.split(",")
    class9_grade = float(class9_g[1].split(')')[0].split('(')[1])    
    denominator.append(class9_grade)  
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
    class1_code = class_codes[0]
    class1_name = class1.split(class1_code)[0]
except:
    pass
try:
    class2_code = class_codes[1]
    class2_name = class2.split(class2_code)[0]
except:
    pass
try:
    class3_code = class_codes[2]
    class3_name = class3.split(class3_code)[0]
except:
    pass
try:
    class4_code = class_codes[3]
    class4_name = class4.split(class4_code)[0]
except:
    pass
try:
    class5_code = class_codes[4]
    class5_name = class5.split(class5_code)[0]
except:
    pass
try:
    class6_code = class_codes[5]
    class6_name = class6.split(class6_code)[0]
except:
    pass
try:
    class7_code = class_codes[6]
    class7_name = class7.split(class7_code)[0]
except:
    pass
try:
    class8_code = class_codes[7]
    class8_name = class8.split(class8_code)[0]
except:
    pass
try:
    class9_code = class_code[8]
    class9_name = class9.split(class9_code)[0]
except:
    pass
try:
    class10_code = class_codes[9]
    class10_name = class10.split(class10_code)[0]
except:
    pass

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
    data_1 = open("C:\\Users\\click\\Downloads\\T\\one.txt", "r")
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
    data_2 = open("C:\\Users\\click\\Downloads\\T\\two.txt", "r")
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
    data_3 = open("C:\\Users\\click\\Downloads\\T\\three.txt", "r")
    data33 = data_3.read().split(',')
    data_3.close()

    data33y = []
    data44x = []

    for items in data33:
        y_valuer = items.split('@')[0]
        if len(y_valuer) > 1:
            y_value = float(y_valuer)
            data33y.append(y_value)
        x_valuer = items.split('@')[-1]
        if len(x_valuer) > 1:
            data44x.append(x_valuer)
except:
    pass

try:
    data_4 = open("C:\\Users\\click\\Downloads\\T\\four.txt", "r")
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
    data_5 = open("C:\\Users\\click\\Downloads\\T\\five.txt", "r")
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
    data_6 = open("C:\\Users\\click\\Downloads\\T\\six.txt", "r")
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
    data_7 = open("C:\\Users\\click\\Downloads\\T\\seven.txt", "r")
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

try:
    data_file = open("C:\\Users\\click\\Downloads\\T\\avg.txt", "a")
    data_file.write(str(average)+ '@'+ today + ',')
    data_file.close()
    avg_data = open("C:\\Users\\click\\Downloads\\T\\avg.txt", "r")
    avg_data1 = avg_data.read().split(',')

    avg_data1y = []
    avg_data1x = []

    for items in avg_data1:
        y_valuer = items.split('@')[0]
        if len(y_valuer) > 1:
            y_value = float(y_valuer)
            avg_data1y.append(y_value)
        x_valuer = items.split('@')[-1]
        if len(x_valuer) > 1:
            avg_data1x.append(x_valuer)
except:
    pass

Largest_Font = ("Times New Roman", "16")
Large_Font = ("Times New Roman", "12")
smaller_font = ("Times New Roman", "9")
smallest_font = ("Times New Roman", "7")
style.use("ggplot")
title = "Tim Uzoegbu GRADES Graph\n Avg= "+str(average)

f = Figure(figsize = (10,5), dpi=100)
g = Figure(figsize = (5,5), dpi=100)
a = f.add_subplot(111)
b = g.add_subplot(111)
b.pie(denominator)
a.set_title(title)


try:    
    a.plot(avg_data1x, avg_data1y, label= 'Average')
except:
    pass

try:    
    a.plot(data11x, data11y, "#ED1F11", label= class1_name)
except:
    pass

try:    
    a.plot(data22x, data22y, "#010101", label= class2_name)
except:
    pass

try:    
    a.plot(data33x, data33y, "#7628B4", laabel= class3_name)
except:
    pass

try:    
    a.plot(data44x, data44y, "#29A223", label= class4_name)
except:
    pass

try:    
    a.plot(data55x, data55y, "#2E3ACA", label= class5_name)
except:
    pass

try:    
    a.plot(data66x, data66y, "#FF8CEC", label= class6_name)
except:
    pass

try:    
    a.plot(data77x, data77y, "#F5891C", label= class7_name)
except:
    pass

a.legend()

class GradeGetterApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="gradealert.ico")
        tk.Tk.wm_title(self, "Grade Getter for MHS studets")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand="true")
        container.grid_rowconfigure(0, weight= 1)
        container.grid_columnconfigure(0, weight= 1)

        self.frames = {}
        
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.configure(background= "#95c8f4")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text= 'Welcome to the MHS Live Student Portal graph for data visualization created by T.U. .', font= Largest_Font, background= "#95c8f4")
        label1.pack()
        label2 = tk.Label(self, text= 'This program can be used to plot the course of you courses over a month, semester, or even a year!\nLets get started...', font= smaller_font, background= "#95c8f4")
        label2.pack()
        button1 = ttk.Button(self, text= 'Go to Student Portal Class Data Graph', command= lambda: controller.show_frame(PageOne))
        button1.pack()
        button2 = ttk.Button(self, text= 'Go to Class Data Pie Chart', command= lambda: controller.show_frame(PageTwo))
        button2.pack()
        button3 = ttk.Button(self, text= "Quit App", command= quit)
        button3.pack()
        self.showImg()
        self.showGrade()


    def showGrade(self):
        lab = tk.Label(self, text = class1_name , bg ="#95c8f4", font = smaller_font )       
        lab1 = tk.Label(self, text = class2_name , bg ="#95c8f4", font = smaller_font)
        lab2= tk.Label(self, text = class3_name , bg ="#95c8f4",font = smaller_font )
        lab3 = tk.Label(self, text = class4_name , bg ="#95c8f4", font = smaller_font )
        lab4 = tk.Label(self, text = class5_name , bg ="#95c8f4",font = smaller_font )
        lab5 = tk.Label(self, text = class6_name , bg ="#95c8f4",font = smaller_font )
        lab6 = tk.Label(self, text = class6_name , bg ="#95c8f4",font = smaller_font )
        lab7 = tk.Label(self, text = "Average" , bg ="#95c8f4",font = smaller_font )

        lab0 = tk.Label(self, text = class1_grade , bg ="#95c8f4", font = smaller_font )       
        lab11 = tk.Label(self, text = class2_grade , bg ="#95c8f4", font = smaller_font)
        lab22 = tk.Label(self, text = class3_grade , bg ="#95c8f4",font = smaller_font )
        lab33 = tk.Label(self, text = class4_grade , bg ="#95c8f4", font = smaller_font )
        lab44 = tk.Label(self, text = class5_grade , bg ="#95c8f4",font = smaller_font )
        lab55 = tk.Label(self, text = class6_grade , bg ="#95c8f4",font = smaller_font )
        lab66 = tk.Label(self, text = class6_grade , bg ="#95c8f4",font = smaller_font )
        


        lab.pack(expand= True)
        lab0.pack(expand= True)
        lab1.pack(expand= True)
        lab11.pack(expand= True)
        lab2.pack(expand= True)
        lab22.pack(expand= True)
        lab3.pack(expand= True)
        lab33.pack(expand= True)
        lab4.pack(expand= True)
        lab44.pack(expand= True)
        lab5.pack(expand= True)
        lab55.pack(expand= True)
        lab6.pack(expand= True)
        lab66.pack(expand= True)
        
        

    def showImg(self):
        load = Image.open("home_img.jpg")
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image= render)
        img.image = render
        img.pack()



class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  

        label1 = ttk.Label(self, text= "Graph Page", font= Large_Font, background= "#95c8f4")
        label1.pack()
        button1 = ttk.Button(self, text= 'Go back to HOME PAGE', command= lambda: controller.show_frame(StartPage))
        button1.pack()
       
       
 

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side= tk.TOP, fill= tk.BOTH, expand= True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side= tk.TOP, fill= tk.BOTH, expand= True)
  





class PageTwo(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  

        label = tk.Label(self, text= 'Still in BETA...', font= Largest_Font)
        button1 = ttk.Button(self, text= 'Go back to HOME PAGE', command= lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text= 'Go to Student Portal Class Data Graph', command= lambda: controller.show_frame(PageOne))
        button2.pack()
        label.pack()

        
        '''
        canvas = FigureCanvasTkAgg(g, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side= tk.TOP, fill= tk.BOTH, expand= True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side= tk.TOP, fill= tk.BOTH, expand= True)
        '''
        
  


app = GradeGetterApp()
app.mainloop()