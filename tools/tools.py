from urllib.parse import urlparse
from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name: str, platform: str = "linkedin") -> str:
    """
    Queries Tavily and returns either:
    - full profile URL for LinkedIn
    - username for Twitter (without @)
    """
    if platform.lower() == "linkedin":
        query = f"{name} site:linkedin.com/in"
    elif platform.lower() == "twitter":
        query = f"{name} site:twitter.com"
    else:
        return f"Unsupported platform: {platform}"

    search = TavilySearchResults()
    results = search.run(query)

    if not isinstance(results, list):
        return f"No {platform} profile found for {name}"

    platform_results = [r for r in results if platform.lower() in r.get("url", "").lower()]

    if not platform_results:
        return f"No {platform} profile found for {name}"

    sorted_results = sorted(platform_results, key=lambda r: r.get("score", 0), reverse=True)
    best_url = sorted_results[0]["url"]

    if platform.lower() == "twitter":
        parsed = urlparse(best_url)
        path_parts = parsed.path.strip("/").split("/")
        if path_parts and path_parts[0].lower() != "status":
            return path_parts[0] 
        elif len(path_parts) > 1 and path_parts[0].lower() == "status":
            return parsed.netloc 
        else:
            return "Twitter username not found"

    return best_url
