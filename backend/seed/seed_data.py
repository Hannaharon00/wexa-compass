"""Realistic seed dataset for Career Compass.

Everything here is hand-curated (no random generation) so the graph
reads as a plausible slice of a real learning/career catalog: skills
grouped into categories, courses that teach and require skills and
chain into each other as prerequisites, and roles that require skills
at a given importance/level.
"""

# (skill_id, name, category, description)
SKILLS = [
    # Programming Languages
    ("python", "Python", "Programming Languages", "General-purpose language widely used in backend, data and ML work."),
    ("pandas", "Pandas", "Data & ML", "Python library for tabular data manipulation."),
    ("etl", "ETL Pipelines", "Data & ML", "Extracting, transforming and loading data between systems."),
    ("data_warehousing", "Data Warehousing", "Data & ML", "Designing systems for large-scale analytical storage."),
    ("deep_learning", "Deep Learning", "Data & ML", "Neural network based machine learning."),
    ("nlp", "Natural Language Processing", "Data & ML", "Modeling and understanding human language with computers."),
    ("data_modeling", "Data Modeling", "Data & ML", "Structuring data for correctness and query efficiency."),
    # Cloud & DevOps
    ("aws", "AWS", "Cloud & DevOps", "Amazon's cloud computing platform."),
    ("docker", "Docker", "Cloud & DevOps", "Packaging applications into portable containers."),
    ("kubernetes", "Kubernetes", "Cloud & DevOps", "Orchestrating containerized workloads at scale."),
    ("ci_cd", "CI/CD", "Cloud & DevOps", "Automating build, test and deployment pipelines."),
    ("linux", "Linux Administration", "Cloud & DevOps", "Operating, securing and troubleshooting Linux systems."),
    ("terraform", "Terraform", "Cloud & DevOps", "Declarative infrastructure-as-code tooling."),
    ("computer_networking", "Computer Networking", "Cloud & DevOps", "How data moves between systems: TCP/IP, DNS, load balancing."),
    ("monitoring_observability", "Monitoring & Observability", "Cloud & DevOps", "Metrics, logs and traces for understanding live systems."),
    ("git", "Git & Version Control", "Cloud & DevOps", "Tracking and collaborating on code changes."),
    # Design & UX
    ("ui_design", "UI Design", "Design & UX", "Visual design of interfaces."),
    ("ux_research", "UX Research", "Design & UX", "Methods for understanding user needs and behavior."),
    ("figma", "Figma", "Design & UX", "Collaborative interface design tool."),
    ("design_systems", "Design Systems", "Design & UX", "Reusable components and standards for consistent UI."),
    ("typography", "Typography", "Design & UX", "The craft of arranging type for legibility and tone."),
    ("prototyping", "Prototyping", "Design & UX", "Building interactive mockups to validate ideas quickly."),
    ("accessibility", "Accessibility (a11y)", "Design & UX", "Designing usable experiences for people with disabilities."),
    # Product
    ("product_strategy", "Product Strategy", "Product", "Defining what to build and why, aligned to business goals."),
    ("user_research", "User Research", "Product", "Talking to and observing users to inform product decisions."),
    ("roadmapping", "Roadmapping", "Product", "Sequencing and communicating product plans over time."),
    ("market_analysis", "Market Analysis", "Product", "Assessing competitors, market size and positioning."),
    ("ab_testing", "A/B Testing", "Product", "Running controlled experiments to validate product changes."),
    # Security
    ("application_security", "Application Security", "Security", "Finding and preventing vulnerabilities in software."),
    ("cryptography_basics", "Cryptography Basics", "Security", "Core concepts behind encryption, hashing and signatures."),
    ("threat_modeling", "Threat Modeling", "Security", "Systematically identifying and prioritizing security risks."),
    ("identity_access_management", "Identity & Access Management", "Security", "Controlling who can access what, and how identity is verified."),
    # Soft Skills
    ("communication", "Communication", "Soft Skills", "Clearly conveying ideas to varied audiences."),
    ("project_management", "Project Management", "Soft Skills", "Planning and coordinating work to hit goals on time."),
    ("agile_scrum", "Agile & Scrum", "Soft Skills", "Iterative delivery frameworks for product teams."),
    ("technical_writing", "Technical Writing", "Soft Skills", "Writing clear documentation and technical content."),
    ("public_speaking", "Public Speaking", "Soft Skills", "Presenting ideas confidently to an audience."),
