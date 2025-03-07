print("Welcome to the Tip Calculator!")

# Get bill amount
while True:
    try:
        bill = float(input("What was the total bill? $"))
        if bill <= 0:
            raise ValueError("Bill amount must be greater than zero.")
        break
    except ValueError as e:
        print(f"Invalid input: {e} Please enter a valid number.")

# Get custom tip percentage
while True:
    try:
        tip_percentage = float(input("What percentage tip would you like to give? (e.g., 10, 12.5, 15): "))
        if tip_percentage < 0:
            raise ValueError("Tip percentage cannot be negative.")
        break
    except ValueError as e:
        print(f"Invalid input: {e} Please enter a valid percentage.")

# Get number of people paying
while True:
    try:
        people = int(input("How many people are paying? "))
        if people <= 0:
            raise ValueError("Number of people must be at least 1.")
        break
    except ValueError as e:
        print(f"Invalid input: {e} Please enter a valid number.")

# If only one person is paying, calculate total immediately
if people==1:
    total_due = bill * (1 + tip_percentage / 100)
    print(f"\nTotal amount to be paid: ${total_due:.2f}")

else:
    # Ask if users want to split evenly
    split_evenly = input("Would you like to split the bill evenly? (yes/no): ").strip().lower()

    if split_evenly=="yes":
        # Even split case
        base_per_person = bill / people
        tip_per_person = (bill * tip_percentage / 100) / people
        total_per_person = base_per_person + tip_per_person

        print("\nFinal breakdown (even split):")
        for i in range(1, people + 1):
            print(
                f"Person {i}: Base = ${base_per_person:.2f}, Tip = ${tip_per_person:.2f}, Total = ${total_per_person:.2f}")

    else:
        # Uneven split case
        while True:
            # Enter each person's contribution before tip
            amounts = []
            print("\nEnter the amount each person is paying (before tip):")
            for i in range(people):
                while True:
                    try:
                        amt = float(input(f"Person {i + 1} pays: $"))
                        if amt < 0:
                            raise ValueError("Amount cannot be negative.")
                        amounts.append(amt)
                        break
                    except ValueError as e:
                        print(f"Invalid input: {e} Please enter a valid amount.")

            # Calculate total contribution
            total_paid = sum(amounts)

            # Check if total entered matches the bill
            if round(total_paid, 2)!=round(bill, 2):
                print("\n⚠️ Warning: The total entered does not match the bill amount!")
                print(f"Total entered: ${total_paid:.2f}, Expected total: ${bill:.2f}")

                retry = input("Would you like to re-enter the amounts? (yes/no): ").strip().lower()
                if retry=="yes":
                    continue  # Restart amount entry
                else:
                    print("Proceeding with entered amounts...")

            break  # Exit loop if user chooses not to re-enter

        # Calculate total tip
        total_tip = (bill * tip_percentage) / 100

        # Distribute tip proportionally based on each person's contribution
        tip_per_person = [(amt / total_paid) * total_tip for amt in amounts]

        # Display results
        print("\nFinal breakdown (uneven split):")
        for i, (amt, tip) in enumerate(zip(amounts, tip_per_person)):
            total_due = amt + tip
            print(f"Person {i + 1}: Base = ${amt:.2f}, Tip = ${tip:.2f}, Total = ${total_due:.2f}")

print("\nThank you for using the Tip Calculator! 😊")
