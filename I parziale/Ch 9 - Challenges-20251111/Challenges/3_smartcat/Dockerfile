FROM python:3

# Strumenti di sistema necessari (ping)
RUN apt-get update \
 && apt-get install -y --no-install-recommends iputils-ping \
 && rm -rf /var/lib/apt/lists/*

# Directory di lavoro
WORKDIR /chall

# Copia dei sorgenti
COPY chall/ /chall/

# uWSGI compatibile con Py3.14
RUN pip install --no-cache-dir "uwsgi==2.0.31"

# Avvio uWSGI in HTTP (porta 5000) e specifica esplicita del callable
CMD ["uwsgi","--http", "0.0.0.0:5000","--wsgi-file", "/chall/index.py","--callable", "application","--master","--threads", "4","--die-on-term"]
