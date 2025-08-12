# fleet_adapter_template

## Build Instructions

This demo uses `cleanerBotA_config.yaml` and `hotel.build.yaml` map from the rmf-demos repository to create a fleet adapter.

## Step 1: Generate Traffic Navigation Path File
```bash
ros2 run rmf_building_map_tools building_map_generator nav \
  ${building_map_path}/map/hotel.building.yaml ${output_nav_graphs_dir}/map
```

## Step 2: Start fleet manager
```bash
ros2 run fleet_adapter_template fleet_adapter -c CONFIG_FILE -n NAV_GRAPH
Example:
ros2 run rmf_demos_fleet_adapter_1 fleet_manager_1 -c src/rmf_demos_fleet_adapter_1/cleanerBotA_config.yaml -n src/rmf_demos_fleet_adapter_1/map/1.yaml
```

## Step 3: Start fleet adapter
```bash
ros2 run fleet_adapter_template fleet_adapter -c CONFIG_FILE -n NAV_GRAPH -s ws://localhost:8000/_internal
Example:
ros2 run fleet_adapter_template fleet_adapter -c src/fleet_adapter_template/fleet_adapter_template/cleanerBotA_config.yaml -n src/fleet_adapter_template/fleet_adapter_template/map/1.yaml -s "http://192.168.1.16:8000/_internal"
```
