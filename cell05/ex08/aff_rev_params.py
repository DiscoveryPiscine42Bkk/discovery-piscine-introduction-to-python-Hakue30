import sys

if len(sys.argv) < 3:
    print("threee twoo onee")
else:
    for param in reversed(sys.argv[1:]):
        print(param)
        