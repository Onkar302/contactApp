from contact_details import Contact_Details
class Contact:
    contactID = -1
    def __init__(self, fName, lName, username, isActive, contactDetailsList):
        self.contactID = Contact.contactID
        self.fName = fName
        self.lName = lName
        self.username = username
        self.isActive = isActive
        self.contactDetailsList = contactDetailsList

    @staticmethod
    def findContactDetails(contactObject, contactDetailUsername):
        for contactDetail in contactObject.contactDetailsList:
            if contactDetail.contactDetailsUsername == contactDetailUsername:
                return True, contactDetail
        return False, None

    @staticmethod
    def createContact(fName, lName, username, isActive, contactDetailsList):
        Contact.contactID += 1
        newContact = Contact(fName, lName, username, isActive, contactDetailsList)
        return newContact

    @staticmethod
    def deleteContact(contactObject):
        contactObject.isActive = False
        
    @staticmethod
    def updateContact(contactObject, propertyName, value):
        setattr(contactObject, propertyName, value)

    @staticmethod
    def readContact(contactObject):
        print(vars(contactObject)) 

    @staticmethod
    def createContactDetails(contactObject, contactDetailUsername, type, numberOrEmail):
        isContactDetailpresent, contactDetail = contactObject.findContactDetails(contactObject, contactDetailUsername)
        if isContactDetailpresent:
            print("Details already present")
            return
        Contact_Details.contactDetailsID += 1
        contactDetailObject = Contact_Details(contactDetailUsername, type, numberOrEmail)
        contactObject.contactDetailsList.append(contactDetailObject)
        print("Contact Details added successfully")

    @staticmethod
    def updateContactDetails(contactObject, contactDetailUsername, propertyName, value):
        isContactDetailpresent, contactDetail = contactObject.findContactDetails(contactObject, contactDetailUsername)
        if isContactDetailpresent:
            setattr(contactDetail, propertyName, value)
            print("Updated contact details successfully")
            return
        print("Contact Details not found")

    @staticmethod
    def readContactDetails(contactObject, contactDetailUsername):
        isContactDetailpresent, contactDetail = contactObject.findContactDetails(contactObject, contactDetailUsername)
        if isContactDetailpresent:
            print(vars(contactDetail)) 
            return
        print("Contact Details not found")

    
        



        