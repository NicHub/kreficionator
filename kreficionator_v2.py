"""

kreficionator_v2

La faute de l’orthographe
Arnaud Hoedt
Jérôme Piron
TEDxRennes

https://youtu.be/5YO7Vg1ByA8
https://onlinephp.io/
["s", "ss", "c", "ç", "sc", "t", "x", "z", "th", "sth", "cc", "sç"],
["ss", "c", "t", "sc"],

"""

import itertools


def apply_french_rules(word):
    """___"""
    if any(elem in word for elem in ["ffy", "fy", "tiond", "tiont"]):
        word = None
    else:
        word.replace("èff", "eff")
    return word


def generate_combinations(phonemes):
    """___"""
    combinations = itertools.product(*phonemes)
    combinations = ["".join(line) for line in combinations]
    combinations = [apply_french_rules(line) for line in combinations]
    combinations = [elem for elem in combinations if elem is not None]
    return combinations


def print_results(combinations, phonemes):
    """___"""
    count = lambda l: l[0] if len(l) == 1 else l[0] * count(l[1:])
    for id, combination in enumerate(combinations):
        print(f"{id+1:4d}. {combination}")
    print(
        "Nombre de combinaisons avant application des règles de français :"
        f" {count([len(row) for row in phonemes])}"
    )
    print(
        "Nombre de combinaisons après application des règles de français :"
        f" {len(combinations)}"
    )


if __name__ == "__main__":
    phonemes = (
        ("k", "c", "ch"),
        ("r"),
        ("ai", "è"),
        ("f", "ff", "ph"),
        ("i", "y"),
        ("ss", "c", "t", "sc"),
        ("i"),
        ("on", "ond", "ont"),
    )

    combinations = generate_combinations(phonemes)
    print_results(combinations, phonemes)
