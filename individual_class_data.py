from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import functools
import time

def alternate(a,b):
    options = webdriver.ChromeOptions()

    options.add_argument("-headless")
    driver = webdriver.Chrome(chrome_options=options)
    #driver = webdriver.Chrome()

    driver.get('https://www.mms669.org/MMSGB45/default.aspx?ReturnUrl=%2fMMSGB45%2fstudent')
    uname = driver.find_element_by_name('LoginControl1$txtUsername')
    password = driver.find_element_by_name('LoginControl1$txtPassword')
    login_btn = driver.find_element_by_name('LoginControl1$btnLogin')

    uname.clear()
    password.clear()
    uname.send_keys(a)
    password.send_keys(b)
    login_btn.click()
    time.sleep(1)

    try:
        error_msg = driver.find_element_by_xpath("//span[@id='LoginControl1_lblErrMsg']").text
        if type(error_msg) != None:
            data_file = open("temp3.txt", 'w')
            data_file.write(error_msg)
            data_file.close()        
    except:
        pass


    timeout = 4.6
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='rgMasterTable rgClipCells']")))
    except:
        driver.close()

    class_names1 = driver.find_elements_by_xpath("//tr[@class='rgRow']")
    evens = [x.text for x in class_names1]

    class_names2 = driver.find_elements_by_xpath("//tr[@class='rgAltRow']")
    odds = [x.text for x in class_names2]

    code_grade = []
    all_class_codes = driver.find_elements_by_xpath("//td[@style='background-color:White;width:95px;']")
    class_codes = [x.text for x in all_class_codes]
    global denominator
    denominator = []

    ids = []
    id_descriptors = []
    grdr = []
    grdr2 = []
    grdr3 = []

    numero = len(driver.find_elements_by_xpath("//td[@style= 'background-color:White;width:145px;']"))

    for links in driver.find_elements_by_xpath("//td[@style= 'background-color:White;width:145px;']"):
        try:
            links.click()
            
            try:
                driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id= 'ctl00_ContentPlaceHolder1_ReportViewer1ReportFrame']"))
                class_identifiers = [x.text for x in driver.find_elements_by_xpath("//div[@class='HtmlTextBox2 s22-']")]
                if len(class_identifiers) > 0:
                    ids.append(class_identifiers)
                    descriptor = [x.text.replace('\n',  ' ') for x in driver.find_elements_by_xpath("//div[@class='TextBox41 s28-']") ]
                    if len(descriptor) > 0:
                        id_descriptors.append(descriptor)
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
                numero += -1
                print("Error, click method imposed on item that is not a class")
                
        except:
            try:
                links = driver.find_elements_by_xpath("//td[@style= 'background-color:White;width:145px;']")[numero]
                links.click()
                                
                try:
                    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id= 'ctl00_ContentPlaceHolder1_ReportViewer1ReportFrame']"))
                    class_identifiers = [x.text for x in driver.find_elements_by_xpath("//div[@class='HtmlTextBox2 s22-']")]
                    if len(class_identifiers) > 0:
                        ids.append(class_identifiers)
                        descriptor = [x.text.replace('\n',  ' ') for x in driver.find_elements_by_xpath("//div[@class='TextBox41 s28-']") ]
                        if len(descriptor) >0:
                            id_descriptors.append(descriptor)
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
                    print('Error, click method imposed on item that is not a class')
                    numero += -1
            except:
                pass


    tabs = driver.find_elements_by_class_name("rmItem")
    hisstorical_grades_tab = tabs[7]

    loggout = driver.find_element_by_xpath("//div[@id='SignOutHolder']")
    hover = ActionChains(driver).move_to_element(loggout)
    hover.perform()
    time.sleep(1)

    studentName = driver.find_elements_by_xpath("//a[@class='rmLink']")[0].text[0:-9]
    data_file = open("temp4.txt", "w")
    data_file.write(studentName)
    data_file.close()

    hover = ActionChains(driver).move_to_element(hisstorical_grades_tab)
    hover.perform()
    time.sleep(1)

    report_card = driver.find_elements_by_xpath("//span[@class='rmText']")[5]
    report_card.click()
    time.sleep(1.5)
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id= 'ctl00_ContentPlaceHolder1_ReportViewer3ReportFrame']"))

    class_name_coullumn = driver.find_elements_by_xpath("//div[@class='TextBox87 s8-']")
    class_name_coullumn = [x.text for x in class_name_coullumn]

    grade_collumn1 = driver.find_elements_by_xpath("//div[@class='TextBox93 s9-']")
    grade_collumn1 = [x.text for x in grade_collumn1]
    grade_collumn2 = driver.find_elements_by_xpath("//div[@class='TextBox107 s9-']")
    grade_collumn2 = [x.text for x in grade_collumn2]
    grade_collumn3 = driver.find_elements_by_xpath("//div[@class='TextBox112 s9-']")
    grade_collumn3 = [x.text for x in grade_collumn3]

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
        class1 = evens[0]
        class1_g = class1.split(",")
        class1_grade = float(class1_g[1].split(')')[0].split('(')[1])
        if class1_grade == 100.0:
            class1_grade = 100
        denominator.append(class1_grade)
    except:
        class1_grade = 0
    try:
        class2 = odds[0]
        class2_g = class2.split(",")
        class2_grade = float(class2_g[1].split(')')[0].split('(')[1])
        if class2_grade == 100.0:
            class2_grade = 100
        denominator.append(class2_grade)         
    except:
        class2_grade = 0
    try:
        class3 = evens[1]
        class3_g = class3.split(",")
        class3_grade = float(class3_g[1].split(')')[0].split('(')[1])   
        if class3_grade == 100.0:
            class3_grade = 100 
        denominator.append(class3_grade)   
    except:
        class3_grade = 0
    try:
        class4 = odds[1]
        class4_g = class4.split(",")
        class4_grade = float(class4_g[1].split(')')[0].split('(')[1])   
        if class4_grade == 100.0:
            class4_grade = 100 
        denominator.append(class4_grade)   
    except:
        class4_grade = 0
    try:
        class5 = evens[2]
        class5_g = class5.split(",")
        class5_grade = float(class5_g[1].split(')')[0].split('(')[1])    
        if class5_grade == 100.0:
            class5_grade = 100
        denominator.append(class5_grade)   
    except:
        class5_grade = 0
    try:
        class6 = odds[2]
        class6_g = class6.split(",")
        class6_grade = float(class6_g[1].split(')')[0].split('(')[1])    
        if class6_grade == 100.0:
            class6_grade = 100
        denominator.append(class6_grade)  
    except:
        class6_grade = 0
    try:
        class7 = evens[3]
        class7_g = class7.split(",")
        class7_grade = float(class7_g[1].split(')')[0].split('(')[1])    
        if class7_grade == 100.0:
            class7_grade = 100
        denominator.append(class7_grade)   
    except:
        class7_grade = 0
    try:
        class8 = odds[3]
        class8_g = class8.split(",")
        class8_grade = float(class8_g[1].split(')')[0].split('(')[1])   
        if class8_grade == 100.0:
            class8_grade = 100
        denominator.append(class8_grade)  
    except:
        class8_grade = 0
    try:
        class9 = evens[4]
        class9_g = class9.split(",")
        class9_grade = float(class9_g[1].split(')')[0].split('(')[1])    
        if class9_grade == 100.0:
            class9_grade = 100
        denominator.append(class9_grade)  
    except:
        class9_grade = 0
    try:
        class10 = odds[4]
        class10_g = class10.split(",")
        class10_grade = float(class10_g[1].split(')')[0].split('(')[1])  
        if class10_grade == 100.0:
            class10_grade = 100
        denominator.append(class10_grade)  
    except:
        class10_grade = 0


    try:
        class1_code = class_codes[0]
        class1_name = class1.split(class1_code)[0]
        code_grade.append( str(class1_code) + '4465' + str(class1_grade) )
    except:
        pass
    try:
        class2_code = class_codes[1]
        class2_name = class2.split(class2_code)[0]
        code_grade.append( str(class2_code) + '4465' + str(class2_grade) )
    except:
        pass
    try:
        class3_code = class_codes[2]
        class3_name = class3.split(class3_code)[0]
        code_grade.append( str(class3_code) + '4465' + str(class3_grade) )
    except:
        pass
    try:
        class4_code = class_codes[3]
        class4_name = class4.split(class4_code)[0]
        code_grade.append( str(class4_code) + '4465' + str(class4_grade) )
    except:
        pass
    try:
        class5_code = class_codes[4]
        class5_name = class5.split(class5_code)[0]
        code_grade.append( str(class5_code) + '4465' + str(class5_grade) )
    except:
        pass
    try:
        class6_code = class_codes[5]
        class6_name = class6.split(class6_code)[0]
        code_grade.append( str(class6_code) + '4465' + str(class6_grade) )
    except:
        pass
    try:
        class7_code = class_codes[6]
        class7_name = class7.split(class7_code)[0]
        code_grade.append( str(class7_code) + '4465' + str(class7_grade) )
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

