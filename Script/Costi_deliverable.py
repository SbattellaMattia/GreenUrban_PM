import pandas as pd

def allocate_budget(total_budget, weights):
    # Calcola la somma totale dei pesi
    total_weight = sum(weights.values())
    
    # Ripartisce il budget in base ai pesi
    budget_allocation = {key: (value / total_weight) * total_budget for key, value in weights.items()}
    
    return budget_allocation

# Dizionario con le attività e i pesi iniziali (da modificare a piacere)
weights = {
    "1.1 Project Charter": 1, "1.2 Registro degli stakeholders": 1, "1.3 Project Management Plan": 1,
    "1.4 Registro delle modifiche": 1, "1.5 Registro delle questioni": 1, "1.6 Registro dei rischi": 1,
    "1.7 Registro delle lesson learned": 1, "1.8 Documento di chiusura": 1, "2.1 Progetto architettonico": 3,
    "2.2 Progetto dei pannelli": 3, "2.3 Progetto del sistema di irrigazione": 3, "2.4 Progetto del sistema dei sensori": 3,
    "2.5 Relazione ambientale": 1, "3.1 Sostegni per i pannelli": 4, "3.2 Pannelli modulari": 4,
    "3.3 Documentazione della struttura": 1, "3.4 Piano di manutenzione della struttura": 1, "4.1 Sistema di irrigazione automatica": 1,
    "4.2 Sistema di sensori di umidità": 1, "4.3 Documentazione del sistema di irrigazione": 1, "4.4 Piano di manutenzione del sistema di irrigazione": 1,
    "5.1 Sistema di sensori": 1, "5.2 Centralina raccolta dati": 1, "5.3 Documentazione impianto di sensori": 1,
    "5.4 Piano di manutenzione sistema di sensori": 1, "6.1 Documentazione verifica funzionamento sensori": 1,
    "6.2 Documentazione verifica funzionamento sistema di irrigazione": 1, "6.3 Documentazione verifica funzionamento sistema di sensori": 1,
    "6.4 Analisi conclusiva e redazione report finale": 1, "7.1 Piano di comunicazione": 1,
    "7.2 Materiale informativo e promozionale": 1, "7.3 Documento di raccolta feedback della comunità": 1,
    "7.4 Aggiornamenti periodici": 1
}

# Budget totale
total_budget = 2550000

# Allocazione del budget
budget_allocation = allocate_budget(total_budget, weights)

# Creazione di un DataFrame per visualizzare i dati
df = pd.DataFrame(list(budget_allocation.items()), columns=["Attività", "Budget Allocato (€)"])
print(df.to_string(index=False))
