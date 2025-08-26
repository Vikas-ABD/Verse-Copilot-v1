📘 **hud_message_device – UEFN Verse Device Documentation**

---

### 🔹 Description
The `hud_message_device` is used to display custom HUD messages to one or more agents (players) in your Fortnite experience. This device is versatile for:
- Objectives
- Alerts
- Narrative messages
- Score change feedback
- Other notifications

You can:
- Control display time
- Change the message text dynamically
- Show or hide messages per agent
- Trigger messages via Verse code or device events

---

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `hud_message_device`

---

### 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| `SetText(message)` | Sets the message to be displayed (up to 150 characters). |
| `Show()` | Shows the current HUD message on all players’ screens. |
| `Show(agent)` | Shows the message to a specific agent. |
| `Hide()` | Hides the HUD message for all players. |
| `Hide(agent)` | Hides the message for a specific agent. |
| `SetDisplayTime(float)` | Sets how long (in seconds) the message is shown. 0 means "persistent." |
| `GetDisplayTime()` | Gets the current display time duration. |
| `GetTransform()` | Gets the current transform for the device. |
| `MoveTo()` / `TeleportTo()` | Moves or teleports the device in the world. |

---

### 🎛 Configuration Options (Details Panel)
| Option | Description |
|--------|-------------|
| **Default Message** | The starting message text (can be changed in Verse). |
| **Display Time** | How long the message should appear (seconds; 0 = unlimited). |
| **HUD Widget** | Reference to a widget blueprint for custom UI. |
| **Show On Game Start** | Displays the message automatically at game start. |
| **Color/Style** | Appearance of the HUD message bar. |
| **Fade In/Out Delay** | Animates appearance/disappearance of messages. |

> *Set all options in the Details panel for the device in UEFN.*

---

### 🧩 Events
This device does **not** expose custom Verse events; use Verse functions or wiring to trigger messages.

---

### 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use hud_message_device
hud_message_example := class(creative_device):

  @editable
  HUDMessage : hud_message_device = hud_message_device{}

  @editable
  ShowButton : button_device = button_device{}

  @editable
  HideButton : button_device = button_device{}

  OnBegin<override>()<suspends> : void =
    # Subscribe to control buttons
    ShowButton.InteractedWithEvent.Subscribe(OnShowPressed)
    HideButton.InteractedWithEvent.Subscribe(OnHidePressed)

  # Button control handlers
  OnShowPressed(Agent : agent) : void =
    HUDMessage.Show(Agent)
    Print("HUD message shown!")

  OnHidePressed(Agent : agent) : void =
    HUDMessage.Hide(Agent)
    Print("HUD message hidden!")
```

### Explanation
- The device references:
  - One `hud_message_device`
  - A `button_device` to show
  - A `button_device` to hide
- Pressing `ShowButton` calls `HUDMessage.Show(Agent)`, showing the message only for the interacting agent.
- Pressing `HideButton` calls `HUDMessage.Hide(Agent)`, hiding the message for that player.
- Use `SetText()` before `Show()` to update the message.
- Use `SetDisplayTime(0)` to make the message persistent.

---

### 🔧 Step-by-Step Setup in UEFN

1. **Create the Verse Device**
   - Open **Verse Explorer** in UEFN
   - Right-click a folder → Create a new Verse file (e.g., `hud_message_example.verse`)
   - Click **Create Empty**, paste the code, and save
   - Press `Ctrl+Shift+B` or click **Verse → Build Verse Code** until you see "Build Succeeded"

2. **Add Devices to Your Level**
   - Drag your Verse device from the Content Browser into the level
   - Add:
     - One `hud_message_device`
     - Two `button_device` objects (for show/hide)

3. **Assign @editable References**
   - Select the Verse device in the level
   - In the **Details panel**, set:
     - `HUDMessage` → the placed hud_message_device
     - `ShowButton` / `HideButton` → your placed button devices

4. **Configure Device Options**
   - Set `Default Message`, `Display Time`, `Color/Style`, etc., in the hud_message_device Details panel

5. **Test Your Setup**
   - Enter **Play mode**
   - Interact with the buttons to see the HUD message appear/disappear for different players

---

### 🧠 Best Practices
- Always use `SetText()` before `Show()` to ensure dynamic message updates
- Use `Show(agent)` and `Hide(agent)` for player-specific feedback
- Use `Show()` and `Hide()` for all players
- Combine with quest or objective logic for immersive feedback
- Attach a custom `HUD Widget` for a more advanced UI experience

---

### ❌ Common Issues & Fixes
| Issue | ❌ Wrong Example | ✅ Correct Example | Explanation |
|-------|------------------|--------------------|-------------|
| Text doesn't update | Only use message from Details panel | Call `SetText()` in Verse | Dynamic messages require Verse update |
| Message doesn’t persist | Default display time is used | Use `SetDisplayTime(0)` | 0 = stays until explicitly hidden |
| Wrong agent targeted | Called `Show()` with no argument | Use `Show(Agent)` | No agent = message shown to all |
| Blank device references | Did not assign devices in Details panel | Always assign `@editable` fields | Required for Verse logic to function |

---

### 📝 Note
You can fully control message content, style, duration, and targeting per agent or globally. Ideal for:
- Custom quests
- Narrative storytelling
- Timed alerts
- Tutorial instructions

