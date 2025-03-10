import os
import re
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from pypdf.annotations import Link
from pypdf.generic import Fit
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def get_pdf_files():
    """Ottiene tutti i file PDF nella cartella corrente, ordinati numericamente"""
    def extract_number(filename):
        match = re.match(r"(\d+)-", filename)  # Prende il numero iniziale prima di '-'
        return int(match.group(1)) if match else float('inf')  # Se non c'è numero, va in fondo

    pdf_files = [f for f in os.listdir() if f.endswith(".pdf") and f not in ["index.pdf", "index_with_links.pdf", "0- Frontespizio.pdf", "output.pdf", ]]
    return sorted(pdf_files, key=extract_number)  # Ordina in base al numero

def clean_filename(filename):
    """Rimuove il numero iniziale (es. '1- ') dal nome per l'indice"""
    #return re.sub(r"^\d+-\s*", "", filename)  # Rimuove il numero iniziale e lo spazio

    return filename[:-4].replace("_", "'")

def create_index_pdf(pdf_list, output_index, bookmark):
    """Crea un PDF con un indice e registra le posizioni per i link"""
    c = canvas.Canvas(output_index, pagesize=A4)
    c.setFont("Times-Roman", 16)
    c.drawString(100, 800, "Indice")

    y_position = 780
    links = []

    for i, pdf in enumerate(pdf_list):
        c.setFont("Times-Roman", 12)
        text = clean_filename(pdf)
        c.drawString(100, y_position, text)

        # Usa il dizionario bookmark per ottenere la pagina corretta
        target_page = list(bookmark.values())  # Default a pagina 2 se non trova la chiave
        links.append((100, y_position - 3, target_page[i]+1))

        y_position -= 20  # Spaziatura tra le righe

    c.save()
    return links

def add_links_to_index(index_pdf, links, output_index_with_links):
    """Aggiunge i link cliccabili all'indice nel PDF"""
    reader = PdfReader(index_pdf)
    writer = PdfWriter()
    writer.add_page(reader.pages[0])

    for x, y, target_page in links:
        annotation = Link(
            rect=(x, y, x + 200, y + 10),  # Area cliccabile
            target_page_index=target_page - 1,  # La pagina parte da 0
            fit=Fit(fit_type="/FitH", fit_args=(800,))  # Posiziona l'utente in alto nella pagina target
        )
        writer.add_annotation(page_number=0, annotation=annotation)  # Aggiunge link alla prima pagina (indice)

    with open(output_index_with_links, "wb") as output_file:
        writer.write(output_file)

def merge_pdfs_with_index(pdf_list, output_pdf):
    """Unisce i PDF e inserisce un indice con link interni"""
    if not pdf_list:
        print("❌ Nessun file PDF trovato nella cartella corrente.")
        return

    merger = PdfMerger()

    # Creazione PDF dell'indice
    index_pdf = "index.pdf"
    frontespizio = "0- Frontespizio.pdf"
    bookmarks = {}
    page_number = 2  # Il frontespizio è la pagina 1, l'indice è la pagina 2

    for pdf in pdf_list:
        reader = PdfReader(pdf)
        num_pages = len(reader.pages)
        bookmarks[pdf] = page_number
        page_number += num_pages

    links = create_index_pdf(pdf_list, index_pdf, bookmarks)

    # Aggiunge l'indice con i link
    index_with_links = "index_with_links.pdf"
    add_links_to_index(index_pdf, links, index_with_links)

    # Aggiunge il frontespizio e l'indice
    merger.append(frontespizio)
    merger.append(index_with_links)

    # Aggiunge i PDF con segnalibri
    merger.add_outline_item("Indice", 1)

    for pdf, page in bookmarks.items():
        merger.append(pdf)
        merger.add_outline_item(pdf[:-4], page)

    # Salva il PDF finale
    merger.write(output_pdf)
    merger.close()

    print(f"✅ PDF unito creato: {output_pdf}")

# ----- USO -----
pdf_files = get_pdf_files()
merge_pdfs_with_index(pdf_files, "GreenUrban.pdf")
