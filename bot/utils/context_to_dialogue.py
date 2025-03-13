def context_to_dialogue(context: list):
    dialogue = []
    for replica in context:
        role, text = replica
        if role == "user":
            dialogue.append(f"Пользователь: {text}")
        elif role == "assistant":
            dialogue.append(f"Твой ответ: {text}")
    return '\n'.join(dialogue)
