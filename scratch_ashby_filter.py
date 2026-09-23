import json, re, sys, urllib.request

KEYWORDS = [
    "customer success", "csm", "account manager", "key account", "technical account",
    "solutions engineer", "sales engineer", "solutions consultant", "pre-sales", "presales",
    "implementation consultant", "onboarding manager", "professional services",
    "data migration", "hris", "sirh", "sap hcm", "successfactors", "sap hr",
    "product manager", "product owner", "head of product",
    "ux designer", "ui designer", "product designer", "ux lead", "ux researcher",
    "seo manager", "seo lead", "head of seo", "seo specialist", "seo strategist", "geo manager",
    "generative engine optimization", "answer engine optimization", "aeo",
    "formateur", "ai trainer", "genai", "ai enablement", "ai adoption", "chief of staff",
    "renewals manager", "customer retention", "customer education", "customer training",
    "partner manager", "alliances manager", "engagement manager", "delivery manager",
]

EXCLUDE = [
    "intern", "internship", "alternance", "alternant", "stage", "stagiaire", "apprenti",
    "entry-level", "entry level", "new grad", "graduate program"
]

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read().decode("utf-8", "replace"))
    except Exception as e:
        return {"__error__": str(e)}

def match_title(title):
    t = title.lower()
    if any(x in t for x in EXCLUDE):
        return False
    return any(k in t for k in KEYWORDS)

def ashby(slug):
    data = fetch(f"https://api.ashbyhq.com/posting-api/job-board/{slug}")
    if "__error__" in data or "jobs" not in data:
        return []
    out = []
    for j in data["jobs"]:
        if not j.get("isListed", True):
            continue
        title = j.get("title", "")
        if not match_title(title):
            continue
        out.append({
            "source": f"Ashby:{slug}",
            "title": title,
            "location": j.get("location"),
            "secondaryLocations": [sl.get("location") for sl in j.get("secondaryLocations", [])],
            "isRemote": j.get("isRemote"),
            "workplaceType": j.get("workplaceType"),
            "publishedAt": j.get("publishedAt"),
            "jobUrl": j.get("jobUrl") or j.get("applyUrl"),
            "department": j.get("department"),
        })
    return out

def lever(slug):
    data = fetch(f"https://api.lever.co/v0/postings/{slug}?mode=json")
    if isinstance(data, dict) and "__error__" in data:
        return []
    if not isinstance(data, list):
        return []
    out = []
    for j in data:
        title = j.get("text", "")
        if not match_title(title):
            continue
        cats = j.get("categories", {})
        out.append({
            "source": f"Lever:{slug}",
            "title": title,
            "location": cats.get("location"),
            "workplaceType": j.get("workplaceType"),
            "team": cats.get("team"),
            "commitment": cats.get("commitment"),
            "publishedAt": j.get("createdAt"),
            "hostedUrl": j.get("hostedUrl"),
        })
    return out

def greenhouse(slug):
    data = fetch(f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs?content=true")
    if isinstance(data, dict) and "__error__" in data:
        return []
    if not isinstance(data, dict) or "jobs" not in data:
        return []
    out = []
    for j in data["jobs"]:
        title = j.get("title", "")
        if not match_title(title):
            continue
        out.append({
            "source": f"Greenhouse:{slug}",
            "title": title,
            "location": (j.get("location") or {}).get("name"),
            "updated_at": j.get("updated_at"),
            "absolute_url": j.get("absolute_url"),
        })
    return out

if __name__ == "__main__":
    kind = sys.argv[1]
    slugs = sys.argv[2:]
    fn = {"ashby": ashby, "lever": lever, "greenhouse": greenhouse}[kind]
    results = {}
    for s in slugs:
        r = fn(s)
        if r:
            results[s] = r
    print(json.dumps(results, indent=1, ensure_ascii=False))
