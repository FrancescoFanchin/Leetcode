class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dicnum={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        
        if len(digits)==0:
            return []
        elif len(digits)==1:
            return dicnum[digits]
        else:
            word_list=[]
            word_list.extend(dicnum[digits[0]])
            for i in range(1,len(digits)):
                max_j=len(word_list)
                j=0
                while j < max_j:
                    root=word_list[0]
                    word_list.pop(0)
                    for k in range(len(dicnum[digits[i]])):
                        word_list.append(root+dicnum[digits[i]][k])
                    j=j+1
                    
            return word_list
        
        
