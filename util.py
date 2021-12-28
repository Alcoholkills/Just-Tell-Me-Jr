def formatedString(string: str, space: int = 25, endString: str = "|") -> str:
    if len(string) > space:
        mess: str = ""
        messList: list[str] = string.split()
        tempList: list[str] = [""]
        index = 0
        for i, x in enumerate(messList):
            if len(x) > space:
                if len(x[: len(x) // 2]) < space:
                    messList[i : i + 1] = (x[: len(x) // 2] + "-", x[len(x) // 2 :])
                else:
                    messList[i : i + 1] = (x[: space - 1] + "-", x[space - 1 :])
        else:
            for x in messList:
                count: int = len(x) + len(tempList[index])
                if count > space:
                    count = len(x)
                    index += 1
                    tempList.append(f" {x}")
                else:
                    tempList[index] += f" {x}"
        for line in tempList:
            mess += f"|{line[1:]:^{space}}{endString}\n"
    else:
        mess = "|{m:^{num}}{end}\n".format(m=string, end=endString, num=space)
    return mess

def boxString(string: str, space: int = 25) -> str:
    box = "+" + "-"*space + "+\n"
    return box + formatedString(string, space) + box

def tableString(array: list, firstColName: str = "Index", secColName: str = "Name", firstSpace = 7, secondSpace = 25) -> str:
    div = f"+{'-'*firstSpace}+{'-'*secondSpace}+\n"
    table = div
    table += formatedString(firstColName, firstSpace)[:-2] + formatedString(secColName, secondSpace)
    table += div
    for index, item in enumerate(array):
        table += formatedString(str(index), firstSpace)[:-2] + formatedString(item, secondSpace)
    return table + div

if __name__ == "__main__":
    print(formatedString("This is a title"))
    print(formatedString("This is a title")[:-1])
