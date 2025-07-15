import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import webbrowser
import os
import requests
import json
from urllib.parse import urlparse
from PIL import Image

# Configuration CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Chemins fixes
base_dir = os.path.join(os.path.expanduser("~"), "OneDrive - Kuehne+Nagel", "08 - Fichiers en cours", "Visual studio code", "Favoris_Data")
data_dir = os.path.join(base_dir, "data")
icons_dir = os.path.join(base_dir, "icons")
favicon_dir = os.path.join(base_dir, "favicons")
os.makedirs(data_dir, exist_ok=True)
os.makedirs(icons_dir, exist_ok=True)
os.makedirs(favicon_dir, exist_ok=True)

folders_json = os.path.join(data_dir, "folders.json")
websites_json = os.path.join(data_dir, "websites.json")

# Données par défaut
default_folders = {
    "Téléchargements": os.path.expanduser("~/Downloads"),
    "Documents": os.path.expanduser("~/Documents"),
    "TSSR": os.path.expanduser("~/OneDrive - Kuehne+Nagel/98 - TSSR"),
    "liste matériel": os.path.expanduser("~/OneDrive - Kuehne+Nagel/01 - Liste Matériel"),
    "Suivi panne": os.path.expanduser("~/OneDrive - Kuehne+Nagel/02 - Suivi Pannes"),
    "Commande matériel": os.path.expanduser("~/OneDrive - Kuehne+Nagel/03 - Commande Matériel"),
    "Mod OP": os.path.expanduser("~/OneDrive - Kuehne+Nagel/06 - Procédure et Modes Opératiores"),
    "Fichiers en cours": os.path.expanduser("~/OneDrive - Kuehne+Nagel/08 - Fichiers en cours"),
    "Python": os.path.expanduser("~/OneDrive - Kuehne+Nagel/08 - Fichiers en cours/Visual studio code"),
}

default_websites = {
    "topdesk": "https://emea.servicedesk.int.kn/tas/public/ssp/",
    "Wifi-Guest": "https://nac.int.kn/guest/main_intranet.php",
    "Chat GPT": "https://chatgpt.com/",
    "Google": "https://www.google.com",
    "Kammi": "https://kuehnenagelchatres3.kammi.pro/00home/home.php?home=homeV2/index"
}

# Chargement JSON
def load_json(path, default_data):
    try:
        if os.path.exists(path):
            with open(path, "r") as f:
                return json.load(f)
    except Exception as e:
        print(f"Erreur lecture JSON : {e}")

    with open(path, "w") as f:
        json.dump(default_data, f, indent=4)
    return default_data

favorite_folders = load_json(folders_json, default_folders)
favorite_websites = load_json(websites_json, default_websites)

# Icône par défaut
def create_default_icon(size=(20, 20), color=(50, 100, 200)):
    img = Image.new("RGBA", size, color + (255,))
    return ctk.CTkImage(light_image=img, dark_image=img, size=size)

default_icon = create_default_icon()

# Chargement icône "Outils.png" pour bouton modifier (doit exister dans icons_dir)
def load_tools_icon():
    path = os.path.join(icons_dir, "Outils.png")
    if os.path.exists(path):
        img = Image.open(path)
        return ctk.CTkImage(light_image=img, dark_image=img, size=(20, 20))
    return default_icon

tools_icon = load_tools_icon()

# Récupération des icônes personnalisées
def get_custom_icon(name, is_folder=False, is_web=False):
    icon_path = os.path.join(icons_dir, f"{name}.png")
    if os.path.exists(icon_path):
        img = Image.open(icon_path)
        return ctk.CTkImage(light_image=img, dark_image=img, size=(20, 20))

    fallback = "folder.png" if is_folder else "world-wide-web.png" if is_web else None
    if fallback:
        fallback_path = os.path.join(icons_dir, fallback)
        if os.path.exists(fallback_path):
            img = Image.open(fallback_path)
            return ctk.CTkImage(light_image=img, dark_image=img, size=(20, 20))

    return None

# Récupération favicon web
def get_favicon_ctkimage(url, size=(20, 20)):
    try:
        parsed_url = urlparse(url)
        domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
        favicon_url = domain + "/favicon.ico"
        filename = os.path.join(favicon_dir, parsed_url.netloc.replace(":", "_") + ".ico")
        if not os.path.exists(filename):
            try:
                r = requests.get(favicon_url, timeout=3)
                if r.status_code == 200:
                    with open(filename, "wb") as f:
                        f.write(r.content)
                else:
                    return None
            except requests.RequestException as e:
                print(f"Erreur favicon pour {url} : {e}")
                return None
        if os.path.exists(filename):
            image = Image.open(filename)
            return ctk.CTkImage(light_image=image, dark_image=image, size=size)
    except Exception as e:
        print(f"Erreur favicon générale pour {url} : {e}")
    return None

# Actions d'ouverture
def open_folder(path):
    os.startfile(path)

def open_website(url):
    webbrowser.open(url)

# Thème et vue
def switch_theme():
    new_mode = "light" if ctk.get_appearance_mode() == "Dark" else "dark"
    ctk.set_appearance_mode(new_mode)

def toggle_view():
    global showing_folders
    showing_folders = not showing_folders
    update_view()

def update_view():
    if showing_folders:
        folder_frame.pack(fill="both", expand=True, padx=20, pady=10)
        web_frame.pack_forget()
        toggle_button.configure(text="Web")
    else:
        web_frame.pack(fill="both", expand=True, padx=20, pady=10)
        folder_frame.pack_forget()
        toggle_button.configure(text="Dossiers")

# Fenêtre de confirmation custom CTk
def confirm_deletion(name, is_folder):
    confirm_win = ctk.CTkToplevel(app)
    confirm_win.title("Confirmer la suppression")
    confirm_win.geometry("350x130")
    confirm_win.resizable(False, False)
    confirm_win.grab_set()  # Modal

    label = ctk.CTkLabel(confirm_win, text=f"Voulez-vous vraiment supprimer\n'{name}' ?", justify="center", font=ctk.CTkFont(size=16, weight="bold"))
    label.pack(pady=(20, 15), padx=15)

    button_frame = ctk.CTkFrame(confirm_win)
    button_frame.pack(pady=(0, 15))

    def on_yes():
        if is_folder:
            if name in favorite_folders:
                del favorite_folders[name]
                # Supprimer icône associée
                icon_path = os.path.join(icons_dir, f"{name}.png")
                if os.path.exists(icon_path):
                    os.remove(icon_path)
            save_json(folders_json, favorite_folders)
        else:
            if name in favorite_websites:
                del favorite_websites[name]
                icon_path = os.path.join(icons_dir, f"{name}.png")
                if os.path.exists(icon_path):
                    os.remove(icon_path)
            save_json(websites_json, favorite_websites)
        refresh_favorites()
        confirm_win.destroy()

    def on_no():
        confirm_win.destroy()

    yes_btn = ctk.CTkButton(button_frame, text="Oui", width=80, fg_color="#d9534f", hover_color="#c9302c", command=on_yes)
    yes_btn.pack(side="left", padx=15)

    no_btn = ctk.CTkButton(button_frame, text="Non", width=80, command=on_no)
    no_btn.pack(side="right", padx=15)

# Suppression avec confirmation custom
def delete_favorite(name, is_folder=True):
    confirm_deletion(name, is_folder)

# Fonction de modification (stub à compléter)
def edit_favorite(name, is_folder):
    # Exemple simple : ouvrir une fenêtre pour modifier nom, lien/chemin, icône
    edit_win = ctk.CTkToplevel(app)
    edit_win.title(f"Modifier '{name}'")
    edit_win.geometry("400x350")

    ctk.CTkLabel(edit_win, text="Nom :").pack(pady=5)
    name_entry = ctk.CTkEntry(edit_win)
    name_entry.insert(0, name)
    name_entry.pack(pady=5)

    icon_path_var = tk.StringVar()
    icon_path_var.set(name)  # On suppose nom = icône associée (par défaut)

    def browse_icon():
        file_path = filedialog.askopenfilename(initialdir=icons_dir, filetypes=[("Images", "*.png;*.ico")])
        if file_path:
            icon_name = os.path.splitext(os.path.basename(file_path))[0]
            icon_path_var.set(icon_name)

    ctk.CTkButton(edit_win, text="Parcourir une icône…", command=browse_icon).pack(pady=5)
    ctk.CTkLabel(edit_win, textvariable=icon_path_var).pack(pady=5)

    if is_folder:
        ctk.CTkLabel(edit_win, text="Chemin du dossier :").pack(pady=5)
        path_entry = ctk.CTkEntry(edit_win)
        path_entry.insert(0, favorite_folders[name])
        path_entry.pack(pady=5)

        def confirm():
            new_name = name_entry.get().strip()
            new_path = path_entry.get().strip()
            if new_name and new_path:
                # Mise à jour du dictionnaire
                # Gestion renommage clé
                if new_name != name:
                    favorite_folders[new_name] = favorite_folders.pop(name)
                    # Renommer icône aussi si existant
                    old_icon = os.path.join(icons_dir, f"{name}.png")
                    new_icon = os.path.join(icons_dir, f"{new_name}.png")
                    if os.path.exists(old_icon):
                        os.rename(old_icon, new_icon)
                favorite_folders[new_name] = new_path
                # Copier ou renommer icône si modifiée
                icon_name = icon_path_var.get()
                if icon_name and icon_name != new_name:
                    source = os.path.join(icons_dir, f"{icon_name}.png")
                    dest = os.path.join(icons_dir, f"{new_name}.png")
                    if os.path.exists(source):
                        if os.path.exists(dest):
                            os.remove(dest)
                        os.rename(source, dest)
                save_json(folders_json, favorite_folders)
                refresh_favorites()
                edit_win.destroy()
    else:
        ctk.CTkLabel(edit_win, text="URL du site :").pack(pady=5)
        url_entry = ctk.CTkEntry(edit_win)
        url_entry.insert(0, favorite_websites[name])
        url_entry.pack(pady=5)

        def confirm():
            new_name = name_entry.get().strip()
            new_url = url_entry.get().strip()
            if new_name and new_url:
                if new_name != name:
                    favorite_websites[new_name] = favorite_websites.pop(name)
                    old_icon = os.path.join(icons_dir, f"{name}.png")
                    new_icon = os.path.join(icons_dir, f"{new_name}.png")
                    if os.path.exists(old_icon):
                        os.rename(old_icon, new_icon)
                favorite_websites[new_name] = new_url
                icon_name = icon_path_var.get()
                if icon_name and icon_name != new_name:
                    source = os.path.join(icons_dir, f"{icon_name}.png")
                    dest = os.path.join(icons_dir, f"{new_name}.png")
                    if os.path.exists(source):
                        if os.path.exists(dest):
                            os.remove(dest)
                        os.rename(source, dest)
                save_json(websites_json, favorite_websites)
                refresh_favorites()
                edit_win.destroy()

    ctk.CTkButton(edit_win, text="Valider", command=confirm).pack(pady=15)

# Actualisation favoris avec boutons modification et suppression
def refresh_favorites():
    for w in folder_frame.winfo_children():
        w.destroy()
    for w in web_frame.winfo_children():
        w.destroy()

    # Folders
    for name, path in favorite_folders.items():
        icon = get_custom_icon(name, is_folder=True) or default_icon

        frame = ctk.CTkFrame(folder_frame)
        frame.pack(fill="x", pady=4)

        # Bouton principal ouvrant dossier
        btn = ctk.CTkButton(frame, text=name, command=lambda p=path: open_folder(p), image=icon, compound="left")
        btn.pack(side="left", fill="x", expand=True)

        # Bouton supprimer
        del_btn = ctk.CTkButton(frame, text="✖", width=30, fg_color="red", hover_color="#aa0000",
                               command=lambda n=name: delete_favorite(n, is_folder=True))
        del_btn.pack(side="right", padx=5)

        
        # Bouton modifier (icone seule)
        mod_btn = ctk.CTkButton(frame, width=30, height=30, image=tools_icon, text="", fg_color="transparent",
                                hover_color="#005f99",
                                command=lambda n=name: edit_favorite(n, is_folder=True))
        mod_btn.pack(side="right", padx=(0, 5))


    # Websites
    for name, url in favorite_websites.items():
        icon = (get_custom_icon(name) or get_favicon_ctkimage(url) or get_custom_icon(name, is_web=True) or default_icon)

        frame = ctk.CTkFrame(web_frame)
        frame.pack(fill="x", pady=4)

        btn = ctk.CTkButton(frame, text=name, command=lambda u=url: open_website(u), image=icon, compound="left")
        btn.pack(side="left", fill="x", expand=True)

        mod_btn = ctk.CTkButton(frame, width=30, height=30, image=tools_icon, text="", fg_color="transparent",
                                hover_color="#005f99",
                                command=lambda n=name: edit_favorite(n, is_folder=False))
        mod_btn.pack(side="right", padx=(0, 5))

        del_btn = ctk.CTkButton(frame, text="✖", width=30, fg_color="red", hover_color="#aa0000",
                               command=lambda n=name: delete_favorite(n, is_folder=False))
        del_btn.pack(side="right", padx=5)

def save_json(path, data):
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Erreur sauvegarde JSON {path}: {e}")

def add_favorite():
    add_window = ctk.CTkToplevel(app)
    add_window.title("Ajouter un favori")
    add_window.geometry("400x350")  # un peu plus haut pour l'icône

    ctk.CTkLabel(add_window, text="Nom du favori :").pack(pady=5)
    name_entry = ctk.CTkEntry(add_window)
    name_entry.pack(pady=5)

    # Variable pour stocker le nom de l'icône choisie
    icon_name_var = tk.StringVar()
    icon_preview_label = ctk.CTkLabel(add_window, text="Aucune icône sélectionnée")
    icon_preview_label.pack(pady=5)

    def choose_icon():
        file_path = filedialog.askopenfilename(initialdir=icons_dir, filetypes=[("Images PNG", "*.png")])
        if file_path:
            basename = os.path.basename(file_path)
            icon_name_var.set(basename)
            # Afficher un aperçu de l'icône sélectionnée
            img = Image.open(file_path)
            img = img.resize((40, 40))
            icon_img = ctk.CTkImage(light_image=img, dark_image=img, size=(40, 40))
            icon_preview_label.configure(image=icon_img, text="")
            icon_preview_label.image = icon_img  # garder référence

    ctk.CTkButton(add_window, text="Choisir une icône", command=choose_icon).pack(pady=5)

    if showing_folders:
        ctk.CTkLabel(add_window, text="Chemin du dossier :").pack(pady=5)
        path_entry = ctk.CTkEntry(add_window)
        path_entry.pack(pady=5)

        def browse_folder():
            path = filedialog.askdirectory()
            if path:
                path_entry.delete(0, tk.END)
                path_entry.insert(0, path)

        ctk.CTkButton(add_window, text="Parcourir...", command=browse_folder).pack(pady=5)

        def confirm():
            name, path = name_entry.get().strip(), path_entry.get().strip()
            icon_filename = icon_name_var.get()
            if name and path:
                favorite_folders[name] = path

                # Copier l'icône sélectionnée dans icons_dir avec le nom du favori
                if icon_filename:
                    source_path = os.path.join(icons_dir, icon_filename)
                    dest_path = os.path.join(icons_dir, f"{name}.png")
                    if os.path.exists(source_path):
                        # Copie (ou écrase) l'icône sous le nom du favori
                        import shutil
                        shutil.copyfile(source_path, dest_path)

                save_json(folders_json, favorite_folders)
                refresh_favorites()
                add_window.destroy()

    else:
        ctk.CTkLabel(add_window, text="URL du site :").pack(pady=5)
        url_entry = ctk.CTkEntry(add_window)
        url_entry.pack(pady=5)

        def confirm():
            name, url = name_entry.get().strip(), url_entry.get().strip()
            icon_filename = icon_name_var.get()
            if name and url:
                favorite_websites[name] = url

                if icon_filename:
                    source_path = os.path.join(icons_dir, icon_filename)
                    dest_path = os.path.join(icons_dir, f"{name}.png")
                    if os.path.exists(source_path):
                        import shutil
                        shutil.copyfile(source_path, dest_path)

                save_json(websites_json, favorite_websites)
                refresh_favorites()
                add_window.destroy()

    ctk.CTkButton(add_window, text="Ajouter", command=confirm).pack(pady=15)


# Création fenêtre principale
app = ctk.CTk()
app.geometry("400x600")
app.title("Favoris Gestionnaire")

# Boutons thème et toggle dossier/web
top_frame = ctk.CTkFrame(app)
top_frame.pack(fill="x", pady=5)

theme_button = ctk.CTkButton(top_frame, text="Thème", command=switch_theme)
theme_button.pack(side="right", padx=10)

toggle_button = ctk.CTkButton(top_frame, text="Web", command=toggle_view)
toggle_button.pack(side="left", padx=10)

# AJOUT : bouton "Ajouter" centré juste sous top_frame

folder_frame = ctk.CTkScrollableFrame(app)
web_frame = ctk.CTkScrollableFrame(app)

fav_frame = ctk.CTkFrame(app)
fav_frame.pack(fill="x", padx=10, pady=5)
ctk.CTkButton(fav_frame, text="Ajouter un favori", command=add_favorite).pack()

showing_folders = True
update_view()

refresh_favorites()

app.mainloop()