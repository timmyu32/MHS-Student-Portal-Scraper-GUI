from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import functools
import time





options = webdriver.ChromeOptions()

options.add_argument("-headless")
#driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome()


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

denominator = []

try:
    class1 = evens[0]
    class1_g = class1.split(",")
    class1_grade = float(class1_g[1].split(')')[0].split('(')[1]) 
    denominator.append(class1_grade)
    data_file = open("C:\\Users\\click\\Downloads\\T\\one.txt", "a")
    data_file.write(str(class1_grade) +',')    
    data_file.close()    
except:
    class1_grade = None
try:
    class2 = odds[0]
    class2_g = class2.split(",")
    class2_grade = float(class2_g[1].split(')')[0].split('(')[1])
    denominator.append(class2_grade)
    data_file = open("C:\\Users\\click\\Downloads\\T\\two.txt", "a")
    data_file.write(str(class2_grade) +',')
    data_file.close()          
except:
    class2_grade = None
try:
    class3 = evens[1]
    class3_g = class3.split(",")
    class3_grade = float(class3_g[1].split(')')[0].split('(')[1])    
    denominator.append(class3_grade) 
    data_file = open("C:\\Users\\click\\Downloads\\T\\three.txt", "a")
    data_file.write(str(class3_grade) +',')
    data_file.close()  
except:
    class3_grade = None
try:
    class4 = odds[1]
    class4_g = class4.split(",")
    class4_grade = float(class4_g[1].split(')')[0].split('(')[1])    
    denominator.append(class4_grade) 
    data_file = open("C:\\Users\\click\\Downloads\\T\\four.txt", "a")
    data_file.write(str(class4_grade) +',')
    data_file.close()  
except:
    class4_grade = None
try:
    class5 = evens[2]
    class5_g = class5.split(",")
    class5_grade = float(class5_g[1].split(')')[0].split('(')[1])    
    denominator.append(class5_grade)  
    data_file = open("C:\\Users\\click\\Downloads\\T\\five.txt", "a")
    data_file.write(str(class5_grade) +',')
    data_file.close() 
except:
    class5_grade = None
try:
    class6 = odds[2]
    class6_g = class6.split(",")
    class6_grade = float(class6_g[1].split(')')[0].split('(')[1])    
    denominator.append(class6_grade)  
    data_file = open("C:\\Users\\click\\Downloads\\T\\six.txt", "a")
    data_file.write(str(class6_grade) +',')
    data_file.close() 
except:
    class6_grade = None
try:
    class7 = evens[3]
    class7_g = class7.split(",")
    class7_grade = float(class7_g[1].split(')')[0].split('(')[1])    
    denominator.append(class7_grade)  
    data_file = open("C:\\Users\\click\\Downloads\\T\\seven.txt", "a")
    data_file.write(str(class7_grade) +',')
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
    n = functools.reduce(lambda x,y: x+y, denominator)
except:
    pass

try:
    average = round(n/d, 2)
except:
    pass

try:
    data_1 = open("C:\\Users\\click\\Downloads\\T\\one.txt", "r")
    data11 = float(data_1.read().split(',')[-3])
    data_1.close()
except:
    pass

try:
    data_2 = open("C:\\Users\\click\\Downloads\\T\\two.txt", "r")
    data22 = float(data_2.read().split(',')[-3])
    data_2.close()
except:
    pass

try:
    data_3 = open("C:\\Users\\click\\Downloads\\T\\three.txt", "r")
    data33 = float(data_3.read().split(',')[-3])
    data_3.close()
except:
    pass

try:
    data_4 = open("C:\\Users\\click\\Downloads\\T\\four.txt", "r")
    data44 = float(data_4.read().split(',')[-3])
    data_4.close()
except:
    pass
try:    
    data_5 = open("C:\\Users\\click\\Downloads\\T\\five.txt", "r")
    data55 = float(data_5.read().split(',')[-3])
    data_5.close()
except:
    pass

try:  
    data_6 = open("C:\\Users\\click\\Downloads\\T\\six.txt", "r")
    data66 = float(data_6.read().split(',')[-3])
    data_6.close()
except:
    pass

try:
    data_7 = open("C:\\Users\\click\\Downloads\\T\\seven.txt", "r")
    data77 = float(data_7.read().split(',')[-3])
    data_7.close()
except:
    pass

try:
    data_file = open("C:\\Users\\click\\Downloads\\T\\avg.txt", "a")
    data_file.write(str(average)+ ',')
    data_file.close()
    avg_data = open("C:\\Users\\click\\Downloads\\T\\avg.txt", "r")
    avg_data1 = float(avg_data.read().split(',')[-3])
    avg_data.close()
except:
    pass

def good_bad(last_grade, current_grade):
    if last_grade == current_grade:
        print('+0')
    elif current_grade > last_grade:
        print('+', str(round((current_grade - last_grade), 2)))
    elif current_grade < last_grade:
        print('-', str(round((last_grade - current_grade), 2)))

#print statements
print(class1_name, class1_grade)
try:
    good_bad(data11, class1_grade)
except:
    pass
print(class2_name, class2_grade)
try:
    good_bad(data22, class2_grade)
except:
    pass
print(class3_name, class3_grade)
try:
    good_bad(data33, class3_grade)
except:
    pass
print(class4_name, class4_grade)
try:
    good_bad(data44, class4_grade)
except:
    pass
print(class5_name, class5_grade)
try:
    good_bad(data55, class5_grade)
except:
    pass
print(class6_name, class6_grade)
try:
    good_bad(data66, class6_grade)
except:
    pass
print(class7_name, class7_grade)
try:
    good_bad(data77, class7_grade)
except:
    pass
print(average)
try:
    good_bad(average, avg_data1)
except:
    pass


'''
if avg_data1 == average:
    driver = webdriver.Chrome()
    driver.get("https://www.textnow.com/login")
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='submitLogin']")))

    #login info
    username_field = driver.find_element_by_xpath("//input[@name= 'username']")
    username_field.click()
    username_field.send_keys('gradealert')
    password_field = driver.find_element_by_xpath("//input[@name= 'password']")
    password_field.click()
    password_field.send_keys("Moonlight321")
    next_btn = driver.find_element_by_xpath("//button[@id= 'submitLogin']")
    next_btn.click()
    #end login

    #sending of alert
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='newText']")))
    new_text_btn = driver.find_element_by_xpath("//button[@id='newText']")
    new_text_btn.click()
    number_field = driver.find_element_by_xpath("//input[@class= 'newConversationTextField']")
    number_field.send_keys("5086638436")
    message_feild = driver.find_element_by_xpath("//textarea[@id= 'message']")
    message_feild.click()
    message_feild.send_keys('This is an alert from Grade Alert letting you know your AVERAGE has gone from '+avg_data1+ ' to '+average+ '. To see the report in greater detail go to https://www.mms669.org/MMSGB45/default.aspx?ReturnUrl=%2fMMSGB45%2fstudent')
    driver.find_element_by_xpath("//div[@class= 'send-btn']").click()
    time.sleep(12)
    driver.close()
    #end send
else:
    print('There is a change in average... how? idk.')
'''


if avg_data1 == average:
    timeout = 15
    #go to gmail.com
    driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//input[@class='whsOnd zHQkBf']")))
    #this is where you enter email address
    textbox = driver.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
    #ths is the "Next" button to get to the page where you type the password
    next_btn = driver.find_element_by_xpath("//div[@id='identifierNext']")
    #sends email adress info
    textbox.send_keys("johnstarte@gmail.com")
    #clicks next
    next_btn.click()
    time.sleep(5)
    textbox2 = driver.find_element_by_xpath("//input[@name='password']")
    textbox2.send_keys("jjjkkklll")
    next_btn2 = driver.find_element_by_xpath("//span[@class='RveJvd snByac']")

    next_btn2.click()
    timeout = 20
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='T-I J-J5-Ji T-I-KE L3']")))
    compose_btn = driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji T-I-KE L3']")
    compose_btn.click()
    time.sleep(3.3)
    email_address = driver.find_element_by_xpath("//textarea[@class= 'vO']")
    subject_box = driver.find_element_by_xpath("//input[@name='subjectbox']")
    email_address.send_keys("tuzoegbu@student.medwayschools.org")
    subject_box.send_keys('GradeGetter Alert')
    messege_box = driver.find_element_by_xpath("//div[@class='Am Al editable LW-avf']")
    messege_box.click()
    averagestr = str(average)
    avg_data11 = str(avg_data1)
    messege_box.send_keys('TIMOTHY JOHN UZOEGBU, Your grades have been updated on the Medway High School Student Portal website. Your average went from ', avg_data11,' to ', averagestr,'. Go to https://www.mms669.org/MMSGB45/default.aspx?ReturnUrl=%2fMMSGB45%2fstudent to see more.')
    send_btn = driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji aoO T-I-atl L3']")
    send_btn.click()
    time.sleep(2)
    driver.close()       
else:
    print('no new updates')
    driver.close()

