# 📘 vehicle_spawner_siege_cannon_device – UEFN Verse Device Documentation

## 🔹 Description
The `vehicle_spawner_siege_cannon_device` is a spawner for Siege Cannon vehicles in Unreal Editor for Fortnite (UEFN). This device can be enabled, disabled, respawned, eliminated, and driven via Verse scripting. It is designed for creative vehicle encounters, objectives, and arena battles—providing full control over the vehicle’s presence, interactions, and player assignment.

---

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `vehicle_spawner_device`
- `vehicle_spawner_siege_cannon_device`

---

## 🛠️ Key Methods & Functions
| Method | Description |
|--------|-------------|
| `Enable()` | Enables the spawner so the cannon can spawn/respawn. |
| `Disable()` | Disables the spawner (optionally eliminates the cannon vehicle). |
| `RespawnVehicle()` | Spawns a new Siege Cannon (eliminates any previous vehicle). |
| `DestroyVehicle()` | Immediately eliminates the current Siege Cannon spawned. |
| `AssignDriver(agent)` | Makes an agent/player the driver of the spawned Siege Cannon. |
| `GetTransform()` | Gets the spawner’s world transform (location, rotation, scale). |
| `MoveTo()/TeleportTo()` | Moves/teleports the spawner (and its vehicle if active) in the level. |

---

## 🧩 Events (Data Members)
| Name | Type | When It Fires |
|------|------|----------------|
| `SpawnedEvent` | `listenable(fort_vehicle)` | When the siege cannon is spawned or respawned |
| `DestroyedEvent` | `listenable(tuple())` | When the siege cannon is eliminated |
| `AgentEntersVehicleEvent` | `listenable(agent)` | When an agent/player enters the siege cannon |
| `AgentExitsVehicleEvent` | `listenable(agent)` | When an agent/player exits the siege cannon |

---

## 🎛 Device Configuration (Details Panel)
- **Spawn When Enabled**: Spawns the cannon when device is enabled
- **Destroy on Disable**: Removes the siege cannon when disabling the device
- **Customization**: Appearance, durability, drive settings, etc.
- **Vehicle HP/Indestructible**: Set HP, destruction on disable, respawn rules

---

## 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

siege_cannon_example := class(creative_device):

    @editable
    SiegeCannonSpawner : vehicle_spawner_siege_cannon_device = vehicle_spawner_siege_cannon_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    RespawnButton : button_device = button_device{}

    var CurrentVehicle : ?fort_vehicle = false

    OnBegin<override>()<suspends> : void =
        # Subscribe to vehicle events
        SiegeCannonSpawner.SpawnedEvent.Subscribe(OnVehicleSpawned)
        SiegeCannonSpawner.DestroyedEvent.Subscribe(OnVehicleDestroyed)
        SiegeCannonSpawner.AgentEntersVehicleEvent.Subscribe(OnAgentEntersVehicle)
        SiegeCannonSpawner.AgentExitsVehicleEvent.Subscribe(OnAgentExitsVehicle)

        # Subscribe to control buttons
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        RespawnButton.InteractedWithEvent.Subscribe(OnRespawnPressed)

    # Event handlers
    OnVehicleSpawned(Vehicle : fort_vehicle) : void =
        set CurrentVehicle = option{Vehicle}
        Print("Siege Cannon spawned!")

    OnVehicleDestroyed() : void =
        set CurrentVehicle = false
        Print("Siege Cannon destroyed!")

    OnAgentEntersVehicle(Agent : agent) : void =
        Print("Agent entered Siege Cannon!")

    OnAgentExitsVehicle(Agent : agent) : void =
        Print("Agent exited Siege Cannon!")

    # Button control handlers
    OnEnablePressed(Agent : agent) : void =
        SiegeCannonSpawner.Enable()
        Print("Siege Cannon spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        SiegeCannonSpawner.Disable()
        Print("Siege Cannon spawner disabled!")

    OnRespawnPressed(Agent : agent) : void =
        SiegeCannonSpawner.RespawnVehicle()
        Print("Siege Cannon respawned!")
```

### 🔍 Explanation
- `SiegeCannonSpawner`: Reference to your placed siege cannon spawner.
- `EnableButton`, `DisableButton`, `RespawnButton`: Manual controls for testing or gameplay scripting; assign them in your Verse device’s Details panel.
- **Event Handlers**: Subscribe to all major events to handle entry/exit, spawn, and destruction. Print statements can be swapped for game logic (score, state changes, elimination, etc.).
- Use `.AssignDriver(Agent)` in your own logic (not shown here) to force a player inside the cannon.

---

## 🧪 How to Use in UEFN
1. **Place Devices in Your Level**
   - Add a `vehicle_spawner_siege_cannon_device` from the Devices panel.
   - Add three `button_device`s for Enable, Disable, and Respawn.

2. **Configure in Details Panel**
   - Set “Spawn When Enabled”, “Destroy on Disable”, vehicle health, durability, colors, and appearance.
   - Adjust drive settings as needed for your gameplay.

3. **Create & Add Your Verse Device**
   - Open **Verse Explorer** (menu: Verse → Verse Explorer).
   - Right-click a folder, choose **Create New Verse File** (e.g., `siege_cannon_example.verse`).
   - Create Empty, paste the provided code, and save.
   - Click **Verse → Build Verse Code** (Ctrl+Shift+B) until “Build Succeeded.”
   - Drag your Verse device into the world.

4. **Assign `@editable` References**
   - In your Verse device Details panel, set:
     - `SiegeCannonSpawner` → your siege cannon spawner device
     - `EnableButton`, `DisableButton`, `RespawnButton` → your button devices

5. **Launch & Test**
   - Use your buttons to spawn, destroy, or respawn the Siege Cannon.
   - Watch the Output Log for print statements or extend the logic.

---

## 🧠 Best Practices
- Use event handlers to award points, advance objectives, or react to Siege Cannon destruction or capture.
- Combine auto-respawn and manual respawn logic for creative challenges, minigames, or boss fights.
- Assign drivers programmatically for quick round starts or forced cannon control moments.

---

## ❌ Common Issues & Fixes
| Issue | ❌ Problem | ✅ Solution |
|-------|-------------|--------------|
| Cannon not spawning | Not enabled or “Spawn on Enable” off | Call `.Enable()` or set option in Details panel |
| Cannon not removed on disable | “Destroy on Disable” not set | Set option in Details panel |
| No Verse event outputs | Not subscribed to events | Add `.Subscribe(...)` in `OnBegin` |
| `@editable` not set | Not linked in Details panel | Set references in Verse device’s Details panel |

---

## 📌 Notes
- All base functions for driver assignment, movement, respawn, and destruction are universal to all vehicle spawner devices.
- The Siege Cannon is suitable for arenas, puzzles, siege events, creative elimination win/protect mechanics, and much more.
- Use built-in device options for cosmetic and gameplay tweaks, supplement with Verse for logic and control.

