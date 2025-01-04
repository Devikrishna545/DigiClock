import time

def userChoice(choice):
    if choice == 1:
        generateDigitalClock()
    elif choice == 2:
        try:
            target_Time = int(input("Enter the number of seconds to countdown"))
            if target_Time >0:
                 generateTimer(target_Time)
            else:
                 print("Enter a valid positive number")
        except ValueError:
             print("Invalid input.Enter a valid number.")             
    else:
        print("Invalid Option!")

def generateDigitalClock(): 
     try:
        print("Ctrl+ C to exit Digital clock")    
        while True:
                current_time = time.localtime()
                time_string = time.strftime("%H:%M:%S", current_time)
                print("\r"+ time_string, end='')
                time.sleep(1) 
     except KeyboardInterrupt:
         print("\n Digital clock exiting...")

def generateTimer(target_time):
    try:
        print("Ctrl+ C to exit Timer")  

        while target_time > 0:         
            target_time-=1
            print("\r"+ str(target_time),end='')
            time.sleep(1)

        print("\n Time's Up")        
    except KeyboardInterrupt:
        print("\n Timer exited manually")

if __name__ == '__main__':
    while True:
        try:
            choice = int(input("Select your choices\n 1.Digital Clock\n 2.Timer\n 3.Exit Program"))
            if choice == 3:
                print("Exiting Program !")
                break
            userChoice(choice)
        except ValueError:
            print("Invalid Input! Please enter a valid input.")
    