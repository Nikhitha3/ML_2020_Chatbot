'''
This functions returns the greeting message according to the tym
'''
from datetime import datetime
import random
def current_time():
    current_time = datetime.now()
    greeting="Good morning"
    if current_time.hour>12 and current_time.hour<17:
        greeting="Good afternoon"
    elif current_time.hour>=17 and current_time.hour<22:
        greeting="Good evening"
    elif current_time.hour>=22:
        greeting="Hi, its too late"
    return greeting
'''
This function gives the welcome message
'''

def welcome(name):
    message = [
        "How may I help you?",
        "Is there anything I can help with?",
        "How can i help you?"
    ]
    print(f"{current_time()}! {name}, {random.choice(message)}")

def show_opt():
    print("1. List of Best Mobiles")
    print("2. List of Latest and Trending Mobiles")
    print("3. End the chat")
    print("---------------------------")
    try:
        return(int(input("Enter your choice[1-3]: ")))
    except :
        print("Only enter choice from 1, 2and 3")
        return 0

def list_mob():
    print("Select Your choice from 1 to 5")
    def mob_list():
        print("1. ONE PLUS 8T")
        print("2. SAMSUNG GALAXY NOTE 20 ULTRA 5G")
        print("3. ASUS ROG ")
        print("4. VIVO X50 PRO")
        print("5. End chat")
        print("---------------------------")
        try:
            return(int(input("Select Your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def one_8t():
        print("ONE PLUS 8T")
        print("Display - 6.55 inch,1080×2400 pixels")
        print("RAM - 12Gb")
        print("Storage - 256GB")
        print("Battery Capacity - 4500mAh")
        print("Front Camera - 16MP")
        print("Rear Camera - 48MP + 16MP + 5MP + 2MP")
        print("--------------------------------------")
    def sam_gal():
        print("SAMSUNG GALAXY NOTE 20 ULTRA 5G")
        print("Display - 6.90 inch,1440×3200 pixels")
        print("RAM - 12Gb")
        print("Storage - 128GB")
        print("Battery Capacity - 4500mAh")
        print("Front Camera - 10MP")
        print("Rear Camera - 108MP + 12MP + 12MP")
        print("--------------------------------------")
    def as_us():
        print("ASUS ROG ")
        print("Display - 6.59 inch,1080×2340 pixels")
        print("RAM - 8Gb")
        print("Storage - 128GB")
        print("Battery Capacity - 6000mAh")
        print("Front Camera - 24MP")
        print("Rear Camera - 64MP + 13MP + 5MP")
        print("--------------------------------------")
    def vi_vo():
        print("VIVO X50 PRO")
        print("Display - 6.56 inch,1080×2376 pixels")
        print("RAM - 8Gb")
        print("Storage - 128GB")
        print("Battery Capacity - 4315mAh")
        print("Front Camera - 32MP")
        print("Rear Camera - 48MP + 13MP + 8MP + 13MP")
        print("--------------------------------------")
    def print_list():
        option=mob_list()
        while option!= 5:
            if option == 1:
                one_8t()
            elif option == 2:
                sam_gal()
            elif option == 3:
                as_us()
            elif option == 4:
                vi_vo() 
            else:
                return "Invalid Input"
            option=mob_list()
    print_list()

def lat_tre():
    print("Select Your choice from 1 to 5")
    def tre_lat():
        print("1. ONE PLUS NORD")
        print("2. REAL ME X3 SUPER ZOOM")
        print("3. ONE PLUS 8 PRO ")
        print("4. POCO M2 PRO")
        print("5. End chat")
        print("------------------------")
        try:
            return(int(input("Select Your choice: ")))
        except:
            print("Invalid Input")
            return 0
    def one_nod():
        print("ONE PLUS NORD")
        print("Display - 6.48 inch,1080×2400 pixels")
        print("RAM - 12Gb")
        print("Storage - 256GB")
        print("Battery Capacity - 4115mAh")
        print("Front Camera - 32MP + 8MP")
        print("Rear Camera - 48MP + 8MP + 5MP + 2MP")
        print("--------------------------------------")
    def real_me():
        print("REAL ME X3 SUPER ZOOM")
        print("Display - 6.60 inch,1080×2400 pixels")
        print("RAM - 12Gb")
        print("Storage - 256GB")
        print("Battery Capacity - 4200mAh")
        print("Front Camera - 32MP + 8MP")
        print("Rear Camera - 64MP + 8MP + 8MP + 2MP")
        print("--------------------------------------")    
    def one_8pro():
        print("ONE PLUS 8 PRO")
        print("Display - 6.78 inch,1440×3168 pixels")
        print("RAM - 8Gb")
        print("Storage - 128GB")
        print("Battery Capacity - 4510mAh")
        print("Front Camera - 16MP")
        print("Rear Camera - 48MP + 8MP + 48MP + 5MP")
        print("--------------------------------------")
    def po_co():
        print("POCO M2 PRO")
        print("Display - 6.67 inch,1080×2400 pixels")
        print("RAM - 6Gb")
        print("Storage - 128GB")
        print("Battery Capacity - 5000mAh")
        print("Front Camera - 16MP")
        print("Rear Camera - 48MP + 8MP + 5MP + 2MP")
        print("--------------------------------------")
    def trend_list():
        option=tre_lat()
        while option!= 5:
            if option == 1:
                one_nod()
            elif option == 2:
                real_me()
            elif option == 3:
                one_8pro()
            elif option == 4:
                po_co() 
            else:
                return "Invalid Input"
            option=tre_lat()
    trend_list()
    
def chatbot():
    print("This bot helps you to know the latest mobile phones and their features")
    name = input("Enter your name : ") 
    welcome(name)
    print("select your choice")
    choice = show_opt()
    while choice != 3:
        if choice == 1:
            list_mob()
        elif choice == 2:
            lat_tre()
        else:
            print("Please enter the number between 1 to 10")
        choice = show_opt()
        
chatbot()
