import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Read collected book URLs
with open("book_urls.txt", "r") as f:
    book_urls = [line.strip() for line in f.readlines()]

def get_book_data(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        title = soup.select_one("div.product_main h1").text.strip()

        table = soup.select("table.table.table-striped tr")
        data = {row.th.text: row.td.text for row in table}

        description = soup.select_one("#product_description")
        if description:
            desc_text = description.find_next_sibling("p").text.strip()
        else:
            desc_text = ""

        category = soup.select("ul.breadcrumb li a")[-1].text.strip()
        image_url = "http://books.toscrape.com/" + soup.select_one("div.item.active img")["src"].replace("../", "")

        rating_class = soup.select_one("p.star-rating")["class"]
        rating = rating_class[1] if len(rating_class) > 1 else "No rating"

        return {
            "Title": title,
            "UPC": data.get("UPC"),
            "Product Type": data.get("Product Type"),
            "Price (Excl. Tax)": data.get("Price (excl. tax)"),
            "Price (Incl. Tax)": data.get("Price (incl. tax)"),
            "Tax": data.get("Tax"),
            "Availability": data.get("Availability"),
            "Number of Reviews": data.get("Number of reviews"),
            "Rating": rating,
            "Category": category,
            "Description": desc_text,
            "Image URL": image_url,
            "Product Page URL": url
        }
    except Exception as e:
        print(f"Error on {url}: {e}")
        return None

# Scrape all books
all_books = []
for i, url in enumerate(book_urls):
    print(f"[{i+1}/{len(book_urls)}] Scraping: {url}")
    book_data = get_book_data(url)
    if book_data:
        all_books.append(book_data)
    time.sleep(1)  # Polite scraping

# Save to Excel
df = pd.DataFrame(all_books)
df.to_excel("books_detailed_data.xlsx", index=False)
print("\n✅ Done! Data saved to 'books_detailed_data.xlsx'")
