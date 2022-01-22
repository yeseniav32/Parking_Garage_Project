
class Parking_Garage():

    def __init__(self):
        self.tickets_available = [1,2,3,4,5]
        self.parking_space_available = [1,2,3,4,5] 
        self.current_ticket = {} #tickets in circulation are stored here. Fale:haven't paid, True:have paid
        self.ticket = None
        self.space = None

    def take_ticket(self):
        if self.parking_space_available:
            self.ticket = self.tickets_available.pop()      # reduces available ticket count by 1
            self.space = self.parking_space_available.pop() # reduces available space count by 1
            self.current_ticket[self.ticket] = False        # add ticket to the dict, with non-payment status
            print(f"Your ticket number is {self.ticket}")
        else:
            print("Sorry, there are currently no spaces available.  Please try again later.")  

    def pay_for_parking(self):
        self.ticket = input("What is your ticket number?" )  # set current ticket to be paid

        if not self.ticket.isnumeric():
            print("Please input numeric values only.")

        elif  int(self.ticket) not in self.current_ticket:
            print("ERROR -- That ticket is not in circulation. Please enter a valid ticket number")

        elif self.current_ticket[int(self.ticket)]:
            print(f"Ticket number {int(self.ticket)} has alredy been paid. Please proceed to the exit gate.")

        elif int(self.ticket) in self.current_ticket.keys():  
            payment = input("Please pay ticket. The amount due is $10: ")

            if payment.isnumeric():

                if int(payment) == 10:
                    print("Thank you for your payment!") 
                    print("Please be advised you have 15 minutes to leave before your vehicle is impounded by TSA security personnel.")
                    self.current_ticket[int(self.ticket)] = True
                else:
                    print("Incorrect. Please pay the correct amount due.")

            elif not payment.isnumeric():
                print("Incorrect. Please enter a numeric value.")

    def leave_parking_garage(self):
        ticket_paid = input("What was the ticket you paid for? ")

        if not ticket_paid.isnumeric():
            print("Please enter a numeric value only.")

        elif  int(ticket_paid) not in self.current_ticket:
            print("Incorrect, that ticket number is currently not in use. Please try again: ")
        
        elif self.current_ticket[int(ticket_paid)]:
            print("Thank you for parking with us, have a nice day!")
            self.tickets_available.append(self.ticket)       # increment tickets available by 1
            self.parking_space_available.append(self.space)  # increment parking spaces available by 1
            del self.current_ticket[int(ticket_paid)]             # remove ticket (key, value) from ticket dict

        elif self.current_ticket[int(ticket_paid)] == False:
            print("The ticket number entered has not been paid.")
            print("Please verify that you are entering the correct ticket number ")
            print("or return to the payment kiosk if you have not yet paid.")

        # else:
        #     print("Incorrect ticket number, please try again: ")

class Main():

    def __init__(self):
        self.garage = Parking_Garage()  # creates an instance of Parking_Garage to access that class from Main.

    def instructions(self):
        print(f"""
Welcome O'hare International Parking Garage!
There are currently {len(self.garage.parking_space_available)} spaces available. 
Please select from the below options:
    [1] Take ticket
    [2] Pay ticket
    [3] Leave parking garage
""")
    def run(self):
        self.instructions()

        while True:
            option = input("What would you like to do? ")
            if option == "1": 
                self.garage.take_ticket()

            elif option == "2": 
                self.garage.pay_for_parking()
            
            elif option == "3": 
                self.garage.leave_parking_garage()

            elif option.lower() == "break":  #easter egg
                break

            elif option == "311":  #easter egg
                print(f"FOR ADMIN USE ONLY -- TICKETS IN CIRCULATION & PAYMENT STATUS: {self.garage.current_ticket}")

            else:
                print("Sorry, I didn't understand you, please try again: ")
                
garage_A = Main()

garage_A.run()