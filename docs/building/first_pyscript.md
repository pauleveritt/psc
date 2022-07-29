# First PyScript Example

Well, that was certainly a lot of prep.

Let's get into PyScript and examples.
In this step we'll add the "Hello World" example along with unit/shallow/full tests.
We will *not* though go further into how this example gets listed.
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

Using `curl`, I grabbed the latest `pyscript.css` and `pyscript.js`.
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

