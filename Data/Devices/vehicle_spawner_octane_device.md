# UEFN Verse Device Documentation: `vehicle_spawner_octane_device`

## 🔹 Description
The `vehicle_spawner_octane_device` allows the creation and control of Octane vehicles—agile, rocket-boosted cars inspired by Rocket League. It supports full Verse scripting to:

- Spawn, eliminate, and manage Octane cars
- Enable/disable the spawner
- Respawn vehicles at runtime
- Assign drivers
- Teleport or move the spawner
- Subscribe to events such as vehicle spawn, destruction, agent enter/exit

Ideal for races, stunts, and team-based games.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `vehicle_spawner_device`
- `vehicle_spawner_octane_device`

## 🛠️ Key Methods & Functions
| Method | Description |
|--------|-------------|
| `Enable()` | Enables the vehicle spawner. |
| `Disable()` | Disables the spawner and optionally eliminates the vehicle. |
| `RespawnVehicle()` | Spawns a new Octane vehicle, destroying the old one. |
| `DestroyVehicle()` | Immediately eliminates the spawned Octane. |
| `AssignDriver(agent)` | Assigns a player as the vehicle’s driver. |
| `GetTransform()` | Gets the spawner’s position/rotation. |
| `MoveTo()/TeleportTo()` | Relocates the spawner. |

## 🧹 Events
| Event | Type | Description |
|-------|------|-------------|
| `SpawnedEvent` | `listenable(fort_vehicle)` | Fires when vehicle spawns or respawns. |
| `DestroyedEvent` | `listenable(tuple())` | Fires when vehicle is eliminated. |
| `AgentEntersVehicleEvent` | `listenable(agent)` | Player enters vehicle. |
| `AgentExitsVehicleEvent` | `listenable(agent)` | Player exits vehicle. |

## 🎛 Device Configuration (Details Panel)
- **Octane Vehicle Customization**: Colors, FX, wheels, decals/flags, boost, handling
- **Vehicle Health/Indestructible**: Health points, destruction rules
- **Spawn When Enabled**: Vehicle spawns immediately if set
- **Destroy on Disable**: Removes car when disabling device
- **Can Be Damaged/Killed by Vehicles**: Collisions settings
- **Tricks Enabled**: Enables Rocket League-style tricks
- **Water Destruction**: Destroys car if submerged (optional delay)

## 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

octane_vehicle_example := class(creative_device):

    @editable
    OctaneSpawner : vehicle_spawner_octane_device = vehicle_spawner_octane_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    RespawnButton : button_device = button_device{}

    var CurrentVehicle : ?fort_vehicle = false

    OnBegin<override>()<suspends> : void =
        OctaneSpawner.SpawnedEvent.Subscribe(OnVehicleSpawned)
        OctaneSpawner.DestroyedEvent.Subscribe(OnVehicleDestroyed)
        OctaneSpawner.AgentEntersVehicleEvent.Subscribe(OnAgentEntersVehicle)
        OctaneSpawner.AgentExitsVehicleEvent.Subscribe(OnAgentExitsVehicle)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        RespawnButton.InteractedWithEvent.Subscribe(OnRespawnPressed)

    OnVehicleSpawned(Vehicle : fort_vehicle) : void =
        set CurrentVehicle = option{Vehicle}
        Print("Octane vehicle spawned!")

    OnVehicleDestroyed() : void =
        set CurrentVehicle = false
        Print("Octane vehicle destroyed!")

    OnAgentEntersVehicle(Agent : agent) : void =
        Print("Agent entered Octane vehicle!")

    OnAgentExitsVehicle(Agent : agent) : void =
        Print("Agent exited Octane vehicle!")

    OnEnablePressed(Agent : agent) : void =
        OctaneSpawner.Enable()
        Print("Octane spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        OctaneSpawner.Disable()
        Print("Octane spawner disabled!")

    OnRespawnPressed(Agent : agent) : void =
        OctaneSpawner.RespawnVehicle()
        Print("Octane vehicle respawned!")

    AssignDriver(Agent : agent) : void =
        if (Vehicle := CurrentVehicle?):
            # Assign logic here
            Print("Driver assigned to vehicle")

    RemoveDriver(Agent : agent) : void =
        if (Vehicle := CurrentVehicle?):
            # Removal logic here
            Print("Driver removed from vehicle")
```

## 📖 How to Use in UEFN
### 1. Place Devices in Level
- Add `vehicle_spawner_octane_device` from Devices tab
- Add three `button_device`s labeled Enable, Disable, Respawn

### 2. Configure the Octane Spawner
- Set colors, boost, FX, health, and spawn/destroy rules in Details panel

### 3. Create and Add Verse Script
- Go to Verse Explorer > Create New Verse File (e.g., `octane_vehicle_example.verse`)
- Paste sample code, save, and build (Ctrl+Shift+B)

### 4. Assign @editable References
- In the Verse device's Details, set OctaneSpawner and Button references

### 5. Test the Level
- Launch a session and interact with buttons

## 🧠 Best Practices
- Use events to update score, show FX, or switch rounds
- Use `AssignDriver()` for race logic or checkpoint starts
- Use `TeleportTo()` or `MoveTo()` to make dynamic tracks

## ❌ Common Issues & Fixes
| Issue | Problem | Solution |
|-------|---------|----------|
| Vehicle not spawning | Not enabled or spawn-on-enable off | Call `.Enable()` or change settings |
| Car not eliminated | "Destroy on Disable" not set | Enable destroy option in Details |
| No driver assigned | No `AssignDriver(agent)` call | Trigger logic to call assignment |
| Verse script not working | Missing @editable or not built | Set refs and build Verse |

## 🔧 Note
- Octane physics, tricks, and movement handled by Fortnite
- Use Verse for game logic, scoring, and race/obstacle design
- Perfect for creative stunt and racing maps

