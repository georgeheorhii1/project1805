from argparse import ArgumentParser

parser_example = ArgumentParser()
parser_example.add_argument('--a', default='15')
parser_example.add_argument('--b', default='30')
arguments = parser_example.parse_args()
arguments_converted = arguments.__dict__
a = int(arguments_converted['a'])
b = int(arguments_converted['b'])

print(a, b)
