# A personal introduction program using variables and f-string

# Personal details
first_name = "Josh"
last_name = "Johnson"
age = 36
city = "Surprise, AZ"                    #Current city added to the introduction
current_job = "Sales Professional"       #Current job added to the introduction
favorite_language = "Python"

# Display formatted introduction
print("=" * 40)
print("Personal Introduction")
print("=" * 40)
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Location: {city}")
print(f"Current Job: {current_job}")
print(f"Favorite Language: {favorite_language}")
print("=" * 40)
print(f"\\n {first_name} is {age} years old and lives in {city}.")
print(f"They are learning {favorite_language} to work for a Formula 1 team.")   # Dream job