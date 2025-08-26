## UEFN Verse Device Documentation: `powerup_device`

---

### 🔹 Description

The `powerup_device` is the foundational class for all powerup-related devices in UEFN, such as health, stat, and effect powerups. It provides the core interface for spawning, granting, and tracking powerup pickups. A key component of this class is the `ItemPickedUpEvent`, which is fired when a player collects the powerup. This class or its subclasses are ideal for creating boost mechanics, timed effects, and stat-modifying pickups.

---

### 🧱 Verse Using Statement

```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy

- `creative_object`
- `creative_device_base`
- `powerup_device`
  - `health_powerup_device`
  - `stat_powerup_device`
  - *(other specific powerup devices)*

---

### 🧩 Data Members (Events)

| Name                | Type                | Description                                            |
| ------------------- | ------------------- | ------------------------------------------------------ |
| `ItemPickedUpEvent` | `listenable(agent)` | Fired when the powerup is picked up by an agent/player |

---

### 🛠️ Functions & Methods

| Name                        | Description                                                      |
| --------------------------- | ---------------------------------------------------------------- |
| `Spawn()`                   | Spawns the powerup item into the experience.                     |
| `Despawn()`                 | Removes the powerup from the world.                              |
| `Pickup(agent)`             | Grants the powerup effect to the specified agent.                |
| `Pickup()`                  | Grants to all players if device is configured for "All Players". |
| `SetMagnitude(float)`       | Sets the effect strength (e.g., health/shield/stat boost).       |
| `GetMagnitude()`            | Retrieves the current effect strength.                           |
| `SetDuration(float)`        | Sets the effect duration in seconds.                             |
| `GetDuration()`             | Gets the current configured effect duration.                     |
| `GetRemainingTime(agent)`   | Returns the remaining time of effect for a specific agent.       |
| `HasEffect(agent)`          | Checks if an agent currently has the effect active.              |
| `IsSpawned()`               | Returns whether the item is currently spawned in the world.      |
| `GetTransform()`            | Gets the item's current transform (position, rotation, scale).   |
| `MoveTo()` / `TeleportTo()` | Moves or teleports the device.                                   |

---

### 🎛 Configuration Options (Details Panel)

| Option              | Description                                                            |
| ------------------- | ---------------------------------------------------------------------- |
| Magnitude           | Amount of effect (health, stat, etc.) applied or removed.              |
| Effect Duration     | Duration the effect is active ("0" = instant, "-1" = permanent).       |
| Apply To            | Choose between All Players, Triggering Player, or specific team/class. |
| Auto Respawn        | Automatically respawn the powerup after it is picked up.               |
| Pickup Visual/FX    | Customize appearance, VFX, and sound.                                  |
| Spawn on Game Start | Whether the powerup is visible at game start or spawned via Verse.     |
| Enable/Disable      | Dynamically turn the device on or off.                                 |

---

### 🧩 Events

| Event               | Description                                                                     |
| ------------------- | ------------------------------------------------------------------------------- |
| `ItemPickedUpEvent` | Fires when a player picks up the powerup, passing the agent/player as argument. |

---

### 🧰 Verse Usage Example

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use powerup_device
powerup_device_example := class(creative_device):

    @editable
    PowerupDevice : health_powerup_device = health_powerup_device{}

    @editable
    SpawnButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to powerup pickup event
        PowerupDevice.ItemPickedUpEvent.Subscribe(OnPowerupPickedUp)

        # Subscribe to control button
        SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)

    # Event handler for powerup pickup
    OnPowerupPickedUp(Agent : agent) : void =
        Print("Powerup picked up by agent!")

    # Button control handler
    OnSpawnPressed(Agent : agent) : void =
        PowerupDevice.Spawn()
        Print("Powerup spawned!")
```

---

### How to Use in UEFN

1. **Place Your Powerup Device**

   - From the Content Browser, add a powerup (e.g., `health_powerup`, `stat_powerup`) to your map.

2. **Configure Device**

   - In the Details panel, configure settings such as magnitude, duration, apply target, VFX, and respawn.

3. **(Optional) Add and Configure a Verse Device**

   - In Verse Explorer: Right-click folder → Create New Verse File → Paste sample code → Save.
   - Build Verse Code (Ctrl+Shift+B) until "Build Succeeded".

4. **Assign Devices as @editable References**

   - Select the Verse device and assign `PowerupDevice` and `SpawnButton` in the Details panel.

5. **Test and Iterate**

   - Activate the button to spawn the powerup. Observe pickup behavior and adjust logic as needed.

---

### 🧠 Best Practices

- Use `SetMagnitude()` and `SetDuration()` for scaling effects or timed buffs.
- Implement advanced behavior such as conditional respawning or UI feedback using Verse scripting.
- Utilize `ItemPickedUpEvent` to trigger rewards, mission progress, or achievements.

---

### ❌ Common Issues & Fixes

| Issue                | Cause/Mistake                       | Solution                                   |
| -------------------- | ----------------------------------- | ------------------------------------------ |
| Item doesn’t spawn   | Did not call `.Spawn()`             | Call `.Spawn()` or enable spawn on start   |
| No event triggers    | Didn’t `.Subscribe()` to event      | Use `.Subscribe()` for `ItemPickedUpEvent` |
| Config doesn’t apply | Config set but not saved or applied | Save settings and restart play session     |

---

### Notes

- Use `powerup_device` directly for generic effects, or subclass for custom logic (e.g., `health_powerup_device`).
- All pickup logic and event handling are unified through `ItemPickedUpEvent` and shared functions.

