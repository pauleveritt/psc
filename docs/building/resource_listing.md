# Resource Listing

Our navigation needs to list the available examples.
Equally, we need a cleaner way to extract the data from an example.
In this step, we make "resource" objects for various models: page, example, contributor.
We'll leave page and contributor for the next step.

Big ideas: A standard model helps us with all the representations of an example.

## What's an Example?

We'll start with, of course, tests.
This time in `test_resources`.
Let's write `test_example` and see if we can correctly construct an instance.
It will need all the bits the template relies on.

Our resource implementation will use dataclasses, with a base `Resource`.
We'll use `__post_init__` to fill in the bits by opening the file.
Also, as "keys", we'll use a `PurePath` scheme to name/id each example.

To help testing and to keep `__post_init__` dead-simple, we move most of the logic to easily-testable helpers.

## Gathering the Resources

We'll make a "resource dB" available at startup with the examples.
For now, we'll do a `Resources` dataclass with an examples field as `dict[PurePath, Example]`.
Later, we'll add fields for pages and contributors.

First a test, of course, to see if `get_resources` returns a `Resources.examples` with `PurePath("hello_world")` mapping to an `Example`.

We then write the `resources.get_resources` function that generates a populated `Resources`.

## Listing Examples

Now that we have the listing of examples, we head back to `app.py` and put it to work.

- Get the "database"
- Make /examples/index.html
- List them there
