import pandas as pd

from zerobnl.kernel import Node


class Consumers( Node ):

    def __init__( self ):
        super().__init__()
        self.gas_demand = pd.read_pickle( 'gas_demand.pkl' )
        self.t0 = pd.Timestamp( self.init_values['start_date'] )

    def set_attribute( self, attr, value ):
        super().set_attribute( attr, value )
        setattr( self, attr, value )

    def get_attribute( self, attr ):
        super().get_attribute( attr )
        return float( self.gas_demand[attr][self.t] )

    def step( self, value ):
        super().step( value )
        self.t = self.t0 + pd.Timedelta( seconds = self.simu_time )


if __name__ == '__main__':
    node = Consumers()
    node.run()
