# Fatigue-Detection 👁️🚘

**Fatigue-Detection** est un système de vision par ordinateur en temps réel développé en Python. Il utilise **OpenCV** et **MediaPipe** pour analyser les points caractéristiques du visage (Face Mesh) et détecter la fatigue ou le somnolence du conducteur en calculant le taux d'ouverture des yeux (*Eye Aspect Ratio - EAR*).

---

## 🌟 Fonctionnalités Principales

- **📹 Test et Capture Vidéo** : Vérification rapide et simple du flux de la caméra web.
- **👤 Analyse Faciale en Temps Réel** : Cartographie complète du visage grâce aux 468 points de repère de MediaPipe Face Mesh.
- **👁️ Calcul de l'EAR (Eye Aspect Ratio)** : Mesure précise de la fermeture des yeux en temps réel.
- **🚨 Alerte de Fatigue Automatique** : Affichage d'un avertissement visuel sur le flux vidéo (`FATIGUE DETECTED`) si les yeux restent fermés pendant plus de 2 secondes.

---

## 🛠️ Technologies Utilisées

- **Python 3.8+**
- **OpenCV** (`opencv-python`) : Capture et traitement d'images en temps réel.
- **MediaPipe** (`mediapipe`) : Modèle avancé de détection de repères faciaux (Face Mesh).
- **NumPy** (`numpy`) : Calculs matriciels et scientifiques.

---

## 📂 Structure du Projet

```text
Fatigue-Detection/
├── assets/             # Fichiers médias, captures d'écran et démos
├── data/               # Données de test ou enregistrements
├── docs/               # Documentation complémentaire
├── models/             # Modèles pré-entraînés (si applicables)
├── src/                # Modules sources du projet
├── cameratest.py       # Script de test de la webcam
├── detection.py        # Script principal de détection de fatigue (EAR)
├── face.py             # Script de démonstration du Face Mesh MediaPipe
├── test.py             # Script de vérification de l'environnement Python
├── .gitignore          # Fichiers et dossiers à ignorer par Git
├── requirements.txt    # Dépendances du projet
└── README.md           # Documentation principale
```

---

## 🚀 Installation et Configuration

### 1. Prérequis
Assurez-vous d'avoir **Python 3.8** ou une version supérieure installée sur votre machine.

### 2. Cloner le projet
```bash
git clone https://github.com/VOTRE_NOM_UTILISATEUR/Fatigue-Detection.git
cd Fatigue-Detection
```

### 3. Créer et activer un environnement virtuel (recommandé)

- **Sur Windows (PowerShell) :**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```

- **Sur Linux / macOS :**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 4. Installer les dépendances
```bash
pip install -r requirements.txt
```

---

## 💻 Utilisation

### 1. Vérifier l'installation
Pour vérifier que toutes les bibliothèques sont bien installées :
```bash
python test.py
```

### 2. Tester la caméra
Pour s'assurer que la webcam fonctionne correctement :
```bash
python cameratest.py
```
*(Appuyez sur la touche `q` pour quitter).*

### 3. Tester la détection faciale (Face Mesh)
Pour observer le suivi des points caractéristiques du visage en temps réel :
```bash
python face.py
```
*(Appuyez sur la touche `q` pour quitter).*

### 4. Lancer la détection de fatigue (Script Principal)
Pour démarrer la surveillance et le calcul de l'EAR :
```bash
python detection.py
```
- **Seuil EAR** : Fixé à `0.20`.
- **Durée d'alerte** : Si les yeux restent fermés plus de `2 secondes`, l'alerte **FATIGUE DETECTED** s'affiche en rouge à l'écran.
- *(Appuyez sur la touche `q` pour quitter).*

---

## 🧠 Principe du Calcul de l'EAR (Eye Aspect Ratio)

L'**Eye Aspect Ratio (EAR)** est une mesure géométrique basée sur la distance entre les repères des paupières supérieures et inférieures par rapport à la distance entre les coins de l'œil :

$$EAR = \frac{||p_2 - p_6|| + ||p_3 - p_5||}{2 \times ||p_1 - p_4||}$$

Lorsque les yeux sont ouverts, la valeur de l'EAR est élevée et stable. Lorsque la personne ferme les yeux ou cligne des paupières, l'EAR chute brusquement vers zéro.

---

## 📤 Publication sur GitHub

Pour envoyer ce projet sur votre compte GitHub :

1. **Initialiser le dépôt local (déjà fait) :**
   ```bash
   git init
   ```
2. **Ajouter les fichiers et faire le commit :**
   ```bash
   git add .
   git commit -m "Update project name to Fatigue-Detection"
   ```
3. **Lier à votre dépôt distant GitHub et envoyer :**
   ```bash
   git branch -M main
   git remote add origin https://github.com/VOTRE_NOM_UTILISATEUR/Fatigue-Detection.git
   git push -u origin main
   ```

---

## 📄 Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, le modifier et le distribuer.
