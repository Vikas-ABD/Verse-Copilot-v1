📘 **vehicle_spawner_taxi_device – UEFN Verse Device Documentation**

---

🔹 **Description**

The `vehicle_spawner_taxi_device` is a specialized spawner used in Fortnite Creative that allows you to spawn and control Taxi vehicles. Inheriting from `vehicle_spawner_device`, this device provides the ability to enable or disable spawning, assign drivers, and handle vehicle events such as entering and exiting. It supports gameplay design around taxi-based interactions like pickup systems, checkpoint navigation, or event relays through scripting in Verse.

---

🧱 **Verse Using Statement**
```verse
using { /Fortnite.com/Devices }
```

---

🔗 **Inheritance Hierarchy**
- `creative_object`
- `creative_device_base`
- `vehicle_spawner_device`
- `vehicle_spawner_taxi_device`

---

🛠️ **Functions & Methods**
| Name | Description |
|------|-------------|
| `Enable()` | Activates the taxi spawner. |
| `Disable()` | Deactivates the spawner, stopping taxi spawning. |
| `RespawnVehicle()` | Destroys any existing taxi and spawns a new one. |
| `AssignDriver(agent)` | Sets an agent as the driver of the taxi. |
| `DestroyVehicle()` | Removes the currently spawned taxi, if any. |
| `GetTransform()` | Retrieves the device's world transform. |
| `MoveTo()` / `TeleportTo()` | Moves or teleports the device in the world. |

---

🧩 **Events (Data Members)**
| Name | Type | Description |
|------|------|-------------|
| `SpawnedEvent` | `listenable(fort_vehicle)` | Fires when a taxi is spawned. |
| `DestroyedEvent` | `listenable(tuple())` | Fires when a taxi is destroyed. |
| `AgentEntersVehicleEvent` | `listenable(agent)` | Fires when an agent enters the taxi. |
| `AgentExitsVehicleEvent` | `listenable(agent)` | Fires when an agent exits the taxi. |
| *(Deprecated)* `VehicleSpawnedEvent` / `VehicleDestroyedEvent` | Legacy events; use the above instead. |

---

🎛 **Configuration Options (Details Panel)**
| Option | Description |
|--------|-------------|
| Vehicle to Spawn | Taxi (fixed) |
| Enable at Start | Whether spawner is active on game start. |
| Respawn Handling | Manual, timer-based, or automatic. |
| Team Limit | Restricts spawn access by team. |
| Spawn Effects | Toggle for spawn/destruction VFX/SFX. |
| Spawn Volume/Position | Set specific spawn location. |
| Simultaneous Vehicles | Max active taxis at once. |

---

🧰 **Verse Usage Example**
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use vehicle_spawner_taxi_device
taxi_spawner_example := class(creative_device):

    @editable
    TaxiSpawner : vehicle_spawner_taxi_device = vehicle_spawner_taxi_device{}

    @editable
    SpawnButton : button_device = button_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        TaxiSpawner.SpawnedEvent.Subscribe(OnVehicleSpawned)
        TaxiSpawner.DestroyedEvent.Subscribe(OnVehicleDestroyed)
        TaxiSpawner.AgentEntersVehicleEvent.Subscribe(OnAgentEntersVehicle)
        TaxiSpawner.AgentExitsVehicleEvent.Subscribe(OnAgentExitsVehicle)

        SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnVehicleSpawned(Vehicle : fort_vehicle) : void =
        Print("Taxi spawned!")

    OnVehicleDestroyed() : void =
        Print("Taxi destroyed!")

    OnAgentEntersVehicle(Agent : agent) : void =
        Print("Agent entered taxi!")

    OnAgentExitsVehicle(Agent : agent) : void =
        Print("Agent exited taxi!")

    OnSpawnPressed(Agent : agent) : void =
        TaxiSpawner.RespawnVehicle()
        Print("Taxi respawned!")

    OnEnablePressed(Agent : agent) : void =
        TaxiSpawner.Enable()
        Print("Taxi spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        TaxiSpawner.Disable()
        Print("Taxi spawner disabled!")
```

**Explanation:**
- Connects button devices to control the taxi spawner.
- Subscribes to vehicle lifecycle and player interaction events.
- Uses print statements to visualize the process.

---

🛠️ **How to Use in UEFN**
1. **Add Devices to Level**
   - Drag `vehicle_spawner_taxi_device` and three `button_devices` (Spawn, Enable, Disable) into the level.

2. **Configure Spawner**
   - Set options like spawn method, team access, max taxi count, etc.

3. **Create Verse File**
   - In Verse Explorer: Create New Verse File → Paste code → Save.
   - Build (Ctrl+Shift+B) until "Build Succeeded".

4. **Assign Editable Fields**
   - Link the TaxiSpawner and buttons in the Verse device Details panel.

5. **Test and Debug**
   - Use buttons to control taxi spawn and state.
   - View print logs or add game logic for advanced features.

---

🧠 **Best Practices**
- Leverage events for mission triggers, rewards, checkpoints.
- Use `.AssignDriver(agent)` in team quests to automate taxi control.
- Adjust spawner settings for gameplay balance and team access.
- Combine with timers, triggers, and UI for immersive experiences.

---

❌ **Common Issues & Fixes**
| Issue | ❌ Example | ✅ Solution | Explanation |
|-------|------------|-------------|-------------|
| Taxi not spawning | `.RespawnVehicle()` not called | Trigger via button/event | Required to spawn taxi manually unless auto-respawn is set |
| No Verse output | Events not subscribed | Add `.Subscribe()` in `OnBegin` | Event handlers must be linked manually |
| Editable fields empty | Missing device assignment | Link in Details panel | Required for references to work |
| Vehicle inaccessible | Incorrect team/spawn config | Set proper team permissions | Only configured teams can access taxi |

---

💡 **Use Cases**
- Taxi races with checkpoints
- Pickup and drop quests
- Relay races using vehicle triggers
- Cinematics or cutscene transport setups

For complex logic like scores or missions, extend your Verse scripts with timers, triggers, and HUD updates.

