fileref = open("olympics.txt", "r") # to make full dir use open (../x location/y location / ... / .txt ,  )
contents = fileref.read() 
print (contents [ :100]) # read and print the first 100 
contents_2 = fileref.readline() 
print(contents_2 [ :4]) #print first 4 lines and they ending ith /n , using for loo pwill elemnte this and make each line in a new line 
fileref.close()
#********************************
file_obj = open (r"C:\Users\mahdi\OneDrive\Desktop\python course 2\Python-Course-2\square.txt" , "w" ) 
for number in range (13) : 
    sqaure =number * number 
    file_obj.write(str(sqaure) + '\n')
file_obj.close 
new_file_obj = open ("square.txt ", "r")
print(new_file_obj.read()[ :9])
#********************************
frame = "square.txt"
with open (frame ,'w') as md : 
      #md.read()
       #.
       #.
   for num in range(10): 
       md.write(str(num))
       md.write('\n')
#********************************
