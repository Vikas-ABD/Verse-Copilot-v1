## gameplay\_controls\_third\_person\_device – UEFN Verse Device Documentation

### 🔹 Description

The `gameplay_controls_third_person_device` lets you adapt player movement and interaction to classic third-person controls and camera perspectives in Unreal Editor for Fortnite (UEFN). Use it to create over-the-shoulder, twin-stick shooter, or custom camera/movement schemes. The device can be enabled/disabled globally or per-player, combined with camera devices for unique experiences, and all assignments can be dynamically scripted via Verse.

### 🛡️ Verse Using Statement

```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy

- `creative_object`
- `creative_device_base`
- `gameplay_controls_device`
- `gameplay_controls_third_person_device`

### 🛠️ Key Methods & Functions

| Method                    | Description                                                                 |
| ------------------------- | --------------------------------------------------------------------------- |
| `Enable()`                | Enables the third person controls device (allows assignments/interactions). |
| `Disable()`               | Disables device (stops third-person controls from being assigned/used).     |
| `AddTo(agent)`            | Assigns third-person controls to a specific agent (player).                 |
| `RemoveFrom(agent)`       | Removes the control mode from a specific agent (if already assigned).       |
| `AddToAll()`              | Assigns third-person controls to all players.                               |
| `RemoveFromAll()`         | Removes from all players, restoring previous mode if stacked.               |
| `GetTransform()`          | Returns device’s position/rotation/scale.                                   |
| `MoveTo()`/`TeleportTo()` | Moves or teleports device in world space.                                   |

### 🔹 Device Configuration (Details Panel)

- **Priority**: Control stacking; higher values override lower.
- **Add to Players on Start**: Auto-assigns controls to all players at round start.
- **Remove on Elimination**: Removes controls when player is eliminated.
- **Facing Direction**: Choose: Movement, Twin Stick, Fixed, etc.
- **Twin Stick Mouse Aim Mode**: Cursor aiming style for mouse/Twin Stick.
- **Auto Fire on Controller**: Auto-fire when aiming with right stick.
- **Movement/Turn Speed Multipliers**: Adjust per movement state.
- **Targeting Assistance**: Tune for aim assist (angle, distance, behaviors).

### 🤩 Verse Usage Example

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

third_person_controls_example := class(creative_device):

    @editable
    ThirdPersonControls : gameplay_controls_third_person_device = gameplay_controls_third_person_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    AddToButton : button_device = button_device{}

    @editable
    RemoveFromButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        AddToButton.InteractedWithEvent.Subscribe(OnAddToPressed)
        RemoveFromButton.InteractedWithEvent.Subscribe(OnRemoveFromPressed)

    OnEnablePressed(Agent : agent) : void =
        ThirdPersonControls.Enable()
        Print("Third person controls enabled!")

    OnDisablePressed(Agent : agent) : void =
        ThirdPersonControls.Disable()
        Print("Third person controls disabled!")

    OnAddToPressed(Agent : agent) : void =
        ThirdPersonControls.AddTo(Agent)
        Print("Third person controls added to agent!")

    OnRemoveFromPressed(Agent : agent) : void =
        ThirdPersonControls.RemoveFrom(Agent)
        Print("Third person controls removed from agent!")
```

#### Explanation:

- `ThirdPersonControls`: Reference to placed `gameplay_controls_third_person_device`
- `EnableButton`, `DisableButton`, `AddToButton`, `RemoveFromButton`: Button devices wired to test/demo logic.
- Logic: Button presses control per-agent or global control assignment.
- `Print`: Placeholder—customize with your own gameplay logic.
- Configuration (facing, speed, priority) handled in Details Panel.

### ☑ How to Use in UEFN

1. **Place Devices**
   - Add a `gameplay_controls_third_person_device` (Devices > Controls > Third Person Controls).
   - Add four `button_device` actors (Enable, Disable, AddTo, RemoveFrom).
2. **Configure Controls**
   - Use Details Panel to adjust facing, speed, auto-assign, elimination settings.
3. **Create Verse Script**
   - In Verse Explorer → Right-click folder → Create New Verse File.
   - Paste the example code and save.
   - Build (Ctrl+Shift+B) until "Build Succeeded."
   - Place the custom device and assign all @editable fields.
4. **Playtest & Extend**
   - Start session and test control assignment live.
   - Expand logic: mode switches, camera unlocks, narrative triggers.

### 🧠 Best Practices

- Use `Priority` to manage overlapping control devices.
- Pair with camera devices for richer gameplay.
- Assign/remove controls per-agent for multiplayer differentiation.

### ❌ Common Issues & Fixes

| Problem                    | Likely Cause                   | Solution                              |
| -------------------------- | ------------------------------ | ------------------------------------- |
| No control effect          | Device not enabled/assigned    | Call `.Enable()`, use `.AddTo(agent)` |
| Removes unexpectedly       | "Remove on Elimination" active | Adjust property in Details panel      |
| Overridden by other device | Priority conflict              | Raise third-person device priority    |

### ℹ️ Note

- Third-person controls can be dynamically stacked/removed for advanced gameplay flows.
- Ensure all @editable fields are linked and "Build Succeeded" before testing.

