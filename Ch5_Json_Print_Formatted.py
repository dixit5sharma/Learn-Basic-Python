import json
def main():
    with open("Files/example_2.json","r") as j:
        a=json.load(j)
        # print(type(a))  # Dict type
        print(json.dumps(a,indent=2))
        # print(type(json.dumps(a,indent=2))) # String type


if __name__=='__main__':
    main()
