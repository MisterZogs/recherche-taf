"""
Relance de recherche complète du 24/08/2026 : 5 recherches parallèles
(FR/freelance, APIs ATS + éditeurs HRIS, boards remote/VC/LinkedIn,
IA/PM/niche, USA remote-friendly).

Nettoyage appliqué avant insertion :
- Liens de pages catégorie/listing (free-work.com/jobs/sirh générique,
  eursap sans URL individuelle) : Lien vidé, gardé en note (règle absolue
  du projet contre les liens génériques).
- Liens Ashby/Lever/Greenhouse trouvés via WebSearch et non via API directe
  ont été revérifiés par fetch direct le 24/08 ; les liens morts
  (title générique "Jobs" sur Ashby, redirection ?error=true sur Greenhouse,
  404 sur Lever/Datadog/Flatchr) ont été retirés.
- Doublons inter-agents laissés au dédoublonnage automatique de
  add_offre.py (comparaison stricte de la colonne Lien).
"""

import add_offre
from add_offre import ajouter_offres

add_offre.COLS = add_offre.COLS + ['Date trouvée', 'Date publiée']

D = '2026-08-24'


def prio(remote_txt, fit_txt, note_level='normal'):
    """Heuristique de priorité à partir du texte Remote/Fit."""
    r = (remote_txt or '').lower()
    f = (fit_txt or '').lower()
    if note_level == 'low':
        return '⭐⭐'
    excellent = any(k in f for k in ['excellent fit', 'excellent match', 'meilleure offre', 'confiance maximale'])
    france_explicite = 'france' in r and ('explicite' in r or 'nommée' in r or 'nommément' in r or 'confirmé' in r)
    full_remote = any(k in r for k in ['full remote', 'télétravail total', '100% remote', '100% télétravail', 'remote confirmé', 'remote (isremote=true'])
    if (excellent and (france_explicite or full_remote)) or (france_explicite and excellent):
        return '⭐⭐⭐⭐⭐'
    if france_explicite or (full_remote and excellent):
        return '⭐⭐⭐⭐'
    if full_remote or 'remote emea' in r or 'remote europe' in r:
        return '⭐⭐⭐'
    if 'non précisé' in r or 'à vérifier' in r or 'à confirmer' in r or 'à reconfirmer' in r:
        return '⭐⭐'
    return '⭐⭐'


CSM_EN = 'CV_GaetanFRANCOIS_CSM_EN.pdf'
CSM_FR = 'CV_GaetanFRANCOIS_CSM.pdf'
SIRH_EN = 'Resume_GaetanFRANCOIS_SIRH_EN.pdf'
SIRH_FR = 'Resume_GaetanFRANCOIS_SIRH.pdf'
PM_EN = 'Resume_GaetanFRANCOIS_PM_EN.pdf'
PM_FR = 'Resume_GaetanFRANCOIS_PM_FR.pdf'
PM_PLATFORM_EN = 'Resume_GaetanFRANCOIS_PM_Platform_EN.pdf'
ASHBY_EN = 'Resume_GaetanFRANCOIS_Ashby_EN.pdf'
CONSTRUCTOR_EN = 'Resume_GaetanFRANCOIS_Constructor_EN.pdf'

OFFRES = []

# ============================================================
# 1. Recherche APIs ATS + éditeurs HRIS (agent 2) — 64 offres
#    Source la plus fiable : tirée d'appels API directs.
# ============================================================
_ats = [
    dict(Poste='Senior Customer Success Manager - France', Entreprise='Alan', Lien='https://jobs.ashbyhq.com/alan/fb56b456-c00c-418c-b5b9-ea3aee8a2169', Contrat='CDI', Localisation='Paris, France', Remote='Hybride (télétravail partiel habituel)', CV=CSM_FR),
    dict(Poste='Operational Onboarding Manager - France', Entreprise='Alan', Lien='https://jobs.ashbyhq.com/alan/149e6bff-b83d-4f7f-bfa8-9eb251bf437c', Contrat='CDI', Localisation='Anywhere in France', Remote='Hybride', CV=ASHBY_EN),
    dict(Poste='Senior Product Manager', Entreprise='Pennylane', Lien='https://jobs.ashbyhq.com/pennylane/a4555925-195a-4a59-9367-fcaf27f2113d', Contrat='CDI', Localisation='Paris + remote EU', Remote='Full remote EU', CV=PM_FR),
    dict(Poste='Customer Success Manager - Medium Accounts', Entreprise='Pennylane', Lien='https://jobs.ashbyhq.com/pennylane/d9c454b4-11ab-49f3-9ffe-4b444aecb99d', Contrat='CDI', Localisation='France', Remote='Full remote France', CV=CSM_FR),
    dict(Poste='Customer Success Manager - SAAS', Entreprise='Pennylane', Lien='https://jobs.ashbyhq.com/pennylane/9f24fb70-d2bb-496f-9ed3-02bb9c9d7ad0', Contrat='CDI', Localisation='All France (remote)', Remote='Full remote France', CV=CSM_FR),
    dict(Poste='Manager of Dedicated Implementations - EMEA', Entreprise='Ashby', Lien='https://jobs.ashbyhq.com/ashby/35a01a05-8efd-4bc3-a4bf-0a31d902102d', Contrat='CDI', Localisation='Remote - UE', Remote='Full remote EU', CV=ASHBY_EN),
    dict(Poste='Strategic Customer Success Manager - EMEA', Entreprise='Ashby', Lien='https://jobs.ashbyhq.com/ashby/1cf7c730-caba-4fc3-8b98-52a0735ef14b', Contrat='CDI', Localisation='Remote - UE', Remote='Full remote EU', CV=CSM_EN),
    dict(Poste='Mid-Market Customer Success Manager - EMEA', Entreprise='Ashby', Lien='https://jobs.ashbyhq.com/ashby/62d4f71e-f56c-447a-a965-a9c2ea8eac5e', Contrat='CDI', Localisation='Remote - UE', Remote='Full remote EU', CV=CSM_EN),
    dict(Poste='Senior Sales Engineer - UK', Entreprise='Camunda', Lien='https://jobs.ashbyhq.com/camunda/e98c0d0c-9e42-4fa1-979d-8f2e77295efc', Contrat='CDI', Localisation='United Kingdom', Remote='Full remote UK', CV=PM_PLATFORM_EN),
    dict(Poste='Technical Account Manager - Benelux', Entreprise='Camunda', Lien='https://jobs.ashbyhq.com/camunda/d5ce4070-2d06-4529-956f-a93d05eefd99', Contrat='CDI', Localisation='Netherlands', Remote='Full remote Benelux', CV=CSM_EN),
    dict(Poste='Commercial Solutions Engineer - EMEA', Entreprise='Dash0', Lien='https://jobs.ashbyhq.com/dash0/88dc8222-497c-4d58-ad5b-e862a6602c51', Contrat='CDI', Localisation='EMEA - Remote', Remote='Full remote EMEA', CV=CSM_EN),
    dict(Poste='Enterprise Solutions Engineer - EMEA', Entreprise='Dash0', Lien='https://jobs.ashbyhq.com/dash0/d7fa3468-1e5c-4109-bdcf-0fa0f2f9c15b', Contrat='CDI', Localisation='EMEA - Remote', Remote='Full remote EMEA', CV=CSM_EN),
    dict(Poste='Senior Customer Success Manager', Entreprise='Zip', Lien='https://jobs.ashbyhq.com/zip/a0f04025-e8e7-4164-b02c-d167371e035a', Contrat='CDI', Localisation='London', Remote='Hybride Londres', CV=CSM_EN, low=True),
    dict(Poste='Senior ERP Solutions Consultant', Entreprise='Zip', Lien='https://jobs.ashbyhq.com/zip/8529f344-71e2-4fcf-944a-c8457e71faa1', Contrat='CDI', Localisation='Remote - Germany', Remote='Full remote Allemagne', CV=SIRH_EN),
    dict(Poste='Customer Success Manager - Public Sector & Defense, France', Entreprise='Cohere', Lien='https://jobs.ashbyhq.com/cohere/597e18f5-c33c-4350-8bcd-05a751cece3a', Contrat='CDI', Localisation='France', Remote='France explicite', CV=CSM_EN, excellent=True),
    dict(Poste='Regional Manager, Customer Success EMEA', Entreprise='Constructor', Lien='https://jobs.ashbyhq.com/constructor/5f24d378-f17b-4032-a2cc-079fd670563d', Contrat='CDI', Localisation='Remote - France/Espagne/Portugal', Remote='Full remote, France explicite', CV=CONSTRUCTOR_EN, excellent=True),
    dict(Poste='Account Manager, DACH', Entreprise='Constructor', Lien='https://jobs.ashbyhq.com/constructor/776e4870-92d3-40d4-b2ea-c530537cd616', Contrat='CDI', Localisation='Remote - EMEA', Remote='Full remote EMEA', CV=CONSTRUCTOR_EN),
    dict(Poste='Implementation Consultant, EMEA', Entreprise='Fieldguide', Lien='https://jobs.ashbyhq.com/fieldguide/ce860562-e628-4bf3-9a3a-24caf7734405', Contrat='CDI', Localisation='Remote (UK/Irlande)', Remote='Full remote EMEA', CV=ASHBY_EN),
    dict(Poste='Senior Technical Account Manager (EMEA)', Entreprise='Docker', Lien='https://jobs.ashbyhq.com/docker/de4dce34-7643-4c29-9113-230e7a591195', Contrat='CDI', Localisation='England + EU', Remote='Full remote EMEA', CV=CSM_EN),
    dict(Poste='Senior Implementation Engineer (EMEA)', Entreprise='Docker', Lien='https://jobs.ashbyhq.com/docker/7eb2fabc-f792-4e92-bd5f-50a646732163', Contrat='CDI', Localisation='England + EU', Remote='Full remote EMEA', CV=ASHBY_EN),
    dict(Poste='Senior Solutions Engineer (Pre-Sales); EMEA', Entreprise='Omni', Lien='https://jobs.ashbyhq.com/omni/6f7d41f0-c449-44be-845c-2fbdf226d0fa', Contrat='CDI', Localisation='Dublin / Londres', Remote='Hybride EMEA', CV=CSM_EN, low=True),
    dict(Poste='Technical Programs Manager - Scaled Customer Success (Remote Europe)', Entreprise='n8n', Lien='https://jobs.ashbyhq.com/n8n/d550716c-8cb9-4efe-9a52-b4cd67e193e1', Contrat='CDI', Localisation='Allemagne + EU', Remote='Full remote Europe', CV=CSM_EN),
    dict(Poste='Senior Product Manager - Core Platform', Entreprise='n8n', Lien='https://jobs.ashbyhq.com/n8n/d418f8fb-b2f2-405e-8f22-db73dcf4e8b4', Contrat='CDI', Localisation='Berlin + EU', Remote='Full remote Europe', CV=PM_PLATFORM_EN),
    dict(Poste='Customer Success Lead - Western Europe', Entreprise='ElevenLabs', Lien='https://jobs.ashbyhq.com/elevenlabs/0dbfbe3e-7218-4045-ba78-28b0d2e5ab6d', Contrat='CDI', Localisation='Allemagne + France', Remote='Full remote, France listée', CV=CSM_EN, excellent=True),
    dict(Poste='Customer Success - Scale - Western Europe', Entreprise='ElevenLabs', Lien='https://jobs.ashbyhq.com/elevenlabs/f330bd23-f909-4e50-bf58-9974aee85fc8', Contrat='CDI', Localisation='UK + France', Remote='Full remote, France listée', CV=CSM_EN, excellent=True),
    dict(Poste='GRC Pre-Sales Consultant / Solutions Engineer - EMEA', Entreprise='Vanta', Lien='https://jobs.ashbyhq.com/vanta/d38e7474-2b44-415c-824a-3debb757c9af', Contrat='CDI', Localisation='Londres, UK', Remote='Hybride Londres', CV=CSM_EN, low=True),
    dict(Poste='Senior Product Manager - EMEA - Remote', Entreprise='Pencil', Lien='https://jobs.ashbyhq.com/pencil/e4bbf9ae-0be6-455f-8b24-f960be4c6f2c', Contrat='CDI', Localisation='Europe', Remote='Full remote EMEA', CV=PM_EN, excellent=True),
    dict(Poste='Lead Product Manager - Editor - EMEA', Entreprise='Pencil', Lien='https://jobs.ashbyhq.com/pencil/765370fa-a2b2-487f-af2e-73a53cd1bad6', Contrat='CDI', Localisation='EMEA', Remote='Full remote EMEA', CV=PM_EN),
    dict(Poste='Technical Account Manager, Europe', Entreprise='Socket', Lien='https://jobs.ashbyhq.com/socket/8dec8a77-dafa-448a-a31c-4bf09e9d4f0d', Contrat='CDI', Localisation='United Kingdom', Remote='Full remote UK/Europe', CV=CSM_EN),
    dict(Poste='Customer Success Manager EMEA', Entreprise='Notabene', Lien='https://jobs.ashbyhq.com/notabene/bb86674c-5864-4733-9d37-b585466ebb8b', Contrat='CDI', Localisation='London', Remote='Full remote EMEA', CV=CSM_EN),
    dict(Poste='Client Success Partner - Enterprise', Entreprise='360Learning', Lien='https://jobs.lever.co/360learning/45a216ca-b69f-4623-b3f9-25ceeb444704', Contrat='CDI', Localisation='Paris, Remote', Remote='Full remote France', CV=CSM_FR, excellent=True),
    dict(Poste='Key Account Manager Mid Market', Entreprise='360Learning', Lien='https://jobs.lever.co/360learning/62f460c2-9a8f-4a25-a847-0f8905d9feef', Contrat='CDI', Localisation='Paris, Remote', Remote='Full remote France', CV=CSM_FR),
    dict(Poste='Solution Deployment Manager', Entreprise='360Learning', Lien='https://jobs.lever.co/360learning/0dba50d1-52f4-4114-8421-2f9e19210fde', Contrat='CDI', Localisation='Paris, Remote', Remote='Full remote France', CV=ASHBY_EN),
    dict(Poste='Mid-Market Customer Success Manager EMEA', Entreprise='Teramind', Lien='https://jobs.lever.co/teramind/20c481dc-06b9-41da-99b7-9be053d5b5f7', Contrat='Freelance', Localisation='Pologne', Remote='Full remote EMEA', CV=CSM_EN),
    dict(Poste='Implementation Consultant - Commercial (Remote or Onsite)', Entreprise='Veeva', Lien='https://jobs.lever.co/veeva/f4c4c9f0-4bba-4800-91b5-7dbd61208ac1', Contrat='CDI', Localisation='Paris, France', Remote='France explicite (remote ou onsite)', CV=ASHBY_EN, excellent=True),
    dict(Poste='Product Owner (Link Key Accounts)', Entreprise='Veeva', Lien='https://jobs.lever.co/veeva/eb5a8b4c-d264-4133-a62c-189cd851e38c', Contrat='CDI', Localisation='Londres, UK', Remote='Full remote UK/EU', CV=PM_EN),
    dict(Poste='Product Manager (Internal HRIS / HR Tech)', Entreprise='Jobgether (client anonymisé)', Lien='https://jobs.lever.co/jobgether/c47e031c-99f7-4fb6-aff9-36d2d7f3593e', Contrat='CDI', Localisation='France', Remote='Full remote France', CV=PM_EN, excellent=True),
    dict(Poste='Director of Customer Success', Entreprise='Jobgether (client anonymisé)', Lien='https://jobs.lever.co/jobgether/188b3da3-6e29-455f-af5e-a2e7a62aee4b', Contrat='CDI', Localisation='France', Remote='Full remote France', CV=CSM_EN),
    dict(Poste='Commercial IT Team Lead - Data Migration', Entreprise='Jobgether (client anonymisé)', Lien='https://jobs.lever.co/jobgether/1fdcee08-6ad7-4dec-af34-b21f03b5e9dc', Contrat='CDI', Localisation='France', Remote='Full remote France', CV=SIRH_EN),
    dict(Poste='Group Product Manager - Platform Experience', Entreprise='Jobgether (client anonymisé)', Lien='https://jobs.lever.co/jobgether/3d05c794-a034-48cf-918c-14933214114b', Contrat='CDI', Localisation='France', Remote='Full remote France', CV=PM_PLATFORM_EN),
    dict(Poste='Technical Product Manager - GenAI Programmes', Entreprise='Jobgether (client anonymisé)', Lien='https://jobs.lever.co/jobgether/24b1bb55-b737-4786-9e20-59bd969da871', Contrat='CDI', Localisation='France', Remote='Full remote France', CV=PM_PLATFORM_EN, excellent=True),
    dict(Poste='Chief of Staff for High Growth eCom & DTC Brands', Entreprise='Jobgether (client anonymisé)', Lien='https://jobs.lever.co/jobgether/a86916c1-f3b0-4db6-9be4-3c23bccc029e', Contrat='CDI', Localisation='France', Remote='Full remote France', CV=CSM_EN),
    dict(Poste='Senior Product Manager, Remote Build', Entreprise='Remote.com', Lien='https://job-boards.greenhouse.io/remotecom/jobs/7331443003', Contrat='CDI', Localisation='Remote-France', Remote='France explicite', CV=PM_EN, excellent=True),
    dict(Poste='Senior Workday Implementation Specialist', Entreprise='Remote.com', Lien='https://job-boards.greenhouse.io/remotecom/jobs/7635556003', Contrat='CDI', Localisation='Remote-EMEA', Remote='Full remote EMEA', CV=SIRH_EN, excellent=True),
    dict(Poste='Senior Account Manager - EMEA', Entreprise='Remote.com', Lien='https://job-boards.greenhouse.io/remotecom/jobs/7834363003', Contrat='CDI', Localisation='Remote-EMEA', Remote='Full remote EMEA', CV=CSM_EN),
    dict(Poste='Product Manager, Billing Platform', Entreprise='Remote.com', Lien='https://job-boards.greenhouse.io/remotecom/jobs/7885108003', Contrat='CDI', Localisation='Remote-EMEA', Remote='Full remote EMEA', CV=PM_EN),
    dict(Poste="Senior Payroll Implementation Specialist - NL & Belgium", Entreprise='Remote.com', Lien='https://job-boards.greenhouse.io/remotecom/jobs/7799068003', Contrat='CDI', Localisation="Remote-Western Europe", Remote="Full remote Europe de l'Ouest", CV=SIRH_EN),
    dict(Poste='Customer Success Architect, EMEA', Entreprise='GitLab', Lien='https://job-boards.greenhouse.io/gitlab/jobs/8561952002', Contrat='CDI', Localisation='Remote, Autriche/France/Allemagne', Remote='France explicite', CV=CSM_EN, excellent=True),
    dict(Poste='Manager, Customer Success Managers, EMEA', Entreprise='GitLab', Lien='https://job-boards.greenhouse.io/gitlab/jobs/8613199002', Contrat='CDI', Localisation='Remote, Autriche/Allemagne', Remote='Full remote EMEA', CV=CSM_EN),
    dict(Poste='Implementation Consultant - German Fluency', Entreprise='Samsara', Lien='https://www.samsara.com/company/careers/roles/8076687?gh_jid=8076687', Contrat='CDI', Localisation='Londres, UK / Remote', Remote='Full remote UK/Allemagne', CV=ASHBY_EN),
    dict(Poste='Enterprise Customer Success Manager (French speaker)', Entreprise='Canonical', Lien='https://job-boards.greenhouse.io/canonical/jobs/7084000', Contrat='CDI', Localisation='Home based - EMEA', Remote='Full remote EMEA (francophone)', CV=CSM_EN, excellent=True),
    dict(Poste='Product Manager - AI', Entreprise='Canonical', Lien='https://job-boards.greenhouse.io/canonical/jobs/6643476', Contrat='CDI', Localisation='Home based - EMEA', Remote='Full remote EMEA', CV=PM_EN),
    dict(Poste='Solutions Engineer | France | Remote', Entreprise='Grafana Labs', Lien='https://job-boards.greenhouse.io/grafanalabs/jobs/6121627004', Contrat='CDI', Localisation='France (Remote)', Remote='France explicite, sans prérequis linguistique', CV=CSM_EN, excellent=True),
    dict(Poste='Customer Success Manager, EMEA', Entreprise='Customer.io', Lien='https://job-boards.greenhouse.io/customerio/jobs/8089365', Contrat='CDI', Localisation='EMEA Remote', Remote='Full remote EMEA', CV=CSM_EN),
    dict(Poste='Enterprise Sales Engineer - France', Entreprise='Chainguard', Lien='https://job-boards.greenhouse.io/chainguard/jobs/4702184006', Contrat='CDI', Localisation='France - Remote', Remote='France explicite', CV=CSM_EN, excellent=True),
    dict(Poste='Senior Customer Success Manager - Germany', Entreprise='Chainguard', Lien='https://job-boards.greenhouse.io/chainguard/jobs/4704918006', Contrat='CDI', Localisation='Germany - Remote', Remote='Full remote Allemagne', CV=CSM_EN),
    dict(Poste='Principal Product Manager, Document Domain', Entreprise='PandaDoc', Lien='https://job-boards.greenhouse.io/pandadoc/jobs/7661661', Contrat='CDI', Localisation='Remote (Allemagne + EU)', Remote='Full remote Europe', CV=PM_EN),
    dict(Poste='Onboarding Project Manager', Entreprise='Cloudbeds', Lien='https://job-boards.greenhouse.io/cloudbeds/jobs/4697369005', Contrat='CDI', Localisation='Europe', Remote='Full remote Europe', CV=ASHBY_EN),
    dict(Poste='Professional Services Consultant (Self Service), EMEA', Entreprise='Abnormal Security', Lien='https://abnormal.ai/careers/jobs/7809392003?gh_jid=7809392003', Contrat='CDI', Localisation='Remote - UK', Remote='Full remote EMEA', CV=ASHBY_EN),
    dict(Poste='Senior Implementation Consultant | UK', Entreprise='Degreed', Lien='https://job-boards.greenhouse.io/degreed/jobs/6130184004', Contrat='CDI', Localisation='UK Based | Remote', Remote='Full remote UK', CV=ASHBY_EN, excellent=True),
    dict(Poste='Account Manager, Strategic - France', Entreprise='Atlassian', Lien='https://globalcareers-atlassian.icims.com/jobs/25256/account-manager%2c-strategic---france/job', Contrat='CDI', Localisation='Remote - France', Remote='France explicite', CV=CSM_EN, excellent=True),
    dict(Poste='Principal Customer Success Manager, Strategic, France', Entreprise='Atlassian', Lien='https://globalcareers-atlassian.icims.com/jobs/26057/principal-customer-success-manager%2c-strategic%2c-france/job', Contrat='CDI', Localisation='Remote - France / Paris', Remote='France explicite', CV=CSM_EN, excellent=True),
    dict(Poste='Senior Principal Customer Success Manager, Strategic - France', Entreprise='Atlassian', Lien='https://globalcareers-atlassian.icims.com/jobs/26241/senior-principal-customer-success-manager%2c-strategic---france/job', Contrat='CDI', Localisation='Remote - France / Paris', Remote='France explicite', CV=CSM_EN, excellent=True),
    dict(Poste='Principal Customer Success Manager, Strategic DACH', Entreprise='Atlassian', Lien='https://globalcareers-atlassian.icims.com/jobs/26063/principal-customer-success-manager%2c-strategic-dach/job', Contrat='CDI', Localisation='Remote - Allemagne (France en option)', Remote='France listée en option', CV=CSM_EN),
]
for o in _ats:
    low = o.pop('low', False)
    excellent = o.pop('excellent', False)
    fit = 'Excellent fit' if excellent else 'Bon fit'
    OFFRES.append({
        'Priorité': prio(o['Remote'], fit, 'low' if low else 'normal'),
        'Statut': '', 'Fait': '',
        'Poste': o['Poste'], 'Entreprise': o['Entreprise'], 'Source': 'API ATS (Ashby/Lever/Greenhouse/Atlassian)',
        'Lien': o['Lien'], 'Contrat': o['Contrat'], 'Localisation': o['Localisation'],
        'Remote': o['Remote'], 'Salaire / TJM': 'Non précisé', 'Durée mission': '',
        'Fit / Notes': fit + ' — relance 24/08/2026, API ATS', 'CV à envoyer': o['CV'], 'Prétention': '',
        'Date trouvée': D, 'Date publiée': '',
    })

print(f"Bloc 1 (APIs ATS) : {len(_ats)} offres")
