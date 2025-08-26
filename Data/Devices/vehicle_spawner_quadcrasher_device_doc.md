# Vehicle Spawner Quadcrasher Device – UEFN Verse Device Documentation

## 🔹 Description
The `vehicle_spawner_quadcrasher_device` is a specialized spawner that allows you to configure and spawn the **Quadcrasher** vehicle in your Fortnite experience. It inherits functionality from `vehicle_spawner_device`, enabling dynamic spawning, driver assignment, and event handling for player interactions. Use Verse to control its behavior such as enabling/disabling the spawner or monitoring vehicle events like entering/exiting.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `vehicle_spawner_device`
- `vehicle_spawner_quadcrasher_device`

## 🛠️ Functions & Methods
| Name              | Description                                                  |
|-------------------|--------------------------------------------------------------|
| `Enable()`        | Enables the spawner (active/visible)                         |
| `Disable()`       | Disables the spawner (inactive)                              |
| `RespawnVehicle()`| Spawns or respawns the Quadcrasher                           |
| `AssignDriver(agent)` | Sets the provided agent as driver                      |
| `DestroyVehicle()`| Destroys the current Quadcrasher if it exists                |
| `GetTransform()`  | Retrieves device's world transform                           |
| `MoveTo()` / `TeleportTo()` | Moves or teleports the device                    |

## 🥩 Events (Data Members)
| Name                        | Type                       | Description                                      |
|-----------------------------|----------------------------|--------------------------------------------------|
| `SpawnedEvent`             | `listenable(fort_vehicle)` | Fires when a Quadcrasher is spawned              |
| `DestroyedEvent`           | `listenable(tuple())`      | Fires when the Quadcrasher is destroyed          |
| `AgentEntersVehicleEvent`  | `listenable(agent)`        | Fires when an agent enters the vehicle           |
| `AgentExitsVehicleEvent`   | `listenable(agent)`        | Fires when an agent exits the vehicle            |
| `VehicleSpawnedEvent`      | *deprecated*               | Use `SpawnedEvent` instead                        |
| `VehicleDestroyedEvent`    | *deprecated*               | Use `DestroyedEvent` instead                      |

## 🎠 Configuration Options (Details Panel)
| Option                    | Description                                                   |
|---------------------------|---------------------------------------------------------------|
| Vehicle to Spawn          | Fixed to Quadcrasher                                           |
| Enable at Game Start      | Determines if spawner is active at game begin                  |
| Respawn Settings          | Set to auto-respawn on destroy, by timer, or manually          |
| Available Teams           | Restrict which teams can use the vehicle                       |
| Spawn Effects/FX          | Enable/disable VFX, SFX, and appearance effects                |
| Limit Per Team            | Max number of vehicles per team                                |
| Spawn Area/Volume         | Define the spawn volume or spawn area specifics                |
| Interaction               | Configure auto-entry and player vehicle control behaviors      |

## 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

quadcrasher_spawner_example := class(creative_device):

    @editable
    QuadSpawner : vehicle_spawner_quadcrasher_device = vehicle_spawner_quadcrasher_device{}

    @editable
    SpawnButton : button_device = button_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        QuadSpawner.SpawnedEvent.Subscribe(OnVehicleSpawned)
        QuadSpawner.DestroyedEvent.Subscribe(OnVehicleDestroyed)
        QuadSpawner.AgentEntersVehicleEvent.Subscribe(OnAgentEntersVehicle)
        QuadSpawner.AgentExitsVehicleEvent.Subscribe(OnAgentExitsVehicle)

        SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnVehicleSpawned(Vehicle : fort_vehicle) : void =
        Print("Quadcrasher spawned!")

    OnVehicleDestroyed() : void =
        Print("Quadcrasher destroyed!")

    OnAgentEntersVehicle(Agent : agent) : void =
        Print("Agent entered Quadcrasher!")

    OnAgentExitsVehicle(Agent : agent) : void =
        Print("Agent exited Quadcrasher!")

    OnSpawnPressed(Agent : agent) : void =
        QuadSpawner.RespawnVehicle()
        Print("Quadcrasher respawned!")

    OnEnablePressed(Agent : agent) : void =
        QuadSpawner.Enable()
        Print("Quadcrasher spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        QuadSpawner.Disable()
        Print("Quadcrasher spawner disabled!")
```

## 🔧 How to Use in UEFN
1. **Add the Device**
   - Drag a `vehicle_spawner_quadcrasher_device` into your level.
2. **Configure Spawner Options**
   - In the Details panel, set desired respawn rules, FX, team limits, etc.
3. **Place Button Devices**
   - Add three `button_device` actors to control spawning, enabling, and disabling.
4. **Create Verse File**
   - In Verse Explorer, right-click a folder → *Create New Verse File* (e.g., `quadcrasher_spawner_example.verse`)
   - Paste in the usage example code and save.
   - Build using Ctrl+Shift+B.
5. **Place Verse Device**
   - Drag your Verse class device into the world.
   - In its Details panel, link all references: `QuadSpawner`, `SpawnButton`, `EnableButton`, `DisableButton`.
6. **Test**
   - Enter play mode, press buttons to verify spawn/enable/disable actions.

## 🧠 Best Practices
- Use event listeners to drive gameplay logic when agents interact with vehicles.
- Dynamically enable or disable the spawner during game stages.
- Use `AssignDriver(agent)` to assign drivers programmatically for races or missions.

## ❌ Common Issues & Fixes
| Issue                     | ❌ Problem                            | ✅ Solution                        | Explanation                                           |
|---------------------------|------------------------------------------|----------------------------------------|-------------------------------------------------------|
| No vehicle appears        | Device not enabled or not spawned        | Use `Enable()` and `RespawnVehicle()`  | Spawner must be active and spawn called               |
| Not responding to players | Incorrect team config or bad placement   | Check team access and spawn volume     | Entry may be blocked by team rules or area collision  |
| Blank @editable values    | Device refs not assigned in Details panel| Assign all devices                     | Required for Verse runtime use                        |
| Events not triggering     | No event subscriptions in code           | Ensure OnBegin subscribes to events    | Subscriptions required for callbacks to trigger       |

## 🔹 Notes
- Spawning can be triggered via gameplay logic, triggers, or Verse code.
- Combine with volumes, rounds, or objectives for more dynamic experiences.
- Fully customizable with event-driven scripting.

