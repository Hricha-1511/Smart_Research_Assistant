import os
from langchain_openai import ChatOpenAI
# from config.config import OPENAI_API_KEY

def get_openai_model():
    """Initialize and return OpenRouter model"""

    try:
        llm = ChatOpenAI(
            model="openai/gpt-4o-mini",   # OpenRouter model name
            # api_key=OPENAI_API_KEY,
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
        )

        return llm

    except Exception as e:
        raise RuntimeError(f"Failed to initialize OpenRouter model: {str(e)}")