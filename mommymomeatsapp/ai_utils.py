import os
import openai
from dotenv import load_dotenv

# 환경 변수 설정
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_food_data(food_name):
    prompt = f"Please provide the nutritional facts and potential risks for the food '{food_name}' during pregnancy."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
            ],
        max_tokens=100
    )

    # 응답 데이터 파싱
    generated_data = response.choices[0].message['content'].strip()

    # TODO: 응답 데이터를 딕셔너리로 반환
    food_data = {
        'name': food_name,
        'ingredients': [
            {'name': 'Vitamin C', 'potential_risk': 'low'},
            {'name': 'Sugar', 'potential_risk': 'medium'}
        ],
        'kcal': 250
    }
    return food_data
