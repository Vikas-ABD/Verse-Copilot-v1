# gameplay_controls_side_scroller_device – UEFN Verse Device Documentation

## 🔹 Description
The `gameplay_controls_side_scroller_device` is used in Unreal Editor for Fortnite (UEFN) to adapt player controls for classic side-scroller gameplay. When enabled, it constrains movement and camera controls so players can only move/focus left or right, creating 2D-platformer or beat ‘em up experiences. Pair it with Fixed Angle/Point Camera devices for full side-scroller games. The device can be enabled/disabled, assigned to specific agents (players), and removed dynamically in Verse.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `gameplay_controls_device`
- `gameplay_controls_side_scroller_device`

## 🛠️ Key Methods & Functions
| Method            | Description                                                |
|-------------------|------------------------------------------------------------|
| `Enable()`        | Activates the side scroller control preset.               |
| `Disable()`       | Deactivates the control preset.                           |
| `AddTo(agent)`    | Adds this control mode to the given agent/player.         |
| `RemoveFrom(agent)` | Removes this control mode from the given agent/player.    |
| `AddToAll()`      | Assigns this control mode to all players in the game.     |
| `RemoveFromAll()` | Removes this mode from all players.                       |
| `GetTransform()`  | Returns device's world transform for scripting.           |
| `MoveTo()/TeleportTo()` | Moves or teleports device (rarely needed).                |

## 🎛 Device Configuration (Details Panel)
- **Priority**: Higher priority controls override lower ones.
- **Add to Players on Start**: Auto-assigns control mode to all players at game start.
- **Remove on Elimination**: Removes controls from player when eliminated.
- **Enabled During Phase**: Sets when the device is active (e.g. always, gameplay only).
- **Constrain Movement**: Restricts player movement to X axis.
- **Jump/Crouch**: Toggle, dedicate, or use movement-based options.
- **Ranged Direction**: Adjust aiming behavior in side scroller mode.
- **Movement Speed Multipliers**: Control speed for walking, aiming, and shooting.
- **Targeting Options**: Lock-on, vertical aiming, distance, etc.

## 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use gameplay_controls_side_scroller_device
side_scroller_controls_example := class(creative_device):

    @editable
    SideScrollerControls : gameplay_controls_side_scroller_device = gameplay_controls_side_scroller_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    AddToButton : button_device = button_device{}

    @editable
    RemoveFromButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to control buttons
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        AddToButton.InteractedWithEvent.Subscribe(OnAddToPressed)
        RemoveFromButton.InteractedWithEvent.Subscribe(OnRemoveFromPressed)

    # Button control handlers
    OnEnablePressed(Agent : agent) : void =
        SideScrollerControls.Enable()
        Print("Side scroller controls enabled!")

    OnDisablePressed(Agent : agent) : void =
        SideScrollerControls.Disable()
        Print("Side scroller controls disabled!")

    OnAddToPressed(Agent : agent) : void =
        SideScrollerControls.AddTo(Agent)
        Print("Side scroller controls added to agent!")

    OnRemoveFromPressed(Agent : agent) : void =
        SideScrollerControls.RemoveFrom(Agent)
        Print("Side scroller controls removed from agent!")
```
### Explanation:
- `SideScrollerControls`: Reference to placed gameplay_controls_side_scroller_device.
- `Enable/Disable/AddTo/RemoveFromButton`: 4 button devices wired via Verse.
- Each button executes one control action with feedback via `Print()`.

## ​​​​How to Use in UEFN
### 1. Place Devices in Your Level
- Add `gameplay_controls_side_scroller_device` (Devices > Controls).
- Add four `button_device` actors for enabling/disabling/add/remove actions.

### 2. Configure in Details Panel
- Customize axis constraints, movement behavior, priority, jump/crouch, etc.

### 3. Create and Add Verse Script
- Open `Verse Explorer` > Create new Verse file (e.g. `side_scroller_controls_example.verse`).
- Paste code, save, build with `Ctrl+Shift+B`.
- Place Verse device and configure `@editable` fields in Details Panel.

### 4. Playtest & Extend
- Launch a session and test buttons.
- Use `AddTo` and `RemoveFrom` for per-player logic.

## 🧠 Best Practices
- Combine with Fixed Angle/Point Camera for authentic side-scroller look.
- Use `Priority` to resolve control conflicts.
- Dynamically assign/remove controls for boss fights, cutscenes, or multi-mode levels.

## ❌ Common Issues & Fixes
| Problem                     | Cause                               | Solution                                        |
|-----------------------------|--------------------------------------|-------------------------------------------------|
| Controls not switching      | Device not enabled/added             | Use `.Enable()` and `.AddTo(agent)`            |
| Doesn’t affect all players | Missing AddToAll/RemoveFromAll call | Use `.AddToAll()` or "Add on Start" setting     |
| Players lose controls       | Remove on Elimination is enabled     | Adjust that setting in Details Panel            |

> For camera integration, pair with a Fixed Angle/Fixed Point Camera device at the same time as control changes.

