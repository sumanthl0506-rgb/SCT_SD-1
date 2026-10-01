import requests
from bs4 import BeautifulSoup
import csv

print("--- Task 04: E-Commerce Scraper | SkillCraft Technology ---")

# Using BooksToScrape - a practice e-commerce site allowed for scraping
url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

products = []
books = soup.find_all("article", class_="product_pod")

for book in books:
    name = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating_tag = book.find("p", class_="star-rating")
    rating = rating_tag["class"][1] # One, Two, Three etc
    products.append([name, price, rating])
    print(f"Found: {name[:30]} | {price} | Rating: {rating}")

# Save to CSV
csv_file = "products.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product_Name", "Price", "Rating"])
    writer.writerows(products)

print(f"\nSuccessfully scraped {len(products)} products!")
print(f"Data saved to {csv_file}")
print("Task 04 Completed - Data in structured CSV format")
