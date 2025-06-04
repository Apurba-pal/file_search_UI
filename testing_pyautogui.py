import os
import time
import pyautogui

# STEP 1: Launch WhatsApp from Microsoft Store
print("Launching WhatsApp...")
os.system('start "" "shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"')
time.sleep(3)  # Wait for WhatsApp to fully open

# STEP 2: Click on the search bar
print("Clicking on search bar...")
pyautogui.click(x=200, y=100)  # 🔧 Change to actual search bar position
time.sleep(1)

# STEP 3: Type contact name
contact_name = "Suvendu"
pyautogui.write(contact_name, interval=0.1)
time.sleep(2)

# STEP 4: Click on contact from search result
print("Clicking on contact...")
pyautogui.click(x=200, y=200)  # 🔧 Change to the actual contact position
time.sleep(2)

# STEP 5: Type and send message
message = "Hello from my AI assistant ( banchod edition ) 🤖!"
pyautogui.write(message, interval=0.05)
pyautogui.press("enter")

print("✅ Message sent!")