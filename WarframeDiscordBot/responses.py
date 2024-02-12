import discBot
import threading
def get_response(user_input: str)-> str:
    lowered: str=user_input.lower()

    match lowered :
        case '*':
            return "Wrong command"

        case '*arbitration':
            return discBot.printArb()

        case '*eidolons':
            return discBot.printCetusStatus()


def send_arbitration():
        raise NotImplementedError