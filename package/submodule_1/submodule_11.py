"""Short module description."""
import pandas as pd


class some_class_of_submodule:

    def __init__(self):
        r"""
        Documentation
        """
        print('You can create an instance of this class, but it does nothing.')

    def name(self):
        return 'some_class_of_submodule'


class some_daughter(some_class_of_submodule):

    def name(self):
        return 'some_daughter of some_class_of_submodule'
