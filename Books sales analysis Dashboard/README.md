# 📚 Book Sales Analysis Dashboard

A full end-to-end **Data Analytics Project** that scrapes product data from an e-commerce site, cleans and transforms it in Excel, and builds a professional interactive dashboard for business insights.

---

## 📦 Project Overview

| Phase | Description |
|-------|-------------|
| 🕸️ Web Scraping | Scraped detailed book data from [books.toscrape.com](http://books.toscrape.com) using Python & BeautifulSoup |
| 📊 Data Cleaning | Processed and transformed the raw dataset in Excel |
| 📈 Dashboard | Built an interactive Excel dashboard using PivotTables, charts, slicers, and formulas |

---

## 🧰 Tools & Technologies

- **Python 3.11** (for web scraping)
  - `requests`, `BeautifulSoup4`, `pandas`
- **Microsoft Excel 365**
  - Data tables, helper columns, advanced formulas (XLOOKUP, TEXT, VALUE, IFERROR)
  - PivotTables, PivotCharts
  - Slicers, Drop-down lists, Navigation buttons

---

## 🔍 Web Scraping Details

Scraped ~1000+ books with the following attributes:

| Column | Description |
|--------|-------------|
| Title | Book title |
| Price | Price in GBP |
| Availability | Stock count (parsed from text like `In stock (19 available)`) |
| Category | Genre/category of the book |
| Rating | Star rating (converted to numeric) |
| Product URL | Link to book detail page |
| Description | (Optional) Book summary (from detail page) |

Python script saved final data into:

- `books_detailed_data.xlsx`

---

## 📊 Excel Dashboard Highlights

| Feature | Description |
|--------|-------------|
| ✅ KPI Cards | Total Revenue, Avg Rating, Total Books, Low Stock Count |
| 📈 Sales Trend | Monthly revenue using `Last Purchase Date` |
| 📚 Top Rated Books | Bar chart of books with rating ≥ 4.5 |
| 💰 Top Sellers | Top 10 books by total sales |
| 📦 Low Stock Alert | Table for books with stock < 5 |
| 🔍 Book Lookup | Dropdown + XLOOKUP to display book info |
| 🎛️ Slicers | Interactive filters for category, stock, buyer type |

---

## 📁 Folder Structure

```bash
📦 book-sales-dashboard/
├── 📁 data/
│   └── books_detailed_data.xlsx     # Cleaned data file
├── 📁 scripts/
│   └── scraper.py                   # Python script for scraping
├── 📁 dashboard/
│   └── Book_Sales_Dashboard.xlsx    # Final Excel dashboard
└── README.md
🚀 How to Use
Step 1: Scrape Data
bash
Copy code
python scripts/scraper.py
Step 2: Open Excel
Open Book_Sales_Dashboard.xlsx

Explore KPI cards, use slicers, try Book Lookup

Filter by category to dynamically update charts

📌 Key Excel Techniques Used
TEXT() to extract month from date

XLOOKUP() for Book Info panel

IF(), VALUE(), SUBSTITUTE() for cleaning

PivotTables, PivotCharts

Slicers, Data Validation dropdowns

Navigation via hyperlinks and buttons

📎 Bonus
Export-ready: Can be saved as PDF for reports

Portfolio-grade project for interviews and case studies

🧠 Learnings
Hands-on scraping and parsing HTML

Real-world Excel dashboard building

Data cleaning & feature engineering logic

Business storytelling using charts

📞 Contact
Feel free to connect:

💼 LinkedIn

📧 your.email@example.com

Built with 💻 Python + 📊 Excel by [Your Name]