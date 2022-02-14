from selenium import webdriver
def launchBrowser():
    browser = webdriver.chrome()
    browser.get("https://www.google.com/")
launchBrowser()