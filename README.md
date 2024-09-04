# Supplier Data Processor
This is stage 2 of the FFD stock and pricing automation system. Supplier data will need to be read from various sources and file types, normalised and output as actionable items.

The goal is to read a variety of file types, get the supplier items from them, compare them to the website and output pseudo-products which can be uploaded to the website after being approved by a website admin.

## Designs
Design diagrams have been created used [umlet](https://www.umlet.com/). They are within the designs/ directory.

## Tests
Tests have been written with unittest. They can be run with the command:

`python -m unittest`

Or to point at a specific directory to discover tests in:

`python -m unittest discover -s Sources/tests`

Where `Sources/tests` is the directory you would like to discover tests in.