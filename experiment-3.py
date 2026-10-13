!pip install -q google-genai
-------------------------------------------
from google.colab import userdata
from google import genai
import time

api_key = userdata.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found.")

client = genai.Client(api_key=api_key)

print("✅ Gemini API connected successfully!")
-------------------------------------------------------
def ask_llm(prompt):
    for attempt in range(5):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt,
                config={
                    "temperature": 0.5
                }
            )
            return response.text

        except Exception as e:
            if "503" in str(e) and attempt < 4:
                wait = 10 * (attempt + 1)
                print(f"Server busy. Retrying in {wait} seconds...")
                time.sleep(wait)
            else:
                return f"❌ API Error: {e}"
  -------------------------------------------------------------------
# Iteration 0: Baseline
prompt0 = "Explain photosynthesis to a 10-year-old."

# Iteration 1: Add analogy and length constraint
prompt1 = (
    "You are a friendly science teacher. "
    "Explain photosynthesis to a 10-year-old using a simple analogy. "
    "Use 3 short sentences and avoid technical jargon."
)

# Iteration 2: Add mnemonic and diagram description
prompt2 = (
    "You are a friendly science teacher. Explain photosynthesis "
    "to a 10-year-old using a simple analogy. Use 3 short sentences "
    "and avoid technical jargon. Add a memory trick and a simple "
    "text-only diagram description."
)

prompts = [prompt0, prompt1, prompt2]

print("✅ Three prompt versions defined successfully!")
--------------------------------------------------------------------------
print("=== ITERATION 0 (BASELINE) ===")
print("\nPrompt:")
print(prompt0)

response0 = ask_llm(prompt0)

print("\nResponse:")
print(response0)

print("\nAnalysis:")
print("The baseline prompt gives a general explanation.")
print("It does not specify a length, analogy, or memory aid.")
-------------------------------------------------------------------------------
print("=== ITERATION 1 (FIRST REFINEMENT) ===")
print("\nPrompt:")
print(prompt1)

response1 = ask_llm(prompt1)

print("\nResponse:")
print(response1)

print("\nAnalysis:")
print("The role, analogy, and sentence limit aim to make")
print("the explanation simpler and easier for a child to understand.")
-------------------------------------------------------------------------------
print("=== ITERATION 2 (SECOND REFINEMENT) ===")
print("\nPrompt:")
print(prompt2)

response2 = ask_llm(prompt2)

print("\nResponse:")
print(response2)

print("\nAnalysis:")
print("The memory trick and diagram description aim to improve")
print("recall and help the child visualize photosynthesis.")
------------------------------------------------------------------------
print("\n========== FINAL SUMMARY ==========")

print("\nIteration 0:")
print("Basic explanation of photosynthesis.")

print("\nIteration 1:")
print("Adds a teacher role, analogy, and short explanation.")

print("\nIteration 2:")
print("Adds a memory trick and text-only diagram description.")

print("\nResponse word counts:")
print("Iteration 0:", len(response0.split()), "words")
print("Iteration 1:", len(response1.split()), "words")
print("Iteration 2:", len(response2.split()), "words")

print("\n✅ Prompt refinement experiment completed.")
