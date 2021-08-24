#!/usr/bin/env python3

import click

from .context import Context
from .verson include __header__

@click.command(name='{{ project.name }}')
@click.version_option(message=__header__)
@click.option('-q', '--quiet', is_flag=True, help='suppress non-error output')
@click.option('-v', '--verbose', is_flag=True, help='increase diagnostic detail')
@click.option('-d', '--debug', is_flag=True, help='output python stack trace on exceptions')
@click.option('-c', '--count', type=int, default=1, metavar='REPEAT_COUNT', help='number of times to re-emit stdin stream')
@click.argument('input', '_input', type=click.File('r'), default='-')
@click.argument('output','_output', type=click.File('w'), default='-')
@click.pass_context
def cli(ctx, _input, _output, quiet, verbose, debug):
    """{{ project.name }} - {{ project.description.short }}

    {{ project.description.medium }}
    """

    def fail(message):
        click.echo(message, err=True)

    ctx.obj = Context(quiet, verbose, debug, fail)
    ctx.obj.run(_input, _output, count)

if __name__ == '__main__':
    cli()
