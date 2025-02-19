import os
from typing import List

from crewai import Agent, Task
from pydantic import BaseModel, Field

from src.config import get_settings
from src.Brain import brain

settings = get_settings()


class SuggestedSearchQueries(BaseModel):
    queries: List[str] = Field(
        ...,
        title="Suggested search queries to be passed to the search engine",
        min_items=1,
        max_items=settings.NUM_SEARCH_QUERIES,
    )


QueriesAgent = Agent(
    role="Search Queries Recommendation Agent",
    goal="\n".join(
        [
            "To provide a list of suggested search queries to be passed to the search engine.",
            "The queries must be varied and focused on specific items.",
        ]
    ),
    backstory="The agent is designed to help in looking for products by providing a list of suggested search queries to be passed to the search engine based on the context provided.",
    llm=brain,
    verbose=True,
)

QueriesTask = Task(
    description="\n".join(
        [
            "AQJan is looking to buy {product_name} at the best prices (value for a price strategy).",
            "The company targets any of these websites to buy from: {websites_list}.",
            "The company wants to reach all available products on the internet to be compared later in another stage.",
            "The stores must sell the product in {country_name}.",
            "Generate at maximum {no_keywords} queries.",
            "The search keywords must be in {language} language.",
            "Search keywords must contain specific brands, types, or technologies. Avoid general keywords.",
            "The search query must lead to an ecommerce webpage for a product, not a blog or listing page.",
            "Append the target website's name (from {websites_list}) at the end of each search query.",
        ]
    ),
    expected_output="A JSON object containing a list of suggested search queries.",
    output_json=SuggestedSearchQueries,
    output_file=os.path.join(
        settings.OUTPUT_DIR, "step_1_suggested_search_queries.json"
    ),
    agent=QueriesAgent,
)
