def arithmetic_arranger(problems, solve=False):
    
  if len(problems) > 5:
    return "Error: Too many problems."
    
  arranged_problems = ""
  answers = []
  maxLength = []
    
  for i in range(len(problems)):
    prob = problems[i].split()
        
    num1 = prob[0]
    num2 = prob[2]
        
    if (not num1.isdigit() or not num2.isdigit()):
      return "Error: Numbers must only contain digits."
    if (len(num1) >= 5 or len(num2) >= 5):
        return "Error: Numbers cannot be more than four digits."
        
    maxLength.append(max(len(num1), len(num2)))
        

    arranged_problems += "  " 
    arranged_problems += (" " * (maxLength[i] - len(num1))) + num1
    
    if(i != len(problems) - 1):
      arranged_problems += "    "
        
  arranged_problems += "\n"
    
  for i in range(len(problems)):
    prob = problems[i].split()
        
    num1 = prob[0]
    opp = prob[1]
    num2 = prob[2]
        
    if(opp != '+' and opp != '-'):
      return "Error: Operator must be '+' or '-'."
        
    if(opp == '+'):
      answers.append(str(int(num1) + int(num2)))
    else:
      answers.append(str(int(num1) - int(num2)))
                    
        
    arranged_problems += opp
        
    arranged_problems += " "  
    arranged_problems += (" " * (maxLength[i] - len(num2))) + num2
        
    if(i != len(problems) - 1):
      arranged_problems += "    "
            
  arranged_problems += "\n"
    
  for i in range(len(problems)):
    prob = problems[i].split()
    num1 = prob[0]
    num2 = prob[2]

    arranged_problems += ("-"*(maxLength[i] + 2))
                              
    if(i != len(problems) - 1):
      arranged_problems += "    "
        
  if(solve):
    prob = problems[i].split()
    arranged_problems += "\n"
    for i in range(len(answers)):
      arranged_problems += (" " * ((maxLength[i] + 2) - len(answers[i]))) 
      arranged_problems += answers[i]
      if(i != len(answers) - 1):
        arranged_problems += "    "
        
    
  return arranged_problems
