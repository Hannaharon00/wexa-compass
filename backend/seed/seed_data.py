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
    ("mentoring", "Mentoring & Leadership", "Soft Skills", "Growing the skills of the people around you."),
    ("stakeholder_management", "Stakeholder Management", "Soft Skills", "Aligning people with competing priorities."),
    # CS Fundamentals
    ("data_structures_algorithms", "Data Structures & Algorithms", "CS Fundamentals", "Core building blocks for efficient software."),
    ("discrete_math", "Discrete Math", "CS Fundamentals", "Mathematical foundations behind computer science."),
    ("systems_design", "Systems Design", "CS Fundamentals", "Designing software architecture that scales and stays reliable."),
    ("databases_theory", "Database Theory", "CS Fundamentals", "Relational theory, normalization, transactions and indexing."),
    ("distributed_systems", "Distributed Systems", "CS Fundamentals", "Designing systems that span multiple machines reliably."),
]

    ("monitoring_and_observability", "Monitoring & Observability", "Internal Academy", "Intermediate", 8, "https://example.com/courses/monitoring", ["monitoring_observability"], ["linux"]),
    ("computer_networking_basics", "Computer Networking Basics", "edX", "Beginner", 10, "https://example.com/courses/networking-basics", ["computer_networking"], []),
    ("application_security_fundamentals", "Application Security Fundamentals", "O'Reilly", "Intermediate", 12, "https://example.com/courses/appsec-fundamentals", ["application_security"], ["rest_apis"]),
    ("cryptography_basics_course", "Cryptography Basics", "edX", "Intermediate", 10, "https://example.com/courses/cryptography-basics", ["cryptography_basics"], ["discrete_math"]),
    ("threat_modeling_workshop", "Threat Modeling Workshop", "Internal Academy", "Advanced", 8, "https://example.com/courses/threat-modeling", ["threat_modeling"], ["application_security"]),
    ("identity_access_management_course", "Identity & Access Management", "O'Reilly", "Intermediate", 8, "https://example.com/courses/iam", ["identity_access_management"], ["application_security"]),
    ("ui_design_foundations", "UI Design Foundations", "Coursera", "Beginner", 10, "https://example.com/courses/ui-design-foundations", ["ui_design", "typography"], []),
    ("figma_for_product_design", "Figma for Product Design", "Coursera", "Beginner", 8, "https://example.com/courses/figma", ["figma", "prototyping"], ["ui_design"]),
    ("design_systems_at_scale", "Design Systems at Scale", "Internal Academy", "Advanced", 12, "https://example.com/courses/design-systems", ["design_systems"], ["figma"]),
    ("ux_research_methods", "UX Research Methods", "Coursera", "Intermediate", 12, "https://example.com/courses/ux-research", ["ux_research", "user_research"], []),
    ("accessibility_in_design", "Accessibility in Design", "Coursera", "Intermediate", 8, "https://example.com/courses/accessibility", ["accessibility"], ["ui_design"]),
    ("product_strategy_essentials", "Product Strategy Essentials", "Reforge", "Intermediate", 10, "https://example.com/courses/product-strategy", ["product_strategy", "roadmapping"], []),
    ("ab_testing_for_product_teams", "A/B Testing for Product Teams", "Reforge", "Intermediate", 8, "https://example.com/courses/ab-testing", ["ab_testing"], ["statistics"]),
    ("stakeholder_management_course", "Stakeholder Management", "LinkedIn Learning", "Beginner", 6, "https://example.com/courses/stakeholder-management", ["stakeholder_management", "communication"], []),
    ("agile_scrum_certification", "Agile & Scrum Certification", "Scrum Alliance", "Beginner", 8, "https://example.com/courses/agile-scrum", ["agile_scrum", "project_management"], []),
    ("technical_writing_workshop", "Technical Writing Workshop", "LinkedIn Learning", "Beginner", 6, "https://example.com/courses/technical-writing", ["technical_writing"], []),
    ("public_speaking_for_engineers", "Public Speaking for Engineers", "LinkedIn Learning", "Beginner", 6, "https://example.com/courses/public-speaking", ["public_speaking"], []),
    ("mentoring_and_leadership", "Mentoring & Leadership", "Internal Academy", "Intermediate", 8, "https://example.com/courses/mentoring", ["mentoring"], ["communication"]),
    ("market_analysis_for_pms", "Market Analysis for Product Managers", "Reforge", "Intermediate", 8, "https://example.com/courses/market-analysis", ["market_analysis"], ["product_strategy"]),
]
