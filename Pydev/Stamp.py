# Yihan Xiao 2018/09/27
# Stamp class will build the environment where bionic ant navigate

from BioAnt import BioAnt

class Stamp(object):
    '''The environment where BioAnts are navigating inside'''

    def __init__(self, input_lines):
        '''Process input lines'''
        self.stamp_boundary_x = 0
        self.stamp_boundary_y = 0
        self.ants_list = []

        lines = input_lines.strip().splitlines()
        for i in range(len(lines)):
            # First line should be the boundary of stamp
            if i == 0:
                boundary_positions = lines[i].split()
                self.stamp_boundary_x = int(boundary_positions[0])
                self.stamp_boundary_y = int(boundary_positions[1])
            else:
                if i%2 == 1: # the line indicating initial postion of the ant
                    ant_init_states = lines[i].split()
                elif i%2 == 0: # the line indicating command sequence for the ant
                    ant_command_sequence = lines[i].strip()
                    new_ant = BioAnt(int(ant_init_states[0]), int(ant_init_states[1]), ant_init_states[2], ant_command_sequence)
                    self.ants_list.append(new_ant)

    def AntsNavigate(self):
        '''Run all ants respectively'''
        output = ''
        print('Waiting for ants to finish exploring:')
        for ant in self.ants_list:
            ant.ActionTaken(self.stamp_boundary_x, self.stamp_boundary_y)
            result = str(ant.GetPosition()) + ' ' + ant.GetDirection()
            output += ' ' + result
            # show in console
            print(result)

        return output.strip()
                    


