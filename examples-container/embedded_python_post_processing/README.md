# Malaria_Sim Example with Embedded Python Post-Processing (EP4)

### Run example_comps.py in comps:
    python example_comps.py
### Run example_container.py in container platform:
  - Run example_container.py:
    ```python example_container.py```
  - View running status:
    - idmtools container status <experiment_id>
  - View the output in the local job directory which you can find in console output while running the example_container.py
  - Optionally view the same output in the Docker container:
    - User can find container ID from console output and use the following command to view the output:
    ```bash
        docker exec -it <container_id> bash
        cd /home/container-data/<suite_dir>/<experiment_dir>/<simulation_dir>
    ```