📘 Vehicle Spawner Rocket Racing Device – UEFN Verse Device Documentation

🔹 Description The `vehicle_spawner_rocketracing_device` is a specialized vehicle spawner in Unreal Editor for Fortnite (UEFN) that enables spawning and configuration of a Rocket Racing Vehicle. This high-performance vehicle supports advanced boosting, jumping, sticky wheels for wall/ceiling traversal, and is ideal for creating custom racing gameplay. All controls and gameplay events are exposed to Verse, enabling fine-tuned mission, time attack, or platformer-level logic.

🧱 Verse Using Statement

```verse
using { /Fortnite.com/Devices }
```

🔗 Inheritance Hierarchy

- creative\_object
- creative\_device\_base
- vehicle\_spawner\_device
- vehicle\_spawner\_rocketracing\_device

🛠️ Key Methods & Functions

| Method                | Description                                                  |
| --------------------- | ------------------------------------------------------------ |
| Enable()              | Enables the spawner to allow Rocket Racing Vehicle spawning. |
| Disable()             | Disables the spawner and eliminates any active vehicle.      |
| RespawnVehicle()      | Eliminates current vehicle and spawns a new one.             |
| DestroyVehicle()      | Eliminates the spawned vehicle, if any.                      |
| AssignDriver(agent)   | Assigns a player agent as the driver of the vehicle.         |
| GetTransform()        | Retrieves the world position/rotation/scale of the spawner.  |
| MoveTo()/TeleportTo() | Moves or teleports the spawner device in the world.          |

🧰 Events (Data Members)

| Name                    | Type                      | Fires When...                            |
| ----------------------- | ------------------------- | ---------------------------------------- |
| SpawnedEvent            | listenable(fort\_vehicle) | Vehicle is spawned or respawned.         |
| DestroyedEvent          | listenable(tuple())       | Vehicle is destroyed.                    |
| AgentEntersVehicleEvent | listenable(agent)         | Player enters the vehicle.               |
| AgentExitsVehicleEvent  | listenable(agent)         | Player exits the vehicle.                |
| VehicleSpawnedEvent     | listenable(fort\_vehicle) | (Deprecated) Use SpawnedEvent instead.   |
| VehicleDestroyedEvent   | listenable(tuple())       | (Deprecated) Use DestroyedEvent instead. |

🎠 Device Configuration (Details Panel)

- Enabled During Phase: Choose when the spawner is active (e.g., Always, Pre-game).
- Enable Respawn: Toggle auto-respawn upon elimination.
- Respawn Time: Set delay before vehicle respawn.
- Respawn Vehicle When Enabled: Yes / No / Only if Needed.
- Destroy Vehicle When Disabled: Choose to eliminate vehicle on disable.
- Activating Team & Allowed Class: Restrict spawn/entry based on team/class.
- Additional cosmetic and physics-related settings.

🛠️ Verse Usage Example

```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

rocket_racing_vehicle_example := class(creative_device):

    @editable
    VehicleSpawner : vehicle_spawner_rocketracing_device = vehicle_spawner_rocketracing_device{}

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
        Print("Rocket Racing vehicle spawned!")

    OnVehicleDestroyed() : void =
        set CurrentVehicle = false
        Print("Rocket Racing vehicle destroyed!")

    OnAgentEntersVehicle(Agent : agent) : void =
        Print("Agent entered Rocket Racing vehicle!")

    OnAgentExitsVehicle(Agent : agent) : void =
        Print("Agent exited Rocket Racing vehicle!")

    OnEnablePressed(Agent : agent) : void =
        VehicleSpawner.Enable()
        Print("Rocket Racing vehicle spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        VehicleSpawner.Disable()
        Print("Rocket Racing vehicle spawner disabled!")

    OnRespawnPressed(Agent : agent) : void =
        VehicleSpawner.RespawnVehicle()
        Print("Rocket Racing vehicle respawned!")
```

🏢 How to Use in UEFN

1. **Place Devices in Your Level**

   - Add `vehicle_spawner_rocketracing_device` to your map.
   - Add three `button_device` actors labeled Enable, Disable, and Respawn.

2. **Configure Device in Details Panel**

   - Customize spawn rules, cosmetics, respawn behavior, and team/class restrictions.

3. **Create and Add Verse Script**

   - Open **Verse Explorer**.
   - Create new Verse file (e.g., `rocket_racing_vehicle_example.verse`).
   - Paste provided code and save.
   - Build the code (Ctrl+Shift+B) until "Build Succeeded."
   - Place your custom Verse device in the level and set `@editable` fields.

4. **Playtest & Expand**

   - Play your level and test buttons to control the vehicle.
   - Add logic for scoring, cutscenes, or time-based events.
   - Replace `Print` statements with VFX, sounds, or gameplay functions.

🧠 Best Practices

- Use enable/disable/respawn scripting at race checkpoints.
- Customize driver assignment and elimination logic for gameplay variety.
- Combine Verse scripting with physical settings for multiplayer racing or elimination modes.

❌ Common Issues & Fixes

| Problem                           | Likely Reason                        | Solution                                  |
| --------------------------------- | ------------------------------------ | ----------------------------------------- |
| Vehicle not spawning              | Spawner not enabled or misconfigured | Use `Enable()`, check team/class setup    |
| Events not triggered              | Subscriptions missing                | Ensure event subscriptions in `OnBegin()` |
| Vehicle not eliminated on disable | Setting not configured               | Enable "Destroy on Disable" in Details    |

Note:

- Rocket Racing Vehicles use player locker cosmetics by default.
- All major vehicle logic (spawn, destroy, entry, exit) can be handled in Verse for full customization.

