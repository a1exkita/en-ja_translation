import sys
for arg in sys.argv[1:]:
    print("Input : {}".format(arg))
    with open(arg, "r") as f:
        text = f.read()
    tokens = text.split()
    print("Vocab : {}".format(len(set(tokens))))