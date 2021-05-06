import os

from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub


CHANNEL = "backend-session"
PN_CONFIG = PNConfiguration()
PN_CONFIG.subscribe_key = "sub-c-0a592c68-ae3a-11eb-9538-227feadbaa58"


class MySubscribeCallback(SubscribeCallback):
    def status(self, _, event):
        if event.category == PNStatusCategory.PNConnectedCategory:
            print(f"Connected to channel '{CHANNEL}'")

    def message(self, _, event):
        print(
            f"[{event.timetoken}] ({event.message['sender']}): {event.message['text']}"
        )


def main():
    print("***************************************************")
    print(f"* Listening to channel {CHANNEL}")
    print("***************************************************")
    pubnub = PubNub(PN_CONFIG)
    pubnub.add_listener(MySubscribeCallback())
    pubnub.subscribe().channels(CHANNEL).with_presence().execute()


if __name__ == "__main__":
    main()
