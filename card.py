class Card():
    def __init__(self, name: str, message: str = "", probability: float = -1) -> None:
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

def formatedString(string: str):
    if len(string) > 25:
        mess: str = ""
        messList: list[str] = string.split()
        tempList: list[str] = [""]
        index = 0
        for i, x in enumerate(messList):
            if len(x) > 25:
                if len(x[:len(x)//2]) < 25:
                    messList[i:i+1] = (x[:len(x)//2] + "-", x[len(x)//2:])
                else:
                    messList[i:i+1] = (x[:24] + "-", x[24:])
        else:
            for x in messList:
                count: int = len(x) + len(tempList[index])
                if count > 25:
                    count = len(x)
                    index += 1
                    tempList.append(f" {x}")
                else:
                    tempList[index] += f" {x}"
        for line in tempList:
            mess += f"|{line[1:]:^25}|\n"
    else:
        mess = "|{m:^25}|\n".format(m=string)
    return mess

if __name__ == "__main__":
    c = Card("Dormir","Je test un string assez lqwoihdjawoidawjiodawoidhawoidhawoidiowdhoaiwhdawdwdwadwdhoaiwding ppour qu'il ne puisse pas rentrer")
    print(c)
    