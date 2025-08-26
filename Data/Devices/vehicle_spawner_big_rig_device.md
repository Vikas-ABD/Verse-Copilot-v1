# UEFN Verse Device Documentation: `vehicle_spawner_big_rig_device`

## 📘 Description
The `vehicle_spawner_big_rig_device` is a specialized spawner designed for the **Mudflap semi-truck** (Big Rig) in **Fortnite Creative (UEFN)**. This heavy-duty vehicle supports multiple passengers and is ideal for:
- Large-scale transport
- Destruction-based game modes
- Convoy and escort missions

The device can be fully controlled using **Verse scripting**, enabling spawning, destruction, driver assignment, and responding to key vehicle-related events.

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
- `vehicle_spawner_big_rig_device`

---

## 📙 Events (Data Members)
| Event Name                 | Type                     | Description                                       |
|---------------------------|--------------------------|---------------------------------------------------|
| AgentEntersVehicleEvent   | listenable(agent)        | Fires when an agent enters the Mudflap.          |
| AgentExitsVehicleEvent    | listenable(agent)        | Fires when an agent exits the Mudflap.           |
| DestroyedEvent            | listenable()             | Fires when the Mudflap is destroyed. (Preferred) |
| SpawnedEvent              | listenable(fort_vehicle) | Fires when the Mudflap is spawned. (Preferred)   |
| VehicleDestroyedEvent     | listenable()             | ❌ Deprecated. Use `DestroyedEvent`.            |
| VehicleSpawnedEvent       | listenable(fort_vehicle) | ❌ Deprecated. Use `SpawnedEvent`.              |

---

## 🛠️ Functions & Methods
| Function              | Description                                                              |
|----------------------|--------------------------------------------------------------------------|
| `Enable()`           | Enables the device, allowing vehicles to spawn.                          |
| `Disable()`          | Disables the device and prevents spawns.                                |
| `RespawnVehicle()`   | Destroys any current Mudflap and spawns a new one.                       |
| `DestroyVehicle()`   | Destroys the spawned Mudflap.                                            |
| `AssignDriver(agent)`| Forces the specified agent to enter the truck as the driver.            |
| `GetTransform()`     | Returns the transform of the spawner. Requires `IsValid()` check first. |
| `MoveTo(Position, Rotation, Duration)` | Smoothly moves the spawner to a new position and rotation. |
| `MoveTo(Transform, Duration)` | Moves the spawner using a full transform.                  |
| `TeleportTo(...)`    | Instantly relocates the spawner to a new position/rotation.             |

---

## 🪠 Verse Usage Example
This example spawns the Mudflap on game start and logs vehicle entry and exit:
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

big_rig_example := class(creative_device):

    @editable
    BigRigSpawner : vehicle_spawner_big_rig_device = vehicle_spawner_big_rig_device{}

    OnBegin<override>()<suspends> : void =
        BigRigSpawner.AgentEntersVehicleEvent.Subscribe(OnEnter)
        BigRigSpawner.AgentExitsVehicleEvent.Subscribe(OnExit)

        BigRigSpawner.Enable()
        BigRigSpawner.RespawnVehicle()

    OnEnter(Player : agent) : void =
        Print("Player entered the Mudflap: {Player}")

    OnExit(Player : agent) : void =
        Print("Player exited the Mudflap: {Player}")
```

---

## 🛠️ How to Use in UEFN
1. **Place the Device**
   - Drag and drop `vehicle_spawner_big_rig_device` into your island.

2. **Configure Settings**
   - In the Details panel, customize:
     - Respawn timing
     - Fuel amount
     - Health
     - Team ownership

3. **Create and Assign Verse Script**
   - Use the example above or create custom logic.

4. **Build & Test**
   - Compile Verse (`Ctrl+Shift+B`) and enter playtest mode.

---

## 🧠 Best Practices
- Use `AssignDriver()` to programmatically place players in the vehicle.
- Combine with `vehicle_mod_box_spawner_device` to add upgrades (e.g., turbo, shields).
- Monitor `DestroyedEvent` for:
  - Vehicle respawn
  - Score updates
  - Triggering missions or eliminations

---

## ❌ Common Issues & Solutions
| Issue                                | Problem                  | Solution                                  |
|-------------------------------------|--------------------------|-------------------------------------------|
| Truck doesn’t appear                | Device not enabled       | Use `Enable()` before `RespawnVehicle()`  |
| Players not entering automatically  | Driver not assigned      | Use `AssignDriver(agent)`                 |
| Events not firing                   | Subscriptions missing    | Call `.Subscribe()` inside `OnBegin()`    |
| Truck spawns at wrong location      | Incorrect transform      | Use `TeleportTo()` or fix placement       |

---

## 📌 Notes
The **Mudflap (Big Rig)** is great for:
- Destruction-focused missions
- Mobile cover for teams
- Escort gameplay
- Offensive or defensive moving objectives

Use it to bring impact, chaos, or strategy to your UEFN creations!

