def arithmetic_arranger(problems, *answers):
    
    if len(problems) > 5:
        return("Error: Too many problems.")
    else:
        line1 = ""
        line2 = ""
        line3 = ""
        line4 = ""
        for problem in problems:
            problem = problem.split()
            operand1 = problem[0].strip()
            operand2 = problem[2].strip()
            operator = problem[1].strip()

            if operand1.isdigit() and operand2.isdigit():
                if len(operand1) < 5 and len(operand2) < 5:
                    if operator == '+':
                        ans = str(int(operand1) + int(operand2))
                    elif operator == '-':
                        ans = str(int(operand1) - int(operand2))
                    elif operator == '/' or operator == '*':
                        return("Error: Operator must be '+' or '-'.")
                        break
                else:
                    return("Error: Numbers cannot be more than four digits.")
                    break
            else:
                return("Error: Numbers must only contain digits.")
                break

            spaces = max(len(operand1),len(operand2))+2
            line1 += operand1.rjust(spaces)
            line2 += operator + (operand2.rjust(spaces-1))
            line3 += "-"*spaces
            line4 += ans.rjust(spaces)

            if problem != problems[len(problems)-1]:
                line1 += "    "
                line2 += "    "
                line3 += "    "
                line4 += "    "

        if answers:
            arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip() + "\n" + line4.rstrip()
        else:
            arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()
    return(arranged_problems)
