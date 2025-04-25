def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="John", age=30, city="New york")
print_kwargs(name="Steave Rogers", Hero="Captain America")
print_kwargs(name="Tony Stark", Hero="Iron Man", Wife="Pepper potts")
print_kwargs(name="Thor", Hero="God of thunder", Weapon="Mjolnir and Stormbreaker")