class NotAuthorizedException(Exception):
    pass

class IllegalIdentifierException(Exception):
    pass

class NotAPersonException(Exception):
    pass

class NotAPatientException(Exception):
    pass

class NonexistentVersionException(Exception):
    pass

class PatientAlreadyDeletedException(Exception):
    pass

class NotTheLatestVersionException(Exception):
    def __init__(self, message, latest_version):
        self.latest_version = latest_version
        self.message = message
        super().__init__(self.message)

class NonexistentPatientException(Exception):
    pass

class NonexistentVersionAtTimeException(Exception):
    pass

class NonexistentContributionException(Exception):
    pass