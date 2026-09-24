# Cluster Remote/VC EU + niches + cabinets/éditeurs — sources à interroger

Lire d'abord `relance_regles_communes.md`. Fichier de sortie : donné dans la consigne
de lancement (vérifier s'il existe déjà avant de commencer, voir règles communes).

## Sources remote/niches

| Source | Méthode |
|---|---|
| **remoterocketship.com** | Rendement variable (1 à 7 offres selon les relances). Le slug `-worldwide-remote` dans l'URL n'est PAS un signal fiable d'éligibilité internationale (contre-exemple vérifié avec une offre "Germany Remote") — vérifier le `<title>`/meta de chaque fiche individuelle. |
| **remotifyeurope.com** | Comportement intermittent confirmé plusieurs fois : tester plusieurs User-Agent si le premier échoue (UA Safari Mac a fonctionné une fois, combo Windows+Referer Google une autre fois). Peut rendre 0 résultat France un jour et 10 le lendemain. |
| **geojobs.ai** | Board dédié GEO/AI-search, souvent très US-centré, rendement faible mais 1 offre suffit à justifier le passage (poste GEO pur rare ailleurs). |
| **weworkremotely.com** | Passer par les flux RSS par catégorie plutôt que le HTML (souvent 403 en scraping direct). |
| **dribbble.com/jobs** | Fetch direct fonctionne mais sans localisation/remote dans le listing — qualifier fiche par fiche. |
| **careers.atomico.com** | Board Getro. Très variable d'une relance à l'autre (0 à plusieurs dizaines d'offres éligibles) — le paramètre `?q=` fonctionne mieux que `?query=`. Très US/Canada-centré même en remote. |
| **euremotejobs.com** | `curl` avec User-Agent navigateur (jamais WebFetch). Bloqué en 403 par intermittence — si ça échoue, ne pas insister plus de 2-3 tentatives. |
| **welcometothejungle.com** | **Piège `archived_at` très fréquent** : toujours vérifier via `api.welcometothejungle.com/api/v1/organizations/<org>/jobs/<slug>` que `job.archived_at` est `null` avant de retenir une offre. Beaucoup d'offres indexées sont en fait fermées. |
| **n8n** (Ashby `n8n`) | Souvent tout ancré Berlin/US, peu de fit remote-France. |
| **Nebius** (Greenhouse, Amsterdam) | Bon filon régulier, ~380 postes, plusieurs avec France explicite (Customer Engineer EMEA, Solutions Architect EMEA). |
| **Index Ventures / Balderton** (portfolio VC) | WebSearch `site:jobs.indexventures.com "customer success" OR "product manager" remote`, idem `careers.balderton.com`. Rendement généralement faible. |

## Cabinets de conseil et éditeurs HRIS à repasser périodiquement (pas à chaque fois,
1x/mois suffit sauf changement de verdict)

Deloitte, EY, KPMG (`emplois.kpmg.fr`), Wavestone, Sopra Steria, Capgemini, Colombus
Consulting, Forvis Mazars : historiquement rendement nul ou quasi nul (pages JS non
scrapables en fetch direct). ADP, SD Worx (`careers.sdworx.com`, 0 poste
France/worldwide confirmé plusieurs fois), Workday, ServiceNow, Cegid, Lucca, Payfit,
Personio, Silae, 365talents : idem, passage rapide seulement (WebSearch en repli), ne
pas y consacrer plus de 2-3 minutes au total pour tout ce bloc.

## Règle de filtrage remote (hors France)

Toute offre d'une entreprise non basée en France : ne retenir que le remote ouvert à
l'international (Worldwide/Anywhere/EMEA/Europe), jamais le remote local à un seul
pays. Si l'entreprise est basée aux USA ou en Suisse/Pays-Bas avec remote international
confirmé, ajouter `"Onglet": "Offres USA"` ou `"Onglet": "Offres CH-NL"`.
