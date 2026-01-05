import requests
import lxml.html
try:
    mckdown=requests.get('https://store.steampowered.com/explore/new/')
    item=lxml.html.fromstring(mckdown.content)
    print("The site is downloaded successfully and converted into a searchable format")
except:
    print("Failed to downlaad the site or convert it into a searchabable format ")
new_releases = item.xpath('//div[@id="tab_newreleases_content"]')[0]
titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')
print("GAME NAMES:")
for title in titles:
    print(f"  - {title}")

print("\nGAME PRICES:")
for price in prices:
    print(f"  - {price}")
    