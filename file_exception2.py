import os
def create_file(filename):
    try:
        with open('filename','w') as f:
            f.write("hello accelyzie \n")
        print("file" + filename + "created with data successfully" )

    except IOError:  
          # if we want to specify error
          print("error : file was not created" +filename)

def read_file(filename):
     try:
          with open(filename,'r') as f:
               content = f.read()
               print(content)
     except IOError:
          print("successfully file content readed" +filename)

def append_data(filename,text):
     try:
          with open(filename,'a') as f:
               f.write(text)
          print("text appended to the file" +filename)

     except IOError:
          print("could not  appended to the file" +filename)

def rename_file(filename,newfile):
     try:
          os.rename(filename,new_file)
          print("file:" + filename + "renamed to"  +new_file)

     except IOError:
          print("could not rename the file" +filename)

def delete_file(new_file):
     try:
          os.remove(new_file)
          print("file" +filename + "deleed successfully")

     except IOError:
          print("error : can not delelted" +new_file)






    

    
filename = "ex.txt"
new_file = "changed_ex.txt"
text = "i am add some data"

create_file(filename)
read_file(filename)

append_data(filename,text)
read_file(filename)
rename_file(filename,new_file)
delete_file(new_file)
