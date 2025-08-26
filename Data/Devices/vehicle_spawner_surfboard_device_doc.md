## vehicle_spawner_surfboard_device – UEFN Verse Device Documentation

### 🔹 Description
The `vehicle_spawner_surfboard_device` is a specialized spawner that allows you to configure and spawn surfboard vehicles in Fortnite. It inherits all base vehicle spawner behaviors, enabling dynamic spawning, enabling/disabling the spawner, and tracking player interaction events (enter/exit) from Verse scripts. Ideal for surfing minigames, speed challenges, or custom traversal mechanics.

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `vehicle_spawner_device`
- `vehicle_spawner_surfboard_device`

### 🛠️ Functions & Methods
| Name                 | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `Enable()`           | Enables the device for use.                                                 |
| `Disable()`          | Disables the device; cannot be used until enabled again.                    |
| `RespawnVehicle()`   | Destroys any existing surfboard spawned and creates a new one.              |
| `AssignDriver(agent)`| Instantly assigns the given agent as the driver of the surfboard.           |
| `DestroyVehicle()`   | Destroys the current surfboard (if present).                                |
| `GetTransform()`     | Gets current device transform (position, rotation, scale).                  |
| `MoveTo()` / `TeleportTo()` | Animate or teleport the spawner to a new location.              |

### 🧩 Events (Data Members)
| Name                          | Type                       | Description                                   |
|-------------------------------|----------------------------|-----------------------------------------------|
| `SpawnedEvent`               | `listenable(fort_vehicle)` | Fires when the surfboard is spawned.          |
| `DestroyedEvent`             | `listenable(tuple())`      | Fires when the surfboard is destroyed.        |
| `AgentEntersVehicleEvent`    | `listenable(agent)`        | Fires when an agent gets on the surfboard.    |
| `AgentExitsVehicleEvent`     | `listenable(agent)`        | Fires when an agent gets off the surfboard.   |
| *(Deprecated)* `VehicleSpawnedEvent` / `VehicleDestroyedEvent` | Use updated events instead. |

### 🎛 Configuration Options (Details Panel)
- **Vehicle to Spawn**: Surfboard (fixed)
- **Enable at Game Start**: Whether the spawner device is enabled automatically.
- **Spawn Handling**: Auto, timed, or manual respawn on destroy/after cooldown.
- **Allowed Teams**: Restrict which teams can spawn/use the vehicle.
- **Effects/Visibility**: Toggle VFX and SFX for spawn/destruction, adjust visuals.
- **Maximum Vehicles**: Max count of active surfboards spawned at once.
- **Spawn Region/Volume**: Define optional spawn area.

### 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

surfboard_spawner_example := class(creative_device):

    @editable
    SurfboardSpawner : vehicle_spawner_surfboard_device = vehicle_spawner_surfboard_device{}

    @editable
    SpawnButton : button_device = button_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        SurfboardSpawner.SpawnedEvent.Subscribe(OnVehicleSpawned)
        SurfboardSpawner.DestroyedEvent.Subscribe(OnVehicleDestroyed)
        SurfboardSpawner.AgentEntersVehicleEvent.Subscribe(OnAgentEntersVehicle)
        SurfboardSpawner.AgentExitsVehicleEvent.Subscribe(OnAgentExitsVehicle)

        SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnVehicleSpawned(Vehicle : fort_vehicle) : void =
        Print("Surfboard spawned!")

    OnVehicleDestroyed() : void =
        Print("Surfboard destroyed!")

    OnAgentEntersVehicle(Agent : agent) : void =
        Print("Agent entered surfboard!")

    OnAgentExitsVehicle(Agent : agent) : void =
        Print("Agent exited surfboard!")

    OnSpawnPressed(Agent : agent) : void =
        SurfboardSpawner.RespawnVehicle()
        Print("Surfboard respawned!")

    OnEnablePressed(Agent : agent) : void =
        SurfboardSpawner.Enable()
        Print("Surfboard spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        SurfboardSpawner.Disable()
        Print("Surfboard spawner disabled!")
```

### 🧪 How to Use in UEFN
1. **Add Devices to Your Level**
    - Drag `vehicle_spawner_surfboard_device` into your world.
    - Add three `button_device`s for spawn, enable, and disable actions.

2. **Configure Device Options (Details Panel)**
    - Set spawn method, allowed teams, max vehicles, VFX/SFX, etc.

3. **Create and Place Verse Script**
    - Right-click a folder in Verse Explorer → Create New Verse File.
    - Name it `surfboard_spawner_example.verse`, paste the above code.
    - Build (Ctrl+Shift+B) until "Build Succeeded" appears.
    - Drag the compiled Verse device into your level.

4. **Set @editable References**
    - Assign SurfboardSpawner, SpawnButton, EnableButton, and DisableButton in the Verse device’s Details panel.

5. **Test In-Game**
    - Enter play mode.
    - Interact with buttons to trigger spawner functionality.
    - Observe printed debug messages for event tracking.

### 🧠 Best Practices
- Use all available events to trigger rewards, quests, or effects.
- Control gameplay phases dynamically by enabling/disabling spawner.
- Utilize `AssignDriver()` for puzzles, challenges, or assigning surfboards to specific players.
- Configure team settings and spawn caps for fairness and gameplay balance.

### ❌ Common Issues & Fixes
| Issue                     | ❌ Example                       | ✅ Solution                                 | Explanation                                           |
|--------------------------|----------------------------------|---------------------------------------------|-------------------------------------------------------|
| Surfboard never spawns   | Didn’t call `.RespawnVehicle()` | Use a button, trigger, or script to respawn | Spawner must be active to produce vehicle            |
| No Verse event output    | Forgot to `.Subscribe()`         | Subscribe in `OnBegin()`                    | Events won’t fire without a handler                   |
| @editable refs unset     | Unassigned in Details panel      | Set refs in Verse device Details panel      | Required for Verse to access linked devices          |
| Players can’t ride       | Incorrect team/restrictions      | Fix allowed teams and vehicle count         | Access controlled in the spawner’s Details panel     |

### 🏁 Summary
The `vehicle_spawner_surfboard_device` gives creators full control over surfboard gameplay. Combine with buttons and Verse logic for real-time interaction, dynamic flow control, and enhanced creative gameplay experiences in Fortnite.

