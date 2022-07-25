
def ArthmeticFunction(AnDispl, Functions):
    inputs=""
    arithmProblems = []
    for Fnctn in Functions:
        inputs=inputs+str(Fnctn)+","



    # cleaning the input data by removing all whitespaces and
    inputs = inputs.strip()  # leading and trailing whitespaces
    inputs = inputs.replace(" ", "")  # remaining whitespaces

    # inputting each equation as a string in a list
    arithmProblems = inputs.split(',')

    operands = []
    operations = []

    if len(arithmProblems) > 5:
        print("Error: Too many problems")
        quit()
    for item in arithmProblems:
        if '*' in item or '/' in item or '%' in item:
            print("Error: Operator must be '+' or '-'.")
            quit()
        # Splitting operands from operations and inserting them into list
        if item.find('+') > 0:
            a = item.find('+')
            operands.append(item[:a])
            operands.append(item[a + 1:])
            operations.append('+')

        if item.find('-') > 0:
            a = item.find('-')
            operands.append(item[:a])
            operands.append(item[a + 1:])
            operations.append('-')

    # Checking if operands are more then 4 digits
    for oprnd in operands:
        if len(oprnd) > 4:
            print('Error: Numbers cannot be more than four digits.')
            quit()

    Top = []
    bot = []
    Answr = []

    for w in range(0, len(operands), 2):
        Top.append(operands[w])
        bot.append(operands[w + 1])

    # calculating the results
    for y in range(0, len(Top)):
        if operations[y] == "+":
            result = int(Top[y]) + int(bot[y])
            Answr.append(str(result))
        else:
            result = int(Top[y]) - int(bot[y])
            Answr.append(str(result))

    # Displaying the output
    TopLine = ""
    BottomLine = ""
    DashLine = ""
    AnswerLine = ""

    for a in range(0, len(Top)):
        if len(Top[a]) == len(bot[a]):
            TopAdd = " " + Top[a] + "    "
            BotAdd = operations[a] + bot[a] + "    "
            dash = "-"
            DashAdd = (dash * len(operations[a])) + (dash * len(bot[a])) + "    "

            if len(Answr[a]) == len(Top[a]):
                AnswerLine = AnswerLine + Answr[a] + "    "
            elif len(Answr[a]) > len(Top[a]):
                AnswerLine = " " + AnswerLine + Answr[a] + "    "
            else:
                AnswerLine = AnswerLine + " " + Answr[a] + "    "

            TopLine = TopLine + TopAdd
            BottomLine = BottomLine + BotAdd
            DashLine = DashLine + DashAdd
        elif len(Top[a]) > len(bot[a]):
            TopAdd1 = " " + Top[a] + "    "
            whitespace = " "
            BotAdd1 = operations[a] + whitespace * (len(Top[a]) - len(bot[a])) + bot[a] + "    "
            dash = "-"
            DashAdd1 = (dash * len(operations[a])) + (dash * len(whitespace * (len(Top[a]) - len(bot[a])))) + (
                        dash * len(bot[a])) + "    "

            if len(Answr[a]) == len(Top[a]):
                AnswerLine = AnswerLine + Answr[a] + "    "
            elif len(Answr[a]) > len(Top[a]):
                AnswerLine = " " + AnswerLine + Answr[a] + "    "
            else:
                AnswerLine = AnswerLine + " " + Answr[a] + "    "

            TopLine = TopLine + TopAdd1
            BottomLine = BottomLine + BotAdd1
            DashLine = DashLine + DashAdd1
        else:
            whitespace = " "
            TopAdd2 = " " + whitespace * (len(bot[a]) - len(Top[a])) + " " + Top[a] + "    "
            BotAdd2 = operations[a] + " " + bot[a] + "    "
            dash = "-"
            DashAdd2 = (dash * len(operations[a])) + "-" + (dash * len(bot[a])) + "    "

            if len(Answr[a]) == len(Top[a]):
                AnswerLine = AnswerLine + Answr[a] + "    "
            elif len(Answr[a]) > len(Top[a]):
                AnswerLine = " " + AnswerLine + Answr[a] + "    "
            else:
                AnswerLine = AnswerLine + " " + Answr[a] + "    "

            TopLine = TopLine + TopAdd2
            BottomLine = BottomLine + BotAdd2
            DashLine = DashLine + DashAdd2

    cnt = 0
    Ts = True
    wh = ""
    for dh in DashLine:
        if dh.isspace():
            wh = wh + dh
            Ts = True
        else:
            if Ts == True:
                wh = wh + ","
            Ts = False

    wh = str(wh)
    whts = wh.split(",")

    Dsp_answer = AnswerLine.split()
    LinesA = ""

    dashL = DashLine.split()

    for x in range(0, len(Dsp_answer)):
        if x == 0:
            LinesA = LinesA+whts[x] + Dsp_answer[x]
        elif len(Dsp_answer[x]) == 1 and len(dashL[x])>len(Dsp_answer[x]):
            LinesA = LinesA + "" + whts[x] + Dsp_answer[x]
        elif len(Dsp_answer[x - 1]) >= len(dashL[x - 1]):
            LinesA = LinesA  +whts[x] + Dsp_answer[x]
        elif len(Dsp_answer[x - 1]) < len(dashL[x - 1]):
            Nm = len(dashL[x - 1]) - len(Dsp_answer[x - 1])
            NmWhtsp = " " * Nm
            LinesA = LinesA  +whts[x] + NmWhtsp + Dsp_answer[x]

    # print(TopLine)
    # print(BottomLine)
    # print(DashLine)

    if AnDispl==False:
        LinesA=""

    return TopLine+"\n"+BottomLine+"\n"+DashLine+"\n"+LinesA


print(ArthmeticFunction(True, ["1 + 2", "3801 - 2", "45 + 43", "123 + 49"]))
