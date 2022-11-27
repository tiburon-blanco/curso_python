def hay_rima(p_1, p_2):
    if p_1 [-3:] == p_2[-3:]:
        print("Las palabras", p_1, "y", p_2, "Riman")
    elif p_1[-2:] == p_2[-2:] and p_1[:-3]!= p_2[:-3]:
        print("Las palabras", p_1, "y", p_2,"Riman poco")
    else:
        print("Las palabras", p_1, "y", p_2, "No riman")