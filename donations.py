from collections import defaultdict

class DonationManager:
    def __init__(self):
        self.donations = []
        self.donors = defaultdict(float)

    def register_donation(self, donor_name, donation_type, quantity, donation_date):
        donation = {
            'donor_name': donor_name,
            'donation_type': donation_type,
            'quantity': quantity,
            'donation_date': donation_date
        }
        self.donations.append(donation)
        self.donors[donor_name] += quantity

    def distribute_donation(self, donor_name, donation_type, quantity, distribution_date):
        for donation in self.donations:
            if (donation['donor_name'] == donor_name and
                donation['donation_type'] == donation_type and
                donation['quantity'] >= quantity):
                donation['quantity'] -= quantity
                distribution = {
                    'donor_name': donor_name,
                    'donation_type': donation_type,
                    'quantity': quantity,
                    'distribution_date': distribution_date
                }
                return distribution
        return None

    def generate_inventory_report(self):
        inventory_report = defaultdict(float)
        for donation in self.donations:
            inventory_report[donation['donation_type']] += donation['quantity']
        return dict(inventory_report)

    def generate_donor_report(self):
        return dict(self.donors)

def main():
    manager = DonationManager()

    while True:
        print("\nDonation Inventory Management System")
        print("1. Register Donation")
        print("2. Distribute Donation")
        print("3. Generate Inventory Report")
        print("4. Generate Donor Report")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            donor_name = input("Donor Name: ")
            donation_type = input("Donation Type: ")
            quantity = float(input("Quantity: "))
            donation_date = input("Donation Date (YYYY-MM-DD): ")
            manager.register_donation(donor_name, donation_type, quantity, donation_date)
            print("Donation registered successfully.")

        elif choice == "2":
            donor_name = input("Donor Name: ")
            donation_type = input("Donation Type: ")
            quantity = float(input("Quantity to Distribute: "))
            distribution_date = input("Distribution Date (YYYY-MM-DD): ")
            distribution = manager.distribute_donation(donor_name, donation_type, quantity, distribution_date)
            if distribution:
                print(f"{quantity} {donation_type} distributed from {donor_name} on {distribution_date}.")
            else:
                print("Distribution failed. Check available quantity or donor name.")

        elif choice == "3":
            inventory_report = manager.generate_inventory_report()
            for donation_type, quantity in inventory_report.items():
                print(f"{donation_type}: {quantity}")

        elif choice == "4":
            donor_report = manager.generate_donor_report()
            for donor_name, total_donation in donor_report.items():
                print(f"{donor_name}: {total_donation}")

        elif choice == "5":
            print("Thank you for using the Donation Inventory Management System.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
