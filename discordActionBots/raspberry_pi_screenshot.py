from selenium import webdriver   
from selenium.webdriver.common.by import By 
import time
from discord_webhook import DiscordWebhook 

webhook = DiscordWebhook(url="[INSERT DISCORD WEBHOOK URL]", username="Raspberry Pi 4")
  
def main():  
    try: 
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options)
        driver.get("https://pitunnel.com/")

        driver.find_element(By.XPATH, "/html/body/header/nav/div/div[1]/div/ul/li[6]/a").click()

        input1 = driver.find_element(By.XPATH, "//*[@id='id_login']")
        input1.click()
        input1.send_keys("[PITUNNEL USERNAME]")

        input2 = driver.find_element(By.XPATH, "//*[@id='id_password']")
        input2.click()
        input2.send_keys("[PITUNNEL PASSWORD]")

        driver.find_element(By.XPATH, "//*[@id='form_login']/input[2]").click()

        time.sleep(10) 

        final = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]")
        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = f'./raspberry-pi-screenshots/{timestr}.png'
        final.screenshot(filename)

        with open(filename, "rb") as f:
          webhook.add_file(file=f.read(), filename=filename)
 
        webhook.execute()

        print("Has been sent!") 

    except Exception as e:
        print("Couldn't take picture!\n[ERROR] ", e)

if __name__ == "__main__":
    main()