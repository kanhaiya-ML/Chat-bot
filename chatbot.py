from groq import AsyncGroq
import os
from dotenv import load_dotenv
load_dotenv()

client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))

async def chat(history: list, new_message: str, context: str = "") -> str:
    messages = [
        {"role": "system", "content": "You are a helpful conversational AI assistant. Be concise and friendly. When web search results are provided, use them as your primary source and present the information confidently without disclaimers about knowledge cutoffs."}
    ] + history

    if context:
        messages.append({"role": "system", "content": f"Use this information to answer the user:\n{context}"})

    messages.append({"role": "user", "content": new_message})

    response = await client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    return response.choices[0].message.content


async def generate_title(new_message: str):
    title = [
        {"role": "system","content":"write a short 1-4 words title in context of user message and just return title"}
    ] + [
        {"role":"user","content":new_message}
    ]
    response = await client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=title
)
    return response.choices[0].message.content


async def generate_subquestions(query: str):
    sub_question = [
        {"role":"system","content":"Generate 3 sub-questions for the given query. Return only the questions, one per line, no numbering, no extra text."}
    ] + [
        {"role":"user","content":query}
    ]
    response = await client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=sub_question
    )
    questions = response.choices[0].message.content.strip().split("\n")
    questions = [q.strip() for q in questions if q.strip()]
    return questions[:3]

