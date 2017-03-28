# WordLadder class contains everything you need to run the word ladder 
import copy
class WordLadder:

    def findLadders(self, start, end):
       
        
        file = open('dictionary.txt', 'r') 
        mylist = file.readlines()
        
      
            
        
        result, cur, visited, gotcha, trace = [], [start], set([start]), False, {word: [] for word in mylist}  

        while cur and not gotcha:
            for word in cur:
                visited.add(word)
                
            next = set()
            for word in cur:
                for i in xrange(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        testWord = word[:i] + j + word[i + 1:]
                        if testWord not in visited and testWord in mylist:
                            if testWord == end:
                                gotcha = True
                            next.add(testWord)
                            trace[testWord].append(word)
            cur = next
            
        if gotcha:
            self.backtrack(result, trace, [], end)
        
        return result
    
    def backtrack(self, result, trace, path, word):
        if not trace[word]:
            result.append([word] + path)
        else:
            for prev in trace[word]:
                self.backtrack(result, trace, [word] + path, prev)
    
if __name__ == "__main__":
    print WordLadder().findLadders("hit", "cog")