# Yihan Xiao 2018/09/27
# Main class of BioAnt

import abc, sys
from Position import Position

class BioAnt(object):

    def __init__(self, start_x, start_y, start_direction, command_sequence):
        self._position = Position(start_x, start_y)
        self._direction = start_direction
        self._command_sequence = command_sequence

    def ActionTaken(self, boundary_x, boundary_y):
        # Execute every command in the sequence
        for command in self._command_sequence:
            action = ActionFactory.CreateAction(command)
            # Skip invalid command
            if action is None: 
                continue
            action.SetPosition(self._position)
            action.SetDirection(self._direction)
            # Update the position and direction of this BioAnt
            # If the ant is going to move out of the boundary, ignore this action
            current_position, current_direction = action.TakeAction(command)
            if(current_position.x > boundary_x or 
               current_position.y > boundary_y or
               current_position.x < 0 or 
               current_position.y < 0):
                print("Ant will move out of boundary at " + str(current_position))
            else:
                self._position, self._direction = current_position, current_direction
                
    def GetPosition(self):
        return self._position
        
    def GetDirection(self):
        return self._direction
     
class ActionFactory(object):
    # Generate action
    @staticmethod
    def CreateAction(command):
        assert type(command) == str
        command_list = {
            'L':ActionTurnLeft(),
            'R':ActionTurnRight(),
            'M':ActionMoveForward()
            }
        try:
            return command_list[command]
        except KeyError:
            print("The input command " + command + " is not supported! Skip this command")
            return None

# Abstract type Action. All real actions inherit from it.
class Action(object):
    __metaclass__ = abc.ABCMeta
    # default
    _position = Position(0, 0)
    _direction = None

    def GetPosition(self):
        return _position

    def GetDirection(self):
        return _direction

    def SetPosition(self, position):
        assert type(position) == Position
        self._position = position

    def SetDirection(self, direction):
        assert type(direction) == str
        self._direction = direction

    @abc.abstractmethod
    def TakeAction(self, command):
        'Ant will move according to the command'
        return 

class ActionTurnLeft(Action):
    # Override
    def TakeAction(self, command):
        self.SetDirection({'N':'W', 'E':'N', 'S':'E', 'W':'S'}[self._direction])
        return self._position, self._direction

class ActionTurnRight(Action):
    # Override
    def TakeAction(self, command):
        self.SetDirection({'N':'E', 'E':'S', 'S':'W', 'W':'N'}[self._direction])
        return self._position, self._direction

class ActionMoveForward(Action):
    # Override
    def TakeAction(self, command):
        move = {'N':Position(0, 1), 'E':Position(1, 0), 'S':Position(0, -1), 'W':Position(-1, 0)}[self._direction]
        self.SetPosition(self._position + move)
        return self._position, self._direction
        
