## vehicle_spawner_sports_car_device – UEFN Verse Device Documentation

### 🔹 Description
The `vehicle_spawner_sports_car_device` is a specialized spawner that allows you to configure and spawn a Whiplash sports car in your Fortnite experience. It is based on `vehicle_spawner_device` and exposes all core vehicle spawner controls plus robust event handling for agents and vehicle lifecycle. This makes it straightforward to create races, rewards, or dynamic vehicle gameplay.

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `vehicle_spawner_device`
- `vehicle_spawner_sports_car_device`

### 🧩 Events (Data Members)
| Name | Type | When It Fires |
|------|------|----------------|
| `SpawnedEvent` | `listenable(fort_vehicle)` | When the Whiplash sports car is spawned or respawned. |
| `DestroyedEvent` | `listenable(tuple())` | When the sports car is destroyed. |
| `AgentEntersVehicleEvent` | `listenable(agent)` | When an agent enters the sports car. |
| `AgentExitsVehicleEvent` | `listenable(agent)` | When an agent exits the sports car. |
| `VehicleSpawnedEvent` | (deprecated) | Use `SpawnedEvent` instead. |
| `VehicleDestroyedEvent` | (deprecated) | Use `DestroyedEvent` instead. |

### 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| `Enable()` | Enables the car spawner for in-game use. |
| `Disable()` | Disables the car spawner (no new spawn until enabled again). |
| `RespawnVehicle()` | Spawns (or respawns, if already present) the Whiplash sports car. |
| `AssignDriver(agent)` | Assigns a specific agent as the vehicle's driver. |
| `DestroyVehicle()` | Destroys the spawned Whiplash sports car, if it exists. |
| `GetTransform()` | Returns the world transform of the spawner device. |
| `MoveTo()` / `TeleportTo()` | Move/animates or instantly moves the spawner/device. |

### 🎛 Configuration Options (Details Panel)
- **Vehicle to Spawn**: (Whiplash sports car, fixed for this device)
- **Enable at Game Start**: Start enabled/disabled.
- **Respawn Handling**: Timed/manual respawn, auto on destruction, etc.
- **Allowed Teams**: Restrict which teams can use spawned sports cars.
- **VFX/SFX Toggle**: Enable/disable effects for spawn/destroy events.
- **Simultaneous Vehicles**: Max count of cars that can be spawned concurrently.
- **Spawn Area/Volume**: Position or define area cars spawn in (for advanced use).

### 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

sports_car_spawner_example := class(creative_device):

    @editable
    SportsCarSpawner : vehicle_spawner_sports_car_device = vehicle_spawner_sports_car_device{}

    @editable
    SpawnButton : button_device = button_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        SportsCarSpawner.SpawnedEvent.Subscribe(OnVehicleSpawned)
        SportsCarSpawner.DestroyedEvent.Subscribe(OnVehicleDestroyed)
        SportsCarSpawner.AgentEntersVehicleEvent.Subscribe(OnAgentEntersVehicle)
        SportsCarSpawner.AgentExitsVehicleEvent.Subscribe(OnAgentExitsVehicle)

        SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnVehicleSpawned(Vehicle : fort_vehicle) : void =
        Print("Sports car spawned!")

    OnVehicleDestroyed() : void =
        Print("Sports car destroyed!")

    OnAgentEntersVehicle(Agent : agent) : void =
        Print("Agent entered sports car!")

    OnAgentExitsVehicle(Agent : agent) : void =
        Print("Agent exited sports car!")

    OnSpawnPressed(Agent : agent) : void =
        SportsCarSpawner.RespawnVehicle()
        Print("Sports car respawned!")

    OnEnablePressed(Agent : agent) : void =
        SportsCarSpawner.Enable()
        Print("Sports car spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        SportsCarSpawner.Disable()
        Print("Sports car spawner disabled!")
```

### ❌ Common Issues & Fixes
| Issue | ❌ Problem | ✅ Solution | Explanation |
|-------|-------------|----------------|-------------|
| Car not spawning | Forgot to call `.RespawnVehicle()` | Use button or logic to spawn | No car unless spawned explicitly |
| Players can't enter car | Wrong team or allowed settings | Adjust in Details panel | Teams/limit configs block access |
| Verse event logic not firing | Forgot to subscribe to events | Subscribe in `OnBegin<override>()` | Needed for event-driven logic |
| Device hasn't got ref set | Did not set @editable fields | Set in Verse Details after placing | Required for Verse to work |

### 🧠 Best Practices
- Subscribe to vehicle events for advanced logic (scoring, race checkpoints, elimination on exit, etc.).
- Enable/disable the spawner with game phase to control when vehicles are available.
- Use `.AssignDriver(agent)` to script who controls the car at spawn/restart.
- Carefully configure respawn count and allowed teams for fairness and balance.

### 📚 How to Use in UEFN
1. **Place Device in Level**: Drag a `vehicle_spawner_sports_car_device` into your island/level.
2. **Configure Options**: Set respawn, spawn limits, access teams, FX, and spawn area.
3. **Add Three Button Devices**: For "Spawn", "Enable", and "Disable" controls.
4. **Create and Place Your Verse Device**:
   - Use Verse Explorer → Create New Verse File.
   - Paste example code and build (Ctrl+Shift+B).
   - Drag Verse device into level.
5. **Assign `@editable` References**:
   - SportsCarSpawner → your placed spawner device.
   - SpawnButton, EnableButton, DisableButton → corresponding button devices.
6. **Test**: Play and press buttons to respawn, enable, or disable Whiplash cars.

> Use this spawner for races, time trials, elimination events, or progression systems—whenever you need dynamic and flexible Whiplash vehicle control in Fortnite UEFN.

