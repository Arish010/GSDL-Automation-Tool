GSDL Data Mapping Automation Tool
The GSDL Data Mapping Automation Tool is an internal automation solution developed during my internship at GSDL, aimed at simplifying the complex process of handling large volumes of data across multiple departments. Built collaboratively with a team of analysts and engineers, the tool automates the transformation of 50–80 unstructured Excel files into clean, standardized CSVs, reducing manual effort, increasing reliability, and significantly enhancing the productivity of downstream data teams.

🚀 Key Features:
Automated Data Pipeline -
Converts large batches of Excel spreadsheets into structured CSV format in a single run. Eliminates repetitive manual formatting and validation steps.

Data Standardization & Cleaning -
Utilizes Pandas and NumPy to detect inconsistencies, handle missing data, normalize column structures, and ensure uniform output formats.

Productivity Enhancement -
Reduced manual data preparation efforts by over 50%, enabling analysts to focus more on insights and strategy rather than cleanup.

Visual Feedback & Reporting -
Generates visual summaries and transformation logs to ensure transparency and track changes.

Seamless Integration with Databases -
Outputs are structured to integrate easily into PostgreSQL or other relational databases, feeding into analytics dashboards and business intelligence pipelines.

User-Friendly Interface -
A lightweight Kivy-based GUI allows team members with minimal coding experience to use the tool efficiently.

Tech Stack -
Python – Core language for scripting and logic

Pandas & NumPy – Data manipulation and transformation

Matplotlib – Visualizations and QA feedback

PostgreSQL – Downstream database compatibility

Kivy – GUI development for ease of use

Project Impact -
This tool was designed with scalability and business value in mind. By automating one of the most time-consuming processes in our data operations—manual Excel formatting—we helped the business transition to a more data-driven, reliable, and efficient workflow. The tool has the potential to be scaled across different business units handling repetitive data ingestion tasks.

Example Use Case
Scenario:
A company receives weekly reports in Excel from 10+ departments, each with different formatting styles, inconsistent headers, and duplicate data. Analysts spend hours cleaning and aligning these files before importing into dashboards.

With this tool:
All Excel files are automatically processed, cleaned, standardized, and exported into a unified format, ready to be analyzed or loaded into the central database—saving dozens of hours per month.

Team Contribution
This project was developed in collaboration with a cross-functional team during my internship. I led the development of the data cleaning pipeline and contributed heavily to GUI development and deployment configuration.