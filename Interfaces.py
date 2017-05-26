from abc import ABCMeta, abstractmethod

class IAlterationEntity():

    @abstractmethod
    def check_n_change(self, logLine):
        """ Change the entity due to string from logFile"""

class IAction():
    def do_action(self):
        """ Does some action and returns bool if it valid"""