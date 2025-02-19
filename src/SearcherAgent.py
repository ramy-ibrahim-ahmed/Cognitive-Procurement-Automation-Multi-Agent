import os
from typing import List

from crewai import Agent, Task
from crewai.tools import tool
from tavily import TavilyClient
from pydantic import BaseModel, Field

from src.config import get_settings
from src.Brain import brain

settings = get_settings()
client = TavilyClient(api_key=settings.TAVILY_API_KEY)


class SignleSearchResult(BaseModel):
    title: str
    url: str = Field(..., title="the page url")
    content: str
    score: float
    search_query: str


class AllSearchResults(BaseModel):
    results: List[SignleSearchResult]


@tool
def search_engine_tool(query: str):
    """Useful for search-based queries. Use this to find current information about any query related pages using a search engine"""
    return client.search(query)


SearcherAgent = Agent(
    role="Search Engine Agent",
    goal="To search for products based on the suggested search queries",
    backstory="The agent is designed to help in looking for products by searching for products based on the suggested search queries.",
    llm=brain,
    verbose=True,
    tools=[search_engine_tool],
)

SearcherTask = Task(
    description="\n".join(
        [
            "The task is to search for products based on a provided list of search queries.",
            "You must process **ALL** search queries provided in the input list; do not limit your search to only a couple of queries.",
            "For each query, perform a search using the `search_engine_tool`.",
            "Filter out any suspicious links or results that do not come from a valid ecommerce single product website.",
            "Ignore any search results with a confidence score lower than ({score_th}).",
            "Combine and return the valid search results from all queries as a single JSON object.",
            "The consolidated search results will later be used to compare product prices across different websites.",
        ]
    ),
    expected_output="A JSON object containing the search results.",
    output_json=AllSearchResults,
    output_file=os.path.join(settings.OUTPUT_DIR, "step_2_search_results.json"),
    agent=SearcherAgent,
)
