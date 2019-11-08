from termcolor import colored

__all__ = ['info', 'ask']

class tty_format:
    QUESTION = colored('[?]', 'yellow')
    INFO = colored('[~]', 'blue')
    WARNING = colored('[!]', 'magenta')
    ERROR = colored('[X]', 'red')


def info(text: str) -> None:
    print(f"{tty_format.INFO} {text}")

def ask(que: str, answers: tuple = ('y', 'n')) -> str:
    while True:
        print(f"{tty_format.QUESTION} {que} [{'/'.join(answers)}]")
        answer = str(input())
        if answer in answers:
            return answer