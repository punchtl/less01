time = int(input("Введите время в секундах: "))
hours = time // 3600
residue = time % 3600
minutes = residue // 60
sec = residue % 60
print(f"{hours}:{minutes}:{sec}")
