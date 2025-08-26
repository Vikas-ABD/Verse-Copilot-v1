📘 **vehicle_spawner_ufo_device – UEFN Verse Device Documentation**

---

### 🔹 Description
The `vehicle_spawner_ufo_device` is a specialized spawner for UFO vehicles in Unreal Editor for Fortnite (UEFN). This device enables you to spawn, eliminate, assign drivers to, and fully manage UFOs using both Verse scripting and creative device wiring. It’s ideal for creating flying challenges, sci-fi maps, UFO minigames, or special event objectives with powerful event and driver control.

---

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
* `creative_object`
* `creative_device_base`
* `vehicle_spawner_device`
* `vehicle_spawner_ufo_device`

---

### 🛠️ Key Methods & Functions
| Method               | Description                                            |
|---------------------|--------------------------------------------------------|
| `Enable()`          | Enables the UFO spawner device.                       |
| `Disable()`         | Disables the device and (optionally) eliminates UFO.  |
| `RespawnVehicle()`  | Spawns a new UFO; eliminates old, if present.         |
| `DestroyVehicle()`  | Immediately eliminates the spawned UFO.               |
| `AssignDriver(agent)`| Assigns the provided agent as the UFO driver.         |
| `GetTransform()`    | Gets the world transform of the spawner device.       |
| `MoveTo()`/`TeleportTo()`| Move or teleport the spawner in-game.         |

---

### 🧩 Events (Data Members)
| Name                      | Type                           | When It Fires                        |
|---------------------------|--------------------------------|--------------------------------------|
| `SpawnedEvent`            | `listenable(fort_vehicle)`     | When a UFO is spawned or respawned   |
| `DestroyedEvent`          | `listenable(tuple())`          | When the spawned UFO is eliminated   |
| `AgentEntersVehicleEvent`| `listenable(agent)`            | When an agent enters the UFO         |
| `AgentExitsVehicleEvent` | `listenable(agent)`            | When an agent exits the UFO          |

---

### 🎛 Device Configuration (Details Panel)
* **Appearance/Color/FX** – Customize UFO visuals (lights, colors, etc.)
* **Spawn When Enabled** – UFO appears automatically when device is enabled
* **Destroy on Disable** – Eliminates UFO when device is disabled
* **Indestructibility/Vehicle HP** – Set UFO's durability
* **Auto Respawn** – Recreates UFO automatically after elimination

---

### 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

ufo_vehicle_example := class(creative_device):

    @editable
    UFOSpawner : vehicle_spawner_ufo_device = vehicle_spawner_ufo_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    RespawnButton : button_device = button_device{}

    var CurrentVehicle : ?fort_vehicle = false

    OnBegin<override>()<suspends> : void =
        UFOSpawner.SpawnedEvent.Subscribe(OnVehicleSpawned)
        UFOSpawner.DestroyedEvent.Subscribe(OnVehicleDestroyed)
        UFOSpawner.AgentEntersVehicleEvent.Subscribe(OnAgentEntersVehicle)
        UFOSpawner.AgentExitsVehicleEvent.Subscribe(OnAgentExitsVehicle)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        RespawnButton.InteractedWithEvent.Subscribe(OnRespawnPressed)

    OnVehicleSpawned(Vehicle : fort_vehicle) : void =
        set CurrentVehicle = option{Vehicle}
        Print("UFO spawned!")

    OnVehicleDestroyed() : void =
        set CurrentVehicle = false
        Print("UFO destroyed!")

    OnAgentEntersVehicle(Agent : agent) : void =
        Print("Agent entered UFO!")

    OnAgentExitsVehicle(Agent : agent) : void =
        Print("Agent exited UFO!")

    OnEnablePressed(Agent : agent) : void =
        UFOSpawner.Enable()
        Print("UFO spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        UFOSpawner.Disable()
        Print("UFO spawner disabled!")

    OnRespawnPressed(Agent : agent) : void =
        UFOSpawner.RespawnVehicle()
        Print("UFO respawned!")
```

---

### 💡 Explanation
* `UFOSpawner` – Reference your placed `vehicle_spawner_ufo_device`
* `EnableButton`, `DisableButton`, `RespawnButton` – Assign button devices for control
* `CurrentVehicle` – Tracks the latest spawned UFO
* Events subscribed in `OnBegin`
* Button handlers show how to control the UFO with in-game devices
* Use `AssignDriver(MyAgent)` to assign players to the UFO

---

### 🧪 How to Use in UEFN
1. **Place Devices**
   - Place `vehicle_spawner_ufo_device` in world
   - Add 3 `button_device`s for control (Enable, Disable, Respawn)

2. **Configure UFO in Details Panel**
   - Customize appearance, spawn settings, HP, etc.

3. **Create Verse Script**
   - Open Verse Explorer → Create new Verse file
   - Paste provided code and build with Ctrl+Shift+B

4. **Assign References in Details Panel**
   - Connect the UFO spawner and buttons to your Verse device

5. **Play and Extend**
   - Test interactions, then expand event handlers for gameplay logic

---

### 🧠 Best Practices
* Use `AssignDriver()` to auto-seat players during round starts or objectives
* Leverage events to trigger score, mission updates, or dynamic logic
* Use auto-respawn or destroy-on-disable depending on game mode

---

### ❌ Common Issues & Fixes
| Issue                   | ❌ Problem                          | ✅ Solution                            |
|------------------------|-------------------------------------|----------------------------------------|
| UFO does not spawn     | Device not enabled or config issue | Call `.Enable()` or set auto-spawn     |
| Driver not assigned    | No call to `AssignDriver()`        | Use `AssignDriver(MyAgent)` in logic   |
| Events don’t trigger   | Not subscribed in Verse script     | Ensure `.Subscribe(...)` in `OnBegin`  |
| Reference error        | Editable not linked                | Link devices in Details panel          |

---

### 📌 Note
* Full control over UFO lifecycle and events via Verse
* Details panel sets visual and mechanical configuration
* Suitable for PvP flight events, challenges, missions, and more

