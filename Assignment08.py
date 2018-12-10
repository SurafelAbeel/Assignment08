#-------------------------------------------------#
# Title: Python use of Class
# Dev:   Surafel Abeel
# Date:  Dec 9, 2018
# ChangeLog: (Surafel, 12/9/2018, Commented)
# Surafel.A, 12/9/2018, Created Script
#-------------------------------------------------#

#-- Data --#
# Create a text file called "Products.txt" that will be used throughout code
# Create a Class called "Product"
# Create functions under the Class which become Methods


#-- Input/Output --#
# User inputs ID
# User inputs Name
# User inputs Price
# User chooses weather to exit or continue
# User chooses weather to save the data or not
# User chooses weather to see the data saved or not


#-- Processing --#
# Step 1
# Get user inputs (Id, Name, Price)

# Step 2
# if user chooses to exit, end code; else, continue

# Step 3
# if user chooses to save input, save to "Product.txt" file. Else, move on to next line.

# Step 4
# If user chooses to display saved data, print out saved file. If not, exit code.

# Step 5
# Lastly, use exception handling for errors.

# step 6
# Exit program
#-------------------------------

#Create a file called "Products"
objFile = open("C:\\PythonClass\\Assignment08\\Products.txt", "a")

#--- Make the class ---
class Product(object): #class to hold data about products
    #--Fields-- Not needed

    #--Constructor-- Used as a command to run automatically when object is created
    def __init__(self,Id = "", Name = "", Price = ""): #creates empty object
        #Attribute
        self.__Id = Id
        self.__Name = Name
        self.__Price = Price
    #Properties: Id
    #Gives access to private attributes using public property procedures
    @property #getter or accessor
    def Id (self):
        return self.__Id

    @Id.setter # (setter or mutator)
    def Id (self, Value):
        self.__Id = Value

    # Properties: Name
    #Gives access to private attributes using public property procedures
    @property #getter or accessor
    def Name(self):
        return self.__Name

    @Name.setter # (setter or mutator)
    def Name(self, Value):
        self.__Name = Value

    # Properties: Price
    #Gives access to private attributes using public property procedures
    @property #getter or accessor
    def Price(self):
        return self.__Price

    @Price.setter # (setter or mutator)
    def Price(self, Value):
        self.__Price = Value

    #--Methods--
    #A function iside a class (Method)
    #Methods allow us to organize processing statments into named groups
    def ToString (self):
        return str(self.Id) + "," + str(self.Name) + "," + str(self.Price)

    def __str__(self): # NOTE both double underscores in the name
        """Implictly returns field data"""
        return self.ToString() #referring to all three objects

#--End of class--
# ---Use of class ---

#I/O
try: #exception handling
    while (True): #While loop for user interaction
        intId = input("Enter the Id: ") #user input for Id field
        strName = input("Enter the Name: ") #user input for Name field
        intPrice = input("Enter the Price: ") #user input for Price field
        ObjP1 = Product(intId, strName, intPrice) #referring to "Product"class
        print(ObjP1)
        if(input("Type 'exit' to end or any other key to continue").lower() == "exit"): #input for user to exit or continue code
            break
        else: continue

    if (input("Would you like to save this data to a file? (y/n): ").lower() == "y"): #input to save file to a txt file
        objFile.write(str(ObjP1) + "\n")
        objFile.close()


    if (input ("Would you like to see the data saved? (y/n): ").lower() == "y"): #To view saved data
        objFile = open("C:\\PythonClass\\Assignment08\\Products.txt", "r") #"r" read file saved in txt file
        strData = objFile.read()  # read() reads all the data at once
        print("Here is the data saved" + "\n" + strData) #print txt file to user
        objFile.close() #close file
except FileNotFoundError as e: #exception handling specific to file name error
    print("Error: " + str(e) + "\n Please check the file name")
except Exception as e: #exception handling for error
   print("Error: " + str(e))
finally:
 if(objFile != None):objFile.close() #Close file if no error is found
#end
