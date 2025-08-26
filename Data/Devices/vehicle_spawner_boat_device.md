## vehicle_spawner_boat_device in UEFN

### 🔹 Description
The `vehicle_spawner_boat_device` is a specialized version of `vehicle_spawner_device` for spawning and controlling boats on your island. With this device, you can spawn, eliminate, re-spawn, assign drivers, and respond to the boat’s key events using both device settings and Verse scripting.

---

### 🛡️ Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
- `creative_object`
  - `creative_device_base`
    - `vehicle_spawner_device`
      - `vehicle_spawner_boat_device`

---

### 🛠️ Key Methods & Events
| Name | Description |
|------|-------------|
| `Enable()`, `Disable()` | Enables/disables the boat spawner device |
| `RespawnVehicle()` | Spawns a new boat, eliminating any previous instance |
| `DestroyVehicle()` | Instantly eliminates the spawned boat |
| `AssignDriver(agent)` | Assigns the agent as the boat’s driver |
| `AgentEntersVehicleEvent` | Fires when an agent enters the boat |
| `AgentExitsVehicleEvent` | Fires when an agent exits the boat |
| `SpawnedEvent` | Fires when the boat is spawned/respawned (returns the vehicle) |
| `DestroyedEvent` | Fires when the boat is eliminated |

---

### 🧠 Verse Example
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

vehicle_spawner_boat_example := class(creative_device):

    @editable
    BoatSpawner : vehicle_spawner_boat_device = vehicle_spawner_boat_device{}

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
        BoatSpawner.AgentEntersVehicleEvent.Subscribe(OnEnter)
        BoatSpawner.AgentExitsVehicleEvent.Subscribe(OnExit)
        BoatSpawner.SpawnedEvent.Subscribe(OnSpawn)
        BoatSpawner.DestroyedEvent.Subscribe(OnDestroyed)

        SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)
        DestroyButton.InteractedWithEvent.Subscribe(OnDestroyPressed)
        AssignDriverButton.InteractedWithEvent.Subscribe(OnAssignDriverPressed)
        EnableButton.InteractedWithEvent.Subscribe(OnEnable)
        DisableButton.InteractedWithEvent.Subscribe(OnDisable)

    OnEnter(Agent : agent) : void =
        Print("Agent entered Boat!")

    OnExit(Agent : agent) : void =
        Print("Agent exited Boat!")

    OnSpawn(Vehicle : fort_vehicle) : void =
        Print("Boat spawned!")

    OnDestroyed() : void =
        Print("Boat destroyed!")

    OnSpawnPressed(Agent : agent) : void =
        if (IsEnabled = true):
            BoatSpawner.RespawnVehicle()
            Print("Boat respawned via button.")

    OnDestroyPressed(Agent : agent) : void =
        if (IsEnabled = true):
            BoatSpawner.DestroyVehicle()
            Print("Boat destroyed via button.")

    OnAssignDriverPressed(Agent : agent) : void =
        if (IsEnabled = true):
            BoatSpawner.AssignDriver(Agent)
            Print("Agent assigned as Boat driver.")

    OnEnable(Agent : agent) : void =
        if (IsEnabled = false):
            set IsEnabled = true
            Print("Boat spawner enabled.")

    OnDisable(Agent : agent) : void =
        if (IsEnabled = true):
            set IsEnabled = false
            Print("Boat spawner disabled.")
```

---

### 📆 UEFN Step-by-Step Setup

#### 1. Place Devices in Your Level
- Add a `vehicle_spawner_boat_device` where the boat should appear.
- Place `button_device`s for spawn, destroy, assign driver, enable, and disable functionality as desired.

#### 2. Create the Verse Script
- In Verse Explorer: Right-click folder → **Create New Verse File** (e.g., `vehicle_spawner_boat_example.verse`)
- Choose **Create Empty** and paste the provided code example, then save.

#### 3. Build the Verse Code
- Click **Verse → Build Verse Code** (`Ctrl+Shift+B`) until you see “Build Succeeded”.

#### 4. Place and Reference the Verse Device
- Drag your Verse device from Content Browser into the world.
- In Details panel, assign:
  - `BoatSpawner` → your placed boat spawner device
  - `SpawnButton`, `DestroyButton`, `AssignDriverButton`, `EnableButton`, `DisableButton` → your placed buttons

#### 5. Configure the Boat Spawner
- Adjust respawn timer, access, appearance, and team/class settings in its Details panel.

#### 6. Test the Gameplay
- Press buttons in live mode to spawn, eliminate, assign driver, or enable/disable the boat.
- Watch log outputs to confirm event and control flow.

---

### 🧠 Tips
- Use multiple boat spawners for multi-boat setups.
- Control game logic or chain custom events via the provided event callbacks.
- `AssignDriver` requires a valid agent and a spawned boat.

---

### ❌ Troubleshooting
| Issue | Solution |
|-------|----------|
| Boat does not spawn | Ensure the spawner device is enabled and set up |
| `AssignDriver` fails | Confirm agent and spawned state are valid |
| No output logs | Check event subscriptions and device references |

---

### ✅ Note
Use the correct spawner for each Fortnite vehicle type. The device provides robust control both through settings and Verse APIs for dynamic, customizable gameplay experiences.

