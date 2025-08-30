import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get the absolute path to the HTML files
        base_path = os.path.abspath('.')

        # Verify index.html
        page.goto(f"file://{base_path}/index.html")
        page.screenshot(path="jules-scratch/verification/index.png")

        # Verify about.html
        page.goto(f"file://{base_path}/about.html")
        page.screenshot(path="jules-scratch/verification/about.png")

        # Verify publications.html
        page.goto(f"file://{base_path}/publications.html")
        page.screenshot(path="jules-scratch/verification/publications.png")

        # Verify contact.html
        page.goto(f"file://{base_path}/contact.html")
        page.screenshot(path="jules-scratch/verification/contact.png")

        browser.close()

if __name__ == "__main__":
    run()
