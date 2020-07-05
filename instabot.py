from selenium import webdriver
from time import sleep
from secrets import pw

class InstaBot:
    def __init__(self,username,pw):
        self.driver=webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        
        '''self.driver.find_element_by_xpath("//a[contains(text(),'Log in')]")\
            .click()'''

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')\
            .send_keys(username)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')\
            .click()
        sleep(2)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/div[3]/button')\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a')\
            .click()
        sleep(100)
        

    '''def get_unfollowers(self):
        self.driver.find_elements_by_xpath("//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a".format(self.username))\
            .click()'''

my_bot = InstaBot('tsfthanseef',pw)
#my_bot.get_unfollowers()

'''//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[1]/a'''


('cristiano')