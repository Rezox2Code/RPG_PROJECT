import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class Character:
    def __init__(self, name, description, stats):
        self.name = name
        self.description = description
        self.stats = stats  # Nouveau dictionnaire de stats


class RPGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sélecteur Personnage RPG")
        self.root.geometry("750x550")
        self.root.configure(bg="#1E1E2F")

        self.image_folder = "images"

        self.characters = self.load_characters()
        self.specializations = ["La Cage", "La Fusion", "Le Bourré", "La Sarbacane", "La Magie Noire", "L'Exorcisme"]
        self.selected_char = 0

        self.details_var = tk.StringVar()
        self.spec_var = tk.StringVar(value=self.specializations[0])

        self.setup_ui()
        self.update_display()

    def load_characters(self):
        descriptions = {
            "Fleuriste": {
                "Compétence": "Bouquet explosif (dégâts continus)",
                "Buff": "Parfum apaisant (soin équipe, 3 tours)",
                "Nerf": "Allergies (-10% précision)"
            },
            "Le Pape": {
                "Compétence": "Anathème (gros dégâts)",
                "Buff": "Bénédiction (+attaque & défense)",
                "Nerf": "Dogme rigide (inutilisable <20% PV)"
            },
            "CM": {
                "Compétence": "Bad Buzz (provocation + debuff)",
                "Buff": "Post Viral (boost aléatoire)",
                "Nerf": "Burn-out (-15% vitesse <50% PV)"
            },
            "Cuisinier": {
                "Compétence": "Marmite de destruction (zone)",
                "Buff": "Plat revigorant (+PV max)",
                "Nerf": "Surcuisson (risque auto-brûlure)"
            },
            "Agent Sécurité": {
                "Compétence": "Contrôle musclé (stun 1 tour)",
                "Buff": "Armure anti-émeute (tank)",
                "Nerf": "Procédure admin (perd un tour)"
            },
            "Huissier": {
                "Compétence": "Saisie immédiate (retire buff + dégâts)",
                "Buff": "Avis de passage (+défense/précision)",
                "Nerf": "Papiers manquants (20% échec)"
            },
            "Procureur": {
                "Compétence": "Réquisitoire final (gros dégâts)",
                "Buff": "Pièce à Conviction (+attaque si debuff)",
                "Nerf": "Objection ! (-20% attaque si allié K.O)"
            },
            "Dragon": {
                "Compétence": "Souffle incendiaire (énorme zone)",
                "Buff": "Écailles Titan (-dégâts)",
                "Nerf": "Cupidité (perd un tour si objet rare)"
            },
        }

        # stats chiffrées
        stats = {
            "Fleuriste":     {"Attaque": 40, "Défense": 30, "PV": 50, "Vitesse": 60},
            "Le Pape":       {"Attaque": 70, "Défense": 60, "PV": 80, "Vitesse": 30},
            "CM":            {"Attaque": 45, "Défense": 20, "PV": 40, "Vitesse": 75},
            "Cuisinier":     {"Attaque": 65, "Défense": 50, "PV": 70, "Vitesse": 35},
            "Agent Sécurité":{"Attaque": 55, "Défense": 80, "PV": 90, "Vitesse": 20},
            "Huissier":      {"Attaque": 60, "Défense": 40, "PV": 55, "Vitesse": 50},
            "Procureur":     {"Attaque": 80, "Défense": 50, "PV": 60, "Vitesse": 45},
            "Dragon":        {"Attaque": 95, "Défense": 90, "PV": 120, "Vitesse": 70},
        }

        return [Character(name, descriptions[name], stats[name]) for name in descriptions]

    def setup_ui(self):
        self.center_frame = tk.Frame(self.root, bg="#2A2A3D")
        self.center_frame.place(relx=0.5, rely=0.4, anchor="center", width=400, height=380)

        self.label_name = tk.Label(self.center_frame, text="", font=("Arial", 16, "bold"), bg="#2A2A3D", fg="white")
        self.label_name.pack(pady=10)

        self.label_image = tk.Label(self.center_frame, bg="#2A2A3D")
        self.label_image.pack(pady=5)

        self.label_details = tk.Label(self.center_frame, textvariable=self.details_var, font=("Arial", 11),
                                      bg="#2A2A3D", fg="white", justify="left")
        self.label_details.pack()

        self.dropdown = ttk.Combobox(self.center_frame, textvariable=self.spec_var, values=self.specializations, state="readonly")
        self.dropdown.pack(pady=10)

        self.button_validate = tk.Button(self.center_frame, text="Valider", bg="#2ECC71",
                                         font=("Arial", 12, "bold"), command=self.validate)
        self.button_validate.pack(pady=10)

        tk.Button(self.root, text="⬅️", font=("Arial", 14), command=self.prev_char).place(x=100, y=250)
        tk.Button(self.root, text="➡️", font=("Arial", 14), command=self.next_char).place(x=650, y=250)

        self.result = tk.Label(self.root, text="", font=("Arial", 12, "bold"),
                               fg="#00BFFF", bg="#1E1E2F")
        self.result.pack(side="bottom", pady=20)

    def load_image(self, char_name):
        filepath = os.path.join(self.image_folder, f"{char_name}.png")
        if not os.path.exists(filepath):
            filepath = os.path.join(self.image_folder, "default.png")
        try:
            img = Image.open(filepath)
            return ImageTk.PhotoImage(img)
        except:
            return None

    def update_display(self):
        char = self.characters[self.selected_char]

        # Affichage avec stats
        self.details_var.set(
            f"Compétence : {char.description['Compétence']}\n"
            f"Buff : {char.description['Buff']}\n"
            f"Nerf : {char.description['Nerf']}\n\n"
            f"Stats :\n"
            f"   • Attaque : {char.stats['Attaque']}\n"
            f"   • Défense : {char.stats['Défense']}\n"
            f"   • PV : {char.stats['PV']}\n"
            f"   • Vitesse : {char.stats['Vitesse']}"
        )

        self.label_name.config(text=char.name)
        img = self.load_image(char.name)
        if img:
            self.label_image.config(image=img)
            self.label_image.image = img
        else:
            self.label_image.config(text="Image non trouvée")

    def prev_char(self):
        self.selected_char = (self.selected_char - 1) % len(self.characters)
        self.update_display()

    def next_char(self):
        self.selected_char = (self.selected_char + 1) % len(self.characters)
        self.update_display()

    def validate(self):
        chosen = self.characters[self.selected_char].name
        self.result.config(text=f"Tu as choisi : {chosen} | Spécialisation : {self.spec_var.get()}")


if __name__ == "__main__":
    root = tk.Tk()
    app = RPGUI(root)
    root.mainloop()
