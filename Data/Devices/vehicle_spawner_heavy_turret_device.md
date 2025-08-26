# vehicle_spawner_heavy_turret_device – UEFN Verse Device Documentation

## 🔹 Description
The `vehicle_spawner_heavy_turret_device` is a specialized spawner that creates and manages an **anti-vehicle turret** in Unreal Editor for Fortnite (UEFN). You can configure the turret’s settings and use Verse or device wiring to enable, disable, respawn, assign drivers, or interact with all turret control and entry events—ideal for base defense, convoy/escort, or interactive objective gameplay.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `vehicle_spawner_device`
- `vehicle_spawner_heavy_turret_device`

## 🛠️ Key Methods & Functions
| Method | Description |
|--------|-------------|
| `Enable()` | Enables the turret spawner device (turret can appear). |
| `Disable()` | Disables the device (and can eliminate the turret if configured). |
| `RespawnVehicle()` | Spawns a new turret (destroys previous one). |
| `DestroyVehicle()` | Eliminates the spawned turret instantly. |
| `AssignDriver(agent)` | Assigns an agent/player as turret gunner/driver. |
| `GetTransform()` | Gets the spawner’s current world transform. |
| `MoveTo()` / `TeleportTo()` | Changes the spawner’s (and its turret) position/rotation. |

## 🧹 Events (Data Members)
| Name | Type | When It Fires |
|------|------|---------------|
| `SpawnedEvent` | `listenable(fort_vehicle)` | When a turret is spawned or respawned |
| `DestroyedEvent` | `listenable(tuple())` | When the turret is destroyed/eliminated |
| `AgentEntersVehicleEvent` | `listenable(agent)` | When an agent enters and mounts the turret |
| `AgentExitsVehicleEvent` | `listenable(agent)` | When an agent dismounts the turret |

## 🎛 Device Configuration (Details Panel)
- **Turret Appearance**: Base mesh, color, weapon cosmetics
- **Spawn When Enabled**: Turret appears as soon as device is enabled
- **Destroy on Disable**: Turret eliminated when disabling device
- **Indestructible/HP**: Set turret HP, invulnerability, destruction behavior
- **Driver/Use Settings**: Who can mount/control; class/team, limits, permissions

## 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

heavy_turret_example := class(creative_device):

    @editable
    TurretSpawner : vehicle_spawner_heavy_turret_device = vehicle_spawner_heavy_turret_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    RespawnButton : button_device = button_device{}

    var CurrentVehicle : ?fort_vehicle = false

    OnBegin<override>()<suspends> : void =
        # Subscribe to vehicle events
        TurretSpawner.SpawnedEvent.Subscribe(OnVehicleSpawned)
        TurretSpawner.DestroyedEvent.Subscribe(OnVehicleDestroyed)
        TurretSpawner.AgentEntersVehicleEvent.Subscribe(OnAgentEntersVehicle)
        TurretSpawner.AgentExitsVehicleEvent.Subscribe(OnAgentExitsVehicle)

        # Subscribe to control buttons
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        RespawnButton.InteractedWithEvent.Subscribe(OnRespawnPressed)

    # Event handlers
    OnVehicleSpawned(Vehicle : fort_vehicle) : void =
        set CurrentVehicle = option{Vehicle}
        Print("Heavy Turret spawned!")

    OnVehicleDestroyed() : void =
        set CurrentVehicle = false
        Print("Heavy Turret destroyed!")

    OnAgentEntersVehicle(Agent : agent) : void =
        Print("Agent entered Heavy Turret!")

    OnAgentExitsVehicle(Agent : agent) : void =
        Print("Agent exited Heavy Turret!")

    # Button control handlers
    OnEnablePressed(Agent : agent) : void =
        TurretSpawner.Enable()
        Print("Heavy Turret spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        TurretSpawner.Disable()
        Print("Heavy Turret spawner disabled!")

    OnRespawnPressed(Agent : agent) : void =
        TurretSpawner.RespawnVehicle()
        Print("Heavy Turret respawned!")
```

### Explanation
- **TurretSpawner**: Reference to your placed `vehicle_spawner_heavy_turret_device`.
- **Enable/Disable/RespawnButton**: Button devices for manual control.
- **Event Subscriptions**: Hook into spawn, destruction, and player entry/exit.
- **AssignDriver**: Can be called to force a player into turret control.

## 🔧 How to Use in UEFN
1. **Place Devices in Your Level**
   - Add a `vehicle_spawner_heavy_turret_device`.
   - Place three `button_device` instances.

2. **Configure in Details Panel**
   - Set appearance, HP, driver/team/class permissions.
   - Enable "Spawn When Enabled" and "Destroy on Disable" if needed.

3. **Create & Add the Verse Device**
   - Open **Verse Explorer** → Right-click folder → Create New Verse File (e.g., `heavy_turret_example.verse`).
   - Paste the provided code and build (Ctrl+Shift+B).
   - Place your Verse device in the level.

4. **Assign Editable References**
   - Set `TurretSpawner`, `EnableButton`, `DisableButton`, `RespawnButton` in your Verse device’s Details panel.

5. **Test & Play**
   - Run a session and trigger your buttons. Check logs for confirmation messages.

## 🧠 Best Practices
- Always subscribe to turret events for game logic like scoring or objectives.
- Use Enable/Disable for dynamic or wave-based encounters.
- Use `AssignDriver` for scripted sequences or player control.
- Combine with triggers, zones, and stat counters for custom logic.

## ❌ Common Issues & Fixes
| Issue | ❌ Problem | ✅ Solution |
|-------|----------------|----------------|
| Turret not spawning | Not enabled or option off | Call `.Enable()`; ensure "Spawn When Enabled" is set |
| No event output | Events not subscribed | Use `Subscribe()` in `OnBegin` as shown |
| Reference not working | `@editable` not set or assigned | Mark editable and assign in Details panel |
| Elimination logic missing | `DestroyVehicle()` not called | Handle in `.DestroyedEvent` or script manually |

### Notes
- Use device settings for base behavior and Verse for advanced scripting.
- Ideal for base defense, PvP/PvE objectives, or convoy protection.
- Mix and match with other devices for highly dynamic gameplay setups.

