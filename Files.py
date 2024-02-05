fileref = open("olympics.txt", "r")
contents = fileref.read() 
print (contents [ :100]) # read and print the first 100 
contents_2 = fileref.readline() 
print(contents_2 [ :4]) #print first 4 lines and they ending ith /n , using for loo pwill elemnte this and make each line in a new line 
fileref.close()
