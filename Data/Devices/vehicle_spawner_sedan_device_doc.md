# vehicle_spawner_sedan_device – UEFN Verse Device Documentation

## 🔹 Description
The `vehicle_spawner_sedan_device` is a specialized spawner for the **Prevalent sedan**, a civilian-style car in Fortnite. This device enables creators to dynamically **spawn**, **destroy**, and **manage** the sedan vehicle in their experience using **Verse scripting**. It supports key gameplay events such as vehicle **entry**, **exit**, **destruction**, and **respawning**.

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
- `vehicle_spawner_sedan_device`

---

## 🥉 Events (Data Members)
| Event Name               | Type                   | Description                                              |
|--------------------------|------------------------|----------------------------------------------------------|
| AgentEntersVehicleEvent | `listenable(agent)`    | Fires when a player enters the Prevalent sedan.          |
| AgentExitsVehicleEvent  | `listenable(agent)`    | Fires when a player exits the Prevalent sedan.           |
| DestroyedEvent          | `listenable()`         | Fires when the sedan is destroyed. (**Preferred**)        |
| SpawnedEvent            | `listenable(fort_vehicle)` | Fires when the sedan is spawned or respawned. (**Preferred**) |
| VehicleDestroyedEvent   | `listenable()`         | ❌ Deprecated – use `DestroyedEvent`.                   |
| VehicleSpawnedEvent     | `listenable(fort_vehicle)` | ❌ Deprecated – use `SpawnedEvent`.                 |

---

## 🛠️ Functions & Methods
| Function             | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `Enable()`           | Activates the device to allow sedan spawning.                              |
| `Disable()`          | Deactivates the device to prevent spawning.                                |
| `RespawnVehicle()`   | Destroys any existing sedan and spawns a new one.                          |
| `DestroyVehicle()`   | Destroys the currently spawned sedan, if any.                              |
| `AssignDriver(agent)`| Assigns the agent as the driver of the sedan.                              |
| `GetTransform()`     | Returns the device’s position, rotation, and scale. Use `IsValid()` before. |
| `MoveTo(Position, Rotation, Duration)` | Smoothly moves the device to a new location over time.   |
| `MoveTo(Transform, Duration)` | Moves the device using a full transform struct.                  |
| `TeleportTo(...)`    | Instantly relocates the device to a new location and orientation.          |

---

## 🪰 Verse Usage Example
This script enables the device, spawns the sedan at game start, and logs when a player enters or exits:

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

sedan_example := class(creative_device):

    @editable
    SedanSpawner : vehicle_spawner_sedan_device = vehicle_spawner_sedan_device{}

    OnBegin<override>()<suspends> : void =
        SedanSpawner.AgentEntersVehicleEvent.Subscribe(OnEnter)
        SedanSpawner.AgentExitsVehicleEvent.Subscribe(OnExit)

        SedanSpawner.Enable()
        SedanSpawner.RespawnVehicle()

    OnEnter(Player : agent) : void =
        Print("Player entered the sedan: {Player}")

    OnExit(Player : agent) : void =
        Print("Player exited the sedan: {Player}")
```

---

## 🔧 How to Use in UEFN
1. **Place the Device**
   - Drag `vehicle_spawner_sedan_device` into your level from the **Devices** tab.

2. **Configure Options**
   - Customize settings like vehicle **health**, **respawn timing**, **fuel**, and **team behavior** via the **Details** panel.

3. **Create Verse Script**
   - Use or customize the example provided above to handle vehicle logic.

4. **Assign References**
   - Link the placed device to the `SedanSpawner` field in your Verse script.

5. **Build & Test**
   - Compile Verse (`Ctrl+Shift+B`), playtest, and verify the behavior.

---

## 🧠 Best Practices
- Use `AssignDriver()` during scripted scenes (e.g., races, cutscenes).
- Combine with `trigger_device` or `button_device` to spawn the sedan on demand.
- Use `SpawnedEvent` to access the `fort_vehicle` and apply effects, sounds, or UI.

---

## ❌ Common Issues & Solutions
| Issue                         | Problem ❌                 | Solution ✅                                         |
|------------------------------|-----------------------------|--------------------------------------------------------|
| Sedan doesn’t spawn           | Device is disabled          | Call `Enable()` before `RespawnVehicle()`              |
| Events don’t fire             | Missing subscriptions       | Ensure `.Subscribe()` is used inside `OnBegin()`       |
| Player doesn’t enter auto    | No driver assigned          | Use `AssignDriver(agent)`                             |
| Sedan spawns at wrong place  | Bad transform setup         | Adjust in editor or use `TeleportTo()` at runtime     |

---

## 📌 Note
The **Prevalent sedan** is a balanced, civilian vehicle designed for **moderate speed and durability**. It is ideal for:
- Open-world exploration
- Mission transport
- NPC escort mechanics
- Driving minigames

