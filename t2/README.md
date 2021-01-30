#Crawling, data extraction of a static website
A user asks about how he can obtain data of a website without spending days to extract the data by hand
Look at https://www.urparts.com/index.cfm/page/catalogue and check for a manufacturer, then look into the categories, then the models and the result set where the part (number) before ‘ - ‘ and the part category
crawl the overall at this point in time existing catalogue and create a CSV file with the following data (example with 10 lines):


Need SCRAPY to do this task 

pip install scrapy 

scrapy startproject project . 
scrapy genspider catalog www.urparts.com

go to project -> spiders ->catalog.py and see code


#how to use? 
Spider catalog

scrapy crawl catalog -O 500.csv



 