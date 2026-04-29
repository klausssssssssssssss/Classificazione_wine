# Classificazione Wine
![Wines](vini.jpeg)

Progetto di classificazione supervisionata sul dataset **Wine** di scikit-learn.
L’obiettivo è predire la classe del vino (3 classi) a partire da feature chimico-fisiche.

## Dataset
- Fonte: `sklearn.datasets.load_wine`
- Campioni: 178
- Feature: 13 (continue)
- Classi: 3

## Approccio
Il workflow consiste dei seguenti step:
- split **train/test** con stratificazione
- **Pipeline** per includere preprocessing + modello
- **GridSearchCV** con **StratifiedKFold** sul solo training set
- valutazione finale sul **test set** 

## Modelli
- **K-Nearest Neighbors (KNN)** in pipeline con `StandardScaler`
  - hyperparameter tuning: `n_neighbors`, `weights`, `p` (Manhattan/Euclidean)
- **Logistic Regression** in pipeline con `StandardScaler`

## Metriche
Valutazione tramite:
- Accuracy
- Precision (macro)
- Recall (macro)
- F1-score (macro)



# FastAPI e Pydantic

FastAPI è un framework web moderno per Python progettato per semplificare la creazione di API. È ampiamente apprezzato per le sue prestazioni elevate e per l'ottima esperienza di sviluppo che offre. La sua forza principale risiede nella sinergia con **Pydantic**, che aggiunge uno strato fondamentale per la gestione, la validazione e il parsing dei dati.

## Il Ruolo di Pydantic in FastAPI

Pydantic è una libreria Python essenziale per le applicazioni FastAPI, focalizzata sulla validazione e la conversione dei dati. Svolge un ruolo cruciale in due aree principali:

### 1. Validazione dei Dati
Pydantic permette di definire modelli di dati (**user-defined schemas**) che includono:
*   **Tipi di dato:** Definizione esplicita (stringhe, interi, ecc.).
*   **Regole di validazione:** Vincoli personalizzati per i campi.
*   **Valori di default:** Gestione automatica dei dati mancanti.

Questo processo garantisce che i dati in ingresso rispettino rigorosamente la struttura attesa, assicurando l'integrità e l'affidabilità dell'intera API.

### 2. Parsing e Conversione Automatica
Oltre alla validazione, Pydantic eccelle nel convertire automaticamente i dati provenienti da diversi formati (come **JSON** o **form data**) in oggetti Python coerenti. Basandosi sui modelli definiti, il framework trasforma i dati grezzi in un formato pronto per essere elaborato dalla logica di business, riducendo drasticamente il lavoro manuale di conversione e il rischio di errori.

