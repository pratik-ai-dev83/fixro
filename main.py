from analyzer import analyze_code
from fixer import suggest_fix

def get_user_code():
  print("\nWecome to Fixro - Your AI Bug Fixer")
  print("Peste your code below ant type 'END' when you're done.\n")

  user_code = get_user_code()

  if not user_code.strip():
    print("No code provided. Please try again.")
    return
