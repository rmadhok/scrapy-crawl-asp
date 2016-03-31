## Heavy-Duty Web Crawling Framework for Scraping Data from ASP.net Pages

### Introduction
This project aims to scrape data from all 250+ pages from [this webpage](http://environmentclearance.nic.in/gotosearch.aspx?pid=ECGranted). The page is written in the ASP.net environment so there is not a separate URL for each page. Clicking on the next page at the bottom instead triggers a `javascript __doPostback` function which takes some visible and some hidden arguements. The goal is to use the scrapy framework to iterate through each page, scrape the fields I need, and pipe it to a csv. 

### Method
Although python cannot interact with the javascript function, we can pass the arguments as form data using the scrapy `Formrequest` library. To goal is to collect the `VIEWSTATE` and `EVENTVALIDATION` hiddent arguements and pass it with the other orther arguements to navigate to each subsequent page. The site should interpret this as a human rather than a bot. If this doesn't work, other options include Seleneium or a headless browser. 

### Files
* items.py: Initiates an item class that acts as a container for the data fields we need
* pipelines.py: Sets up a pipeline to take item objects and pipe it to a CSV
* ec_spider.py: Main scraping script. Passes each scraped item row-by-row through the pipeline and into the dataset

### To-Do
* ~~Git~~
* ~~Download scrapy~~
* ~~Set up container, pipeline, and settings~~
* ~~Test scraping code for first page~~
* Generalize to all pages
* Figure out doPostback issue

### Sources
* [stack overflow question 1](http://stackoverflow.com/questions/23885771/scraping-with-dopostback-with-link-url-hidden)
* [stack overflow question 2](http://stackoverflow.com/questions/15560746/troubles-using-scrapy-with-javascript-dopostback-method)
