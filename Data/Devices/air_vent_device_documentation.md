## 📘 air_vent_device – UEFN Verse Device Documentation

### 🔹 Description
The `air_vent_device` boosts agents (players or AI), vehicles, and objects into the air when they enter its area. You can angle, rotate, and stack multiple vents for creative traversal, aerial puzzles, or movement-based minigames. The device supports tuning knockup force, gust range, visual/audio FX, and when it’s enabled during gameplay.

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `air_vent_device`

### 🛠️ Functions & Methods
| Name              | Description                                      |
|-------------------|--------------------------------------------------|
| `Enable()`        | Enables the air vent (starts gust effect).       |
| `Disable()`       | Disables the air vent (no boosting while off).   |
| `Activate()`      | Triggers the air vent’s gust effect immediately. |
| `GetTransform()`  | Gets position, rotation, scale of the device.    |
| `MoveTo()` / `TeleportTo()` | Move or teleport the air vent.     |

### 🎛 Configuration Options (Details Panel)
| Option                    | Description                                                         |
|---------------------------|---------------------------------------------------------------------|
| Visible During Game       | On/Off (controls collision & visuals).                              |
| Enabled During Phase      | None/Always/Pre-Game Only/Gameplay Only/Create Only                 |
| Knockup Force Multiplier  | None, Low, Medium, High, Very High, Super High, Mega High           |
| Gust Range (Meters)       | Set distance effect reaches.                                        |
| Min Knockup Percentage    | Controls force at farthest edge of gust.                            |
| Skydive After Launch      | On/Off: should entering agents begin skydiving?                     |
| Enable SFX / VFX          | Enable/disable sound and visual effects.                            |

### 🧩 Events
*No unique Verse events; driven by enable/disable/activate controls and collision response.*

### 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use air_vent_device with event subscriptions and control
air_vent_example := class(creative_device):

    @editable
    AirVent : air_vent_device = air_vent_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to control buttons
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    # Button control handlers
    OnEnablePressed(Agent : agent) : void =
        AirVent.Enable()
        Print("Air vent enabled!")

    OnDisablePressed(Agent : agent) : void =
        AirVent.Disable()
        Print("Air vent disabled!")
```

### How it works in UEFN:
**1. Place Devices in Level:**
- Add an `air_vent_device` wherever you want a boost area.
- Place any number, rotate to direct their effect, and stack for combos.
- (Optional) Add `button_device`s nearby for enable/disable/test control.

**2. Configure Device Options (Details Panel):**
- Tweak force, gust range, minimum percentage, SFX/VFX, visibility, and "Enabled During Phase" to match your design.

**3. Create & Build Verse Script:**
- In Verse Explorer, right-click your folder, select *Create New Verse File*, and name it (e.g., `air_vent_example.verse`).
- Paste in the Verse code from above, save.
- Click *Verse → Build Verse Code* (or `CTRL+SHIFT+B`) until “Build Succeeded”.

**4. Place & Reference Devices:**
- Drag your Verse device (`air_vent_example`) into your map.
- In the Details panel, assign:
  - `AirVent` → your placed `air_vent_device`
  - `EnableButton` / `DisableButton` → your `button_device`(s) (if used)

**5. Test Gameplay:**
- Launch a session, walk into the air vent area, and use buttons to enable/disable it live.

### 🧠 Best Practices
- Tilt or rotate air vents for creative jump/flight directions.
- Stack vents to chain boosts or make advanced parkour puzzles.
- Link enable/disable to game phases, puzzles, rounds, or minigames for dynamic challenges.
- Adjust force and range carefully to fit area size and desired gameplay.

### ❌ Incorrect Usage Examples and How to Fix
| Issue                                | ❌ Wrong Example                | ✅ Correct Example                        | Explanation                                                        |
|--------------------------------------|----------------------------------|----------------------------------------------|--------------------------------------------------------------------|
| Forgetting to enable vent at runtime | Just place and don’t call Enable() | `AirVent.Enable()` (via logic, wire, or button) | Vent only works when enabled.                                      |
| Overriding vent state at runtime     | Changed visibility/enabled in Details | Use `AirVent.Enable()`/`Disable()` in Verse | Changes in editor only affect game start state.                    |
| Assigning device refs incorrectly    | Did not set `AirVent` in Details | Assign `AirVent = (your air_vent_device)`    | Verse code won’t run correctly if refs left blank.                 |
| Expecting bullet/projectile block    | Use vent to block shots          | Use `barrier_device` for projectile blocking | Air vents affect movement, not projectiles.                        |
| Forgetting “Skydive After Launch”     | Never set, can’t glide            | Set "Skydive After Launch" = On              | Needed for flying/gliding launches.                                |

### Notes
- Air vents are *not* traps—agents must move into the area, and configuration determines boost strength/fun.
- Use creative naming and organization for many vents—in complex maps, this helps with linking and maintenance.
- For unique traversal, combine with skydive/anti-grav zones, or layer vents with variable strengths.

