#!/usr/bin/env python
import click
from chartOracul.plot import simple_line_chart

@click.group()
def cli():
    pass

@cli.command()
def plot():
    simple_line_chart()

# simple use case
# Display single line chart
if __name__ == '__main__': 
    cli()