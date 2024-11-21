def calculate_payback_period(initial_investment, cash_flows):
    cumulative_cash_flow = 0
    for i, cash in enumerate(cash_flows):
        cumulative_cash_flow += cash
        if cumulative_cash_flow >= initial_investment:
            # Se il flusso cumulativo supera l'investimento iniziale
            if cumulative_cash_flow > initial_investment:
                # Calcola la parte dell'anno in cui il payback si realizza
                payback_period = i + (initial_investment - (cumulative_cash_flow - cash)) / cash
            else:
                payback_period = i + 1
            return payback_period
    return None  # Se il payback non viene mai raggiunto


def main():
    # Dati
    initial_investment = 2550000
    cash_flows = [2000000, 1000000, 500000, 500000]

    # Calcolo del Payback Period
    payback = calculate_payback_period(initial_investment, cash_flows)

    print(f"Payback Period: {payback:.2f} anni")


if __name__ == "__main__":
    main()
