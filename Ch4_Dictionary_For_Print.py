Glossary={"Car":"4 wheel vehicle","Demolished":"destroyed","Outstanding":"very good"}

for k in Glossary:
    print(k,"=",Glossary[k])    # k gives Index Names and Glossary[k] gives value.

# Alternative Method
print("ALternative method using 2 arguments in DictionaryName.items()")

for i,j in Glossary.items():
    print(i,"=",j)
