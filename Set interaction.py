setx={'GREEN','BLUE'}
sety={'BLUE','YELLOW'}
print("Orignal set elements:")
print(setx)
print(sety)
print("\nInteraction of two said sets:")
setz=setx.intersection(sety)
print(setz)
setz=setx.union(sety)
print(setz)
setz=setx.difference(sety)
print(setz)
setz=setx.symmetric_difference(sety)
print(setz)