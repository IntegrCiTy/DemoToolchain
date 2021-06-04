# IntegrCiTy Data Access Layer demo application

This is a demo of the [IntegrCiTy](https://www.energy.kth.se/heat-and-power-technology/current-projects/integrcity-1.924848) toolchain.

## About

This demo gives an example of how the IntegrCiTy toolchain can be used:
* **consolidate and store** buildings and network data in the database
* **create simulation models** from this data
* **simulate and analyze** the system, then store the results to the database
* retrieve this data to **visualize the results**

## Installation and prerequisites

1. To install the [IntegrCiTy Data Access Layer](https://github.com/IntegrCiTy/dblayer) and all other Python packages needed for this demo run the following in your terminal:
   ```
   pip install -r requirements.txt
   ```

2. The IntegrCiTy toolchain requires [Docker Engine](https://docs.docker.com/engine/) for the definition and execution of used applications (3DCityDB, co-simulation).
Please follow [these instructions](https://docs.docker.com/get-docker/) to install it.

3. On top of Docker, the IntegrCiTy toolchain uses [Docker Compose](https://docs.docker.com/compose/) for the orchestration of the co-simulation.
Please follow [these instructions](https://docs.docker.com/compose/install/) to install it.

4. In addition, a working **PostgreSQL** implementation of the [3DCityDB](https://www.3dcitydb.org) has to be installed, including its [extensions](https://github.com/gioagu/3dcitydb_ade), the **Energy ADE**, the **Utility Network ADE**, the **Scenario ADE** and the **Simulation Package**.
Such a database setup is referred to as **extended 3DCityDB**.
For this demo, it is recommended to install the 3DCityDB as a Docker container, see [here](https://github.com/IntegrCiTy/dblayer/tree/master/scripts) for instructions.

**NOTE**: This setup has been tested and verified to work with **Python 3.6.8**.

**NOTE**: It is recommended to install this demo in a **separate Python environment** (via [conda](https://docs.conda.io/en/latest/), [virtualenv](https://virtualenv.pypa.io/en/latest/) or others).

## Running the demo

* The demo uses a series of [Jupyter notebooks](https://jupyter.org/) that are intended to be executed in sequence.
  To start the demo, type in your terminal:
  ```
  jupyter notebook
  ```
* This will either start the notebook server in your browser automatically, or you will have to copy the URL displayed in the terminal to your browser.
* In subfolder [1_data](./1_data) you can take a look at the raw data that will be used for this demo.
* The actual demo starts in subfolder [2_citydb](./2_citydb), where you will find the first notebook [2a_buildings.ipynb](./2_citydb/2a_buildings.ipynb).
