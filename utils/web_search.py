from serpapi import GoogleSearch
import os
# from config.config import SERPAPI_API_KEY

def web_search(query: str):

    params = {
        "engine": "google",
        "q": query,
        "api_key": os.getenv("SERPAPI_API_KEY"),
        # "api_key": SERPAPI_API_KEY,
        "num": 5
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()

        formatted_results = ""

        for result in results.get("organic_results", []):
            title = result.get("title", "")
            snippet = result.get("snippet", "")
            link = result.get("link", "")

            formatted_results += f"""
Title: {title}
Snippet: {snippet}
Link: {link}

"""

        return formatted_results

    except Exception as e:
        return f"Search error: {str(e)}"