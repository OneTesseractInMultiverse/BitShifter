from bitshifter import graph
from bitshifter.extensions.time import timestamp
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
        """
            Given an organization id, it fetches the data that currently exists
            in the Graph 
        """
        if self.id is not None:
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
        """
            Gets the Node reference for the current organization. If the org hasn't
            been persisted yet, then this will return None. 
        """
        if self.is_persistent:
            return graph.find_one('Organization', 'id', self.id)
        return None
    
    
    # --------------------------------------------------------------------------
    # METHOD IS STATE VALID
    # --------------------------------------------------------------------------
    def state_is_valid(self):
        """
            Verifies if all the required properties that must be present are present
            if some required property is missing, then this will return false.
        """
        if self.name is not None  and self.description is not None and self.email is not None and self.domain is not None:
            return True
        return False
    
    # --------------------------------------------------------------------------
    # METHOD SAVE
    # --------------------------------------------------------------------------
    def save(self):
        """
            Persists or updates the persisted representation of an organization 
            in the persistent graph. 
        """
        
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
        self.is_persistent = True
        return True
        
        
