# Build Step

## Lots of Paths

There's a `<py-script>` in an example.
What are the ways someone might consume it?
Turns out -- a LOT!

1. *Viewer From Website*.
This is the most normal one.
A Viewer goes to the Collective site, clicks the link for Examples, and sees the listing.
The Viewer then clicks on the example, gets it loaded up, and looks at it.
This one has a later variation -- what if we let Viewers edit in the browser and see the updated example?

2. *Coder From Package*.
A Coder wants the examples locally.
They use `pipx` to directly run the examples or `pip` to install into a virtual environment.
Either way, a Python process starts that runs a web server to show the examples.
Later, we make it easy to edit the example sources and see the changes.

3. *Contributor Writes Example*.
In-place vs. built.

4. *Collaborator Reviews Example*.
5. *Test Runs Example*.
