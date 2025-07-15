import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://books.toscrape.com/"

#Get all category page URLS
def get_all_category_urls():
    res = requests.get(BASE_URL)
    soup= BeautifulSoup(res.text, "html.parser")
    category_links = soup.select(".side_categories ul li ul li a")
    category_urls = [BASE_URL + link['href']for link in category_links]
    return category_urls

#Get all book age URLS from paginated category
def get_all_book_urls_from_category(category_url):
    book_urls =[]
    page_url = category_url
    while True:
        res = requests.get(page_url)
        soup = BeautifulSoup(res.text, "html.parser")
        books = soup.select("article.product_pod h3 a")
        for book in books:
            relative_url = book['href'].replace("../../../","")
            book_urls.append(BASE_URL + "catalogue/" + relative_url)
        
        #check for next page
        next_button = soup.select_one("li.next a")
        if next_button:
            next_page =next_button["href"]
            if "catalogue/" not in page_url:
                page_url = category_url.replace("index.html","")+ next_page
            else:
                page_url =page_url.rsplit("/",1)[0]+"/"+next_page
        else: 
            break
        time.sleep(1)
    return book_urls

#Main:Loop over all categories
all_book_urls=[]
category_urls =get_all_category_urls()
print(f"Found {len(category_urls)} categories.")

for cat_url in category_urls:
    print(f"Processing category: {cat_url}")
    book_links = get_all_book_urls_from_category(cat_url)
    print(f"-> Found {len(book_links)} books.")
    all_book_urls.extend(book_links)

#save to file
with open("book_urls.txt", "w") as f:
    for url in all_book_urls:
        f.write(url + "\n")
print(f"\n Total Books Collected:{len(all_book_urls)}")
