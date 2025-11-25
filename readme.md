# Snake — Pygame

Un petit jeu Snake en Python (Pygame), structuré pour apprendre : grille 20x20, collisions fiables, nourriture alignée, barre latérale (score / meilleur score) et redémarrage après game-over.

V1:
https://github.com/user-attachments/assets/d351cace-28fd-42ec-aaaf-10af3dfbd254


## Prérequis

- Python 3.10+
- Pygame (installé via `requirements.txt`)

## Installation (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Lancer le jeu

```powershell
python main.py
```

## Contrôles

- Flèches: déplacer le serpent
- `R`: redémarrer après un game-over

## Règles & score

- Le serpent se déplace case par case (grille 20x20).
- Manger une pomme allonge le serpent et augmente le score.
- Collision avec soi-même ou les bords (zone de jeu à gauche) = game-over.
- Le meilleur score est persisté dans `best_score.txt` (créé automatiquement).
