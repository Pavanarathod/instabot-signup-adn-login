from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
PATH = 'chromedriver.exe'


class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get('https://www.instagram.com/')

        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name('password').send_keys(username)
        # self.driver.find_element_by_xpath().click()


InstaBot("dasrockatansky139@gmail.com", "PavanDas@1996")


# self.driver.implicitly_wait(5)

# cookie = self.driver.find_element_by_id('bigCookie')
# cookie_count = self.driver.find_element_by_id('cookies')

# items = [self.driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1) ]


# actions = ActionChains(self.driver)
# actions.click(cookie)

# for i in range(100):
# 	actions.perform()
# 	count = int(cookie_count.text.split(" ")[0])
# 	for item in items:
# 		value = int(item.text)
# 		if value <= count:
# 			upgrade_actions = ActionChains(self.driver)
# 			update_actions.move_to_element(item)
