def search_users(query, users):
    return [u for u in users if query.lower() in u["username"].lower()]
