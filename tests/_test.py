from excuse_generator.excuses import generate_excuse, random_excuse, add_custom_excuse, list_categories, EXCUSES, help

def test_generate_excuse_valid_category():
    """Test that generate_excuse returns a valid excuse from a known category."""
    categories = ["bug", "deadline", "PR", "meeting", "deployment"]
    for category in categories:
        excuse = generate_excuse(category)
        assert isinstance(excuse, str)
        assert len(excuse) > 0

def test_generate_excuse_invalid_category():
    """Test that generate_excuse handles invalid categories gracefully."""
    excuse = generate_excuse("not_a_real_category")
    assert excuse == "Invalid category. Use list_categories() to see all available categories."

def test_generate_excuse_with_subcategory():
    """Test that generate_excuse returns a valid excuse from a nested category."""
    excuse = generate_excuse("meeting_resp", "technical")
    assert isinstance(excuse, str)
    assert len(excuse) > 0

def test_generate_excuse_invalid_subcategory():
    """Test that generate_excuse handles invalid subcategories properly."""
    excuse = generate_excuse("meeting_resp", "not_a_real_type")
    assert excuse.startswith("Invalid response type.")

def test_generate_excuse_case_insensitive():
    """Test that generate_excuse is case insensitive"""
    assert generate_excuse("BuG") in EXCUSES["bug"]

def test_random_excuse():
    """Test that random_excuse returns a valid excuse from any category."""
    excuse = random_excuse()
    assert isinstance(excuse, str)
    assert len(excuse) > 0

def test_add_custom_excuse():
    """Test adding a custom excuse to a category."""
    category = "bug"
    new_excuse = "Aliens must have changed the code overnight."
    add_custom_excuse(category, new_excuse)

    # Ensure the new excuse is in the category
    excuses = [generate_excuse(category) for _ in range(50)]
    assert new_excuse in excuses

def test_add_custom_excuse_to_subcategory():
    """Test adding a custom excuse to a subcategory."""
    category = "meeting_resp"
    subcategory = "technical"
    new_excuse = "My screen turned into The Matrix, I swear."
    add_custom_excuse(category, new_excuse, subcategory)

    # Ensure the new excuse is in the subcategory
    excuses = [generate_excuse(category, subcategory) for _ in range(10)]
    assert new_excuse in excuses

def test_list_categories():
    """Test that list_categories returns a non-empty list of available categories."""
    categories = list_categories()
    assert isinstance(categories, list)
    assert len(categories) > 0
    assert "bug" in categories
    assert "meeting_resp -> technical" in categories  # Ensure nested categories appear


def test_help(capsys):
    """Test that the help function"""

    help()
    captured = capsys.readouterr().out.strip()
    expected ="""
    EXCUSE GENERATOR FOR SOFTWARE ENGINEERS
    ---------------------------------------

    Commands:

    1. generate_excuse(category: str, resp_type: str = None) -> str
       - Generates a random excuse based on the specified category.
       - Categories: "bug", "deadline", "PR", "meeting", "deployment", "meeting_resp"
       - Some categories (like "meeting_resp") have subcategories.
       - Example: generate_excuse("bug")
       - Example: generate_excuse("meeting_resp", "technical")

    2. random_excuse() -> str
       - Returns a random excuse from any category.

    3. add_custom_excuse(category: str, excuse: str, resp_type: str = None)
       - Adds a new excuse to an existing category.
       - If the category has subcategories, specify resp_type.
       - Example: add_custom_excuse("meeting_resp", "Dog unplugged my router.", "technical")

    4. list_categories() -> list
       - Returns a list of available excuse categories and subcategories.

    5. help()
       - Displays this help message.

    """

    def normalize(text):

        lines = text.splitlines()

        cleaned_lines = []
        for line in lines:
            cleaned_line = line.strip()
            cleaned_lines.append(cleaned_line)

        normalized = "\n".join(cleaned_lines)
        final = normalized.strip()

        return final
    


    assert normalize(captured) == normalize(expected), f"Expected:{normalize(expected)}Got:{normalize(captured)}"

