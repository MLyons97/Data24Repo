import Animal as A

emby = A.Spaniel("Emby", "Bev")
tot = A.Lab("Tot", "Jenny")
print(emby.get_breed())
tot.breed = "Not A Lab"
print(tot.get_breed())