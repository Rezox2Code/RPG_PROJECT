import tkinter as a
from tkinter import ttk as b
from PIL import Image as c, ImageTk as d
import os as e

class A:
    def __init__(s, n, d, t): s.n, s.d, s.t = n, d, t

class B:
    def __init__(s, r):
        s.R = r
        r.title("Sélécteur")
        r.geometry("800x650")
        r.configure(bg="#1E1E2F")
        s.F, s.C, s.S = "images", s._(), ["La Cage", "La Fusion", "Le Bourré", "La Sarbacane", "La Magie Noire", "L'Exorcisme"]
        s.I = 0
        s.V = a.StringVar()
        s.P = a.StringVar(value=s.S[0])
        s.K = 10
        s.M = [0]*4
        s.X = 4
        s.Y = ["{level}_lvl_attaque.png", "{level}_lvl_shield.png", "{level}_lvl_speed.png", "{level}_lvl_health.png"]
        s.Z = []
        s._1()

    def _(s):
        D = {"Fleuriste": {"Compétence":"Bouquet explosif","Buff":"Parfum apaisant","Nerf":"Allergies"},
             "Le Pape": {"Compétence":"Anathème","Buff":"Bénédiction","Nerf":"Dogme rigide"},
             "CM": {"Compétence":"Bad Buzz","Buff":"Post Viral","Nerf":"Burn-out"},
             "Cuisinier": {"Compétence":"Marmite destructrice","Buff":"Plat revigorant","Nerf":"Surcuisson"},
             "Agent Sécurité": {"Compétence":"Contrôle musclé","Buff":"Armure anti-émeute","Nerf":"Procédure admin"},
             "Huissier": {"Compétence":"Saisie immédiate","Buff":"Avis de passage","Nerf":"Papiers manquants"},
             "Procureur": {"Compétence":"Réquisitoire final","Buff":"Pièce à conviction","Nerf":"Objection !"},
             "Dragon": {"Compétence":"Souffle de feu","Buff":"Écailles titanesques","Nerf":"Cupidité"}}
        T = {"Fleuriste":{"Attaque":40,"Défense":30,"PV":50,"Vitesse":60},
             "Le Pape":{"Attaque":70,"Défense":60,"PV":80,"Vitesse":30},
             "CM":{"Attaque":45,"Défense":20,"PV":40,"Vitesse":75},
             "Cuisinier":{"Attaque":65,"Défense":50,"PV":70,"Vitesse":35},
             "Agent Sécurité":{"Attaque":55,"Défense":80,"PV":90,"Vitesse":20},
             "Huissier":{"Attaque":60,"Défense":40,"PV":55,"Vitesse":50},
             "Procureur":{"Attaque":80,"Défense":50,"PV":60,"Vitesse":45},
             "Dragon":{"Attaque":95,"Défense":90,"PV":120,"Vitesse":70}}
        return [A(x, D[x], T[x]) for x in D]

    def _1(s):
        s._C()
        q = a.Frame(s.R, bg="#2A2A3D")
        q.place(relx=.5, rely=.35, anchor="center", width=400, height=350)
        s.h = a.Label(q, font=("Arial",16,"bold"), bg="#2A2A3D", fg="white"); s.h.pack(pady=10)
        s.i = a.Label(q, bg="#2A2A3D"); s.i.pack(pady=5)
        a.Label(q, textvariable=s.V, font=("Arial",11), bg="#2A2A3D", fg="white", justify="left").pack()
        b.Combobox(q, textvariable=s.P, values=s.S, state="readonly").pack(pady=10)
        a.Button(s.R, text="Valider", bg="#2ECC71", font=("Arial",13,"bold"), command=s._2).place(relx=.5, rely=.65, anchor="center")
        a.Button(s.R, text="⬅️", font=("Arial",14), command=lambda:s._S(-1)).place(x=100, y=250)
        a.Button(s.R, text="➡️", font=("Arial",14), command=lambda:s._S(1)).place(x=650, y=250)
        s._D()

    def _2(s):
        s._C(); C=s.C[s.I]
        a.Label(s.R, text=f"Perso : {C.n} | Spec : {s.P.get()}", font=("Arial",14,"bold"), fg="#00FFAA", bg="#1E1E2F").pack(pady=15)
        s.x = a.Label(s.R, text=f"Points : {s.K}", font=("Arial",13), fg="yellow", bg="#1E1E2F"); s.x.pack(pady=10)
        s.y = a.Label(s.R, text="", font=("Arial",13), fg="white", bg="#1E1E2F"); s.y.pack(pady=5)
        s.z = a.Canvas(s.R, width=700, height=400, bg="#1E1E2F", highlightthickness=0); s.z.pack(pady=20)
        a.Button(s.R, text="✔", bg="#2ECC71", font=("Arial",12,"bold"), command=s._3).pack(side="left", padx=50)
        a.Button(s.R, text="♻", bg="#E74C3C", font=("Arial",12,"bold"), command=s._4).pack(side="right", padx=50)
        s._T()

    def _T(s):
        s.z.delete("all"); s.Z=[]
        for c in range(4):
            X=350+(c-1.5)*150
            for j in range(s.X):
                L=j+1; Y=80+j*75
                f=s.Y[c].format(level=L) if L<=s.M[c] else "locked.png"
                P=e.path.join(s.F, f)
                if not e.path.exists(P): P=e.path.join(s.F,"default.png")
                I=d(c.open(P).resize((55,55))); s.Z.append(I)
                i=s.z.create_image(X,Y,image=I)
                s.z.create_text(X, Y+40, text=f"{L*25}%", fill="white", font=("Arial",10))
                if L==s.M[c]+1:
                    s.z.tag_bind(i, "<Button-1>", lambda E, cc=c, ll=L: s._5(cc,ll))

    def _5(s, c, l):
        if s.K>=l and s.M[c]<l:
            s.K-=l; s.M[c]=l
            s.x.config(text=f"Points : {s.K}")
            s._T()

    def _3(s):
        C=s.C[s.I]; r=""; A=["Attaque","Défense","Vitesse","PV"]
        for i, x in enumerate(A):
            r+=f"{x} : {C.t[x]} (+{int(C.t[x]*(s.M[i]*0.25))})\n"
        s.y.config(text=r)

    def _4(s): s.M=[0]*4; s.K=10; s.x.config(text=f"Points : {s.K}"); s.y.config(text=""); s._T()

    def _S(s, d): s.I=(s.I+d)%len(s.C); s._D()

    def _D(s):
        C=s.C[s.I]
        s.V.set(f"Compétence : {C.d['Compétence']}\nBuff : {C.d['Buff']}\nNerf : {C.d['Nerf']}\n\nStats:\n"
                f"Att : {C.t['Attaque']}\nDef : {C.t['Défense']}\nPV : {C.t['PV']}\nVit : {C.t['Vitesse']}")
        p=e.path.join(s.F, f"{C.n}.png")
        if not e.path.exists(p): p=e.path.join(s.F,"locked.png")
        im=d(c.open(p)); s.i.config(image=im); s.i.image=im
        s.h.config(text=C.n)

    def _C(s):
        for w in s.R.winfo_children(): w.destroy()

if __name__=="__main__":
    r=a.Tk();B(r);r.mainloop()
