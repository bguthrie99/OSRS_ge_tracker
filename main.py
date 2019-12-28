
from bs4 import BeautifulSoup
from osrsbox import items_api
import cfscrape

all_db_items = items_api.load()

print("Welcome to OSRS GE Scraper!")
print("Please type 'quit' to exit.\n")

flag = 1
while flag == 1:
    item_name = input("Please enter item name: ")
    if item_name == "quit":
        flag = 0
        break
        break
    item_name = item_name.capitalize()

    for item in all_db_items:
        if item_name == item.name and item.tradeable_on_ge:
            obj_val = item.id


    for k in range(len(item_name)):
        if item_name[k] == " ": slice_start = k

    item_name_revised = item_name[0:slice_start] + "+" + item_name[slice_start+1:len(item_name)]

    url = "http://services.runescape.com/m=itemdb_oldschool/" + item_name_revised + "/viewitem?obj=" + str(obj_val)

    scraper = cfscrape.create_scraper()

# initialize our scraper
    page = scraper.get(url).content

    soup = BeautifulSoup(page, "html.parser")
# h3 is the only header where the current price data is given
    information = soup.find("h3")
# here we will convert this to a string
    info_string = str(information)

# Loop to check when to cut off copying the integer
# max_range is the index before the ">" character
# Example code we are checking:
# <h3>Current Guide Price <span title='1,034,241,220'>	1.0b
#                                                   ^ this is at index 51
# </span></h3>
    for i in range(0, 52):
        temp_check = info_string[i]
        if temp_check == ">": max_range = i-1

# Most significant value will always start at index 37 of the scraped data
    print("Price: " + info_string[37:max_range])

