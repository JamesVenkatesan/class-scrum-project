def create_post(user_id, text, image_path=None):
    return {"user_id": user_id, "text": text, "image": image_path}
