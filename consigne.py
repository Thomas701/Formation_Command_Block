import os
import json

def remove_last_n_lines(file_path, n=3):
    """Supprime les n dernières lignes d'un fichier"""
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if len(lines) > n:
        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(lines[:-n])
    else:
        open(file_path, "w", encoding="utf-8").close()

def generate_mcfunction(title_file, level, x, y, z, rot_yaw, rot_pitch, tick_delay, gap, start_step, phrase, color, largeur, music):
    """
    Génère un fichier .mcfunction pour afficher du texte avec rotation et affichage progressif.

    rot_yaw : rotation horizontale (0f = nord, 90f = est, 180f = sud, 270f = ouest)
    rot_pitch : rotation verticale (0f = droit, 45f = incliné vers le bas)
    tick_delay : délai en ticks (20 = 1 seconde)
    gap : nombre de lettres ajoutées à chaque étape
    """
    folder = f"data/text_datapack/function/consignes"
    os.makedirs(folder, exist_ok=True)
    
    file_path = os.path.join(folder, f"consigne_{title_file}.mcfunction")

    if start_step > 0 and os.path.exists(file_path):
        remove_last_n_lines(file_path, 8 if music else 4)
        mode = "a"
    else:
        mode = "w"

    with open(file_path, mode, encoding="utf-8") as file:   
        if start_step == 0:
            file.write(f"execute if score CRunning lvl{level} matches 0 run execute positioned {x} {y} {z} run kill @e[type=minecraft:text_display,distance=..6]\n")
            file.write(f"execute if score CRunning lvl{level} matches 0 run scoreboard players set CRunning lvl{level} 1\n")      

        # Création du texte vide avec rotation personnalisée
        text_json = json.dumps({"text": ""})
        file.write(
            f"execute positioned {x} {y} {z} run summon minecraft:text_display "
            f"{x} {y} {z} {{text:{text_json}, Rotation:[{rot_yaw}f,{rot_pitch}f], line_width:{largeur}}}\n"
        )
        
        # Affichage progressif du texte (gap lettres par étape)
        for i in range(0, len(phrase), gap):
            text_part = phrase[:i+gap]
            step_index = start_step + i // gap  # étape correspondante
            file.write(
                f"execute positioned {x} {y} {z} run "
                f"execute if score step lvl{level} matches {step_index} "
                f"run data merge entity @e[type=minecraft:text_display,limit=1,sort=nearest] "
                f"{{text:{{\"text\":\"{text_part}\",\"color\":\"{color}\"}}, line_width:{largeur}}}\n"
            )

        # Planification de la suite
        total_steps = (len(phrase) + gap - 1) // gap  # nombre total d’étapes
        file.write(f"scoreboard players add step lvl{level} 1\n")
        file.write(f"execute if score step lvl{level} matches ..{start_step + total_steps} run schedule function text_datapack:consignes/consigne_{title_file} {tick_delay}t replace\n")
        if music:
            file.write(f"execute if score step lvl{level} matches {start_step + total_steps + 1} run execute as @a if score @s LEVEL matches {level} run stopsound @s block custom:audio1\n")
            file.write(f"execute if score step lvl{level} matches {start_step + total_steps + 1} run execute as @a if score @s LEVEL matches {level} run stopsound @s block custom:audio2\n")
            file.write(f"execute if score step lvl{level} matches {start_step + total_steps + 1} run execute as @a if score @s LEVEL matches {level} run stopsound @s block custom:audio3\n")
            file.write(f"execute if score step lvl{level} matches {start_step + total_steps + 1} run execute as @a if score @s LEVEL matches {level} run stopsound @s block custom:audio4\n")
        file.write(f"execute if score step lvl{level} matches {start_step + total_steps + 1} run scoreboard players set CRunning lvl{level} 0\n")
        file.write(f"execute if score step lvl{level} matches {start_step + total_steps + 1} run scoreboard players set step lvl{level} 0\n")

    print(f"Fichier généré : {file_path}")
    
    
    
# Paramètre	de la Fonction
#0      title_file	        Nom du fichier  
# 1	    level	            Numéro du niveau
# 2	    x	                Position X
# 3	    y	                Position Y
# 4	    z	                Position Z
# 5	    rot_yaw	            Rotation horizontale
# 6	    rot_pitch	        Rotation verticale
# 7	    tick_delay	        Délai entre chaque étape
# 8	    gap	                Nombre de lettres ajoutées à chaque étape
# 9	    start_step	        Index de départ
# 10	phrase	        Texte à afficher
# 11	color	        Couleur du texte
# 12	largeur	        Largeur du texte
# 13    music           stopper la musique à la fin de l'écriture

# Largeur du texte (ex: 200 pixels)
l1 = 200
l2 = 300

# --- LVL0 ---
p1 = "Niveau 0"
p2 = "Consigne :"
p3 = "Casser un command block est vite arrivé. Afin d eviter de perdre involontairement des précieuses commandes, il est fortement conseillé, lorsque vous développez en commande block de conserver une épée en main. En tenant une épée, vous ne pouvez pas casser de block. Votre objectif consiste à tenir une épée en main."

generate_mcfunction(0, 0, 0, 95.5, 3.99, 180, 0, 1, 1, 0, p1, "#FFFF55", l1, True)
generate_mcfunction(0, 0, 1, 95, 3.99, 180, 0, 1, 1, len(p1), p2, "#1dab23", l1, True)
generate_mcfunction(0, 0, 0, 92.5, 3.99, 180, 0, 1, 2, len(p1) + len(p2), p3, "#FFFFFF", l1, True)

# --- LVL1 ---
p1 = "Niveau 1"
p2 = "Consigne :"
p3 = "Ouvrez les paramètres de minecraft, allez dans Option, puis Control et enfin, mettez 'Opération Item Tab' sur ON. Dès lors, vous verrez en mode créatif, dans votre inventaire en bas à droite 'Operator Utilities', prenez les trois commandes blocks de couleurs différentes et posez les sur les blocks de laine correspondants."

generate_mcfunction(1, 1, 12, 95.5, 3.99, 180, 0, 1, 1, 0, p1, "#FFFF55", l1, True)
generate_mcfunction(1, 1, 13, 95, 3.99, 180, 0, 1, 1, len(p1), p2, "#1dab23", l1, True)
generate_mcfunction(1, 1, 12, 92.5, 3.99, 180, 0, 1, 2, len(p1) + len(p2), p3, "#FFFFFF", l1, True)

# --- LVL2 ---
p1 = "Niveau 2"
p2 = "Consigne :"
p3 = "Si vous écrivez une commande dans le chat, les flèches haut/bas de votre clavier vous permettent de parcourir vos anciennes commandes, utile pour réutiliser une de vos précédentes commandes. La touche 'Tab' permet de compléter automatiquement une commande en cours d'écriture, elle vous aide à rédiger vos commandes. L'objectif est de remplacer les deux blocks de laine rouge par de la pierre ('stone' en anglais) à l'aide de la commande /setblock."
p4 = "/setblock <x> <y> <z> minecraft:<nom_du_block>"

generate_mcfunction(2, 2, 24, 96.5, 3.99, 180, 0, 1, 1, 0, p1, "#FFFF55", l1, True)
generate_mcfunction(2, 2, 25, 96, 3.99, 180, 0, 1, 1, len(p1), p2, "#1dab23", l1, True)
generate_mcfunction(2, 2, 24, 92.5, 3.99, 180, 0, 1, 2, len(p1) + len(p2), p3, "#FFFFFF", l1, True)
generate_mcfunction(2.1, 2, 24, 92.5, -2.99, 0, 0, 1, 1, 0, p4, "#DACF00", l2, True)

# --- LVL3 ---
p1 = "Niveau 3"
p2 = "Consigne :"
p3 = "Allez dans 'Option' puis 'Control' puis 'Key Binds' vérifiez que la touche assignées à 'Pick Block' est bien la touche 'Middle Click' (molette de la souris). En mode créatif, cette touche permet de récupérer le block que vous regardez dans votre inventaire. Cependant si vous effectuez ce geste sur un commande block vous ne récupérez pas le contenant de ce dernier. Le command block récupéré sera 'vide' en le posant. Pour récupérer le block + son contenant, faites CTRL + Clic molette. Votre objectif est de récupérer le command block orange disponible avec son contenant et de le poser sur le block 'cible' sur le sol."

generate_mcfunction(3, 3, 36, 97.5, 3.99, 180, 0, 1, 1, 0, p1, "#FFFF55", l1, True)
generate_mcfunction(3, 3, 37, 97, 3.99, 180, 0, 1, 1, len(p1), p2, "#1dab23", l1, True)
generate_mcfunction(3, 3, 36, 92.25, 3.99, 180, 0, 1, 3, len(p1) + len(p2), p3, "#FFFFFF", l1, True)