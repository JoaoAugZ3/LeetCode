# Concluído
# Runtime: 36ms
# Memory: 16.3MB

class Solution:
    def interpret(self, command: str) -> str:
        while '()' in command or '(al)' in command:
            command = command.replace('()', 'o')  
            command = command.replace('(al)', 'al')     
        return command