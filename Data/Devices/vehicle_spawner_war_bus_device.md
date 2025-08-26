# Vehicle Spawner War Bus Device Documentation (UEFN Verse)

## 🔹 Description

The `vehicle_spawner_war_bus_device` is a specialized vehicle spawner in Unreal Editor for Fortnite (UEFN). It provides advanced control for spawning and managing a War Bus vehicle. Features include player entry/exit detection, driver assignment, destruction tracking, and full Verse scripting integration for custom logic in PvPvE and mission-based gameplay.

## 🧱 Verse Using Statement

```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy

- `creative_object`
- `creative_device_base`
- `vehicle_spawner_device`
- `vehicle_spawner_war_bus_device`

## 🛠️ Key Methods & Functions

| Method                  | Description                                                 |
| ----------------------- | ----------------------------------------------------------- |
| `Enable()`              | Enables the spawner and allows the War Bus to spawn.        |
| `Disable()`             | Disables the spawner and eliminates any active War Bus.     |
| `RespawnVehicle()`      | Destroys the current War Bus (if any) and spawns a new one. |
| `DestroyVehicle()`      | Eliminates the spawned War Bus instantly, if present.       |
| `AssignDriver(agent)`   | Sets the specified agent/player as the War Bus's driver.    |
| `GetTransform()`        | Retrieves the spawner’s position, rotation, and scale.      |
| `MoveTo()/TeleportTo()` | Moves or teleports the spawner within the world.            |

## 🧹 Events (Data Members)

| Name                      | Type                       | Fires When                       |
| ------------------------- | -------------------------- | -------------------------------- |
| `SpawnedEvent`            | `listenable(fort_vehicle)` | War Bus is spawned or respawned. |
| `DestroyedEvent`          | `listenable(tuple())`      | War Bus is destroyed/eliminated. |
| `AgentEntersVehicleEvent` | `listenable(agent)`        | A player enters the War Bus.     |
| `AgentExitsVehicleEvent`  | `listenable(agent)`        | A player exits the War Bus.      |
| `VehicleDestroyedEvent`   | `listenable(tuple())`      |                                  |

| *Deprecated; use **`DestroyedEvent`**.* |                            |                                       |
| --------------------------------------- | -------------------------- | ------------------------------------- |
| `VehicleSpawnedEvent`                   | `listenable(fort_vehicle)` | *Deprecated; use **`SpawnedEvent`**.* |

## 🔹 Device Configuration (Details Panel)

- **Appearance/Setup**: Customize cosmetics, health, and other War Bus settings.
- **Auto Spawn**: Automatically spawn on device enable.
- **Destroy On Disable**: Auto-destroy War Bus when disabled.
- **Auto Respawn**: Automatically respawn after being destroyed.
- **Team/Class Restrictions**: Limit which players can enter or drive.

## 🔀 Example Verse Script

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

war_bus_example := class(creative_device):

    @editable
    WarBusSpawner : vehicle_spawner_war_bus_device = vehicle_spawner_war_bus_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    RespawnButton : button_device = button_device{}

    var CurrentBus : ?fort_vehicle = false

    OnBegin<override>()<suspends> : void =
        WarBusSpawner.SpawnedEvent.Subscribe(OnBusSpawned)
        WarBusSpawner.DestroyedEvent.Subscribe(OnBusDestroyed)
        WarBusSpawner.AgentEntersVehicleEvent.Subscribe(OnAgentEntersBus)
        WarBusSpawner.AgentExitsVehicleEvent.Subscribe(OnAgentExitsBus)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        RespawnButton.InteractedWithEvent.Subscribe(OnRespawnPressed)

    OnBusSpawned(Bus : fort_vehicle) : void =
        set CurrentBus = option{Bus}
        Print("War Bus spawned!")

    OnBusDestroyed() : void =
        set CurrentBus = false
        Print("War Bus destroyed!")

    OnAgentEntersBus(Agent : agent) : void =
        Print("Agent entered War Bus!")

    OnAgentExitsBus(Agent : agent) : void =
        Print("Agent exited War Bus!")

    OnEnablePressed(Agent : agent) : void =
        WarBusSpawner.Enable()
        Print("War Bus spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        WarBusSpawner.Disable()
        Print("War Bus spawner disabled!")

    OnRespawnPressed(Agent : agent) : void =
        WarBusSpawner.RespawnVehicle()
        Print("War Bus respawned!")
```

## 🧠 Best Practices

- Use `AgentEntersVehicleEvent` and `AgentExitsVehicleEvent` for gameplay reactions.
- Use `RespawnVehicle()` between rounds for War Bus resets.
- Apply team/class filters to control access for competitive or cooperative modes.

## ❌ Common Issues & Fixes

| Problem                     | Likely Reason                         | Solution                                              |
| --------------------------- | ------------------------------------- | ----------------------------------------------------- |
| War Bus doesn’t spawn       | Not enabled or "Auto Spawn" unchecked | Call `.Enable()` or check Auto Spawn in Details Panel |
| Event handler not triggered | Not subscribed in Verse code          | Ensure `.Subscribe(...)` is correctly set up          |
| Reference error             | Missing @editable field assignment    | Assign devices via Details panel                      |

## 📅 How to Use in UEFN

1. **Place Devices in Your Level**
   - Add `vehicle_spawner_war_bus_device` from the Devices menu.
   - Add three `button_device` actors for control.
2. **Configure Details Panel**
   - Set team filters, visuals, auto-spawn, etc.
3. **Create Verse Script**
   - Open *Verse Explorer* > Create Verse File (e.g., `war_bus_example.verse`).
   - Paste script, build (`Ctrl+Shift+B`), and save.
   - Drag your custom Verse device into the world.
4. **Test & Expand**
   - Playtest using buttons.
   - Add scoring, triggers, cinematic sequences in events.

## 🔍 Notes

- Use `.AssignDriver(agent)` to force driver assignment during cutscenes or scripted gameplay.
- Replace `Print()` with game logic (e.g., elimination logic, phase progression, scoring).
- The War Bus can be fully managed via Verse for complex game scenarios.

