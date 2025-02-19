import os
from typing import List

from crewai import Agent, Task
from crewai.tools import tool
from scrapegraph_py import Client
from pydantic import BaseModel, Field

from src.config import get_settings
from src.Brain import brain

settings = get_settings()
client = Client(api_key=settings.SCRAPEGRAPG_PY_API_KEY)


class ProductSpec(BaseModel):
    specification_name: str
    specification_value: str


class SingleExtractedProduct(BaseModel):
    page_url: str = Field(..., title="The original URL of the product page")
    product_title: str = Field(..., title="The title of the product")
    product_image_url: str = Field(..., title="The URL of the product image")
    product_url: str = Field(..., title="The URL of the product")
    product_current_price: float = Field(..., title="The current price of the product")
    product_original_price: float = Field(
        title="The original price of the product before discount. Set to None if no discount",
        default=None,
    )
    product_discount_percentage: float = Field(
        title="The discount percentage of the product. Set to None if no discount",
        default=None,
    )
    product_specs: List[ProductSpec] = Field(
        ...,
        title="The key specifications of the product for comparison.",
        min_items=1,
        max_items=5,
    )
    agent_recommendation_rank: int = Field(
        ...,
        title="The rank (out of 5) for the product in the final procurement report, with 5 being the best.",
    )
    agent_recommendation_notes: List[str] = Field(
        ...,
        title="Notes explaining the recommendation (or lack thereof) for the product compared to others.",
    )


class AllExtractedProducts(BaseModel):
    products: List[SingleExtractedProduct]


@tool
def web_scraping_tool(page_url: str):
    """
    Web Scraping Tool

    This tool accepts a URL from an ecommerce product page and utilizes the SmartScraper API
    to extract detailed product information. The extraction follows the JSON schema defined by
    the `SingleExtractedProduct` model. The output includes the original URL and a dictionary of
    extracted product details, which will later be used to rank and filter the best products.

    Parameters:
        page_url (str): The URL of the ecommerce product page to scrape.

    Returns:
        dict: A dictionary containing:
            - 'page_url': The original URL provided.
            - 'details': The JSON data extracted from the webpage following the expected schema.
    """
    details = client.smartscraper(
        website_url=page_url,
        user_prompt="Extract ```json\n"
        + SingleExtractedProduct.schema_json()
        + "```\n From the web page",
    )

    return {"page_url": page_url, "details": details}


ScraperAgent = Agent(
    role="Web scraping agent",
    goal="To extract detailed product information from ecommerce websites for further product ranking and recommendation.",
    backstory="The agent is designed to gather product details from various ecommerce pages. It will iterate through a list of search queries, scrape multiple page URLs for each query, and compile the data for product recommendation analysis.",
    llm=brain,
    tools=[web_scraping_tool],
    verbose=True,
)

ScraperTask = Task(
    description="\n".join(
        [
            "The task is to extract product details from ecommerce store page URLs based on multiple search queries.",
            "For each query provided, the agent must scrape multiple page URLs to collect comprehensive product details.",
            "After extraction, the agent should filter and rank the products to compile the top {top_recommendations_no} recommendations.",
            "Ensure that all queries from the given list are processed and no query is omitted.",
        ]
    ),
    expected_output="A JSON object containing the extracted products' details along with a ranked recommendation list.",
    output_json=AllExtractedProducts,
    output_file=os.path.join(settings.OUTPUT_DIR, "step_3_search_results.json"),
    agent=ScraperAgent,
)
