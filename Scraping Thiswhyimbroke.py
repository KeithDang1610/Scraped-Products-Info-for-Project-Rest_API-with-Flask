#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time


# In[5]:


driver = webdriver.Chrome(r'C:\Users\DELL\Desktop\WEB SCRAPING\chromedriver.exe')
driver.get('https://www.thisiswhyimbroke.com/new/')


# In[6]:


last_height = driver.execute_script('return document.body.scrollHeight')                        


# In[7]:


while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(4)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

soup = BeautifulSoup(driver.page_source, 'lxml')
product_card = soup.find_all('div', {"class":'ng-scope',"ng-if":"::post.type == 'post'"})
df=pd.DataFrame({'Product_name':[''], 'Product_link':[''], 'Product_price':[''], 'Product_description':[''], 'Product_image':[''], 'Product_sales':['']})
for product in product_card:
    try:
        product_name = product.find('a', class_='ng-binding ng-scope').text
        product_link = product.find('a', class_='ng-binding ng-scope').get('href')
        product_price = product.find('div', class_='price ng-binding').text
        product_description = product.find('p', class_='ng-binding').text
        product_image = product.find('img', class_='img-fixed lazy-image--handled').get('src')
        product_sales = product.find('a', class_='saved-count ng-binding').text
        df= df.append({'Product_name':product_name, 'Product_link':product_link, 'Product_price':product_price, 'Product_description':product_description,'Product_image':product_image,'Product_sales':Product_sales }, ignore_index=True)
    except:
        pass


# In[19]:


soup = BeautifulSoup(driver.page_source, 'lxml')
product_card = soup.find_all('div', {"class":'ng-scope',"ng-if":"::post.type == 'post'"})
df=pd.DataFrame({'Product_name':[''], 'Product_link':[''], 'Product_price':[''], 'Product_description':[''], 'Product_image':[''], 'Product_sales':['']})
for product in product_card:
    try:
        product_name = product.find('a', class_='ng-binding ng-scope').text
        product_link = product.find('a', class_='ng-binding ng-scope').get('href')
        product_price = product.find('div', class_='price ng-binding').text
        product_description = product.find('p', class_='ng-binding').text
        product_image = product.find('img', class_='img-fixed lazy-image--handled').get('src')
        product_sales = product.find('a', class_='saved-count ng-binding').text
        df= df.append({'Product_name':product_name, 'Product_link':product_link, 'Product_price':product_price, 'Product_description':product_description,'Product_image':product_image,'Product_sales':product_sales }, ignore_index=True)
    except:
        pass
    

df


# In[50]:


df.to_excel(r'C:\Users\DELL\Desktop\thisiswhyimbroke_new.xlsx')


# In[22]:


df = df.dropna()
df


# In[47]:


#df['Product_price']=df['Product_price'].apply(lambda x: x.strip('$'))
#df['Product_price'] =df['Product_price'].apply(lambda x: float(x.replace('.',''))
df['Product_price']


# In[49]:


df


# In[17]:


soup = BeautifulSoup(driver.page_source, 'lxml')
product_card = soup.find_all('div', {"class":'ng-scope',"ng-if":"::post.type == 'post'"})
#df=pd.DataFrame({'Product_name':[''], 'Product_link':[''], 'Product_price':[''], 'Product_description':['']})
df=pd.DataFrame({'Product_name':[''], 'Product_link':[''], 'Product_price':[''], 'Product_description':[''], 'Product_image':[''], 'Product_sales':['']})
for product in product_card:
    try:
        product_name = product.find('a', class_='ng-binding ng-scope').text
        product_link = product.find('a', class_='ng-binding ng-scope').get('href')
        product_price = product.find('div', class_='price ng-binding').text
        product_description = product.find('p', class_='ng-binding').text
        product_image = product.find('img', class_='img-fixed lazy-image--handled').get('src')
        product_sales = product.find('a', class_='saved-count ng-binding').text
        df= df.append({'Product_name':product_name, 'Product_link':product_link, 'Product_price':product_price, 'Product_description':product_description,'Product_image':product_image,'Product_sales':Product_sales},ignore_index=True)
    except:
        pass
df


# In[50]:


df.to_excel(r'C:\Users\DELL\Desktop\thisiswhyimbroke.xlsx')


# In[14]:


soup = BeautifulSoup(driver.page_source, 'lxml')
product_card = soup.find_all('div', {"class":'ng-scope',"ng-if":"::post.type == 'post'"})
soup.find('img', class_='img-fixed lazy-image--handled').get('src')


# In[51]:


import pandas as pd


# In[52]:


df = pd.read_excel(r'C:\Users\DELL\Desktop\thisiswhyimbroke_new.xlsx')
df


# In[63]:


type(df['Product_price'][1])


# In[61]:


df['Product_price'] = df['Product_price'].astype(str).apply(lambda x: x.strip('$'))


# In[65]:


df['Product_price'] = df['Product_price'].apply(lambda x: x.strip(' \xa0'))


# In[71]:


rows_to_drop = df.loc[df.eq('').any(axis=1)]
df = df.drop(rows_to_drop.index)


# In[75]:


df.to_excel(r'C:\Users\DELL\Desktop\thisiswhyimbroke_new1.xlsx')


# In[89]:


df = pd.read_excel(r'C:\Users\DELL\Desktop\thisiswhyimbroke_new1.xlsx')
df


# In[90]:


type(df['Product_description'][1000])


# In[93]:


df['Product_description'] = df['Product_description'].apply(lambda x: x[:80])
df['Product_description']


# In[ ]:




