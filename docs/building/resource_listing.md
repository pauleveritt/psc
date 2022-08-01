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

- Base resource

## Listing Examples

- Get the "database"
- Make /examples/index.html
- List them there
