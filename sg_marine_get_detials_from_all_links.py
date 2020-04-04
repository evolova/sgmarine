import scrapy
import re
from bs4 import BeautifulSoup
import csv

class DataSpider(scrapy.Spider):
    name = 'sg_get_details'

    def start_requests(self):
        with open('sg_get_details.csv','r') as csvinput:
            r = csv.reader(csvinput)
            for url in r:
                yield scrapy.Request(url=url[0], callback=self.parse)

    def parse(self, response):

        results = []

        company = response.xpath('//*[@id="Contentplaceholder1_T5CE92B6B022_Col01"]/div[3]/div[2]/h3').extract()
        if len(company) < 1:
            company = company + response.xpath('//*[@id="Contentplaceholder1_T5CE92B6B022_Col01"]/div[3]/div[2]/p').extract()
        regex_pattern_company = r'(?<=>).*(?=<)'
        company = results.append(re.findall(regex_pattern_company, company[0])[0])


        links = response.xpath('//*[@id="valuephone"]/a').extract()
        regex_pattern = r'(?<=tel:)\+\d*'
        tel = results.append(re.findall(regex_pattern, links[0])[0])


        email = response.xpath('//*[@id="textemail"]').extract()
        regex_pattern_email = r"(?<=showCompanyEmail\(').*(?=\'\,)"
        try:
            email = results.append(re.findall(regex_pattern_email, email[0])[0])
        except:
            results.append("not found")

        contact = ' '.join(BeautifulSoup(response.xpath('//*[@id="Contentplaceholder1_T5CE92B6B022_Col01"]/div[3]/div[2]/div/div[1]').extract()[0]).get_text().split())

        regex_pattern_contact = r"(?<=Contact).*"
        contact = results.append(re.findall(regex_pattern_contact,contact)[0])

        results.append(response.url)

        import csv
        self.log(results)
        with open(r'sg_companies_details.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(results)
