# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).

# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket  to "closed".
# Display all tickets.
#   (Bonus) filter by status

# Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:

ticket_count = 2
service_tickets = {
    1 : {"Customer": "Alice", "Issue": "Login problem", "Open": True},
    2 : {"Customer": "Bob", "Issue": "Payment issue", "Open": False}
}

def main():
    while True:
        print('''
        Welcome to the service ticket system

        1. Open a new ticket
        2. Update status of a ticket
        3. Display all tickets
        4. Filter by status
        5. Close
        ''')
        ans = int(input("How can we help you today?: "))

        if (ans == 1):
            new_ticket(ticket_count)
        elif (ans == 2):
            ans = int(input("Which ticket number would you like to update? : "))
            update_id(ans)
        elif (ans == 3):
            view_tickets()
        elif (ans == 4):
            filter_tickets()
        elif (ans == 5):
            print("Thanks for using the service ticket system. Have a great day!")
            break
            


#---Open new ticket
def new_ticket (ticket_count):
    ticket_count +=1
    service_tickets.update( {
        ticket_count : { 
                "Customer" : input("Enter customer name: "),
                "Issue" : input("What issues are you having?: "),
                "Open": True
        }
        
    }) 

    print(service_tickets)

#--- update existing ticket
def update_id (ticket_id):
    for ticket in service_tickets.keys():
        if (int(ticket_id) == ticket):
            if (service_tickets[ticket_id]["Open"]) == True:
                ans = input("Would you like to close this ticket? y/n : ")
                if ans == "y":
                    service_tickets[ticket_id].update({"Open":False})
                    print(service_tickets)
                else:
                    print("No changes have been made")
            elif (service_tickets[ticket_id]["Open"]) == False:
                ans = input("Would you like to open this ticket? y/n : ")
                if ans == "y":
                    service_tickets[ticket_id].update({"Open":True})
                    print(service_tickets)
                else:
                    print("No changes have been made")

#--- display all tickets
def view_tickets():
    for ticket in service_tickets.keys():
        print(f''' 
        {ticket} - {service_tickets[ticket]}

        ''')
#  (Bonus) filter by status
def filter_tickets():
    ans = input('''
    Would you like to see open or closed tickets?
    o - open
    c - closed
    ''')
    if (ans == "o"):
        for ticket in service_tickets.keys():
            if (service_tickets[ticket]["Open"]) == True:
                print(service_tickets[ticket])
    elif (ans == 'c'):
        for ticket in service_tickets.keys():
            if (service_tickets[ticket]["Open"]) == False:
                print(service_tickets[ticket])
                

main()