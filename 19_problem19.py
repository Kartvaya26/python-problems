def emoji_translator(text):
    emoji_dict = {
        "happy": "😊",
        "sad": "😢",
        "heart": "❤️",
    }

    words = text.split()

    translator = [emoji_dict.get(word, word) for word in words]
    
    return " ".join(translator)

input_text = "I am happy and my heart is full"

print(emoji_translator(input_text))