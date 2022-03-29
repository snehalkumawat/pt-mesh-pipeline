#!/usr/bin/env python
# coding: utf-8

# # Task- Create a Scraper for Projects and Tenders

# ## 1) City of Sunnyvale Public Procurement

# In[1]:


#importing libraries

import pandas as pd
import selenium
from selenium import webdriver
import time
import re
import requests
from selenium.common.exceptions import NoSuchElementException

import warnings
warnings.filterwarnings("ignore")


# In[4]:


# driver initialization
driver=webdriver.Chrome(r'C:\Users\lenovo\Downloads\chromedriver_win32 (5)\chromedriver.exe')


# In[5]:


# browsing url

url="https://www.demandstar.com/app/agencies/california/city-of-sunnyvale/procurement-opportunities/e9a860f4-8f17-43af-aae7-e5dc8389f36e/"
#locationCromedriver="C:\Users\lenovo\Downloads\chromedriver_win32 (5)\chromedriver.exe"

class scrapper:
    def testMethod(self):
        #driver=webdriver.Chrome(r'locationCromedriver')
        driver.get(url) 
        
        
        
obj=scrapper()
obj.testMethod()


# In[36]:


#scrapping the data

Tender_name=[]
Location=[]
ID=[]
Due_date=[]
Broadcast_date=[]
Planholders=[]
Status=[]


for i in driver.find_elements_by_xpath('//a[@class="mw-75 text-truncate"]'):
    Tender_name.append(i.text)

for j in driver.find_elements_by_xpath('//div[@class="listGroupWrapper clearfix"]/p'):
    Location.append(j.text)

for k in driver.find_elements_by_xpath('//ul[@class="list-inline"]/li[1]'):
    ID.append(k.text.replace("ID:"," "))
    
for l in driver.find_elements_by_xpath('//ul[@class="list-inline"]/li[4]'):
    Planholders.append(l.text.replace("#Planholders:"," "))
    
for m in driver.find_elements_by_xpath('//ul[@class="list-inline"]/li[2]'):
    Due_date.append(m.text.replace("Due:"," "))

for n in driver.find_elements_by_xpath('//ul[@class="list-inline"]/li[3]'):
    Broadcast_date.append(n.text.replace("Broadcast:"," "))

for p in driver.find_elements_by_xpath('//h5[@class="mw-100 text-truncate"]/span'):
    Status.append(p.text)


        
print(len(Tender_name))
print(len(Location))
print(len(ID))
print(len(Planholders))
print(len(Due_date))
print(len(Broadcast_date))
print(len(Status))


# In[37]:


#making the dataframe of data
df = pd.DataFrame({})
df["Tender_name"] = Tender_name
df["Location"] = Location
df["ID"] = ID
df["Planholders"] = Planholders
df["Due_date"] = Due_date
df["Broadcast_date"] = Broadcast_date
df["Status"] = Status
df


# In[38]:


df.to_csv('tender_of_City_Sunnyvale.csv') # saving to csv file


# In[39]:


df1=pd.read_csv("tender_of_City_Sunnyvale.csv")
df1


# In[40]:


driver.quit()


# ## 2) UK cabinet Contracts

# In[41]:


driver=webdriver.Chrome(r'C:\Users\lenovo\Downloads\chromedriver_win32 (5)\chromedriver.exe')


# In[107]:


url="https://www.contractsfinder.service.gov.uk/Search/Results"
#locationCromedriver="C:\Users\lenovo\Downloads\chromedriver_win32 (5)\chromedriver.exe"

class scrapper:
    def testMethod(self):
        #driver=webdriver.Chrome(r'locationCromedriver')
        driver.get(url) 
        
        
        
obj=scrapper()
obj.testMethod()


# In[108]:


Tender_name=[]
Company_name=[]
Procurement_stage=[]
Notice_status=[]
Closing=[]
Contract_location=[]
Contract_value=[]
Publication_date=[]


# In[109]:


def calling_fun():
    for i in driver.find_elements_by_xpath('//a[@class="govuk-link search-result-rwh break-word"]'):
        Tender_name.append(i.text)

    for j in driver.find_elements_by_xpath('//div[@class="search-result-sub-header wrap-text"]'):
        Company_name.append(j.text)

    for k in driver.find_elements_by_xpath('//div[@class="search-result-entry"][1]'):
        Procurement_stage.append(k.text.replace("Procurement stage"," "))
    
    for l in driver.find_elements_by_xpath('//div[@class="search-result-entry"][2]'):
        Notice_status.append(l.text.replace("Notice status"," "))
    
    for m in driver.find_elements_by_xpath('//div[@class="search-result-entry"][3]'):
        Closing.append(m.text.replace("Closing"," "))

    for n in driver.find_elements_by_xpath('//div[@class="search-result-entry"][4]'):
        Contract_location.append(n.text.replace("Contract location"," "))

    for o in driver.find_elements_by_xpath('//div[@class="search-result-entry"][5]'):
        try:
            Contract_value.append(o.text.replace("Contract value"," "))
        except:
            Contract_value.append("--")
    
    for p in driver.find_elements_by_xpath('//div[@class="search-result-entry"][6]'):
        try:
            Publication_date.append(p.text.replace("Publication date"," "))
        except:
            Publication_date.append("--")


        
    print(len(Tender_name))
    print(len(Company_name))
    print(len(Procurement_stage))
    print(len(Notice_status))
    print(len(Closing))
    print(len(Contract_location))
    print(len(Contract_value))
    print(len(Publication_date))


# In[110]:


calling_fun()


# In[111]:


Publication_date.append("--")


# In[112]:


varbutton = driver.find_element_by_xpath('//li[@class="standard-paginate "]/a[1]')
varbutton


# In[113]:


varbutton.click()


# In[114]:


calling_fun()


# In[115]:


Publication_date.append("--")


# In[116]:


Publication_date.append("--")


# In[117]:


varbutton = driver.find_element_by_xpath('//ul[@class="gadget-footer-paginate"]/li[4]/a')
varbutton


# In[118]:


varbutton.click()


# In[119]:


calling_fun()


# In[120]:


Publication_date.append("--")


# In[121]:


Publication_date.append("--")


# In[122]:


df = pd.DataFrame({})
df["Tender_name"] = Tender_name
df["Company_name"] = Company_name
df["Procurement_stage"] = Procurement_stage
df["Notice_status"] = Notice_status
df["Closing"] = Closing
df["Contract_location"] = Contract_location
df["Contract_value"] = Contract_value
df["Publication_date"] = Publication_date
df


# In[123]:


df.to_csv("UK_contracts.csv")


# In[124]:


driver.quit()


# In[ ]:




