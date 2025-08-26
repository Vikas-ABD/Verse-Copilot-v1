# vehicle\_spawner\_baller\_device – UEFN Verse Device Documentation

## 🔹 Description

The `vehicle_spawner_baller_device` is a specialized spawner for the **Baller** vehicle—a one-person, rolling and grappling mobility vehicle in **Fortnite**. This device allows you to spawn, manage, and track Ballers via **Verse**, including driver assignment, energy management, and event-driven responses to vehicle use, destruction, or energy depletion.

## 🛠️ Verse Using Statement

```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy

- `creative_object`
- `creative_device_base`
- `vehicle_spawner_device`
- `vehicle_spawner_baller_device`

## 🧹 Events (Data Members)

| Name                    | Type                      | Description                                                                       |
| ----------------------- | ------------------------- | --------------------------------------------------------------------------------- |
| AgentEntersVehicleEvent | listenable(agent)         | Fires when an agent enters the Baller.                                            |
| AgentExitsVehicleEvent  | listenable(agent)         | Fires when an agent exits the Baller.                                             |
| DestroyedEvent          | listenable()              | Fires when the Baller is destroyed. Use this instead of deprecated one.           |
| OutOfEnergyEvent        | listenable()              | Fires when the Baller runs out of energy.                                         |
| SpawnedEvent            | listenable(fort\_vehicle) | Fires when the Baller is spawned or respawned. Preferred over deprecated version. |
| VehicleDestroyedEvent   | listenable()              | ❌ Deprecated. Use `DestroyedEvent`.                                               |
| VehicleSpawnedEvent     | listenable(fort\_vehicle) | ❌ Deprecated. Use `SpawnedEvent`.                                                 |

## 🛠️ Functions & Methods

| Function Name                          | Description                                                                |
| -------------------------------------- | -------------------------------------------------------------------------- |
| `Enable()` / `Disable()`               | Enables or disables the spawner.                                           |
| `RespawnVehicle()`                     | Destroys current Baller and spawns a new one.                              |
| `DestroyVehicle()`                     | Destroys the currently spawned Baller, if any.                             |
| `AssignDriver(agent)`                  | Assigns an agent to immediately enter the Baller as driver.                |
| `RefillEnergy()`                       | Refills the Baller’s energy (used for grappling functions).                |
| `GetTransform()`                       | Returns the transform of the device. Use `IsValid()` check before calling. |
| `MoveTo(Position, Rotation, Duration)` | Smoothly moves the device to a new location over time.                     |
| `MoveTo(Transform, Duration)`          | Moves device using a full transform struct.                                |
| `TeleportTo(...)`                      | Instantly moves the device to a specified location and orientation.        |

## 🔧 Verse Usage Example

Here’s a sample script that spawns a Baller on game start and listens for when a player enters and when the Baller runs out of energy:

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

baller_example := class(creative_device):

    @editable
    BallerSpawner : vehicle_spawner_baller_device = vehicle_spawner_baller_device{}

    OnBegin<override>()<suspends> : void =
        BallerSpawner.AgentEntersVehicleEvent.Subscribe(OnEnter)
        BallerSpawner.OutOfEnergyEvent.Subscribe(OnOutOfEnergy)

        BallerSpawner.Enable()
        BallerSpawner.RespawnVehicle()

    OnEnter(Player : agent) : void =
        Print("Player entered the Baller: {Player}")

    OnOutOfEnergy() : void =
        Print("Baller ran out of energy!")
        BallerSpawner.RefillEnergy()
        Print("Energy refilled.")
```

## 🔧 How to Use in UEFN

1. **Place the Device**
   - Drag a `vehicle_spawner_baller_device` into your level.
2. **Configure the Baller**
   - In the *Details* panel, adjust fuel, grapple settings, respawn behavior, etc.
3. **Assign to Verse**
   - In your Verse device's *Details* panel, assign your `BallerSpawner` reference.
4. **Write or Paste Verse Logic**
   - Use the example script above or create custom logic.
5. **Build and Test**
   - Compile Verse (`Ctrl+Shift+B`), then test your Baller’s interaction in-game.

## 🧠 Best Practices

- Use `RefillEnergy()` to support battery recharge stations or power pickups.
- Use `AssignDriver()` after spawn for racing systems, tutorials, or scripted vehicle handoffs.
- Use `OutOfEnergyEvent` to force pit stops, cooldowns, or disable functions.
- Prefer `SpawnedEvent` and `DestroyedEvent` over deprecated ones for forward compatibility.

## ❌ Common Issues & Solutions

| Issue                              | Problem ❌           | Solution ✅                                   |
| ---------------------------------- | ------------------- | -------------------------------------------- |
| Baller not spawning                | Device disabled     | Call `Enable()` then `RespawnVehicle()`      |
| Energy depleted and can’t continue | No refill logic     | Use `RefillEnergy()`                         |
| No event triggers                  | Did not subscribe   | Ensure `.Subscribe()` is used in `OnBegin()` |
| Agent not entering vehicle         | Driver not assigned | Use `AssignDriver(agent)` if required        |

## 📌 Note

The Baller vehicle is unique in that it has **limited energy** for grappling and may need **manual energy management** in longer experiences. It’s excellent for **parkour-style navigation** or **puzzle traversal systems**.

---

Let me know if you’d like a system that recharges the Baller with a button, gives a boost, or combines it with powerups!

