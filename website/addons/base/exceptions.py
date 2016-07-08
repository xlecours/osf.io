"""
Custom exceptions for add-ons.
"""

class AddonError(Exception):
    pass

class InvalidFolderError(AddonError):
    pass

class HookError(AddonError):
    pass
