from crewai import LLM

from src.config import get_settings

settings = get_settings()

brain = LLM(
    model="ollama/deepseek-r1:8b",
    base_url="http://localhost:11434",
)
