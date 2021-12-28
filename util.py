def formatedString(string: str, endString: str = "|"):
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
            mess += f"|{line[1:]:^25}{endString}\n"
    else:
        mess = "|{m:^25}{end}\n".format(m=string, end=endString)
    return mess

if __name__ == "__main__":
    print(formatedString("This is a title"))
    print(formatedString("This is a title")[:-1])
    