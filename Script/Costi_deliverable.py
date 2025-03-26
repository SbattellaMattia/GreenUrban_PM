import pandas as pd

def allocate_budget(total_budget, weights):
    # Calcola la somma totale dei pesi
    total_weight = sum(weights.values())
    
    # Ripartisce il budget in base ai pesi
    budget_allocation = {key: (value / total_weight) * total_budget for key, value in weights.items()}
    
    return budget_allocation

# Dizionario con le attività e i pesi iniziali

# Icosti dei deliverable rimanenti sono stati calcolati dopo aver calcolato i costi per ogni attività
# e successivamente addizionando le attività inerenti al deliverable
weights = {
    "1.1 Project Charter": 1, "1.2 Registro degli stakeholders": 1, "1.3 Project Management Plan": 1,
    "1.4 Registro delle modifiche": 2, "1.5 Registro delle questioni": 2, "1.6 Registro dei rischi": 3,
    "1.7 Registro delle lesson learned": 3, "1.8 Documento di chiusura": 3,
}

# Budget totale rimanente per le prime
total_budget = 766446.12

# Allocazione del budget
budget_allocation = allocate_budget(total_budget, weights)

# Visualizzazione dei dati
df = pd.DataFrame(list(budget_allocation.items()), columns=["Attività", "Budget Allocato (€)"])
print(df.to_string(index=False))
