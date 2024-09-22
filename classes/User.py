class User:
    def __init__(self, first_name, last_name, gender, membership, remarks):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.membership = membership
        self.remarks = remarks
        self.username = first_name + last_name
