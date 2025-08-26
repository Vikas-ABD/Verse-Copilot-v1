## UEFN Verse Device Documentation: `analytics_device`

### 🔹 Description
The `analytics_device` is used to track gameplay events involving agents (players) for custom analytics, helping creators log key interactions on their island. This includes zone entries, objective completions, item pickups, and more. The collected data supports gameplay analysis, progression tracking, and player behavior insights.

Tracking is manually triggered via Verse using the `TrackAgentEvent()` method.

### 🧱 Required Imports
```verse
using { /Fortnite.com/Devices }
```

### 🧬 Inheritance Hierarchy
| Class | Description |
|-------|-------------|
| `creative_object` | Base class for props and devices. |
| `creative_device_base` | Adds device logic and control. |
| `analytics_device` | Enables agent-based analytics event logging. |

### 🔁 Main Event
This device does **not** expose listenable events. It relies on manual calls to its core method.

### 🧰 Core Methods
| Method | Description |
|--------|-------------|
| `TrackAgentEvent(Player: agent): void` | Logs an analytics event for the given player. Used to track progress or key interactions. |
| `Enable(): void` | Enables the device to start tracking. |
| `Disable(): void` | Disables the device, halting tracking. |
| `IsEnabled(): logic` | Returns current enable status. |
| `GetTransform(): transform` | Returns the device's transform in cm. Use `IsValid()` before calling. |
| `TeleportTo(...) / MoveTo(...)` | Repositioning methods; rarely needed for analytics. |

### ⚙️ Setup in UEFN Editor
- No special visual configuration required.
- Place the device in the level.
- Assign a name for unique identification.
- Control the device via Verse scripting.

### 🚦 Step-by-Step Usage Example
```verse
using { /Fortnite.com/Devices }

analytics_tracker := class(
    @editable AnalyticsDevice: analytics_device
):

    OnBegin<override>() :=
        AnalyticsDevice.Enable()

    TrackPlayerMilestone(Player: agent): void =
        if (AnalyticsDevice.IsEnabled()):
            AnalyticsDevice.TrackAgentEvent(Player)
```
Use cases for `TrackAgentEvent()` include:
- Objective completions
- Match wins
- Zone entries
- Item pickups

### 🧰 Extended Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

analytics_tracker := class(creative_device):

    @editable
    AnalyticsDevice : analytics_device = analytics_device{}

    @editable
    TrackButton : button_device = button_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        TrackButton.InteractedWithEvent.Subscribe(OnButtonPressed)
        EnableButton.InteractedWithEvent.Subscribe(OnEnableAnalytics)
        DisableButton.InteractedWithEvent.Subscribe(OnDisableAnalytics)

    OnButtonPressed(Agent : agent) : void =
        Print("Button pressed by player")
        AnalyticsDevice.TrackAgentEvent(Agent)

    OnEnableAnalytics(Agent : agent) : void =
        AnalyticsDevice.Enable()
        Print("Analytics tracking enabled")

    OnDisableAnalytics(Agent : agent) : void =
        AnalyticsDevice.Disable()
        Print("Analytics tracking disabled")
```
**Explanation:**
- Place the `analytics_device` and related buttons in your level.
- Analytics logs on button press.
- You can explicitly track events with `TrackAgentEvent()`.

### 🧠 Best Practices
- Use descriptive device names (e.g., `ButtonA_Pressed`).
- Prefer event binding via UEFN’s Details panel for basic usage.
- Limit to 100 analytics devices per island.
- Use the Creator Portal's Analytics Dashboard to view/download data.
- Only track events directly involving players (agents).

### ❌ Incorrect Usage and Fixes
| Issue | ❌ Wrong | ✅ Correct | Explanation |
|-------|----------|-------------|-------------|
| Missing agent reference | `AnalyticsDevice.Submit(player)` | Use `agent` type object | Devices require `agent`, not generic player/device references |
| Unassigned in Details | Using device in Verse without assigning it | Assign in Details panel | Prevents nil or unassigned errors |
| Not enabled | Calling Track without enabling | Use `Enable()` first | Device must be active to log events |

| ❌ Wrong | ✅ Fix |
|----------|---------|
| `TrackAgentEvent()` without enable | Call `Enable()` before tracking |
| Passing `none` or invalid agent | Always pass a valid `agent` |
| Expecting in-game feedback | Use `Print()` manually for debug |

### 📌 Notes
- `analytics_device` only logs manually triggered events.
- Avoid excessive or meaningless submissions.
- Label devices clearly for easier analytics dashboard filtering.

---
**End of Documentation**

