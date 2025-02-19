from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    AGENTOPS_API_KEY: str
    TAVILY_API_KEY: str
    SCRAPEGRAPG_PY_API_KEY: str
    NUM_SEARCH_QUERIES: int
    OUTPUT_DIR: str

    class Config:
        env_file = r".env"


def get_settings():
    return Settings()
