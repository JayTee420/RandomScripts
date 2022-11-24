print("How much weed are you using to make the weed butter? (in grams)")
GramsWeed = input()
print("What is the THC content of the weed? (in %)")
StrengthWeed = input()
ButterPotency = 10 * (int(GramsWeed) * int(StrengthWeed))
print(
    "Your weed butter has "
    + str(ButterPotency)
    + " milligrams of THC swimming around in it. Oh my!"
)
print("How much of the weed butter are you going to use in the recipe? (in %)")
ButterAmount = input()
MixPotency = int(ButterPotency) * int(ButterAmount) // 100
print(
    "OK, so there's about "
    + str(MixPotency)
    + " milligrams of THC actually going into the recipe."
)
print("How many servings does the recipe say you're going to make?")
NumberOfServings = input()
BrowniePotency = int(MixPotency) // int(NumberOfServings)
if BrowniePotency <= 10:
    print(
        "Your edibles will be "
        + str(BrowniePotency)
        + " milligrams of THC per serving! This is considered the threshold dosage, so you might not feel it properly."
    )
elif 10 <= BrowniePotency <= 20:
    print(
        "Your edibles will be "
        + str(BrowniePotency)
        + " milligrams of THC per serving! This is the average strength of a homemade brownie."
    )
elif 20 <= BrowniePotency <= 30:
    print(
        "Your edibles will be "
        + str(BrowniePotency)
        + " milligrams of THC per serving! This is pretty intense, about the same strength as an Amsterdam Genetics space-cake."
    )
else:
    print(
        "Your edibles will be "
        + str(BrowniePotency)
        + " milligrams of THC per serving! Buckle up, you're in it for the full send."
    )

