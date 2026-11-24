"""Placeholders only. Standard library. send_email() accepts an injectable opener so it can be tested without the network."""
import json, os, urllib.request

BASE = "https://whats360.live"

def _post(path, body, token=None, opener=urllib.request.urlopen):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    req = urllib.request.Request(BASE + path, data=json.dumps(body).encode(), headers=headers, method="POST")
    with opener(req) as r:
        return json.loads(r.read().decode())

def login(username, password, opener=urllib.request.urlopen):
    return _post("/api/auth/login", {"username": username, "password": password}, opener=opener)["token"]

def send_email(token, sender, to, subject, body, opener=urllib.request.urlopen):
    return _post("/api/v1/email/send", {"from": sender, "to": to, "subject": subject, "body": body}, token, opener)

if __name__ == "__main__":
    t = login(os.environ["WHATS360_USER"], os.environ["WHATS360_PASSWORD"])
    print(send_email(t, "you@yourdomain.com", "recipient@example.com", "Hello from API", "This is the email body."))
