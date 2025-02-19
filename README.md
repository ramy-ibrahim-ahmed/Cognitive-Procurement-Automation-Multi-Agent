# Cognitive Procurement Automation (Multi-Agent)

A CrewAI-based solution to automate product procurement research, price comparison, and report generation.

## Project Overview

This project utilizes multiple AI agents working in sequence to:

1. Generate targeted search queries
2. Perform web searches for products
3. Scrape and extract product details
4. Generate a professional procurement report

### Key Components

- **QueriesAgent**: Generates optimized search queries for product research
- **SearcherAgent**: Performs web searches and filters results
- **ScraperAgent**: Extracts product details from e-commerce pages
- **ReportAgent**: Compiles findings into a structured Markdown report

## Project Structure

```code
procurement-ai/
├── src/
│   ├── Brain.py           # LLM configuration
│   ├── config.py          # Environment configuration
│   ├── QueriesAgent.py    # Search query generation
│   ├── SearcherAgent.py   # Web search functionality
│   ├── ScraperAgent.py    # Product data extraction
│   ├── ReportAgent.py     # Report generation
│   └── main.py            # Crew orchestration
├── .env                   # Environment variables
└── Results.md             # Sample output report
```

### Set Up Environment Variables (.env)

   ```ini
   AGENTOPS_API_KEY=your_agentops_key
   TAVILY_API_KEY=your_tavily_key
   SCRAPEGRAPG_PY_API_KEY=your_scrapegraph_key
   LLM=ollama/deepseek-r1:8b
   NUM_SEARCH_QUERIES=5
   OUTPUT_DIR=./output
   ```

### Tools providers and Agents tracking

| Service     | Purpose          | API Key Source                            |
| ----------- | ---------------- | ----------------------------------------- |
| Tavily      | Web searches     | [Tavily AI](https://tavily.com/)          |
| Scrapegraph | Web scraping     | [Scrapegraph](https://scrapegraphai.com/) |
| AgentOps    | Agent monitoring | [AgentOps](https://agentops.ai/)          |

### Run the procurement crew

```python
python src/main.py
```

**Input Parameters:**

- `product_name`: "coffee machine for the office"
- `websites_list`: ["www.amazon.com", "www.jumia.com"]
- `country_name`: "USA"
- `language`: "English"

## Sample Report

---

# Procurement Report: Coffee Makers

## Executive Summary

This report outlines the procurement process for selecting high-quality coffee makers based on specified criteria, including ratings, price, and popularity. The analysis presents key findings and recommendations to support informed decision-making.

## Introduction

The task involves evaluating and selecting coffee makers that offer optimal value, performance, and features. This report provides a structured overview of the evaluation process, findings, and final recommendations.

## Methodology

### Data Collection

A comprehensive review was conducted on five coffee maker models, sourced from various retailers. Data points including price, ratings, specs, and popularity were collected for analysis.

### Analysis Criteria

Products were evaluated based on:

- **Rating (descending)**: Higher-rated products were prioritized
- **Price (ascending)**: Cheaper options were considered unless performance was compromised
- **Popularity (descending)**: More sought-after products were preferred

---

## Findings

### Product Overview

| Product ID | Title                                      | Price   | Rating | Specs                                      | Recommendation Rank |
| ---------- | ------------------------------------------ | ------- | ------ | ------------------------------------------ | ------------------- |
| 1          | Espresso Coffee Machine - Best Price       | $129.99 | 4.8    | Stainless Steel, Water Filter, Thermoblock | 2                   |
| 2          | Keurig Coffee Maker - K Cup Compatible     | $119.99 | 4.7    | 8oz Water Tank, Brew Time Adjustment       | 5                   |
| 3          | Espresso Coffee Machine - Single Shot      | $199.99 | 4.6    | Grinder, No Milk Frother                   | 3                   |
| 4          | Breville Espresso Maker - Professional Use | $299.99 | 4.5    | 15bar Pressure, Bean Grinder               | 1                   |
| 5          | Breville Espresso Maker - Best Price       | $199.99 | 4.4    | 10bar Pressure, Water Filter               | 4                   |

## Analysis

- **Breville Espresso Maker (Professional Use)** ranked highest due to superior performance and advanced features
- **Espresso Coffee Machine - Best Price** offered good value for its price point
- **Keurig Coffee Maker** was the most affordable option with decent reviews

## Recommendations

1. **Top Recommendation**: Breville Espresso Maker - Professional Use (Rank 1)
   - **Reason**: Exceptional performance and high-rated features justify the investment
2. **Second Choice**: Espresso Coffee Machine - Best Price (Rank 2)
   - **Reason**: Offers a balance of cost-effectiveness and reliable functionality
3. **Third Recommendation**: Espresso Coffee Machine - Single Shot (Rank 3)
   - **Reason**: Strong performance for home use with essential features

## Conclusion

The procurement process identified high-quality coffee makers that cater to various needs and budgets. Prioritizing ratings and performance ensures long-term satisfaction. The top recommendation is the Breville Espresso Maker for professional use, offering exceptional features at a higher price point.

---
