import re,html,json,subprocess,urllib.parse,time
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/124 Safari/537.36"
LOCS=["United Arab Emirates","Saudi Arabia","Qatar","Kuwait","Bahrain","Oman","Portugal","Spain","Poland","Romania","Estonia","Ireland","Belgium","Luxembourg","Netherlands","Greece","Italy","Switzerland","Morocco","Singapore","Canada","Mexico"]
KW=["SuccessFactors","SAP HCM","SIRH","HRIS","Customer Success Manager","Technical Account Manager","Solutions Consultant","Implementation Consultant","Product Manager","Product Owner","Engagement Manager","Data Migration"]
inc=re.compile(r'successfactors|sap (hcm|hr)|\bhcm\b|sirh|hris|people (systems|tech)|hr (tech|information|systems|transformation)|customer success|\bcsm\b|technical account|solutions? (consultant|engineer|architect)|implementation|onboarding|product (manager|owner)|engagement manager|data migration|head of|project manager|programme manager|program manager|delivery manager|chief of staff',re.I)
exc=re.compile(r'stage|intern\b|internship|payroll (specialist|officer|admin)|gestionnaire|developer|software engineer|comptab|recruit|talent acquisition|sales (executive|manager|rep)|account executive|\bbdr\b|\bsdr\b|business developer|junior|graduate|assistant|forklift|driver|nurse|technician|operator|accountant|architect(?!ure)(?! .*solution)',re.I)
seen={};out=[]
for loc in LOCS:
  for kw in KW:
    for start in (0,10):
      u=f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={urllib.parse.quote(kw)}&location={urllib.parse.quote(loc)}&f_WT=2&f_TPR=r1209600&start={start}"
      s=subprocess.run(["curl","-s","-A",UA,u],capture_output=True,text=True).stdout
      cs=s.split('<li>')[1:]
      for c in cs:
        g=lambda p:(html.unescape(re.sub(r'\s+',' ',re.search(p,c,re.S).group(1))).strip() if re.search(p,c,re.S) else '')
        lk=g(r'href="(https://[^"?]*jobs/view[^"?]*)');m=re.search(r'(\d{8,})$',lk)
        if not m or m.group(1) in seen: continue
        t=g(r'base-search-card__title">(.*?)<')
        if not inc.search(t) or exc.search(t): continue
        seen[m.group(1)]=1
        out.append(dict(id=m.group(1),pays=loc,Poste=t,Entreprise=g(r'base-search-card__subtitle">.*?>(.*?)<') or g(r'base-search-card__subtitle">\s*([^<]+)<'),Localisation=g(r'job-search-card__location">(.*?)<'),Date=g(r'datetime="([^"]+)"'),Lien=lk))
      if len(cs)<10: break
      time.sleep(0.3)
  print(loc,len(out),flush=True)
# détails
full=re.compile(r'fully remote|100\s?% remote|remote[- ]first|work(?:ing)? from anywhere|work(?:ing)? remotely|remote (?:position|role|job|opportunity|work)|this is a remote|télétravail (?:complet|total)|full[- ]remote|home[- ]?office|work from home|remote within',re.I)
bad=re.compile(r'must (?:be|reside|live)[^.]{0,40}(?:based|located|resid|living)[^.]{0,30}(?:in|within)|residents? of|right to work in|work (?:permit|authori[sz]ation)[^.]{0,40}(?:required|needed)|eligible to work in|on-?site|in-?office|hybrid|relocat|\d days? (?:a|per|in the) (?:week|office)|US[- ]based|U\.S\. only|must be located',re.I)
lang=re.compile(r'(?:fluent|native|proficien\w+|mother tongue|required|mandatory|courant|erforderlich)[^.]{0,40}(?:german|deutsch|arabic|dutch|italian|spanish|polish|portuguese|greek|french)|(?:german|deutsch|arabic|dutch|italian|polish|greek)[^.]{0,40}(?:fluent|native|required|mandatory)',re.I)
for n,o in enumerate(out):
    s=subprocess.run(["curl","-s","-A",UA,f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{o['id']}"],capture_output=True,text=True).stdout
    m=re.search(r'show-more-less-html__markup[^>]*>(.*?)</div>',s,re.S)
    d=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',m.group(1)))) if m else ''
    o['desc']=d[:5000]
    o['full']=[x.group(0) for x in full.finditer(d)][:3]
    o['bad']=[d[max(0,x.start()-30):x.end()+40] for x in bad.finditer(d)][:3]
    o['lang']=[x.group(0) for x in lang.finditer(d)][:2]
    if n%50==0: print('det',n,flush=True)
    time.sleep(0.25)
json.dump(out,open('intl.json','w'),ensure_ascii=False)
print('FIN',len(out),sum(1 for o in out if o['full']),sum(1 for o in out if o['full'] and not o['bad'] and not o['lang']))
