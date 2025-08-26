# Vehicle Spawner Armored Battle Bus Device – UEFN Verse Device Documentation

## 📙 Description
The `vehicle_spawner_armored_battle_bus_device` is a specialized spawner for the **Armored Battle Bus** vehicle in **Unreal Editor for Fortnite (UEFN)**. This device allows for full control of the Armored Battle Bus via Verse scripting or device wiring. Ideal for:
- Large-scale combat
- Boss events
- Convoy missions
- Escort and interaction objectives with a powerful vehicle on your island

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `vehicle_spawner_device`
- `vehicle_spawner_armored_battle_bus_device`

## 🛠️ Key Functions & Methods
| Method | Description |
|--------|-------------|
| `Enable()` | Enables the spawner device (spawns vehicle if "Spawn on Enable" is set) |
| `Disable()` | Disables the spawner and optionally eliminates the vehicle |
| `RespawnVehicle()` | Spawns a new Battle Bus (destroys previous if one exists) |
| `DestroyVehicle()` | Immediately destroys the spawned Battle Bus |
| `AssignDriver(agent)` | Assigns a driver to the spawned Battle Bus |
| `GetTransform()` | Retrieves the world transform of the spawner |
| `MoveTo()/TeleportTo()` | Changes the spawner’s world position/rotation |

## 🧹 Events (Data Members)
| Name | Type | Trigger |
|------|------|---------|
| `SpawnedEvent` | `listenable(fort_vehicle)` | Fires when a vehicle is spawned or respawned |
| `DestroyedEvent` | `listenable(tuple())` | Fires when the Battle Bus is eliminated |
| `AgentEntersVehicleEvent` | `listenable(agent)` | Fires when an agent enters the vehicle |
| `AgentExitsVehicleEvent` | `listenable(agent)` | Fires when an agent exits the vehicle |

## 🎯 Device Configuration (Details Panel)
- **Vehicle Customization:** Adjust colors, weapons, health, handling
- **Spawn on Enable:** Automatically spawns vehicle when enabled
- **Destroy on Disable:** Eliminates vehicle when disabled
- **Health/Indestructibility:** Set max HP, enable/disable destruction
- **Player Damage:** Customize how bus interacts with players
- **Gameplay Functions:** Toggle skills, movement, and interaction

## 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

battle_bus_example := class(creative_device):

    @editable
    BattleBusSpawner : vehicle_spawner_armored_battle_bus_device = vehicle_spawner_armored_battle_bus_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    RespawnButton : button_device = button_device{}

    var CurrentVehicle : ?fort_vehicle = false

    OnBegin<override>()<suspends> : void =
        BattleBusSpawner.SpawnedEvent.Subscribe(OnVehicleSpawned)
        BattleBusSpawner.DestroyedEvent.Subscribe(OnVehicleDestroyed)
        BattleBusSpawner.AgentEntersVehicleEvent.Subscribe(OnAgentEntersVehicle)
        BattleBusSpawner.AgentExitsVehicleEvent.Subscribe(OnAgentExitsVehicle)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        RespawnButton.InteractedWithEvent.Subscribe(OnRespawnPressed)

    OnVehicleSpawned(Vehicle : fort_vehicle) : void =
        set CurrentVehicle = option{Vehicle}
        Print("Battle Bus spawned!")

    OnVehicleDestroyed() : void =
        set CurrentVehicle = false
        Print("Battle Bus destroyed!")

    OnAgentEntersVehicle(Agent : agent) : void =
        Print("Agent entered Battle Bus!")

    OnAgentExitsVehicle(Agent : agent) : void =
        Print("Agent exited Battle Bus!")

    OnEnablePressed(Agent : agent) : void =
        BattleBusSpawner.Enable()
        Print("Battle Bus spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        BattleBusSpawner.Disable()
        Print("Battle Bus spawner disabled!")

    OnRespawnPressed(Agent : agent) : void =
        BattleBusSpawner.RespawnVehicle()
        Print("Battle Bus respawned!")

    AssignDriver(Agent : agent) : void =
        if (Vehicle := CurrentVehicle?):
            Print("Driver assigned to Battle Bus")

    RemoveDriver(Agent : agent) : void =
        if (Vehicle := CurrentVehicle?):
            Print("Driver removed from Battle Bus")
```

## 📆 How to Use in UEFN
1. **Place Devices in Level**
   - Place `vehicle_spawner_armored_battle_bus_device`
   - Place 3 `button_device` (Enable, Disable, Respawn)

2. **Configure Battle Bus**
   - Customize weapons, health, destruction behavior in the Details panel
   - Enable "Spawn on Enable" if needed

3. **Create & Connect Verse Device**
   - Create new Verse file (e.g., `battle_bus_example.verse`)
   - Paste code and build (Ctrl+Shift+B)
   - Place the Verse device in the world

4. **Assign @editable References**
   - Link `BattleBusSpawner`, `EnableButton`, `DisableButton`, and `RespawnButton` in the Verse device's Details panel

5. **Test**
   - Playtest to observe spawn/destruction/interaction logs and behaviors

## 🧠 Best Practices
- Use `SpawnedEvent` and `DestroyedEvent` to manage score, objectives, or round flow
- Combine device settings with Verse logic for dynamic gameplay
- Use `AssignDriver(agent)` during objectives, respawn, or round start

## ❌ Common Issues & Fixes
| Issue | ❌ Problem | ✅ Solution |
|-------|---------------|----------------|
| Bus not spawning | Spawner not enabled or "Spawn on Enable" off | Use `.Enable()` or enable setting in Details panel |
| Players can't drive | No driver assigned | Call `.AssignDriver(agent)` in logic |
| No destruction logic | Events not handled | Use `DestroyedEvent` or `.DestroyVehicle()` |
| Verse code not working | References unset or code not built | Assign in Details & build (Ctrl+Shift+B) |

---

**Note:** Vehicle customization (weapons, HP, etc.) is handled via the Details panel. Use Verse to control logic: spawn, destroy, and manage vehicle interactions.

Perfect for boss fights, rally scenarios, convoy protection missions, or player-vs-vehicle battles.

