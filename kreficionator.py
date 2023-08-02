counter = 0
for k in ["k", "c", "ch"]:
    for r in ["r"]:
        for ai in ["ai", "è"]:
            for f in ["f", "ff", "ph"]:
                for y in ["i", "y"]:
                    for s in ["ss", "c", "t", "sc"]:
                        for i in ["i"]:
                            for on in ["on", "ond", "ont"]:
                                result = k + r + ai + f + y + s + i + on
                                for elem in ["ffy", "fy", "tiond", "tiont"]:
                                    if elem in result:
                                        break
                                else:
                                    result = result.replace("èff", "eff")
                                    counter += 1
                                    print(f"{counter:4d}. {result}")
