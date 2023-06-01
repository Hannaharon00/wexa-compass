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
    ("javascript", "JavaScript", "Programming Languages", "The language of the web browser, also used server-side via Node.js."),
    ("typescript", "TypeScript", "Programming Languages", "A statically typed superset of JavaScript."),
    ("go", "Go", "Programming Languages", "Compiled language popular for backend services and infrastructure tooling."),
    ("java", "Java", "Programming Languages", "Long-standing enterprise and Android language."),
    ("sql", "SQL", "Programming Languages", "Query language for relational databases."),
    ("rust", "Rust", "Programming Languages", "Systems language focused on memory safety and performance."),
    ("bash_scripting", "Bash Scripting", "Programming Languages", "Shell scripting for automation on Unix-like systems."),
    # Web & Frameworks
    ("react", "React", "Web & Frameworks", "Component-based UI library for building web frontends."),
    ("nodejs", "Node.js", "Web & Frameworks", "JavaScript runtime for building backend services."),
    ("fastapi", "FastAPI", "Web & Frameworks", "Modern Python web framework for building APIs."),
    ("django", "Django", "Web & Frameworks", "Batteries-included Python web framework."),
    ("express", "Express.js", "Web & Frameworks", "Minimal Node.js web framework for building APIs."),
    ("nextjs", "Next.js", "Web & Frameworks", "React framework with server rendering and routing built in."),
    ("vue", "Vue.js", "Web & Frameworks", "Approachable frontend framework."),
    ("rest_apis", "REST API Design", "Web & Frameworks", "Designing resource-oriented HTTP APIs."),
    ("graphql", "GraphQL", "Web & Frameworks", "Query language and runtime for client-driven APIs."),
    # Data & ML
    ("statistics", "Statistics", "Data & ML", "Probability and inference, the foundation of data analysis."),
    ("machine_learning", "Machine Learning", "Data & ML", "Building models that learn patterns from data."),
    ("data_visualization", "Data Visualization", "Data & ML", "Communicating data findings visually."),
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

# (course_id, title, provider, level, duration_hours, url, teaches[], requires[])
COURSES = [
    ("python_fundamentals", "Python Fundamentals", "Codecademy", "Beginner", 12, "https://example.com/courses/python-fundamentals", ["python"], []),
    ("python_intermediate", "Intermediate Python", "Codecademy", "Intermediate", 16, "https://example.com/courses/python-intermediate", ["python", "data_structures_algorithms"], ["python"]),
    ("python_for_data_analysis", "Python for Data Analysis", "Coursera", "Intermediate", 14, "https://example.com/courses/python-data-analysis", ["pandas", "data_visualization"], ["python"]),
    ("statistics_for_data_science", "Statistics for Data Science", "edX", "Beginner", 10, "https://example.com/courses/statistics-for-ds", ["statistics"], []),
    ("intro_machine_learning", "Introduction to Machine Learning", "Coursera", "Intermediate", 20, "https://example.com/courses/intro-ml", ["machine_learning"], ["python", "statistics"]),
    ("deep_learning_specialization", "Deep Learning Specialization", "Coursera", "Advanced", 30, "https://example.com/courses/deep-learning", ["deep_learning", "nlp"], ["machine_learning"]),
    ("sql_fundamentals", "SQL Fundamentals", "Codecademy", "Beginner", 8, "https://example.com/courses/sql-fundamentals", ["sql"], []),
    ("data_modeling_essentials", "Data Modeling Essentials", "Pluralsight", "Intermediate", 10, "https://example.com/courses/data-modeling", ["data_modeling", "databases_theory"], ["sql"]),
    ("data_warehousing_etl", "Data Warehousing & ETL", "Pluralsight", "Intermediate", 14, "https://example.com/courses/data-warehousing-etl", ["etl", "data_warehousing"], ["sql"]),
    ("javascript_fundamentals", "JavaScript Fundamentals", "freeCodeCamp", "Beginner", 10, "https://example.com/courses/javascript-fundamentals", ["javascript"], []),
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
# (before_course_id, after_course_id) -- before must be completed first
COURSE_PREREQUISITES = [
    ("python_fundamentals", "python_intermediate"),
    ("python_intermediate", "python_for_data_analysis"),
    ("python_intermediate", "fastapi_for_python_devs"),
    ("python_intermediate", "systems_design_for_engineers"),
    ("python_for_data_analysis", "intro_machine_learning"),
    ("statistics_for_data_science", "intro_machine_learning"),
    ("intro_machine_learning", "deep_learning_specialization"),
    ("sql_fundamentals", "data_modeling_essentials"),
    ("data_modeling_essentials", "data_warehousing_etl"),
    ("javascript_fundamentals", "typescript_for_js_devs"),
    ("javascript_fundamentals", "react_essentials"),
    ("javascript_fundamentals", "nodejs_backend"),
    ("react_essentials", "advanced_react_patterns"),
    ("react_essentials", "nextjs_fullstack"),
    ("nodejs_backend", "express_api_development"),
    ("rest_apis_placeholder", "graphql_api_design"),  # replaced below
    ("discrete_math_for_cs", "data_structures_deep_dive"),
    ("linux_command_line", "docker_fundamentals"),
    ("docker_fundamentals", "kubernetes_in_production"),
    ("docker_fundamentals", "ci_cd_pipelines"),
    ("aws_cloud_practitioner", "aws_solutions_architect"),
    ("aws_cloud_practitioner", "terraform_infrastructure_as_code"),
    ("application_security_fundamentals", "threat_modeling_workshop"),
    ("application_security_fundamentals", "identity_access_management_course"),
    ("ui_design_foundations", "figma_for_product_design"),
    ("ui_design_foundations", "accessibility_in_design"),
    ("figma_for_product_design", "design_systems_at_scale"),
    ("product_strategy_essentials", "market_analysis_for_pms"),
]
# express_api_development and fastapi_for_python_devs both teach rest_apis;
# graphql builds conceptually on REST API design, so it follows whichever
# REST course a learner path already includes -- modeled as following the
# Express course specifically to keep the chain concrete.
COURSE_PREREQUISITES = [
    p for p in COURSE_PREREQUISITES if p[0] != "rest_apis_placeholder"
] + [("express_api_development", "graphql_api_design")]

