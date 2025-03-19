from excuse_generator.excuses import generate_excuse, EXCUSES, list_categories

def test_category():
    categories = []
    for category in EXCUSES.keys():
        categories.append(category)
    category = categories[0]
    ex = generate_excuse(category)
    assert ex in EXCUSES[category], f"Not a valid excuse: {ex}"

'''
def test_list_categories():
    categories = list_categories()
    assert set(categories.keys() == set(EXCUSES.keys())), f"Major Category Mismatch"
    for category, subcategories in categories.items():
        if isinstance(EX)''
'''

