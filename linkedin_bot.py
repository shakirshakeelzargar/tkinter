from selenium import webdriver
import time
import os
from urllib.parse import quote
import configparser
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext,messagebox
import threading
import webbrowser
from bs4 import BeautifulSoup
chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument('--log-level=3')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])



# country="india"

# f=open("login.txt")
# login_details=[]
# for x in f.readlines():
#     login_details.append(x)
# driver = webdriver.Chrome("chromedriver.exe")
def login():

    add_logs("Opening Linkedin")
    driver.get("https://www.linkedin.com/login")
    add_logs("Trying to Login")
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div/form/div[1]/input")))
    driver.find_element_by_xpath("/html/body/div/main/div/form/div[1]/input").send_keys(username_text)
    driver.find_element_by_xpath("/html/body/div/main/div/form/div[2]/input").send_keys(password_text)
    driver.find_element_by_xpath("/html/body/div/main/div/form/div[3]/button").click()
    if "Login" in driver.title:
        print("\n##############################################")
        print("#######LOGIN FAILED WRONG EMAIL OR PASS#######")
        print("##############################################")
        return False
    else:
        print("Login Successful")
        return True

def goto_connections():
    add_logs("Opening Connections")
    # my_networks = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/div/nav/ul/li[2]/a/span[1]")))
    # my_networks.click()
    # connections = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div[5]/div[3]/div/div/div/div/div/aside/div[1]/div/section/div/div[1]/a/div/div[1]/li-icon")))
    # connections.click()
    driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
def goto_filters():
    add_logs("Opening Filters")
    search_with_filters = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div[5]/div[3]/div/div/div/div/div/div/div/div/section/div/div[2]/a")))
    driver.execute_script("arguments[0].click();", search_with_filters)
    all_filters = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div[5]/div[3]/div/div[1]/header/div/div/div[2]/button/span")))
    driver.execute_script("arguments[0].click();", all_filters)
def apply_filters():
    add_logs("Applying Filters")
    if len(region_text)>0:
        country_region = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div[1]/ul/li[3]/form/div/fieldset/ol/li[1]/div/div/input")))
        country_region.send_keys(region_text)
        time.sleep(5)
        country_region.send_keys(Keys.DOWN)
        country_region.send_keys(Keys.RETURN)
        add_logs("Applied Region Filter--"+str(region_text))
    
    if len(industries_text)>0:
        for x in industries_text:
            industries = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div[1]/ul/li[6]/form/div/fieldset/ol/li[1]/div/div/input")))
            industries.send_keys(x)
            time.sleep(5)
            industries.send_keys(Keys.DOWN)
            industries.send_keys(Keys.RETURN)
            add_logs("Applied Industry Filter--"+str(x))
    if len(current_companies_text)>0:
        company = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div[1]/ul/li[4]/form/div/fieldset/ol/li[1]/div/div/input")))
        company.send_keys(current_companies_text)
        time.sleep(5)
        company.send_keys(Keys.DOWN)
        company.send_keys(Keys.RETURN)
        add_logs("Applied Company Filter--"+str(current_companies_text))
    if len(schools_text)>0:
        school = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div[1]/ul/li[8]/form/div/fieldset/ol/li[1]/div/div/input")))
        school.send_keys(schools_text)
        time.sleep(5)
        school.send_keys(Keys.DOWN)
        school.send_keys(Keys.RETURN)
        add_logs("Applied School Filter--"+str(schools_text))
    apply = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/div/div[2]/button[2]/span")))
    driver.execute_script("arguments[0].click();", apply)
    driver.implicitly_wait(7)

def scroll():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 3);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
    time.sleep(3)
    
def send_message():
    scroll()
    nextt=True
    page=1
    while nextt==True:
        add_logs("Going to page "+ str(page))
        if page>1:
            next_page = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div[5]/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[1]/artdeco-pagination/button[2]")))
            driver.execute_script("arguments[0].click();", next_page)
            scroll()
            scroll()
    # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div[5]/div[3]/div/div[2]/div/div[2]/div/div/div/div")))
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        n=0
        people_list = driver.find_elements_by_xpath('//button[@class="message-anywhere-button search-result__actions--primary artdeco-button artdeco-button--default artdeco-button--2 artdeco-button--secondary"]')
        lenth_of_people=len(people_list)
        while n<lenth_of_people:
#             add_logs("sending message to page "+str(page)+" person" + str(n))
            people_list = driver.find_elements_by_xpath('//button[@class="message-anywhere-button search-result__actions--primary artdeco-button artdeco-button--default artdeco-button--2 artdeco-button--secondary"]')
            # print(len(people_list))
            one_person=people_list[n]
            # try:
            #     name = driver.find_elements_by_xpath('.//span[@class="artdeco-pill__text"]')
            #     # name=driver.find_element_by_css_selector('.artdeco-pill__text').text
            #     name=name[0].text
            #     print(name)

            #     # print("Sending Message to "+str(name))
            # except Exception as ex:
            #     print(ex)
            #     pass
                

            driver.execute_script("arguments[0].click();", one_person)
            try:
                time.sleep(2)
                html = driver.page_source
                page_soup=BeautifulSoup(html,"lxml")
                namee=page_soup.find("span","artdeco-pill__text")
                name_textt=str(namee.text).strip()
                add_logs("Sending message to "+"'"+name_textt+"'")
            except Exception as ex:
                print(ex)
                
            try:
                type_message = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div[5]/aside/div[2]/div[1]/form/div[2]/div/div[1]/div[1]")))
                type_message.send_keys(message_text)

                
            except:
                try:
                    type_message=driver.find_element_by_xpath("//div[contains(@class, 'msg-form__contenteditable t-14 t-black--light t-normal flex-grow-1 notranslate')]")
                    
                    type_message.send_keys(message_text)
                    
                except:
                    pass
                
                n+=1
                pass
            close = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div[5]/aside/div[2]/header/section[2]/button[2]")))
            driver.execute_script("arguments[0].click();", close)
            n+=1
        page+=1
        
#         nextt=check_exists_by_xpath("/html/body/div[5]/div[5]/div[3]/div/div[2]/div/div[2]/div/div/div/div/div[1]/artdeco-pagination/button[2]")
        try:
            html = driver.page_source
            page_soup=BeautifulSoup(html,"lxml")
            
            nxt=page_soup.find("button","artdeco-pagination__button artdeco-pagination__button--next artdeco-button artdeco-button--muted artdeco-button--icon-right artdeco-button--1 artdeco-button--tertiary ember-view")
            if nxt is not None:
                add_logs("Next page found")
                nextt=True
            else:
                add_logs("Next page not found. This is the last page.\n The program will stop")
                nextt=False
                

        except Exception as e:
            add_logs("Next page not found. This is the last page.\n The program will stop")
            nextt=False


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

        

        

        
        
        


    



    

    
    
def run():
    try:
        start_popup.configure(text="Process Started.\n Check Execution logs!",fg='green')
        button_start_process.config(state="disabled")
        add_logs("********Process Started********")
        global driver
        if CheckVar1.get()==1:
            driver = webdriver.Chrome(executable_path="chromedriver.exe",options=chrome_options)
        else:
            driver = webdriver.Chrome(executable_path="chromedriver.exe")
        try_login=login()
        time.sleep(3)
        if try_login==True:
            add_logs("Login Successful...")
            time.sleep(3)
            goto_connections()
            time.sleep(3)
            goto_filters()
            time.sleep(3)
            apply_filters()
            time.sleep(3)
            scroll()
            time.sleep(3)
            send_message()
            time.sleep(3)
            button_start_process.config(state="active")
        else:
            button_start_process.config(state="active")
            add_logs("Login Failed. Check your Credentials")
    except Exception as ex:
        button_start_process.config(state="active")
        add_logs("Error Occured. The erros is: \n"+str(ex))
    


# run()
def save_message():
    if len(message_entry.get(1.0, END))<=1:
        message_popup.configure(text="Enter Valid Message!",fg='red')
    else:
        global message_text
        message_text=str(message_entry.get(1.0, END))
        message_popup.configure(text="Successfully saved!",fg='green')
        add_logs("Message Saved")
def save_credentials():
    if len(username_entry.get())==0 or len(password_entry.get())==0:
        login_popup.configure(text="Enter Valid Credentials!",fg='red')
    else:
        global username_text
        global password_text
        username_text=str(username_entry.get())
        password_text=str(password_entry.get())
        add_logs("Login Credentials Saved")
        login_popup.configure(text="Successfully saved!",fg='green')
def save_filters():
    if len(str(region_entry.get()))>0:
        global region_text
        region_text=str(region_entry.get())
    if len(str(schools_entry.get()))>0:
        global schools_text
        schools_text=str(schools_entry.get())
    if len(str(current_companies_entry.get()))>0:
        global current_companies_text
        current_companies_text=str(current_companies_entry.get())
    filter_popup.configure(text="Successfully Saved!",fg='green')
    add_logs("Filters Saved")
# def run():
#     start_popup.configure(text="Process Started.\n Check Execution logs!",fg='green')
#     button_start_process.config(state="disabled")
#     add_logs("********Process Started********")
def add_logs(message):
    sctext.configure(state='normal')
    sctext.insert(tk.END, message + '\n')
    sctext.configure(state='disabled')
    # Autoscroll to the bottom
    sctext.yview(tk.END)

def submit():
    button_start_process.config(state="disabled")
    time.sleep(5) # put your stuff here
    run()
def start_submit_thread(event):
    global submit_thread
    submit_thread = threading.Thread(target=submit)
    submit_thread.daemon = True
#     progressbar.start()
    submit_thread.start()
    root.after(20, check_submit_thread)
def check_submit_thread():
    if submit_thread.is_alive():
        root.after(20, check_submit_thread)
    else:
        pass
def save_industries():
    
    for name, var in choices.items():
        if var.get()==1:
            if name not in industries_text:
                industries_text.append(name)
        else:
            if name in industries_text:
                industries_text.remove(name)
    print(industries_text)
def callback(url):
    webbrowser.open_new(url)

# t = threading.Thread(target=add_logs)
# t.start()
username_text=""
password_text=""
region_text=""
message_text=""
current_companies_text=""
schools_text=""
global industries_text
industries_text=[]
choices = {}
f=open("industries.txt","r")
x=f.readlines()
f.close()
root = tk.Toplevel()
root.iconbitmap('icon.ico')
root.withdraw()

window = Toplevel(root)
window.protocol("WM_DELETE_WINDOW", root.destroy)
window.geometry('900x570')
window.title("LinkedIn Marketing Tool")
window.resizable(0,0)
window.iconbitmap('icon.ico')

header_frame=tk.Frame(window,bg="white",borderwidth = 1,highlightcolor="green",highlightbackground="green",highlightthickness=2,height=60,width=890)
footer_frame=tk.Frame(window,bg='white',borderwidth = 1,highlightcolor="green",highlightbackground="green",highlightthickness=2,height=20,width=890)
login_frame=tk.Frame(window,bg='white',borderwidth = 1,highlightcolor="green",highlightbackground="green",highlightthickness=2,height=223,width=218)
message_frame=tk.Frame(window,bg='white',borderwidth = 1,highlightcolor="green",highlightbackground="green",highlightthickness=2,height=223,width=218)
filter_frame=tk.Frame(window,bg='white',borderwidth = 1,highlightcolor="green",highlightbackground="green",highlightthickness=2,height=223,width=440)
final_submit_frame=tk.Frame(window,bg="white",borderwidth = 1,highlightcolor="green",highlightbackground="green",highlightthickness=2,height=60,width=445)
log_frame=tk.Frame(window,bg="white",borderwidth = 1,highlightcolor="green",highlightbackground="green",highlightthickness=2,height=385,width=445)
log_title_frame=tk.Frame(log_frame,bg="white",borderwidth = 1,highlightcolor="green",highlightbackground="green",highlightthickness=2,height=60,width=433)
sctext=scrolledtext.ScrolledText(log_frame,bg='black',width=51,height=19,fg='white',state='disabled')
log_title_label=tk.Label(log_title_frame,text="Execution Log", font=("Arial Bold",20),bg='white',fg='green')
message_title_frame=tk.Frame(message_frame,bg='white',borderwidth = 1,highlightcolor="green",highlightbackground="green",highlightthickness=2,height=40,width=206)
login_title_frame=tk.Frame(login_frame,bg='white',borderwidth = 1,highlightcolor="green",highlightbackground="green",highlightthickness=2,height=40,width=206)
message_title_label=tk.Label(message_title_frame,text="Enter Message", font=("Arial Bold",13),bg='white',fg='green')
login_title_label=tk.Label(login_title_frame,text="Login Credentials", font=("Arial Bold",13),bg='white',fg='green')
username_label=tk.Label(login_frame,text="LinkedIn Username:", font=("Arial ",10),bg='white',fg='green')
password_label=tk.Label(login_frame,text="LinkedIn Password:", font=("Arial ",10),bg='white',fg='green')
username_entry=tk.Entry(login_frame,width=30,bg='black',fg='white',insertbackground='white')
password_entry=tk.Entry(login_frame,show="*",width=30,bg='black',fg='white',insertbackground='white')
message_entry=scrolledtext.ScrolledText(message_frame,bg='black',width=23,height=7,fg='white',insertbackground='white')
button_login = tk.Button(login_frame, text="    Save    ", fg="black", activebackground = "green",command=save_credentials) 
button_message = tk.Button(message_frame, text="    Save    ", fg="black", activebackground = "green",command=save_message) 
message_popup=tk.Label(message_frame,text="", font=("Arial",8),bg='white')
login_popup=tk.Label(login_frame,text="", font=("Arial",8),bg='white')
filter_title_frame=tk.Frame(filter_frame,bg='white',borderwidth = 1,highlightcolor="green",highlightbackground="green",highlightthickness=2,height=40,width=425)
filter_title_label=tk.Label(filter_title_frame,text="Enter Search Filters", font=("Arial Bold",15),bg='white',fg='green')
region_label=tk.Label(filter_frame,text="Region:", font=("Arial ",10),bg='white',fg='green')
region_entry=tk.Entry(filter_frame,width=30,bg='black',fg='white',insertbackground='white')
button_filter = tk.Button(filter_frame, text="    Save    ", fg="black", activebackground = "green",command=save_filters) 
filter_popup=tk.Label(filter_frame,text="", font=("Arial",8),bg='white')
button_start_process = tk.Button(final_submit_frame, text="    Start Process    ", fg="black", activebackground = "green",command=lambda:start_submit_thread(None)) 
start_popup=tk.Label(final_submit_frame,text="", font=("Arial",8),bg='white')
current_companies_label=tk.Label(filter_frame,text="Company:", font=("Arial ",10),bg='white',fg='green')
current_companies_entry=tk.Entry(filter_frame,width=30,bg='black',fg='white',insertbackground='white')
schools_label=tk.Label(filter_frame,text="School:", font=("Arial ",10),bg='white',fg='green')
schools_entry=tk.Entry(filter_frame,width=30,bg='black',fg='white',insertbackground='white')
title_label=tk.Label(header_frame,text="LinkedIn Messaging Bot", font=("Arial ",20),bg='white',fg='green')
title_label2=tk.Label(header_frame,text="By Shakir Shakeel", font=("Arial ",10),bg='white',fg='green')
# title_label3=tk.Label(header_frame,text="http://instagram.com/sshakirzargar", font=("Arial ",10),bg='white',fg='blue')
facebook=PhotoImage(file="facebook.png")
insta=PhotoImage(file="insta.png")
github=PhotoImage(file="github.png")
facebook_button=tk.Button(header_frame, text = 'Click Me !', image = facebook,bg='white')
insta_button=tk.Button(header_frame, text = 'Click Me !', image = insta,bg='white')
github_button=tk.Button(header_frame, text = 'Click Me !', image = github,bg='white')
CheckVar1 = IntVar()
check_button_invisible = tk.Checkbutton(final_submit_frame, text = "Invisible", variable = CheckVar1,onvalue = 1, offvalue = 0, height=2,width = 10,bg='white')





industry_dropdown = tk.Menubutton(filter_frame, text="Choose Industries", indicatoron=True, borderwidth=1, relief="raised")
menu = tk.Menu(industry_dropdown, tearoff=False)
industry_dropdown.configure(menu=menu)





menubar = Menu(window)
window.config(menu=menubar)

# Create a menu button labeled "File" that brings up a menu
filemenu = Menu(menubar)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Print')
filemenu.add_command(label='Save')
filemenu.add_separator(  )
filemenu.add_command(label='Quit' )


editmenu = Menu(menubar)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Undo')
editmenu.add_command(label='Redo')
editmenu.add_command(label='Clear' )



header_frame.place(x=5,y=5)
footer_frame.place(x=5,y=525)
login_frame.place(x=5,y=70)
message_frame.place(x=227,y=70)
filter_frame.place(x=5,y=297)
final_submit_frame.place(x=450,y=460)
log_frame.place(x=450,y=70)
# log_title_frame.place(x=455,y=75)
log_title_frame.place(x=3,y=5)
sctext.place(x=5,y=70)
log_title_label.place(x=125,y=7)
message_title_frame.place(x=3,y=5)
login_title_frame.place(x=3,y=5)
message_title_label.place(x=40,y=6)
login_title_label.place(x=27,y=6)
message_entry.place(x=4,y=50)
username_label.place(x=45,y=60)
password_label.place(x=45,y=110)
username_entry.place(x=15,y=85)
password_entry.place(x=15,y=135)
button_login.place(x=75,y=165)
button_message.place(x=75,y=172)
message_popup.place(x=10,y=197)
login_popup.place(x=10,y=197)
filter_title_frame.place(x=5,y=5)
filter_title_label.place(x=110,y=3)
region_label.place(x=5,y=70)
region_entry.place(x=5,y=95)
button_filter.place(x=5,y=190)
filter_popup.place(x=320,y=195)
button_start_process.place(x=160,y=14)
check_button_invisible.place(x=50,y=11)
industry_dropdown.place(x=270,y=70)
for choice in x:
    choice=choice.replace("\n","")
    choices[choice] = tk.IntVar(value=0)
    menu.add_checkbutton(label=choice, variable=choices[choice], onvalue=1, offvalue=0, command=save_industries)
current_companies_label.place(x=5,y=130)
current_companies_entry.place(x=5,y=155)
schools_label.place(x=245,y=130)
schools_entry.place(x=245,y=155)
title_label.place(x=280,y=8)
title_label2.place(x=750,y=1)
# title_label3.place(x=660,y=30)
# title_label3.bind("<Button-1>", lambda e: callback("http://instagram.com/sshakirzargar"))
facebook_button.place(x=750,y=25)
facebook_button.bind("<Button-1>", lambda e: callback("http://facebook.com/sshakirshakeel"))
insta_button.place(x=790,y=25)
insta_button.bind("<Button-1>", lambda e: callback("http://instagram.com/sshakirzargar"))
github_button.place(x=830,y=25)
github_button.bind("<Button-1>", lambda e: callback("http://github.com/shakirshakeelzargar"))

window.mainloop()
    