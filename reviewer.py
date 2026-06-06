from groq import AsyncGroq
import os
from dotenv import load_dotenv
load_dotenv()


client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))

async def review_code(code: str, question: str):
    message = [
        {"role":"system","content":'''You are an expert code reviewer. Analyze the provided code and return ONLY a JSON object with no extra text, no markdown, no code blocks. The JSON must follow this exact structure:
json{
  "bugs": ["bug1", "bug2"],
  "security_issues": ["issue1", "issue2"],
  "quality_score": 8,
  "quality_explanation": "brief explanation of the score",
  "suggestions": ["suggestion1", "suggestion2"],
  "refactored_code": "improved version of the code"
}
If there are no bugs or security issues, return empty arrays. Quality score is out of 10. Never return anything outside the JSON object.'''}
    ] + [
        {"role":"user","content":f"Code:\n{code}\n\nQuestion: {question}"}
    ]

    response = await client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=message
    )
    return response.choices[0].message.content