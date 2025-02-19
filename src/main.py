import os
import agentops
from crewai import Crew, Process
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

from src.config import get_settings
from src.QueriesAgent import QueriesAgent, QueriesTask
from src.SearcherAgent import SearcherAgent, SearcherTask
from src.ScraperAgent import ScraperAgent, ScraperTask
from src.ReportAgent import ReportAgent, ReportTask

settings = get_settings()
os.makedirs(settings.OUTPUT_DIR, exist_ok=True)

agentops.init(
    api_key=settings.AGENTOPS_API_KEY,
    skip_auto_end_session=True,
)

about_company = "AQJan is a company that provides AI solutions to help websites refine their search and recommendation systems."
company_context = StringKnowledgeSource(content=about_company)

AQJan_crew = Crew(
    agents=[
        QueriesAgent,
        SearcherAgent,
        ScraperAgent,
        ReportAgent,
    ],
    tasks=[
        QueriesTask,
        SearcherTask,
        ScraperTask,
        ReportTask,
    ],
    process=Process.sequential,
    knowledge_sources=[company_context],
)

crew_results = AQJan_crew.kickoff(
    inputs={
        "product_name": "coffee machine for the office",
        "websites_list": [
            "www.amazon.com",
            "www.jumia.com",
        ],
        "country_name": "USA",
        "no_keywords": settings.NUM_SEARCH_QUERIES,
        "language": "English",
        "score_th": 0.7,
        "top_recommendations_no": 5,
    }
)
