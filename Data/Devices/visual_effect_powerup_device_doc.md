## 📘 visual_effect_powerup_device – UEFN Verse Device Documentation

### 🔹 Description
The `visual_effect_powerup_device` is a type of powerup device in Unreal Editor for Fortnite (UEFN) that grants a **visual effect**—such as a **glow** or **outline**—to a player when picked up. It is commonly used for highlighting, marking, or buff-style visuals in gameplay. This device supports pickup detection, spawn/despawn control, and customizable durations using Verse scripting.

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `powerup_device`
- `visual_effect_powerup_device`

### 🧩 Events (Data Members)
| Name                | Type              | Description                                             |
|---------------------|-------------------|---------------------------------------------------------|
| ItemPickedUpEvent   | listenable(agent) | Fires when an agent (player) picks up the powerup. Returns the agent that triggered it. |

### 🛠️ Functions & Methods

#### 🎮 Powerup Management
| Function     | Description                                        |
|--------------|----------------------------------------------------|
| `Spawn()`    | Spawns the powerup into the world.                |
| `Despawn()`  | Removes the powerup from the world.               |
| `IsSpawned()`| Returns true if the powerup is currently spawned. |

#### ⚡ Pickup & Effect Control
| Function                          | Description                                                                                   |
|-----------------------------------|-----------------------------------------------------------------------------------------------|
| `Pickup(Agent: agent)`            | Applies the powerup's visual effect to a specific agent.                                     |
| `Pickup()`                        | Applies the effect to all players (if "Apply To" is set to All Players in the device settings). |
| `HasEffect(Agent: agent)`         | Returns whether the agent currently has the visual effect active.                            |
| `GetRemainingTime(Agent: agent)` | Returns remaining effect time on the agent. `-1.0` = infinite, `0.0` = no effect.             |
| `GetDuration()`                   | Gets the configured duration (in seconds).                                                    |
| `SetDuration(Duration: float)`   | Sets the effect duration. Does not affect already-applied effects.                           |

#### 📦 Transform & Positioning
| Function                         | Description                                                               |
|----------------------------------|---------------------------------------------------------------------------|
| `GetTransform()`                | Returns the device's transform. Always check `.IsValid()` first.         |
| `MoveTo(Position, Rotation, Duration)` | Smoothly moves the device to a new position.                         |
| `MoveTo(Transform, Duration)`   | Moves the device using a full transform struct.                          |
| `TeleportTo(...)`              | Instantly moves the device to a new location.                            |

### 🧰 Verse Usage Example
Here’s a simple script that spawns the powerup at game start and logs when a player picks it up:
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

powerup_effect_example := class(creative_device):

    @editable
    VFXPowerup : visual_effect_powerup_device = visual_effect_powerup_device{}

    OnBegin<override>()<suspends> : void =
        VFXPowerup.ItemPickedUpEvent.Subscribe(OnPickedUp)
        VFXPowerup.Spawn()

    OnPickedUp(Player : agent) : void =
        Print("Powerup picked up by: {Player}")
```

### 🔧 How to Use in UEFN
1. **Place the Device**
    - Drag a `visual_effect_powerup_device` into your level.
2. **Configure Details**
    - Set "Apply To", "Effect Duration", and "Effect Type" (e.g. glow, outline) in the Details panel.
3. **Optional: Add Verse Logic**
    - Create custom scripts for events like pickups.
4. **Build and Test**
    - Compile Verse (Ctrl+Shift+B), test interactions and effect behavior in-game.

### 🧠 Best Practices
- Use `Pickup(Agent)` to manually assign effects via buttons or triggers.
- Combine the effect with score boosts, ability unlocks, or UI prompts.
- Use `HasEffect()` and `GetRemainingTime()` to track and manage stateful logic.

### ❌ Common Issues & Solutions
| Issue                     | Problem ❌                                     | Solution ✅                                         |
|--------------------------|-----------------------------------------------|----------------------------------------------------|
| Effect doesn’t apply     | Powerup not spawned or "Apply To" misconfigured | Use `Spawn()`, check settings in Details panel     |
| Effect is permanent/too long | Duration misconfigured                        | Use `SetDuration()` or adjust in Details           |
| Players can’t pick up    | Pickup range or collision setup                | Adjust placement or pickup radius                  |

### 📎 Note
This device is **visual only**—it does not affect player stats or gameplay functionality by default. For stat-based powerups (e.g., speed, shield), use appropriate powerup device types or integrate with logic devices.

