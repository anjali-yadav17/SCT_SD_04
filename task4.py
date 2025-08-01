from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time
import re

search_term = input("🔍 Enter AJIO product search term (e.g., sneakers for men): ").strip().replace(" ", "%20")
base_url = "https://www.ajio.com"
max_pages = 3 

# 🚀 Set up Chrome browser options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 📁 Prepare CSV file
csv_filename = f"{search_term.replace('%20', '_')}_ajio_products.csv"
with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Original Price", "Discount %", "Product URL", "Image URL"])

    for page in range(1, max_pages + 1):
        url = f"https://www.ajio.com/search/?text={search_term}&page={page}"
        print(f"🔄 Scraping page {page}: {url}")
        driver.get(url)

        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@class="item rilrtl-products-list__item item"]'))
            )
            time.sleep(2)
            products = driver.find_elements(By.XPATH, '//div[@class="item rilrtl-products-list__item item"]')
        except:
            print("❌ Products did not load. Stopping.")
            break

        if not products:
            print("❌ No products found. Stopping.")
            break

        for product in products:
            try:
                name = product.find_element(By.CLASS_NAME, 'nameCls').text
            except:
                name = "N/A"

            try:
                price_text = product.find_element(By.CLASS_NAME, 'price').text
                original_price_match = re.search(r'₹\s?([\d,]+)', price_text)
                if original_price_match:
                    original_price = original_price_match.group(1).replace(",", "")
                else:
                    original_price = "N/A"
            except:
                original_price = "N/A"

            try:
                discount = product.find_element(By.CLASS_NAME, 'discount').text
                discount_percentage_match = re.search(r'(\d+)%', discount)
                discount_percent = discount_percentage_match.group(1) + "%" if discount_percentage_match else "N/A"
            except:
                discount_percent = "N/A"

            try:
                product_url = product.find_element(By.TAG_NAME, "a").get_attribute("href")
            except:
                product_url = "N/A"

            try:
                image_url = product.find_element(By.TAG_NAME, "img").get_attribute("src")
            except:
                image_url = "N/A"

            writer.writerow([name, original_price, discount_percent, product_url, image_url])

        print(f"✅ Page {page} scraped.")

driver.quit()
print(f"\n✅ Scraping complete. Data saved to '{csv_filename}'")