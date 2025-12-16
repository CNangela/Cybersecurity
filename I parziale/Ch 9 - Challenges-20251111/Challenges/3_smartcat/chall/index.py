#!/usr/bin/env python3
import os
import subprocess
from urllib.parse import parse_qs
import html

# uWSGI/WSGI callable
def application(environ, start_response):
    header_xpb = [
        "mod_cassette_is_back/0.1",
        "format-me-i-im-famous",
        "dirbuster.will.not.help.you",
        "solve_me_already",
    ]
    headers = [
        ("X-Powered-By", header_xpb[os.getpid() % 4]),
        ("Content-Type", "text/html; charset=utf-8"),
    ]

    # Leggi input (POST o GET)
    method = environ.get("REQUEST_METHOD", "GET").upper()
    try:
        size = int(environ.get("CONTENT_LENGTH") or 0)
    except (ValueError, TypeError):
        size = 0

    body = ""
    if method == "POST" and size > 0:
        body = environ["wsgi.input"].read(size).decode("utf-8", "ignore")
        qs = parse_qs(body)
    else:
        qs = parse_qs(environ.get("QUERY_STRING", ""))

    # Valore di default
    dest = qs.get("dest", ["8.8.8.8"])[0]

    # ATTENZIONE: per mantenere la natura della challenge potresti voler lasciare shell=True.
    # Se vuoi mitigare, passa lista di argomenti e rimuovi shell=True.
    try:
        # Esegue un solo ping per evitare attese infinite
        completed = subprocess.run(
            f"ping -c 1 {dest}",
            shell=True,               # volutamente vulnerabile per la challenge
            capture_output=True,
            text=True,
            timeout=3
        )
        results = (completed.stdout or "") + (completed.stderr or "")
    except Exception as e:
        results = f"Error running ping: {e}"

    # Escaping sicuro per renderizzare l'output
    safe_results = html.escape(results)

    r = f"""<!doctype html>
<html>
  <head>
    <meta charset="utf-8"/>
    <title>SmartCat</title>
  </head>
  <body>
    <h1>SmartCat debugging interface</h1>
    <form method="POST">
      <p>Ping destination: <input type="text" name="dest" value="{html.escape(dest)}"/></p>
      <button type="submit">Ping</button>
    </form>
    <p>Ping results:</p>
    <pre>{safe_results}</pre>
  </body>
</html>"""

    status = "200 OK"
    start_response(status, headers)
    # uWSGI/WSGI in Python 3 si aspetta bytes
    return [r.encode("utf-8")]
