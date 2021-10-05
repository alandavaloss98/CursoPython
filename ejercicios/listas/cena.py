invitados = ["Chuy", "Anzony", "Omar"]

print(f"Bienvenido a la cena {invitados[0]}")
print(f"Bienvenido a la cena {invitados[1]}")
print(f"Bienvenido a la cena {invitados[2]}")
print("Lo siento, Anzony no nos podra acompaniar")

invitados[1] = "Francisco"

print(f"Bienvenido a la cena {invitados[1]}")
print("Chicos, encontre una mesa mas grande, puedo invitar a mas gente")

invitados.insert(0, "Octavio")
invitados.insert(2, "Luis Angel")
invitados.append("Isaac")

print(f"Bienvenido a la cena {invitados[0]}")
print(f"Bienvenido a la cena {invitados[1]}")
print(f"Bienvenido a la cena {invitados[2]}")
print(f"Bienvenido a la cena {invitados[3]}")
print(f"Bienvenido a la cena {invitados[4]}")
print(f"Bienvenido a la cena {invitados[5]}")
print("Lo siento chicos, la mesa que iba a reservar no esta disponible, solo pude reservar una mesa para 3 y solo podran ir 2 personas conmigo")

print(f"Lamento no poder invitarte {invitados[0]}")
invitados.pop(0)

print(f"Lamento no poder invitarte {invitados[1]}")
invitados.pop(1)

print(f"Lamento no poder invitarte {invitados[2]}")
invitados.pop(2)

print(f"Lamento no poder invitarte {invitados[2]}")
invitados.pop(2)

print(f"{invitados[0]} tu sigues invitado")
print(f"{invitados[1]} tu sigues invitado")
print("Como les parecio la cena?")