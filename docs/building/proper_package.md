# Proper Package

This PSC isn't just prototyping examples to list on a webpage.
It's actually an installable Python package, making it easy for people to _consume and tinker with_ the examples.

As such, PSC starts with a clean-slate:

- A new repo
- Built from (controversially) the [Hypermodern Python cookiecutter](https://cookiecutter-hypermodern-python.readthedocs.io/en/latest/index.html)
- Switch from conda to Poetry/pip
- An installable package on PyPI
- A full Collective website based on Sphinx

Let's look at each decision in detail.

## A New Repo

It's just a disposable prototype, but PSC was written as if it was the new repo.
I'm using a Release Drafter style GitHub workflow to allow release notes to be generated.

## Installable Package

As part of the repo reboot, it's written as if it is a Python package, meant to be installed.
This will potentially make it dead-simple for people to play with the examples, even to edit them and see results.
They will just `pip install our-package` and get everything needed.
Or even simpler, use `pipx` to just run the examples.

:::{attention} Package name?
The PyScript ecosystem should adopt a prefix for add-on packages, as done in Django, Flask, Pyramid, etc.
Presumably this package will be named `pyscript-collective`.

That's pretty long, though.
Perhaps PyScript should adopt `ps-` as the prefix?
:::

## Hypermodern Python

Our repo will have some of "our" software:

- `pytest` fixtures
- Command runners, e.g. a CLI to run the examples

For our stuff, we'll want _some_ automation and quality control tools, such as linters.
For the examples themselves, we might want a small subset of that (low bar for them to _give_ contribution) or large subset (high bar for us to _take_ contribution.)

This stuff is hard to wire together and keep working.
I used the [Hypermodern Python cookiecutter](https://cookiecutter-hypermodern-python.readthedocs.io/en/latest/index.html) as the starting point:

- I have experience with it
- I know it works
- I know how to turn things off that are too pedantic

Some of my Collective brethren will certainly vomit when confronted with all that Hypermodern does.
We can dial it back until we get the right balance of "best practice and long-term maintenance" vs. "easy of contribution."

## Conda -> Poetry

The existing `pyscript-collective` repo starts with a `Makefile`.
It also presumes Conda for everything.

This PSC prototype switches over to Poetry for contributors and pip for consumers.
The use of Poetry isn't important -- we could easily switch to `virtualenv` and `requirements.txt`.
But the switch away from Conda is more intentional: it's less used per the PSF survey, and we want to show that PyScript isn't tied to Anaconda no Conda.

## Website in Sphinx

The writing of this prototype will ultimately result in a full website, based on Sphinx, with a highly-custom and attractive landing page.
Since it is in Sphinx, and since the main PyScript docs are in Sphinx, it should be straightword for PSC to be included into the main site.
