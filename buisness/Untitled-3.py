class Eleve:
    def __init__(self, capacite, incitation):
        self.capacite = capacite
        self.incitation = incitation

    def calculer_valeur(self, k):
        return k * self.capacite * self.incitation


# Création d'instances d'élèves avec différentes capacités et incitations
eleve1 = Eleve(0.8, 0.9)
eleve2 = Eleve(0.6, 0.7)
eleve3 = Eleve(0.9, 0.5)

# Définition de la constante k pour ajuster l'importance relative des facteurs
k = 2.0

# Calcul de la valeur pour chaque élève
valeur_eleve1 = eleve1.calculer_valeur(k)
valeur_eleve2 = eleve2.calculer_valeur(k)
valeur_eleve3 = eleve3.calculer_valeur(k)

# Affichage des résultats
print("Valeur de l'élève 1 :", valeur_eleve1)
print("Valeur de l'élève 2 :", valeur_eleve2)
print("Valeur de l'élève 3 :", valeur_eleve3)


def calculer_chute_bulle_speculative(F, P, D, C):
    # Développement du facteur F
    facteurs_F = []  # Liste pour stocker les différents facteurs F
    facteurs_F.append("Niveau des taux d'intérêt")  # Exemple de facteur F
    facteurs_F.append("Inflation")  # Exemple de facteur F
    facteurs_F.append("Politiques monétaires")  # Exemple de facteur F

    # Développement du facteur P
    etudes_personne = []  # Liste pour stocker les différentes études menées par la personne
    etudes_personne.append("Expérience")  # Exemple d'étude menée par la personne
    etudes_personne.append("Compétences")  # Exemple d'étude menée par la personne
    etudes_personne.append("Connaissances")  # Exemple d'étude menée par la personne

    # Développement du facteur D
    credits_marges = []  # Liste pour stocker les différents crédits et marges de stock options
    credits_marges.append("Quantité de crédit disponible sur le marché")  # Exemple de crédit/marge
    credits_marges.append("Utilisation des marges de stock options")  # Exemple de crédit/marge

    # Développement du facteur C
    capacite_trading = []  # Liste pour stocker les différents éléments liés à la capacité de trading
    capacite_trading.append("Gestion active des investissements")  # Exemple d'élément de capacité de trading
    capacite_trading.append("Réaction aux signaux du marché")  # Exemple d'élément de capacité de trading
    capacite_trading.append("Prise de décisions éclairées")  # Exemple d'élément de capacité de trading

    # Calcul de la chute de bulle spéculative
    chute_bulle_speculative = (F * P) / (D * C)
    return chute_bulle_speculative

# Exemple d'utilisation avec des valeurs spécifiques
facteurs_F = 0.8
probabilite_P = 0.6
credits_marges_D = 10000
capacite_trading_C = 500

resultat = calculer_chute_bulle_speculative(facteurs_F, probabilite_P, credits_marges_D, capacite_trading_C)
print("Chute de bulle spéculative :", resultat)


class Eleve:
    def __init__(self, capacite, incitation):
        self.capacite = capacite
        self.incitation = incitation

    def calculer_valeur(self, k):
        return k * self.capacite * self.incitation


def calculer_valeur_enseignement(C, A, R, P):
    valeur = (C * A * R) / P
    return valeur


def calculer_chute_bulle_speculative(F, P, D, C):
    chute = (F * P) / (D * C)
    return chute


# Demande des valeurs des facteurs pour l'enseignement
C = float(input("Entrez la valeur du facteur C (qualité du contenu) : "))
A = float(input("Entrez la valeur du facteur A (compétences et expérience de l'enseignant) : "))
R = float(input("Entrez la valeur du facteur R (relation enseignant-apprenant) : "))
P = float(input("Entrez la valeur du facteur P (prix ou coût de l'enseignement) : "))

# Calcul de la valeur de l'enseignement
valeur_enseignement = calculer_valeur_enseignement(C, A, R, P)

# Affichage du résultat
print("La valeur de l'enseignement sur le marché boursier est de :", valeur_enseignement)

# Création d'instances d'élèves avec différentes capacités et incitations
eleve1 = Eleve(0.8, 0.9)
eleve2 = Eleve(0.6, 0.7)
eleve3 = Eleve(0.9, 0.5)

# Définition de la constante k pour ajuster l'importance relative des facteurs
k = 2.0

# Calcul de la valeur pour chaque élève
valeur_eleve1 = eleve1.calculer_valeur(k)
valeur_eleve2 = eleve2.calculer_valeur(k)
valeur_eleve3 = eleve3.calculer_valeur(k)

# Affichage des résultats
print("Valeur de l'élève 1 :", valeur_eleve1)
print("Valeur de l'élève 2 :", valeur_eleve2)
print("Valeur de l'élève 3 :", valeur_eleve3)

# Création d'une liste d'élèves
liste_eleves = [eleve1, eleve2, eleve3]

# Demande des valeurs des facteurs pour la chute de bulle spéculative
facteurs_F = float(input("Entrez la valeur du facteur F : "))
probabilite_P = float(input("Entrez la valeur du facteur P : "))
credits_marges_D = float(input("Entrez la valeur du facteur D : "))
capacite_trading_C = float(input("Entrez la valeur du facteur C : "))

# Calcul de la chute de bulle spéculative
chute_bulle = calculer_chute_bulle_speculative(facteurs_F, probabilite_P, credits_marges_D, capacite_trading_C)

# Affichage du résultat
print("La chute de bulle spéculative est de :", chute_bulle)
