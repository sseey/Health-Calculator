def calculate_bmi(height, weight):
    """
    Calcule l'Indice de Masse Corporelle (BMI).
    :param height: Taille en mètres.
    :param weight: Poids en kilogrammes.
    :return: BMI (float).
    """
    return weight / (height ** 2)

def calculate_bmr(height, weight, age, gender):
    """
    Calcule le Taux Métabolique de Base (BMR).
    :param height: Taille en centimètres.
    :param weight: Poids en kilogrammes.
    :param age: Âge en années.
    :param gender: Sexe ('male' ou 'female').
    :return: BMR (float).
    """
    if gender.lower() == 'male':
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender.lower() == 'female':
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Le genre doit être 'male' ou 'female'.")
