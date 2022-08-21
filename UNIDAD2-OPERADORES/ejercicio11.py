# En la heladera tengo 5 cubeteras de 2 x 6 (1 de ellas está vacía)
# Tengo que preparar 5 fernet y 3 campari
# El fernet lleva 3 hielos y el campari 2
# Escribir un programa que me diga cuantos hielos me sobran

cubetera=2*6
x=5
cant_cubeteras=x
total_hielos=(cubetera*cant_cubeteras)
print("En este momento existe un total de",total_hielos,"hielos disponibles para preparar 5 fernet y 3 campari: ")

fernet_hielo=3 # el fernet lleva 3 hielos
campari_hielo=2 # el campari lleva 2 hielos
q1=5
q2=3
q_fernet=q1
q_campari=q2

q_hielo_fernet=fernet_hielo*q1
q_hielo_campari=campari_hielo*q2

q_hielo_total=q_hielo_fernet+q_hielo_campari

hielo_sobrante=total_hielos-q_hielo_total

print("para preparar 5 fernet necesito 3 hielos por c/u, por lo tanto utilizo: ",q_hielo_fernet, "hielos.")
print("para preparar 3 camparis necesito 2 hielos por c/u, por lo tanto utilizo: ",q_hielo_campari, "hielos.")

print("Para hacer estos 7 tragos consumi un total de: ",q_hielo_total,"hielos. Me sobran por lo tanto: ",hielo_sobrante,"hielos.")

