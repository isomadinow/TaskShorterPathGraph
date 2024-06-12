import pandas as pd
from playwright.sync_api import sync_playwright

def scrape_python_releases(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url,timeout=0)
        
      
        page.wait_for_selector('.list-row-container.menu li')

        releases = []
        
        rows = page.query_selector_all('.list-row-container.menu li')
        for row in rows:
            try:
                release_version_element = row.query_selector('.release-number a')
                release_date_element = row.query_selector('.release-date')
                download_link_element = row.query_selector('.release-download a')
                release_notes_link_element = row.query_selector('.release-enhancements a')

                if not release_version_element or not release_date_element or not download_link_element or not release_notes_link_element:
                    continue  # Skip this row if any element is missing

                release_version = release_version_element.inner_text()
                release_date = release_date_element.inner_text()
                download_link = download_link_element.get_attribute('href')
                release_notes_link = release_notes_link_element.get_attribute('href')
                
                releases.append({
                    "Release Version": release_version,
                    "Release Date": release_date,
                    "Download Link": f"https://www.python.org{download_link}",
                    "Release Notes Link": release_notes_link
                })
            except Exception as e:
                print(f"Ошибка при обработке строки: {e}")
                continue

        browser.close()
        return releases

def save_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

if __name__ == "__main__":
    url = "https://www.python.org/downloads/"
    data = scrape_python_releases(url)
    save_to_excel(data, 'python_releases.xlsx')
