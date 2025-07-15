# AccesRapide ✨ - Votre Gestionnaire de Favoris Personnel

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-green.svg)
![PyInstaller](https://img.shields.io/badge/Packaging-PyInstaller-orange.svg)
![Installer](https://img.shields.io/badge/Installer-InnoSetup-lightgrey.svg)
![License](https://img.shields.io/badge/License-No%20License-red.svg)

Bienvenue sur **AccesRapide**, votre application de bureau intuitive pour gérer et accéder rapidement à vos dossiers et sites web favoris. Fini les recherches fastidieuses ! Organisez tout en un seul endroit pratique et stylé.

## 🚀 Table des Matières

-   [AccesRapide ✨ - Votre Gestionnaire de Favoris Personnel](#AccesRapide---votre-gestionnaire-de-favoris-personnel)
-   [🚀 Table des Matières](#-table-des-matières)
-   [🌟 À Propos de AccesRapide](#-à-propos-de-AccesRapide)
-   [💡 Fonctionnalités Clés](#-fonctionnalités-clés)
-   [📸 Aperçu](#-aperçu)
-   [📦 Technologies Utilisées](#-technologies-utilisées)
-   [🚀 Démarrage Rapide](#-démarrage-rapide)
    -   [Prérequis](#prérequis)
    -   [Installation](#installation)
    -   [Exécuter le Script Python](#exécuter-le-script-python)
    -   [Construire l'Exécutable (.exe) avec PyInstaller](#construire-lexécutable-exe-avec-pyinstaller)
-   [📦 Versions Distribuées](#-versions-distribuées)
    -   [Exécutable Autonome](#exécutable-autonome)
-   [🖥️ Utilisation](#️-utilisation)
-   [🗂️ Stockage des Données et Paramètres](#️-stockage-des-données-et-paramètres)
-   [🤝 Contribution](#-contribution)
-   [✉️ Contact](#️-contact)


## 🌟 À Propos de AccesRapide

**AccesRapide** est une application de bureau légère et élégante conçue pour simplifier votre navigation quotidienne. Que ce soit pour accéder rapidement à un dossier de projet fréquemment utilisé ou pour lancer votre site web préféré, Fav-Me met tout à portée de main.

Construite avec `CustomTkinter` pour une interface utilisateur moderne et personnalisable, elle offre une expérience fluide et agréable. Vos favoris et vos préférences de thème sont sauvegardés automatiquement, pour que vous retrouviez votre environnement de travail exactement comme vous l'avez laissé.

## 💡 Fonctionnalités Clés

* **📁 Gestion des Dossiers Favoris :**
    * Ajoutez n'importe quel dossier de votre système de fichiers.
    * Ouvrez les dossiers directement via l'explorateur (Windows) ou le Finder (macOS).
    * Modifiez facilement le nom ou le chemin d'un dossier existant.
    * icone par défaut pour les dossier.
    * Choisir l'icone de votre choix parmis un catalogue.
    * Supprimez les dossiers devenus obsolètes.
    * Vérification automatique de l'existence des chemins de dossiers au démarrage.

* **🌐 Gestion des Sites Web Favoris :**
    * Enregistrez vos URLs préférées.
    * Ouvrez les sites web dans votre navigateur par défaut.
    * **Récupération automatique des Favicons** : L'application tente de télécharger et d'afficher l'icône de chaque site web pour une identification visuelle rapide.
    * icone par défaut pour les liens dont les sites ne permettent pas la récupération des icones.
    * Choisir l'icone de votre choix parmis un catalogue.
    * Modifiez l'URL ou le nom d'un site web.
    * Supprimez les sites web de votre liste.

* **🔄 Bascule Rapide :**
    * Passez instantanément de la vue des dossiers à la vue des sites web grâce à un bouton dédié.

* **🎨 Thèmes Personnalisables :**
    * Choisissez entre les modes d'apparence **Sombre** ou **Clair**.


* **💾 Persistance des Données :**
    * Tous vos favoris et vos paramètres de thème sont automatiquement sauvegardés dans des fichiers JSON.

* **✨ Interface Intuitive :**
    * Design épuré et facile à utiliser grâce à CustomTkinter.
    * Icônes dédiées pour chaque action (ajouter, modifier, supprimer).

## 📸 Aperçu

* **Écran principal - Vue Dossiers :**
  
    ![Favoris Dossiers](https://github.com/KiralyGeddon/Fav-Me/blob/main/images/1.png)
   
* **Écran principal - Vue Sites Web (avec favicons) :**
  
    ![Favoris Websites](https://github.com/KiralyGeddon/Fav-Me/blob/main/images/2.png)
   
* **Fenêtre d'ajout/édition de favori :**
  
    ![Ajout de Favori](https://github.com/KiralyGeddon/Fav-Me/blob/main/images/3.png)
   
    ![Ajout de Dossier Favori](https://github.com/KiralyGeddon/Fav-Me/blob/main/images/4.png)

    ![Ajout de Site Web Favori](https://github.com/KiralyGeddon/Fav-Me/blob/main/images/5.png)

* **Fenêtre des paramètres de thème :**
  
    ![Theme Settings](https://github.com/KiralyGeddon/Fav-Me/blob/main/images/6.png)
    
* **Mode Clair :**
  
    ![Light Mode](https://github.com/KiralyGeddon/Fav-Me/blob/main/images/7.png)


## 📦 Technologies Utilisées

* **[Python](https://www.python.org/)** - Langage de programmation
* **[CustomTkinter](https://customtkinter.tomsons.de/)** - Bibliothèque GUI moderne pour Tkinter
* **[Pillow (PIL Fork)](https://python-pillow.org/)** - Pour le traitement des images (icônes, favicons)
* **[Requests](https://requests.readthedocs.io/en/latest/)** - Pour les requêtes HTTP (téléchargement des favicons)
* **[PyInstaller](https://pyinstaller.org/en/stable/)** - Pour compiler l'application en exécutable autonome
* **[Inno Setup](https://jrsoftware.org/isinfo.php)** - Pour créer un installateur Windows convivial

## 🚀 Démarrage Rapide

Suivez ces étapes pour faire fonctionner Fav-Me sur votre machine locale.

### Prérequis

Assurez-vous d'avoir Python 3.x installé sur votre système.

### Installation

1.  **Clonez le dépôt** (ou téléchargez le fichier `AccesRapide.py` et les icônes) :
    ```bash
   git clone https://github.com/Nounoursss93/AccesRapide
    cd AccesRapide/Fav-Me/script  # Accédez au répertoire du projet # Accédez au répertoire du projet
    ```

2.  **Installez les dépendances Python :**
    ```bash
    pip install customtkinter Pillow requests
    ```

### Exécuter le Script Python

Pour lancer l'application directement depuis le script Python :

```bash
python AccesRapide.py
```
### Construire l'Exécutable (.exe) avec PyInstaller

1.  **Installer PyInstaller** :
   
    Si vous ne l'avez pas déjà fait, installez PyInstaller en utilisant pip :
    ```bash
    pip install pyinstaller
    ```

2.  **Naviguez vers le répertoire du script** :
  
    Assurez-vous d'être dans le répertoire `script` où se trouve `AccesRapide.py`.
    ```bash
    cd AccesRapide/Fav-Me/script
    ```

3.  **Exécutez PyInstaller** :
    ```bash
    pyinstaller --noconfirm --onefile --windowed --icon="AccesRapide.ico" --add-data "Favoris_Data/icons;icons" --add-data "Favoris_Data/settings.json;." --add-data "Favoris_Data/favs.json;." "AccesRapide.py"
    ```
    * `--noconfirm` : Écrase les anciens fichiers `dist/` et `build/` sans confirmation.
    * `--onefile` : Crée un seul fichier exécutable.
    * `--windowed` : Empêche l'ouverture d'une console (pour les applications GUI).
    * `--icon="AccesRapide.ico" : Spécifie l'icône de l'exécutable (assurez-vous que AccesRapide.ico est dans le même répertoire ou spécifiez le chemin complet).
    * `--add-data "Favoris_Data/icons;icons" : Inclut le dossier icons dans l'exécutable.
    * `--add-data "Favoris_Data/settings.json;." et --add-data "Favoris_Data/favs.json;." : Incluent les fichiers de config et données.

    L'exécutable sera généré dans le dossier `dist/`.

## 📦 Versions Distribuées

### Exécutable Autonome

Une fois construit avec PyInstaller, vous trouverez un fichier `.exe` (ou l'équivalent pour votre OS) dans le répertoire `dist/`. Vous pouvez le copier et l'exécuter directement sur n'importe quel système Windows sans avoir besoin d'installer Python ou des dépendances.

Une version est déjà fournie dans le dossier `Version Portable/` à partir du script actuel.


## 🖥️ Utilisation

1.  **Lancement de l'Application :**
    * Si vous exécutez le script Python : `python AccesRapide.py`
    * Si vous utilisez l'exécutable : Double-cliquez sur `AccesRapide.exe` dans le dossier `dist/`.
    * Si vous avez utilisé l'installateur : Lancez l'application depuis le menu Démarrer ou le raccourci sur le bureau.

2.  **Gestion des Favoris :**
    * **Ajouter :** Cliquez sur le bouton `Ajouter favoris` pour ajouter un nouveau dossier ou site web favori.
    * **Modifier :** Cliquez sur l'icône d'édition (Outils) à côté d'un élément pour modifier son nom ou son chemin/URL.
    * **Supprimer :** Cliquez sur l'icône de suppression (Croix blanche sur carré rouge) à côté d'un élément pour le retirer de votre liste.
    * **Ouvrir :** Cliquez sur le nom d'un dossier ou d'un site web pour l'ouvrir.

3.  **Bascule entre Vues :**
    * Utilisez le bouton en bas de l'interface pour passer de la vue "Dossiers" à la vue "Sites Web" et inversement.

4.  **Paramètres de Thème :**
    * Choisissez votre mode d'apparence. Les modifications sont appliquées instantanément et sauvegardées.

## 🗂️ Stockage des Données et Paramètres

AccesRapide sauvegarde automatiquement vos favoris et paramètres dans des fichiers JSON situés dans le dossier de données :

    favs.json : contient la liste complète de vos dossiers et sites web favoris.

    settings.json : stocke les préférences utilisateur comme le thème et la couleur d’accentuation.

Les icônes personnalisées associées aux favoris sont conservées dans le sous-dossier icons/.


Ces fichiers sont créés et mis à jour dans le même répertoire que l'exécutable de l'application.

## 🤝 Contribution

Merci à [Samuel aka Nounoursss93(https://github.com/KiralyGeddon)] pour la mise en page! 

Les contributions sont les bienvenues ! Si vous avez des idées d'amélioration, des rapports de bugs ou de nouvelles fonctionnalités à proposer, n'hésitez pas à :

1.  Faire un fork du dépôt.
2.  Créer une nouvelle branche (`git checkout -b feature/AmazingFeature`).
3.  Effectuer vos modifications et committer (`git commit -m 'Add some AmazingFeature'`).
4.  Pousser vers la branche (`git push origin feature/AmazingFeature`).
5.  Ouvrir une Pull Request.

## ✉️ Contact

Pour toute question ou commentaire, vous pouvez me contacter via GitHub.
