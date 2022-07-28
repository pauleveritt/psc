"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """PyScript Collective."""


if __name__ == "__main__":
    main(prog_name="psc")  # pragma: no cover
