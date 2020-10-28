# DemoToolchain

This is a demo of the [IntegrCiTy](https://www.energy.kth.se/heat-and-power-technology/current-projects/integrcity-1.924848) toolchain.

## About

This demo gives an example of how the IntegrCiTy toolchain can be used:
* **consolidate and store** buildings and network data in the database
* **create simulation models** from this data
* **simulate and analyze** the system, then store the results to the database
* retrieve this data to **visualize the results**


## Installation and prerequisites

1. The [IntegrCiTy Data Access Layer](https://github.com/IntegrCiTy/dblayer) (including access to PostgreSQL databases and the IntegrCiTy co-simulation platform) can be installed from the command line:
```
pip install git+https://github.com/IntegrCiTy/dblayer#egg=dblayer
```

2. This demo uses [Docker Engine](https://docs.docker.com/engine/) for the execution of applications (3DCityDB, co-simulation).
Please follow [these instructions](https://docs.docker.com/get-docker/) to install it.

3. In addition, a working **PostgreSQL** implementation of the [3DCityDB](https://www.3dcitydb.org) has to be installed, including its [extensions](https://github.com/gioagu/3dcitydb_ade), the **Energy ADE**, the **Utility Network ADE**, the **Scenario ADE** and the **Simulation Package**.
Such a database setup is referred to as **extended 3DCityDB**.
For this demo, it is recommended to install the 3DCityDB as a Docker container, see [here](https://github.com/IntegrCiTy/dblayer/tree/master/scripts) for instructions.
