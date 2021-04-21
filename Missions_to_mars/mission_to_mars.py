#!/usr/bin/env python
# coding: utf-8

# In[14]:


#notebook for scraping
#dependencies 

import os 
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


#website to scrape 
url = 'https://redplanetscience.com/'
#retrieve page wiht splinter module - this page will need to stay open to retreive the parsed text
browser.visit(url)


# In[4]:


html = browser.html
#parse with soup
soup = BeautifulSoup(html, 'html.parser')


# #### Scrape the Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

# In[5]:


#parent divs for latest article title and parargaraph

title = soup.find('div', class_='content_title').text
print(title)
para = soup.find('div', class_='article_teaser_body').text
print(para)


# In[6]:


#remeber to quit broswer 
browser.quit()


# #### JPL Mars Space Images - Featured Image

# In[8]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[9]:


jpl_url = 'https://spaceimages-mars.com/'
#open the website for scraping
browser.visit(jpl_url)


# In[10]:


html = browser.html
#parse
soup = BeautifulSoup(html, 'html.parser')


# In[11]:


featured_img_url = soup.find('img', class_="headerimage fade-in")['src']
featured_img_url = (jpl_url + featured_img_url)
print(featured_img_url)


# In[76]:


browser.quit()


# ### Pandas Scraping 

# #### Mars Facts

# In[77]:


mars_facts_url = 'https://galaxyfacts-mars.com/'
#create a tablular structure out of the URL
table = pd.read_html(mars_facts_url)
table


# In[78]:


facts_df = table[0]
facts_df.head()


# In[79]:


facts_df = facts_df.rename(columns={0:'Mars-Earth Comparison', 1: 'Mars', 2:'Earth' })
facts_df


# In[80]:


facts_df = facts_df.drop([0])


# In[81]:


facts_df = facts_df.set_index(['Mars-Earth Comparison'])
facts_df.head()


# In[82]:


#convert table to html string
html_table = facts_df.to_html()
html_table
#do they want us to export the HTML as well ?


# #### Mars Hemispheres

# In[83]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[85]:


#hesmisphere website for scraping
img_url = 'https://marshemispheres.com/'
#retreive page with requests module 
browser.visit(img_url)
#create soup object with parser
html = browser.html
#parse
soup = BeautifulSoup(html, 'html.parser')


# In[86]:


print(soup.prettify())


# In[87]:


results = soup.find_all('div', class_ ='item')
results


# In[104]:


hemisphere_dict = []

for result in results:
    title = result.find('h3').text
    h_url = result.find('img', class_ = 'thumb')['src']
    full_url = (img_url+h_url)
    print(title)
    print(full_url)
    print('---------')
    hemisphere_dict.append({'Image Title': title ,'Image URL': full_url})
#only printing the small images 
hemisphere_dict
    


# In[ ]:





# In[ ]:




