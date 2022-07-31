# Bulma Styling

Let's start moving towards the goal of providing attractive examples.
Each example will appear in several "targets", primarily a website like
the [existing examples](https://pyscript.net/examples/).

In this step, we'll start building the PSC website.
We will *not* in this step, though, tackle any concept of a build step, nor anything beyond the homepage.

Big ideas: use off-the-shelf CSS framework, static generation, dead-simple web tech.

## Why Bulma?

We're making a website -- the PyScript Collective.
But we're also making a web app -- the PyScript Gallery.
As it turns out, we're also shipping a PyPI package -- the PyScript Gallery, aka `psga`.

We need a nice-looking web app.
Since we're not designers, let's use a popular, off-the-shelf CSS framework.
I have experience with (and faith in) [Bulma](https://bulma.io): it's attractive out-of-the-box, mature, and strikes the
right balance.

## New Test With `beautifulsoup`

Let's start with a failing test in `tests/test_assets.py`.
We'll move the `test_app.test_favicon` there as a start.

We don't want to just make sure the favicon is at the URL.
We want to parse the HTML, find the target, and test *that*, to make sure the HTML link isn't broken.

Let's add `beautifulsoup` as a parser, grab the response body, and make it easy to go find links.
Since I'm using `mypy`, I also do `poetry add -D types-beautifulsoup4`.
I'll also install `html5lib` as an HTML parser.

The `test_favicon` test was changed to get the `favicon.png` path from the `<link>`, then fetch it.

:::{note} PyCharm Tip For Resources

I'd like PyCharm to warn me about bad links in HTML.
So I marked the `src/psc` directory as a "Resource Root".
This gives me autocomplete, warnings, refactoring, etc.
:::

## Bring In Bulma

The tests are in good shape and having `beautifulsoup` will prove...beautiful.
Let's add a `<link rel="stylesheet" href="/static/bulma.min.css"/>` to the home page.
We start with a failing test, similar to the favicon one.

To make it pass, I:

- Downloaded the bits into static
- Added a `<link rel="stylesheet" href="/static/bulma.min.css"/>` to the home page.

I also added the other parts of the Bulma starter (doctype, meta.)
If we open it up in the browser, it looks a bit different.

## Navbar and Footer

We'd like a common navbar on all our pages.
Bulma [has a navbar](https://bulma.io/documentation/components/navbar/).
This also means a download of the PyScript SVG logo, which we'll write a test for.

Ditto for a -- for now, *very* simple -- [footer component](https://bulma.io/documentation/layout/footer/).

## Body

Bulma makes use of `<section>`, `<footer>`, etc.
Let's put the "main" part of our page into a `<main class="section">` tag.

For the failing test, we'll simply look to see there is a `<main>`.
But, as this is no longer a static asset, we'll put this in `test_app.test_homepage`.

## Templating

It sucks to repeat the layout across every static HTML file.
Let's make some Jinja2 templates, then [setup Starlette](https://www.starlette.io/templates/) to use it the templates.

As precursor, install Jinja2 as a dev dependency.

We'll start by making a templates directory at `src/psc/templates`.
In there, we'll make `page.jinja2` and `layout.jinja2`.

:::{note} PyCharm Template Setup

If you use PyCharm, use `Mark This Directory` to make it a template directory.
Also, go into preferences and set the project as using Jinja2 for `Template Languages`.
:::

In `layout.jinja2`, take everything out that isn't in `<main>`.
Provide a slot for title and main.
Then change `page.jinja2` to point at `layout.jinja2`, filling those two slots.

In `app.py`, we change the `homepage` route to return a template.
The context dictionary for the template will have two pieces of data:
- The title of the current page
- The HTML that should go in the main block.

Let's do three things:

- Change `index.html` only have the `<main>` part
- In the route, read the file content
- Then pass the file contents into `page.jinja2`, using `| safe`

When done correctly, the tests should pass.

## Future

This PSC prototype just uses downloaded Bulma CSS and other assets.
It doesn't bring in the SASS customizations and software, nor does it look at Bulma forks that bring in CSS Variables.

While we did a little templating, we didn't go far.
It's going to get a lot more interesting and intricate, as we have different ways we want to package things.
