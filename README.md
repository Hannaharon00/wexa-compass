# Career Compass

**Career Compass** turns a job-search question — *"what do I actually need to learn to become an X?"* — into a graph traversal. Skills, courses and job roles are modeled as a connected graph in [CognoDB](https://console.cognodb.com), and the app walks that graph to answer questions a flat spreadsheet can't: which roles are you already closest to, which courses close the gap, and in what order should you take them given each course's own prerequisites.

Built for the Wexa AI CognoDB take-home assignment.

- **Live demo:** [wexa-career-compass.vercel.app](https://wexa-career-compass.vercel.app) (frontend on Vercel, API on Railway, data on CognoDB Cloud)
- **Screen recording:** _TODO — add link_

---

## Table of contents

1. [Why a graph database?](#why-a-graph-database)
2. [Data model](#data-model)
3. [Screenshots](#screenshots)
4. [Project structure](#project-structure)
5. [Setup](#setup)
6. [Running locally](#running-locally)
7. [The main queries, explained](#the-main-queries-explained)
8. [Error handling](#error-handling)
9. [Deployment](#deployment)

- **Recursive CTEs with no fixed depth**, because a course's prerequisite chain isn't a fixed number of joins — `python_fundamentals → python_intermediate → python_for_data_analysis → intro_machine_learning → deep_learning_specialization` is 4 hops deep in this dataset, and a different role might need a 1-hop or 6-hop chain. SQL can express *a* recursive CTE for *one* fixed relationship, but combining "walk the prerequisite chain" with "and also find the shortest conceptual bridge between two skills that aren't directly connected" means stacking multiple recursive CTEs and reconciling them in application code anyway — at which point the database has stopped doing the interesting part of the work.
- **Shortest-path queries with unbounded hop count** — "what's the closest skill I already know to this one I'm missing?" is exactly `shortestPath()` in Cypher (`SHORTEST_SKILL_BRIDGE` in [`queries.py`](backend/app/queries.py)). The relational equivalent is either a hand-rolled BFS in application code pulling the *entire* edge table into memory, or a recursive CTE with manual visited-set / cycle-guard logic re-implemented by hand.
- **Cheap traversal in any direction** — `Skill → RELATED_TO → Skill → TEACHES ← Course → PREREQUISITE_OF → Course → TEACHES → Skill ← REQUIRES_SKILL ← Role` is one pattern match in Cypher. In a relational schema each hop is another join, and the query planner has no notion that these tables represent a connected graph — every additional hop is a linear cost the database can't reason about the way a native graph index can.

None of this is *impossible* in SQL — it's that the moment "how are these things connected, and how many steps apart" becomes the actual question your product needs answered, a database built around join tables is fighting its own grain, and a graph database is answering the question directly.

## Data model

```mermaid
graph LR
    Skill1((Skill)) -- RELATED_TO --> Skill2((Skill))
    Course -- TEACHES --> Skill1
    Course -- REQUIRES --> Skill2
    CourseA((Course)) -- PREREQUISITE_OF --> CourseB((Course))
    Role -- REQUIRES_SKILL --> Skill1
```

**Nodes**

## Screenshots

| | |
|---|---|
| **Home — skill picker** | ![Home page with skill picker](docs/screenshots/01-home.png) |
| **Roles, ranked by match** | ![Roles grid ranked by skill match percentage](docs/screenshots/02-roles.png) |
| **Learning path for a role** | ![Role detail page with computed learning path](docs/screenshots/03-role-detail.png) |
| **Course catalog** | ![Searchable, filterable course catalog](docs/screenshots/04-courses.png) |
| **Course prerequisite chain** | ![Course detail page with prerequisite chain breadcrumb](docs/screenshots/05-course-detail.png) |
| **Skill graph explorer** | ![Radial skill graph showing multi-hop related skills](docs/screenshots/06-skill-graph.png) |

## Project structure

```
backend/
  app/
    main.py          FastAPI app, CORS, error handling, serves the built frontend
    config.py         Environment variable loading
    db.py              CognoDB driver lifecycle + graceful error handling
    queries.py        Every Cypher statement in the app, with comments on why each is shaped the way it is
    schemas.py        Pydantic request/response models
    routers/
      skills.py, courses.py, roles.py, paths.py
  seed/
    seed_data.py       The hand-curated dataset (skills, courses, roles, edges)
    seed.py             Idempotent loader script (MERGE-based, safe to re-run)
  requirements.txt
frontend/
  src/
    api/                Typed fetch client + data-fetching hooks
    components/         Reusable UI (skill picker, cards, loading/empty/error states, skill graph SVG)
    pages/               One file per route
    state/               Known-skills selection, persisted to localStorage
README.md
.env.example
```

