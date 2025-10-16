import os

def generate_datapack_file(n: int):
    # Définir le chemin du dossier et du fichier
    folder_path = "./data/text_datapack/function"
    file_path = os.path.join(folder_path, "load.mcfunction")

    # Créer le dossier si besoin
    os.makedirs(folder_path, exist_ok=True)

    # Contenu de base
    header = "############# Formation Command Block Data Pack ############\n\n"
    header += "scoreboard objectives add LEVEL dummy\n\n"

    # Génération du contenu pour chaque niveau
    levels_content = ""
    for i in range(n + 1):
        levels_content += f"############ --- LVL_{i} --- ############ \n\n"
        levels_content += f"scoreboard objectives add lvl{i} dummy\n"
        levels_content += f"scoreboard players set step lvl{i} 0\n"
        levels_content += f"scoreboard players set CRunning lvl{i} 0\n"
        levels_content += f"scoreboard players set validate lvl{i} 0\n"
        levels_content += f"scoreboard players set timeTesting lvl{i} 0\n"
        levels_content += f"scoreboard players set modulo lvl{i} 1\n"
        levels_content += f"scoreboard players set temp lvl{i} 1\n\n"

    # Message final
    footer = 'tellraw @a {"text": "Formation command block data pack loaded!", "color": "gold"}\n'

    # Écriture du fichier (remplacement s’il existe)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(header + levels_content + footer)

    print(f"✅ Fichier généré avec succès : {file_path}")

# Exemple d'utilisation :
generate_datapack_file(50)
