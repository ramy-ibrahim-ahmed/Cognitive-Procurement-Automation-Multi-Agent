import os

from crewai import Agent, Task

from src.config import get_settings
from src.Brain import brain

settings = get_settings()

ReportAgent = Agent(
    role="Procurement Report Markdown Author Agent",
    goal="To generate a professional Markdown document for the procurement report",
    backstory=(
        "The agent is designed to assist in generating a professional Markdown document "
        "for the procurement report after reviewing a list of products."
    ),
    llm=brain,
    verbose=True,
)

ReportTask = Task(
    description="\n".join(
        [
            "The task is to generate a professional Markdown document for the procurement report.",
            "Utilize Markdown formatting to structure the report clearly and effectively.",
            "Use the provided context about the company to tailor the report.",
            "The report will include search results and product prices from various websites.",
            "Structure the report with the following sections:",
            "1. **Executive Summary**: A brief overview of the procurement process and key findings.",
            "2. **Introduction**: An introduction to the purpose and scope of the report.",
            "3. **Methodology**: A description of the methods used to gather and compare prices.",
            "4. **Findings**: Detailed comparison of prices from different websites, including tables and charts.",
            "5. **Analysis**: An analysis of the findings, highlighting any significant trends or observations.",
            "6. **Recommendations**: Suggestions for procurement based on the analysis.",
            "7. **Conclusion**: A summary of the report and final thoughts.",
            "8. **Appendices**: Additional information such as raw data or supplementary materials.",
        ]
    ),
    expected_output="A professional Markdown document for the procurement report.",
    output_file=os.path.join(settings.OUTPUT_DIR, "step_4_procurement_report.md"),
    agent=ReportAgent,
)
