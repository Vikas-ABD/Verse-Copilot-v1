# vehicle\_spawner\_dirtbike\_device – UEFN Verse Device Documentation

## 🔹 Description

The `vehicle_spawner_dirtbike_device` is a specialized spawner in Unreal Editor for Fortnite (UEFN) that allows you to configure and spawn Dirtbike vehicles. You can enable/disable the spawner, respawn or destroy the vehicle, and subscribe to vehicle/agent events for gameplay scripting. This is ideal for racing, stunts, open-world traversal, and challenge events involving Dirtbikes.

## 🧱 Verse Using Statement

```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy

- creative\_object
- creative\_device\_base
- vehicle\_spawner\_device
- vehicle\_spawner\_dirtbike\_device

## 🛠️ Key Methods & Functions

| Method                | Description                                                   |
| --------------------- | ------------------------------------------------------------- |
| Enable()              | Enables the dirtbike spawner (vehicle can appear).            |
| Disable()             | Disables the spawner (and optionally eliminates the vehicle). |
| RespawnVehicle()      | Spawns a new Dirtbike (the previous is eliminated first).     |
| DestroyVehicle()      | Destroys the spawned Dirtbike immediately.                    |
| AssignDriver(agent)   | Assigns a player as driver of the spawned Dirtbike.           |
| GetTransform()        | Returns the spawner’s transform (position, rotation, scale).  |
| MoveTo()/TeleportTo() | Moves/teleports the spawner in the world.                     |

## 🧹 Major Events

| Name                    | Type                      | When It Fires                           |
| ----------------------- | ------------------------- | --------------------------------------- |
| SpawnedEvent            | listenable(fort\_vehicle) | When a Dirtbike is spawned or respawned |
| DestroyedEvent          | listenable(tuple())       | When the Dirtbike is eliminated         |
| AgentEntersVehicleEvent | listenable(agent)         | When a player enters the vehicle        |
| AgentExitsVehicleEvent  | listenable(agent)         | When a player exits the vehicle         |

## 🗜️ Device Configuration (Details Panel)

- **Dirtbike Appearance**: Color, wheels, visual/fx, boost, handling
- **Spawn When Enabled**: Yes/No (spawns vehicle immediately when enabled)
- **Destroy on Disable**: Eliminates vehicle if device is disabled
- **Vehicle Health**: Max HP, destructibility, respawn handling
- **Can Be Damaged**: Sets if vehicles/eliminations allowed by physics

## 🧰 Verse Usage Example

```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

dirtbike_vehicle_example := class(creative_device):

    @editable
    DirtbikeSpawner : vehicle_spawner_dirtbike_device = vehicle_spawner_dirtbike_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    RespawnButton : button_device = button_device{}

    var CurrentVehicle : ?fort_vehicle = false

    OnBegin<override>()<suspends> : void =
        # Subscribe to vehicle events
        DirtbikeSpawner.SpawnedEvent.Subscribe(OnVehicleSpawned)
        DirtbikeSpawner.DestroyedEvent.Subscribe(OnVehicleDestroyed)
        DirtbikeSpawner.AgentEntersVehicleEvent.Subscribe(OnAgentEntersVehicle)
        DirtbikeSpawner.AgentExitsVehicleEvent.Subscribe(OnAgentExitsVehicle)

        # Subscribe to control buttons
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        RespawnButton.InteractedWithEvent.Subscribe(OnRespawnPressed)

    # Event handlers
    OnVehicleSpawned(Vehicle : fort_vehicle) : void =
        set CurrentVehicle = option{Vehicle}
        Print("Dirtbike spawned!")

    OnVehicleDestroyed() : void =
        set CurrentVehicle = false
        Print("Dirtbike destroyed!")

    OnAgentEntersVehicle(Agent : agent) : void =
        Print("Agent entered Dirtbike!")

    OnAgentExitsVehicle(Agent : agent) : void =
        Print("Agent exited Dirtbike!")

    # Button control handlers
    OnEnablePressed(Agent : agent) : void =
        DirtbikeSpawner.Enable()
        Print("Dirtbike spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        DirtbikeSpawner.Disable()
        Print("Dirtbike spawner disabled!")

    OnRespawnPressed(Agent : agent) : void =
        DirtbikeSpawner.RespawnVehicle()
        Print("Dirtbike respawned!")
```

### Explanation

- `vehicle_spawner_dirtbike_device`: Place in your level, assign reference in your Verse device.
- **Button Devices**: Add three button devices (“Enable”, “Disable”, “Respawn”), connect to your Verse device for manual demo/test control.
- **Verse Event Subscriptions**: Listen to spawned/destroyed/agent-enter/agent-exit events for live feedback, triggers, or custom logic.
- **Print Statements**: For clear output testing (replace with gameplay logic as needed).

## 🖩 How to Use in UEFN

1. **Place Devices in Your Level**
   - Put a `vehicle_spawner_dirtbike_device` in your world.
   - Add three `button_device`s for Enable, Disable, Respawn.
2. **Configure in Details Panel**
   - Set Dirtbike visual, HP, spawn, destruction, boost, and color options as needed.
   - Decide if device is enabled and/or auto-spawns at round start.
3. **Create & Add Your Verse Script**
   - In *Verse Explorer* (top menu), right-click a folder → *Create New Verse File* (e.g., `dirtbike_vehicle_example.verse`).
   - Choose Empty, paste the code above, save.
   - Build Verse Code (`Ctrl+Shift+B`) until you see "Build Succeeded."
   - Place your Verse device in the world.
4. **Assign @editable References**
   - In the Details panel of your Verse device, set:
     - `DirtbikeSpawner` → your spawner
     - `EnableButton`, `DisableButton`, `RespawnButton` → corresponding button devices
5. **Test**
   - Click your control buttons and observe vehicle spawning, elimination, and driver entry/exit in playtest.

## 🪖 Best Practices

- Combine event callbacks with triggers or stat counters for scoring, elimination, or checkpoint logic.
- Use respawn logic for skill challenges, time trials, races, or “bike wave” events.
- Assign drivers automatically on round start, checkpoint, or button press for controlled gameplay.

## ❌ Common Issues & Solutions

| Issue                  | ❌ Problem                     | ✅ Solution                           |
| ---------------------- | ----------------------------- | ------------------------------------ |
| Bike not spawning      | Device not enabled/spawn      | Call `.Enable()` or set spawn option |
| Bike not eliminated    | Wrong destroy settings        | Call `.DestroyVehicle()` or disable  |
| No events in Verse     | Not subscribed in `OnBegin`   | Subscribe as shown in example        |
| Device reference error | `@editable` reference not set | Set in Details panel                 |

> **Note:**
>
> - Use Verse methods for dynamic, real-time control.
> - Configure base properties in Details panel.
> - All handling, eliminations, and player/vehicle events are tracked and scriptable via Verse for custom gameplay.

