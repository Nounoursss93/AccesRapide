# AccesRapide ✨ - Votre Gestionnaire de Favoris Personnel

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-green.svg)
![PyInstaller](https://img.shields.io/badge/Packaging-PyInstaller-orange.svg)
![License](https://img.shields.io/badge/License-No%20License-red.svg)

Bienvenue sur **AccesRapide**, Votre outil de bureau tout-en-un pour retrouver instantanément vos ressources essentielles. Une solution pratique, intuitive et esthétique pour rester organisé.

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

**AccesRapide** est une application de bureau légère et élégante conçue pour simplifier votre navigation quotidienne. Que ce soit pour accéder rapidement à un dossier de projet fréquemment utilisé votre application favorite ou bien pour lancer votre site web préféré, AccesRapide met tout à portée de main.

Construite avec `CustomTkinter` pour une interface utilisateur moderne et personnalisable, elle offre une expérience fluide et agréable. Vos favoris sont sauvegardés automatiquement, pour que vous retrouviez votre environnement de travail exactement comme vous l'avez laissé.

## 💡 Fonctionnalités Clés

* **📁 Gestion des Dossiers Favoris :**
    * Ajoutez n'importe quel dossier de votre système de fichiers.
    * Ouvrez les dossiers directement via l'explorateur (Windows) ou le Finder (macOS).
    * Modifiez facilement le nom, l'icône ou le chemin d'un dossier existant.
    * Icône par défaut pour les dossier.
    * Choisir l'icone de votre choix parmis un catalogue.
    * Supprimez les dossiers devenus obsolètes.
    * Vérification automatique de l'existence des chemins de dossiers au démarrage.
 
 * **📁 Gestion des Applications Favorites :**
    * Ajoutez votre application en renseignant le chemun ou se trouve son exécutable.
    * Ouvrez les applications directement via l'explorateur (Windows).
    * Modifiez facilement le nom, l'icône ou le chemin d'une application existante.
    * Icône par défaut pour les application.
    * Choisir l'icone de votre choix parmis un catalogue.
    * Supprimez les applications devenus obsolètes.
    * Vérification automatique de l'existence des chemins des applications au démarrage.

* **🌐 Gestion des Sites Web Favoris :**
    * Enregistrez vos URLs préférées.
    * Ouvrez les sites web dans votre navigateur par défaut.
    * **Récupération automatique des Favicons** : L'application tente de télécharger et d'afficher l'icône de chaque site web pour une identification visuelle rapide.
    * Icône par défaut pour les liens dont les sites ne permettent pas la récupération des icones.
    * Choisir l'icone de votre choix parmis un catalogue.
    * Modifiez facilement l'URL, l'icône ou le nom d'un site web.
    * Supprimez les sites web obsolètes de votre liste.

* **🔄 Bascule Rapide :**
    * Passez instantanément de la vue des dossiers à la vue des sites web ou encore à la vue de vos applications grâce aux boutons dédiés.

* **🎨 Thèmes Personnalisables :**
    * Choisissez entre les modes d'apparence **Sombre** ou **Clair**.


* **💾 Persistance des Données :**
    * Tous vos favoris sont automatiquement sauvegardés dans des fichiers JSON.

* **✨ Interface Intuitive :**
    * Design épuré et facile à utiliser grâce à CustomTkinter.
    * Icônes dédiées pour chaque action (ajouter, modifier, supprimer).

## 📸 Aperçu

* **Écran principal - Vue Web thème sombre :**                    **Écran principal - Vue Web thème clair :**

<table>
  <tr>
    <th style="text-align:center">Vue Web Foncé</th>
    <th style="text-align:center">Vue Web Clair</th>
  </tr>
  <tr>
    <td><img src="https://github.com/Nounoursss93/AccesRapide/blob/main/Images/Web%20Sombre.jpg?raw=true" width="400"/></td>
    <td><img src="https://github.com/Nounoursss93/AccesRapide/blob/main/Images/Web%20Clair.jpg?raw=true" width="395"/></td>
  </tr>
</table>


   
* **Écran principal - Vue Sites Web (avec favicons) :**
  
    ![Favoris Websites](https://github.com/KiralyGeddon/Fav-Me/blob/main/images/2.png)
   
* **Fenêtre d'ajout/édition de favori :**
  
    https://github.com/Nounoursss93/AccesRapide/blob/main/Images/Ajout%20favoris%20dossier.jpg
   
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

Suivez ces étapes pour faire fonctionner AccesRapide sur votre machine locale.

### Prérequis

Assurez-vous d'avoir Python 3.x installé sur votre système.

### Installation

1.  **Clonez le dépôt** (ou téléchargez le fichier `AccesRapide.py` et les icônes) :
    ```bash
    git clone https://github.com/Nounoursss93/AccesRapide
    cd AccesRapide/script  # Accédez au répertoire du projet # Accédez au répertoire du projet
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
    cd "C:\Users\$env:USERNAME\AccesRapide\Script"
    ```

3.  **Exécutez PyInstaller** :
    ```bash
    pyinstaller --noconfirm --onefile --windowed --icon="Logo_Raccourci.png" --add-data "../Favoris_Data/Icons;Icons" --add-data "../Favoris_Data/Favicons;Favicons" --add-data "../Favoris_Data/data;data" "AccesRapide.py"
    ```
    * `--noconfirm` : Écrase les anciens fichiers `dist/` et `build/` sans confirmation.
    * `--onefile` : Crée un seul fichier exécutable.
    * `--windowed` : Empêche l'ouverture d'une console (pour les applications GUI).
    * `--icon="Logo_Raccourci.png" : Spécifie l'icône de l'exécutable (assurez-vous que Logo_Raccourci.png est dans le même répertoire ou spécifiez le chemin complet).
    * `--add-data "Favoris_Data/icons;icons" : Inclut le dossier icons dans l'exécutable.
    * `--add-data "Favoris_Data/settings.json;." et --add-data "Favoris_Data/favs.json;." : Incluent les fichiers de config et données.

    L'exécutable sera généré dans le dossier `dist/`.

## 📦 Versions Distribuées

### Exécutable Autonome

#### Option 1 : Création via PyInstaller

Une fois construit avec PyInstaller, vous trouverez un fichier `.exe` (ou l'équivalent pour votre OS) dans le répertoire `dist/`. Vous pouvez le copier et l'exécuter directement sur n'importe quel système Windows sans avoir besoin d'installer Python ou des dépendances.

#### Option 2 : Exécutables et dossiers déjà créés
Une version est déjà fournie dans le dossier `Application` à partir du script actuel avec les dossiers et fchiers nécessaire ainsi qu'un fichier texte indiquant les diférentes étapes à suivre.


## 🖥️ Utilisation

1.  **Lancement de l'Application :**
    * Si vous exécutez le script Python : `python AccesRapide.py`
    * Si vous utilisez l'exécutable : Double-cliquez sur `AccesRapide.exe` dans le dossier `dist/`.
    * Si vous avez utilisé l'installateur : Lancez l'application depuis le menu Démarrer ou le raccourci sur le bureau.

2.  **Gestion des Favoris :**
    * **Ajouter :** Cliquez sur le bouton `Ajouter un favori` pour ajouter un nouveau dossier, application ou site web favori.
    * **Modifier :** Cliquez sur l'icône d'édition (Outils) à côté d'un élément pour modifier son nom,son icône ou son chemin/URL.
    * **Supprimer :** Cliquez sur l'icône de suppression (Croix blanche sur carré rouge) à côté d'un élément pour le retirer de votre liste.
    * **Ouvrir :** Cliquez sur le nom d'un dossier,d'une application ou d'un site web pour l'ouvrir.

3.  **Bascule entre Vues :**
    * Utilisez le bouton voulu en haut de l'interface pour passer de la vue "Dossier" à la vue "Application" ou à la vue "Web".

4.  **Paramètres de Thème :**
    * Choisissez votre mode d'apparence ( Sombre ou Clair ). Les modifications sont appliquées instantanément et sauvegardées.

## 🗂️ Stockage des Données et Paramètres

AccesRapide sauvegarde automatiquement vos favoris et paramètres dans des fichiers .JSON situés dans le dossier de données :

    folders.json : contient la liste complète de vos dossiers ( ce fichier sera crée lors de la première utilisation de AccesRapide ).

    websites.json : contient la liste complète de vos sites web favoris ( ce fichier sera crée lors de la première utilisation de AccesRapide ).

    applications.json : contient la liste complète de vos sites web favoris ( ce fichier sera crée lors de la première utilisation de AccesRapide ).

    icones.json : contient l'association de vos icônes avec le favoris dossier , application ou Web associé ( ce fichier est déjà pré-rempli pour que ce soit plus agréable au démarrage ).

Les icônes personnalisées associées aux favoris sont conservées dans le dossier icons/ et vos favicons dans le dossier favicons/.

Ces fichiers sont créés et mis à jour dans le même répertoire que l'exécutable de l'application.

## 🤝 Contribution

Merci à [Samuel aka KiralyGeddon(https://github.com/KiralyGeddon)] pour la mise en page! 

Les contributions sont les bienvenues ! Si vous avez des idées d'amélioration, des rapports de bugs ou de nouvelles fonctionnalités à proposer, n'hésitez pas à :

1.  Faire un fork du dépôt.
2.  Créer une nouvelle branche (`git checkout -b feature/AmazingFeature`).
3.  Effectuer vos modifications et committer (`git commit -m 'Add some AmazingFeature'`).
4.  Pousser vers la branche (`git push origin feature/AmazingFeature`).
5.  Ouvrir une Pull Request.

## ✉️ Contact

Pour toute question ou commentaire, vous pouvez me contacter via GitHub.
