import numpy_financial as npf


def main():
    # Definizione dei flussi di cassa: investimento iniziale negativo e flussi di cassa positivi nei tre anni
    cash_flows = [-2550000, 2000000, 1000000, 500000, 500000]

    # Calcolo dell'IRR
    irr = npf.irr(cash_flows)

    # Conversione in percentuale
    irr_percent = irr * 100

    print(f"Il tasso interno di rendimento (IRR) è: {irr_percent:.2f}%")


if __name__ == "__main__":
    main()
