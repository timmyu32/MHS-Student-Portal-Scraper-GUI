from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from functools import reduce as reducer
from datetime import date as date

options = webdriver.ChromeOptions()

options.add_argument("-headless")
driver = webdriver.Chrome(chrome_options=options)



driver.get('https://www.mms669.org/MMSGB45/default.aspx?ReturnUrl=%2fMMSGB45%2fstudent')
uname = driver.find_element_by_name('LoginControl1$txtUsername')
password = driver.find_element_by_name('LoginControl1$txtPassword')
login_btn = driver.find_element_by_name('LoginControl1$btnLogin')


uname.send_keys('Tuzoegbu')
password.send_keys('Cheeze10')
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
    data11y = [x for x.split('@')[0] in data11]
    data11x = [x for x.split('@')[1] in data11]
    data_1.close()
except:
    pass

try:
    data_2 = open("C:\\Users\\click\\Downloads\\T\\two.txt", "r")
    data22 = data_2.read().split(',')
    data22y = [x for x.split('@')[0] in data22]
    data22x = [x for x.split('@')[1] in data22]
    data_2.close()
except:
    pass

try:
    data_3 = open("C:\\Users\\click\\Downloads\\T\\three.txt", "r")
    data33 = data_3.read().split(',')
    data33y = [x for x.split('@')[0] in data33]
    data33x = [x for x.split('@')[1] in data33]
    data_3.close()
except:
    pass

try:
    data_4 = open("C:\\Users\\click\\Downloads\\T\\four.txt", "r")
    data44 = data_4.read().split(',')
    data44y = [x for x.split('@')[0] in data44]
    data44x = [x for x.split('@')[1] in data44]
    data_4.close()
except:
    pass
try:    
    data_5 = open("C:\\Users\\click\\Downloads\\T\\five.txt", "r")
    data55 = data_5.read().split(',')
    data55y = [x for x.split('@')[0] in data55]
    data55x = [x for x.split('@')[1] in data55]
    data_5.close()
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
            y_value = float(valuer)
            data66y.append(value)
        x_valuer = items.split('@')[1]
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
            y_value = float(valuer)
            data77y.append(value)
        x_valuer = items.split('@')[1]
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
            y_value = float(valuer)
            avg_data1y.append(value)
        x_valuer = items.split('@')[1]
        if len(x_valuer) > 1:
            avg_data1x.append(x_valuer)
except:
    pass


