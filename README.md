# Classificazione Wine

Progetto di classificazione supervisionata sul dataset **Wine** di scikit-learn.
L’obiettivo è predire la classe del vino (3 classi) a partire da feature chimico-fisiche.

## Dataset
- Fonte: `sklearn.datasets.load_wine`
- Campioni: 178
- Feature: 13 (continue)
- Classi: 3

## Approccio
Il workflow segue buone pratiche per evitare **data leakage**:
- split **train/test** con stratificazione
- **Pipeline** per includere preprocessing + modello
- **GridSearchCV** con **StratifiedKFold** sul solo training set
- valutazione finale sul **test set** (hold-out)

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

