# Sample calculator automation using Appium

# Getting started
***
*You have to update DESIRED_CAPS in conftest.py 
##### Run Appium 
`$ appium` 
##### Connect android phone to pc or run any Emulator 
##### Run command 
`$ adb devices` 
##### Get your Android device name and put it to conftest.py -> DESIRED_CAPS['deviceName'] 
##### Check and change DESIRED_CAPS['platformVersion']


*Install base.apk on your android or add path to apk file in DESIRED_CAPS
*pip install -r requirements.txt

# Running the test
***
`pytest -v test_main_window.py`




