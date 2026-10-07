"""Interroge France Travail + Adzuna (identifiants lus dans .env, jamais affichés).
Usage : python3 fetch_api_ft_adzuna.py <YYYYMMDD>
Écrit relance_<date>_api_brut.json : candidats bruts, déjà filtrés des liens connus du classeur."""
import json, os, sys, time, re, urllib.parse, urllib.request
import openpyxl, add_offre

date = sys.argv[1]
env = {}
for l in open('.env', encoding='utf-8'):
    l = l.strip()
    if l and not l.startswith('#') and '=' in l:
        k, v = l.split('=', 1)
        env[k.strip()] = v.strip().strip('"').strip("'")

MOTS = ["SIRH", "SAP HCM", "SuccessFactors", "consultant SIRH", "chef de projet SIRH", "AMOA SIRH",
        "customer success manager", "account manager SaaS", "product manager", "product owner",
        "UX designer", "product designer", "SEO manager", "formateur IA", "chef de projet digital",
        "project manager", "solutions engineer", "technical account manager", "consultant SAP HR", "HRIS"]
EXCL = re.compile(r'stage|alternan|apprenti|intern\b|internship', re.I)

def get(url, headers=None, data=None):
    req = urllib.request.Request(url, data=data, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read()
            return r.status, (json.loads(body) if body else None)
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception:
        return 0, None

wb = openpyxl.load_workbook('offres_emploi.xlsx')
connus = add_offre._liens_existants(wb)
res, vus = [], set()

# France Travail
d = urllib.parse.urlencode({'grant_type': 'client_credentials', 'client_id': env['FRANCE_TRAVAIL_CLIENT_ID'],
    'client_secret': env['FRANCE_TRAVAIL_CLIENT_SECRET'], 'scope': 'api_offresdemploiv2 o2dsoffre'}).encode()
st, tok = get('https://entreprise.francetravail.fr/connexion/oauth2/access_token?realm=%2Fpartenaire',
              {'Content-Type': 'application/x-www-form-urlencoded'}, d)
print('France Travail auth :', st)
if tok:
    h = {'Authorization': 'Bearer ' + tok['access_token']}
    for m in MOTS:
        for rng in ('0-49', '50-99'):
            st, j = get('https://api.francetravail.io/partenaire/offresdemploi/v2/offres/search?sort=1&range=%s&motsCles=%s'
                        % (rng, urllib.parse.quote(m)), h)
            time.sleep(0.4)
            for o in (j or {}).get('resultats', []):
                lien = (o.get('origineOffre') or {}).get('urlOrigine') or ''
                if not lien or lien in vus or lien in connus or EXCL.search(o.get('intitule', '')) \
                        or o.get('typeContrat') in ('SAI',):
                    continue
                vus.add(lien)
                res.append({'source': 'FranceTravail', 'mot': m, 'Poste': o.get('intitule'),
                    'Entreprise': (o.get('entreprise') or {}).get('nom') or 'N/C',
                    'Localisation': (o.get('lieuTravail') or {}).get('libelle'), 'Contrat': o.get('typeContrat'),
                    'Date': (o.get('dateCreation') or '')[:10], 'Lien': lien,
                    'Description': (o.get('description') or '')[:600]})
# Adzuna
for m in MOTS[:15]:
    st, j = get('https://api.adzuna.com/v1/api/jobs/fr/search/1?app_id=%s&app_key=%s&what=%s&results_per_page=50&sort_by=date&max_days_old=14'
                % (env['ADZUNA_APP_ID'], env['ADZUNA_APP_KEY'], urllib.parse.quote(m)))
    time.sleep(0.5)
    if st != 200:
        print('Adzuna', m, st); continue
    for o in j.get('results', []):
        lien = re.sub(r'\?.*$', '', o.get('redirect_url', ''))
        if not lien or lien in vus or lien in connus or EXCL.search(o.get('title', '')):
            continue
        vus.add(lien)
        res.append({'source': 'Adzuna', 'mot': m, 'Poste': re.sub('<.*?>', '', o.get('title', '')),
            'Entreprise': (o.get('company') or {}).get('display_name') or 'N/C',
            'Localisation': (o.get('location') or {}).get('display_name'), 'Contrat': o.get('contract_time'),
            'Date': (o.get('created') or '')[:10], 'Lien': lien,
            'Description': re.sub('<.*?>', '', o.get('description', ''))[:600]})
json.dump(res, open('relance_%s_api_brut.json' % date, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(res), 'candidats nouveaux écrits dans relance_%s_api_brut.json' % date)
