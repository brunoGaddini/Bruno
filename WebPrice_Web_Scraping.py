#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!pip install selenium


# In[ ]:


#!pip install webdriver-manager 


# In[ ]:


#!pip install html5lib


# In[ ]:


#pip install --upgrade pip


# In[29]:


from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime
from pathlib import Path

import time
import pandas as pd
import os # Working with files on the computer
import glob


# In[16]:


# Installing drive manager and opening website link
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

url = "https://app.webprice.com.br/login?_gl=1*1h5uve9*_ga*MTI1Nzc2ODgyOC4xNjc0NDk0OTcw*_ga_9MSYN0HT5G*MTY3NjMwODM3Ni42LjAuMTY3NjMwODM3Ni4wLjAuMA..*_ga_EGFEJH6CGC*MTY3NjMwODM3Ni42LjAuMTY3NjMwODM3Ni42MC4wLjA.&_ga=2.232303065.730229673.1676308376-1257768828.1674494970"

driver.get(url)


# In[17]:


# Criar tempo de espera entre as ações ou código para executar a px linhas apenas concluido a etapa anterior

# Find the place to enter email
email_element = driver.find_element("xpath", '''/html/body/div/div/div[2]/div/div[3]/form[1]/div[1]/input''')
email_element.click()

# Enter e-mail
email_element.send_keys("lg.pamela")


# In[18]:


# Find the place to enter password
password_element = driver.find_element("xpath", '''/html/body/div/div/div[2]/div/div[3]/form[1]/div[2]/input''')
password_element.click()

# Enter password
password_element.send_keys("pamela4645")
password_element.click()


# In[19]:


# Entering the page
enter_button = driver.find_element("xpath", '''/html/body/div/div/div[2]/div/div[3]/form[1]/div[4]/button''')
enter_button.click()


# In[23]:


# Accessing location to generate report export
enter_button = driver.find_element("xpath", '''/html/body/div[2]/div[2]/div[3]/div[1]/div/div[1]/div[2]/div[2]/button''').click()


# In[25]:


# Exporting products report
enter_button = driver.find_element("xpath", '''/html/body/div[2]/div[2]/div[3]/div[1]/div/div[1]/div[2]/div[2]/ul/li[1]/div[3]/a/i''').click()


# In[ ]:


#print(list_files)


# In[40]:


# Looking for downloads folder path
def get_download_path():
    """Returns the default downloads path for windows"""

    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    return os.path.join(os.path.expanduser('~'), 'downloads')

# Searching for the latest file in the downloads folder
def get_latest_file_path(path):
    """return the latest file in a path"""

    file_paths = glob.glob(f'{path}/*')
    all_files_modification_time = [ os.path.getmtime(path) for path in file_paths ]
    latest_file_index = all_files_modification_time.index(max(all_files_modification_time))
    return file_paths[latest_file_index]

downloads_path = get_download_path()
latest_file_path = get_latest_file_path(downloads_path)

with open(latest_file_path, 'r') as file:
    #print(latest_file_path)
    df = pd.read_csv(latest_file_path, sep=';', encoding='utf-8', skiprows=1, decimal='.')
    df.rename(columns = {'WebGlobal ID': 'ID'}, inplace = True)
    df.drop(["REFERENCIA"       ,
             "No DE LOJAS"      ,
             "MAIS BARATO"      ,
             "CODIGO INTERNO"   ,
             "No DE PARCELAS"   ,
             "VALOR DA PARCELA"], axis = 1, inplace = True)
    pass


# In[41]:


df


# In[ ]:


# Pandas deletar linhas com condições


# In[ ]:





# In[ ]:


getdate = datetime.now().strftime("%m-%d-%y")
print(getdate)

