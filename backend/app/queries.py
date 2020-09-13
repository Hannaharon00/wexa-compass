"""Every Cypher statement the app runs, kept in one place so the data
model and query design can be read start to finish without hunting
through route handlers. All statements are parameterised -- values are
always passed via the `parameters` dict, never interpolated into the
query string.
"""

