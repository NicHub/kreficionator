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

counter = 0


def follow_french_rules(result):
    """___"""
    for elem in ["ffy", "fy", "tiond", "tiont"]:
        if elem in result:
            return None
    result = result.replace("èff", "eff")
    return result


def generate_combinations(phonemes, current_combination=[], index=0):
    """___"""
    if not index == len(phonemes):
        for element in phonemes[index]:
            generate_combinations(phonemes, current_combination + [element], index + 1)
        return

    result = "".join(current_combination)
    result = follow_french_rules(result)
    if result is None:
        return

    global counter
    counter += 1
    print(f"{counter:4d}. {result}")


if __name__ == "__main__":
    phonemes = [
        ["k", "c", "ch"],
        ["r"],
        ["ai", "è"],
        ["f", "ff", "ph"],
        ["i", "y"],
        ["ss", "c", "t", "sc"],
        ["i"],
        ["on", "ond", "ont"],
    ]

    generate_combinations(phonemes)
