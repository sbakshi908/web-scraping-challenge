

#notebook for scraping
#dependencies 

import os 
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, render_template, redirect



def scrape():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #website to scrape
    url = 'https://redplanetscience.com/'
    #retrieve page wiht splinter module - this page will need to stay open to retreive the parsed text
    browser.visit(url)

    html = browser.html
    #parse with soup
    soup = BeautifulSoup(html, 'html.parser')

    # #### Scrape the Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

    title = soup.find('div', class_='content_title').text
    print(title)
    para = soup.find('div', class_='article_teaser_body').text
    print(para)

    # #### JPL Mars Space Images - Featured Image

    jpl_url = 'https://spaceimages-mars.com/'
    #open the website for scraping
    browser.visit(jpl_url)

    html = browser.html
    #parse
    soup = BeautifulSoup(html, 'html.parser')

    featured_img_url = soup.find('img', class_="headerimage fade-in")['src']
    featured_img_url = (jpl_url + featured_img_url)
    print(featured_img_url)

    #Pandas Scraping

    # Mars Facts

    mars_facts_url = 'https://galaxyfacts-mars.com/'
    #create a tablular structure out of the URL
    table = pd.read_html(mars_facts_url)
    table

    facts_df = table[0]
    facts_df.head()

    facts_df = facts_df.rename(
        columns={0: 'Mars-Earth Comparison', 1: 'Mars', 2: 'Earth'})
    facts_df

    facts_df = facts_df.drop([0])

    facts_df = facts_df.set_index(['Mars-Earth Comparison'])
    facts_df.head()

    html_table = facts_df.to_html('mars_facts_table.html')
    html_table

    hemi_url = 'https://marshemispheres.com/'
    #retreive page with requests module
    browser.visit(hemi_url)
    #create soup object with parser
    html = browser.html
    #parse
    soup = BeautifulSoup(html, 'html.parser')

    hemi = soup.find_all('div', class_='description')
    print(hemi)

    hem_list = []

    for i in range(len(hemi)):

        hemi_link = browser.find_by_css('a.product-item h3')
        hemi_link[i].click()
        #time.sleep(1)

        img_html = browser.html
        img_soup = BeautifulSoup(img_html, 'html.parser')

        img_title = img_soup.find('h2', class_="title").text

        img_find_class = img_soup.find('div', class_='downloads')
        img_find_click = img_find_class.find('li')
        img_find = img_find_click.find('a')['href']

        img_url = f'{hemi_url}{img_find}'

        hem_list.append({'title': img_title,
                         'img_url': img_url})

        browser.back()
    hem_list

    browser.quit()

    mars_dict = {
        'titles': title,
        'para': para,
        'featured_img': featured_img_url,
        'hemisphere_imgs': hem_list
    }
    mars_dict
   

    return mars_dict
    





