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
    Please provide the nutritional facts and potential risks for the food '{food_name}' during pregnancy.
    Respond only with a JSON object containing the following keys:
    - "name" (the name of the food)
    - "ingredients" (a list of ingredients, each as an object with "name" and "potential_risk")
    - "kcal" (the total kcal for the food)
    Example(It's just example. Key is important, not value here.):
    {{
        "name": "Apple",
        "ingredients": [
            {{"name": "Vitamin C", "potential_risk": "low"}},
            {{"name": "Sugar", "potential_risk": "medium"}}
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
        max_tokens=150
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
