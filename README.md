# Member-Firearms-Investment-Tracker
The goal of this project was to scrape the Congressional disclosures record to find evidence of members investing directly into the firearms industry. I leveraged web scraping to automate this process. I constructed web scrapers using Selenium and PyPDF2, to read Financial Disclosure reports and detect keywords that are related to the gun industry.

Below is a list of keywords used for search:

Top 10 Gun Stocks
- AMMO, Inc. (NASDAQ: POWW)
- National Presto Industries, Inc. (NYSE: NPK)
- American Outdoor Brands, Inc. (NASDAQ: AOUT)
- Big 5 Sporting Goods Corporation (NASDAQ: BGFV) 
- Smith & Wesson Brands, Inc. (NYSE: SWBI) 
- Sportsman’s Warehouse Holdings, Inc. (NASDAQ: SPWH)
- Sturm, Ruger & Company, Inc. (NYSE: RGR) 
- Vista Outdoor Inc. (NYSE: VSTO)
- Axon Enterprise, Inc. (NASDAQ: AXON) 
- Olin Corporation (NYSE: OLN) 

Miscellaneous terms searched for:
- Firearm
- Shooting
- Armory
- Gun
- Range

Senate Disclosures Database
I drew from the Senate Ethics Committee Financial Disclosures (eFD) database to acquire data to scrape. In the spreadsheet linked above is the record of financial disclosures from 01/01/2023 - 08/05/2025, spread across three sheets corresponding to each full year (i.e. 2023, 2024). These years correspond to the filing date of the disclosures, but are not necessarily representative of when a member acquired or sold a given asset. 

To acquire the data for a given year, I accepted the legal acknowledgement which then leads to a “Find Reports” page. Under “Search Options” I filtered for a certain year using the “Date Filed/Received“ filter, clicked search, and was returned with a table of financial disclosures from that year. I highlighted the entirety of the output table and copied it into the googlesheet (may take highlighting multiple pages, I suggest scrolling to the bottom and toggling the “Show ___ entries” button and selecting “100”. 

Because the links to financial disclosure forms are embedded in text of the “Report Type” column, I created a googlesheet function to extract those links and put them into their own column. The function is below, to activate it on googlesheets, at the top click “Extensions” -> “Apps Script” then copy and paste the function. Watch this video of you find trouble.

function GetURL(input) {
 var myFormula = SpreadsheetApp.getActiveRange().getFormula();
 var myAddress = myFormula.replace('=GetURL(','').replace(')','');
 var myRange = SpreadsheetApp.getActiveSheet().getRange(myAddress);
 return myRange.getRichTextValue().getLinkUrl();
}

After extracting the links into a separate column “Report Link”, I downloaded the data on my computer and was then able to run it in the webcrawler.

House Disclosures Database
I drew from the House Ethics Committee Financial Disclosures (eFD) database to acquire data to scrape. In the spreadsheet linked above is the record of financial disclosures from 01/01/2023 - 08/05/2025, spread across three sheets corresponding to each full year (i.e. 2023, 2024). These years correspond to the filing date of the disclosures, but are not necessarily representative of when a member acquired or sold a given asset. 

To acquire the data for a given year, I navigated to the “Search” link on the home webpage, and filtered by “Filing Year” the year I wanted to scrape. This provided a table of search results that I then copied and pasted into a googlesheet. Only 10 outputs are provided at a time, so it takes a lot of copying and pasting, so if you’re replicating this for a given year do not be discouraged. 

Because the links to financial disclosure forms are embedded in text of the “Report Type” column, I created a googlesheet function to extract those links and put them into their own column. The function is below, to activate it on googlesheets, at the top click “Extensions” -> “Apps Script” then copy and paste the function. Watch this video of you find trouble.

function GetURL(input) {
 var myFormula = SpreadsheetApp.getActiveRange().getFormula();
 var myAddress = myFormula.replace('=GetURL(','').replace(')','');
 var myRange = SpreadsheetApp.getActiveSheet().getRange(myAddress);
 return myRange.getRichTextValue().getLinkUrl();
}

After extracting the links into a separate column “Report Link”, I downloaded the data on my computer and was then able to run it in the PDF reader.

There are two files in this github repo:
(1) A .ipynb file (Jupyter Notebook) that has the code that is necessary to run, commented with instructions for use in a Jupyter environment, and the outputs of sample code that demonstrates functionality.
(2) A .py file that is the base Python script without sample outputs.
