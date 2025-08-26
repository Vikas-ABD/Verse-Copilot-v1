# vehicle_spawner_atk_device – UEFN Verse Device Documentation

## 🔹 Description
The `vehicle_spawner_atk_device` is a specialized spawner for ATKs (All Terrain Karts) in Fortnite. It allows full control over the spawn, destruction, and management of an ATK vehicle. You can interact with this device via Verse to dynamically spawn or destroy the kart, assign drivers, and respond to in-game events like entering, exiting, or destroying the vehicle.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `vehicle_spawner_device`
- `vehicle_spawner_atk_device`

## 🦩 Events (Data Members)
| Name                    | Type                      | Description                                               |
|-------------------------|---------------------------|-----------------------------------------------------------|
| AgentEntersVehicleEvent | listenable(agent)         | Fired when an agent enters the ATK.                      |
| AgentExitsVehicleEvent  | listenable(agent)         | Fired when an agent exits the ATK.                       |
| DestroyedEvent          | listenable()              | Fired when the ATK is destroyed.                         |
| SpawnedEvent            | listenable(fort_vehicle)  | Fired when the ATK is spawned or respawned.             |
| VehicleDestroyedEvent   | listenable()              | ❌ Deprecated. Use `DestroyedEvent`.                  |
| VehicleSpawnedEvent     | listenable(fort_vehicle)  | ❌ Deprecated. Use `SpawnedEvent`.                    |

## 🛠️ Functions & Methods
| Function Name       | Description                                                            |
|---------------------|------------------------------------------------------------------------|
| Enable()            | Enables the spawner, allowing the ATK to spawn.                        |
| Disable()           | Disables the spawner; no vehicle will be spawned.                      |
| RespawnVehicle()    | Destroys any existing vehicle and spawns a new ATK.                    |
| DestroyVehicle()    | Destroys the current ATK if one exists.                                |
| AssignDriver(agent) | Assigns a specific agent as the driver of the spawned ATK.             |
| GetTransform()      | Returns the transform of the spawner (position, rotation, scale). Use `IsValid()` check first. |
| MoveTo(Position, Rotation, Duration) | Smoothly moves the spawner to a new position and rotation. |
| MoveTo(Transform, Duration)         | Moves the spawner using a full transform.                |
| TeleportTo(...)     | Instantly moves the spawner to a new location.                         |

## 🪠 Verse Usage Example
A simple script that respawns the ATK and logs when a player enters or exits:

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

atk_vehicle_example := class(creative_device):

    @editable
    ATKSpawner : vehicle_spawner_atk_device = vehicle_spawner_atk_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to events
        ATKSpawner.AgentEntersVehicleEvent.Subscribe(OnEntered)
        ATKSpawner.AgentExitsVehicleEvent.Subscribe(OnExited)

        # Ensure the device is enabled and spawn a vehicle
        ATKSpawner.Enable()
        ATKSpawner.RespawnVehicle()

    OnEntered(Player : agent) : void =
        Print("Agent entered the ATK: {Player}")

    OnExited(Player : agent) : void =
        Print("Agent exited the ATK: {Player}")
```

## 🛠️ How to Use in UEFN
1. **Place the Device**
    - Drag a `vehicle_spawner_atk_device` into your level from the Devices tab.
2. **Configure in Details Panel**
    - Set respawn rules, custom settings, driver permissions, etc.
3. **Create Verse Script**
    - Use the example above or customize logic to control the ATK.
4. **Assign Reference**
    - In the Details panel of your Verse device, assign `ATKSpawner` to the ATK spawner placed in the world.
5. **Build & Test**
    - Compile Verse code and test interactions such as entering/exiting or respawning.

## 🧠 Best Practices
- Use `AssignDriver()` after spawning for race starts, team logic, or tutorials.
- Combine with `vehicle_mod_box_spawner_device` to apply upgrades to spawned ATKs.
- Use the `SpawnedEvent` to retrieve and modify the `fort_vehicle` object dynamically after spawning.
- Prefer the non-deprecated event names (`SpawnedEvent`, `DestroyedEvent`) for forward compatibility.

## ❌ Common Issues & Solutions
| Issue                         | Problem                            | Solution                                  |
|-------------------------------|-------------------------------------|-------------------------------------------|
| Vehicle doesn't spawn         | Device is disabled                  | Use `Enable()` and then `RespawnVehicle()`|
| No response to events         | Subscriptions missing               | Ensure `.Subscribe()` is used in `OnBegin()`|
| Agent not driving after spawn | Agent not assigned                  | Use `AssignDriver(agent)` after spawn     |
| Vehicle reappears immediately | Respawn delay settings in Details panel | Adjust auto-respawn logic in editor   |

## 📌 Note
This device spawns **only the ATK (All Terrain Kart)** vehicle. For other vehicles (Baller, Rocket League car, etc.), use their respective `vehicle_spawner_*_device`.

---

Let me know if you want to combine this with triggered spawns, mod integration, or multiplayer logic!

