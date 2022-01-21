
class Parking_Garage():
    
    def __init__(self):
        self.tickets_available = [1,2,3,4,5]
        self.parking_space_available = [1,2,3,4,5] 
        self.current_ticket = {} #ticket payment status  #1: False, 2: False, 3:False, 4:False, 5:False
        self.ticket = None
        self.space = None

    def take_ticket(self):
        if self.parking_space_available:
            self.ticket = self.tickets_available.pop()      # reduces available ticket count by 1
            self.space = self.parking_space_available.pop() # reduces available space count by 1
            self.current_ticket[self.ticket] = False  #add ticket to the dict, with non-payment status
            print(f"Your ticket number is {self.ticket}")

        else:
            print("Sorry no spaces are currently available.")

    def pay_for_parking(self):

        #set current ticket to be paid
        self.ticket = int(input("What is your ticket number?" ))
        print(f"Current tickets in use: {list(self.current_ticket.keys())}")
        print(self.current_ticket[self.ticket])

        if not self.current_ticket[self.ticket]:  #this might be what we
            payment = int(input("Please pay ticket. Your amount due is $10: "))

            if payment == 10:
                print("Thank you for your payment! Please be advised you have 15 minutes to leave before your vehicle is towed.")
                self.current_ticket[self.ticket] = True
            else:
                print("Please pay the correct amount due.")
        else:
            print("Check yourself! That ticket is not in circulation.")


    def leave_parking_garage(self):
        ticket_paid = int(input("What was the ticket you paid for?"))
            
        if self.current_ticket[ticket_paid]:
            print("Thank you for parking with us, have a nice day!")
            self.tickets_available.append(self.ticket)      #increment tickets available by 1
            self.parking_space_available.append(self.space) #increment parking spaces available by 
            del self.current_ticket[self.ticket]  #remove ticket (key, value) from ticket dict

        elif self.current_ticket[ticket_paid] == False:
            print("You have not paid! Please go back and pay your parking ticket")
            self.pay_for_parking()

        else:
            print("incorrect ticket number, please try again: ")

class Main():

    def __init__(self):
        self.garage = Parking_Garage()

    def instructions(self):
        print(f"""
Welcome O'hare International Parking Garage!
There are currently X spaces available. 
Please select from the below options:
    [1] Take ticket
    [2] Pay ticket
    [3] Leave parking garage
""")
    def run(self):
        self.instructions()

        while True:
            option = input("What would you like to do? ")
            if option == "1": #take ticket
                self.garage.take_ticket()
                # print(self.garage.tickets_available)
                # print(f"You have a ticket.")

            elif option == "2": #pay ticket
                self.garage.pay_for_parking()
            
            elif option == "3": #leave parking garage1
                self.garage.leave_parking_garage()

            elif option.lower() == "break":  #easter egg
                break

            else:
                print("Sorry, didn't understand you, please try again: ")
                
garage_A = Main()

garage_A.run()