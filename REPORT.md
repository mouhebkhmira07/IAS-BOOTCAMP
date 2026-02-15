# 📋 Rapport de Projet — Laser Leak Detection System

## 1. Contexte et Objectif

**Problème :** Les fuites d'air dans les canalisations industrielles sont difficiles à détecter visuellement. Les méthodes traditionnelles (savon, ultrasons) sont lentes et coûteuses.

**Solution :** Un système de vision par ordinateur qui détecte la **perte de signature laser** sur les tuyaux. Un laser est projeté le long du tuyau — si le faisceau est interrompu ou absent, cela indique une fuite d'air à haute pression.

---

## 2. Architecture du Projet

```
IAS-BOOTCAMP/
├── .github/workflows/         # CI/CD Pipeline (GitHub Actions)
│   └── pipeline.yml
├── Laser-detection-1/         # Dataset Roboflow (train/test/valid)
│   ├── data.yaml
│   ├── train/images & labels/
│   ├── valid/images & labels/
│   └── test/images & labels/
├── data/                      # Données brutes et traitées
├── runs/                      # Résultats d'entraînement et d'évaluation
├── src/vision/
│   └── load_model.py          # Chargement du modèle via Roboflow API
├── app.py                     # Interface Streamlit
├── train.py                   # Script d'entraînement YOLOv8
├── evaluate.py                # Évaluation + matrice de confusion
├── Laser_Leak_Detection.ipynb # Notebook Google Colab
├── dvc.yaml                   # Pipeline DVC
└── requirements.txt           # Dépendances
```

---

## 3. Techniques et Technologies Utilisées

### 3.1 Deep Learning — YOLOv8 (Object Detection)

| Aspect | Détail |
|--------|--------|
| **Modèle** | YOLOv8n (nano) — rapide et léger |
| **Framework** | Ultralytics |
| **Type** | Détection d'objets en temps réel |
| **Classe** | 1 classe : `laser` |
| **Transfer Learning** | Poids pré-entraînés sur COCO, fine-tunés sur notre dataset |
| **Epochs** | 50 (avec early stopping) |
| **Image Size** | 640×640 pixels |
| **Batch Size** | 16 |

**Pourquoi YOLOv8 ?**
- Architecture one-stage : détection rapide en une seule passe
- Excellent rapport précision/vitesse
- Idéal pour le déploiement en temps réel

### 3.2 Dataset — Roboflow

| Aspect | Détail |
|--------|--------|
| **Source** | Roboflow Universe |
| **Workspace** | laser-detection-cco13 |
| **Projet** | laser-detection-w531n |
| **Format** | YOLOv8 (images + labels txt) |
| **Split** | Train / Validation / Test |
| **Annotation** | Bounding boxes autour des signatures laser |

### 3.3 Interface Web — Streamlit

- Upload d'images de tuyaux
- Inférence en temps réel via l'API Roboflow
- Alertes automatiques : ✅ Laser détecté / 🚨 Fuite potentielle

### 3.4 MLOps & CI/CD

| Outil | Usage |
|-------|-------|
| **DVC** | Versioning des données et du pipeline |
| **GitHub Actions** | Linting automatique, vérification des dépendances |
| **Git** | Contrôle de version du code source |
| **Google Colab** | Entraînement GPU (T4) |

### 3.5 Métriques d'Évaluation

| Métrique | Description |
|----------|-------------|
| **Précision** | Parmi les détections positives, combien sont correctes |
| **Rappel (Recall)** | Parmi les vrais lasers, combien sont détectés |
| **mAP@50** | Mean Average Precision à IoU=0.5 |
| **mAP@50-95** | mAP moyennée sur IoU de 0.5 à 0.95 |
| **F1-Score** | Moyenne harmonique de Précision et Rappel |
| **Matrice de confusion** | Vrais/faux positifs et négatifs |

---

## 4. Pipeline d'Exécution

```
Dataset (Roboflow) → Entraînement (YOLOv8) → Évaluation (métriques) → Déploiement (Streamlit)
```

### Commandes :
```bash
# Entraîner le modèle
python train.py

# Générer la matrice de confusion et les rapports
python evaluate.py

# Lancer l'application web
python -m streamlit run app.py
```

---

## 5. Résumé des Livrables

- ✅ Modèle YOLOv8 entraîné pour la détection laser
- ✅ Interface web Streamlit pour la surveillance
- ✅ Matrice de confusion et courbes de performance
- ✅ Pipeline CI/CD avec GitHub Actions
- ✅ Notebook Colab pour l'entraînement GPU
- ✅ Documentation complète

---

*Projet réalisé dans le cadre de l'IAS Bootcamp.*
