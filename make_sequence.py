arr = [1,2,3,4]
no = 2
length = len(arr)

for i in range(length):
    #print("iiiiiiii ",i)
    for j in range(1,(length-no+1)):
        #print("jjjjjjjjjj ",j)
        #length-no-j+2
        for k in range((length-1)-(i+j+no-3)):
            print(i+j," ",i+j+no-3)
            if (i+j) - (i+j+no-3) == 0:
                arr1 = arr[i+j]
            else:
                arr1 = arr[i+j:i+j+no-3]
      #      print("last value",no+j-2+k)
            if j != length-no+1:
                #no+j-2+k
                print(arr[i],"",arr1,"",arr[i+j+no-2+k])
