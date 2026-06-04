# ==========================================
# DecodeLabs - Project 1: Rule-Based AI Chatbot
# The Logic Engine - Built by Shahzaib
# ==========================================

def run_chatbot():
    print("========================================")
    print("=== LOGIC ENGINE INITIATED ===")
    print("System Online. Type 'exit' to trigger the Kill Command.")
    print("========================================\n")

    # KNOWLEDGE BASE: Hash Map (Dictionary) for O(1) Direct Access
    # PPT Requirement: Dictionary with 5+ intents (Expanded for unique personality)
    responses = {
        # --- Greetings & Farewells ---
        "hello": "Hi there! Welcome to the Logic Engine.",
        "hi": "Hello! System is online and ready.",
        "hey": "Greetings! How can I assist you today?",
        "good morning": "Good morning! Initializing daytime protocols.",
        "goodbye": "Shutting down... Goodbye!",
        "bye": "See you later. Terminating session.",

        # --- System & DecodeLabs Context ---
        "what is project 1": "Project 1 is the Rule-Based AI Chatbot, focusing on control flow and deterministic logic.",
        "what is decodelabs": "DecodeLabs is the platform powering this industrial training kit for AI engineering.",
        "are you an ai": "I am System 2: The Engineer. I am a deterministic logic engine, not a generative probabilistic model.",
        "what is a white box": "A white box is a system where the internal logic is transparent and traceability is 100%, just like me!",
        "who made you": "I was developed by Shahzaib, a software engineer with a strong focus on Python and Android development.",

        # --- Tech, CS & Personality Intents ---
        "what is dsa": "Data Structures and Algorithms are the core of efficient programming. For instance, I use Hash Maps for O(1) instant lookups instead of slow If-Elif ladders!",
        "what is python": "Python is a versatile programming language, great for backend, database management, and AI.",
        "what is android": "Android is a mobile operating system. My creator builds apps for it using modern architectures.",
        "how are you": "My runtime is optimal, memory usage is stable, and no bugs have been detected. I'm doing great!",
        "what is your name": "I am the Logic Engine, Project 1 of the DecodeLabs AI track.",
        
        # --- Polite fillers ---
        "thank you": "You're extremely welcome! System ready for the next query.",
        "thanks": "Anytime! Let me know if you need more information.",
        "ok": "Acknowledged.",
        "cool": "Indeed. Logic is very cool."
    }

    # THE HEARTBEAT: Continuous 'while' cycle
    while True:
        # PHASE 1: INPUT (Raw Feed)
        raw_input = input("You: ")
        
        # PHASE 2: NORMALIZATION & SANITIZATION
        # Handling case & whitespace as per IPO model blueprint
        clean_input = raw_input.lower().strip()
        
        # EXIT STRATEGY: Clean break command
        if clean_input == 'exit':
            print("Bot: KILL COMMAND received. Shutting down the logic engine... Goodbye!")
            break
            
        # PHASE 3: PROCESS & OUTPUT (Response Engine)
        # ATOMIC OPERATION: Lookup + Fallback
        # Instantly finds the key or returns the fallback default response for unknowns
        reply = responses.get(clean_input, "I do not understand. Please try a valid predefined command.")
        
        # Final Output Feedback Loop
        print(f"Bot: {reply}")

# Run the system loop
if __name__ == "__main__":
    run_chatbot()