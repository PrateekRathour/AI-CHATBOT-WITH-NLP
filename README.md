COMPANY: CODETECH IT SOLUTIONS

NAME: PRATEEK RATHOUR

INTERN ID: CT06DL752

DOMAIN: PYTHON DEVELOPEMENT

DURATION: 6 WEEKS

MENTOR: NEELA SANTOSH

DESCRIPTION-

1. Project Overview
The AI Chatbot project aims to develop a conversational agent using Natural Language Processing (NLP) with the spaCy library in Python. The chatbot is designed to handle basic user queries by recognizing intents (e.g., greetings, jokes, farewells) and providing relevant responses. The deliverable is a functional Python script that can be run in an IDE like VS Code.
2. Objectives for the Reporting Period
Develop the chatbot script with core NLP functionality using spaCy.
Set up the development environment in VS Code, including dependency installation.
Test the chatbot for basic functionality and resolve any implementation issues.
Document progress and challenges for stakeholder review.
3. Work Completed
Script Development:
oCreated the initial chatbot.py script, incorporating spaCy for NLP tasks.
oDefined intents (e.g., greeting, farewell, joke, weather) with corresponding patterns and responses.
oImplemented functions for text preprocessing, intent recognition (using spaCy similarity), and response generation.
Environment Setup:
oSet up VS Code with a Python virtual environment (venv).
oInstalled spaCy (pip install spacy) and attempted to download the en_core_web_sm model, but encountered issues due to incorrect terminal commands.
   
Dependency Resolution:
oSuccessfully downloaded the spaCy model en_core_web_sm using the command python -m spacy download en_core_web_sm after ensuring the virtual environment was activated in VS Code.
Code Refinement:
oRemoved unused imports (List, Tuple) from the script to clean up warnings in VS Code.
oFixed a syntax error in chatbot.py where an erroneous line (chat bot().pip install spacy) was removed and replaced with the correct chatbot() function call.
Testing and Debugging:
oRan the chatbot in VS Code and tested interactions:
Input: "Hi" → Output: "Hello! How can I help you today?"
Input: "Tell me a joke" → Output: "Why did the scarecrow become a programmer? Because he was outstanding in his field!"
Input: "Bye" → Output: "Bye! Have a great day!"
oConfirmed the chatbot handles basic intents correctly and exits cleanly with the "exit" command.
4. Challenges Encountered
Model Installation Issue: Initially failed to download the spaCy model due to an unactivated virtual environment and incorrect command placement in the script. Resolved by running the correct command in the terminal.
Syntax Error: Accidentally added a terminal command (pip install spacy) into the Python script, causing a SyntaxError. Fixed by removing the invalid line and ensuring proper function calls.
VS Code Warnings: Encountered linter warnings about unused imports, which were resolved by removing unnecessary imports.
5. Next Steps (June 15 - June 28, 2025)
Enhance the chatbot by adding more intents (e.g., handling questions about time or basic facts).
Improve intent recognition accuracy by fine-tuning the similarity threshold or exploring additional NLP techniques.
Conduct user testing to gather feedback on usability and response quality.
Prepare a final report and presentation for project stakeholders.
6. Summary
Over the past two weeks, the AI Chatbot project has progressed from initial development to a working prototype. The script is now functional, with basic NLP capabilities implemented using spaCy. Environment setup issues and syntax errors were resolved, and the chatbot successfully handles simple user queries. The next phase will focus on expanding functionality and improving accuracy.
