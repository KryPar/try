

def move_foward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}") 

def start_engien():
    print("starting engine") 
    
def stop_engine():
    print("stopping engine") 


destination = input("Where do you want to go? ")

start_engien ()
move_foward ()

if destination == "school":
    turn("right")
    print("we arrived at school")

elif destination == "groccery store" or destination == "dentist":
    turn ("left")
    move_foward()
    if destination == "groccery store":
        turn("right")
        print("we arrive at groccery store")
    else:
        turn("left")
        print("we arrived at dentist")

elif destination == "restaurant":
    move_foward()
    print ("we arrived at restaurant")

else: 
    print("invalid destinaton")



    

