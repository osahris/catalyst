
import click
from .parser import read_catalyst_directory
from .generators.fhir_shorthand import generate_fhir_shorthand as generate_fhir_shorthand_impl

@click.group()
def catalyst_cli():
    pass

@catalyst_cli.command()
@click.option('--input-directory', '-i', help='The input directory containing the Catalyst markdown files.', required=True)
@click.option('--output-directory', '-o', help='The output directory to write the generated files to.', required=True)
def generate_fhir_shorthand(input_directory, output_directory):
    print("Generating FHIR Shorthand...",input_directory)
    metadata = read_catalyst_directory(input_directory)
    generate_fhir_shorthand_impl(metadata,output_directory)
