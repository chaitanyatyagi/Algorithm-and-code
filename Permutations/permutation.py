def permute(nums):
        res = []
        hmap = {}
        for i in range(len(nums)):
            hmap[i] = False
        def recursor(n,res,curr,arr,hmap):
    
            if len(curr) == n:
                x = []
                for j in curr:
                    x.append(j)
                res.append(x)
                return
            
            for i in range(n):
                if hmap[i] == False:
                    hmap[i] = True
                    curr.append(arr[i])
                    recursor(n,res,curr,arr,hmap)
                    curr.remove(arr[i])
                    hmap[i] = False
        recursor(len(nums),res,[],nums,hmap)
        return res