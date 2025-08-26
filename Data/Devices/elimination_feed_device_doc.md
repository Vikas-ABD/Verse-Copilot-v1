## elimination_feed_device – UEFN Verse Device Documentation

### 📙 Description
The `elimination_feed_device` allows you to send custom messages to the elimination feed ("elim feed") that players see in your Fortnite island. This device can be used to display on-screen notifications for eliminations, achievements, captures, or any custom event. It enables you to customize real-time feedback for players using Verse scripting or trigger logic.

---

### 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
```

---

### 🔗 Inheritance Hierarchy
- `creative_object`
  - *Base class for creative devices and props.*
- `creative_device_base`
  - *Base class for creative_device.*
- `elimination_feed_device`

---

### 🥩 Core Methods
| Function Name | Signature / Description |
|---------------|--------------------------|
| `Activate(Agent)` | Sends the configured feed message to the elimination feed, using the provided agent as the instigator. |
| `Enable()` | Enables the device so it can appear and send messages. |
| `Disable()` | Disables the device from sending feed messages. |
| `GetTransform()` | Gets device transform (rarely needed for feed messaging). |
| `MoveTo()` / `TeleportTo()` | Standard movement methods from `creative_object` (rarely needed for this device). |

---

### 🎛 Configuration Options (Details Panel)
| Option | Description |
|--------|-------------|
| **Message** | The custom message to display in the elimination feed |
| **Message Color** | Set the color for your custom message |
| **Player Highlight Color** | Set custom color for the player name in the message |
| **Message Icon** | Display an icon next to your text (optional) |
| **Message Visibility** | Control who sees the message (all, team, enemies, triggers) |
| **Message Visibility by Class** | Restrict visibility to class |
| **Activating Team/Class** | Restrict which agents can trigger (optional, for teams/classes) |

> Configure all these in UEFN's Details panel for each device instance.

---

### 🧰 Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Device to send custom messages to the elimination feed
elimination_feed_example := class(creative_device):

    @editable
    EliminationFeed : elimination_feed_device = elimination_feed_device{}

    @editable
    FeedButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to button interaction
        FeedButton.InteractedWithEvent.Subscribe(OnButtonPressed)

    # Send custom elimination feed message when button is pressed
    OnButtonPressed(Agent : agent) : void =
        EliminationFeed.Activate(Agent)
        Print("Custom elimination feed message sent!")
```

#### Explanation:
- Place both an `elimination_feed_device` and a `button_device` in your level.
- Assign the `elimination_feed_device` and `button_device` to the respective `@editable` variables in the Details panel.
- Configure message, color, icon, and visibility in the `elimination_feed_device`'s Details panel.
- When the button is pressed, the configured message will be sent to the elimination feed, attributed to the player.

---

### 🧠 Best Practices
- Keep messages short, clear, and visually distinct.
- Use color and icons to improve message visibility.
- Use visibility and team/class restrictions for targeted gameplay scenarios.
- Suitable for eliminations, captures, power-ups, objectives, and other key events.

---

### ❌ Incorrect Usage Examples and Fixes
| Issue | ❌ Wrong Example | ✅ Correct Example | Explanation |
|-------|---------------------|------------------------|-------------|
| Not assigning device reference | `Activate()` without assignment | Assign in Details panel as `@editable` | Prevents nil/error access to device |
| Incorrect argument | `Activate(player)` | `Activate(Agent)` as provided to handler | Must use a valid agent object |
| Message not showing | Device not enabled/configured | Use `Enable()` and configure all message options | Device must be enabled and properly set up |

#### Notes:
- Message display may vary based on team/class/visibility settings.
- The device does **not** auto-detect eliminations—you must explicitly call `Activate()` during events or use triggers.
- Use multiple instances for different messages or events.

