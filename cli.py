#!/usr/bin/env python

"""
Commandline tool for interacting with library
"""

import json
import click
from flask import Flask
from cirepolib.cirepomod import fake_data
from cirepolib.cirepomod import print_name
from cirepolib import __version__

@click.version_option(__version__)
@click.command()
@click.option("--name", help="name to print")
def pname(name):
    """Prints a name out with apple at the end"""
    try:
        res = print_name(name)
        click.echo(click.style(res, bg='blue', fg='white'))
    except TypeError:
        click.echo("Must pass in Name")

    url_version = "http://localhost:5000/"
    url_fake = "http://localhost:5000/fakedata"
    url_name = "http://localhost:5000/wname"
    click.echo("try these pages:")
    click.echo(url_version)
    click.echo(url_fake)
    click.echo(url_name)

    app = Flask(__name__)

    @app.route("/")
    def hello():
        return f"This is my library version {__version__}"

    @app.route("/fakedata")
    def fakedata():
        return json.dumps(fake_data())

    @app.route("/wname")
    def wname():
        return f"name is {print_name(name)}"

    app.run()

    # just to satisfy lint's complaint of unused variable
    hello();fakedata();wname()

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    pname()
