#!/usr/bin/env python
# coding: utf-8

# # Member Gun Investment Tracking
# ### Jasir Rahman
# ### 07/31/25

# In[1]:


import pandas as pd


# In[2]:


# Load Data
senDisclosures23 = pd.read_csv('/Users/jasirrahman/Desktop/Brady/Projects:Tasks/Member Gun Investments/Senate Financial Disclosures - 2023.csv')
senDisclosures24 = pd.read_csv("/Users/jasirrahman/Desktop/Brady/Projects:Tasks/Member Gun Investments/2024-Senate-Financial-Disclosures - 2024-Senate-Financial-Disclosures.csv")
senDisclosures25 = pd.read_csv('/Users/jasirrahman/Desktop/Brady/Projects:Tasks/Member Gun Investments/Senate Financial Disclosures - 2025.csv')
houseDisclosures23 = pd.read_csv('/Users/jasirrahman/Desktop/Brady/Projects:Tasks/Member Gun Investments/House Financial Disclosures - 2023.csv')
houseDisclosures24 = pd.read_csv("/Users/jasirrahman/Desktop/Brady/Projects:Tasks/Member Gun Investments/2024 House Financial Disclosures.csv")
houseDisclosures25 = pd.read_csv('/Users/jasirrahman/Desktop/Brady/Projects:Tasks/Member Gun Investments/House Financial Disclosures - 2025.csv')


# In[3]:


# Check loading status
print(senDisclosures25.head(n=5))
print(senDisclosures24.head(n=5))
print(senDisclosures23.head(n=5))
print(houseDisclosures25.head(n=5))
print(houseDisclosures24.head(n=5))
print(houseDisclosures23.head(n=5))


# ## Data Cleaning

# In[4]:


## Column Cleaning
# Make Sen24 clean full "Name" column
senDisclosures23["Name"] = senDisclosures23["First Name (Middle)"] + " " + senDisclosures23["Last Name (Suffix)"]
print(senDisclosures23["Name"].head(5))
# Make Sen "Filing Year" Column
senDisclosures23["Filing Year"] = "2023"
print(senDisclosures23["Filing Year"].head(5))

# Make Sen24 clean full "Name" column
senDisclosures24["Name"] = senDisclosures24["First Name (Middle)"] + " " + senDisclosures24["Last Name (Suffix)"]
print(senDisclosures24["Name"].head(5))
# Make Sen "Filing Year" Column
senDisclosures24["Filing Year"] = "2024"
print(senDisclosures24["Filing Year"].head(5))

# Make Sen25 clean full "Name" column
senDisclosures25["Name"] = senDisclosures25["First Name (Middle)"] + " " + senDisclosures25["Last Name (Suffix)"]
print(senDisclosures25["Name"].head(5))
# Make Sen "Filing Year" Column
senDisclosures25["Filing Year"] = "2025"
print(senDisclosures25["Filing Year"].head(5))


# In[5]:


## Merge Preparation
# Make "senDisclosuresMerge25" with fewer variables for merging
senDisclosuresMerge25 = senDisclosures25[["Name", "Filing Year", "Report Link"]]
print(senDisclosuresMerge25.head(5))

# Make "senDisclosuresMerge24" with fewer variables for merging
senDisclosuresMerge24 = senDisclosures24[["Name", "Filing Year", "Report Link"]]
print(senDisclosuresMerge24.head(5))

# Make "senDisclosuresMerge23" with fewer variables for merging
senDisclosuresMerge23 = senDisclosures23[["Name", "Filing Year", "Report Link"]]
print(senDisclosuresMerge23.head(5))

# Make "houseDisclosuresMerge25" with fewer variables for merging
houseDisclosuresMerge25 = houseDisclosures25[["Name", "Filing Year", "Report Link"]]
print(houseDisclosuresMerge25.head(5))

# Make "houseDisclosuresMerge24" with fewer variables for merging
houseDisclosuresMerge24 = houseDisclosures24[["Name", "Filing Year", "Report Link"]]
print(houseDisclosuresMerge24.head(5))

# Make "houseDisclosuresMerge23" with fewer variables for merging
houseDisclosuresMerge23 = houseDisclosures23[["Name", "Filing Year", "Report Link"]]
print(houseDisclosuresMerge23.head(5))


# In[6]:


## Merging
congressDisclosures = pd.concat([senDisclosuresMerge23, senDisclosuresMerge24, senDisclosuresMerge25, houseDisclosures23, houseDisclosuresMerge24, houseDisclosuresMerge25], ignore_index=True)
print(congressDisclosures.head(5))
print(len(congressDisclosures))


# In[7]:


## Add test case
new_row = {
    "Name": "Helena Eagan",
    "Filing Year": "2024",
    "Report Link": "/Users/jasirrahman/Desktop/Brady/Projects:Tasks/Member Gun Investments/Test Disclosure.html"
}

congressDisclosures = pd.concat([congressDisclosures, pd.DataFrame([new_row])], ignore_index=True)
#Check if added
print(len(congressDisclosures))


# ## Senate Files
# 
# Senate files are accessible from the "Financials Diclosure" website on the Senate office: https://efdsearch.senate.gov/search/home/. They are not available to examine in bulk, but we can easily access the links to the individual member disclosures for any given year from the website. The key barrier to access is the need to acknowledge the legality of accesing and using disclosure information. This is automatically navigated to when you click on the links in our databases, and must be circumnavigated when starting a bulk session to access them. We can use Selenium to crawl the web through a remote driver, which automatically controls webpages and can interact with elements, for example by clicking on an acknowledgement box. We use Selenium to click the box, then access the webpages in our database, and search them for firearms industry actors.

# In[8]:


## Setting up Selenium
#pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# In[11]:


# Open website using driver
website = 'https://efdsearch.senate.gov/search/home/'
path = '/Users/jasirrahman/Downloads/chromedriver-mac-arm64/chromedriver'
service = Service(executable_path=path)
driver = webdriver.Chrome(service = service)
driver.get(website)


# In[20]:


# Testing functionality of "agree statement" clicker

from selenium.webdriver.common.by import By
import time

# Launch the site
driver.get("https://efdsearch.senate.gov/search/home/")

# Wait for the page to load (simple sleep or use WebDriverWait for production code)
time.sleep(2)

# Find the checkbox and click it
checkbox = driver.find_element(By.ID, "agree_statement")
checkbox.click()


# In[13]:


## Test driver on individual link from "congressDisclosures"

# Open link from congressDisclosures
# Open website using driver
website = 'https://efdsearch.senate.gov/search/home/'
path = '/Users/jasirrahman/Downloads/chromedriver-mac-arm64/chromedriver'
service = Service(executable_path=path)
driver = webdriver.Chrome(service = service)
driver.get(website)

# Click checkbox
# Find the checkbox and click it
checkbox = driver.find_element(By.ID, "agree_statement")
checkbox.click()

# now open congressDisclosures link in same browser
link = congressDisclosures['Report Link'][1]
print(link)
driver.get(link)

# open the next congressDisclosures link in the same browser
link = congressDisclosures['Report Link'][2]
print(link)
driver.get(link)

# next step is to iterate


# In[14]:


# Create subset of data for testing
test = congressDisclosures[1:10]
print(test)
print(len(test))
# Test iteration
links = test['Report Link']
print(links)


# In[15]:


## webScraper 2.0 for Senate

# initialize list of matches
matches = []

# import packages
import re

# define function
def webScraper(links):
    matches = []  # Initialize matches list inside function
    
    for i, link in enumerate(links, 1):
        print(f"Opening: {link} ; {i} of {len(links)}")
        
        # Skip NaN/null links
        if pd.isna(link): 
            continue
            
        try:
            driver.get(link)
            time.sleep(2)
            
            # Get page source and convert to lowercase
            page_text = driver.page_source.lower()
            
            # Check for keywords in the page text
            found_keywords = []
            
            # Regular keywords (simple substring match)
            regular_keywords = ["ammo", "american outdoor", "big 5", "sturm", "firearm", "shooting", "armory",
                               "sportsman's warehouse", "smith & wesson", "ruger", "axon", "olin", "gun", "vista"]
            
            for keyword in regular_keywords:
                if keyword in page_text:
                    found_keywords.append(keyword)
            
            # Special handling for "range" - use word boundaries to avoid "arrangement"
            if re.search(r'\brange\b', page_text):
                found_keywords.append('range')
            
            # Optional: Check if "arrangement" was detected for debugging
            if "arrangement" in page_text and "range" not in found_keywords:
                print(f"ℹ️  'arrangement' detected but 'range' not found as standalone word in: {link}")
            
            # If any keywords found, add to matches
            if found_keywords:
                print(f"🔍 Found keywords {found_keywords} in: {link}")
                matches.append({
                    'url': link,
                    'keywords_found': found_keywords
                })
            else:
                print("✅ No keywords found - Success")
        
        except Exception as e:
            print(f"❌ Error processing {link}: {e}")
            continue
    
    return matches


# In[16]:


# test functionality
webScraper(links)


# In[19]:


# run for senDisclosures23
links = senDisclosures23['Report Link']
len(links)

webScraper(links)


# ## House Files
# 
# We were able to use Selenium to read the files for Senators because they were webpages and not PDFs. Selenium does not work for reading PDFs, which are used for all of the House files. To scrape for the House we have to create a different system. 
# 
# Importantly, the pdf files are linked to through webpages (as indicated by "http://" at the front of each link). So we must:
#     (1) iterate through the list of links
#     (2) open the links as PDFs
#     (3) read them as PDFs
#     (4) output relevant information

# In[15]:


import requests
from PyPDF2 import PdfReader
import pandas as pd
from io import BytesIO

# Web PDF Scraper Function
def pdfScraper(links):
    matches = []  # Initialize matches list
    
    for i, link in enumerate(links, 1):
        print(f"Opening: {link} ; {i} of {len(links)}")
        
        # Skip NaN/null links
        if pd.isna(link): 
            continue
            
        try:
            # Fixed: use 'link' instead of 'url'
            response = requests.get(link, timeout=30)
            response.raise_for_status()
            
            pdf_file = BytesIO(response.content)
            reader = PdfReader(pdf_file)
            
            # Extract text from ALL pages, not just the last one
            full_text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:  # Only add if text exists
                    full_text += page_text + "\n"
            
            # Convert to lowercase for case-insensitive matching
            full_text_lower = full_text.lower()
            
            # Check for keywords in the complete document text
            found_keywords = []
            for keyword in ["ammo", "american outdoor", "big 5", "sturm", "firearm", "range", "shooting",
                           "sportsman's warehouse", "smith", "wesson", "ruger", "axon", "olin", "gun", "vista"]:
                if keyword.lower() in full_text_lower:
                    found_keywords.append(keyword)
            
            # If any keywords found, add to matches
            if found_keywords:
                print(f"🔍 Found keywords {found_keywords} in: {link}")
                matches.append({
                    'url': link,
                    'keywords_found': found_keywords,
                    'text_length': len(full_text)
                })
        
        except Exception as e:
            print(f"❌ Error processing {link}: {e}")
            continue
    
    return matches


# In[11]:


## Test pdfScraper
links = houseDisclosuresMerge25['Report Link'][1:10]
print(links)

pdfScraper(links)


# In[16]:


## Test pdfScraper on full dataset
links = houseDisclosuresMerge23['Report Link']
print(links)

pdfScraper(links)

