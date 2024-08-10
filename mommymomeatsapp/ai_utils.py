import json
import os
import openai
from django.http import HttpResponse
from dotenv import load_dotenv

# 환경 변수 설정
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_food_data(food_name):
    prompt = f"""
    Please provide the nutritional facts for the food '{food_name}' during pregnancy.
    Respond only with a JSON object. Must contain the 3 following keys:
    1. "name": the name of the food
    2. "ingredients": a list of ingredients, each as an object with:
        - "name": the name of the ingredient
        - "potential_risks": a list of risk levels during pregnancy, each as an object with:
            - "week_start": the starting week of the pregnancy when this risk is relevant
            - "week_end": the ending week of the pregnancy when this risk is relevant
            - "risk_level": the level of risk during this period (e.g., "low", "medium", "high")
    3. "kcal": the total kcal for the food

    The response should be a valid JSON object. Do not include any additional text or explanation.

    response example:
    {{
        "name": "Apple",
        "ingredients": [
            {{
                "name": "Vitamin C",
                "potential_risks": [
                    {{"week_start": 1, "week_end": 12, "risk_level": "low"}},
                    {{"week_start": 13, "week_end": 28, "risk_level": "medium"}},
                    {{"week_start": 29, "week_end": 40, "risk_level": "high"}}
                ]
            }},
            {{
                "name": "Sugar",
                "potential_risks": [
                    {{"week_start": 1, "week_end": 40, "risk_level": "high"}}
                ]
            }}
        ],
        "kcal": 52
    }}
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )

    # 응답 데이터 파싱
    generated_data = response.choices[0]['message']['content'].strip()

    # 응답 데이터를 JSON으로 변환
    try:
        food_data = json.loads(generated_data)

        # 필수 키가 모두 있는지 확인
        if 'name' not in food_data or 'ingredients' not in food_data or 'kcal' not in food_data:
            raise ValueError("Missing essential keys in the JSON response")
    except (json.JSONDecodeError, ValueError) as e:
        # JSON 형식이 잘못되었거나 필수 키가 없을 경우 예외 처리
        return HttpResponse("Error processing the request. Please try again.", status=400)

    return food_data
