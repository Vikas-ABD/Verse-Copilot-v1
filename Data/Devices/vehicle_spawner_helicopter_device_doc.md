## vehicle_spawner_helicopter_device – UEFN Verse Device Documentation

### 📙 Description
The `vehicle_spawner_helicopter_device` is a specialized spawner for helicopters in Unreal Editor for Fortnite (UEFN). This device lets you spawn, configure, and control helicopters—perfect for aerial gameplay, objectives, traversal, or cinematic moments. You can programmatically enable/disable, respawn, destroy, and assign drivers or handle events with Verse, giving you powerful control for custom game modes.

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `vehicle_spawner_device`
- `vehicle_spawner_helicopter_device`

### 🛠️ Key Methods & Functions
| Method | Description |
|--------|-------------|
| `Enable()` | Enables the spawner device; vehicle appears if "Spawn on Enable" is set. |
| `Disable()` | Disables the spawner; can also eliminate vehicle if set. |
| `RespawnVehicle()` | Spawns a new helicopter, removing the old one if present. |
| `DestroyVehicle()` | Destroys the spawned helicopter immediately. |
| `AssignDriver(agent)` | Assigns an agent/player as the helicopter pilot. |
| `GetTransform()` | Gets the spawner’s position/rotation/scale. |
| `MoveTo()` / `TeleportTo()` | Moves or teleports the spawner (and its vehicle). |

### 🧹 Events (Data Members)
| Name | Type | When It Fires |
|------|------|----------------|
| `SpawnedEvent` | `listenable(fort_vehicle)` | When a helicopter is spawned or respawned |
| `DestroyedEvent` | `listenable(tuple())` | When the helicopter is eliminated |
| `AgentEntersVehicleEvent` | `listenable(agent)` | When an agent enters the helicopter |
| `AgentExitsVehicleEvent` | `listenable(agent)` | When an agent exits the helicopter |

### 🎯 Device Configuration (Details Panel)
- **Helicopter Cosmetic** – Paint, light, seating, handling, HP customization
- **Spawn When Enabled** – Whether helicopter appears when device is enabled
- **Destroy on Disable** – If on, eliminates vehicle when disabling device
- **Indestructible/HP** – Set max health or allow destruction settings
- **Can Be Damaged** – If checked, helicopter can be destroyed in gameplay

### 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

helicopter_vehicle_example := class(creative_device):

    @editable
    HelicopterSpawner : vehicle_spawner_helicopter_device = vehicle_spawner_helicopter_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    RespawnButton : button_device = button_device{}

    var CurrentVehicle : ?fort_vehicle = false

    OnBegin<override>()<suspends> : void =
        HelicopterSpawner.SpawnedEvent.Subscribe(OnVehicleSpawned)
        HelicopterSpawner.DestroyedEvent.Subscribe(OnVehicleDestroyed)
        HelicopterSpawner.AgentEntersVehicleEvent.Subscribe(OnAgentEntersVehicle)
        HelicopterSpawner.AgentExitsVehicleEvent.Subscribe(OnAgentExitsVehicle)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        RespawnButton.InteractedWithEvent.Subscribe(OnRespawnPressed)

    OnVehicleSpawned(Vehicle : fort_vehicle) : void =
        set CurrentVehicle = option{Vehicle}
        Print("Helicopter spawned!")

    OnVehicleDestroyed() : void =
        set CurrentVehicle = false
        Print("Helicopter destroyed!")

    OnAgentEntersVehicle(Agent : agent) : void =
        Print("Agent entered Helicopter!")

    OnAgentExitsVehicle(Agent : agent) : void =
        Print("Agent exited Helicopter!")

    OnEnablePressed(Agent : agent) : void =
        HelicopterSpawner.Enable()
        Print("Helicopter spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        HelicopterSpawner.Disable()
        Print("Helicopter spawner disabled!")

    OnRespawnPressed(Agent : agent) : void =
        HelicopterSpawner.RespawnVehicle()
        Print("Helicopter respawned!")
```

### How to Use in UEFN
1. **Place Devices in Your Level**
   - Drag in a `vehicle_spawner_helicopter_device`
   - Optionally add three `button_device` instances for Enable, Disable, Respawn

2. **Configure Helicopter in Details Panel**
   - Choose color, seats, handling, HP, and spawn/destroy rules

3. **Create and Add Your Verse Script**
   - In *Verse Explorer*, right-click a folder → Create New Verse File (e.g., `helicopter_vehicle_example.verse`)
   - Paste the code, save, and build the script (Ctrl+Shift+B)
   - Drag your Verse device into the world

4. **Assign @editable References**
   - Assign the helicopter device to `HelicopterSpawner`
   - Set each button field to your placed `button_device`

5. **Test Thoroughly In-Game**
   - Use buttons to control, check logs for event messages

### 🧠 Best Practices
- Use vehicle events to lock, eliminate, or assign drivers programmatically
- Combine with triggers, timers, volumes, or objectives for complex sequences (air drops, rescues, etc.)
- Customize HP, damage, appearance for unique mechanics or cinematic effects

### ❌ Common Issues & Fixes
| Issue | ❌ Problem | ✅ Solution |
|-------|---------------|----------------|
| Helicopter not spawning | Device not enabled or "Spawn When Enabled" is off | Call `.Enable()` or enable auto-spawn |
| No event output in Verse | Not subscribed in `OnBegin` | Ensure `.Subscribe(...)` is used |
| Reference errors in Verse | `@editable` values not set | Assign references in Details panel, then build |
| Immediate destroy on disable | "Destroy on Disable" is on | Adjust this setting in Details panel |

### Note
- All standard vehicle elimination, entry/exit, assignment, and cosmetic options are supported.
- Use Verse to script any logic for missions, sequences, scoring, or effects involving the helicopter.

