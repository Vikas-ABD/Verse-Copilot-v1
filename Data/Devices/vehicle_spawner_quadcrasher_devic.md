📘 **vehicle_spawner_quadcrasher_device – UEFN Verse Device Documentation**

---

### 🔹 Description
The `vehicle_spawner_quadcrasher_device` is a specialized spawner that allows you to configure and spawn the **Quadcrasher** vehicle in your Fortnite experience. It inherits all controls and event abilities from `vehicle_spawner_device`, including dynamic spawning, driver assignment, and detailed event handling for player interaction. You can use **Verse** to control spawning, enable/disable the spawner, and monitor events such as agents entering or exiting the vehicle.

---

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `vehicle_spawner_device`
- `vehicle_spawner_quadcrasher_device`

---

### 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| `Enable()` | Enables the device—spawner is active/visible. |
| `Disable()` | Disables the device—spawner is inactive. |
| `RespawnVehicle()` | Spawns or respawns the Quadcrasher (replacing previous one). |
| `AssignDriver(agent)` | Instantly sets the provided agent as the vehicle driver. |
| `DestroyVehicle()` | Destroys the spawned vehicle if it exists. |
| `GetTransform()` | Gets device’s world transform. |
| `MoveTo()` / `TeleportTo()` | Animates/moves or teleports the device. |

---

### 🧹 Events (Data Members)
| Name | Type | Description |
|------|------|-------------|
| `SpawnedEvent` | `listenable(fort_vehicle)` | Fires when a Quadcrasher is spawned (provides the vehicle handle). |
| `DestroyedEvent` | `listenable(tuple())` | Fires when the Quadcrasher is destroyed. |
| `AgentEntersVehicleEvent` | `listenable(agent)` | Fires when an agent enters the Quadcrasher. |
| `AgentExitsVehicleEvent` | `listenable(agent)` | Fires when an agent exits the Quadcrasher. |
| `VehicleSpawnedEvent` (deprecated) | - | Use `SpawnedEvent` instead. |
| `VehicleDestroyedEvent` (deprecated) | - | Use `DestroyedEvent` instead. |

---

### 🎯 Configuration Options (Details Panel)
- **Vehicle to Spawn:** Quadcrasher (fixed for this device)
- **Enable at Game Start:** Whether spawner is active at game start
- **Respawn Settings:** Auto-respawn, manual, or timed options
- **Available Teams:** Restrict team access
- **Spawn Effects/FX:** Toggle VFX/SFX and visuals
- **Limit Per Team:** Cap number of vehicles per team
- **Spawn Area/Volume:** Define spawn region or logic
- **Interaction:** Auto-entry, player control behaviors

---

### 🧰 Verse Usage Example
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

---

### 📚 How to Use in UEFN
1. **Add the Device**
    - In Content Browser, drag a `vehicle_spawner_quadcrasher_device` into your world.

2. **Configure Spawner Options**
    - Set respawn settings, team availability, FX, and handling in Details panel.

3. **Place Supporting Devices**
    - Add three `button_device` objects: Spawn, Enable, and Disable.

4. **Create Your Verse File**
    - Right-click a folder in Verse Explorer > Create New Verse File (e.g., `quadcrasher_spawner_example.verse`)
    - Paste the code above and build it (`Ctrl+Shift+B`).

5. **Place and Set Up Your Verse Device**
    - Drag the custom Verse device into your level.
    - Link all `@editable` properties: set the spawner and buttons.

6. **Test Your Setup**
    - Enter play mode. Test buttons to respawn, enable, or disable spawner and observe event prints.

---

### 🧠 Best Practices
- Use event subscriptions to drive game logic.
- Control spawn availability per game round or challenge.
- Use `AssignDriver(agent)` to dynamically assign players.

---

### ❌ Common Issues & Fixes
| Issue | ❌ Problem | ✅ Solution | Explanation |
|-------|--------------|----------------|-------------|
| No vehicle appears | Device not enabled/spawned | Enable + `RespawnVehicle()` | Spawner must be active and trigger spawn |
| Not responding to players | Team restrictions or spawn area | Configure team access & placement | Proper access and placement needed |
| Blank `@editable` values | References not set | Assign spawner & buttons | Required to function in Verse |
| Events not triggering | Missing `Subscribe` calls | Add event subscriptions | Must hook into event handlers |

---

**Note:**
- Full support for script, trigger, and manual control.
- Pair with volumes, triggers, or spawn phases for creative setups.
- Control all logic in Verse for full flexibility.

