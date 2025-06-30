#leetcode
#Median of Two Sorted Arrays
nums1=[1,4]
nums2=[2,3]
arr=nums1+nums2
arr.sort()
if len(arr)%2==1:
    print(arr[len(arr)//2])
else :
    print((arr[(len(arr)//2)-1]+arr[len(arr)//2])/2)
