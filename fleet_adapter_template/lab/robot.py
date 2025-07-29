
from functools import partial

# Mock Robot class
class Robot:
    def __init__(self, name):
        self.name = name
        self.update_handle = None

# Mock update handle
class UpdateHandle:
    def __init__(self, info):
        self.info = info

# The callback function
def _updater_inserter(cmd_handle, update_handle):
    cmd_handle.update_handle = update_handle
    print(f"Set update_handle for {cmd_handle.name} to {update_handle.info}")

# Create a robot instance
robot = Robot("robot1")

# Create a partial function with robot as the first argument
callback = partial(_updater_inserter, robot)

# Simulate add_robot calling the callback with an update handle
update_handle = UpdateHandle("handle_123")
callback(update_handle)  # Equivalent to _updater_inserter(robot, update_handle)

# Check result
print(robot.update_handle.info)  # Output: handle_123