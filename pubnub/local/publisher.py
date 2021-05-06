# Based of the example @ https://www.pubnub.com/docs/quickstarts/python

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

CHANNEL = "backend-session"
PN_CONFIG = PNConfiguration()
PN_CONFIG.publish_key = "YOUR_PUBLISH_KEY"
PN_CONFIG.subscribe_key = "YOUR_SUBSCRIPTION_KEY"


def main():
    print("********************************************")
    print("* Publish messages for HUJI Hackathon 2021 *")
    print("********************************************")

    your_name = input("What is your name?: ")

    pubnub = PubNub(PN_CONFIG)
    while True:
        text = input("What do you want to say?: ")
        if not text:
            print("I didn't hear you...")
            continue

        the_message = {"sender": your_name, "text": text}
        envelope = pubnub.publish().channel(CHANNEL).message(the_message).sync()

        if envelope.status.is_error():
            print("[PUBLISH: fail]")
            print(f"error: {envelope.status.error}")
        else:
            print("[PUBLISH: sent]")
            print(f"timetoken: {envelope.result.timetoken}")


if __name__ == "__main__":
    main()
