# 📘 vehicle_spawner_shopping_cart_device – UEFN Verse Device Documentation

## 🔹 Description
The `vehicle_spawner_shopping_cart_device` is a specialized spawner that allows you to configure and spawn a Shopping Cart vehicle in your Fortnite island. It inherits all core vehicle spawner functionality, letting you programmatically enable, disable, and respawn the vehicle, assign drivers, and respond to agent and vehicle events using Verse scripts or device wiring.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `vehicle_spawner_device`
- `vehicle_spawner_shopping_cart_device`

## 🛠️ Functions & Methods
| Name                 | Description                                               |
|----------------------|-----------------------------------------------------------|
| `Enable()`           | Enables the spawner device.                               |
| `Disable()`          | Disables the spawner so the shopping cart can no longer be spawned. |
| `RespawnVehicle()`   | Spawns (or respawns) the shopping cart—previous is destroyed. |
| `AssignDriver(agent)`| Instantly assigns the agent as the vehicle driver.        |
| `DestroyVehicle()`   | Destroys the spawned shopping cart if present.            |
| `GetTransform()`     | Gets world transform of the device.                       |
| `MoveTo()` / `TeleportTo()` | Animates or teleports device in the world.        |

## 🤩 Events (Data Members)
| Name                         | Type                          | When It Fires                                   |
|------------------------------|-------------------------------|--------------------------------------------------|
| `SpawnedEvent`              | `listenable(fort_vehicle)`    | When a shopping cart is spawned by the device.   |
| `DestroyedEvent`            | `listenable(tuple())`         | When the spawned shopping cart is destroyed.     |
| `AgentEntersVehicleEvent`   | `listenable(agent)`           | When an agent enters the shopping cart.          |
| `AgentExitsVehicleEvent`    | `listenable(agent)`           | When an agent exits the shopping cart.           |
| *Deprecated:*               |                               | Use the new events above instead.                |
| `VehicleSpawnedEvent`       | *(deprecated)*                |                                                  |
| `VehicleDestroyedEvent`     | *(deprecated)*                |                                                  |

## 🛋️ Configuration Options (Details Panel)
- **Vehicle to Spawn**: Shopping Cart (fixed for this device)
- **Enable at Game Start**: Whether spawner is active when the game begins
- **Respawn Handling**: Timer, auto, or manual respawn
- **Team Selection**: Restrict vehicle usage to specific teams
- **Spawn Effects**: Toggle VFX and SFX
- **Spawn Volume**: Set the spawn region
- **Max Vehicles**: Limit the number of simultaneous spawned carts

> Configure all options in the Details panel in UEFN after placing the device.

## 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Fortnite.com/Vehicles }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use vehicle_spawner_shopping_cart_device
shopping_cart_spawner_example := class(creative_device):

    @editable
    CartSpawner : vehicle_spawner_shopping_cart_device = vehicle_spawner_shopping_cart_device{}

    @editable
    SpawnButton : button_device = button_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        CartSpawner.SpawnedEvent.Subscribe(OnVehicleSpawned)
        CartSpawner.DestroyedEvent.Subscribe(OnVehicleDestroyed)
        CartSpawner.AgentEntersVehicleEvent.Subscribe(OnAgentEntersVehicle)
        CartSpawner.AgentExitsVehicleEvent.Subscribe(OnAgentExitsVehicle)

        SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnVehicleSpawned(Vehicle : fort_vehicle) : void =
        Print("Shopping cart spawned!")

    OnVehicleDestroyed() : void =
        Print("Shopping cart destroyed!")

    OnAgentEntersVehicle(Agent : agent) : void =
        Print("Agent entered shopping cart!")

    OnAgentExitsVehicle(Agent : agent) : void =
        Print("Agent exited shopping cart!")

    OnSpawnPressed(Agent : agent) : void =
        CartSpawner.RespawnVehicle()
        Print("Shopping cart respawned!")

    OnEnablePressed(Agent : agent) : void =
        CartSpawner.Enable()
        Print("Shopping cart spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        CartSpawner.Disable()
        Print("Shopping cart spawner disabled!")
```

## ⚡ How to Use in UEFN
1. **Add Devices to Your Level**
   - Drag `vehicle_spawner_shopping_cart_device` into your world.
   - Add three `button_device` instances (for Spawn, Enable, Disable).

2. **Configure Device Options**
   - In Details panel, set respawn type, active state, teams, vehicle count, VFX/SFX, etc.

3. **Create and Add Your Verse Device**
   - In Verse Explorer, right-click folder > Create New Verse File (e.g., `shopping_cart_spawner_example.verse`).
   - Paste code above and save.
   - Press Ctrl+Shift+B to build code.
   - Drag your Verse device into the world.

4. **Assign `@editable` References**
   - In Details panel of Verse device:
     - `CartSpawner` → Your shopping cart spawner device
     - `SpawnButton`, `EnableButton`, `DisableButton` → Your button devices

5. **Test Your Setup**
   - Press buttons in play mode to control Shopping Cart.
   - Watch log output for spawn/enter/exit/destroy events.

## 🧠 Best Practices
- Use events for gameplay triggers (e.g., rewards when player enters cart).
- Control respawn logic for timed/puzzle/minigame events.
- Use team settings to restrict access during game phases.

## ❌ Common Issues & Fixes
| Issue                | ❌ Example Problem                   | ✅ Solution                             | Explanation                                   |
|----------------------|----------------------------------------|---------------------------------------------|-----------------------------------------------|
| Cart does not spawn  | Did not call `.RespawnVehicle()`        | Use button/device to run respawn            | Manual or triggered spawn required            |
| Spawner isn’t responding | Device not enabled                  | Enable via `.Enable()` or set in Details    | Spawner must be active                        |
| Missing Verse references | Did not set `@editable` fields     | Assign all required fields in Details Panel | Verse won't function without these references |
| Events not firing    | No `.Subscribe()` in `OnBegin<override>()` | Add all event subscriptions properly    | Required to hook event handlers              |

## 💡 Note
- Great for races, creative games, vehicle mini-games, and obstacle challenges.
- Full control via Verse for logic-heavy scenarios.
- Use `AssignDriver(agent)` to force agent into the cart when needed.

