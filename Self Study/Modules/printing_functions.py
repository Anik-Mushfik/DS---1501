def printing(unprinted, printed):
    while unprinted:
        current = unprinted.pop()
        print(f"Printing Model: {current.title()}")
        printed.append(current)

def printed(printed):
    print("\nThe following desings have been printed-")
    for design in printed:
        print(design.title())

