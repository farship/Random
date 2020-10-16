
import pyautogui
import time

hire_previous_1X = 1500
hire_previous_1Y = 80
hire_previous_2X = 1500
hire_previous_2Y = 80
levelupchair_X = 1620
levelupchair_Y = 980

#Following are coordinates for each chair
    #8: Set to not interfer with pop-up when hiring
    #1: Set as the first hiring chair position
    #All values rounded to nearest ten to look nice

click_chair_11X = 1430
click_chair_11Y = 530
click_chair_10X = 1190
click_chair_10Y = 660
click_chair_9X = 940
click_chair_9Y = 810
click_chair_8X = 820
click_chair_8Y = 800
click_chair_7X = 970
click_chair_7Y = 550
click_chair_6X = 1230
click_chair_6Y = 400
click_chair_5X = 1000
click_chair_5Y = 290
click_chair_4X = 760
click_chair_4Y = 430
click_chair_3X = 560
click_chair_3Y = 590
click_chair_2X = 320
click_chair_2Y = 460
click_chair_1X = 560
click_chair_1Y = 320

reached10000lvlsX = 890
reached10000lvlsY = 40
sellcompanybuttonX = 1100
sellcompanybuttonY = 920

#while 1==1: #Used to get coordinates for different spots
#    input()
#    getcoordinates = pyautogui.position()
#    print (getcoordinates)

def lvlupthosechairs(): #Clicks 125 times over 6.25 seconds taking all employees to max
    pyautogui.click(x=levelupchair_X, y=levelupchair_Y, clicks=125, interval=0.05)

def lvlupthosechairsX(): #Clicks taking employees to max
    pyautogui.click(x=levelupchair_X, y=levelupchair_Y, clicks=1)

def LevelUpCompany(repeatsdone, repeats):
    if (repeatsdone == repeats):
        print ("How many levels do you want to progress?")
        repeats = int(input())
        LevelUpCompany(0, repeats)
    else:
        pyautogui.click(x=click_chair_1X, y=click_chair_1Y) #opens emplyee menu
        time.sleep(0.5)
        pyautogui.click(x=hire_previous_1X, y=hire_previous_1Y) #hires first 7 employees
        time.sleep(0.5)
        pyautogui.click(x=click_chair_9X, y=click_chair_9Y)
        time.sleep(0.5)
        pyautogui.click(x=hire_previous_2X, y=hire_previous_2Y) #hires the last 4 employees
        time.sleep(0.5)
        pyautogui.click(x=click_chair_11X, y=click_chair_11Y)
        time.sleep(0.5)
        lvlupthosechairs() #levels up chair 11
        pyautogui.click(x=click_chair_10X, y=click_chair_10Y)
        time.sleep(0.5)
        lvlupthosechairs() #levels up chair 10
        pyautogui.click(x=click_chair_9X, y=click_chair_9Y)
        time.sleep(0.5)
        lvlupthosechairs() #levels up chair 9
        pyautogui.click(x=click_chair_8X, y=click_chair_8Y)
        time.sleep(0.5)
        lvlupthosechairsX() #levels up chair 8
        pyautogui.click(x=click_chair_7X, y=click_chair_7Y)
        time.sleep(0.5)
        lvlupthosechairsX() #levels up chair 7
        pyautogui.click(x=click_chair_6X, y=click_chair_6Y)
        time.sleep(0.5)
        lvlupthosechairsX() #levels up chair 6
        pyautogui.click(x=click_chair_5X, y=click_chair_5Y)
        time.sleep(0.5)
        lvlupthosechairsX() #levels up chair 5
        pyautogui.click(x=click_chair_4X, y=click_chair_4Y)
        time.sleep(0.5)
        lvlupthosechairsX() #levels up chair 4
        pyautogui.click(x=click_chair_3X, y=click_chair_3Y)
        time.sleep(0.5)
        lvlupthosechairsX() #levels up chair 3
        pyautogui.click(x=click_chair_2X, y=click_chair_2Y)
        time.sleep(0.5)
        lvlupthosechairsX() #levels up chair 2
        pyautogui.click(x=click_chair_1X, y=click_chair_1Y)
        time.sleep(0.5)
        lvlupthosechairsX() #levels up chair 1
        pyautogui.click(x=reached10000lvlsX, y=reached10000lvlsY) #Clicks selling banner
        time.sleep(0.5)
        pyautogui.click(x=sellcompanybuttonX, y=sellcompanybuttonY) #Sells company
        time.sleep(3)
        repeatsdone = repeatsdone + 1
        print (str(repeatsdone))
        LevelUpCompany(repeatsdone, repeats)

LevelUpCompany(0,0)
