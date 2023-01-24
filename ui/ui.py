import click


@click.command()
@click.option("--command",
              type=click.Choice["start", "play"])