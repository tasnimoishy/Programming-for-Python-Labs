def search_by_category(resources, category):
    for r in resources:
        if r[2] == category:
            print(r)

search_by_category(resources, "Electronics")
