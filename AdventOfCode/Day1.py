def check2020(num1, num2, num3):
    if num1 + num2 + num3 == 2020:
        return True
    else:
        return False


with open('Expense_Report.txt', 'r') as report:
    data = report.readlines()

    for i in data:
        for j in data:
            for k in data:
                if check2020(int(i), int(j), int(k)):
                    print(f"{i}{j}{k}{int(i)*int(j)*int(k)}")

