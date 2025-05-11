# To accept args from cmd line that is values that we will pass in to the programs that we call, we need to use a module - argparse

def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)

if __name__ == "__main__":
    import argparse

    parser =  argparse.ArgumentParser(
        description="Provides a personal greeting." #has set basic description for our args parser.
    )

    # metavar is just a display name if u get a msg that refers back to this args
    parser.add_argument(
        "-n", "--name", metavar="name", #dest="firstName"
        required=True, help="The name of person to greet."
    )

    parser.add_argument(
        "-l", "--lang", metavar="language",
        required=True, help="Langauge to greet in.", 
        choices=['English', 'Spanish', 'German']
    )

    args = parser.parse_args()
    hello(args.name, args.lang)

# ---- no need as this is being done via hello function.
    # msg = f"Hello {args.name}!" #if we have dest set in add arg then we would use that value and not name
    # print(msg)

    # in this case we can't simply run the file via play button becoz we r expecting an argument.
