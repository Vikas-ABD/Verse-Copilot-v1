# Guide to Using `vehicle_spawner_pickup_truck_device` in Unreal Editor for Fortnite (UEFN)

## 🔊 Description
The `vehicle_spawner_pickup_truck_device` is a specialized spawner for configuring and managing Pickup Trucks in UEFN. It offers built-in methods for enabling/disabling the device, spawning and destroying vehicles, assigning agents (players or AI) as drivers, and handling key events like vehicle spawn, destruction, and agent entry/exit.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
```
creative_object
└ creative_device_base
   └ vehicle_spawner_device
      └ vehicle_spawner_pickup_truck_device
```

## 🛠️ Key Methods & Events
| Name | Description |
|------|-------------|
| Enable() / Disable() | Enable or disable the spawner device |
| RespawnVehicle() | Spawns a new Pickup Truck (destroys existing one) |
| DestroyVehicle() | Eliminates the currently spawned Pickup Truck |
| AssignDriver(agent) | Assigns an agent as the driver of the truck |
| AgentEntersVehicleEvent | Triggered when an agent enters the truck |
| AgentExitsVehicleEvent | Triggered when an agent exits the truck |
| SpawnedEvent | Triggered when the truck is spawned |
| DestroyedEvent | Triggered when the truck is destroyed |

## 🛠️ Verse Example
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

vehicle_spawner_pickup_truck_example := class(creative_device):

    @editable
    TruckSpawner : vehicle_spawner_pickup_truck_device = vehicle_spawner_pickup_truck_device{}

    @editable
    SpawnButton : button_device = button_device{}

    @editable
    DestroyButton : button_device = button_device{}

    @editable
    AssignDriverButton : button_device = button_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    var IsEnabled : logic = true

    OnBegin<override>()<suspends> : void =
        TruckSpawner.AgentEntersVehicleEvent.Subscribe(OnEnter)
        TruckSpawner.AgentExitsVehicleEvent.Subscribe(OnExit)
        TruckSpawner.SpawnedEvent.Subscribe(OnSpawn)
        TruckSpawner.DestroyedEvent.Subscribe(OnDestroyed)

        SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)
        DestroyButton.InteractedWithEvent.Subscribe(OnDestroyPressed)
        AssignDriverButton.InteractedWithEvent.Subscribe(OnAssignDriverPressed)
        EnableButton.InteractedWithEvent.Subscribe(OnEnable)
        DisableButton.InteractedWithEvent.Subscribe(OnDisable)

    OnEnter(Agent : agent) : void =
        Print("Agent entered Pickup Truck!")

    OnExit(Agent : agent) : void =
        Print("Agent exited Pickup Truck!")

    OnSpawn(Vehicle : fort_vehicle) : void =
        Print("Pickup Truck spawned!")

    OnDestroyed() : void =
        Print("Pickup Truck destroyed!")

    OnSpawnPressed(Agent : agent) : void =
        if (IsEnabled = true):
            TruckSpawner.RespawnVehicle()
            Print("Pickup Truck respawned via button.")

    OnDestroyPressed(Agent : agent) : void =
        if (IsEnabled = true):
            TruckSpawner.DestroyVehicle()
            Print("Pickup Truck destroyed via button.")

    OnAssignDriverPressed(Agent : agent) : void =
        if (IsEnabled = true):
            TruckSpawner.AssignDriver(Agent)
            Print("Agent assigned as Pickup Truck driver.")

    OnEnable(Agent : agent) : void =
        if (IsEnabled = false):
            set IsEnabled = true
            Print("Pickup Truck spawner enabled.")

    OnDisable(Agent : agent) : void =
        if (IsEnabled = true):
            set IsEnabled = false
            Print("Pickup Truck spawner disabled.")
```

## 💪 UEFN Step-by-Step Setup

### 1. Place Devices in the Level
- Add one `vehicle_spawner_pickup_truck_device` to your world.
- Add up to five `button_device` instances for control actions: Spawn, Destroy, Assign Driver, Enable, Disable.

### 2. Create a Verse Script
- Open Verse Explorer (Verse → Verse Explorer).
- Right-click your project folder → Create New Verse File → name it (e.g., `vehicle_spawner_pickup_truck_example.verse`).
- Choose "Create Empty" and paste in the code sample above. Save the file.

### 3. Build the Verse Script
- From the top menu, choose: Verse → Build Verse Code (Ctrl+Shift+B).
- Ensure "Build Succeeded" appears.

### 4. Place and Reference Devices
- Drag your new Verse device into the level.
- In the Details panel:
  - Set `TruckSpawner` to your pickup truck spawner device.
  - Link the button devices to the corresponding variables (SpawnButton, DestroyButton, etc).

### 5. Customize the Truck Spawner
- In the Details panel of the spawner, configure:
  - Respawn delay
  - Team access
  - Vehicle settings
  - Initial enabled state

### 6. Test
- Start a play session.
- Press the buttons to spawn/destroy the truck, assign a driver, or enable/disable the spawner.
- Watch logs for event confirmations.

## 🧠 Tips
- Use multiple truck spawners for team-based gameplay.
- Trigger gameplay logic, UI updates, or scoring from the event handlers.
- Ensure a truck is spawned before assigning a driver.

## ❌ Troubleshooting
| Issue | Solution |
|-------|----------|
| Truck doesn’t spawn | Make sure the device is enabled and Verse is built |
| Agent not assigned | Ensure the truck exists and the agent is valid |
| No logs/events firing | Check subscriptions and Verse script bindings |

---
All major vehicle logic (spawn, destroy, enable/disable, assign driver) is controllable via Verse scripting for dynamic, interactive gameplay experiences.

