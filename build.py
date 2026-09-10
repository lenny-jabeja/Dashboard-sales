import re, pathlib

src = pathlib.Path("index.html").read_text(encoding="utf-8")

title = re.search(r"<title>(.*?)</title>", src, re.S)
title = title.group(1).strip() if title else "Test Dashboard Sales"

links = re.findall(r'<link rel="stylesheet"[^>]*>', src)

body = src
body = re.sub(r"<title>.*?</title>\s*", "", body, count=1, flags=re.S)
for l in links:
    body = body.replace(l, "", 1)
body = body.strip()

head_extra = "\n  ".join(links)

doc = f"""<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="Zwart-wit salesdashboard voor het marketingteam: hero, KPI's en een werkblad met alle leads.">
  {head_extra}
  <style>
    html{{color-scheme:light dark}}
    body{{margin:0}}
    img{{max-width:100%}}
    [hidden]{{display:none!important}}
  </style>
</head>
<body>
{body}
</body>
</html>
"""

out = pathlib.Path("docs")
out.mkdir(exist_ok=True)
(out / "index.html").write_text(doc, encoding="utf-8")
(out / ".nojekyll").write_text("", encoding="utf-8")
print("docs/index.html geschreven —", len(doc), "bytes")
