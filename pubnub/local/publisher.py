# Based of the example @ https://www.pubnub.com/docs/quickstarts/python

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

CHANNEL = "backend-session"
PN_CONFIG = PNConfiguration()
PN_CONFIG.publish_key = "pub-c-3976abaa-8a0b-4b4b-8247-9904e9470a26"
PN_CONFIG.subscribe_key = "sub-c-0a592c68-ae3a-11eb-9538-227feadbaa58"


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
