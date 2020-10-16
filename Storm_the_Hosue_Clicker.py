import time as t
import math as m
import pyautogui
import PIL.ImageGrab as imageGrab

too_close_radius = 30
col = 0
row = 0
black_pixels= []
#previous_x = None
#previous_y = None
previous_pixel = (0, 0, 0)
startTrigger = "2"
def find_black(previous_pixel):
    image = imageGrab.grab(bbox = (600, 600, 1050, 865))
    pixels = image.load()
    width, height = image.size
    for col in range(width):
        for row in range(height):
            pixel = pixels[col, row] #finds pixel
            if pixel == (0, 0, 0): #checks if black
                print ((pixels)) #same hex retern for black pixel 
#previous_x = col
#previous_y = row
                #if col - previous_pixel[0] < too_close_radius or row - previous_pixel[1] < too_close_radius: #checks if close to previous black pixel
                    #too_close = True #attempts to take tuple from int and compare to an int
                    #break                       #####UNABLE TO USE MATHS ON A HEXADECIMAL VALUE, NON-INTERPRETED
                #else:
#click_black() #clicks if not close to previous
                    #pyautogui.doubleClick(x=col + 600, y=row + 600)
                    #too_close = False
                    #previous_pixel = pixel

                    
                    
                    
#may have to intergrate clicking function to keep for loop going.############## may be fine as is
#black_pixels.append((col, row))
#print (black_pixels)



def click_black():
    #pyautogui.click(x=col + 600, y=row + 600)
    pyautogui.doubleClick(x=col + 600, y=row + 600)
    #print (black_pixels)
    t.sleep(1)
    

def start():
    startTrigger = input ("Type '1' to start...")
    print (startTrigger)
    if startTrigger == str(1):
        find_black(previous_pixel)
    else:
        start()

#start()

#image = imageGrab.grab(bbox = (600, 600, 1050, 865))
#image.show()
find_black(previous_pixel)