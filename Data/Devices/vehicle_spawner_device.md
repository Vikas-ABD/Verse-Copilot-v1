📘 **vehicle_spawner_device – UEFN Verse Device Documentation**

---

🔹 **Description**

The `vehicle_spawner_device` is the **base class** for all specialized vehicle spawner devices in Unreal Editor for Fortnite (UEFN). It supports dynamic spawning, enabling/disabling, and vehicle management in your island. Derived devices extend its functionality to specific vehicle types (e.g., cars, tanks, surfboards) for more control and customization.

---

🧱 **Verse Using Statement**
```verse
using { /Fortnite.com/Devices }
```

---

🔗 **Inheritance Hierarchy**
- creative_object
- creative_device_base
- vehicle_spawner_device
- (specialized spawners: sports car, taxi, quadcrasher, etc.)

---

🛠️ **Functions & Methods**
| Name                | Description                                                  |
|---------------------|--------------------------------------------------------------|
| `Enable()`          | Enables the spawner to allow vehicle spawning.              |
| `Disable()`         | Disables the spawner from spawning vehicles.                |
| `RespawnVehicle()`  | Spawns or respawns the vehicle, removing the current one.   |
| `DestroyVehicle()`  | Destroys the currently spawned vehicle if present.          |
| `AssignDriver(agent)` | Sets the agent as the driver of the vehicle.               |
| `GetTransform()`    | Returns the world transform of the spawner.                 |
| `MoveTo()`/`TeleportTo()` | Moves or teleports the spawner (and vehicle).           |

---

🧹 **Events (Data Members)**
| Name                        | Type                        | Description                                     |
|-----------------------------|-----------------------------|-------------------------------------------------|
| `SpawnedEvent`              | `listenable(fort_vehicle)`  | Fired when a vehicle is spawned or respawned.   |
| `DestroyedEvent`            | `listenable(tuple())`       | Fired when a vehicle is destroyed.              |
| `AgentEntersVehicleEvent`   | `listenable(agent)`         | Fired when an agent enters the vehicle.         |
| `AgentExitsVehicleEvent`    | `listenable(agent)`         | Fired when an agent exits the vehicle.          |
| *(Deprecated)*              |                             | Use `SpawnedEvent` and `DestroyedEvent`.        |

---

🎮 **Configuration Options (Details Panel)**
- **Vehicle Type**: Choose which specialized vehicle to spawn.
- **Enable At Game Start**: Set if the spawner is active at game start.
- **Respawn Handling**: Choose respawn logic (manual, timer, on destroy).
- **Team/Class Filtering**: Restrict vehicle usage by team or class.
- **Max Vehicles**: Cap simultaneous vehicle count.
- **VFX/SFX**: Enable or disable visual/audio effects on spawn/destroy.
- **Spawn Location**: Define where the vehicle appears.

---

🛠️ **Verse Usage Example**
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use vehicle_spawner_device
vehicle_spawner_example := class(creative_device):

    @editable
    VehicleSpawner : vehicle_spawner_sports_car_device = vehicle_spawner_sports_car_device{}

    @editable
    SpawnButton : button_device = button_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        VehicleSpawner.SpawnedEvent.Subscribe(OnVehicleSpawned)
        VehicleSpawner.DestroyedEvent.Subscribe(OnVehicleDestroyed)
        VehicleSpawner.AgentEntersVehicleEvent.Subscribe(OnAgentEntersVehicle)
        VehicleSpawner.AgentExitsVehicleEvent.Subscribe(OnAgentExitsVehicle)

        SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnVehicleSpawned(Vehicle : fort_vehicle) : void =
        Print("Vehicle spawned!")

    OnVehicleDestroyed() : void =
        Print("Vehicle destroyed!")

    OnAgentEntersVehicle(Agent : agent) : void =
        Print("Agent entered vehicle!")

    OnAgentExitsVehicle(Agent : agent) : void =
        Print("Agent exited vehicle!")

    OnSpawnPressed(Agent : agent) : void =
        VehicleSpawner.RespawnVehicle()
        Print("Vehicle respawned!")

    OnEnablePressed(Agent : agent) : void =
        VehicleSpawner.Enable()
        Print("Vehicle spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        VehicleSpawner.Disable()
        Print("Vehicle spawner disabled!")
```

---

💼 **How to Use in UEFN**
1. **Place Device**: Drag a specialized vehicle spawner into your level.
2. **Configure Options**: Set respawn method, access filters, effects, etc.
3. **Add Buttons**: Place three `button_device`s labeled "Spawn", "Enable", and "Disable".
4. **Create Verse File**:
   - Right-click folder in Verse Explorer → Create New Verse File (e.g., `vehicle_spawner_example.verse`)
   - Paste example code and save
   - Build with Ctrl+Shift+B until "Build Succeeded"
   - Drag your Verse device into the world
5. **Assign @editable References** in Details panel:
   - `VehicleSpawner`: Link to your placed spawner device
   - `SpawnButton` / `EnableButton` / `DisableButton`: Link to button devices
6. **Test**: Interact with buttons in-game to test spawning, enabling, disabling, and observe event prints.

---

🧠 **Best Practices**
- Use events for custom gameplay logic: scoring, tracking, objectives
- Enable/Disable devices to manage vehicle access phases
- Use `.AssignDriver(agent)` for guided missions, racing, team play

---

❌ **Common Issues & Fixes**
| Issue                  | Problem Example                     | Solution                                     | Explanation                                  |
|------------------------|-------------------------------------|----------------------------------------------|----------------------------------------------|
| No vehicle spawned     | Didn’t call `RespawnVehicle()`      | Use button/event/script to trigger spawn     | Explicit call needed to spawn vehicle        |
| Players can't interact | Wrong team/class setting            | Configure correct team/class in Details      | Spawner restricts access without config      |
| Code not working       | @editable fields not assigned       | Assign all references in Details             | Verse code fails without proper linking      |
| Deprecated events used | Using `VehicleSpawnedEvent`         | Switch to `SpawnedEvent` and `DestroyedEvent`| Legacy events not supported in new Verse     |

---

💡 **Note:**
- Always use a **specific derived spawner** for the intended vehicle (e.g., `vehicle_spawner_sports_car_device`).
- The `vehicle_spawner_device` provides core logic for spawning, events, and state control, extendable in your custom devices.

