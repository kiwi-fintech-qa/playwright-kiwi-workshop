# Methods cheatsheet

Here you can find a brief overview of some basic methods and commands useful for developing tests with Playwright.

## Methods of the [Page](https://playwright.dev/python/docs/api/class-page) class:
- [page.goto(url, **kwargs)](https://playwright.dev/python/docs/api/class-page#page-goto) for navigating to a specific `url`
- [page.locator(selector, **kwargs)](https://playwright.dev/python/docs/api/class-page#page-locator) for returning a locator to be further used (can be stored into a variable, e.g., for identifying the textual value of the given object)

## Methods of the [Locator](https://playwright.dev/python/docs/api/class-locator) class:
- [locator.click(**kwargs)](https://playwright.dev/python/docs/api/class-locator#locator-click) for clicking objects on the page
- [locator.count()](https://playwright.dev/python/docs/api/class-locator#locator-count) for getting the count of occurrences of the given object
- [locator.fill(value, **kwargs)](https://playwright.dev/python/docs/api/class-locator#locator-fill) for filling out input fields (e.g., login forms or search fields)
- [locator.first](https://playwright.dev/python/docs/api/class-locator#locator-first) for identifying the first matching object
- [locator.get_attribute(name, **kwargs)](https://playwright.dev/python/docs/api/class-locator#locator-get-attribute) for getting the value of the attribute specified by `name` from the given object
- [locator.inner_text(**kwargs)](https://playwright.dev/python/docs/api/class-locator#locator-inner-text) for capturing the textual content of the matching object
- [locator.is_hidden(**kwargs)](https://playwright.dev/python/docs/api/class-locator#locator-is-hidden) for checking whether an object is not visible on the page
- [locator.is_visible(**kwargs)](https://playwright.dev/python/docs/api/class-locator#locator-is-visible) for checking whether an object is visible on the page
- [locator.nth(index)](https://playwright.dev/python/docs/api/class-locator#locator-nth) for returning the nth matching object
- [locator.select_option(**kwargs)](https://playwright.dev/python/docs/api/class-locator#locator-select-option) for selecting an option from a dropdown list
- [locator.wait_for(**kwargs)](https://playwright.dev/python/docs/api/class-locator#locator-wait-for) for waiting until an object is visible or hidden (visibility is expected based on the keyword argument `state="visible"` or `state="hidden"`)

## Useful Python statements, functions, constructors etc.:
- [assert statement](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement) for evaluating expressions (e.g., `assert 1 < 2`; raises `AssertionError` if the expression evaluates as `False`)
- [float(x="0.0")](https://docs.python.org/3/library/functions.html#float) returns a float from the provided number or string (e.g., `float("1.23")` returns the `1.23` float)
- [for statement](https://docs.python.org/3/tutorial/controlflow.html#for-statements) for iterating over the items of a sequence (e.g., to repeatedly perform a certain action)
- [formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) for formatting strings (e.g., `f"a = {n}"` with `n = 1` is decoded as `"a = 1"`)
- [if statement](https://docs.python.org/3/tutorial/controlflow.html#if-statements) for making decisions based on the `True` or `False` value of the provided condition
- [int(x="0")](https://docs.python.org/3/library/functions.html#int) returns an integer from the provided number or string (e.g., `int("123")` returns the `123` integer)
- [list indexing](https://docs.python.org/3/tutorial/introduction.html#lists) for identifying the nth item of a list (e.g., with the list `l = ["a", "b", "c"]`, `l[0]` returns `"a"`)
- [math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)](https://docs.python.org/3/library/math.html#math.isclose) for comparing float values
- [min(iterable, *, key=None)](https://docs.python.org/3/library/functions.html#min) for selecting the smallest item of the provided iterable (e.g., a list with values; `min([1, 2, 3])` returns `1`)
- [range(start, stop[, step])](https://docs.python.org/3/library/stdtypes.html#typesseq-range) returns an immutable sequence of numbers and can, e.g., be used for creating lists of numbers when combined with the [list](https://docs.python.org/3/library/stdtypes.html#list) constructor (e.g., `list(range(3))` returns `[0, 1, 2]`)
- [str.replace(old, new[, count])](https://docs.python.org/3.3/library/stdtypes.html?highlight=split#str.replace) for returning a string with replaced characters (e.g., `"a,b".replace(",", "")` returns `ab`)
- [str.split(sep=None, maxsplit=-1)](https://docs.python.org/3.3/library/stdtypes.html?highlight=split#str.split) for splitting strings into lists based on a separator (e.g., `"a-b".split("-")` returns `['a', 'b']`)
- [str.strip([chars])](https://docs.python.org/3/library/stdtypes.html#str.strip) for removing the leading and trailing characters from a string (e.g., `"-asd--".strip("-")` returns `"asd"`)
