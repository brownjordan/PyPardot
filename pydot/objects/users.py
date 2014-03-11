class Users():
    """
    A class to query and use Pardot users.
    Prospect field reference: http://developer.pardot.com/kb/api-version-3/object-field-references#user
    """

    def __init__(self, client):
        self.client = client

    def query(self, **kwargs):
        """
        Returns the users matching the specified criteria parameters.
        Supported search parameters: http://http://developer.pardot.com/kb/api-version-3/querying-users#supported-search-criteria
        """
        result = self._get(path='/do/query', params=kwargs)
        return result

    def read_by_id(self, id=None, **kwargs):
        """
        Returns the data for the user specified by <id>. <id> is the Pardot ID of the target user."""
        kwargs['id'] = id
        result = self._post(path='/do/read/id/{id}'.format(id=kwargs.get('id')), params=kwargs)
        return result

    def read_by_email(self, email=None, **kwargs):
        """
        Returns the data for the user specified by <email>. <email> is the email address of the target user."""
        kwargs['email'] = email
        result = self._post(path='/do/read/email/{email}'.format(email=kwargs.get('email')), params=kwargs)
        return result

    def _get(self, path=None, params={}):
        """GET requests for the User object"""
        result = self.client._get(object='user', path=path, params=params)
        return result

    def _post(self, path=None, params={}):
        """POST requests for the User object"""
        result = self.client._post(object='user', path=path, params=params)
        return result

