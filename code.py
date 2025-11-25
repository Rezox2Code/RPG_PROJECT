import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class Character:
    def __init__(self, name, description, stats):
        self.name = name
        self.description = description
        self.stats = stats

class RPGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sélecteur Personnage RPG")
        self.root.geometry("800x650")
        self.root.configure(bg="#1E1E2F")

        self.image_folder = "images"
        self.characters = self.load_characters()
        self.specializations = ["La Cage", "La Fusion", "Le Bourré", "La Sarbacane", "La Magie Noire", "L'Exorcisme"]
        self.selected_char = 0

        self.details_var = tk.StringVar()
        self.spec_var = tk.StringVar(value=self.specializations[0])

        self.skill_points = 10
        self.skill_tree_levels = [0, 0, 0, 0]
        self.max_skill_level = 4

        self.skill_image_patterns = [
            "{level}_lvl_attaque.png",
            "{level}_lvl_shield.png",
            "{level}_lvl_speed.png",
            "{level}_lvl_health.png",
        ]

        self.skill_images_cache = []
        self.show_select_screen()

    def load_characters(self):
        descriptions = {
            "Fleuriste": {"Compétence": "Bouquet explosif", "Buff": "Parfum apaisant", "Nerf": "Allergies"},
            "Le Pape": {"Compétence": "Anathème", "Buff": "Bénédiction", "Nerf": "Dogme rigide"},
            "CM": {"Compétence": "Bad Buzz", "Buff": "Post Viral", "Nerf": "Burn-out"},
            "Cuisinier": {"Compétence": "Marmite destructrice", "Buff": "Plat revigorant", "Nerf": "Surcuisson"},
            "Agent Sécurité": {"Compétence": "Contrôle musclé", "Buff": "Armure anti-émeute", "Nerf": "Procédure admin"},
            "Huissier": {"Compétence": "Saisie immédiate", "Buff": "Avis de passage", "Nerf": "Papiers manquants"},
            "Procureur": {"Compétence": "Réquisitoire final", "Buff": "Pièce à conviction", "Nerf": "Objection !"},
            "Dragon": {"Compétence": "Souffle de feu", "Buff": "Écailles titanesques", "Nerf": "Cupidité"},
        }

        stats = {
            "Fleuriste": {"Attaque": 40, "Défense": 30, "PV": 50, "Vitesse": 60},
            "Le Pape": {"Attaque": 70, "Défense": 60, "PV": 80, "Vitesse": 30},
            "CM": {"Attaque": 45, "Défense": 20, "PV": 40, "Vitesse": 75},
            "Cuisinier": {"Attaque": 65, "Défense": 50, "PV": 70, "Vitesse": 35},
            "Agent Sécurité": {"Attaque": 55, "Défense": 80, "PV": 90, "Vitesse": 20},
            "Huissier": {"Attaque": 60, "Défense": 40, "PV": 55, "Vitesse": 50},
            "Procureur": {"Attaque": 80, "Défense": 50, "PV": 60, "Vitesse": 45},
            "Dragon": {"Attaque": 95, "Défense": 90, "PV": 120, "Vitesse": 70},
        }

        return [Character(name, descriptions[name], stats[name]) for name in descriptions]

    # Écran 1 : sélection personnage
    def show_select_screen(self):
        self.clear_screen()

        self.center_frame = tk.Frame(self.root, bg="#2A2A3D")
        self.center_frame.place(relx=0.5, rely=0.35, anchor="center", width=400, height=350)

        self.label_name = tk.Label(self.center_frame, text="", font=("Arial", 16, "bold"), bg="#2A2A3D", fg="white")
        self.label_name.pack(pady=10)

        self.label_image = tk.Label(self.center_frame, bg="#2A2A3D")
        self.label_image.pack(pady=5)

        self.label_details = tk.Label(
            self.center_frame, textvariable=self.details_var, font=("Arial", 11),
            bg="#2A2A3D", fg="white", justify="left"
        )
        self.label_details.pack()

        self.dropdown = ttk.Combobox(self.center_frame, textvariable=self.spec_var,
                                     values=self.specializations, state="readonly")
        self.dropdown.pack(pady=10)

        tk.Button(self.root, text="Valider", bg="#2ECC71", font=("Arial", 13, "bold"),
                  command=self.show_skills_screen).place(relx=0.5, rely=0.65, anchor="center")

        tk.Button(self.root, text="⬅️", font=("Arial", 14), command=self.prev_char).place(x=100, y=250)
        tk.Button(self.root, text="➡️", font=("Arial", 14), command=self.next_char).place(x=650, y=250)

        self.update_display()

    # Écran 2 : Arbre compétences
    def show_skills_screen(self):
        self.clear_screen()

        char = self.characters[self.selected_char]
        tk.Label(self.root,
                 text=f"Personnage : {char.name} | Spécialisation : {self.spec_var.get()}",
                 font=("Arial", 14, "bold"), fg="#00FFAA", bg="#1E1E2F").pack(pady=15)

        self.skill_label = tk.Label(self.root,
                                    text=f"Points restants : {self.skill_points}",
                                    font=("Arial", 13), fg="yellow", bg="#1E1E2F")
        self.skill_label.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 13), fg="white", bg="#1E1E2F")
        self.result_label.pack(pady=5)

        self.canvas = tk.Canvas(self.root, width=700, height=400, bg="#1E1E2F", highlightthickness=0)
        self.canvas.pack(pady=20)

        tk.Button(self.root, text="Valider", bg="#2ECC71", font=("Arial", 12, "bold"),
                  command=self.validate_stats).pack(side=tk.LEFT, padx=50)
        tk.Button(self.root, text="Réinitialiser", bg="#E74C3C", font=("Arial", 12, "bold"),
                  command=self.reset_skills).pack(side=tk.RIGHT, padx=50)

        self.draw_skill_tree()

    def draw_skill_tree(self):
        self.canvas.delete("all")
        self.skill_images_cache = []

        center_x = 350
        spacing_x = 150
        spacing_y = 75

        for col in range(4):
            x = center_x + (col - 1.5) * spacing_x
            for lvl_index in range(self.max_skill_level):
                lvl = lvl_index + 1
                y = 80 + lvl_index * spacing_y

                img_file = (
                    self.skill_image_patterns[col].format(level=lvl)
                    if lvl <= self.skill_tree_levels[col] else "locked.png"
                )

                filepath = os.path.join(self.image_folder, img_file)
                if not os.path.exists(filepath):
                    filepath = os.path.join(self.image_folder, "default.png")

                pil_img = Image.open(filepath).resize((55, 55))
                img = ImageTk.PhotoImage(pil_img)
                self.skill_images_cache.append(img)

                img_id = self.canvas.create_image(x, y, image=img)

                percent = lvl * 25
                self.canvas.create_text(x, y + 40, text=f"{percent}%", fill="white", font=("Arial", 10))

                self.canvas.tag_bind(img_id, "<Button-1>", lambda e, c=col, l=lvl: self.upgrade_skill(c, l))

    def upgrade_skill(self, col, lvl):
        cost = lvl
        if self.skill_points >= cost and self.skill_tree_levels[col] < lvl:
            self.skill_points -= cost
            self.skill_tree_levels[col] = lvl
            self.skill_label.config(text=f"Points restants : {self.skill_points}")
            self.draw_skill_tree()

    def validate_stats(self):
        char = self.characters[self.selected_char]
        result = f"Stats finales de {char.name} :\n"
        categories = ["Attaque", "Défense", "Vitesse", "PV"]

        for i, stat in enumerate(categories):
            bonus = char.stats[stat] * (self.skill_tree_levels[i] * 0.25)
            result += f"• {stat} : {char.stats[stat]} (+{int(bonus)})\n"

        self.result_label.config(text=result)

    def reset_skills(self):
        self.skill_tree_levels = [0, 0, 0, 0]
        self.skill_points = 10
        self.skill_label.config(text=f"Points restants : {self.skill_points}")
        self.result_label.config(text="")
        self.draw_skill_tree()

    def prev_char(self):
        self.selected_char = (self.selected_char - 1) % len(self.characters)
        self.update_display()

    def next_char(self):
        self.selected_char = (self.selected_char + 1) % len(self.characters)
        self.update_display()

    def update_display(self):
        char = self.characters[self.selected_char]
        self.details_var.set(
            f"Compétence : {char.description['Compétence']}\n"
            f"Buff : {char.description['Buff']}\n"
            f"Nerf : {char.description['Nerf']}\n\n"
            f"Stats :\n"
            f"  • Attaque : {char.stats['Attaque']}\n"
            f"  • Défense : {char.stats['Défense']}\n"
            f"  • PV : {char.stats['PV']}\n"
            f"  • Vitesse : {char.stats['Vitesse']}"
        )

        img = self.load_image(char.name)
        if img:
            self.label_image.config(image=img)
            self.label_image.image = img

        self.label_name.config(text=char.name)

    def load_image(self, char_name):
        filepath = os.path.join(self.image_folder, f"{char_name}.png")
        if not os.path.exists(filepath):
            filepath = os.path.join(self.image_folder, "locked.png")
        return ImageTk.PhotoImage(Image.open(filepath))

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RPGUI(root)
    root.mainloop()
