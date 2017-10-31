from bitshifter import graph
import uuid

# ------------------------------------------------------------------------------
# CLASS ORGANIZATION
# ------------------------------------------------------------------------------
class Organization:
    
    """
        This entity represents an organization's identity within the system. There
        are users that are entitled to perform several actions or tasks on a
        given organization through entitlements linked to 
    """
    
    # --------------------------------------------------------------------------
    # CONSTRUCTOR
    # --------------------------------------------------------------------------
    def __init__(self, **kwargs):
        """
            Creates instances of Organization. If an organization is created with
            the org_id parameter supplied, the system will attempt to load the 
            organiszation from persistent storage, if no org_id is supplied, then
            a new instance of 
        """
        
        if 'id' in kwargs:
            self.id = kwargs['id']
            self.__load__()
        else:
            if 'name' in kwargs:
                self.name = kwargs['name']
            if 'description' in kwargs:
                self.description = kwargs['description']
            if 'email' in kwargs:
                self.email = kwargs['email']
            if 'domain' in kwargs:
                self.domain = kwargs['domain']
            self.is_persistent = False
                
    # --------------------------------------------------------------------------
    # METHOD LOAD 
    # --------------------------------------------------------------------------
    def __load__(self):
        if self.org_id is not None:
            org = graph.find_one('Organization', 'id', self.id)
            if 'name' in org:
                self.name = org['name']
            if 'description' in org:
                self.description = org['description']
            if 'email' in org:
                self.email = org['email']
            if 'domain' in org:
                self.domain = org['domain']
            self.is_persistent = True

    # --------------------------------------------------------------------------
    # METHOD AS NODE
    # --------------------------------------------------------------------------
    def as_node(self):
        return graph.find_one('Organization', 'id', self.id)
    
    # --------------------------------------------------------------------------
    # METHOD IS STATE VALID
    # --------------------------------------------------------------------------
    def is_state_valid(self):
        pass
    
    # --------------------------------------------------------------------------
    # METHOD SAVE
    # --------------------------------------------------------------------------
    def save(self):
        
        if self.id is None:
            self.id = uuid.uuid4()
        
        # Merge or create Node with unique property
        org = Node(
            'Organization',
            id = self.id
        )
        
        graph.merge(org)
        
        # Now we update all the non-unique properties
        org['name'] = self.name, 
        org['description'] = self.description, 
        org['email'] = self.email, 
        org['domain'] = self.domain
        
        # Persist changes in the Node
        org.push()
        
        return True