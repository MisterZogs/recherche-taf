import json
import re
import unicodedata

FILES = [
    "relance_20260923_cluster_fr.json",
    "relance_20260923_cluster_ats.json",
    "relance_20260923_cluster_remote.json",
    "relance_20260923_cluster_pb.json",
]


def norm(s):
    if not s:
        return ""
    s = str(s).lower().strip()
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"\(.*?\)", "", s)  # retire mentions entre parenthèses
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def norm_link(l):
    if not l:
        return ""
    l = str(l).strip()
    l = re.sub(r"[?#].*$", "", l)  # retire query string / fragment
    l = l.rstrip("/")
    l = re.sub(r"^https?://(www\.)?", "", l)
    return l.lower()


all_offres = []
for f in FILES:
    with open(f, encoding="utf-8") as fh:
        data = json.load(fh)
    print(f"{f}: {len(data)} offres")
    all_offres.append((f, data))

merged = []
seen_links = set()
seen_pairs = set()
dropped_link = 0
dropped_pair = 0

for fname, data in all_offres:
    for offre in data:
        # normalisation défensive : Contrat parfois une liste (bug connu)
        if isinstance(offre.get("Contrat"), list):
            offre["Contrat"] = ", ".join(str(x) for x in offre["Contrat"])
        for k, v in list(offre.items()):
            if isinstance(v, list):
                offre[k] = ", ".join(str(x) for x in v)

        lien = norm_link(offre.get("Lien"))
        pair = (norm(offre.get("Entreprise")), norm(offre.get("Poste")))

        if lien and lien in seen_links:
            dropped_link += 1
            continue
        if pair[0] and pair[1] and pair in seen_pairs:
            dropped_pair += 1
            continue

        if lien:
            seen_links.add(lien)
        if pair[0] and pair[1]:
            seen_pairs.add(pair)
        merged.append(offre)

print(f"\nTotal brut : {sum(len(d) for _, d in all_offres)}")
print(f"Doublons lien retirés : {dropped_link}")
print(f"Doublons paire Entreprise+Poste retirés : {dropped_pair}")
print(f"Total fusionné : {len(merged)}")

with open("relance_20260923_merged.json", "w", encoding="utf-8") as fh:
    json.dump(merged, fh, ensure_ascii=False, indent=1)

print("\nÉcrit dans relance_20260923_merged.json")
