class Contact_Details:
    contactDetailsID = -1
    def __init__(self, contactDetailsUsername, type, numberOrEmail):
        self.contactDetailsUsername = contactDetailsUsername
        self.contactDetailsID = Contact_Details.contactDetailsID
        self.type = type
        self.numberOrEmail = numberOrEmail