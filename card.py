from util import formatedString

class Card():
    def __init__(self, name: str, message: str = "", probability: float = 1) -> None:
        self.name: str = name
        self.hash: int = hash(name)
        self.message: str = message
        self.proba: float = probability
    
    def __repr__(self) -> str:
        return {"Name":self.name, "Hash":self.hash, "Message":self.message}

    def __str__(self) -> str:
        namm = formatedString(f"{self.name} ({self.proba:.2f}%)")
        mess = formatedString(self.message)
        temp: str = "{div}{name:^25}{div}{message}{div}".format(name=namm, div="+" + "-"*25 + "+\n", message=mess)
        return temp


if __name__ == "__main__":
    c = Card("Dormir","Je test un string assez lqwoihdjawoidawjiodawoidhawoidhawoidiowdhoaiwhdawdwdwadwdhoaiwding ppour qu'il ne puisse pas rentrer")
    print(c)
    