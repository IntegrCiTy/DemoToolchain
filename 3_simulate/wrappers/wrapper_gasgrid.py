import json

import numpy as np
import pandas as pd

import pandangas as pg
import pandangas.simulation as pgsim
import pandangas.utilities as pgutil

from dblayer.sim.pandangas import *
from dblayer import *

from zerobnl.kernel import Node


class GasGrid( Node ):

    def __init__( self ):
        super().__init__()

        connect = PostgreSQLConnectionInfo(
            user = self.init_values[ 'dbuser' ],
            pwd = self.init_values[ 'dbpwd' ],
            host = self.init_values[ 'dbhost' ],
            port = self.init_values[ 'dbport' ],
            dbname = self.init_values[ 'dbname' ]
        )

        pg_reader = PandaNGasModelDBReader( connect )
        
        self.net = pg_reader.get_net( network_id = self.init_values[ 'network_id' ] )
        print(self.net)
        
        self.p_nodes, self.m_dot_pipes, self.m_dot_nodes, gas = \
            pgsim._run_sim( self.net, level = 'BP' )



    def set_attribute( self, attr, value ):
        super().set_attribute( attr, value )

        if '/' in attr:
            load_name, value_name = attr.split( '/' )
            idx = pgutil.get_index( load_name, self.net.load )
            self.net.load[ value_name ][ idx ] = value
        else:
            setattr( self, attr, value )

        
    def get_attribute( self, attr ):
        super().get_attribute( attr )

        element_name, value_name = attr.split( '/' )
        element_type = element_name[:8]
        
        if element_type == 'gas_pipe' and value_name == 'm_dot':
            return self.m_dot_pipes[ element_name ]
        elif element_type == 'gas_node' and value_name == 'm_dot':
            return self.m_dot_nodes[ element_name ]
        elif element_type == 'gas_node' and value_name == 'P':
            return self.p_nodes[ element_name ]


    def step( self, value ):
        super().step( value )

        self.p_nodes, self.m_dot_pipes, self.m_dot_nodes, gas = \
            pgsim._run_sim( self.net, level = 'BP' )

        for attr in [ '{}/P'.format(k) for k in self.p_nodes.keys() ]:
            self.save_attribute( attr )

        for attr in [ '{}/m_dot'.format(k) for k in self.m_dot_pipes.keys() ]:
            self.save_attribute( attr )


if __name__ == '__main__':
    node = GasGrid()
    node.run()
