import excuse_generator

print("Available categories and subcategories:")
categories = excuse_generator.list_categories()
print(categories)

print("\nGenerating a random excuse from 'bug' category:")
print(excuse_generator.generate_excuse("bug"))

print("\nGenerating a random excuse from 'meeting_resp' -> 'technical' subcategory:")
print(excuse_generator.generate_excuse("meeting_resp", "technical"))

print("\nAdding a custom excuse to 'meeting_resp' -> 'technical':")
excuse_generator.add_custom_excuse("meeting_resp", "My screen turned into The Matrix, I swear.", "technical")

print("\nGenerating excuse from 'meeting_resp' -> 'technical' after adding custom excuse:")
print(excuse_generator.generate_excuse("meeting_resp", "technical"))

print("\nGenerating a random excuse from any category:")
print(excuse_generator.random_excuse())

print("\nHelp Function:")
excuse_generator.help()  
