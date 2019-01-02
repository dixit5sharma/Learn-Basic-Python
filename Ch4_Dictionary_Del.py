Glossary={"Car":"4 wheel vehicle","Demolished":"destroyed","Outstanding":"very good"}

if "Outstanding" in Glossary:
    del Glossary["Outstanding"] # Deletes the index and the value
    print(Glossary)
else:
    print("Not Found")

# Alternative Method

Glossary.pop("Car")    # Glossary.pop("Car",None) is the function. No need of None as of here.
print(Glossary)
