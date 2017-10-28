# ------------------------------------------------------------------------------
# CLASS ENTITLEMENT
# ------------------------------------------------------------------------------
class Entitlement:
    
    """
        An entitlement establishes a relationship between an organization and a 
        user. The relationships represents an action that a given user is entitled
        to do within the context of a given organization. 
    """
    
    # --------------------------------------------------------------------------
    # CONSTRUCTOR
    # --------------------------------------------------------------------------
    def __init__(self, org_id, user_id, **kwargs):
        self.org_id = org_id
        self.user_id = user_id
        if 'entitlement_id' in kwargs:
            self.entitlement_id = kwargs['entitlement_id']
    
    # --------------------------------------------------------------------------
    # METHOD IS STATE VALID
    # --------------------------------------------------------------------------
    def is_state_valid(self):
        pass
    
    # --------------------------------------------------------------------------
    # METHOD SAVE
    # --------------------------------------------------------------------------
    def save(self):
        pass