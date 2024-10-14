
def calculate_total_value(contract_size, selling_price):
    return contract_size * selling_price

def calculate_profit(selling_price, buying_price, contract_size):
    profit_per_gbp = selling_price - buying_price
    total_profit = profit_per_gbp * contract_size
    return total_profit

def calculate_loss(selling_price, buying_price, contract_size):
    loss_per_gbp = selling_price - buying_price
    total_loss = loss_per_gbp * contract_size
    return total_loss

def calculate_annualized_return(profit, margin, months):

    r = profit / margin
    periods = 12 / months
    annualized_return = (((1 + profit) / margin) ** (12 / months)) - 1

    print("r", r)
    print("periods", periods)
    print("annualized_return", annualized_return)
    return annualized_return * 100  # Convert to percentage

#################################################
def Futures_Contract_Calculator():

    def display_menu():
        """
        Display the menu options to the user.
        """
        print("=== British Pound (GBP) Futures Contract Calculator ===\n")

        # 1. User Inputs
        print("Please enter the following details for your GBP futures contract:\n")

        # Question 1
        print(" [Question #1] Calculating Total Value of the Futures Contract...\n")
        contract_size = float(input(" Contract Original Size (Number of GBP): "))
        selling_price = float(input(" Selling Original Price (USD per GBP): "))
        total_value = calculate_total_value(contract_size, selling_price)

        print("\n\n[MENU] \n Select the question you want to solve:")
        print("2. Calculate Profit in Bear Market Scenario")
        print("3. Calculate Annualized Compound Rate of Return")
        print("4. Calculate Loss in Bull Market Scenario")
        print("5. Exit")
        global profit_bear
        profit_bear = 0

        while True:
           # display_menu()
            print(f"\n\n[ANSWER #1] Total Value of the Futures Contract: \n${total_value:,.2f}\n\n")
            choice = input("\nEnter the number corresponding to your choice (2-4): ")

            if choice == '2':
                profit_bear = question_2(selling_price, contract_size)
            elif choice == '3':
                question_3(profit_bear)
            elif choice == '4':
                question_4(selling_price, contract_size)
            elif choice == '5':
                print("\nThank you for using the GBP Futures Contract Calculator. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please select a valid option (1-5).\n")

    # Question 2
    def question_2(selling_price, contract_size):
        print("\n2. [Question #2] Calculating Profit in Bear Market Scenario...\n")
        buying_price_bear = float(input("\nEnter Buying Price in Bear Market Scenario [price GPB Falls too](USD per GBP): "))
        profit_bear = calculate_profit(selling_price, buying_price_bear, contract_size)
        print(f"\n [GIVEN #2] Profit if GBP Falls to ${buying_price_bear}, and selling price is ${selling_price} \n\n [ANSWER #2]profit in a bear market: ${profit_bear:,.2f}")
        return profit_bear
    # Question 3
    def question_3(profit_bear):
        print("\n3. [Question #3] Calculating Annualized Compound Rate of Return, when given [Margin] and [Investment Horizon]...\n")
        initial_margin = float(input("Enter Initial Margin Deposit (USD): "))
        investment_horizon = float(input("\nWhen do you expect to make a profit? "
                                         "\n EnterInvestment Horizon (Months): \n"))
        annuatized_return = calculate_annualized_return(profit_bear, initial_margin, investment_horizon)
        print(f" \n[GIVEN #3] Annualized Compound Rate of Return, when \n* profit/loss = {profit_bear}, time horizon = {investment_horizon}, and initial_margin = {initial_margin}: \n\n [ANSWER #3] [Annutized Return] = {annuatized_return:.2f}%")

    # Question 4
    def question_4(selling_price, contract_size):
        print("\n4. [Question #4] Calculating Loss in Bull Market Scenario...\n")
        buying_price_bull = float(input(" Buying Price in Bull Market Scenario [Market Recovery] (USD per GBP): "))
        loss_bull = calculate_loss(selling_price, buying_price_bull, contract_size)
        print(f" [GIVEN #4] Loss if GBP Rises to : ${buying_price_bull}: and is sold at: $ {selling_price} \n [ANSWER #4].[Profit/Loss] = {loss_bull:,.2f}")


    display_menu()
##################################################



def main():
    print("(GBP) Futures Contract Calculator!")
    Futures_Contract_Calculator()

if __name__ == "__main__":
    main()
