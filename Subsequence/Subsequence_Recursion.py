def subsequence(indx,arr,given):
        if indx>=len(given):
            print(arr)
            return
        arr.append(given[indx])
        subsequence(indx+1,arr,given)
        arr.remove(given[indx])
        subsequence(indx+1,arr,given)

def main_function():
    arr = []
    given = [3,1,2]
    subsequence(0,arr,given)

main_function()
