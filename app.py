def send_message(sender_id, recipient_id, text):
    return {"from": sender_id, "to": recipient_id, "text": text}
