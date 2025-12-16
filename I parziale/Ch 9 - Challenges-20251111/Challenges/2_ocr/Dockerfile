# Base compatibile con Python 3.12+ (anche 3.14). Va bene anche la tua immagine “slim” recente.
FROM python:3-slim

# Evita prompt interattivi
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Dipendenze di sistema necessarie a tesseract/pillow
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        tesseract-ocr \
        tesseract-ocr-eng \
        libtesseract-dev \
        libleptonica-dev \
        libc6 \
        libjpeg62-turbo \
        zlib1g \
        ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Crea utente non-root
RUN useradd -m -U -s /usr/sbin/nologin python-runner

# Directory di lavoro
RUN mkdir -p /var/www
WORKDIR /var/www

# Requisiti Python (pin ragionevoli e compatibili con Py3.12+)
COPY www/requirements.txt /var/www/requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /var/www/requirements.txt

# Aggiunge il "paracadute" per librerie legacy che importano distutils
COPY www/sitecustomize.py /var/www/sitecustomize.py

# Copia l'app
COPY www/ /var/www/

# Permessi
RUN chown -R python-runner:python-runner /var/www
USER python-runner

# Porta HTTP
EXPOSE 5000

# Avvio con gunicorn
# NB: server:app assume che in /var/www/server.py ci sia 'app = Flask(__name__)'
CMD ["gunicorn", "server:app", "-b", "0.0.0.0:5000", "--access-logfile", "-", "--error-logfile", "-"]
