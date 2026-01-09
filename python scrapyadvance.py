from playwright.sync_api import sync_playwright
with sync_playwright() as p:
     browser = p.chromium.launch(headless=False)
     page = browser.new_page()
     page.goto('https://www.zara.com/in/en/s-man-50-off-l10330.html?v1=2584161&regionGroupId=230')
     page.wait_for_load_state('domcontentloaded', timeout=100000000)
     titles = page.locator('h3').all_text_contents()
     print("✅ SUCCESS! Found products:")
     for i, title in enumerate(titles[:10], 1) :
        print(f"  {i}. {title.strip()}")
     print("browser closed")
     browser.close()