"""Relance exhaustive du 18/08/2026.

Sources couvertes : API carrieres Atlassian (iCIMS), API Ashby (constructor,
elevenlabs, n8n, vanta, linear, owkin, ashby, notion, pennylane, alan, pleo,
harvey, amplitude, doctolib, qonto, docker, vapi, fieldguide, siena, neara,
openai, replit, supabase, clickup, sift, revenuecat), API Lever (sitetracker,
swile, aircall, qonto, malt, valiantys, scality, remofirst, jobgether, mistral),
API Greenhouse (remotecom, gitlab, samsara, canonical, grafanalabs, cloudflare,
figma, airtable, gusto, justworks), free-work (/jobs/sirh pages 1-2,
/jobs/sap-hcm, /jobs/ia, /jobs/ia-generative), LinkedIn pages categories (HRIS,
CSM France, formateur IA France), eursap, hansonregan, jobs.hr-path.com,
jobs.sap.com, mission-freelances, collective.work, weworkremotely,
welcometothejungle, upwork, remoterocketship, plus WebSearch sur les quatre
metiers ajoutes le 14/08 (Solutions Engineer, TAM, Implementation Consultant,
Data Migration Lead).

Verifications faites avant ajout :
- Les liens Ashby, Lever, Greenhouse et iCIMS proviennent directement des API
  publiques : un poste absent du JSON est ferme, donc tout lien retenu est vif.
- SMARTPOINT Consultant IA Generative / Claude et Freelance.com Expert IA
  generative : fiches ouvertes une par une, les deux sont en teletravail
  partiel, donc NoRemote malgre un intitule tres proche du profil.
- Valiantys Principal Transformation Consultant : la variante France est en
  hybride Paris, seule la variante Allemagne est en remote.

Ecartes (deja presents au tableur) : Docker Senior TAM EMEA, Customer.io CSM
EMEA, Canonical Enterprise CSM French speaker, ElevenLabs Customer Success Lead
Western Europe et Customer Success - Southern Europe, n8n AI Product Manager et
Technical Programs Manager, Constructor Regional Manager CS EMEA et Senior PM
Merchant Intelligence, Linear Product Manager Europe, Jobgether Technical
Product Manager GenAI, mission-freelances Formateur en ligne IA.

Ecartes (hors profil) : Pennylane Responsable Onboarding Comptable (expertise
comptable requise), Grafana Senior Solutions Engineer France (arabe exige),
Docker Senior Sales Engineer Strategic EMEA (allemand exige), Fieldguide et
Vanta (remote US uniquement), Samsara Implementation Consultant (UK/Allemagne
uniquement, pas la France).
"""

import add_offre

add_offre.COLS = add_offre.COLS + ['Date trouvée', 'Date publiée']

D = '18/08/2026'
FW = 'https://www.free-work.com'

CV_SIRH_FR = 'Resume_GaetanFRANCOIS_SIRH.pdf'
CV_SIRH_EN = 'Resume_GaetanFRANCOIS_SIRH_EN.pdf'
CV_CSM_EN = 'CV_GaetanFRANCOIS_CSM_EN.pdf'
CV_CSM_FR = 'CV_GaetanFRANCOIS_CSM.pdf'
CV_PM_EN = 'Resume_GaetanFRANCOIS_PM_EN.pdf'
CV_PM_FR = 'Resume_GaetanFRANCOIS_PM_FR.pdf'
CV_PM_PLAT = 'Resume_GaetanFRANCOIS_PM_Platform_EN.pdf'
CV_ASHBY = 'Resume_GaetanFRANCOIS_Ashby_EN.pdf'
CV_CONSTR = 'Resume_GaetanFRANCOIS_Constructor_EN.pdf'
CV_IA = 'Resume_GaetanFRANCOIS_IA.pdf'


def o(prio, poste, entreprise, source, contrat, loc, remote, salaire, duree,
      notes, lien, cv, publiee=''):
    return {
        'Priorité': prio, 'Statut': '', 'Fait': '', 'Poste': poste,
        'Entreprise': entreprise, 'Source': source, 'Contrat': contrat,
        'Localisation': loc, 'Remote': remote, 'Salaire / TJM': salaire,
        'Durée mission': duree, 'Fit / Notes': notes, 'Lien': lien,
        'CV à envoyer': cv, 'Prétention': '',
        'Date trouvée': D, 'Date publiée': publiee,
    }


OFFRES = [

    # ── Atlassian (API carrieres iCIMS) ──────────────────────────────────────
    o('⭐⭐⭐⭐', 'Account Manager, Strategic - France', 'Atlassian',
      'API carrières Atlassian', 'CDI', 'France', 'Full remote', 'n.c.', '-',
      'Gestion de comptes stratégiques France chez un éditeur SaaS majeur ; '
      'remote France confirmé dans les localisations du poste.',
      'https://globalcareers-atlassian.icims.com/jobs/25256/account-manager%2c-strategic---france/job',
      CV_CSM_EN),

    o('⭐⭐⭐⭐', 'Senior Services Solutions Advocate', 'Atlassian',
      'API carrières Atlassian', 'CDI', 'Paris / Remote France', 'Full remote',
      'n.c.', '-',
      'Avant-vente des services professionnels ; croisement direct entre '
      'déploiement client et posture conseil, remote France listé.',
      'https://globalcareers-atlassian.icims.com/jobs/26249/senior-services-solutions-advocate/job',
      CV_ASHBY),

    o('⭐⭐⭐', 'Strategic Solutions Sales Executive - Southern Europe', 'Atlassian',
      'API carrières Atlassian', 'CDI', 'Paris / Remote France', 'Full remote',
      'n.c.', '-',
      'Poste très orienté vente de solutions ; le remote France est listé mais '
      'le quota commercial pèse plus que le conseil.',
      'https://globalcareers-atlassian.icims.com/jobs/25170/strategic-solutions-sales-executive---southern-europe/job',
      CV_CSM_EN),

    # ── Ashby (API publique) ─────────────────────────────────────────────────
    o('⭐⭐⭐⭐⭐', 'Manager of Dedicated Implementations - EMEA', 'Ashby',
      'API Ashby', 'CDI', 'Remote European Union', 'Full remote', 'n.c.', '-',
      'Encadrement d\'une équipe de déploiement client chez un éditeur SaaS, '
      'remote UE : c\'est exactement le poste pour lequel le CV Ashby a été '
      'construit.',
      'https://jobs.ashbyhq.com/ashby/35a01a05-8efd-4bc3-a4bf-0a31d902102d',
      CV_ASHBY),

    o('⭐⭐⭐⭐', 'Enterprise Solutions Engineer - France', 'ElevenLabs',
      'API Ashby', 'CDI', 'France', 'Full remote', 'n.c.', '-',
      'Avant-vente technique grands comptes depuis la France ; le bagage '
      'ingénieur et l\'appel d\'offres L\'Oréal servent directement.',
      'https://jobs.ashbyhq.com/elevenlabs/ce00fe7b-a93a-436b-bd5e-2eff87c48f23',
      CV_CSM_EN),

    o('⭐⭐⭐⭐', 'Customer Success Manager - SAAS', 'Pennylane',
      'API Ashby', 'CDI', 'France', 'Full remote (All France)', 'n.c.', '-',
      'Éditeur français, poste ouvert partout en France en remote ; '
      'candidature en français.',
      'https://jobs.ashbyhq.com/pennylane/9f24fb70-d2bb-496f-9ed3-02bb9c9d7ad0',
      CV_CSM_FR),

    o('⭐⭐⭐', 'Présales & Enablement Specialist', 'Pennylane',
      'API Ashby', 'CDI', 'France', 'Full remote (All France)', 'n.c.', '-',
      'Avant-vente et enablement chez un éditeur SaaS français, remote total ; '
      'poste plus junior que la cible mais bien aligné sur le métier.',
      'https://jobs.ashbyhq.com/pennylane/69d31eee-dff2-449a-ab07-4f941af74ccc',
      CV_CSM_FR),

    o('⭐⭐⭐', 'Operational Onboarding Manager - France', 'Alan',
      'API Ashby', 'CDI', 'Anywhere in France', 'Full remote', 'n.c.', '-',
      'Déploiement et onboarding client chez un assureur santé SaaS ; remote '
      'partout en France, annonce en français.',
      'https://jobs.ashbyhq.com/alan/149e6bff-b83d-4f7f-bfa8-9eb251bf437c',
      CV_SIRH_FR),

    o('⭐⭐⭐⭐⭐', 'Product Manager: Customer Onboarding Experience', 'Constructor',
      'API Ashby', 'CDI', 'Remote', 'Full remote', 'n.c.', '-',
      'Produit sur l\'onboarding et l\'adoption client : l\'intersection la '
      'plus crédible entre le parcours Customer Success et le rôle de Product '
      'Manager chez WallOfTraders.com.',
      'https://jobs.ashbyhq.com/constructor/e8fa6194-ef2e-47d3-ab45-a9112d87da24',
      CV_PM_EN),

    o('⭐⭐', 'Senior Product Manager: Recall', 'Constructor',
      'API Ashby', 'CDI', 'Remote EMEA', 'Full remote', 'n.c.', '-',
      'Produit search/recall très technique ; remote EMEA confirmé mais le '
      'domaine reste éloigné du parcours.',
      'https://jobs.ashbyhq.com/constructor/7bc86d05-145d-4b7c-aa6e-b0b207d46117',
      CV_PM_PLAT),

    o('⭐⭐⭐', 'Head of Solutions Engineering', 'n8n',
      'API Ashby', 'CDI', 'Remote Europe', 'Full remote', 'n.c.', '-',
      'Direction d\'une équipe avant-vente, remote Europe ; la France ne '
      'figure pas dans la liste des pays, à vérifier avant de postuler.',
      'https://jobs.ashbyhq.com/n8n/443fd5c2-6501-45cf-b8c8-851fe94d48f9',
      CV_CONSTR),

    o('⭐⭐⭐⭐', 'Head of Customer Success', 'RevenueCat',
      'API Ashby', 'CDI', 'EMEA', 'Full remote', 'n.c.', '-',
      'Direction Customer Success chez un éditeur remote-first où Gaëtan a '
      'déjà une offre CSM au tableur ; poste d\'encadrement.',
      'https://jobs.ashbyhq.com/revenuecat/90ae74ea-0127-4755-8f68-277138027d7e',
      CV_CONSTR),

    o('⭐⭐⭐', 'Senior Sales Engineer', 'RevenueCat',
      'API Ashby', 'CDI', 'Remote Europe', 'Full remote', 'n.c.', '-',
      'Avant-vente technique remote Europe ; produit orienté développeurs, '
      'c\'est la lacune connue à concéder en lettre de motivation.',
      'https://jobs.ashbyhq.com/revenuecat/7be6fbcd-dc75-4336-975a-e2460b867581',
      CV_CSM_EN),

    o('⭐⭐⭐', 'Customer Solution Architect (EMEA)', 'Supabase',
      'API Ashby', 'CDI', 'Remote EMEA', 'Full remote', 'n.c.', '-',
      'Architecte solution côté client, remote EMEA ; profil produit '
      'développeur, plus technique que la cible habituelle.',
      'https://jobs.ashbyhq.com/supabase/c3099780-60d5-4b8a-ab08-c701d114cf62',
      CV_CSM_EN),

    o('⭐⭐', 'Product Manager - Marketplace', 'Supabase',
      'API Ashby', 'CDI', 'Remote', 'Full remote', 'n.c.', '-',
      'Produit marketplace pour développeurs ; remote total mais audience '
      'technique éloignée du parcours.',
      'https://jobs.ashbyhq.com/supabase/23c9ce7e-6b7b-4316-8f00-8f318e902441',
      CV_PM_PLAT),

    o('⭐⭐⭐', 'Solutions Engineer - EMEA', 'Vapi',
      'API Ashby', 'CDI', 'Amsterdam / EMEA', 'Full remote', 'n.c.', '-',
      'Avant-vente sur une plateforme d\'agents vocaux IA ; croisement '
      'intéressant entre l\'axe IA et l\'axe avant-vente.',
      'https://jobs.ashbyhq.com/vapi/dce1928f-b432-4d6b-8c2f-b7c63c672310',
      CV_CSM_EN),

    o('⭐⭐', 'Strategic Account Manager', 'Siena AI',
      'API Ashby', 'CDI', 'Remote Europe', 'Full remote', 'n.c.', '-',
      'Gestion de comptes stratégiques, remote Europe ; poste basé New York '
      'avec une option Europe, décalage horaire à vérifier.',
      'https://jobs.ashbyhq.com/siena/6335ebaf-54e2-49ae-bc50-4a686de55d9e',
      CV_CSM_EN),

    o('⭐⭐', 'Customer Success Manager, Portugal', 'Neara',
      'API Ashby', 'CDI', 'UK / Europe', 'Full remote', 'n.c.', '-',
      'CSM sur un produit de jumeau numérique de réseaux électriques ; zone '
      'Portugal affichée, ouverture France à confirmer.',
      'https://jobs.ashbyhq.com/neara/e9105548-20c6-40d4-8d97-b1c9676f582b',
      CV_CSM_EN),

    # ── Greenhouse (API publique) ────────────────────────────────────────────
    o('⭐⭐⭐⭐⭐', 'Customer Success Architect, EMEA', 'GitLab',
      'API Greenhouse', 'CDI', 'Remote France / Allemagne / Autriche',
      'Full remote (France listée)', 'n.c.', '-',
      'La France est explicitement dans les localisations remote ; poste '
      'd\'architecte Customer Success, la meilleure trouvaille de la relance '
      'côté CSM.',
      'https://job-boards.greenhouse.io/gitlab/jobs/8561952002',
      CV_CSM_EN),

    o('⭐⭐⭐⭐', 'Senior Professional Services Project Manager (EMEA)', 'GitLab',
      'API Greenhouse', 'CDI', 'Remote EMEA', 'Full remote', 'n.c.', '-',
      'Pilotage de projets de services professionnels : quinze ans de '
      'déploiement client répondent directement au besoin.',
      'https://job-boards.greenhouse.io/gitlab/jobs/8622433002',
      CV_ASHBY),

    o('⭐⭐⭐⭐⭐', 'Senior Product Manager, HRIS Integrations', 'Remote.com',
      'API Greenhouse', 'CDI', 'Remote EMEA', 'Full remote', 'n.c.', '-',
      'Produit sur les intégrations SIRH : le croisement exact entre le rôle '
      'de Product Manager et quatorze ans de SAP HR ; à traiter en priorité.',
      'https://job-boards.greenhouse.io/remotecom/jobs/7791136003',
      CV_PM_PLAT),

    o('⭐⭐⭐⭐', 'Senior Workday Implementation Specialist', 'Remote.com',
      'API Greenhouse', 'CDI', 'Remote EMEA', 'Full remote', 'n.c.', '-',
      'Déploiement Workday chez un acteur paie/RH global ; le parcours SAP HR '
      'et OnePayroll se transpose, l\'outil diffère.',
      'https://job-boards.greenhouse.io/remotecom/jobs/7635556003',
      CV_SIRH_EN),

    o('⭐⭐⭐⭐', 'Senior Account Manager - EMEA', 'Remote.com',
      'API Greenhouse', 'CDI', 'Remote EMEA', 'Full remote', 'n.c.', '-',
      'Gestion de comptes chez un éditeur RH/paie global, remote EMEA ; '
      'plusieurs postes Remote.com sont déjà suivis au tableur.',
      'https://job-boards.greenhouse.io/remotecom/jobs/7834363003',
      CV_CSM_EN),

    o('⭐⭐⭐⭐', 'Senior Product Manager, Remote Build', 'Remote.com',
      'API Greenhouse', 'CDI', 'Remote France', 'Full remote', 'n.c.', '-',
      'Poste produit avec une localisation remote France explicite chez un '
      'éditeur RH ; combinaison rare et à privilégier.',
      'https://job-boards.greenhouse.io/remotecom/jobs/7331443003',
      CV_PM_EN),

    o('⭐⭐⭐', 'Senior Product Manager, Reporting & Insights', 'Remote.com',
      'API Greenhouse', 'CDI', 'Remote EMEA', 'Full remote', 'n.c.', '-',
      'Produit reporting et analytics RH ; domaine familier, remote EMEA.',
      'https://job-boards.greenhouse.io/remotecom/jobs/7885155003',
      CV_PM_EN),

    o('⭐⭐⭐', 'Product Manager, Contractor Management', 'Remote.com',
      'API Greenhouse', 'CDI', 'Remote EMEA', 'Full remote', 'n.c.', '-',
      'Produit sur la gestion des contractors, proche des processus RH '
      'connus ; remote EMEA.',
      'https://job-boards.greenhouse.io/remotecom/jobs/7885031003',
      CV_PM_EN),

    o('⭐⭐⭐', 'Product Manager, Billing Platform', 'Remote.com',
      'API Greenhouse', 'CDI', 'Remote EMEA', 'Full remote', 'n.c.', '-',
      'Plateforme de facturation ; sujet plateforme B2B, remote EMEA.',
      'https://job-boards.greenhouse.io/remotecom/jobs/7885108003',
      CV_PM_PLAT),

    o('⭐⭐', 'Senior Product Manager, APIs', 'Remote.com',
      'API Greenhouse', 'CDI', 'Remote EMEA', 'Full remote', 'n.c.', '-',
      'Produit orienté développeurs (API, SDK) : c\'est la lacune identifiée '
      'sur les postes produit dev-facing.',
      'https://job-boards.greenhouse.io/remotecom/jobs/7831380003',
      CV_PM_PLAT),

    o('⭐⭐⭐⭐', 'Solutions Engineer | France | Remote', 'Grafana Labs',
      'API Greenhouse', 'CDI', 'France', 'Full remote', 'n.c.', '-',
      'Avant-vente technique basée en France chez un éditeur observabilité ; '
      'remote France confirmé, sans exigence de langue supplémentaire.',
      'https://job-boards.greenhouse.io/grafanalabs/jobs/6121627004',
      CV_CSM_EN),

    o('⭐⭐⭐', 'Product Manager', 'Canonical',
      'API Greenhouse', 'CDI', 'Home based EMEA', 'Full remote', 'n.c.', '-',
      'Éditeur entièrement remote où Gaëtan suit déjà des postes CSM ; '
      'plusieurs postes produit ouverts simultanément.',
      'https://job-boards.greenhouse.io/canonical/jobs/5029257',
      CV_PM_EN),

    o('⭐⭐⭐', 'Product Manager - AI', 'Canonical',
      'API Greenhouse', 'CDI', 'Home based EMEA', 'Full remote', 'n.c.', '-',
      'Poste produit sur les sujets IA chez un éditeur 100% remote ; '
      'croisement des deux axes de recherche produit et IA.',
      'https://job-boards.greenhouse.io/canonical/jobs/6643476',
      CV_PM_EN),

    o('⭐⭐⭐', 'Manager, Product Manager', 'Canonical',
      'API Greenhouse', 'CDI', 'Home based EMEA', 'Full remote', 'n.c.', '-',
      'Encadrement d\'une équipe produit, remote EMEA ; process de '
      'recrutement Canonical réputé long et écrit.',
      'https://job-boards.greenhouse.io/canonical/jobs/6458166',
      CV_PM_EN),

    # ── Jobgether (Lever, variantes France uniquement) ───────────────────────
    o('⭐⭐⭐⭐', 'Technical Account Manager', 'n.c. (via Jobgether)',
      'Lever / Jobgether', 'CDI', 'France', 'Full remote', 'n.c.', '-',
      'Gestion de compte à composante technique, remote France ; client masqué '
      'par Jobgether, à identifier avant de candidater.',
      'https://jobs.lever.co/jobgether/287fb3ac-1df4-43e4-9125-bf4f109ee898',
      CV_CSM_EN, '13/08/2026'),

    o('⭐⭐⭐', 'Senior Customer Success Manager', 'n.c. (via Jobgether)',
      'Lever / Jobgether', 'CDI', 'France', 'Full remote', 'n.c.', '-',
      'CSM senior remote France ; vérifier l\'employeur réel, Jobgether '
      'republie la même annonce par pays.',
      'https://jobs.lever.co/jobgether/992dc8f5-c2a5-4745-a261-e0761069a1a5',
      CV_CSM_EN, '12/08/2026'),

    o('⭐⭐⭐', 'Customer Success Manager', 'n.c. (via Jobgether)',
      'Lever / Jobgether', 'CDI', 'France', 'Full remote', 'n.c.', '-',
      'CSM remote France publié le 14/08 ; client non identifié.',
      'https://jobs.lever.co/jobgether/bbf57ea5-fdfc-458b-841b-f49d0704e96d',
      CV_CSM_EN, '14/08/2026'),

    o('⭐⭐⭐', 'Enterprise Sales Engineer', 'n.c. (via Jobgether)',
      'Lever / Jobgether', 'CDI', 'France', 'Full remote', 'n.c.', '-',
      'Avant-vente grands comptes remote France ; niveau de technicité à '
      'vérifier sur la fiche complète.',
      'https://jobs.lever.co/jobgether/6f743dda-8412-42fe-b9d6-83b3921c35ac',
      CV_CSM_EN, '14/08/2026'),

    o('⭐⭐', 'Sr Account Manager', 'n.c. (via Jobgether)',
      'Lever / Jobgether', 'CDI', 'France', 'Full remote', 'n.c.', '-',
      'Gestion de comptes senior remote France ; annonce générique.',
      'https://jobs.lever.co/jobgether/5eb603e4-d687-47a7-8321-de504996ba6d',
      CV_CSM_EN, '13/08/2026'),

    o('⭐⭐', 'SMB Account Manager', 'n.c. (via Jobgether)',
      'Lever / Jobgether', 'CDI', 'France', 'Full remote', 'n.c.', '-',
      'Segment PME, donc en dessous du niveau grands comptes visé.',
      'https://jobs.lever.co/jobgether/170d75f7-38b2-4792-8502-469e704636e6',
      CV_CSM_EN, '14/08/2026'),

    o('⭐⭐', 'Customer Success Partner - German Speaking', 'n.c. (via Jobgether)',
      'Lever / Jobgether', 'CDI', 'France', 'Full remote', 'n.c.', '-',
      'Remote France mais allemand courant exigé, que Gaëtan ne parle pas.',
      'https://jobs.lever.co/jobgether/73173375-9297-4bfc-a2b9-abbb7eadf01e',
      CV_CSM_EN, '17/08/2026'),

    o('⭐⭐⭐', 'Senior Product Manager', 'n.c. (via Jobgether)',
      'Lever / Jobgether', 'CDI', 'France', 'Full remote', 'n.c.', '-',
      'Poste produit senior remote France ; identifier l\'éditeur avant de '
      'choisir entre le CV PM_EN et le CV PM_FR.',
      'https://jobs.lever.co/jobgether/a5a8bf12-9b94-4d4c-a39e-ce4c0351f9fb',
      CV_PM_EN, '14/08/2026'),

    o('⭐⭐⭐', 'Product Manager', 'n.c. (via Jobgether)',
      'Lever / Jobgether', 'CDI', 'France', 'Full remote', 'n.c.', '-',
      'Product Manager remote France publié le 17/08.',
      'https://jobs.lever.co/jobgether/37a7e1bf-c2be-4125-991c-51a0e397840a',
      CV_PM_EN, '17/08/2026'),

    o('⭐⭐⭐', 'Group Product Manager - Platform Experience',
      'n.c. (via Jobgether)', 'Lever / Jobgether', 'CDI', 'France',
      'Full remote', 'n.c.', '-',
      'Produit plateforme avec une dimension encadrement ; remote France, '
      'publié le 18/08.',
      'https://jobs.lever.co/jobgether/3d05c794-a034-48cf-918c-14933214114b',
      CV_PM_PLAT, '18/08/2026'),

    o('⭐⭐', 'Product owner', 'n.c. (via Jobgether)',
      'Lever / Jobgether', 'CDI', 'France', 'Full remote', 'n.c.', '-',
      'Intitulé très générique, contexte produit à clarifier.',
      'https://jobs.lever.co/jobgether/5405e9ec-8ab3-4075-8f5e-96425e4f11a6',
      CV_PM_FR, '11/08/2026'),

    o('⭐⭐', 'Senior Product Manager, APIs', 'n.c. (via Jobgether)',
      'Lever / Jobgether', 'CDI', 'France', 'Full remote', 'n.c.', '-',
      'Produit API dev-facing ; même lacune que le poste Remote.com du même '
      'intitulé, il s\'agit peut-être de la même annonce republiée.',
      'https://jobs.lever.co/jobgether/b8f8d83e-53fd-4a1b-a22d-2f2ac946a353',
      CV_PM_PLAT, '18/08/2026'),

    o('⭐', 'Product Manager (Kubernetes / Ansible / IaC)',
      'n.c. (via Jobgether)', 'Lever / Jobgether', 'CDI', 'France',
      'Full remote', 'n.c.', '-',
      'Infrastructure pure : hors profil, gardé pour trace.',
      'https://jobs.lever.co/jobgether/2c75a0c6-0b7a-4400-b3df-67b03d82a60d',
      CV_PM_PLAT, '18/08/2026'),

    # ── SIRH / SAP ───────────────────────────────────────────────────────────
    o('⭐⭐⭐⭐', 'Consultant SAP SuccessFactors (H/F)', 'HR Path',
      'jobs.hr-path.com', 'CDI', 'Paris La Défense', 'Oui (télétravail)',
      'n.c.', '-',
      'Modules EC, PMGM, RCM, ONB, LMS, ECP ; télétravail confirmé dans '
      'l\'annonce avec déplacements ponctuels. HR Path est le cabinet le plus '
      'ciblé du dispositif.',
      'https://jobs.hr-path.com/job/Paris-La-D%C3%A9fense-Cedex-Consultant-SAP-SuccessFactors-(HF)-75-92042/818651901/',
      CV_SIRH_FR, '14/08/2026'),

    o('⭐⭐⭐', 'Senior SAP SuccessFactors Consultant', 'Zalaris',
      'remoterocketship / zalaris.com', 'CDI', 'Royaume-Uni', 'Full remote',
      'n.c.', '-',
      'Spécialiste SAP HR nordique ; poste remote UK, ouverture depuis la '
      'France à confirmer auprès du recruteur.',
      'https://www.remoterocketship.com/company/zalaris/jobs/senior-sap-successfactors-consultant-united-kingdom-remote/',
      CV_SIRH_EN),

    o('⭐⭐⭐', 'SAP HCM Payroll or SF EC Payroll Consultant', 'n.c. (via Eursap)',
      'eursap.eu', 'CDI', 'Pays-Bas', 'Non', '103 480 €/an + bonus', '-',
      'Néerlandais exigé et poste sur site ; conservé pour mémoire du marché '
      'paie SAP en Europe du Nord.',
      'https://eursap.eu/jobs/sap-hcm-payroll-or-sf-ec-payroll-consultant-35441-nl',
      CV_SIRH_EN),

    o('⭐⭐', 'SAP SF LMS Consultant', 'n.c. (via Hanson Regan)',
      'hansonregan.com', 'Freelance', 'Portugal', 'Full remote (anywhere)',
      'Négociable', '-',
      'Trois implémentations LMS de bout en bout exigées ; le module LMS reste '
      'périphérique dans le parcours.',
      'https://hansonregan.com/job/sap-sf-lms-consultant/',
      CV_SIRH_EN),

    # ── Free-work : missions SIRH et IA (télétravail non confirmé) ───────────
    o('⭐⭐⭐⭐', 'Manager SIRH', 'HR DNA', 'free-work.com', 'CDI', 'Paris',
      'n.p.', '60 000 - 110 000 €/an', '-',
      'Fourchette salariale large qui couvre la cible Group HRIS Manager ; '
      'télétravail non précisé dans l\'annonce.',
      FW + '/fr/tech-it/job-mission/administrateur-applicatif-erp-crm-sirh/manager-sirh-11',
      CV_SIRH_FR, '12/08/2026'),

    o('⭐⭐⭐⭐', 'Chef de projet IT / Responsable SIRH (H/F)', 'LeHibou',
      'free-work.com', 'Freelance', 'Bordeaux', 'n.p.', '675 €/j', '9 mois',
      'Mission longue à TJM élevé dans le Sud-Ouest ; télétravail à négocier, '
      'Bordeaux reste proche d\'Anglet.',
      FW + '/fr/tech-it/job-mission/administrateur-applicatif-erp-crm-sirh/chef-de-projet-it-responsable-sirh-h-f',
      CV_SIRH_FR, '13/08/2026'),

    o('⭐⭐⭐', 'Responsable applicatif SIRH (H/F) - Freelance', 'GROUPE ARTEMYS',
      'free-work.com', 'Freelance', 'Paris', 'n.p.', '550 - 650 €/j', '6 mois',
      'Pilotage applicatif SIRH ; télétravail non précisé.',
      FW + '/fr/tech-it/job-mission/administrateur-applicatif-erp-crm-sirh/responsable-applicatif-sirh-h-f-freelance',
      CV_SIRH_FR, '14/08/2026'),

    o('⭐⭐⭐', 'Chargé de missions SIRH N2 - Workday HCM (H/F)', 'HR DNA',
      'free-work.com', 'Freelance', 'Neuilly-sur-Marne', 'n.p.',
      '250 - 500 €/j', '24 mois',
      'Mission de deux ans sur Workday HCM ; niveau N2 en dessous de la cible.',
      FW + '/fr/tech-it/job-mission/administrateur-applicatif-erp-crm-sirh/charge-de-missions-sirh-n2-workday-hcm-h-f-25',
      CV_SIRH_FR, '16/08/2026'),

    o('⭐⭐⭐', 'Chef de projet MOE SIRH H/F', 'HAYS France', 'free-work.com',
      'CDI', 'Paris', 'n.p.', 'n.c.', '-',
      'Chef de projet MOE côté SIRH ; télétravail non précisé.',
      FW + '/fr/tech-it/job-mission/administrateur-applicatif-erp-crm-sirh/chef-de-projet-moe-sirh-h-f-1',
      CV_SIRH_FR, '12/08/2026'),

    o('⭐⭐⭐', 'Consultant SAP SuccessFactors CoreHR (H/F)', 'HR Path',
      'free-work.com', 'Freelance', 'Paris', 'n.p.', '450 - 600 €/j', '3 mois',
      'Cœur de compétence SuccessFactors ; le poste CDI HR Path de la même '
      'relance affiche, lui, du télétravail.',
      FW + '/fr/tech-it/job-mission/consultant-erp-ms-dynamics-oracle-sage-sap/consultant-sap-successfactors-corehr-h-f',
      CV_SIRH_FR, '10/08/2026'),

    o('⭐⭐', 'Project Manager SIRH', 'DSI group', 'free-work.com', 'Freelance',
      'Luxembourg', 'n.p.', 'n.c.', '5 mois',
      'Mission luxembourgeoise, mobilité à clarifier.',
      FW + '/fr/tech-it/job-mission/administrateur-applicatif-erp-crm-sirh/project-manager-sirh-2',
      CV_SIRH_FR, '11/08/2026'),

    o('⭐⭐', 'Gestionnaire d\'Application SIRH', 'Montreal Associates',
      'free-work.com', 'Freelance', 'Bretagne', 'n.p.', '400 - 600 €/j',
      '6 mois',
      'Gestion applicative plus que pilotage de projet ; télétravail non '
      'précisé.',
      FW + '/fr/tech-it/job-mission/administrateur-applicatif-erp-crm-sirh/gestionnaire-dapplication-sirh',
      CV_SIRH_FR, '05/08/2026'),

    o('⭐⭐⭐', 'Consultant IA Générative / Claude (Anthropic)', 'SMARTPOINT',
      'free-work.com', 'Freelance', 'Île-de-France', 'Partiel',
      '500 - 600 €/j', '12 mois',
      'Sujet idéal sur le papier (Claude, acculturation métier) mais '
      'télétravail partiel confirmé sur la fiche, et Python plus RAG exigés.',
      FW + '/fr/tech-it/job-mission/consultant/consultant-ia-generative-claude-anthropic',
      CV_IA, '17/08/2026'),

    o('⭐⭐', 'Expert IA générative et Plateforme IA H/F', 'Freelance.com',
      'free-work.com', 'Freelance', 'Île-de-France', 'Partiel',
      '510 - 590 €/j', '1 an',
      'Adoption utilisateurs d\'une plateforme IA bancaire ; télétravail '
      'partiel vérifié sur la fiche, socle technique LLM/RAG exigé.',
      FW + '/fr/tech-it/job-mission/expert-seo-consultant-referencement/expert-ia-generative-et-plateforme-ia-h-f',
      CV_IA, '14/08/2026'),

    o('⭐⭐', 'Chef de Projet IA agentique, gouvernance et archi Data',
      'ARDEMIS PARTNERS', 'free-work.com', 'Freelance', 'Paris', 'n.p.',
      '400 - 500 €/j', '6 mois',
      'Pilotage de programme IA ; gouvernance et architecture data au '
      'programme, télétravail non précisé.',
      FW + '/fr/tech-it/job-mission/chef-de-projet-ia-agentique-gouvernance-et-archi-data',
      CV_IA, '18/08/2026'),

    o('⭐⭐', 'Product Owner Solutions IA H/F', 'DAVRICOURT', 'free-work.com',
      'CDI', 'Lille', 'n.p.', '45 000 - 50 000 €/an', '-',
      'Product Owner sur des solutions IA ; salaire nettement sous la cible '
      'et télétravail non précisé.',
      FW + '/fr/tech-it/job-mission/product-owner/product-owner-solutions-ia-h-f-6',
      CV_PM_FR, '17/08/2026'),

    # ── LinkedIn : formateurs IA et SIRH (radar, télétravail non confirmé) ───
    o('⭐⭐⭐', 'Consultant Formateur IA Agentique', 'Scaltify',
      'LinkedIn', 'CDI', 'Paris', 'n.p.', 'n.c.', '-',
      'Formation à l\'IA agentique en entreprise, exactement la cible '
      'formateur IA ; télétravail non précisé sur l\'annonce.',
      'https://fr.linkedin.com/jobs/view/consultant-formateur-ia-agentique-at-scaltify-4445952904',
      CV_IA),

    o('⭐⭐⭐', 'OpenAI Master Trainer (H/F)', 'nonplusultra', 'LinkedIn',
      'CDI', 'Paris', 'n.p.', 'n.c.', '-',
      'Formation d\'entreprises aux outils OpenAI ; poste parisien, '
      'télétravail à clarifier.',
      'https://fr.linkedin.com/jobs/formateur-intelligence-artificielle-emplois-france',
      CV_IA),

    o('⭐⭐⭐', 'Global HRIS Europe & Core HR Lead', 'Nexans', 'LinkedIn',
      'CDI', 'Puteaux', 'n.p.', 'n.c.', '-',
      'Pilotage SIRH Europe et Core HR chez un industriel mondial ; profil '
      'très proche du parcours L\'Oréal, télétravail non précisé.',
      'https://fr.linkedin.com/jobs/hris-emplois',
      CV_SIRH_FR),

    o('⭐⭐', 'Consultant in Talent Management / HRIS', 'mc2i', 'LinkedIn',
      'CDI', 'Paris', 'n.p.', 'n.c.', '-',
      'Cabinet de conseil SIRH parisien ; annonce publiée le jour même de la '
      'relance, télétravail non précisé.',
      'https://fr.linkedin.com/jobs/hris-emplois',
      CV_SIRH_FR),

    o('⭐⭐', 'Global HRIS Specialist', 'Back Market', 'LinkedIn', 'CDI',
      'Paris / Bordeaux', 'n.p.', 'n.c.', '-',
      'Scale-up française, poste ouvert aussi à Bordeaux ; télétravail non '
      'précisé.',
      'https://fr.linkedin.com/jobs/hris-emplois',
      CV_SIRH_FR),

    # ── Autres éditeurs, télétravail non confirmé ────────────────────────────
    o('⭐⭐⭐', 'Principal Solution Advisor, HCM - F/M', 'SAP', 'jobs.sap.com',
      'CDI', 'Levallois-Perret', 'n.p.', 'n.c.', '-',
      'Avant-vente HCM chez SAP, le poste le plus aligné du marché français ; '
      'aucune mention de télétravail dans l\'annonce.',
      'https://jobs.sap.com/go/SAP-Jobs-in-France/850401/',
      CV_SIRH_FR),

    o('⭐⭐', 'Manager, Solutions Consultants, France', 'Notion', 'API Ashby',
      'CDI', 'Paris', 'n.p.', 'n.c.', '-',
      'Encadrement d\'une équipe avant-vente chez Notion ; poste rattaché au '
      'bureau parisien, sans mention de remote.',
      'https://jobs.ashbyhq.com/notion/77af0faa-8f69-4dc5-baa6-6e253823bccb',
      CV_CONSTR),

    o('⭐⭐', 'Customer Enablement Manager (Paris, France)', 'Figma',
      'API Greenhouse', 'CDI', 'Paris', 'n.p.', 'n.c.', '-',
      'Enablement client chez Figma ; poste parisien sans mention de '
      'télétravail.',
      'https://boards.greenhouse.io/figma/jobs/5976498004',
      CV_CONSTR),

    o('⭐⭐', 'Principal Transformation Consultant (f/m/d)', 'Valiantys',
      'Lever', 'CDI', 'Remote Allemagne', 'Full remote', 'n.c.', '-',
      'Conseil en transformation chez un partenaire Atlassian ; la variante '
      'France est en hybride Paris, seule celle-ci est en remote.',
      'https://jobs.lever.co/valiantys/53fcffba-4ef7-46e0-907f-d37c4a4bb9c0',
      CV_CONSTR),
]

if __name__ == '__main__':
    add_offre.ajouter_offres(OFFRES)
