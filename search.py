from duckduckgo_search import DDGS
from tavily import TavilyClient
from chatbot import generate_subquestions
import os
from dotenv import load_dotenv
load_dotenv()

# def web_search(query: str):
    # with DDGS() as ddgs:
    #     results = list(ddgs.text(query, max_results=5))
    #     output = ""
    #     for r in results:
    #         output += f"Title: {r['title']}\nSummary: {r['body']}\nURL: {r['href']}\n\n"
    #     return output

def web_search(query: str):
    tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    response = tavily_client.search(query, max_results=3,search_depth="advanced")
    
    output = ""
    if response['results']:
        for r in response["results"]:
            output += f"Title: {r['title']}\n"
            output += f"Summary: {r['content']}\n\n"
    return output


async def deep_research(query: str):
    questions = await generate_subquestions(query)

    all_results = ""
    for question in questions:
        result = web_search(question)
        all_results += f"Question: {question}\n{result}\n\n"
    return all_results
    