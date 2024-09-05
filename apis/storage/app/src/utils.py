import json
from storage.app.src.route import person_save, account_save, card_save

def process_message(ch, method, properties, body):
    try:
        message = json.loads(body)
        event = method.routing_key.split('.')[1]

        if event == "person":
            response = person_save(message)
        elif event == "account":
            response = account_save(message)
        elif event == "card":
            response = card_save(message)
        else:
            raise ValueError(f"Unknown event type: {event}")

        if response.status_code != 200:
            raise Exception(f"Failed to save data: {response.text}")

        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Failed to process message: {e}")

