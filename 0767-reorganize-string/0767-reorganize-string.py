class Solution:
    def reorganizeString(self, s: str) -> str:
        mpp={}
        for i in s:
            mpp[i] = mpp.get(i,0)+1

        heap=[]
        for char,freq in mpp.items():
            heapq.heappush(heap,(-freq,char))
        
        print(heap)
        prev=None
        res=[]

        while heap:
            freq,char=heapq.heappop(heap)
            res.append(char)
            print(res)
            if prev:
                heapq.heappush(heap,prev)
                prev=None
            if freq<-1:
                prev=(freq+1,char)
        return ''.join(res) if not prev else ""
        
        

        
