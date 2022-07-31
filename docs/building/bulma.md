# Bulma Styling

Let's start moving towards the goal of providing attractive examples.
Each example will appear in several "targets", primarily a website like the [existing examples](https://pyscript.net/examples/).

In this step, we'll start building the PSC website.
We will *not* in this step, though, tackle any concept of a build step, not even a template language.

Big ideas: use off-the-shelf CSS framework, static generation, dead-simple web tech.

## Why Bulma?

We're making a website -- the PyScript Collective.
But we're also making a web app -- the PyScript Gallery.
As it turns out, we're also shipping a PyPI package -- the PyScript Gallery, aka `psga`.

We need a nice-looking web app.
Since we're not designers, let's use a popular, off-the-shelf CSS framework.
I have experience with (and faith in) [Bulma](https://bulma.io): it's attractive out-of-the-box, mature, and strikes the right balance.

## Bring In Assets

Let's start with a failing test in `tests/test_assets.py` to request the Bulma assets at `/static/bulma.css`.

To make it pass, I:

- Downloaded the bits into static
- And...that's it.

Along the way, I moved the `test_app.test_favicon` to the new `test_assets.py` file.

## Basic Homepage Layout

We'll start by changing just the homepage.
I'll write a failing test that looks for the `<link>` in the `<head>`, plus other bits in [the standard Bulma boilerplate](https://bulma.io/documentation/overview/start/#code-requirements)

With that in place, I'll edit `src/psc/index.html` and make it look like the boilerplate.

## Navbar and Footer

We'd like a common navbar on all our pages.
Bulma [has a navbar](https://bulma.io/documentation/components/navbar/).
Same routine -- failing test, then implementation.

Ditto for a -- for now, *very* simple -- [footer component](https://bulma.io/documentation/layout/footer/).

## Body

Bulma makes use of `<section>`, `<footer>`, etc.
Let's put the "main" part of our page into a `<main>` tag, with a test first, then implementation.

## Future

We won't go any further in this step, as we'll quickly discover -- it will suck to repeat the layout across every file.
We will likely want templating, but we'll also want to retain the "just copy-paste the example" part as well.

This PSC prototype just uses downloaded Bulma CSS and other assets.
It doesn't bring in the SASS customizations and software, nor does it look at Bulma forks that bring in CSS Variables.
