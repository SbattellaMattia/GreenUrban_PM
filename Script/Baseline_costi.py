import locale

# Imposta la localizzazione italiana
locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')


def ripartisci_costi(costo_totale, attivita_per_settimana, pesi_attivita):
    """
    Ripartisce i costi proporzionalmente al numero e al peso delle attività settimanali.

    Args:
        costo_totale: L'importo totale che deve essere ripartito tra tutte le settimane.
        attivita_per_settimana: Una lista di liste, dove ogni lista interna rappresenta le attività pianificate per una determinata settimana.
        pesi_attivita: Un dizionario che associa a ciascuna attività un peso, indicando quanto è importante o impegnativa. Se un'attività non è presente nel dizionario, la funzione assume un peso di default pari a 1.

    Funzionamento:

        Calcolo dei pesi settimanali:
            La funzione crea una lista pesi_settimanali in cui ogni elemento rappresenta la somma dei pesi delle attività di una settimana.
            Se una settimana ha più attività, la somma dei pesi per quella settimana rifletterà l'importanza cumulativa delle attività.

        Calcolo del totale dei pesi:
            Viene calcolata la somma di tutti i pesi settimanali per ottenere totale_pesi. Questo valore rappresenta la somma totale dei pesi di tutte le attività in tutte le settimane.

        Gestione della divisione per zero:
            Se totale_pesi è zero (ad esempio, se non ci sono attività), la funzione restituisce una lista di zeri della stessa lunghezza di attivita_per_settimana, evitando errori di divisione per zero.

        Ripartizione dei costi:

        La funzione calcola il costo per ciascuna settimana in modo proporzionale al peso delle attività in quella settimana rispetto al totale_pesi.
        Ogni costo settimanale viene calcolato come:
        Costo_settimanale=costo_totale×peso_settimana/totale_pesi

        Questo significa che le settimane con attività più "pesanti" (cioè, più impegnative o importanti) riceveranno una quota maggiore del costo totale.

    Returns:
        list: Una lista di costi settimanali distribuiti in base ai pesi delle attività.
    """



    # Calcola il peso totale delle attività per ciascuna settimana
    pesi_settimanali = [sum(pesi_attivita.get(attivita, 1) for attivita in settimana) for settimana in
                        attivita_per_settimana]

    # Calcola il totale dei pesi su tutte le settimane
    totale_pesi = sum(pesi_settimanali)

    # Evita la divisione per zero nel caso non ci siano attività
    if totale_pesi == 0:
        return [0] * len(attivita_per_settimana)

    # Calcola il costo per ciascuna settimana proporzionalmente ai pesi delle attività
    costi_settimanali = [
        (costo_totale * peso_settimana / totale_pesi)
        for peso_settimana in pesi_settimanali
    ]

    return costi_settimanali


def __main__():
    # Esempio di input
    costo_totale= 2550000
    attivita_per_settimana = [
        ['1.1'],  # Settimana 1
        ['1.1', '1.2'],  # Settimana 2
        ['1.2'],  # Settimana 3
        ['1.2'],  # Settimana 4
        ['1.2'],  # Settimana 5
        ['1.2', '2.1'],  # Settimana 6
        ['1.2', '2.1'],  # Settimana 7
        ['1.2', '2.2'],  # Settimana 8
        ['1.2', '2.2'],  # Settimana 9
        ['1.2', '2.2'],  # Settimana 10
        ['2.2'],  # Settimana 11
        ['1.3', '1.4', '2.2', '3.1'], # Settimana 12
        ['1.3', '1.4', '2.2', '3.1'],  # Sett. 13
        ['1.3', '1.4', '2.2', '3.2', '3.3', '3.7'],  # Sett. 14
        ['1.3', '1.4', '2.2', '3.2', '3.3', '3.7'],  # Sett. 15
        ['1.3', '1.4', '3.2', '3.8'],  # Sett. 16
        ['1.3', '1.4', '3.2'],  # Sett. 17
        ['1.3', '1.4', '3.2'],  # Sett. 18
        ['1.3', '1.4', '3.2'],  # Sett. 19
        ['1.3', '1.4', '3.2'],  # Sett. 20
        ['1.3', '1.4', '3.2'],  # Sett. 21
        ['1.3', '1.4', '2.3', '2.4', '2.5', '3.2'],  # Sett. 22
        ['1.3', '1.4', '2.3', '2.4', '2.5', '3.4', '3.5'],  # Sett. 23
        ['1.3', '1.4', '2.3', '2.4', '2.5', '3.4', '3.5', '5.1'],  # Sett. 24
        ['1.3', '1.4', '2.3', '2.4', '2.5', '3.4', '4.1', '5.1'],  # Sett. 25
        ['1.3', '1.4', '2.3', '2.4', '2.5', '3.4', '5.1', '5.3'],  # Sett. 26
        ['1.3', '1.4', '2.3', '2.4', '2.5', '3.4', '4.2', '4.3', '5.2', '5.3'],  # Sett. 27
        ['1.3', '1.4', '2.3', '2.4', '2.5', '3.6', '4.2', '4.3', '5.2'],  # Sett. 28
        ['1.3', '1.4', '2.3', '2.4', '2.5', '3.6', '4.3', '5.4'],  # Sett. 29
        ['1.3', '1.4', '2.3', '2.4', '2.5', '3.6', '4.4', '5.4'],  # Sett. 30
        ['1.3', '1.4', '2.6', '3.6', '4.4'],  # Sett. 31
        ['1.3', '1.4', '2.6', '3.6', '4.4', '5.5', '5.6'],  # Sett. 32
        ['1.3', '1.4', '3.6', '4.4', '5.5', '5.6'],  # Sett. 33
        ['1.3', '1.4', '3.8', '4.5', '5.6'],  # Sett. 34
        ['1.3', '1.4', '3.8', '4.5', '5.6'],  # Sett. 35
        ['1.3', '1.4', '3.8', '4.5', '5.7'],  # Sett. 36
        ['1.3', '1.4', '3.9', '5.7', '6.1', '6.2', '6.3'],  # Sett. 37
        ['1.3', '1.4', '3.9', '4.6', '5.7', '6.1', '6.2', '6.3'],  # Sett. 38
        ['1.3', '1.4', '3.9', '4.6', '6.1', '6.2', '6.3'],  # Sett. 39
        ['1.3', '1.4', '3.9', '4.6', '5.8', '6.1', '6.2', '6.3'],  # Sett. 40
        ['1.3', '1.4', '4.6', '5.8', '6.2', '6.3'],  # Sett. 41
        ['1.3', '1.4', '3.10', '4.7', '5.8', '6.2'],  # Sett. 42
        ['1.3', '1.4', '3.10', '4.7', '6.4', '6.5'],  # Sett. 43
        ['1.3', '1.4', '3.10', '4.7', '6.4', '6.5'],  # Sett. 44
        ['1.3', '1.4', '4.7', '6.4', '6.5'],  # Sett. 45
        ['1.3', '1.4', '6.4', '6.5'],  # Sett. 46
        ['1.3', '1.4', '6.4', '6.6'],  # Sett. 47
        ['1.3', '1.4', '6.4', '6.6'],  # Sett. 48
        ['1.3', '1.4', '6.4', '6.6'],  # Sett. 49
        ['1.3', '1.4', '6.4', '6.6'],  # Sett. 50
        ['1.3', '1.4', '6.4', '6.6'],  # Sett. 51
        ['1.3', '1.4', '6.4'],  # Sett. 52
        ['1.3', '1.4', '6.7'],  # Sett. 53
        ['1.3', '1.4', '6.7'],  # Sett. 54
        ['1.3', '1.4', '6.7'],  # Sett. 55
        ['1.3', '7.1'],  # Sett. 56
        ['1.3', '7.1'],  # Sett. 57
        ['1.3', '7.1'],  # Sett. 58
        ['1.3', '7.1'],  # Sett. 59
        ['1.3'],         # Sett. 60
        ['1.3', '7.2'],  # Sett. 61
        ['1.3', '7.2'],  # Sett. 62
        ['1.3', '7.2'],  # Sett. 63
        ['1.3', '7.2'],  # Sett. 64
        ['1.3', '7.2'],  # Sett. 65
        ['1.3', '7.3'],  # Sett. 66
        ['1.3', '7.3'],  # Sett. 67
        ['1.3', '7.3'],  # Sett. 68
        ['1.3', '7.3'],  # Sett. 69
        ['1.3', '7.3'],  # Sett. 70
        ['1.3', '7.4'],  # Sett. 71
        ['1.3', '7.5'],  # Sett. 72
        ['1.3', '7.5'],  # Sett. 73
        ['1.3', '7.5'],  # Sett. 74
        ['1.3', '7.5'],  # Sett. 75
        ['1.3', '7.5'],  # Sett. 76
        ['1.3'],         # Sett. 77
        ['1.3', '7.6'],  # Sett. 78
        ['1.3', '7.6'],  # Sett. 79
        ['1.3', '7.6'],  # Sett. 80
        ['1.3', '7.6'],  # Sett. 81
        ['1.3', '7.6'],  # Sett. 82
        ['1.3', '7.6'],  # Sett. 83
        ['1.3', '7.6'],  # Sett. 84
        ['1.3', '7.6'],  # Sett. 85
        ['1.3', '7.6'],  # Sett. 86
        ['1.3', '7.6'],  # Sett. 87
        ['1.5', '6.8'],  # Sett. 88
        ['1.5', '6.8'],  # Sett. 89
        ['1.5', '6.8'],  # Sett. 90
        ['1.5', '6.8'],  # Sett. 91
        ['1.5', '6.8'],  # Sett. 92
    ]

    # Pesi delle attività (Scala da 1-2)
    pesi_attivita = {
        '1.1': 1.0,
        '1.2': 1.0,
        '1.3': 1.0,
        '1.4': 1.0,
        '1.5': 1.0,
        '2.1': 1.5,
        '2.2': 1.5,
        '2.3': 1.5,
        '2.4': 1.5,
        '2.5': 1.5,
        '2.6': 1.5,
        '3.1': 1.5,
        '3.2': 2.0,
        '3.3': 2.0,
        '3.4': 2.0,
        '3.5': 2.0,
        '3.6': 2.0,
        '3.7': 2.0,
        '3.8': 2.0,
        '3.9': 1.0,
        '3.10': 1.5,
        '4.1': 1.5,
        '4.2': 2.0,
        '4.3': 2.0,
        '4.4': 2.0,
        '4.5': 2.0,
        '4.6': 1.0,
        '4.7': 1.5,
        '5.1': 1.5,
        '5.2': 2.0,
        '5.3': 2.0,
        '5.4': 2.0,
        '5.5': 2.0,
        '5.6': 2.0,
        '5.7': 1.0,
        '5.8': 1.5,
        '6.1': 1.5,
        '6.2': 1.5,
        '6.3': 1.5,
        '6.4': 1.5,
        '6.5': 1.5,
        '6.6': 1.5,
        '6.7': 1.5,
        '6.8': 1.5,
        '7.1': 1.0,
        '7.2': 1.5,
        '7.3': 1.0,
        '7.4': 1.5,
        '7.5': 1.0,
        '7.6': 1.0,
    }

    # Calcolo dei costi settimanali
    costi = ripartisci_costi(costo_totale, attivita_per_settimana, pesi_attivita)

    totale_trimestre=0
    totale_progetto=0
    cont_trimestri=0
    # Stampa dei costi ripartiti
    for i, costo in enumerate(costi):
        totale_trimestre+=costo
        totale_progetto+=costo
        print(f"Settimana {i + 1}: {locale.format_string('%.2f', costo, grouping=True)} €\t\t\t\t\t Costo cumulativo: {locale.format_string('%.2f', totale_progetto, grouping=True)} €")
        if ((i+1)%12==0):
            cont_trimestri+=1
            print(f"Totale trimrstre {cont_trimestri}: "+ '\033[1m' + locale.format_string('%.2f', totale_trimestre, grouping=True) + '\033[0m' + " €\t\t\t Costo cumulativo: "+ '\033[1m' + locale.format_string('%.2f', totale_progetto, grouping=True) + " €" + '\033[0m')
            totale_trimestre=0

    print(f"Totale trimrstre 8: " + '\033[1m' + locale.format_string('%.2f', totale_trimestre, grouping=True) + " €" '\033[0m' )
    print('\033[1m' + f"Totale progetto: {locale.format_string('%.2f', totale_progetto, grouping=True)} €"+ '\033[0m')
if __name__ == "__main__":
    __main__()
