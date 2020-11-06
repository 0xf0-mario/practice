"""
parkingCharges.py: This program will process parking charges ($2.00 min fee to park for up to 3 hrs an additional .50$/hr will be added after 3hrs. the max charge will be 24hrs at $10)

Mario Medel

7/27/2020
"""
# Introduction

print("                      Parking Charges")
print("==================================================================================")
print("- $2.00 minimum fee to park for up to 3hrs -")
print("- An additional $0.50/hr will be charged after 3 hours -")
print("- $10 dollar max charge for a given 24 hour period. 19 hours and above are 10$ -")
print("==================================================================================")



def main():
    customerNum = 0
    total_charge = 0
    # User Input to indicate if they are going to park
    inputPark = input("\nEnter any button to park (enter N to end the program): ")

    while inputPark.lower() != "n":
        # maintaining the amount of customers
        customerNum += 1
        # asking the user to input amount of hours parked
        hours_parked = float(input("If you are finished parking, Input Hours parked: "))
        # Input validating
        while hours_parked < .01 or hours_parked > 24.01:
            hours_parked = float(input("\nIncorrect number of hours(24hr max period), Input Hours parked: "))

        # Calling the calculate_charge() function that takes in the hours_parked parameter from user input
        charge = calculate_charge(hours_parked)
        # maintain total charge
        total_charge += charge
        # maintaining and outputting the customer number and the total charge
        print(f"~Customer #: {customerNum}          ~Total Charge: ${charge}")
        inputPark = input("\nEnter Any Button To Park (N to end the program): ")
        if inputPark.lower() == "n":
            break
    return customerNum, total_charge


def calculate_charge(hours_parked):
    if hours_parked <= 3:
        return 2
    elif hours_parked >= 4 and hours_parked <= 18.99:
        hours_parked -= 3
        return 2 + (hours_parked * .50)
    elif hours_parked >= 19:
        return 10 + 0


day = main()
(allCustomers, dayTotal) = day

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f'~TOTAL CUSTOMERS: {allCustomers}')
print(f'~DAY TOTAL: ${dayTotal}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

input("\npress enter to close window: ")
