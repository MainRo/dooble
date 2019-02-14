import argparse
from dooble.idl import Idl
from dooble.dooble import create_marble_from_ast, default_theme
from dooble.render import render_to_file


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--input',
        help='marble diagram definition file',
        required=True)
    parser.add_argument(
        '--output',
        help='file where rendered diagram will be saved',
        required=True)
    return parser.parse_args()


def main():
    args = parse_arguments()

    idl_file = open(args.input, 'r')
    idl_text = idl_file.read()

    idl = Idl()
    ast = idl.parse(idl_text)

    #print(ast)
    marble = create_marble_from_ast(ast)
    render_to_file(marble, args.output, default_theme)
