## race_manager_device – UEFN Verse Device Documentation

### 🔹 Description
The `race_manager_device` is used to coordinate and control racing game modes in Fortnite Creative. It works in conjunction with `race_checkpoint_device` to manage laps, race progression, and timing.

This device provides essential functionality for:
- Starting and ending races
- Tracking lap completions
- Emitting events when laps or the full race are completed
- Supporting advanced racing logic, like multi-lap competitions or timed challenges

### 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
| Class | Description |
|-------|-------------|
| `creative_object` | Base for all props/devices. |
| `creative_device_base` | Adds enabling/disabling and device control logic. |
| `race_manager_device` | Manages race logic and events for race gameplay. |

### 🪀 Listenable Events
| Event Name | Type | Description |
|------------|------|-------------|
| `RaceBeganEvent` | listenable(agent) | Fires when an agent starts the race. |
| `FirstLapCompletedEvent` | listenable(agent) | Fires when a player finishes their first lap. |
| `LapCompletedEvent` | listenable(agent) | Fires each time a player completes a lap. |
| `RaceCompletedEvent` | listenable(agent) | Fires when a player finishes the race. |

### 🪰 Core Methods
| Method Signature | Description |
|------------------|-------------|
| `Begin(): void` | Starts the race — agents can begin progressing through checkpoints. |
| `End(): void` | Ends the race manually. No further lap progress is recorded. |
| `Enable(): void` | Activates the device for use. |
| `Disable(): void` | Deactivates the device and halts its functionality. |
| `GetTransform(): transform` | Returns the device’s transform (position, rotation, scale). |
| `MoveTo(...) / TeleportTo(...)` | Move or reposition the device in the world. Not usually needed for race logic. |

### ⚙️ Configuration Notes
- **Use with `race_checkpoint_device`**: Checkpoints must be linked and configured to define the race path.
- **Laps & Timing**: Number of laps and any race conditions are set in the UEFN editor under race device options.
- **Team-Based Support**: Races can be individual or team-based depending on your island settings.

### 🚦 Common Usage: Step-by-Step Example
```verse
using { /Fortnite.com/Devices }

race_controller := class(
    @editable RaceManager: race_manager_device
):

    OnBegin<override>()<suspends>: void =
        RaceManager.Enable()
        RaceManager.RaceBeganEvent.Subscribe(OnRaceStart)
        RaceManager.FirstLapCompletedEvent.Subscribe(OnFirstLap)
        RaceManager.LapCompletedEvent.Subscribe(OnLap)
        RaceManager.RaceCompletedEvent.Subscribe(OnRaceFinish)

    OnRaceStart(Player: agent): void =
        Print("Race started for: {Player}")

    OnFirstLap(Player: agent): void =
        Print("First lap completed by: {Player}")

    OnLap(Player: agent): void =
        Print("Lap completed by: {Player}")

    OnRaceFinish(Player: agent): void =
        Print("Race finished by: {Player}")
```

### 🧠 Best Practices
- Use `Begin()` to start the race once all players are ready or after a countdown.
- Use `RaceCompletedEvent` to trigger post-race logic: victory message, teleport, item reward, etc.
- Combine with `hud_message_device`, `trigger_device`, and `score_manager_device` for full race UIs and scoring systems.
- You can have multiple `race_manager_device` instances to support different race types or difficulty levels.
- Always pair with `race_checkpoint_device` to define the course and enable lap tracking.

### ❌ Incorrect Usage Examples and How to Fix
| Issue | ❌ Wrong | ✅ Fix | Explanation |
|-------|-------------|----------|-------------|
| Not enabling the device | `RaceManager.Begin()` has no effect | Call `RaceManager.Enable()` before starting the race | Device must be enabled first |
| Forgetting to use checkpoints | Only using manager device | Must place and configure `race_checkpoint_device` in sequence | Checkpoints are required for lap tracking |
| Expecting `RaceCompletedEvent` without race start | Listening for completion too early | Use `Begin()` to start race tracking | Race must start before tracking |

### 🌟 Great for:
- Time trials and leaderboard races
- Multiplayer racing games
- Lap-based competitions and elimination laps
- Obstacle courses and speed runs
- Skill challenges that track movement and pacing

