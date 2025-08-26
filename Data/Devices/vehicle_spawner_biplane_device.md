**UEFN: vehicle_spawner_biplane_device - Complete Setup & Reference Guide**

---

### 🔹 Description
The `vehicle_spawner_biplane_device` is a specialized vehicle spawner for the Stormwing Biplane. It enables spawning, controlling, and managing the biplane using device settings or Verse scripting. You can use Verse to handle spawning, elimination, driver assignment, enabling/disabling, and vehicle event responses.

---

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
```
creative_object
└ creative_device_base
   └ vehicle_spawner_device
      └ vehicle_spawner_biplane_device
```

---

### 🛠️ Key Methods & Events
| Name | Description |
|------|-------------|
| `Enable()`, `Disable()` | Enables or disables the spawner device |
| `RespawnVehicle()` | Spawns a new Stormwing Biplane (removes the previous one) |
| `DestroyVehicle()` | Immediately eliminates the spawned biplane |
| `AssignDriver(agent)` | Assigns the specified agent as the pilot |
| `AgentEntersVehicleEvent` | Fires when an agent enters the biplane |
| `AgentExitsVehicleEvent` | Fires when an agent exits the biplane |
| `SpawnedEvent` | Fires when the biplane is spawned or respawned |
| `DestroyedEvent` | Fires when the biplane is destroyed |

---

### 🪠 Verse Example: Manual Biplane Control and Event Handling
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

vehicle_spawner_biplane_example := class(creative_device):

    @editable
    BiplaneSpawner : vehicle_spawner_biplane_device = vehicle_spawner_biplane_device{}

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
        BiplaneSpawner.AgentEntersVehicleEvent.Subscribe(OnEnter)
        BiplaneSpawner.AgentExitsVehicleEvent.Subscribe(OnExit)
        BiplaneSpawner.SpawnedEvent.Subscribe(OnSpawn)
        BiplaneSpawner.DestroyedEvent.Subscribe(OnDestroyed)

        SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)
        DestroyButton.InteractedWithEvent.Subscribe(OnDestroyPressed)
        AssignDriverButton.InteractedWithEvent.Subscribe(OnAssignDriverPressed)
        EnableButton.InteractedWithEvent.Subscribe(OnEnable)
        DisableButton.InteractedWithEvent.Subscribe(OnDisable)

    OnEnter(Agent : agent) : void =
        Print("Agent entered Biplane!")

    OnExit(Agent : agent) : void =
        Print("Agent exited Biplane!")

    OnSpawn(Vehicle : fort_vehicle) : void =
        Print("Biplane spawned!")

    OnDestroyed() : void =
        Print("Biplane destroyed!")

    OnSpawnPressed(Agent : agent) : void =
        if (IsEnabled = true):
            BiplaneSpawner.RespawnVehicle()
            Print("Biplane respawned via button.")

    OnDestroyPressed(Agent : agent) : void =
        if (IsEnabled = true):
            BiplaneSpawner.DestroyVehicle()
            Print("Biplane destroyed via button.")

    OnAssignDriverPressed(Agent : agent) : void =
        if (IsEnabled = true):
            BiplaneSpawner.AssignDriver(Agent)
            Print("Agent assigned as Biplane driver.")

    OnEnable(Agent : agent) : void =
        if (IsEnabled = false):
            set IsEnabled = true
            Print("Biplane spawner enabled.")

    OnDisable(Agent : agent) : void =
        if (IsEnabled = true):
            set IsEnabled = false
            Print("Biplane spawner disabled.")
```

---

### 📅 UEFN Setup Instructions

#### 1. Place Devices in Your Level
- Add a `vehicle_spawner_biplane_device` to your level.
- (Optional) Add button devices for spawn, destroy, assign driver, enable, and disable.

#### 2. Create and Build the Verse Script
- In Verse Explorer: Right-click a folder → **Create New Verse File** (e.g. `vehicle_spawner_biplane_example.verse`)
- Select **Create Empty** and paste the sample code above
- Save, then go to **Verse → Build Verse Code** (or Ctrl+Shift+B)

#### 3. Place and Assign Devices
- Drag your Verse device into the world
- In the Details panel, assign:
  - `BiplaneSpawner` → your biplane spawner device
  - `SpawnButton`, `DestroyButton`, etc. → the respective button devices

#### 4. Customize the Biplane Spawner
- Adjust respawn settings, access controls, team/class filters, and biplane-specific settings in its Details panel

#### 5. Test
- Launch a play session
- Interact with buttons to test spawn/elimination, driver assignment, enable/disable
- Watch the output log for events and messages

---

### 🧠 Tips
- Use multiple spawners for multiple biplanes
- Trigger gameplay logic (scoring, HUD, effects) from event callbacks
- `AssignDriver` only works when the biplane is actively spawned

---

### ❌ Troubleshooting
| Issue | Solution |
|-------|----------|
| Biplane doesn’t spawn | Ensure the device is enabled and placed correctly |
| AssignDriver fails | Verify agent is valid and the biplane is spawned |
| No event logging | Check event subscriptions and assigned references |

---

### ⚠️ Note
- Always use the correct vehicle-specific spawner
- Full biplane lifecycle (spawn, destroy, enable, assign driver) can be handled through Verse or the Details panel

