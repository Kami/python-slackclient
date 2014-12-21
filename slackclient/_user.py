class User(object):
    def __init__(self, id, name, first_name, last_name, real_name,
                 is_admin=False, is_owner=False):
        self.id = id
        self.name = name
        self.first_name = first_name
        self.last_name = last_name
        self.real_name = real_name
        self.is_admin = is_admin
        self.is_owner = is_owner
