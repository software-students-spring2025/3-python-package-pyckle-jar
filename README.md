# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

## Excuse Generator for Software Engineers

excuse-generator is a fun and practical Python package that helps software engineers come up with excuses for common coding problems. Whether you're dealing with bugs, missed deadlines, PR delays, failed deployments, or awkward meetings, this package has you covered!

### Possible Functions

1. generate_excuse(category:str)-> str
    - generates an excuse based on a specificed category (bug, deadline, PR, meeting, deploymeent)
    - some categories have subcategories and will ask for a sub category parameter.
2. random_excuse() -> str
    - generates a completely random excuse from all categories
3. add_custom_excuse(category:str, excuse:str)
    - allows users to add a custom excuse to the existing collection
4. list_categories() -> list
    - returns a list of available excuse categories
