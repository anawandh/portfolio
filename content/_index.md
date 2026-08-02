---
name: "Aditya Nawandhar"
subtitle: "CS & Math Student at Purdue University | Incoming Software Engineering Intern at Walmart"
bio: "Hi, I'm Aditya. I am a Computer Science and Mathematics undergraduate at Purdue University, with a passion for software systems, CI/CD optimization, and machine learning. I've designed distributed systems, automated hardware performance analysis workflows, and built developer infrastructure through my internships at Walmart, Intel, and ModalAI."

contact_links:
  - text: "anawandh@purdue.edu"
    url: "mailto:anawandh@purdue.edu"
  - text: "LinkedIn"
    url: "https://www.linkedin.com/in/aditya-nawandhar"
  - text: "GitHub"
    url: "https://github.com/anawandh"
  - text: "Resume"
    url: "/documents/resume.pdf"

education:
  - institution: "Purdue University"
    location: "West Lafayette, IN"
    degree: "Bachelor of Science in Computer Science & Mathematics"
    date: "Expected May 2028"
    details: "**Leadership:** Software Lead, Purdue IEEE ROV (Remotely Operated Vehicle) Team"

experience:
  - title: "Software Engineering Intern"
    company: "Walmart Global Tech • Sunnyvale, CA"
    date: "Jun 2026 – Aug 2026"
    bullets:
      - "Incoming Software Engineering Intern at Walmart Global Tech."

  - title: "Software Engineering Intern"
    company: "Intel Corporation • San Diego, CA"
    date: "May 2025 – Aug 2025"
    bullets:
      - "Reduced manual workload by 70% and cut runtime setup time by over 50% by automating GPU power estimation workflows using Python and the Jenkins API, integrating ZTDB/netlist data from 3+ external teams."
      - "Parsed over 20GB of emulation data from GPU architecture workloads (e.g., Cyberpunk 2077) to extract and categorize 8,000+ clockgate and register cells based on functionality clusters to create clock tree structure."
      - "Achieved a 30% reduction in design review time by creating dynamic PowerBI pivot tables and visualizations to identify inefficient register and clockgate placements and architectural bottlenecks."
      - "Analyzed 10,000+ buffer and functional cells through a robust TCL script to extract physical placement data and other cell characteristics, uncovering 3+ high-latency paths/placements caused by suboptimal clustering."

  - title: "Software Engineering Intern"
    company: "ModalAI Inc. • San Diego, CA"
    date: "Jun 2023 – Aug 2024"
    bullets:
      - "Increased test throughput by 500+ tests daily by optimizing the testing environment and CI/CD pipeline using Docker, Grafana, and Python scripts, enabling faster bug identification."
      - "Saved 4+ hours of manual work weekly by automating production tasks with Python scripts that generate XLS files for DHL and FedEx shipping orders."
      - "Handled 50% of the VOXL migration from LU1 to LU2.0 (Ubuntu 18 to 20) by using BitBake and C to set up GPIOs, enable wireless connectivity, and debug critical dependency errors."

  - title: "Software Intern"
    company: "Shifting Orbits Foundation • Bangalore, India"
    date: "Jun 2022 – Aug 2022"
    bullets:
      - "Organized and cleaned large datasets using Excel, CSV files, and SQL, improving data accuracy and usability."
      - "Eliminated garbage data and conducted data analysis using Python and the Pandas library, leading to actionable insights and data-driven conclusions."
      - "Collaborated with software engineers to design and develop frontend web pages, enhancing user interface and experience."

projects:
  - title: "Purdue IEEE ROV (X18 Core & Surface)"
    description: "Guided software development for an underwater vehicle. Designed real-time ROS2 nodes on Raspberry Pi 4 communicating with STM32 microcontrollers via custom, CRC-32 validated UART packets, alongside a dashboard for telemetry and camera stream ingestion."
    tags:
      - "ROS2"
      - "C++"
      - "Python"
      - "UART"
      - "Raspberry Pi"
    links:
      - text: "Organization"
        url: "https://github.com/purduerov"
      - text: "Core/Backend"
        url: "https://github.com/purduerov/X18-Core"
      - text: "Surface/Frontend"
        url: "https://github.com/purduerov/X18-Surface"

  - title: "Spotify Del Norte"
    description: "A full-featured music streaming clone. Resolved complex cross-origin session authorization challenges by engineering a secure JWT authentication flow stored in secure HttpOnly cookies to mitigate XSS vulnerabilities."
    tags:
      - "Node.js"
      - "Express"
      - "React"
      - "JWT"
      - "Tailwind"
    links:
      - text: "Frontend"
        url: "https://github.com/aidenhuynh/cj_frontend"
      - text: "Backend"
        url: "https://github.com/aidenhuynh/cj_backend"

  - title: "Investopedia Clone"
    description: "A stock simulator platform replicating the Investopedia trading experience. Integrated Yahoo Finance API for real-time tracking and trained an LSTM deep learning model to forecast price paths (AAPL, MSFT) with 75-80% accuracy."
    tags:
      - "Java"
      - "Spring Boot"
      - "AWS RDS"
      - "LSTM"
      - "Tailwind"
    links:
      - text: "Frontend"
        url: "https://github.com/CSA-AI/CSA_AI_Frontend"
      - text: "Backend"
        url: "https://github.com/CSA-AI/CSA_AI_Backend"

  - title: "Bublur"
    description: "A collaborative real-time social platform where users submit answers to random topics. Structured REST APIs for community posts and deployed backend database indexing for performance on Google Cloud."
    tags:
      - "Python"
      - "Flask"
      - "PostgreSQL"
      - "GCP"
      - "Tailwind"
    links:
      - text: "Organization Repositories"
        url: "https://github.com/orgs/Crimson-Nebula/repositories"

skills:
  - category: "Languages"
    items:
      - "Java"
      - "Python"
      - "C / C++"
      - "SQL (PostgreSQL)"
      - "JavaScript / HTML / CSS"
      - "R"
      - "Bash"
      - "SystemVerilog"
      - "TCL"

  - category: "Frameworks"
    items:
      - "React"
      - "Node.js"
      - "Flask"
      - "Spring Boot"
      - "Tailwind CSS"
      - "Sails.js"
      - "FastAPI"

  - category: "Tools & Infra"
    items:
      - "Git & GitHub"
      - "Docker"
      - "Google Cloud Platform (GCP)"
      - "AWS"
      - "BitBake"
      - "Firebase"
      - "PowerBI"
      - "Agile / Scrum"
      - "CI/CD & TDD"

cta:
  text: "Want to talk about collaboration or opportunities?"
  buttons:
    - text: "Get in Touch"
      url: "/contact/"
      class: "btn-secondary"
    - text: "Read My Blogs"
      url: "/post/"
      class: "btn-primary"
---
