# First PyScript Example

Well, that was certainly a lot of prep.

Let's get into PyScript and examples.
In this step we'll add the "Hello World" example along with unit/shallow/full tests.
We will _not_ though go further into how this example gets listed.
We also won't do any automation across examples: each example gets its own tests.

Big ideas: tests run offline, as the CSS/JS and even Pyodide WASM/JS are locally "served".

## Re-Organize Tests

In the previous step, we made an `src/psc/examples` directory with `first.html` in it.
Let's remove `first.html` and instead, have a `hello_world` directory with `index.html` in it.
For now, it will be the same content as `first.html`, though we need to change the CSS path to `../static/psc.css`.

We also have our "first example" tests in `test_app.py`.
Let's leave that test file to test the application itself, not each individual test.
Thus, let's start `tests/examples/test_hello_world.py` and move `test_first_example*` into it.
We'll finish with `test_hello_world` and `test_hello_world_full` in that file.

With these changes, the tests pass.
Let's change the example to be the actual PyScript `Hello World` HTML file.

## Download PyScript/Pyodide Into Static

Using `curl`, I grabbed the latest `pyscript.css`, `pyscript.js`, and `pyscript.py`, plus the '.map` etc.
This brings up an interesting question about versions.
Should the Collective examples all use the same PyScript/Pyodide versions, or do we need to support variations?

:::{note} Git LFS Support

These Pyodide WASM distributions are...big.
Putting them in the repo, then updating them frequently, will make cloning slow.
OTOH, we don't want to lose "run everything locally".

This might mean enabling Git LFS on the repo.
As an alternative, an extra install step to fetch the latest Pyodide WASM and put in a non-versioned directory.
For now, punting on this.
As final note...it appears to be around 23 MB to include all the WASM, wheels, etc.
:::

Next up, Pyodide.
I got the `.bz2` from the releases and uncompressed/untarred into a release directory.
Bit by bit, I copied over pieces until "Hello World" loaded:

- The `.mjs` and `.asm*`
- `packages.json`
- The distutils.tar and pyodide_py.tar files
- `.whl` directories for micropip, packaging, and pyparsing

## Hello World Example

Back to `src/psc/examples/hello_world/index.html`.
Before starting, we should ensure the shallow test -- `TestClient` -- in `test_hello_world.py` works.

To set up PyScript, first, in `head`:

```html
<link rel="icon" type="image/png" href="../../favicon.png" />
<link rel="stylesheet" href="../../static/pyscript.css" />
<script defer src="../../static/pyscript.js"></script>
```

That gets PyScript stuff.
The JS requests `pyscript.py` which is also in `static`.

To get Pyodide from local installation instead of remove, I added `<py-config>`:

```xml
<py-config>
- autoclose_loader: true
  runtimes:
    - src: "../../static/pyodide.js"
      name: pyodide-0.20
      lang: python
</py-config>
```

This was complicated by a few factors:

- The [PyScript docs page is broken](https://github.com/pyscript/pyscript/issues/528)
- There are no examples in PyScript (and thus no tests) that show a working version of `<py-config>`
- The default value on `autoclose_loader` appears to be `false` so if you use `<py-config>` you need to explicitly turn it off.

At this point, the page loaded correctly in a browser, going to `http://127.0.0.1:3000/examples/hello_world/index.html`.
Now, on to Playwright.

## Playwright Tests

And...that was it.
It just worked.

- Key was `wait_for_selector`
- Ran into numerous problems in the `<py-config>` loader's YAML
- Use `PWDEBUG=1 poetry run pytest -s tests/examples/test_hello_world.py`

## Could Be Better

- Lots of failure modes in the interceptor
- Perhaps a move to async Playwright? (But quite painful)
- Set up more of the `Response`
- Perhaps even use Starlette `FileResponse` with some kind of adapter
- Speed up test running with [ideas from Pyodide Playwright ticket](https://github.com/pyodide/pyodide/issues/2048)
-
