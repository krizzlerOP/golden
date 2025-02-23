from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Browser Driver Setup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

# Enable headless mode (runs in the background)
options.add_argument("--headless=new")  # New headless mode
options.add_argument("--disable-gpu")  # Necessary for headless mode
options.add_argument("--window-size=1920,1080")  # Prevent viewport issues
options.add_argument("--no-sandbox")  # Bypass OS security restrictions
options.add_argument("--disable-dev-shm-usage")  # Prevent memory issues
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36")  # Avoid detection

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# List of tokens
tokens = [
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7ImlkIjoiMWFhMGU0NDgtNDkzNy00YWM1LWExODQtODY5MWM4YTNlMTNhIiwiZmlyc3RfbmFtZSI6Im5pdCBhc3NwaWVudCIsImxhbmd1YWdlX2NvZGUiOiJlbiIsInVzZXJuYW1lIjoiYW1zZWVzdGVuIn0sInNlc3Npb25faWQiOjE0MTI5MjAsInN1YiI6IjFhYTBlNDQ4LTQ5MzctNGFjNS1hMTg0LTg2OTFjOGEzZTEzYSIsImV4cCI6MTc0MjY5MjEzNH0.jbMVVxHsvcKq64NZrJoJFadI7w8UB7JqGpg1T4h8Mf4",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7ImlkIjoiMjc3ZDJlOGItMDMwYi00MTE4LWE0OTYtMTdiMTdhMzczNTUxIiwiZmlyc3RfbmFtZSI6ImtyaXp6IGFjNyIsImxhbmd1YWdlX2NvZGUiOiJlbiIsInVzZXJuYW1lIjpudWxsfSwic2Vzc2lvbl9pZCI6MTQxMzA0Miwic3ViIjoiMjc3ZDJlOGItMDMwYi00MTE4LWE0OTYtMTdiMTdhMzczNTUxIiwiZXhwIjoxNzQyNjk0MTQzfQ.KP4OftJ6qtx-ZgjMt31niirmCVKi_tFoVY0oxjW6ufM",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7ImlkIjoiNDFjMjI3ZDEtNTI0My00NDFlLTkwYjUtMjZjY2MyMDMyMDRlIiwiZmlyc3RfbmFtZSI6Im1jc3RhbiIsImxhbmd1YWdlX2NvZGUiOiJlbiIsInVzZXJuYW1lIjoibWNzdGFuaHVtZSJ9LCJzZXNzaW9uX2lkIjoxNDEzMDQzLCJzdWIiOiI0MWMyMjdkMS01MjQzLTQ0MWUtOTBiNS0yNmNjYzIwMzIwNGUiLCJleHAiOjE3NDI2OTQxNTF9.TekSd-y6l9spV50jMgYOHhfLorBf56zrmTEX9F1QKos",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7ImlkIjoiOGI3MzE1ODQtNTQ4ZS00NjE4LWE4NmQtM2QxY2Y0NzQwOTk3IiwiZmlyc3RfbmFtZSI6ImFjYyA2IiwibGFuZ3VhZ2VfY29kZSI6ImVuIiwidXNlcm5hbWUiOm51bGx9LCJzZXNzaW9uX2lkIjoxNDEzMDQ0LCJzdWIiOiI4YjczMTU4NC01NDhlLTQ2MTgtYTg2ZC0zZDFjZjQ3NDA5OTciLCJleHAiOjE3NDI2OTQxNjF9.VAANXyFh626X56yv9I1ZA0FUSj2IlyNFg2XXButIYmg",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7ImlkIjoiMTRmYWM5NWQtNmU5ZC00NjAwLWJiZWYtMTQ0YjI4Nzc0MDdhIiwiZmlyc3RfbmFtZSI6ImFjYyAxMCIsImxhbmd1YWdlX2NvZGUiOiJlbiIsInVzZXJuYW1lIjpudWxsfSwic2Vzc2lvbl9pZCI6MTQxMzA0Nywic3ViIjoiMTRmYWM5NWQtNmU5ZC00NjAwLWJiZWYtMTQ0YjI4Nzc0MDdhIiwiZXhwIjoxNzQyNjk0MTg2fQ.WJIOQnvfREZvuJtf3RLRn4ZRA_kWcejSKpSHJAXY9E4",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7ImlkIjoiMDZhMmI1YmYtNDE3YS00NzU4LWJlYjQtZDcxZGIzNTMyZWUwIiwiZmlyc3RfbmFtZSI6IlZhbGl4VGhvcm4iLCJsYW5ndWFnZV9jb2RlIjoiZW4iLCJ1c2VybmFtZSI6IlZhbGl4VGhvcm4ifSwic2Vzc2lvbl9pZCI6MTQxMzA1MSwic3ViIjoiMDZhMmI1YmYtNDE3YS00NzU4LWJlYjQtZDcxZGIzNTMyZWUwIiwiZXhwIjoxNzQyNjk0MjEzfQ.eBsIJg8M7uM_50lvqSxV4dCX7BRRC-tg4YhqUAmieqY",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7ImlkIjoiOWE3NTE5ODctNjBjMi00YmE5LTg2YjMtYjA4MjIwNzAwOTc5IiwiZmlyc3RfbmFtZSI6Ikp1bm9MaWdodCIsImxhbmd1YWdlX2NvZGUiOiJlbiIsInVzZXJuYW1lIjoiSnVub0xpZ2h0In0sInNlc3Npb25faWQiOjE0MTMwNTcsInN1YiI6IjlhNzUxOTg3LTYwYzItNGJhOS04NmIzLWIwODIyMDcwMDk3OSIsImV4cCI6MTc0MjY5NDI1NX0.NOriVFxrA1apVlstOVnIOHRnlAhJtmdDEQkFUZSgz1M",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7ImlkIjoiY2I5M2EwZmUtYmY0Mi00MDgxLTgxMGMtZGMzNGFjZDhhZjllIiwiZmlyc3RfbmFtZSI6IkJsdWVwcmludCIsImxhbmd1YWdlX2NvZGUiOiJlbiIsInVzZXJuYW1lIjoia2FhbV9icnV0YWwifSwic2Vzc2lvbl9pZCI6MTQxMzA1OSwic3ViIjoiY2I5M2EwZmUtYmY0Mi00MDgxLTgxMGMtZGMzNGFjZDhhZjllIiwiZXhwIjoxNzQyNjk0MjY0fQ.WbYxvaC9sSeUhSBviafSd7Knpe3i5OpGaK3DsTPA00I",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7ImlkIjoiZjY2Njc1NjUtOWIxOS00YzRkLTgyNGEtOTVlMzYwZTdlZDEwIiwiZmlyc3RfbmFtZSI6IlNoaXNodHVtIiwibGFuZ3VhZ2VfY29kZSI6ImVuIiwidXNlcm5hbWUiOiJtZXJpZHVzcmlpZCJ9LCJzZXNzaW9uX2lkIjoxNDEzMDYxLCJzdWIiOiJmNjY2NzU2NS05YjE5LTRjNGQtODI0YS05NWUzNjBlN2VkMTAiLCJleHAiOjE3NDI2OTQyNzd9.QU9kH-ZOBeYE3qJXkmlfFiYIW1QHNiyuBdPzuWXhW9M",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7ImlkIjoiMTAyNmNjY2ItZWQzMC00ZjkyLWI4YjctYTdkYzlmNzMwMGQ0IiwiZmlyc3RfbmFtZSI6IlBpa2EiLCJsYW5ndWFnZV9jb2RlIjoiZW4iLCJ1c2VybmFtZSI6ImluYWN0aXZldGlsbDRtYXl5In0sInNlc3Npb25faWQiOjE0MTMwNjYsInN1YiI6IjEwMjZjY2NiLWVkMzAtNGY5Mi1iOGI3LWE3ZGM5ZjczMDBkNCIsImV4cCI6MTc0MjY5NDMxOX0.Vz0L3PI65Tf0EQVmMcRCMEAJLJHMpzazcT5bKqfnakw",
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7ImlkIjoiMGVlNDA5NTUtY2NjMC00YjAyLTkyYzctMzkzMTY1ZGUyYzJjIiwiZmlyc3RfbmFtZSI6Ik9mZmxpbmUgKERvbid0IERNKSIsImxhbmd1YWdlX2NvZGUiOiJlbiIsInVzZXJuYW1lIjoiWW91ckZhdk5pZ2dhSGVyZSJ9LCJzZXNzaW9uX2lkIjoxNDEzMDMxLCJzdWIiOiIwZWU0MDk1NS1jY2MwLTRiMDItOTJjNy0zOTMxNjVkZTJjMmMiLCJleHAiOjE3NDI2OTQwMDV9.BIVhYHsbWd6Asua0YHkNDihYmXJuBMoN43rf0KqISe8"
]

def tap_button(token):
    try:
        # Open Website
        driver.get("https://telegram.geagle.online/")

        # Inject Auth Token into Local Storage
        driver.execute_script(f"window.localStorage.setItem('session_token', '{token}');")
        driver.refresh()  # Refresh to apply login

        # Wait for page to load
        time.sleep(10)

        # Find the button
        button = driver.find_element(By.CLASS_NAME, "_tapArea_njdmz_15")
        actions = ActionChains(driver)

        # Perform 250 taps instantly
        for _ in range(250):
            actions.move_to_element(button).click().perform()
            print(f"Token: {token[:10]}... | Tap successful [{_+1}/250]")

    except Exception as e:
        print(f"Error with token {token[:10]}...: {e}")

if __name__ == "__main__":
    while True:
        for token in tokens:
            tap_button(token)
            print(f"Completed taps for token: {token[:10]}...")

        print("Waiting 5 minutes before restarting the process...")
        time.sleep(5 * 60)  # Wait for 5 minutes before repeating