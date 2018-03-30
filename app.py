import click
from api import get_definition

@click.command()
@click.option('--word', '-w', prompt=True, help='Include a word to look up.')
@click.option('--target', '-t', help='Select target language by language code.', default='en')
@click.option('--origin', '-f', help='Select origin language by language code.', default='')

def cli(word, origin, target):
    get_definition(word, origin, target)
