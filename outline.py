
"""
    garage where cars park,
    take a ticket that decreases ticket count 
    decrease parking availability by 1
    
    Options:
        park
        pay for parking
            once ticket is paid, display count down exit time
            once ticket is paid, display a thank you message
            if a tickets is not paid, display an input prompt for payment
    after someone pays and leaves, 
        increase a parking ticket by 1
        increase parking space by 1 
"""

class Parking_Garage():
    
    def __init__(self):
        self.tickets_list = [1,2,3,4,5]
        self.parking_spaces = [1,2,3,4,5]
        self.current_ticket = {"paid": False, }

    def take_ticket(self):
        #this is where we decrement tickets by 1
        #this is where we decrement parking spaces by 1
        pass

    def pay_for_parking(self):
        payment = int(input("Please pay ticket. Your amount due is 10"))
        if payment == 10:
            print("Thank you for your payment! Please be advised you have 15 minutes to leave before your vehicle is towed.")
            self.current_ticket["paid"] = True
            # Parking_Garage.leave_parking_garage()
        else:
            print("Please pay the correct amount due.")
        

    def leave_parking_garage(self):
        if self.current_ticket["paid"] == True:
            print("Thank you for parking with us, have a nice day!")
        else:
            print("You have not paid! Please go back and pay your parking ticket")
            Parking_Garage.pay_for_parking()




class Main():
    def instructions():
        print("""
Welcome O'hare International Parking Garage!
Please select from the below options:
    Take ticket
    Pay ticket
    Leave parking garage
""")

    def run():
        Main.instructions()

        while True:
            option = input("What would you like to do? ")
            if option == "Take Ticket":
                print(f"You have ticket {} of 5. Please proceed.")
            
            elif option == "Pay ticket":
                Parking_Garage.pay_for_parking()

            elif option == "Leave parking garage":
                Parking_Garage.leave_parking_garage()

            else:
                print("Please evacuate the premises..")
                break

