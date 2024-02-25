from langchain_community.tools import tool

class CalculatorTools():
    @tool("Make a calculator")
    def calculate(operation):
        """ Useful to perform any mathematical operation, like 
        addition, subtraction, multiplication, division, etc.
        The input to this tool shoould be a mathmatical expression 
        a couple of examples are `2048*40` or `328/51-10`"""
        try:
            return eval(operation)
        except SystemError:
            return "Invalid operation in mathamtical expression"
    
    