#!/usr/bin/env python3

import click

from .version import __header__, __version__
from .context import Context
from .repeater import Repeater


@click.command(name='repeat')
@click.version_option(message=__header__)
@click.option('-q', '--quiet', is_flag=True, help='suppress non-error output')
@click.option('-v', '--verbose', is_flag=True, help='increase diagnostic detail')
@click.option('-d', '--debug', is_flag=True, help='output python stack trace on exceptions')
@click.option('-l', '--length', is_flag=True, help='output number of lines before any input')
@click.argument('count', type=int, default=1)
@click.argument('input', type=click.File('r'), default='-')
@click.argument('output', type=click.File('w'), default='-')
@click.pass_context
def cli(ctx, input, output, count, length, quiet, verbose, debug):
    """Read input lines and write them to output COUNT times.

        If --length is set, begin output with the number of lines read.
        COUNT may be 0, in which case the input lines won't be sent.
    """

    def fail(message):
        click.echo(message, err=True)
        click.Abort()

    ctx.obj = Context(quiet, verbose, debug, fail)
    Repeater().run(input, output, count, length)


if __name__ == '__main__':
    cli()
