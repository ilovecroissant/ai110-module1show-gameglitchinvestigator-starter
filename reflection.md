# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
1. New game button does not work, expected to start new game
2. Keep saying go lower although I reach minimum, expected to correctly give hint
3. The Show hint does it backward, expected to give a right hint

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). In the state of new game, AI suggested to add session state score to be back to 0 and the session state status to back to playing so the new game will start again.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). When I asked Claude to help fixing the New Game button, it changed the code in app.py which was not what I wanted. I asked to move the check_guess function to logic_utils.py instead and updated the import in app.py.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? I read through the updated code to see if it was logically correct.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code. I ran the test to check if the guess is too low by having the secret is 50 and the guess is 40.

- Did AI help you design or understand any tests? How? Yes of course. It helps me to write the tests and have the comment on how it works in plain English so I understand they do.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Always question the suggestions of AI and check if they are logically correct.
- What is one thing you would do differently next time you work with AI on a coding task? I am not sure yet, still learning from lecturer.
- In one or two sentences, describe how this project changed the way you think about AI generated code. I have a better understanding of how to prompt for AI to code and make it more reliable and less prone-error. Always question the suggested code from it and make sure to fully understand what you want from them so you are not overly dependent on it.
