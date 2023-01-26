import argparse

def read_arguments():
    parser = argparse.ArgumentParser(description='''Hello World''', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--name",
                        type=str,
                        required=True,
                        help="Name")
    return parser

def say_hello_world(name):
    print(f"Hello to {name} from the crazy Docker world")

# Main section
if __name__ == "__main__":
    parser = read_arguments()
    args = parser.parse_args()
    name = args.name
    say_hello_world(name)