## end_game_device – UEFN Verse Device Documentation

### 🔹 Description
The `end_game_device` is used to end the current round or the entire game based on gameplay logic or scripted conditions. It is a crucial tool for implementing custom win/loss mechanics, round-based game modes, score-dependent matches, or scripted endings.

This device allows creators to end the game programmatically using Verse or other device signals (e.g., upon objective completion, timer expiration, or reaching a specific score).

✅ **Configurable:** Ends either the current round or the entire match based on how it is triggered.

---

### 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
| Class                    | Description                                      |
|-------------------------|--------------------------------------------------|
| `creative_object`       | Base class for props and devices.               |
| `creative_device_base`  | Adds general device control functionality.      |
| `end_game_device`       | Controls end-of-game or end-of-round behavior.  |

---

### 🔁 Main Event
This device does **not** expose any listenable events. It is activated directly via Verse or from signals emitted by other devices.

---

### 🧰 Core Methods
| Method Signature                | Description                                                            |
|--------------------------------|------------------------------------------------------------------------|
| `Activate(): void`             | Triggers the end of the game or round based on island settings.       |
| `Enable(): void`               | Enables the device, allowing activation.                              |
| `Disable(): void`              | Disables the device to prevent game-ending actions.                   |
| `IsEnabled(): logic`           | Returns `true` if the device is currently enabled.                    |
| `GetTransform(): transform`    | Gets the device's transform—used for positioning if needed.           |
| `TeleportTo(...) / MoveTo(...)`| Moves or animates the device, though not commonly used.               |

---

### ⚙️ Setup in UEFN Editor
In the Details panel:
- **⏹️ Game End Type** – Choose whether to end the round or the entire game.
- **🎯 Activation Conditions** – Define how to activate (e.g., triggers, buttons, Verse logic).
- **🔄 Reset Behavior** – Configure restart or phase load behavior with round settings.
- **✅ UI/Elimination Options** – Customize what players see or experience when the game ends.

---

### 🚦 Common Usage: Step-by-Step Example
```verse
using { /Fortnite.com/Devices }

end_game_controller := class(
    @editable EndGameDevice: end_game_device
):

    OnBegin<override>() :=
        EndGameDevice.Enable()

    TriggerGameOver(): void =
        if (EndGameDevice.IsEnabled()):
            EndGameDevice.Activate()
```

**Typical Activation Scenarios:**
- All objectives completed
- A score threshold is reached
- Timer expires
- Player enters victory zone

---

### ❌ Incorrect Usage Examples and Fixes
| Issue                           | ❌ Wrong Example      | ✅ Correct Example         | Explanation                                             |
|--------------------------------|------------------------|----------------------------|---------------------------------------------------------|
| Calling `Activate()` directly  | `Activate()`           | Call `Enable()` before it  | The device must be enabled before activation.           |
| Expecting round end vs game    | Misconfigured end type | Set correct end type       | Properly configure in the editor (round vs game).       |
| No response on trigger         | No signal sent         | Connect device or call it  | Must be called via Verse or device signal.              |

---

### 🧠 Best Practices
- Use for advanced win/loss logic beyond built-in game modes.
- Place multiple `end_game_device` instances for different game outcomes.
- Ideal with devices like:
  - `trigger_device` (e.g., finish zone)
  - `score_manager_device` (e.g., score goal met)
  - `elimination_manager_device` (e.g., last team standing)
- Optionally pair with:
  - `elimination_feed_device`
  - `hud_message_device` for visual end alerts

**Perfect For:**
- Custom competitive games with unique win conditions
- Puzzle/escape maps that end on objective completion
- Timed survival or boss fight challenges
- Minigames or tournaments with round-based logic

