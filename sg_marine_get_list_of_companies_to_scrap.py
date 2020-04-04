import scrapy
import re
import csv

class DataSpider(scrapy.Spider):
    name = 'sg_companies_links'

    def start_requests(self):
        # first we are creating a list of URLs to scrap the Company Details pages from
        base_url = 'https://www.sgmarineindustries.com/company-listings?page='
        urls = []
        for ii in range(int(3127/10)+1):
        # 3127 is the total number of total entities shown on the top of each company-listing page;
        # 10 is the number of results per page
            url = base_url + str(ii)
            urls.append(url)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("=")[1]
        links = response.xpath('/html/body/form/div[3]/div/div[2]/div[2]/div[2]/div/div/div[2]/h3/a').extract()

        if len(links) < 10:
            links_2 = response.xpath('//*[@id="Contentplaceholder1_T5CE92B6B022_Col01"]/div[2]/div/div/div[2]/p[1]/a').extract()
            links = links + links_2
        self.log(links)

        regex_pattern = r'(?<=<a href=").*(?=")'
        results = []

        for item in links:
            link = "https://www.sgmarineindustries.com" + re.findall(regex_pattern, item)[0]
            results.append(link)

            # this is a csv file listing all 3127 Company Details pages' urls which will be used for another crawler
            with open(r'sg_get_details.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([link])
