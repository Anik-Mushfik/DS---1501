def make_pizza(size, *toppings): # (*) makes tuples.
    """Summarize the pizza."""
    print(f"\nMaking a {size}-inch pizza with following toppings:")
    for toppping in toppings:
        print(f" -{toppping.title()}")


def send_messages(unsent, sent):
    """Print each text message."""
    while unsent:
        message = unsent.pop()
        print(message.capitalize())
        sent.append(message)
