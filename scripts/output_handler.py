def display_result(result, title):
    print(f"\n{title}:")
    if isinstance(result, list) and not result:
        print("Not found.")
    else:
        print(result)