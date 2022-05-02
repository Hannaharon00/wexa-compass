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

# Multi-hop traversal (2+ hops): walk the RELATED_TO skill graph outward
# from a starting skill up to `depth` hops, and for every skill reached
# along the way, pull in the courses that teach it. A relational schema
# would need a separate self-join per hop (or a recursive CTE) to do
# this; here it's one variable-length pattern.
SKILL_NEIGHBORHOOD = """
MATCH (origin:Skill {skill_id: $skill_id})
CALL {
    WITH origin
    MATCH path = (origin)-[:RELATED_TO*1..%(depth)s]-(related:Skill)
    RETURN related, min(length(path)) AS hops
    ORDER BY hops
}
OPTIONAL MATCH (related)<-[:TEACHES]-(c:Course)
RETURN related.skill_id AS skill_id, related.name AS name,
       related.category AS category, hops,
       collect(DISTINCT {course_id: c.course_id, title: c.title}) AS courses
ORDER BY hops, related.name
"""

GET_SKILL = """
MATCH (s:Skill {skill_id: $skill_id})
OPTIONAL MATCH (c:Course)-[:TEACHES]->(s)
OPTIONAL MATCH (r:Role)-[:REQUIRES_SKILL]->(s)
RETURN s.skill_id AS skill_id, s.name AS name, s.category AS category,
       s.description AS description,
       collect(DISTINCT {course_id: c.course_id, title: c.title}) AS taught_by,
       collect(DISTINCT {role_id: r.role_id, title: r.title}) AS required_by
"""

LIST_ROLES = """
MATCH (r:Role)
OPTIONAL MATCH (r)-[req:REQUIRES_SKILL]->(s:Skill)
RETURN r.role_id AS role_id, r.title AS title, r.industry AS industry,
       r.seniority AS seniority, r.description AS description,
       count(DISTINCT s) AS skill_count
ORDER BY r.title
"""

