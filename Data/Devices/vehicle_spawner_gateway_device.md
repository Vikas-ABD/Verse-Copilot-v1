📘 **vehicle_spawner_getaway_device – UEFN Verse Device Documentation**

---

🔹 **Description**
The `vehicle_spawner_getaway_device` is a specialized vehicle spawner in Unreal Editor for Fortnite (UEFN) allowing you to configure, spawn, and control a GetAway Car. You can enable/disable, force respawn, assign drivers, and wire up all vehicle/player events via Verse—ideal for getaway scenarios, heist maps, or any game mode requiring dynamic car control and event scripting.

🧱 **Verse Using Statement**
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
```

🔗 **Inheritance Hierarchy**
- creative_object
- creative_device_base
- vehicle_spawner_device
- vehicle_spawner_getaway_device

🛠️ **Key Methods & Functions**
| Method | Description |
|--------|-------------|
| Enable() | Enables this car spawner (makes spawning possible). |
| Disable() | Disables the device and eliminates any spawned car. |
| RespawnVehicle() | Eliminates current spawned car and spawns a new one. |
| DestroyVehicle() | Eliminates the spawned getaway car, if present. |
| AssignDriver(agent) | Sets the given agent/player as the vehicle’s driver. |
| GetTransform() | Returns spawner’s transform (location/rotation/scale). |
| MoveTo()/TeleportTo() | Animates or teleports the spawner (and car, if present). |

🧩 **Events (Data Members)**
| Name | Type | Description |
|------|------|-------------|
| SpawnedEvent | listenable(fort_vehicle) | When GetAway car is spawned/respawned |
| DestroyedEvent | listenable(tuple()) | When the car is eliminated (destroyed) |
| AgentEntersVehicleEvent | listenable(agent) | When an agent/player enters the car |
| AgentExitsVehicleEvent | listenable(agent) | When an agent/player exits the car |

🎠 **Device Configuration (Details Panel)**
- **Appearance/Setup**: Car color, wheels, effects, HP, etc.
- **Spawn When Enabled**: Spawn car automatically when enabled
- **Destroy On Disable**: Eliminate car when spawner disabled
- **Respawn On Elimination**: Auto-respawn after the car is eliminated
- **Can Be Damaged**: Vehicle destructibility
- **Driver Restrictions**: Team/class restrictions for vehicle use

🛠️ **Verse Usage Example**
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

getaway_vehicle_example := class(creative_device):

    @editable
    GetawaySpawner : vehicle_spawner_getaway_device = vehicle_spawner_getaway_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    RespawnButton : button_device = button_device{}

    var CurrentVehicle : ?fort_vehicle = false

    OnBegin<override>()<suspends> : void =
        GetawaySpawner.SpawnedEvent.Subscribe(OnVehicleSpawned)
        GetawaySpawner.DestroyedEvent.Subscribe(OnVehicleDestroyed)
        GetawaySpawner.AgentEntersVehicleEvent.Subscribe(OnAgentEntersVehicle)
        GetawaySpawner.AgentExitsVehicleEvent.Subscribe(OnAgentExitsVehicle)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        RespawnButton.InteractedWithEvent.Subscribe(OnRespawnPressed)

    OnVehicleSpawned(Vehicle : fort_vehicle) : void =
        set CurrentVehicle = option{Vehicle}
        Print("Getaway vehicle spawned!")

    OnVehicleDestroyed() : void =
        set CurrentVehicle = false
        Print("Getaway vehicle destroyed!")

    OnAgentEntersVehicle(Agent : agent) : void =
        Print("Agent entered Getaway vehicle!")

    OnAgentExitsVehicle(Agent : agent) : void =
        Print("Agent exited Getaway vehicle!")

    OnEnablePressed(Agent : agent) : void =
        GetawaySpawner.Enable()
        Print("Getaway vehicle spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        GetawaySpawner.Disable()
        Print("Getaway vehicle spawner disabled!")

    OnRespawnPressed(Agent : agent) : void =
        GetawaySpawner.RespawnVehicle()
        Print("Getaway vehicle respawned!")
```

**Explanation:**
- `GetawaySpawner`: Reference to the `vehicle_spawner_getaway_device` placed in the world.
- `EnableButton`, `DisableButton`, `RespawnButton`: Button devices assigned to control spawning logic.
- Subscribes to vehicle events to allow tracking, scoring, or mission logic.
- Modify `Print()` calls to implement custom gameplay effects (quests, scoring, progression).

🚀 **How to Use in UEFN**
1. **Place Devices in Your Level**
   - Place a `vehicle_spawner_getaway_device` (Devices > Vehicles > GetAway Car Spawner).
   - Place three `button_device` actors for Enable, Disable, and Respawn.

2. **Configure the GetAway Car**
   - Adjust settings like appearance, destructibility, auto-spawn in the Details panel.

3. **Create and Add Your Verse Script**
   - Open **Verse Explorer** (Verse → Verse Explorer).
   - Create a new Verse file (e.g., `getaway_vehicle_example.verse`).
   - Paste the provided script and save.
   - Build your Verse code with Ctrl+Shift+B.
   - Drag the Verse device into the world.

4. **Assign @editable References**
   - In the Verse device’s Details panel:
     - Link `GetawaySpawner` to your getaway car spawner device.
     - Link buttons to `EnableButton`, `DisableButton`, `RespawnButton`.

5. **Test & Extend**
   - Run a session.
   - Use the buttons to test spawn/disable/respawn.
   - Replace `Print()` calls with advanced game logic.

🧠 **Best Practices**
- Use event handlers (like `AgentEntersVehicleEvent`) for quests, triggers, races, or cinematics.
- Combine `Enable/Disable` and `RespawnVehicle` for round-based or phase-based gameplay.
- Use `AssignDriver(agent)` for intro cutscenes or automatic race setups.

❌ **Common Issues & Fixes**
| Issue | Cause | Solution |
|-------|--------|----------|
| Car doesn’t spawn | Not enabled or auto-spawn off | Call `.Enable()` or enable “Spawn When Enabled” |
| No event output | Missing event subscription | Ensure `.Subscribe(...)` is used properly |
| Reference errors | @editable links not set | Set all references in the Details panel |

---

**Note:** Combine device and Verse scripting to craft layered missions, synchronized car escapes, or interactive cutscenes using the GetAway Car system.

