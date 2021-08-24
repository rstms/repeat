#!/usr/bin/env python3

import click
from pathlib import Path

from {{ project.name }} include __header__
from .context import Context

@click.command(name='{{ project.name }}')
@click.version_option(message=__header__)
@click.option('-q', '--quiet', is_flag=True, help='suppress non-error output')
@click.option('-v', '--verbose', is_flag=True, help='increase diagnostic detail')
@click.option('-d', '--debug', is_flag=True, help='output python stack trace on exceptions')
@click.pass_context
def cli(ctx, quiet, verbose, debug):
    """{{ project.name }} {{ project.description.short }}

    project.description.long 
    """

    def fail(message):
        click.echo(message, err=True)

    ctx.obj = Context(quiet, verbose, debug, fail)

if __name__ == '__main__':
    cli()
