"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #12 - Braces Brackets & Bows Balance (balancechecking.py)


Author: Ali Qattan

Difficulty Level: 6/10

Prompt: In your IDEs, your code editors and sometimes Vim (for those 
unfortunate ones who use vim) your application will yell at you when you don’t
have matching closing brackets. Python does not have that problem as much as
other languages like Java and C which rely heavily on curly braces.  You need 
to write a program that allows for that functionality so that every ‘[‘ and ‘{‘ 
and ‘(‘ has a matching ‘]’  ‘}’  ‘)’. 
This problem can be solved quickly using the right data structure.

Test Cases:
Input: {[()]}  Output: True

Input: [()]  Output: True

Input:{[{}]  Output: False

"""
class Solution:
    def isBalanced(self, parenthesis): 
            #type parenthesis: string
            #return type: boolean
            # stack = []
            # open = ['(', '[', '{']
            # close = [')',']','}']
            # matching = dict(zip(close, open))
            # for c in parenthesis:
            #     if c in open:
            #         stack.append(c)
            #     elif c in close:
            #         if len(stack ) == 0:

            c1 = 0
            c2 = 0
            c3 = 0
            cc1 = 0
            cc2 = 0
            cc3 = 0
            for i in parenthesis:
                if i == '[':
                    c1 += 1
                elif i == '(':
                    c2 +=1
                elif i == '{': 
                    c3 +=1
                elif i == '}':
                    cc1 += 1
                elif i == ')':
                    cc2 +=1
                elif i == '}': 
                    cc3+=1
            print(c1, cc1,c2,cc2,c3,cc3)
            if c1 == cc1 and c2 == cc2 and c3 == cc3:
                return True
            else:
                return False
    #isBalanced("{[()]}")
                     
            
            #TODO: Write code below to returnn a boolean value with the solution to the prompt.
            

def main():
    str1=input()
    tc1= Solution()
    ans=tc1.isBalanced(str1)
    print(ans)

if __name__ == "__main__":
    main()
