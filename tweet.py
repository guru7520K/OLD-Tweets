from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# replace with the Twitter handle of the user whose tweets you want to see
twitter_handle = "GuruPra64610906"

# replace with the path to your chromedriver executable
driver = webdriver.Chrome("/path/to/chromedriver")

# navigate to the user's profile
driver.get("https://twitter.com/" + twitter_handle)

# scroll down to the bottom of the page
body = driver.find_element(By.TAG_NAME, "body")
for i in range(500):
    body.send_keys(Keys.END)
    time.sleep(1)

# find and print the oldest tweet on the page
tweets = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='tweet']")
oldest_tweet = tweets[-1]
print(oldest_tweet.text)

# close the browser
driver.quit()



# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# # replace with the Twitter handle of the user whose tweets you want to see
# twitter_handle = "twitter"

# # replace with the path to your chromedriver executable
# driver = webdriver.Chrome("/path/to/chromedriver")

# # navigate to the user's profile
# driver.get("https://twitter.com/" + twitter_handle)

# # scroll down to the bottom of the page
# body = driver.find_element(By.TAG_NAME, "body")
# for i in range(10):
#     body.send_keys(Keys.END)
#     time.sleep(1)

# # find and print the oldest tweet on the page
# tweets = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='tweet']")
# if tweets:
#     oldest_tweet = tweets[-1]
#     print(oldest_tweet.text)
# else:
#     print("No tweets found on the page.")





























# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# # replace with the Twitter handle of the user whose tweets you want to see
# twitter_handle = "anirudhofficial"

# # replace with the path to your chromedriver executable
# driver = webdriver.Chrome("/path/to/chromedriver")

# # navigate to the user's profile
# driver.get("https://twitter.com/" + twitter_handle)

# # scroll down to the bottom of the page
# body = driver.find_element_by_tag_name("body")
# for i in range(10):
#     body.send_keys(Keys.END)
#     time.sleep(1)

# # find and print the oldest tweet on the page
# oldest_tweet = driver.find_elements_by_css_selector("div[data-testid='tweet']")[-1]
# print(oldest_tweet.text)

# # close the browser
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# # replace with the Twitter handle of the user whose tweets you want to see
# twitter_handle = "anirudhofficial"

# # replace with the path to your chromedriver executable
# driver = webdriver.Chrome("/path/to/chromedriver")

# # navigate to the user's profile
# driver.get("https://twitter.com/" + twitter_handle)

# # scroll down to the bottom of the page
# body = driver.find_element(By.TAG_NAME, "body")
# for i in range(10):
#     body.send_keys(Keys.END)
#     time.sleep(1)

# # find and print the oldest tweet on the page
# oldest_tweet = driver.find_elements_by_css_selector("div[data-testid='tweet']")[-1]
# print(oldest_tweet.text)

# # close the browser
# driver.quit()
