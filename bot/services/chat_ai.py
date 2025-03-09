from yandex_cloud_ml_sdk import YCloudML

from bot.config import YC_OAUTH_TOKEN, YC_FOLDER_ID


# Создаём клиент для работы с ML API
sdk = YCloudML(
    folder_id=YC_FOLDER_ID,
    auth=YC_OAUTH_TOKEN
)
# Настройка модели
model = sdk.models.completions("yandexgpt-lite")
model = model.config(temperature=0.7) # TODO: Сделать настройку температуры динамичной (эмоции перса)

# Обращение к модели
def get_ai_response(user_input: str) -> str:
    """Обращается к Yandex Cloud ML API для генерации текста"""
    response = model.run(
        messages=[
            {
                "role": "system",
                "text": """
                1. You communicate only in English.
                1.1. If you detect any other language then English, you reply with 'Vanechkin! English!'.
                2. Your name is Max.
                3. Your task is to chat and support vibes, not to resolve problems.
                4. You are form the UK and like to remember interesting facts about it rarely, where it fits into the dialogue.
                5. Your latest adventure was traveling from the head of the Thames to the sea, you like to remember it occasionally, where it fits into the dialogue.
                """
            },
            {
                "role": "user",
                "text": user_input
            }
        ]
    )
    return response.alternatives[0].text
