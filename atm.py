print("Welcome to AWESH Bank !!")
pin = 1256
chances = 3
balance = 50000
transactions = []

while chances != 0:
    user_pin = int(input("Please enter four digit pin :"))
    if user_pin != pin:
        chances -= 1
        print("wrong pin number ")
        print(f"you have {chances} chances left")
    else:
        print("Select Operation to be perform :-")
        user_choice = input("B : balance\nD : deposit\nW : withdraw\nH : transaction History\nT : Transfer\n")

        if user_choice == "B":
            print(f"your total balace is Rs.{balance} ")

        if user_choice == "D":
            deposite_user = int(input("How much do you want to deposit Rs."))
            total_balance = deposite_user + balance
            print(f"you have deposit Rs.{deposite_user}")
            print(f"your total balance is Rs.{total_balance}")
            # Add transaction for deposit
            transactions.append({"type": "deposit", "amount": deposite_user, "balance": total_balance})

        if user_choice == "W":
            widhraw_user = int(input("Enter the amount you want to withdrawn Rs."))
            total_balance = balance - widhraw_user
            print(f"you have widhraw Rs.{widhraw_user}")
            print(f"your total balance is Rs.{total_balance}")
            # Add transaction for withdrawal
            transactions.append({"type": "withdrawal", "amount": widhraw_user, "balance": total_balance})

        # Add similar logic for transfer transactions (explained later)

        if user_choice == "H":
            print("Transaction History:")
            for transaction in transactions:
                print(f"{transaction['type']}: Rs.{transaction['amount']}, Balance: Rs.{transaction['balance']}")

        if user_choice == "T":
            recipient_account = int(input("Enter recipient account number: "))
            transfer_amount = int(input("Enter transfer amount Rs."))

            # Implement transfer logic (assuming simulation environment)
            # (e.g., update balances of mock accounts)
            recipient_balance = recipient_account + transfer_amount  # Update recipient's balance
            balance -= transfer_amount  # Update sender's balance

            # Add transaction for transfer
            transactions.append({"type": "transfer", "amount": transfer_amount, "balance": balance})

    user_exit = input("Would you like to exit ?[Yes/No]\n")
    if user_exit == "Yes":
        print("Thankyou for using AWESH Bank !!!")
        break
    else:
        continue
