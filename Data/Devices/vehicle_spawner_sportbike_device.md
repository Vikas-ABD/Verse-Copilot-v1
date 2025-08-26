📘 **vehicle_spawner_sportbike_device – UEFN Verse Device Documentation**

---

### 🔹 Description
The `vehicle_spawner_sportbike_device` is a specialized spawner in Unreal Editor for Fortnite (UEFN) that allows you to configure and spawn a **Sportbike** vehicle. You can fully control the spawner and the spawned bike using Verse—enabling/disabling, respawning, assigning drivers, moving the device, and subscribing to all driving events—making this device perfect for racing, stunts, open-world play, or skill challenges.

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `vehicle_spawner_device`
- `vehicle_spawner_sportbike_device`

---

### 🛠️ Key Methods & Functions
| Method              | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `Enable()`          | Enables the spawner (bike can spawn or be spawned by code/trigger).         |
| `Disable()`         | Disables the device (and eliminates the bike if “destroy on disable” set).  |
| `RespawnVehicle()`  | Spawns a new Sportbike (destroys previous if exists).                       |
| `DestroyVehicle()`  | Instantly eliminates the current Sportbike.                                 |
| `AssignDriver(agent)` | Assigns the given agent/player as the bike’s driver.                        |
| `GetTransform()`    | Gets the spawner’s transform (location, rotation, etc.).                    |
| `MoveTo()` / `TeleportTo()` | Moves/teleports the spawner (and its Sportbike if active).                |

---

### 🧩 Events (Data Members)
| Name                        | Type                         | When It Fires                                      |
|-----------------------------|------------------------------|----------------------------------------------------|
| `SpawnedEvent`             | `listenable(fort_vehicle)`   | When a Sportbike is spawned or respawned          |
| `DestroyedEvent`           | `listenable(tuple())`        | When the Sportbike is eliminated                  |
| `AgentEntersVehicleEvent`  | `listenable(agent)`          | When an agent/player enters the Sportbike         |
| `AgentExitsVehicleEvent`   | `listenable(agent)`          | When an agent/player exits the Sportbike          |

---

### 🎛 Device Configuration (Details Panel)
- **Bike Appearance:** Color, wheels, boost, FX, handling, etc.
- **Spawn When Enabled:** Sportbike appears immediately on enable
- **Destroy on Disable:** Eliminates bike when disabling device
- **Vehicle Health:** Set max HP, destructibility, auto-respawn
- **Driver Permissions:** Restrict by team/class, control who can ride

---

### 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

sportbike_vehicle_example := class(creative_device):

    @editable
    SportbikeSpawner : vehicle_spawner_sportbike_device = vehicle_spawner_sportbike_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    RespawnButton : button_device = button_device{}

    var CurrentVehicle : ?fort_vehicle = false

    OnBegin<override>()<suspends> : void =
        SportbikeSpawner.SpawnedEvent.Subscribe(OnVehicleSpawned)
        SportbikeSpawner.DestroyedEvent.Subscribe(OnVehicleDestroyed)
        SportbikeSpawner.AgentEntersVehicleEvent.Subscribe(OnAgentEntersVehicle)
        SportbikeSpawner.AgentExitsVehicleEvent.Subscribe(OnAgentExitsVehicle)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        RespawnButton.InteractedWithEvent.Subscribe(OnRespawnPressed)

    OnVehicleSpawned(Vehicle : fort_vehicle) : void =
        set CurrentVehicle = option{Vehicle}
        Print("Sportbike spawned!")

    OnVehicleDestroyed() : void =
        set CurrentVehicle = false
        Print("Sportbike destroyed!")

    OnAgentEntersVehicle(Agent : agent) : void =
        Print("Agent entered Sportbike!")

    OnAgentExitsVehicle(Agent : agent) : void =
        Print("Agent exited Sportbike!")

    OnEnablePressed(Agent : agent) : void =
        SportbikeSpawner.Enable()
        Print("Sportbike spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        SportbikeSpawner.Disable()
        Print("Sportbike spawner disabled!")

    OnRespawnPressed(Agent : agent) : void =
        SportbikeSpawner.RespawnVehicle()
        Print("Sportbike respawned!")
```

---

### 📝 Explanation
- `SportbikeSpawner`: Reference your placed `vehicle_spawner_sportbike_device`
- `EnableButton`, `DisableButton`, `RespawnButton`: Button devices placed in your world for manual/demo control—assign them from your Verse device’s Details panel.
- Subscribes to spawn, destruction, and agent-enter/exit events.
- Print output can be replaced with your race, challenge, or scoring logic.
- Use `.AssignDriver(agent)` for forced entry/race start logic if desired.

---

### 🧪 How to Use in UEFN
1. **Place Devices in Your Level**
   - Add a `vehicle_spawner_sportbike_device` where you want the bike to spawn.
   - Add three `button_device` instances for Enable, Disable, and Respawn.

2. **Configure Bike in Details Panel**
   - Choose appearance, HP, spawn-on-enable, destroy-on-disable, and driver/team/class options.

3. **Create and Add Your Verse Script**
   - In *Verse Explorer* → Right-click any folder → *Create New Verse File* (e.g., `sportbike_vehicle_example.verse`)
   - Choose *Create Empty*, paste the code above, and save.
   - Click *Verse → Build Verse Code* (Ctrl+Shift+B).
   - Drag your custom Verse device into the world.

4. **Assign `@editable` References**
   - In your Verse device’s Details panel:
     - Assign `SportbikeSpawner` to your bike spawner
     - Assign the three button devices

5. **Test in Play Session**
   - Use the buttons to confirm that the bike appears, is enabled/disabled, and respawns.
   - Watch Output Log for printed messages, or replace with your gameplay logic.

---

### 🧠 Best Practices
- Subscribe to all vehicle and entry/exit events for race timers, scoring, or extra rewards.
- Combine event logic and device settings for advanced race/obstacle/arena design.
- Use `.Enable()` / `.Disable()` and `.RespawnVehicle()` for round-based gameplay or timed challenges.

---

### ❌ Common Issues & Fixes
| Issue                  | ❌ Problem                                  | ✅ Solution                                                 |
|------------------------|---------------------------------------------|-------------------------------------------------------------|
| Bike not spawning      | Device not enabled or spawn option unset    | Call `.Enable()` or set "Spawn When Enabled"               |
| No event output in Verse | Not subscribed to events                    | Use `.Subscribe(...)` as in the example                     |
| Reference errors       | `@editable` not set in Details              | Assign all references in Details, then build Verse         |

> **Note:** Use all built-in device settings for visuals and restrictions. Verse gives you maximum control for interactive, dynamic, or competitive gameplay using the Sportbike.

