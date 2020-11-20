def arithmetic_arranger(problems,show_answers=False):
  if len(problems)>5:
    return "Error: Too many problems."
  else:
    for problem in problems: 
      if not problem.split(" ")[0].isnumeric() or not problem.split(" ")[-1].isnumeric():
        return "Error: Numbers must only contain digits."
      elif problem.split(" ")[1] not in ("+","-"):
        return "Error: Operator must be '+' or '-'."
      elif len(problem.split(" ")[0])>4 or len(problem.split(" ")[-1])>4:
        return "Error: Numbers cannot be more than four digits."
      else:
        pass
    
    result=""
    
    first_operands=[i.split(" ")[0] for i in problems]
    operators=[i.split(" ")[1] for i in problems]
    second_operands=[i.split(" ")[-1] for i in problems]

    longest_operands=[]

    for i in problems:
        if len(i.split(" ")[0])>len(i.split(" ")[-1]):
            longest_operands.append(i.split(" ")[0])
        else:
            longest_operands.append(i.split(" ")[-1])
    
    if show_answers is False:
        
        for i in range(len(first_operands)):
            if i<len(first_operands)-1:
                result+=first_operands[i].rjust(len(longest_operands[i])+2)+" "*4
            else:
                result+=first_operands[i].rjust(len(longest_operands[i])+2)
    
        result+="\n"
    
        for i in range(len(first_operands)):
            if i<len(first_operands)-1:
                result+=operators[i]+" "+(second_operands[i]).rjust(len(longest_operands[i]))+" "*4
            else:
                result+=operators[i]+" "+(second_operands[i]).rjust(len(longest_operands[i]))

    
        result+="\n"
    
        for i in range(len(first_operands)):
            if i<len(first_operands)-1:
                result+="-"*(len(longest_operands[i])+2)+" "*4
            else:
                result+="-"*(len(longest_operands[i])+2) 

        return result
    
    else:    
        
        for i in range(len(first_operands)):
            if i<len(first_operands)-1:
                result+=first_operands[i].rjust(len(longest_operands[i])+2)+" "*4
            else:
                result+=first_operands[i].rjust(len(longest_operands[i])+2)
    
        result+="\n"
    
        for i in range(len(first_operands)):
            if i<len(first_operands)-1:
                result+=operators[i]+" "+(second_operands[i]).rjust(len(longest_operands[i]))+" "*4
            else:
                result+=operators[i]+" "+(second_operands[i]).rjust(len(longest_operands[i]))

    
        result+="\n"
    
        for i in range(len(first_operands)):
            if i<len(first_operands)-1:
                result+="-"*(len(longest_operands[i])+2)+" "*4
            else:
                result+="-"*(len(longest_operands[i])+2)
        
        result+="\n"
        
        answers=[str(eval(i)) for i in problems]
        
        for i in range(len(first_operands)):
            if i<len(first_operands)-1:
                result+=answers[i].rjust(len(longest_operands[i])+2)+" "*4
            else:
                result+=answers[i].rjust(len(longest_operands[i])+2)   
        
        return result
        
    
