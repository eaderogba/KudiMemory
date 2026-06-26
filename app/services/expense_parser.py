# app/services/expense_parser.py

import json
from pathlib import Path
from openai import OpenAI
from app.config import config

client = OpenAI(base_url=config.OLLAMA_BASE_URL, api_key="ollama")

PROMPTS_DIR = Path(__file__).parent.parent.parent / "prompts"

def load_prompt(input_type: str) -> str:
    base_prompt = (
        PROMPTS_DIR / "base" / "base_v1.txt"
    ).read_text(encoding="utf-8")
    
    input_prompt = (
        PROMPTS_DIR / input_type / f"{input_type}_v1.txt"
    ).read_text(encoding="utf-8")
    
    
    return base_prompt + "\n\n" + input_prompt

def parse_expense(text: str,
                  input_type: str = "typed_message") -> dict | None:
    try:
        prompt = load_prompt(input_type)

        response = client.chat.completions.create(
            model=config.OLLAMA_MODEL,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": text}
            ]
        )

        content = response.choices[0].message.content
        
        # Defensive: strip markdown fences if LLM added them
        content = content.strip()
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()


        parsed = json.loads(content)
        return parsed
        
    except json.JSONDecodeError as e:
        print(f"Error: The LLM did not return valid JSON. {e}")
        return None
    
    except Exception as e:
        print(f"Expense parser failed: {e}")
        return None