import hashlib, hmac, json, requests

secret = "hg2026_python_engineer@!"
endpoint = "https://howgood-apply-api.howgood.workers.dev/apply"

payload = {
    "name": "Alejandro Luperon",
    "email": "alejandro.luperon@gmail.com",
    "resume": "https://github.com/AlejandroLuperon/how-good/blob/main/Alejandro%20Luperon%20-%20Resume%20-%2010_21_2026.pdf",       # URL to your resume
    "location": "Miami, Florida",     # e.g. "New York, NY"
    "linkedin": "https://www.linkedin.com/in/alejandroluperon/",
    "codeLink": "https://github.com/AlejandroLuperon/how-good/blob/main/how_good.py",     # URL to the repo/gist containing THIS script
    "yearsPython": 12,
    "yearsDjango": 1,
}

body = json.dumps(payload)
signature = hmac.new(secret.encode(), body.encode(), hashlib.sha256).hexdigest()

resp = requests.post(
    endpoint,
    data=body,
    headers={
        "Content-Type": "application/json",
        "X-HMAC-Signature": signature,
    },
)
print(resp.status_code, resp.json())
