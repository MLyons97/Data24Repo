import Main_Class as classes

# Bug Moves
b_buzz = classes.Moves("Bug Buzz", 80, 1, "Bug", "spec")

# Dark Moves
crunch = classes.Moves("Crunch", 80, 1, "Dark", "phys")

# Dragon Moves
drag_claw = classes.Moves("Dragon Claw", 80, 1, "Dragon", "phys")

# Electric Moves
tbolt = classes.Moves("Thunderbolt", 90, 1, "Electric", "spec")

# Fairy Moves
mblast = classes.Moves("Moonblast", 95, 1, "Fairy", "spec")

# Fighting Moves
s_ucut = classes.Moves("Sky Uppercut", 85, 0.9, "Fighting", "phys")

# Fire Moves
fthrower = classes.Moves("Flamethrower", 90, 1, "Fire", "spec")

# Flying Moves
w_attack = classes.Moves("Wing Attack", 60, 1, "Flying", "phys")
hcane = classes.Moves("Hurricane", 110, 0.7, "Flying", "spec")

# Ghost Moves
s_ball = classes.Moves("Shadow Ball", 80, 1, "Ghost", "spec")

# Grass Moves
se_bomb = classes.Moves("Seed Bomb", 80, 1, "Grass", "phys")

# Ground Moves
equake = classes.Moves("Earthquake", 100, 1, "Ground", "phys")

# Ice Moves
i_beam = classes.Moves("Ice Beam", 90, 1, "Ice", "spec")

# Normal Moves #
tackle = classes.Moves("Tackle", 40, 1, "Normal", "phys")
b_slam = classes.Moves("Body Slam", 85, 1, "Normal", "phys")
splash = classes.Moves("Splash", 0, 1, "Normal", "phys")
struggle = classes.Moves("Struggle", 5, 1, "Normal", "phys")

# Poison Moves
sdg_bomb = classes.Moves("Sludge Bomb", 90, 1, "Poison", "spec")

# Psychic Moves
psyc_ = classes.Moves("Psychic", 90, 1, "Psychic", "spec")

# Rock Moves
r_slide = classes.Moves("Rock Slide", 75, 0.9, "Rock", "phys")

# Steel Moves
m_mash = classes.Moves("Meteor Mash", 90, 0.95, "Steel", "phys")

# Water Moves
surf = classes.Moves("Surf", 90, 1, "Water", "spec")


# Status Moves
#                       Name, Power, Accuracy, Type, Category
#                       Name, Stage diff, accuracy, Stat, Boost
sdance = classes.Moves("Swords Dance", 2, 1, "Attack", "boost")

# Playtesting Moves
missing = classes.Moves("Missing move", 100000, 0, "Test", "phys")