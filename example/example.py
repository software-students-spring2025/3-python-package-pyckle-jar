from excuse_generator.excuses import generate_excuse, random_excuse, add_custom_excuse, list_categories

print("Available Categories:", list_categories())

print("Random bug excuse:", generate_excuse("bug"))
print("Random PR excuse:", generate_excuse("PR"))
print("Random deadline excuse:", generate_excuse("deadline"))
print("Random meeting excuse:", generate_excuse("meeting"))
print("Random deployment excuse:", generate_excuse("deployment"))

print("Random excuse", random_excuse())

