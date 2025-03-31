# Python mocking intro (using pytest)

See tests in [`tests/`](tests/) for details. The tests are split into separate files, that should explain things
bit by bit - following the [agenda](AGENDA.md).

There are some skipped tests that would fail. You may want to play around with those as well. Also there are
some [links you might want to read](DOCS.md).

Happy coding!

## Running the tests

You need to have [`uv`](https://github.com/astral-sh/uv) installed.

If you have [`nur`](https://nur-taskrunner.github.io/docs/) installed you can just use `nur install` and then
`nur test`.

In all other cases:

* Use `uv sync --groups dev` to install everything
* Use `uv run pytest tests/` to install the tests  
  (you may also run single files of course)
