
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

def calculate_annualized_return(profit, initial_investment, months):
    r = profit / initial_investment
    periods = 12 / months
    annualized_return = (1 + r) ** periods - 1
    return annualized_return * 100  # Convert to percentage


def Futures_Contract_Calculator():
    print("=== British Pound (GBP) Futures Contract Calculator ===\n")

    # 1. User Inputs
    print("Please enter the following details for your GBP futures contract:\n")

    # Question 1
    print("1. [Question #1] Calculating Total Value of the Futures Contract...\n")
    contract_size = float(input(" Contract Original Size (Number of GBP): "))
    selling_price = float(input(" Selling Original Price (USD per GBP): "))
    total_value = calculate_total_value(contract_size, selling_price)
    print(f"[ANSWER #1] Total Value of the Futures Contract: \n${total_value:,.2f}")

    # Question 2
    print("\n2. [Question #2] Calculating Profit in Bear Market Scenario...\n")
    buying_price_bear = float(input("3. Buying Price in Bear Market Scenario [when GPB Falls](USD per GBP): "))
    profit_bear = calculate_profit(selling_price, buying_price_bear, contract_size)
    print(f"\n [ANSWER #2]  Profit if GBP Falls to ${buying_price_bear}, and selling price is ${selling_price} \n profit: ${profit_bear:,.2f}")

    # Question 3
    print("\n3. [Question #] Calculating Annualized Compound Rate of Return...\n")
    initial_margin = float(input(" Initial Margin Deposit (USD): "))
    investment_horizon = float(input(" Investment Horizon (Months): "))
    annuatized_return = calculate_annualized_return(profit_bear, initial_margin, investment_horizon)
    print(f"\n3. [ANSWER #2] \nAnnualized Compound Rate of Return, when \n* profit/loss = {profit_bear} time horizon = {investment_horizon}, and initial_margin = {initial_margin}: \n [Annutized Return] = {annuatized_return:.2f}%")

    # Question 4
    print("\n4. [Question #4] Calculating Loss in Bull Market Scenario...\n")
    buying_price_bull = float(input(" Buying Price in Bull Market Scenario [Market Recovery] (USD per GBP): "))
    loss_bull = calculate_loss(selling_price, buying_price_bull, contract_size)
    print(f"4. Loss if GBP Rises to : ${buying_price_bull}: and is sold at: $ {selling_price} \n [Profit/Loss] = {loss_bull:,.2f}")

    print("\n\n=== Summary ===\n")
    print(f"* Total Value of Contract: ${total_value:,.2f}\n")
    print(f"* Profit in Bear Market: ${profit_bear:,.2f}\n")
    print(f"* Annualized Return: {annuatized_return:.2f}%\n")
    print(f"* Loss in Bull Market: ${loss_bull:,.2f}\n")




def main():
    Futures_Contract_Calculator()

if __name__ == "__main__":
    main()