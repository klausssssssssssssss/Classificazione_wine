FROM python:3.12-slim

WORKDIR /app

#ciao

# Copia e installa dipendenze prima (cache layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice
COPY . .

# Espone la porta (documentativo)
EXPOSE 8001

# Avvia FastAPI (modifica "app.main:app" se il tuo path è diverso)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]

# Per buildare: docker build -t wine-classification-api .
# Per runnare: docker run -p 8001:8001 wine-classification-api