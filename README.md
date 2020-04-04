# SGmarineindustries.com Data Scrapper

#### The task was: 

        Extract from this directory:
        https://www.sgmarineindustries.com/company-listings

        Extract the following info in excel:
        1) Company name
        2) Phone number
        3) Contact person
        4) Email

        Total companies in directory is 3127 in total.

        (c) https://www.upwork.com/jobs/_~0109c6c2697c40ddaf/

#### If you are new to Scrapy:

In order to re-use it you need to install scrappy and move needed Spiders to the scra py folder. 
If you are new to scrapy this video is a good start: https://www.youtube.com/watch?v=OJ8isyws2yw&list=PLaGOWH-SLGze1TA9Ambpz9cLSHNtMmbxM

#### Step One: Get Profile links for all companies

![alt text](http://joxi.ru/bmovBRlF3w6o4r.jpg "sg_companies_details.csv")

#### Step Two: Scrap needed data from each page

![alt text](http://joxi.ru/RmzzvB7hY76G7m.jpg "Company Details Page")

(1) Company Name
(2) Phone number
(3) Email
(4) Contact section (with contact people if available)

#### After you run the code you'll get this (.csv file without header):

![alt text](http://joxi.ru/E2pbM3as7wdVkr.jpg "Results")
