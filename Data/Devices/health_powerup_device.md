📘 **health_powerup_device – UEFN Verse Device Documentation**

---

🔹 **Description**

The `health_powerup_device` is a powerup object designed to regenerate a player's health and/or shields when picked up. This device supports full control via Verse, including custom duration, magnitude of healing, spawn/despawn behavior, and tracking who picked it up. It can also be configured for negative effects like draining health using a negative magnitude.

---

🧱 **Verse Using Statement**
```verse
using { /Fortnite.com/Devices }
```

---

🔗 **Inheritance Hierarchy**
- `creative_object`
- `creative_device_base`
- `powerup_device`
- `health_powerup_device`

---

🧩 **Events (Data Members)**

| Event Name         | Type             | Description                                         |
|--------------------|------------------|-----------------------------------------------------|
| ItemPickedUpEvent  | listenable(agent)| Fires when the powerup is picked up by an agent.   |

---

🛠️ **Functions & Methods**

### 🎮 Powerup Application & Control

| Function         | Description                                                              |
|------------------|--------------------------------------------------------------------------|
| Spawn()          | Spawns the health powerup into the game world, making it collectible.    |
| Despawn()        | Removes the powerup from the world.                                      |
| Pickup(agent)    | Manually grants the powerup effect to a specific agent.                  |
| Pickup()         | Grants the effect to all players (requires “Apply To: All Players”).     |
| IsSpawned()      | Returns true if the powerup is currently active/spawned in the world.    |
| HasEffect(agent) | Checks if the given agent currently has the powerup effect applied.      |

### 🧪 Effect Parameters

| Function              | Description                                                                    |
|-----------------------|--------------------------------------------------------------------------------|
| SetDuration(seconds)  | Sets the effect duration (clamped to min/max). Doesn’t affect active effects.  |
| GetDuration()         | Returns the current effect duration.                                           |
| SetMagnitude(value)   | Sets healing/shield amount (positive) or damage (negative).                   |
| GetMagnitude()        | Returns current healing/damage value.                                          |
| GetRemainingTime(agent)| Returns time left on effect for an agent. -1.0 = infinite, 0.0 = not active. |

### 📦 Movement & Positioning

| Function              | Description                                                             |
|-----------------------|-------------------------------------------------------------------------|
| GetTransform()        | Gets the position, rotation, and scale of the device.                   |
| MoveTo(Position, Rotation, Duration) | Smoothly moves the device over time.                       |
| MoveTo(Transform, Duration) | Moves the device using a full transform struct.                   |
| TeleportTo(...)       | Instantly moves the device to a new location.                            |

---

🧰 **Verse Usage Example**
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

health_powerup_example := class(creative_device):

    @editable
    HealthPowerup : health_powerup_device = health_powerup_device{}

    OnBegin<override>()<suspends> : void =
        HealthPowerup.SetMagnitude(50.0)
        HealthPowerup.SetDuration(5.0)

        HealthPowerup.ItemPickedUpEvent.Subscribe(OnPickedUp)
        HealthPowerup.Spawn()
        Print("Health powerup spawned.")

    OnPickedUp(Player : agent) : void =
        Print("Health powerup picked up by: {Player}")
```

---

🔧 **How to Use in UEFN**

1. **Place the Device**
   - Add a `health_powerup_device` to your level from the Devices panel.

2. **Configure Healing Options**
   - Adjust magnitude, duration, respawn behavior, and visuals in the Details panel.

3. **Create and Connect Verse Script**
   - Use the provided example or create custom pickup/timing logic.

4. **Assign References**
   - Assign the `HealthPowerup` variable to your placed device in the script’s Details panel.

5. **Build and Playtest**
   - Compile (`Ctrl+Shift+B`), launch the experience, and test the powerup behavior.

---

🧠 **Best Practices**

- Combine with `button_device`, `trigger_device`, or `damage_zone_device` for interactive gameplay.
- Use `SetMagnitude()` to heal only health or shield (set in Details panel).
- Call `Pickup(agent)` after special events (e.g. kill streaks).
- Apply negative values to create harmful pickups.

---

❌ **Common Issues & Solutions**

| Issue                      | Problem                            | Solution                                    |
|----------------------------|-------------------------------------|---------------------------------------------|
| Powerup doesn’t spawn      | Device not called with `Spawn()`    | Use `Spawn()` in script or auto-spawn setting|
| Effect doesn’t apply       | Duration or magnitude is 0         | Set with `SetDuration()` and `SetMagnitude()`|
| Powerup doesn’t affect shield | Wrong setting in Details Panel     | Set to Health, Shield, or Both               |
| Script doesn’t trigger     | Event not subscribed                | Use `.Subscribe()` for `ItemPickedUpEvent`   |

---

📌 **Note**

This device focuses on health/shield regeneration. For combat modifiers, movement boosts, or class changes, pair with other devices or systems.

