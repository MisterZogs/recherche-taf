# Récupère les offres LinkedIn via l'API publique guest (curl, sans compte).
# Trier ensuite à la main les titres pertinents ; détail d'une offre : https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/<id>
import re,html,json,time,subprocess,urllib.parse,openpyxl
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36"
KW=["SuccessFactors","SAP HCM","SAP HR","SIRH","HRIS","consultant SIRH","chef de projet SIRH","data migration SAP","Customer Success Manager","Senior Customer Success Manager","Technical Account Manager","Solutions Consultant","Solutions Engineer","Implementation Consultant","Onboarding Manager","Product Manager","Product Owner","Product Designer","UX Designer","SEO Manager","GEO SEO","formateur IA","IA générative consultant","AI enablement","chef de projet","Project Manager SaaS","Engagement Manager","Chief of Staff"]
LOCS=["France","European Union"]
MODES={"2":"Remote","3":"Hybride"}
# liens existants
wb=openpyxl.load_workbook('offres_emploi.xlsx',read_only=True)
ids=set()
for ws in wb:
    rows=list(ws.iter_rows(values_only=True))
    if not rows or 'Lien' not in rows[0]: continue
    li=rows[0].index('Lien')
    for r in rows[1:]:
        m=re.search(r'(\d{8,})',str(r[li] or ''))
        if m and 'linkedin' in str(r[li]): ids.add(m.group(1))
print('ids linkedin déjà connus',len(ids))
seen={};out=[]
for kw in KW:
  for loc in LOCS:
    for wt,mode in MODES.items():
      if mode=="Hybride" and loc!="France": continue
      for start in (0,10,20):
        u=f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={urllib.parse.quote(kw)}&location={urllib.parse.quote(loc)}&f_WT={wt}&f_TPR=r1209600&start={start}"
        s=subprocess.run(["curl","-s","-A",UA,u],capture_output=True,text=True).stdout
        cards=s.split('<li>')[1:]
        for c in cards:
            g=lambda p:(html.unescape(re.sub(r'\s+',' ',re.search(p,c,re.S).group(1))).strip() if re.search(p,c,re.S) else '')
            lk=g(r'href="(https://[^"?]*jobs/view[^"?]*)'); m=re.search(r'(\d{8,})$',lk)
            if not m: continue
            i=m.group(1)
            if i in ids or i in seen: continue
            seen[i]=1
            out.append(dict(id=i,kw=kw,mode=mode,Poste=g(r'base-search-card__title">(.*?)<'),Entreprise=g(r'base-search-card__subtitle">.*?>(.*?)<') or g(r'base-search-card__subtitle">\s*([^<]+)<'),Localisation=g(r'job-search-card__location">(.*?)<'),Date=g(r'datetime="([^"]+)"'),Lien=lk))
        if len(cards)<10: break
        time.sleep(0.4)
print(len(out))
json.dump(out,open('relance_linkedin_brut.json','w'),ensure_ascii=False,indent=1)
