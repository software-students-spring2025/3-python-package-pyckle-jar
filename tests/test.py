from excuse_generator.excuses import generate_excuse, EXCUSES

def test_category():
    categories = []
    for category in EXCUSES.keys():
        categories.append(category)
    category = categories[0]
    ex = generate_excuse(category)
    assert ex in EXCUSES[category], f"Not a valid excuse: {ex}"


