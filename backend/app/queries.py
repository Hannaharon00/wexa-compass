"""Every Cypher statement the app runs, kept in one place so the data
model and query design can be read start to finish without hunting
through route handlers. All statements are parameterised -- values are
always passed via the `parameters` dict, never interpolated into the
query string.
"""

# ---------------------------------------------------------------------------
# Skills
# ---------------------------------------------------------------------------

LIST_SKILLS = """
MATCH (s:Skill)
RETURN s.skill_id AS skill_id, s.name AS name, s.category AS category,
       s.description AS description
ORDER BY s.category, s.name
"""

