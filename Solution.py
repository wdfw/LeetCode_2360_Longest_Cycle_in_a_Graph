class Solution:
    def longestCycle(self, edges) :
        
        self.travel_step = [0]*len(edges) 
        self.passed = [0]*len(edges) 
        self.ans = -1
        self.edges = edges
        self.size = len(edges) 

        def DFS(node,stamp) :            
            step = 1 
            
            while node != -1 :
                
                if self.passed[node] == stamp : 
                    self.ans = max(self.ans,step - self.travel_step[node])
                    return
                elif self.travel_step[node] : 
                    return

                self.travel_step[node] += step
                self.passed[node] = stamp
                
                node = self.edges[node]
                step += 1
                
        
        for i in range(self.size) :
            if not self.travel_step[i] :  DFS(i,i+1)
                
        return self.ans 
