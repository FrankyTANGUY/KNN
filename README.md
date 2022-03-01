# KNN
## Algorithme de KNN from Scratch/avec Sklearn

## Partie 1 : Base de données, Analyse, Prétraitement et Préparation 

- Importation d'un **dataset** créé par la promotion.
- Analyse.
- Prétraitement : correction des valeurs **manquantes et erronées**.
- Préparation : encodage des valeurs qualitatives (**LabelEncoder**), mise en forme pour le modèle.

## Partie 2 : Développement et entraînement d’un modèle KNN 

- Fonction pour **calculer la distance entre 2 points** (3 métriques : euclidienne, Manhattan, Minkowski)
- Fonction pour **calculer les plus proches voisins** et **prédire la classe**.
- Affichage du **score en fonction de k**, **validation croisée**.
- Utilisation de **GridSearchCv** pour choisir les paramètres optimaux.

## Partie 3 : Mettre en place la solution dans l’application de test de personnalité

- Enregistrement du modèle optimal avec **joblib**.
