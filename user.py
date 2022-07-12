
from contact import Contact
class User:
    userID = -1
    userList = []
    def __init__(self, userName, fName, lName, isAdmin, isActive, contactsList):
        self.userID = User.userID
        self.userName = userName
        self.fName = fName
        self.lName = lName
        self.isAdmin = isAdmin
        self.isActive = isActive
        self.contactsList = contactsList

    def findContact(self, username):
        for contact in self.contactsList:
            if contact.username == username and contact.isActive == True:
                return True, contact
        return False, None

    def findUser(username):
        for user in User.userList:
            if user.userName == username and user.isActive == True:
                return True, user
        return False, None
    
    def addContact(self, f_name, l_name, username, isActive, contactDetailsList):
        if(self.isActive):
            isContactExist, contact = self.findContact(username)
            if not isContactExist:
                contactObject = Contact.createContact(f_name, l_name, username, isActive, contactDetailsList)
                self.contactsList.append(contactObject)
                print("Contact added successfully")
            else:
                print("Contact Already Exists")
        else:
            print("Operation Denied")

    def removeContact(self, username):
        if(self.isActive):
            isContactExist, contact = self.findContact(username)
            if isContactExist:
                Contact.deleteContact(contact)
                print("Deleted succesfully")
            else:
                print("Contact not found")
        else:
            print("Operation Denied")

    def modifyContact(self, username, propertyName, value):
        if(self.isActive):
            isContactExist, contact = self.findContact(username)
            if isContactExist:
                Contact.updateContact(contact)
                print("Updated succesfully")
            else:
                print("Contact not found")
        else:
            print("Operation Denied")

    def aboutContact(self, username):
        if(self.isActive):
            isContactExist, contact = self.findContact(username)
            if isContactExist:
                Contact.readContact(contact)
            else:
                print("Contact not found")
        else:
            print("Operation Denied")

    def addContactDetails(self, contactUsername, contactDetailUsername, type, numberOrEmail):
        if(self.isActive):
            isContactExist, contact = self.findContact(contactUsername)
            if isContactExist:
                Contact.createContactDetails(contact, contactDetailUsername, type, numberOrEmail)
            else:
                print("Contact not found")
        else:
            print("Operation Denied")
        

    def aboutContactDetails(self, contactUsername, contactDetailUsername):
        if(self.isActive):
            isContactExist, contact = self.findContact(contactUsername)
            if isContactExist:
                Contact.readContactDetails(contact, contactDetailUsername)
            else:
                print("Contact not found")
        else:
            print("Operation Denied")


    def modifyContactDetails(self, contactUsername, contactDetailUsername, propertyName, value):
        if(self.isActive):
            isContactExist, contact = self.findContact(contactUsername)
            if isContactExist:
                Contact.updateContactDetails(contact, contactDetailUsername, propertyName, value)
            else:
                print("Contact not found")
        else:
            print("Operation Denied")
        
    def createUser(self, userName, fName, lName, isAdmin, isActive, contactsList):
        if(self.isAdmin):
            if(self.isActive):
                isUserPresent, userObject = self.findUser(userName)
                if isUserPresent:
                    print("User with this username already exists")
                    return None
                else:
                    User.userID += 1
                    userObj = User(userName, fName, lName, isAdmin, isActive, contactsList)
                    User.userList.append(userObj)
                    print("User added succesfully")
                    return userObj
            else:
                print("Operation Denied")
        else:
            print("Operation denied")


    def deleteUser(self, userName):
        if(self.isAdmin):
            if(self.isActive):
                isUserPresent, userObject = self.findUser(userName)
                if isUserPresent:
                    userObject.isActive = False
                    print("User Deleted successfully")
                    return
                else:
                    print("User not found")
                    return 
            else:
                print("Operation Denied")
        else:
            print("Operation denied")

    def updateUser(self, userName, propertyName, value):
        if(self.isAdmin):
            if(self.isActive):
                isUserPresent, userObject = self.findUser(userName)
                if isUserPresent:
                    setattr(userObject, propertyName, value)
                    print("User updated successfully")
                    return
                else:
                    print("User not found")
                    return 
            else:
                print("Operation Denied")
        else:
            print("Operation denied")

    def readUser(self, userName, propertyName, value):
        if(self.isAdmin):
            if(self.isActive):
                isUserPresent, userObject = self.findUser(userName)
                if isUserPresent:
                    print(vars(userObject))
                    return
                else:
                    print("User not found")
                    return 
            else:
                print("Operation Denied")
        else:
            print("Operation denied")

    