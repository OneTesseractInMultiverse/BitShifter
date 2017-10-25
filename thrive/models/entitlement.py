class Entitlement:
    
    def __init__(self, org_id, user_id, **kwargs):
        self.org_id = org_id
        self.user_id = user_id
        if 'entitlement_id' in kwargs:
            self.entitlement_id = kwargs['entitlement_id']
    
    def state_valid(self):
        pass
    
    def save(self):
        pass