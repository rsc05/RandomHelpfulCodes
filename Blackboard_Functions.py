from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import re
import pandas as pd

def Click_Rami(driver, Content, time):
       # wait for email field and enter email
    WebDriverWait(driver, time).until(
        EC.element_to_be_clickable(Content)).click()

# Sign in to Microsoft MS Streams
# requires you to use authentication app
def Open_BB_page_of_unit(UserEmail, Password, path_to_unit):
    url1 = "https://www.ole.bris.ac.uk/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_17_1"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url1)
    # Make sure you are back on the top of the page
    driver.maximize_window()

    # Click log-in button
    log_in_BB = (By.ID, 'loginLink')
    Click_Rami(driver, log_in_BB, 10)

    EMAILFIELD = (By.ID, "i0116")
    PASSWORDFIELD = (By.ID, "i0118")
    NEXTBUTTON = (By.ID, "idSIButton9")
    Yes = (By.ID, "idSIButton9")
    # wait for email field and enter email
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(EMAILFIELD)).send_keys(UserEmail)

    # Click Next
    Click_Rami(driver, NEXTBUTTON, 10)

    # wait for password field and enter password
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(PASSWORDFIELD)).send_keys(Password)

    # Click Login - same id?
    Click_Rami(driver, NEXTBUTTON, 10)

    # Click Login - same id?
    Click_Rami(driver, Yes, 30)

    link_of_unit = (By.XPATH, path_to_unit)

    # Click Login - same id?
    Click_Rami(driver, link_of_unit, 10)

    return driver

def get_course_content(driver):
    # Click on course content
    Units_material=(By.LINK_TEXT,"COMSM0091_2022_TB-2")
    Content_BUTTON = (By.ID, "controlpanel.course.files_groupExpanderLink")
    Click_Rami(driver, Content_BUTTON, 10)
    Click_Rami(driver, Units_material, 10)
        

def Extract_Speach(driver):
    # Search by text
    Units_material=(By.LINK_TEXT,"txt")
    Click_Rami(driver, Units_material, 10)
    
    # Get number of rows in the table
    path1="/html/body/div[5]/div[3]/div/div[1]/div/div/div[4]/form/div[3]/div[2]/div/table/tbody"
    element1=driver.find_element(By.XPATH,path1).find_elements(By.CSS_SELECTOR, 'tr')
    number_of_rows = len(element1)
    
    # Create a Dataframe with name of videos and hyperlinks

    # Extract information
    name_of_lectures=[]
    html_of_speach=[]

    for j in range(1,number_of_rows+1):
        path=f"{path1}/tr[{j}]/th"
        ele=driver.find_element(By.XPATH,path)
        string=ele.get_attribute("innerText")
        name_of_lectures.append(re.search('(.+?).txt', string).group(1))

        # Get link
        ele1 = ele.find_element(By.XPATH, ".//descendant::a")
        html_of_speach.append(ele1.get_attribute('href'))

    # Create a dataframe containing all these information
    d = {'Title of Video':name_of_lectures,'Speach of Video':html_of_speach}
    df1 = pd.DataFrame(d)   
    df1.set_index('Title of Video', inplace=True)
    driver.back()
    
    return df1

def Extract_Week_lectures(driver):
    # Extract information
    name_of_lectures=[]
    html_of_lectures=[]

    # Search by text
    Units_material=(By.LINK_TEXT,"Work on Progress BB 2023")
    Click_Rami(driver, Units_material, 10)

    p1="/html/body/div[5]/div[3]/div/div[1]/div/div/div[4]/form/div[3]/div[2]/div/table/tbody"
    # element1=driver.find_element(By.XPATH,p1)
    
    element1 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,p1))).find_elements(By.CSS_SELECTOR, 'tr')
    number_of_folders = len(element1)

    for i in range(1,number_of_folders+1):
        # click on week
        Units_material=(By.LINK_TEXT,f"Week{i}")
        Click_Rami(driver, Units_material, 10)
        
        # click on lectures
        Units_material=(By.LINK_TEXT,"Lectures")
        Click_Rami(driver, Units_material, 10)
        
        # How many lectures
        p2='/html/body/div[6]/div[3]/div/div[1]/div/div/div[4]/form/div[3]/div[2]/div/table/tbody'
        element2=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,p2))).find_elements(By.CSS_SELECTOR, 'tr')
        # driver.find_element(By.XPATH,p2).find_elements(By.CSS_SELECTOR, 'tr')
        number_of_folders2 = len(element2)
        
        for k in range(1, number_of_folders2+1):
            path=f"{p2}/tr[{k}]/th"
            ele=driver.find_element(By.XPATH,path)
            string=ele.get_attribute("innerText")
            name_of_lectures.append(re.search('(.+?).pdf', string).group(1))

            # Get link
            ele1 = ele.find_element(By.XPATH, ".//descendant::a")
            html_of_lectures.append(ele1.get_attribute('href'))
            
        driver.back()
        driver.back()
        
        d = {'Title of Lecture':name_of_lectures,'HTML of Lecture':html_of_lectures}
        df1 = pd.DataFrame(d)   
        df1.set_index('Title of Lecture', inplace=True)
        
    return df1