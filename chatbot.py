import spacy
import random
import spacy
import random

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define intents and responses
INTENTS = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning", "good evening"],
        "responses": ["Hello! How can I help you today?", "Hi there!", "Hey, nice to see you!"]
    },
    "farewell": {
        "patterns": ["bye", "goodbye", "see you", "take care"],
        "responses": ["Goodbye! Have a great day!", "See you later!", "Take care!"]
    },
    "thanks": {
        "patterns": ["thank you", "thanks", "appreciate it"],
        "responses": ["You're welcome!", "No problem!", "Happy to help!"]
    },
    "help": {
        "patterns": ["help", "what can you do", "assist"],
        "responses": ["I can answer questions, greet you, or help with basic queries. Try asking something like 'What's the weather?' or 'Tell me a joke!'"]
    },
    "joke": {
        "patterns": ["joke", "tell me a joke", "funny"],
        "responses": ["Why did the scarecrow become a programmer? Because he was outstanding in his field!", "What do you call a dinosaur that takes back its teeth? A Flossiraptor!"]
    },
    "weather": {
        "patterns": ["weather", "forecast", "how's the weather"],
        "responses": ["I don't have real-time weather data, but I can tell you to bring an umbrella if it looks cloudy!", "Check your local weather app for the latest forecast!"]
    }
}

def preprocess_text(text: str) -> str:
    """Clean and normalize input text."""
    return text.lower().strip()

def get_intent(text: str) -> str:
    """Identify intent from user input using spaCy similarity."""
    doc = nlp(preprocess_text(text))
    max_similarity = 0.0
    matched_intent = "unknown"
    
    for intent, data in INTENTS.items():
        for pattern in data["patterns"]:
            pattern_doc = nlp(pattern)
            similarity = doc.similarity(pattern_doc)
            if similarity > max_similarity and similarity > 0.6:  # Threshold for matching
                max_similarity = similarity
                matched_intent = intent
    
    return matched_intent

def get_response(intent: str) -> str:
    """Return a random response for the identified intent."""
    if intent in INTENTS:
        return random.choice(INTENTS[intent]["responses"])
    return "Sorry, I didn't understand that. Try something like 'tell me a joke' or 'help'!"

def chatbot():
    """Run the chatbot."""
    print("Chatbot: Hi! I'm your friendly AI assistant. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Bye! Have a great day!")
            break
        
        intent = get_intent(user_input)
        response = get_response(intent)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()