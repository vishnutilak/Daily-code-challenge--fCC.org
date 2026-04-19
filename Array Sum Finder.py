def find_sum(arr, target):
    n= len(arr)

    def dfs(start, path, total):
        if total==target and len(path)>=2:
            return path
        if total >target and all(x>=0 for x in arr):
            return None
        for i in range(start, n):
            res = dfs(i+1, path+ [arr[i]], total+arr[i])
            if res:
                return res
        return None

    result =dfs(0, [],0)

    return result if result else "Sum not found"
