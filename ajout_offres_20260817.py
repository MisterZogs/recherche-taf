"""Relance exhaustive du 17/08/2026.

Sources couvertes : free-work (/jobs/sirh pages 1-3, /jobs/sap-hcm, /jobs/ia,
/jobs/ia-generative, /jobs/product-owner, /jobs/product-manager), LinkedIn
pages categories (HRIS, CSM France, consultant SIRH, SuccessFactors Paris),
API Ashby (constructor, elevenlabs, n8n, ashby, notabene, linear, vanta, tilla,
sift, delinea, mural, easygenerator, pylon, upflow, deel, owkin, hackerone),
API Lever (qonto, aircall, vendavo, remofirst, jobgether, pennylane...),
Greenhouse via WebSearch, eursap, mission-freelances, welcometothejungle,
jobs.sap.com, jobs.hr-path.com, careers.hostaway.com, workingnomads,
remoterocketship, upwork.

Ecartes apres verification de lien (annonce fermee ou introuvable) :
- Veeam Technical Account Manager France : plus aucun TAM France dans les 225
  postes ouverts de careers.veeam.com, le resultat moteur etait perime.
- Semrush Manager Customer Onboarding EMEA + Onboarding Consultant French
  Speaking EMEA : les URL JR100237 / JR100424 redirigent vers le listing, donc
  postes fermes (meme piege que himalayas.app).
- Hostaway Senior PM AI / Payments / Communications : 404, seuls les deux
  Staff PM restent ouverts.
- Jobgether Customer Success Manager (m/f/d) cybersecurite : lien Lever en 404.
- ClickUp Solutions Engineer EMEA French Speaking : base Dublin, remote limite
  a l'Irlande et au Royaume-Uni.
- EBSCO Senior Solutions Consultant French speaking : aucune URL directe
  trouvee, seulement des agregateurs.
"""

import openpyxl

import add_offre

add_offre.COLS = add_offre.COLS + ['Date trouvée', 'Date publiée']

D = '17/08/2026'
FW = 'https://www.free-work.com'
CV_SIRH_FR = 'Resume_GaetanFRANCOIS_SIRH.pdf'
CV_SIRH_EN = 'Resume_GaetanFRANCOIS_SIRH_EN.pdf'
CV_CSM_EN = 'CV_GaetanFRANCOIS_CSM_EN.pdf'
CV_CSM_FR = 'CV_GaetanFRANCOIS_CSM_FR.pdf'
CV_PM_EN = 'Resume_GaetanFRANCOIS_PM_EN.pdf'
CV_PM_FR = 'Resume_GaetanFRANCOIS_PM_FR.pdf'
CV_PM_PLAT = 'Resume_GaetanFRANCOIS_PM_Platform_EN.pdf'
CV_IA = 'Resume_GaetanFRANCOIS_IA.pdf'

OFFRES = [

    # ══════════════════ PRODUIT — remote confirme ══════════════════
    {
        'Priorité': '⭐⭐⭐⭐⭐', 'Poste': 'Product Manager: Customer Onboarding Experience',
        'Entreprise': 'Constructor', 'Source': 'jobs.ashbyhq.com (API Ashby)',
        'Contrat': 'CDI', 'Localisation': 'Remote', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Poste produit centre sur l'onboarding client : exactement l'intersection la plus credible entre 15 ans de deploiement client et le role de Product Manager chez WallOfTraders.com. Constructor connait deja le profil (candidature CSM EMEA en cours). Verifie ouvert par l'API Ashby le 17/08.",
        'Lien': 'https://jobs.ashbyhq.com/constructor/e8fa6194-ef2e-47d3-ab45-a9112d87da24',
        'CV à envoyer': CV_PM_EN, 'Prétention': '90-110 K€',
        'Date trouvée': D, 'Date publiée': '23/06/2026',
    },
    {
        'Priorité': '⭐⭐⭐⭐', 'Poste': 'Senior Product Manager: Recall',
        'Entreprise': 'Constructor', 'Source': 'jobs.ashbyhq.com (API Ashby)',
        'Contrat': 'CDI', 'Localisation': 'Remote EMEA', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Produit plateforme de recherche e-commerce, horaires EMEA. Composante technique forte ; envoyer la variante plateforme du CV produit.",
        'Lien': 'https://jobs.ashbyhq.com/constructor/7bc86d05-145d-4b7c-aa6e-b0b207d46117',
        'CV à envoyer': CV_PM_PLAT, 'Prétention': '90-110 K€',
        'Date trouvée': D, 'Date publiée': '28/07/2026',
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Senior Product Manager - Merchant Intelligence and Analytics',
        'Entreprise': 'Constructor', 'Source': 'jobs.ashbyhq.com (API Ashby)',
        'Contrat': 'CDI', 'Localisation': 'Remote', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Analytics marchand : plus data que les deux autres postes Constructor, mais meme employeur full remote et meme process.",
        'Lien': 'https://jobs.ashbyhq.com/constructor/e7426b59-431b-418b-a501-dde7f13b21bf',
        'CV à envoyer': CV_PM_PLAT, 'Prétention': '90-110 K€',
        'Date trouvée': D, 'Date publiée': '01/06/2026',
    },
    {
        'Priorité': '⭐⭐⭐⭐', 'Poste': 'Staff Product Manager - Mobile - 100% Remote - EMEA',
        'Entreprise': 'Hostaway', 'Source': 'careers.hostaway.com',
        'Contrat': 'CDI', 'Localisation': 'Remote EMEA', 'Remote': '100% remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Plateforme SaaS de gestion locative, entierement remote sur l'EMEA. Le niveau Staff vise un profil produit senior ; le parcours WallOfTraders.com plus la dimension client grands comptes tiennent la comparaison. Lien verifie ouvert le 17/08.",
        'Lien': 'https://careers.hostaway.com/o/staff-product-manager-mobile-100-remote-emea',
        'CV à envoyer': CV_PM_EN, 'Prétention': '90-110 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Product Manager (Europe)',
        'Entreprise': 'Linear', 'Source': 'jobs.ashbyhq.com (API Ashby)',
        'Contrat': 'CDI', 'Localisation': 'Europe', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Linear recrute un PM sur l'Europe en full remote. Produit tres oriente equipes de developpement ; c'est la lacune a concede honnetement en lettre de motivation.",
        'Lien': 'https://jobs.ashbyhq.com/linear/86abcce0-04b2-405c-9a8e-e0ca84813914',
        'CV à envoyer': CV_PM_PLAT, 'Prétention': '90-110 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Senior Product Manager - Core Platform (Remote Europe)',
        'Entreprise': 'n8n', 'Source': 'jobs.ashbyhq.com (API Ashby)',
        'Contrat': 'CDI', 'Localisation': 'Berlin / Remote', 'Remote': 'Remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Poste plateforme chez n8n, deja cible sur l'axe CSM. Profil produit technique attendu ; la variante plateforme du CV est la seule qui tienne.",
        'Lien': 'https://jobs.ashbyhq.com/n8n/d418f8fb-b2f2-405e-8f22-db73dcf4e8b4',
        'CV à envoyer': CV_PM_PLAT, 'Prétention': '90-110 K€',
        'Date trouvée': D, 'Date publiée': None,
    },

    # ══════════════════ IA ══════════════════
    {
        'Priorité': '⭐⭐⭐⭐', 'Poste': 'Formateur(trice) en ligne - Intelligence artificielle et développement web',
        'Entreprise': 'n.c. (via mission-freelances.fr)', 'Source': 'mission-freelances.fr',
        'Contrat': 'Freelance', 'Localisation': 'Télétravail', 'Remote': '100% remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Mission de formation IA entierement en ligne, publiee il y a deux jours. La partie developpement web est a clarifier ; le volet IA generative correspond a l'usage quotidien et a la pratique de formation.",
        'Lien': 'https://www.mission-freelances.fr/missions/formateur-trice-en-ligne-intelligence-artificielle-et-developpement-web-teletravail-de3cf7d0/',
        'CV à envoyer': CV_IA, 'Prétention': '600-750 €/j',
        'Date trouvée': D, 'Date publiée': '15/08/2026',
    },
    {
        'Priorité': '⭐⭐⭐⭐', 'Poste': 'Staff Product Manager - AI - 100% Remote - EMEA',
        'Entreprise': 'Hostaway', 'Source': 'careers.hostaway.com',
        'Contrat': 'CDI', 'Localisation': 'Remote EMEA', 'Remote': '100% remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Poste produit sur les fonctions IA de la plateforme : croisement direct entre la cible Product Manager et la cible IA. Full remote EMEA, lien verifie ouvert le 17/08.",
        'Lien': 'https://careers.hostaway.com/o/staff-product-manager-ai-remote-emea',
        'CV à envoyer': CV_PM_EN, 'Prétention': '90-110 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'AI Product Manager (Remote Europe)',
        'Entreprise': 'n8n', 'Source': 'jobs.ashbyhq.com (API Ashby)',
        'Contrat': 'CDI', 'Localisation': 'Berlin / Remote', 'Remote': 'Remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Produit IA chez n8n, remote autorise depuis l'Europe. Meme employeur que plusieurs postes CSM deja suivis.",
        'Lien': 'https://jobs.ashbyhq.com/n8n/42e72645-d99a-4545-97b7-53ba3a699893',
        'CV à envoyer': CV_PM_EN, 'Prétention': '90-110 K€',
        'Date trouvée': D, 'Date publiée': None,
    },

    # ══════════════════ CSM / avant-vente — remote confirme ══════════════════
    {
        'Priorité': '⭐⭐⭐⭐', 'Poste': 'Senior Customer Success Manager (Remote) ES/FR/EN',
        'Entreprise': 'Urbantz', 'Source': 'urbantz.breezy.hr',
        'Contrat': 'CDI', 'Localisation': 'Remote Europe (siège Bruxelles)', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Plateforme de livraison dernier kilometre pour grands comptes retail et logistique. Portefeuille enterprise, plans de succes et QBR : c'est le coeur du metier exerce chez L'Oreal. Trilingue FR/ES/EN demande, l'espagnol intermediaire suffit a l'ecrit. Lien editeur verifie, pas d'agregateur.",
        'Lien': 'https://urbantz.breezy.hr/p/bde2c8af2adc-senior-customer-success-manager-remote-es-fr-en',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '80-95 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Customer Success Manager EMEA',
        'Entreprise': 'Notabene', 'Source': 'jobs.ashbyhq.com (API Ashby)',
        'Contrat': 'CDI', 'Localisation': 'Londres / Remote', 'Remote': 'Remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Conformite crypto ; le passe WallOfTraders.com donne une vraie familiarite avec l'univers. Un poste Senior CSM Notabene est deja suivi, celui-ci porte sur l'EMEA.",
        'Lien': 'https://jobs.ashbyhq.com/notabene/bb86674c-5864-4733-9d37-b585466ebb8b',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '80-95 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Customer Success Lead - Western Europe',
        'Entreprise': 'ElevenLabs', 'Source': 'jobs.ashbyhq.com (API Ashby)',
        'Contrat': 'CDI', 'Localisation': 'Europe de l\'Ouest', 'Remote': 'Remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Poste d'encadrement sur l'Europe de l'Ouest, un cran au-dessus du poste Scaled deja suivi chez le meme editeur. La France entre dans le perimetre.",
        'Lien': 'https://jobs.ashbyhq.com/elevenlabs/0dbfbe3e-7218-4045-ba78-28b0d2e5ab6d',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '85-100 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Customer Success - Southern Europe',
        'Entreprise': 'ElevenLabs', 'Source': 'jobs.ashbyhq.com (API Ashby)',
        'Contrat': 'CDI', 'Localisation': 'Europe du Sud', 'Remote': 'Remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Perimetre Europe du Sud, France incluse. Annonce rattachee a l'Espagne mais ouverte en remote.",
        'Lien': 'https://jobs.ashbyhq.com/elevenlabs/78c564eb-ee87-46d9-b2fd-4322a223a547',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '80-95 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Technical Programs Manager - Scaled Customer Success (Remote Europe)',
        'Entreprise': 'n8n', 'Source': 'jobs.ashbyhq.com (API Ashby)',
        'Contrat': 'CDI', 'Localisation': 'Remote Europe', 'Remote': 'Remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Industrialisation du succes client a grande echelle : programme, outillage et process plutot que portefeuille. Croise le pilotage de programme SIRH et la composante technique.",
        'Lien': 'https://jobs.ashbyhq.com/n8n/d550716c-8cb9-4efe-9a52-b4cd67e193e1',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '85-100 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Customer Success Manager - EMEA',
        'Entreprise': 'Tilla', 'Source': 'jobs.ashbyhq.com (API Ashby)',
        'Contrat': 'CDI', 'Localisation': 'Remote EMEA', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Petite structure, poste EMEA full remote. Annonce de mai encore ouverte a l'API le 17/08.",
        'Lien': 'https://jobs.ashbyhq.com/tilla/823e58d1-e986-42d9-9441-47f31bb77a52',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '75-90 K€',
        'Date trouvée': D, 'Date publiée': '21/05/2026',
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Customer Success Manager (French speaking)',
        'Entreprise': 'Go1 Europe', 'Source': 'job-boards.greenhouse.io',
        'Contrat': 'CDI', 'Localisation': 'Europe', 'Remote': 'Remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Plateforme de formation en entreprise, editeur remote-first. Le marche francais et le lien avec la formation croisent les deux axes CSM et IA/formation. Lien Greenhouse verifie actif.",
        'Lien': 'https://job-boards.greenhouse.io/go1eu/jobs/4635904005',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '80-95 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Solutions Engineer, Europe',
        'Entreprise': 'Linear', 'Source': 'jobs.ashbyhq.com (API Ashby)',
        'Contrat': 'CDI', 'Localisation': 'Londres / Europe', 'Remote': 'Remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Avant-vente technique, axe ajoute le 14/08. L'appel d'offres d'infogerance L'Oreal gagne chez ALTI-TCS est la reference a mettre en avant.",
        'Lien': 'https://jobs.ashbyhq.com/linear/d37b3d76-3080-47f9-8a19-60505573112c',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '85-100 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Manager, Solutions Engineering - EMEA',
        'Entreprise': 'Vanta', 'Source': 'jobs.ashbyhq.com (API Ashby)',
        'Contrat': 'CDI', 'Localisation': 'Londres', 'Remote': 'Remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Encadrement d'une equipe d'avant-vente EMEA. Vanta a deja une candidature CSM marche francais en cours. Base Londres, question visa a clarifier.",
        'Lien': 'https://jobs.ashbyhq.com/vanta/2daebe8c-69af-44f3-a81f-38fb17da30a0',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '95-115 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Enterprise Customer Success Manager - UK, Remote Contract',
        'Entreprise': 'HeyGen', 'Source': 'job-boards.greenhouse.io',
        'Contrat': 'Freelance / contrat', 'Localisation': 'Royaume-Uni', 'Remote': 'Remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Portefeuille enterprise EMEA avec focus sur les clients francophones, en contrat plutot qu'en CDI. Editeur video IA. Contrat britannique : statut et fiscalite a clarifier.",
        'Lien': 'https://job-boards.greenhouse.io/heygen/jobs/5198172007',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '600-750 €/j',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Customer Success Manager (Remote)',
        'Entreprise': 'Sorcero', 'Source': 'job-boards.greenhouse.io',
        'Contrat': 'CDI', 'Localisation': 'Remote', 'Remote': 'Remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "IA appliquee aux sciences de la vie. Annonce remote sans zone precisee ; verifier l'eligibilite depuis la France avant de postuler.",
        'Lien': 'https://job-boards.greenhouse.io/sorcero/jobs/5982234004',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '80-95 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Customer Success Manager (Remote, UK)',
        'Entreprise': 'Easygenerator', 'Source': 'jobs.ashbyhq.com (API Ashby)',
        'Contrat': 'CDI', 'Localisation': 'Royaume-Uni', 'Remote': 'Remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Editeur d'outil auteur e-learning. Poste rattache au Royaume-Uni ; interet surtout si la zone s'ouvre a l'Europe continentale.",
        'Lien': 'https://jobs.ashbyhq.com/easygenerator/10b80b2e-c506-488a-a15f-39d962072d4f',
        'CV à envoyer': CV_CSM_EN, 'Prétention': '75-90 K€',
        'Date trouvée': D, 'Date publiée': '04/08/2026',
    },

    # ══════════════════ Implementation / Professional Services — remote confirme ══════════════════
    {
        'Priorité': '⭐⭐⭐⭐', 'Poste': 'Manager of Dedicated Implementations - EMEA',
        'Entreprise': 'Ashby', 'Source': 'jobs.ashbyhq.com (API Ashby)',
        'Contrat': 'CDI', 'Localisation': 'Remote Union européenne', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Encadrement d'une equipe de deploiement client sur l'EMEA, chez un editeur d'ATS. Quinze ans de deploiement SIRH multi-pays plus l'encadrement d'equipe : c'est le poste le plus proche du parcours reel dans cette relance. Full remote depuis l'Union europeenne.",
        'Lien': 'https://jobs.ashbyhq.com/ashby/35a01a05-8efd-4bc3-a4bf-0a31d902102d',
        'CV à envoyer': CV_SIRH_EN, 'Prétention': '90-110 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Professional Services Consultant',
        'Entreprise': 'Sift', 'Source': 'jobs.ashbyhq.com (API Ashby)',
        'Contrat': 'CDI', 'Localisation': 'Remote', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Deploiement client chez un editeur de lutte contre la fraude. Sift a deja un poste CSM EMEA suivi. Zone remote a confirmer.",
        'Lien': 'https://jobs.ashbyhq.com/sift/bfd58e03-9ff6-4843-9560-3352fcda8e19',
        'CV à envoyer': CV_SIRH_EN, 'Prétention': '80-95 K€',
        'Date trouvée': D, 'Date publiée': '16/06/2026',
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Senior Product Manager, Integrations (Remote EMEA)',
        'Entreprise': 'Remote.com', 'Source': 'job-boards.greenhouse.io',
        'Contrat': 'CDI', 'Localisation': 'Remote EMEA', 'Remote': 'Full remote',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Produit d'integrations sur une plateforme RH mondiale : croise le produit, l'integration systeme et le SIRH. Remote.com est full remote par construction et plusieurs postes y sont deja suivis. Le volet ecosysteme partenaires et API est la zone a travailler.",
        'Lien': 'https://job-boards.greenhouse.io/remotecom/jobs/7599380003',
        'CV à envoyer': CV_PM_PLAT, 'Prétention': '90-110 K€',
        'Date trouvée': D, 'Date publiée': None,
    },

    # ══════════════════ SIRH / SAP France — telepresence partielle, ira en NoRemote ══════════════════
    {
        'Priorité': '⭐⭐⭐⭐', 'Poste': 'Consultant IA Générative / Claude (Anthropic)',
        'Entreprise': 'SMARTPOINT', 'Source': 'free-work.com',
        'Contrat': 'Freelance / CDI', 'Localisation': 'Île-de-France', 'Remote': 'Partiel',
        'Salaire / TJM': '500-600 €/j', 'Durée mission': '12 mois',
        'Fit / Notes': "Cas d'usage Claude en entreprise, conception de prompts, gouvernance IA : le contenu correspond a l'usage quotidien des outils IA. La partie Python, RAG et LangChain depasse le perimetre non-technique vise. Teletravail partiel seulement, d'ou le classement NoRemote.",
        'Lien': FW + '/fr/tech-it/job-mission/consultant/consultant-ia-generative-claude-anthropic',
        'CV à envoyer': CV_IA, 'Prétention': '600-700 €/j',
        'Date trouvée': D, 'Date publiée': '17/08/2026',
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Expert IA générative et Plateforme IA H/F',
        'Entreprise': 'Freelance.com', 'Source': 'free-work.com',
        'Contrat': 'Freelance', 'Localisation': 'Île-de-France', 'Remote': 'Partiel',
        'Salaire / TJM': '510-590 €/j', 'Durée mission': '1 an renouvelable',
        'Fit / Notes': "Accompagnement des usages IA et animation d'une plateforme interne : la moitie du poste est de l'acculturation. L'autre moitie demande du scripting Python et des connecteurs MCP.",
        'Lien': FW + '/fr/tech-it/job-mission/expert-seo-consultant-referencement/expert-ia-generative-et-plateforme-ia-h-f',
        'CV à envoyer': CV_IA, 'Prétention': '600-700 €/j',
        'Date trouvée': D, 'Date publiée': '14/08/2026',
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Manager SIRH',
        'Entreprise': 'HR DNA', 'Source': 'free-work.com',
        'Contrat': 'CDI', 'Localisation': 'Paris', 'Remote': 'Partiel',
        'Salaire / TJM': '60-110 K€', 'Durée mission': None,
        'Fit / Notes': "Poste de developpement commercial et de structuration d'offre SIRH en cabinet, plus de 10 ans d'experience demandes. Fourchette haute interessante ; la dimension prospection commerciale est nouvelle.",
        'Lien': FW + '/fr/tech-it/job-mission/administrateur-applicatif-erp-crm-sirh/manager-sirh-11',
        'CV à envoyer': CV_SIRH_FR, 'Prétention': '90-110 K€',
        'Date trouvée': D, 'Date publiée': '12/08/2026',
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Chef de projet IT / Responsable SIRH (H/F)',
        'Entreprise': 'LeHibou', 'Source': 'free-work.com',
        'Contrat': 'Freelance', 'Localisation': 'Bordeaux', 'Remote': 'Partiel (2j/sem)',
        'Salaire / TJM': '675 €/j', 'Durée mission': '9 mois',
        'Fit / Notes': "Deploiement d'une solution Paie jusqu'au go-live de janvier 2027 plus gouvernance du portefeuille SIRH : correspondance directe avec OnePayroll. Bordeaux est a deux heures d'Anglet. Deux jours de teletravail seulement.",
        'Lien': FW + '/fr/tech-it/job-mission/administrateur-applicatif-erp-crm-sirh/chef-de-projet-it-responsable-sirh-h-f',
        'CV à envoyer': CV_SIRH_FR, 'Prétention': '675 €/j',
        'Date trouvée': D, 'Date publiée': '13/08/2026',
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Consultant SAP SuccessFactors CoreHR (H/F)',
        'Entreprise': 'HR Path', 'Source': 'free-work.com',
        'Contrat': 'Freelance', 'Localisation': 'Paris', 'Remote': 'Partiel',
        'Salaire / TJM': '450-600 €/j', 'Durée mission': '3 mois',
        'Fit / Notes': "Employee Central, module central du parcours L'Oreal. HR Path est deja en contact sur un autre poste SuccessFactors.",
        'Lien': FW + '/fr/tech-it/job-mission/consultant-erp-ms-dynamics-oracle-sage-sap/consultant-sap-successfactors-corehr-h-f',
        'CV à envoyer': CV_SIRH_FR, 'Prétention': '650-750 €/j',
        'Date trouvée': D, 'Date publiée': '10/08/2026',
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Expert SAP SuccessFactors',
        'Entreprise': 'LeHibou', 'Source': 'free-work.com',
        'Contrat': 'Freelance', 'Localisation': 'Saint-Ouen-sur-Seine', 'Remote': 'Partiel',
        'Salaire / TJM': '575 €/j', 'Durée mission': '6 mois',
        'Fit / Notes': "Mission d'expertise SuccessFactors en Ile-de-France. TJM sous les fourchettes cibles, ce qui ne disqualifie pas l'offre.",
        'Lien': FW + '/fr/tech-it/job-mission/consultant-erp-ms-dynamics-oracle-sage-sap/expert-sap-successfactors-1',
        'CV à envoyer': CV_SIRH_FR, 'Prétention': '650-750 €/j',
        'Date trouvée': D, 'Date publiée': '05/08/2026',
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'SAP SuccessFactors Consultant - Europe',
        'Entreprise': 'HR Path', 'Source': 'jobs.hr-path.com',
        'Contrat': 'CDI', 'Localisation': 'Paris La Défense', 'Remote': 'Non précisé',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Poste SuccessFactors a perimetre europeen chez le principal cabinet SIRH francais. Anglais courant et deploiements multi-pays sont le coeur du parcours.",
        'Lien': 'https://jobs.hr-path.com/job/Paris-La-D%C3%A9fense-Cedex-SAP-SuccessFactors-Consultant-Europe-75-92042/1057307701/',
        'CV à envoyer': CV_SIRH_EN, 'Prétention': '75-90 K€',
        'Date trouvée': D, 'Date publiée': '12/08/2026',
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Solution Architect SuccessFactors (H/F)',
        'Entreprise': 'HR Path', 'Source': 'jobs.hr-path.com',
        'Contrat': 'CDI', 'Localisation': 'Paris La Défense', 'Remote': 'Non précisé',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Architecture de solution SuccessFactors : niveau au-dessus du consultant, coherent avec quatorze ans de SAP HR.",
        'Lien': 'https://jobs.hr-path.com/job/Paris-La-D%C3%A9fense-Cedex-Solution-Architect-SuccessFactors-%28HF%29-75-92042/1079264001/',
        'CV à envoyer': CV_SIRH_FR, 'Prétention': '85-100 K€',
        'Date trouvée': D, 'Date publiée': '12/08/2026',
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Consultant SIRH Paie HR Access - Paris La Défense (H/F)',
        'Entreprise': 'HR Path', 'Source': 'jobs.hr-path.com',
        'Contrat': 'CDI', 'Localisation': 'Paris La Défense', 'Remote': 'Non précisé',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "HR Access plutot que SAP ; la logique paie et le pilotage de projet restent transposables.",
        'Lien': 'https://jobs.hr-path.com/job/Paris-La-D%C3%A9fense-Cedex-Consultant-SIRH-Paie-HR-Access-Paris-La-D%C3%A9fense-%28HF%29-75-92042/888056701/',
        'CV à envoyer': CV_SIRH_FR, 'Prétention': '70-85 K€',
        'Date trouvée': D, 'Date publiée': '16/08/2026',
    },
    {
        'Priorité': '⭐⭐⭐', 'Poste': 'Chargé de missions SIRH N2 - Workday HCM (H/F)',
        'Entreprise': 'HR DNA', 'Source': 'free-work.com',
        'Contrat': 'Freelance', 'Localisation': 'Neuilly-sur-Marne', 'Remote': 'Partiel',
        'Salaire / TJM': '250-500 €/j', 'Durée mission': '24 mois',
        'Fit / Notes': "Ateliers, specifications fonctionnelles, formation des utilisateurs et anomalies de niveau 2 : le quotidien exerce chez L'Oreal, mais sur Workday. Mission longue de 24 mois.",
        'Lien': FW + '/fr/tech-it/job-mission/administrateur-applicatif-erp-crm-sirh/charge-de-missions-sirh-n2-workday-hcm-h-f-25',
        'CV à envoyer': CV_SIRH_FR, 'Prétention': '500 €/j',
        'Date trouvée': D, 'Date publiée': '16/08/2026',
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Responsable applicatif SIRH (H/F) - Freelance',
        'Entreprise': 'Groupe Artemys', 'Source': 'free-work.com',
        'Contrat': 'Freelance', 'Localisation': 'Paris 15e', 'Remote': 'Partiel (2j/sem)',
        'Salaire / TJM': '550-650 €/j', 'Durée mission': '6 mois',
        'Fit / Notes': "Pilotage applicatif oriente maintien en condition operationnelle, avec analyse d'anomalies d'interfaces et reprise de fichiers : proche du travail de migration de donnees.",
        'Lien': FW + '/fr/tech-it/job-mission/administrateur-applicatif-erp-crm-sirh/responsable-applicatif-sirh-h-f-freelance',
        'CV à envoyer': CV_SIRH_FR, 'Prétention': '650 €/j',
        'Date trouvée': D, 'Date publiée': '14/08/2026',
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Consultant AMOA Workday HCM (H/F)',
        'Entreprise': 'HR Path', 'Source': 'free-work.com',
        'Contrat': 'Freelance', 'Localisation': 'Lyon', 'Remote': 'Partiel',
        'Salaire / TJM': '550-600 €/j', 'Durée mission': '3 mois',
        'Fit / Notes': "AMOA sur Workday : l'axe MOA correspond, l'outil differe de SAP.",
        'Lien': FW + '/fr/tech-it/job-mission/consultant-moa-amoa/consultant-amoa-workday-hcm-h-f',
        'CV à envoyer': CV_SIRH_FR, 'Prétention': '600 €/j',
        'Date trouvée': D, 'Date publiée': '10/08/2026',
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Chef de projet MOE SIRH H/F',
        'Entreprise': 'HAYS France', 'Source': 'free-work.com',
        'Contrat': 'CDI', 'Localisation': 'Paris', 'Remote': 'Non précisé',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "MOE sur HR Access V9 et Cegid Talentsoft, avec formation et accompagnement au changement. Le COBOL demande en option sort du perimetre.",
        'Lien': FW + '/fr/tech-it/job-mission/administrateur-applicatif-erp-crm-sirh/chef-de-projet-moe-sirh-h-f-1',
        'CV à envoyer': CV_SIRH_FR, 'Prétention': '70-85 K€',
        'Date trouvée': D, 'Date publiée': '12/08/2026',
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Project Manager SIRH',
        'Entreprise': 'DSI group', 'Source': 'free-work.com',
        'Contrat': 'Freelance', 'Localisation': 'Luxembourg', 'Remote': 'Non précisé',
        'Salaire / TJM': None, 'Durée mission': '5 mois',
        'Fit / Notes': "Chef de projet SIRH au Luxembourg. Teletravail a clarifier ; sans reponse claire, l'offre reste hors cible.",
        'Lien': FW + '/fr/tech-it/job-mission/administrateur-applicatif-erp-crm-sirh/project-manager-sirh-2',
        'CV à envoyer': CV_SIRH_FR, 'Prétention': '650 €/j',
        'Date trouvée': D, 'Date publiée': '11/08/2026',
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Expert GTA - Horoquartz (H/F)',
        'Entreprise': 'Mindquest', 'Source': 'free-work.com',
        'Contrat': 'Freelance', 'Localisation': 'Aix-en-Provence', 'Remote': 'Non précisé',
        'Salaire / TJM': '480-500 €/j', 'Durée mission': '3 mois',
        'Fit / Notes': "Gestion des temps sur Horoquartz. La GTA fait partie du perimetre SIRH couvert, l'outil est nouveau.",
        'Lien': FW + '/fr/tech-it/job-mission/expert-seo-consultant-referencement/expert-gta-horoquartz-h-f',
        'CV à envoyer': CV_SIRH_FR, 'Prétention': '550 €/j',
        'Date trouvée': D, 'Date publiée': '17/08/2026',
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Business Analyst IA',
        'Entreprise': 'VISIAN', 'Source': 'free-work.com',
        'Contrat': 'Freelance', 'Localisation': 'Paris', 'Remote': 'Non précisé',
        'Salaire / TJM': None, 'Durée mission': '1 an',
        'Fit / Notes': "Analyse fonctionnelle sur des projets IA : croise l'axe MOA et l'axe IA. Publiee le 17/08, teletravail a clarifier.",
        'Lien': FW + '/fr/tech-it/job-mission/business-analyst/business-analyst-ia-18',
        'CV à envoyer': CV_IA, 'Prétention': '550-650 €/j',
        'Date trouvée': D, 'Date publiée': '17/08/2026',
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Chef de Produit Plateforme IA (AI Platform Product Manager)',
        'Entreprise': 'JCW Search Ltd', 'Source': 'free-work.com',
        'Contrat': 'Freelance', 'Localisation': 'Paris', 'Remote': 'Partiel',
        'Salaire / TJM': '610-1110 £/j', 'Durée mission': '12 mois renouvelable',
        'Fit / Notes': "Poste produit sur une plateforme IA, francais et anglais courants exiges, 10 ans d'experience minimum. Le volet LLMOps et data engineering depasse le perimetre. TJM tres eleve.",
        'Lien': FW + '/fr/tech-it/job-mission/responsable-produit/chef-de-produit-plateforme-ia-ai-platform-product-manager',
        'CV à envoyer': CV_PM_PLAT, 'Prétention': '800 €/j',
        'Date trouvée': D, 'Date publiée': '05/08/2026',
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Formateur/Formatrice en intelligence artificielle générative',
        'Entreprise': 'MISTER IA', 'Source': 'welcometothejungle.com',
        'Contrat': 'CDI', 'Localisation': 'Paris', 'Remote': 'Occasionnel',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Animation de formations IA generative en presentiel et a distance, en CDI. Teletravail seulement occasionnel, donc hors cible remote ; a garder si le poste evolue.",
        'Lien': 'https://www.welcometothejungle.com/fr/companies/mister-ia',
        'CV à envoyer': CV_IA, 'Prétention': '55-70 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Formateur·rice IA Générative - Montpellier / Marseille',
        'Entreprise': 'FRANCE IA', 'Source': 'welcometothejungle.com',
        'Contrat': 'Freelance', 'Localisation': 'Montpellier / Marseille', 'Remote': 'Non',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Reseau de formateurs independants qui se lance dans six villes francaises a partir de septembre 2026. Annonce explicitement sans teletravail ; utile surtout comme contact reseau.",
        'Lien': 'https://www.welcometothejungle.com/fr/companies/france-ia-1/jobs/ef858357-57c4-4999-a5ef-e1539a62301b',
        'CV à envoyer': CV_IA, 'Prétention': '600 €/j',
        'Date trouvée': D, 'Date publiée': None,
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Product Owner Solutions IA H/F',
        'Entreprise': 'DAVRICOURT', 'Source': 'free-work.com',
        'Contrat': 'CDI', 'Localisation': 'Lille', 'Remote': 'Non précisé',
        'Salaire / TJM': '45-50 K€', 'Durée mission': None,
        'Fit / Notes': "Product Owner sur des solutions IA. Fourchette salariale nettement sous les cibles et teletravail non precise.",
        'Lien': FW + '/fr/tech-it/job-mission/product-owner/product-owner-solutions-ia-h-f-6',
        'CV à envoyer': CV_PM_FR, 'Prétention': '60-70 K€',
        'Date trouvée': D, 'Date publiée': '17/08/2026',
    },
    {
        'Priorité': '⭐⭐', 'Poste': 'Customer Success Manager - SAP Next Gen - Academy for Customer Success - FRANCE (Hybrid)',
        'Entreprise': 'SAP', 'Source': 'jobs.sap.com',
        'Contrat': 'CDI', 'Localisation': 'Levallois-Perret', 'Remote': 'Hybride',
        'Salaire / TJM': None, 'Durée mission': None,
        'Fit / Notes': "Programme Academy for Customer Success de SAP : croise directement le CSM et quatorze ans de SAP. Poste explicitement hybride, d'ou le classement NoRemote.",
        'Lien': 'https://jobs.sap.com/job/Levallois-Perret-Customer-Success-Manager-SAP-Next-Gen-Academy-for-Customer-Success-FRANCE-%28Hybrid%29-92300/1423455033/',
        'CV à envoyer': CV_CSM_FR, 'Prétention': '85-100 K€',
        'Date trouvée': D, 'Date publiée': None,
    },
]


def _cles_existantes():
    wb = openpyxl.load_workbook(add_offre.FICHIER)
    cles = set()
    for ws in wb.worksheets:
        for row in ws.iter_rows(min_row=2, values_only=True):
            poste, entreprise = row[3], row[4]
            if poste:
                cles.add((str(poste).strip().lower(),
                          str(entreprise or '').strip().lower()))
    return cles


if __name__ == '__main__':
    existantes = _cles_existantes()
    nouvelles, doublons = [], []
    for o in OFFRES:
        cle = (o['Poste'].strip().lower(), str(o.get('Entreprise') or '').strip().lower())
        (doublons if cle in existantes else nouvelles).append(o)

    if doublons:
        print("── Doublons ignorés ──")
        for o in doublons:
            print(f"  = {o['Poste']} | {o['Entreprise']}")

    add_offre.ajouter_offres(nouvelles)
    print(f"\n{len(nouvelles)} offres ajoutées, {len(doublons)} doublons ignorés.")
