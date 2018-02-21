# -*- coding: utf-8 -*-

"""Console script for systeminfo2."""

import click


@click.command()
def main1(args=None):
    """Console script for systeminfo2."""
    click.echo("Replace this message by putting your code into "
               "systeminfo2.cli.main1")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main1__":
    import sys
    sys.exit(main1())
