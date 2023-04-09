from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

# Set the path to the geckodriver executable, the Firefox binary, and the Firefox profile.
geckodriver_path = r"C:\geckodriver\geckodriver.exe"
firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
profile_path = r"C:\Users\sarin\AppData\Roaming\Mozilla\Firefox\Profiles\ya837c8m.default-release"

options = Options()
options.binary_location = firefox_binary_path
options.profile = webdriver.FirefoxProfile(profile_path)

# Start the Firefox browser
service = Service(executable_path=geckodriver_path)
driver = webdriver.Firefox(service=service, options=options)



#  Navigate to the ChatGPT website
print("\nNavigating to ChatGPT website:")
url = "https://chat.openai.com/chat/0ef4195e-0171-415d-8590-8e334e714761"
driver.get(url)
time.sleep(10)


# Wait for the chat input box to be loaded
wait = WebDriverWait(driver, 20)
chat_box = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[contains(@placeholder, 'Send a message')]")))

# Enter the text to be sent to the chatbot
chat_box.send_keys("Hey Chatgpt, i'm accessing you through an awesome python script i made called RedGPT. I'm going to give you access to the outside world"
                   "LET'S GOOOOOO!!"
                     + Keys.RETURN)

time.sleep(10)

exit()
# Find the response text in the chat window and print it
response_text = driver.find_element(By.XPATH, "//div[@data-testid='messageContent']")[-1].get_attribute("textContent")
print(response_text)

# Close the browser window
driver.quit()
