from traceback import extract_stack
import scrapy
import json
from bs4 import BeautifulSoup

class PostsSpider(scrapy.Spider):
    name = "posts"
    
    # It probably could be done more automatically, but its not that important
    # just check how many pages the site has at any point
    start_urls = ["https://www.tvp.info/opinie?page={}".format(page) for page in range(1,83)]

    def parse(self, response):
        print(f"Scraping url {response.url}")
        filename = response.url.split("/")[-1].replace("?page=","_")

        with open(f"scraped_htmls/{filename}.html", 'w', encoding='utf-8') as f:
            f.write(response.text)


        # soup = BeautifulSoup(response.body, "html.parser", from_encoding='iso-8859-2')
        # # soup = BeautifulSoup(response.read().decode('utf-8'))
        # # posts_information = results[7]
        # # print(posts_information.prettify())
        # posts_information = soup.find_all("script", type="text/javascript")[7]
        # json_data = str(posts_information)
        # json_data = json_data.split("\"items\":")[1].split("\"items_total_count\"")[0].rstrip().rstrip(",").rstrip()
        # with open('data.json', 'w', encoding='utf-8') as f:
        #     json.dump(json_data, f, ensure_ascii=False, indent=4)
        # # jsondata = json.loads(str(posts_information))        
        # # print(posts_information.prettify())

