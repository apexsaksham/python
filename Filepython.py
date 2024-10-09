# f = open("demo.txt", "r")
# f = open("demo.txt", "a")
# # data = f.read(5) #read particular lines
      
# data = f.read() 
# print(data)

# f.close()




# to write 

# f = open("demo.txt", "r+")
# f.write("\nhappy happy")      
# print(f.read())
# f.close()



# with syntax

# with open("samp.txt", "w") as f:
#     f.write("this is sample text")


# with open("samp.txt", "r") as f:
#     print(f.read())    


# deleting a file

import os

os.remove("samp.txt")
