#4
obj = {"a": 42, "b": 42, "c": 42, "d": 42}
accumulateur = 1
for key, value in obj.items():
    if key != "d":
        accumulateur *= value
    else:
        accumulateur -= value

print(accumulateur)