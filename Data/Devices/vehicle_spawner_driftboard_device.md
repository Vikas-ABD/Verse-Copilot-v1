📘 **vehicle_spawner_driftboard_device – UEFN Verse Device Documentation**

---

🔹 **Description**

The `vehicle_spawner_driftboard_device` is a specialized spawner for the Driftboard—a fast, one-person hoverboard-like vehicle in Fortnite. This device enables you to spawn, destroy, assign riders, and track Driftboard activity using Verse. It supports gameplay event handling like entry, exit, spawn, and destruction of the vehicle.

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
- `vehicle_spawner_driftboard_device`

---

🧩 **Events (Data Members)**
| Name                     | Type                    | Description                                                    |
|--------------------------|-------------------------|----------------------------------------------------------------|
| AgentEntersVehicleEvent  | listenable(agent)       | Fires when an agent enters the Driftboard.                     |
| AgentExitsVehicleEvent   | listenable(agent)       | Fires when an agent exits the Driftboard.                      |
| DestroyedEvent           | listenable()            | Fires when the Driftboard is destroyed. (Preferred usage)      |
| SpawnedEvent             | listenable(fort_vehicle)| Fires when the Driftboard is spawned or respawned.             |
| VehicleDestroyedEvent    | listenable()            | ❌ Deprecated – use DestroyedEvent.                            |
| VehicleSpawnedEvent      | listenable(fort_vehicle)| ❌ Deprecated – use SpawnedEvent.                              |

---

🛠️ **Functions & Methods**

| Function Name       | Description                                                             |
|---------------------|-------------------------------------------------------------------------|
| Enable()            | Enables the spawner so that the Driftboard can be spawned.              |
| Disable()           | Disables the spawner, preventing new spawns.                            |
| RespawnVehicle()    | Destroys the current Driftboard and spawns a new one.                   |
| DestroyVehicle()    | Destroys the currently spawned Driftboard (if it exists).               |
| AssignDriver(agent) | Assigns a player to the Driftboard as the driver.                       |
| GetTransform()      | Returns the spawner’s position, rotation, and scale. Use IsValid() check first. |
| MoveTo(Position, Rotation, Duration) | Smoothly moves the spawner to a new location.           |
| MoveTo(Transform, Duration)         | Moves the spawner using a full transform struct.         |
| TeleportTo(...)     | Instantly teleports the spawner to a given position/rotation.           |

---

🧰 **Verse Usage Example**

This sample Verse script spawns a Driftboard on game start and prints messages when players get on or off the board:
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

driftboard_example := class(creative_device):

    @editable
    DriftboardSpawner : vehicle_spawner_driftboard_device = vehicle_spawner_driftboard_device{}

    OnBegin<override>()<suspends> : void =
        DriftboardSpawner.AgentEntersVehicleEvent.Subscribe(OnEnter)
        DriftboardSpawner.AgentExitsVehicleEvent.Subscribe(OnExit)

        DriftboardSpawner.Enable()
        DriftboardSpawner.RespawnVehicle()

    OnEnter(Player : agent) : void =
        Print("Player entered the Driftboard: {Player}")

    OnExit(Player : agent) : void =
        Print("Player exited the Driftboard: {Player}")
```

---

🔧 **How to Use in UEFN**

1. **Place the Device**
    - Add a `vehicle_spawner_driftboard_device` to your level from the Devices panel.

2. **Configure Options**
    - Adjust speed, jump, boost, or respawn settings via the Details panel.

3. **Create a Verse Script**
    - Use the script above or write custom logic for Driftboard interactions.

4. **Assign Device Reference**
    - In your Verse device's Details panel, link `DriftboardSpawner` to the placed spawner.

5. **Build and Test**
    - Compile Verse (`Ctrl+Shift+B`) and test player interaction in your experience.

---

🧠 **Best Practices**

- Use `AssignDriver()` to auto-place players on the Driftboard, such as after pressing a button or entering a trigger.
- Pair with `vehicle_mod_box_spawner_device` to let players mod their Driftboard mid-game.
- Use `DestroyedEvent` to respawn automatically or trigger consequences (like losing a life or restarting a lap).

---

❌ **Common Issues & Solutions**

| Issue                        | Problem ❌              | Solution ✅                                       |
|-----------------------------|-------------------------|--------------------------------------------------|
| Driftboard doesn’t spawn    | Device disabled         | Use `Enable()` before `RespawnVehicle()`         |
| Agent doesn’t mount         | Driver not assigned     | Use `AssignDriver(agent)`                        |
| No feedback on interaction  | Events not subscribed   | Use `.Subscribe()` in `OnBegin()`                |
| Driftboard stuck/misplaced  | Transform issues        | Use `TeleportTo()` to reposition reliably        |

---

📎 **Note**

The Driftboard is agile and fast, making it ideal for traversal, racing, trick systems, or hover-based gameplay. If you want to add boost pads, timed challenges, or vehicle health tracking, let me know — I can help build that with Verse logic!

