
# SCT_SD_04

Create a program that extracts product information, such as names, prices, and ratings, from an online e-commerce website and stores the data in a structured format like a CSV file.

---

## 📌 Task Overview

A Python-based web scraper that extracts product information from [AJIO.com](https://www.ajio.com) and stores the data in a structured CSV format.

---

## 🚀 Features

- 🔍 Search any product on AJIO via terminal input
- 🧾 Extracts:
  - 🏷️ Product Name
  - 💰 Original Price
  - 🎯 Discount Percentage
  - 🔗 Product URL
  - 🖼 Product Image URL
- 📁 Saves results into a well-formatted `.csv` file
- 🔐 Handles missing data gracefully

---

## 🧰 Technologies Used

- 🐍 Python 3.x
- 🌐 Selenium
- 🔧 WebDriver Manager
- 📦 Built-in CSV Module

---

## 💻 Prerequisites

Make sure you have the following installed:

- Python 3.x
- Google Chrome browser

### Install Required Packages

```bash
pip install selenium webdriver-manager
```

---

## 🛠️ Setup Instructions

1. Clone or download the `task4.py` file from the repository.
2. Run the script from the terminal:

```bash
python task4.py
```

3. Enter the product name when prompted (e.g., `sneakers for men`).
4. The scraper will:
   - Open Chrome
   - Scrape product data from AJIO till 1 page (can be modified)
   - Save it into a CSV file named like: `sneakers_for_men_ajio_products.csv`

---

## 📄 Output Format (CSV)

| Name | Original Price | Discount % | Product URL | Image URL |
|------|----------------|------------|-------------|-----------|
| Nike Air Max | 7999 | 40% | https://ajio.com/... | https://ajio.com/... |
| Puma Slides  | 2499 | 50% | https://ajio.com/... | https://ajio.com/... |

---

## 📄 License

This codebase was created for an internship project and is intended for educational use only.  
**© 2025 Anjali Yadav ([@anjali-yadav17](https://github.com/anjali-yadav17))**

---

## ✍️ Author

**Anjali Yadav**  


