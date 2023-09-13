
import click
from .parser import read_catalyst_directory

@click.group()
def catalyst_cli():
    pass

@catalyst_cli.command()
@click.option('--input-directory', '-i', help='The input directory containing the Catalyst markdown files.', required=True)
def generate_fhir_shorthand(input_directory):
    print("Generating FHIR Shorthand...",input_directory)
    print(read_catalyst_directory(input_directory))
