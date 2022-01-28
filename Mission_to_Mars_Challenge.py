#!/usr/bin/env python
# coding: utf-8

# In[119]:


# Import Splinter and BeautifulSoup
from bs4 import BeautifulSoup as soup
import pandas as pd
from splinter import Browser
import time
from webdriver_manager.chrome import ChromeDriverManager


# In[120]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[46]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_not_visible_by_css("div.list_text", wait_time=1)


# In[47]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[48]:


slide_elem.find('div', class_='content_title')


# In[49]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_="content_title").get_text()
news_title


# In[50]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find("div", class_="article_teaser_body").get_text()
news_p


# Scraping

# In[51]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[23]:


# Find and click the full image button
full_image_elem = browser.find_by_tag("button")[1]
full_image_elem.click()


# In[27]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, "html.parser")


# In[29]:


# Find the relative image url
img_url_rel = img_soup.find("img", class_="fancybox-image").get("src")
img_url_rel


# In[35]:


img_url = f"https://spaceimages-mars.com/{img_url_rel}"
img_url


# In[36]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[37]:


df.to_html()


# In[38]:


browser.quit()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[125]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)

# 2. Create a list to hold the images and titles.
linkName = []
linkImg = []
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Optional delay for loading the page
browser.is_element_not_present_by_css("div.item", wait_time = 1)
# Convert the browser html to a soup object and then quit the browser
html = browser.html
head_soup = soup(html, "html.parser")

slide_element = head_soup.select("div.item")
# Use the parent element to find the first all titles and urls
for item in slide_element:
    linkName.append(item.find("h3").get_text())

    # finding img URLS
    for a in item.find_all("a", href=True):
        if a.text:
            linkImg.append(url + a["href"])

for link in linkImg:
    browser.visit(link)
    time.sleep(1)
    
    # Find 'Sample' Image urls:
    img_url = browser.links.find_by_text("Sample")

    hemisphere_image_urls.append(img_url["href"])

#home page
browser.visit(url)

#making a dictionary for the links and titles
hemisphere_image_urls = [{"img_urls": hemisphere_image_urls, "title": linkName} for hemisphere_image_urls,linkName in  zip(hemisphere_image_urls,linkName)]

print(hemisphere_image_urls)


# In[127]:


hemisphere_image_urls


# In[128]:


browser.quit()


# In[ ]:




