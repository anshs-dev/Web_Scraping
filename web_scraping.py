# STEP 1: Import required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


# STEP 2: Request the first page of the website
url = "http://books.toscrape.com/index.html"
response = requests.get(url)

# STEP 3: Check request status
print("Status code:", response.status_code)


# STEP 4: Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")


# STEP 5: Find all book cards on the first page
books = soup.find_all("article", class_="product_pod")
print("Books found:", len(books))


# STEP 6: Create list to store book data
data = []


# STEP 7: Extract details from each book card
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text.strip()

    rating_class = book.find("p", class_="star-rating")["class"]
    rating = rating_class[1]

    availability = book.find("p", class_="instock availability").text.strip()

    data.append({
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Availability": availability
    })


# STEP 8: Convert data into DataFrame
df = pd.DataFrame(data)


# STEP 9: Save to CSV file
df.to_csv("books_first_page.csv", index=False)


# STEP 10: Confirm and preview
print("✅ books_first_page.csv created successfully")
df
