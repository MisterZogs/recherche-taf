"""
Utilitaire pour ajouter des offres dans offres_emploi.xlsx.

- Les offres CSM (Customer Success) vont dans l'onglet "Offres CSM".
- Les offres IA (formateur IA, IA x SIRH, IA x RH) vont dans "Offres IA".
- Les offres SIRH/SAP vont dans l'onglet "Offres SIRH".
- Avant chaque ajout, les lignes marquées "x" dans la colonne Fait
  sont déplacées vers l'onglet "Fait".
"""

import openpyxl
from openpyxl.styles import PatternFill
from copy import copy

FICHIER = "offres_emploi.xlsx"

COLS = [
    'Priorité', 'Statut', 'Fait', 'Poste', 'Entreprise', 'Source', 'Contrat',
    'Localisation', 'Remote', 'Salaire / TJM', 'Durée mission',
    'Fit / Notes', 'Lien', 'CV à envoyer', 'Prétention'
]

CSM_KEYWORDS = ['Customer Success', 'Client Success', 'CSM']
IA_KEYWORDS  = ['Formateur IA', 'Formation IA', 'IA générative', 'IA x SIRH', 'IA x RH',
                 'Intelligence Artificielle', 'AI Trainer', 'GenAI', 'LLM', 'Prompt',
                 'Plateforme IA', 'AI Platform', 'Projet IA', 'PMO IA']

COLORS = {
    '⭐⭐⭐⭐⭐': '00FF0000',
    '⭐⭐⭐⭐':   '00FF8C00',
    '⭐⭐⭐':     '00FFD700',
    '⭐⭐':       '0070AD47',
    '⭐':         '00969696',
}

PRIORITY_ORDER = {
    '⭐⭐⭐⭐⭐': 0,
    '⭐⭐⭐⭐':   1,
    '⭐⭐⭐':     2,
    '⭐⭐':       3,
    '⭐':         4,
}

STATUS_ORDER = {
    'Postulé': 0,
    'Refusé':  1,
    'Expiré':  2,
}


def _is_csm(poste: str) -> bool:
    return any(kw in poste for kw in CSM_KEYWORDS)


def _is_ia(poste: str) -> bool:
    return any(kw.lower() in poste.lower() for kw in IA_KEYWORDS)


def _capture_cell(cell):
    return {
        'value':         cell.value,
        'data_type':     cell.data_type,
        'font':          copy(cell.font)       if cell.has_style else None,
        'border':        copy(cell.border)     if cell.has_style else None,
        'fill':          copy(cell.fill)       if cell.has_style else None,
        'number_format': cell.number_format    if cell.has_style else None,
        'protection':    copy(cell.protection) if cell.has_style else None,
        'alignment':     copy(cell.alignment)  if cell.has_style else None,
        'hyperlink':     cell.hyperlink,
    }


def _restore_cell(cell, data):
    cell.value = data['value']
    if data['font']:          cell.font          = data['font']
    if data['border']:        cell.border        = data['border']
    if data['fill']:          cell.fill          = data['fill']
    if data['number_format']: cell.number_format = data['number_format']
    if data['protection']:    cell.protection    = data['protection']
    if data['alignment']:     cell.alignment     = data['alignment']
    if data['hyperlink']:     cell.hyperlink     = data['hyperlink']


def _clear_cell(cell):
    cell.value = None


def _col_index(ws, name):
    for i, cell in enumerate(ws[1]):
        if cell.value == name:
            return i
    raise ValueError(f"Colonne '{name}' introuvable dans {ws.title}")


def _archiver_faits(ws_src, ws_fait, fait_idx, verbose):
    """Déplace les lignes 'x' de ws_src vers ws_fait. Retourne les lignes conservées."""
    kept = []
    archived = []
    for row in ws_src.iter_rows(min_row=2, max_row=ws_src.max_row):
        row_data = [_capture_cell(c) for c in row]
        # Ignorer les lignes entièrement vides
        if all(d['value'] is None for d in row_data):
            continue
        if str(row_data[fait_idx]['value'] or '').strip().lower() == 'x':
            archived.append(row_data)
        else:
            kept.append(row_data)

    if archived:
        if ws_fait.max_row == 1 and ws_fait.cell(1, 1).value is None:
            for j, cell in enumerate(ws_src[1]):
                ws_fait.cell(row=1, column=j + 1).value = cell.value
        next_row = ws_fait.max_row + 1
        for row_data in archived:
            for j, cell_data in enumerate(row_data):
                _restore_cell(ws_fait.cell(row=next_row, column=j + 1), cell_data)
            next_row += 1
        if verbose:
            print(f"  Archivé ({ws_src.title}) → Fait : {len(archived)} ligne(s)")

    return kept


def _ecrire_onglet(ws, rows, verbose):
    """Trie et réécrit les lignes dans ws, efface le surplus."""
    prio_idx   = _col_index(ws, 'Priorité')
    status_idx = _col_index(ws, 'Statut')

    def sort_key(r):
        status   = r[status_idx]['value'] or ''
        priority = r[prio_idx]['value']   or ''
        return (STATUS_ORDER.get(status, 3), PRIORITY_ORDER.get(priority, 99))

    rows.sort(key=sort_key)

    old_max = ws.max_row
    for i, row_data in enumerate(rows):
        for j, cell_data in enumerate(row_data):
            _restore_cell(ws.cell(row=i + 2, column=j + 1), cell_data)

    for r in range(len(rows) + 2, old_max + 1):
        for cell in ws[r]:
            _clear_cell(cell)

    if verbose:
        print(f"  {ws.title} : {len(rows)} offres")


def _nouvelle_ligne(offre: dict) -> list:
    row_data = []
    for col in COLS:
        val = offre.get(col)
        cell_data = {
            'value': val, 'data_type': None, 'font': None,
            'border': None, 'fill': None, 'number_format': None,
            'protection': None, 'alignment': None, 'hyperlink': None,
        }
        if col == 'Priorité' and val in COLORS:
            cell_data['fill'] = PatternFill(fill_type='solid', fgColor=COLORS[val])
        row_data.append(cell_data)
    return row_data


def ajouter_offres(offres: list[dict], verbose=True):
    """
    1. Archive les lignes 'x' (colonne Fait) de chaque onglet vers Fait.
    2. Route les nouvelles offres : CSM → Offres CSM, IA → Offres IA, autres → Offres SIRH.
    3. Trie chaque onglet.
    """
    wb = openpyxl.load_workbook(FICHIER)
    ws_sirh = wb['Offres SIRH']
    ws_csm  = wb['Offres CSM']
    ws_ia   = wb['Offres IA']
    ws_fait = wb['Fait']

    fait_idx = _col_index(ws_sirh, 'Fait')

    if verbose:
        print("── Archivage ──")

    rows_sirh = _archiver_faits(ws_sirh, ws_fait, fait_idx, verbose)
    rows_csm  = _archiver_faits(ws_csm,  ws_fait, fait_idx, verbose)
    rows_ia   = _archiver_faits(ws_ia,   ws_fait, fait_idx, verbose)

    if verbose:
        print("── Ajout ──")

    for offre in offres:
        poste = offre.get('Poste', '')
        ligne = _nouvelle_ligne(offre)
        if _is_ia(poste):
            rows_ia.append(ligne)
            target = 'Offres IA'
        elif _is_csm(poste):
            rows_csm.append(ligne)
            target = 'Offres CSM'
        else:
            rows_sirh.append(ligne)
            target = 'Offres SIRH'
        if verbose:
            print(f"+ [{target}] {offre.get('Priorité')} | {poste} | {offre.get('Entreprise')}")

    if verbose:
        print("── Tri & sauvegarde ──")

    _ecrire_onglet(ws_sirh, rows_sirh, verbose)
    _ecrire_onglet(ws_csm,  rows_csm,  verbose)
    _ecrire_onglet(ws_ia,   rows_ia,   verbose)

    wb.save(FICHIER)
