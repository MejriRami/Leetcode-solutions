class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        positions=[]
        for i in range(len(words)) :
            if x in  words[i]:
                positions.append(i)
        return(positions)