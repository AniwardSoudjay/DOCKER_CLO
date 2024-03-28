# Étape 1: Création de l'image de base
FROM debian:latest as base

# Installation des dépendances communes
RUN apt-get update && apt-get install -y python3 python3-pip curl
RUN pip3 install --no-cache-dir requests

# Étape 2: Image pour les tests d'authentification
FROM base as authentication

WORKDIR /my_project/

# Copie des fichiers nécessaires
COPY my_project/ /my_project/
RUN mkdir -p /my_log/

CMD ["python3", "main.py"]

# Étape 3: Image pour les tests d'autorisation
FROM base as authorization

WORKDIR /my_project/

# Copie des fichiers nécessaires
COPY my_project/ /my_project/
RUN mkdir -p /my_log/

CMD ["python3", "main.py"]

# Étape 4: Image pour les tests de contenu
FROM base as content

WORKDIR /my_project/

# Copie des fichiers nécessaires
COPY my_project/ /my_project/
RUN apt-get update && apt-get install -y curl
RUN mkdir -p /my_project/log/

CMD ["python3", "main.py"]
