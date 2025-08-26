# 📘 Vehicle Spawner Armored Transport Device – UEFN Verse Device Documentation

## 🔹 Description
The `vehicle_spawner_armored_transport_device` is a specialized vehicle spawner in Unreal Editor for Fortnite (UEFN) designed for spawning and managing an **Armored Transport** (e.g., armored truck). It supports scripting vehicle behavior, assignment, and event reactions in Verse, enabling dynamic mission or objective design.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `vehicle_spawner_device`
- `vehicle_spawner_armored_transport_device`

## 🛠️ Key Methods & Functions
| Method | Description |
|--------|-------------|
| `Enable()` | Enables the spawner to allow vehicle spawning. |
| `Disable()` | Disables the spawner and destroys any active vehicle. |
| `RespawnVehicle()` | Destroys the current vehicle and spawns a new one. |
| `DestroyVehicle()` | Immediately destroys the active vehicle. |
| `AssignDriver(agent)` | Assigns a player as the vehicle driver. |
| `GetTransform()` | Gets the world transform of the spawner. |
| `MoveTo()` / `TeleportTo()` | Moves or teleports the spawner in world space. |

## 🧍 Events (Data Members)
| Name | Type | Fires When |
|------|------|------------|
| `SpawnedEvent` | `listenable(fort_vehicle)` | When a vehicle is spawned. |
| `DestroyedEvent` | `listenable(tuple())` | When the vehicle is destroyed. |
| `AgentEntersVehicleEvent` | `listenable(agent)` | When a player enters the vehicle. |
| `AgentExitsVehicleEvent` | `listenable(agent)` | When a player exits the vehicle. |
| `VehicleSpawnedEvent` | `listenable(fort_vehicle)` | **Deprecated**; use `SpawnedEvent`. |
| `VehicleDestroyedEvent` | `listenable(tuple())` | **Deprecated**; use `DestroyedEvent`. |

## 🎛 Device Configuration (Details Panel)
- **Enabled During Phase**: Choose which phases the spawner is active.
- **Respawn On Elimination**: Automatically respawns when destroyed.
- **Respawn Delay**: Seconds to wait before respawning.
- **Destroy Vehicle When Disabled**: Eliminates the vehicle if the device is disabled.
- **Activating Team/Class**: Limits interaction to specific agents/teams.
- Other armored transport-specific options.

## 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

armored_transport_example := class(creative_device):

    @editable
    VehicleSpawner : vehicle_spawner_armored_transport_device = vehicle_spawner_armored_transport_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    RespawnButton : button_device = button_device{}

    var CurrentVehicle : ?fort_vehicle = false

    OnBegin<override>()<suspends> : void =
        VehicleSpawner.SpawnedEvent.Subscribe(OnVehicleSpawned)
        VehicleSpawner.DestroyedEvent.Subscribe(OnVehicleDestroyed)
        VehicleSpawner.AgentEntersVehicleEvent.Subscribe(OnAgentEntersVehicle)
        VehicleSpawner.AgentExitsVehicleEvent.Subscribe(OnAgentExitsVehicle)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        RespawnButton.InteractedWithEvent.Subscribe(OnRespawnPressed)

    OnVehicleSpawned(Vehicle : fort_vehicle) : void =
        set CurrentVehicle = option{Vehicle}
        Print("Armored transport vehicle spawned!")

    OnVehicleDestroyed() : void =
        set CurrentVehicle = false
        Print("Armored transport vehicle destroyed!")

    OnAgentEntersVehicle(Agent : agent) : void =
        Print("Agent entered armored transport vehicle!")

    OnAgentExitsVehicle(Agent : agent) : void =
        Print("Agent exited armored transport vehicle!")

    OnEnablePressed(Agent : agent) : void =
        VehicleSpawner.Enable()
        Print("Armored transport vehicle spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        VehicleSpawner.Disable()
        Print("Armored transport vehicle spawner disabled!")

    OnRespawnPressed(Agent : agent) : void =
        VehicleSpawner.RespawnVehicle()
        Print("Armored transport vehicle respawned!")
```

## 🔎 Explanation
- **VehicleSpawner**: Reference to the armored transport spawner.
- **Enable/Disable/RespawnButton**: Button devices hooked to Verse events.
- **Event Hooks**: Connect to spawn, destroy, entry, and exit events.
- **Print Statements**: Used for debugging; can be replaced with gameplay logic (triggers, rewards, objectives).

## ⚡ How to Use in UEFN
1. **Place Devices**
   - Add `vehicle_spawner_armored_transport_device` in the level.
   - Add 3 `button_device` actors for control.

2. **Configure Details Panel**
   - Set activation phases, respawn settings, team/class restrictions, etc.

3. **Create & Add Verse Script**
   - Open **Verse Explorer**.
   - Create a new Verse file (e.g., `armored_transport_example.verse`).
   - Paste code, save, then **Build** (Ctrl+Shift+B).
   - Assign @editable references in the Details Panel.

4. **Test & Extend**
   - Run the level. Use buttons or triggers to control the vehicle.
   - Customize events for cinematic, scoring, or mission logic.

## 🧠 Best Practices
- Use for escort, capture, defense missions.
- Combine with respawn logic for rounds or waves.
- Trigger progression, effects, or rewards on `AgentEntersVehicleEvent` or `DestroyedEvent`.

## ❌ Common Issues & Fixes
| Problem | Likely Reason | Solution |
|--------|----------------|----------|
| Vehicle won’t spawn | Not enabled or wrong phase | Use `.Enable()`, check phase settings |
| Events not triggered | Not subscribed in Verse | Add event subscriptions in `OnBegin()` |
| No reference in Verse panel | Missing assignments | Set all `@editable` fields in Details Panel |

## ℹ️ Notes
- Replace `Print()` with your own gameplay effects.
- Use `SpawnedEvent` or `DestroyedEvent` to drive delivery or checkpoint mechanics.

