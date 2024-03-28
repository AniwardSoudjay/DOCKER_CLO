#!/bin/bash

# Chemin absolu du script 
SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
echo "Chemin du script : ${SCRIPT_PATH}"

# Vérifier si le répertoire du projet existe
PROJECT_PATH="/home/ubuntu/my_project"
if [ ! -d "$PROJECT_PATH" ]; then
    echo "Le répertoire du projet '$PROJECT_PATH' n'existe pas. Veuillez vérifier le chemin."
    exit 1
fi

# Nom du conteneur de l'API dans une variable d'environnement
export api_name="fastapi"

# Valeur de la variable LOG (1 pour enregistrer)
export LOG=1

# Phrases pour Alice et Bob
export pos_sentence="life is beautiful"
export neg_sentence="that sucks"

# Lancement du docker-compose 
cd "$PROJECT_PATH" || exit
if docker-compose up -d; then
    echo "Docker-compose lancé avec succès."
else
    echo "Erreur lors du lancement de docker-compose. Veuillez vérifier les erreurs ci-dessus."
    exit 1
fi

# restart 
docker-compose restart

# Revenir au répertoire d'origine (pour éviter de modifier le répertoire de travail du shell)
cd - || exit

# Supprimer les variables d'environnement
# unset api_name
# unset LOG
# unset pos_sentence
# unset neg_sentence
