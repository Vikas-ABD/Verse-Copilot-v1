# Gameplay Controls Device – UEFN Verse Device Documentation

## 🔹 Description
The `gameplay_controls_device` is a powerful and highly reusable device in **Unreal Editor for Fortnite (UEFN)** that dynamically manages **player input and movement control schemes**. This device enables developers to modify player control modes mid-game, supporting various perspectives and movement mechanics, such as **first person, third person, side scroller**, or **custom control restrictions**.

It can be toggled on/off, and its control schemes can be applied to specific players or globally. The device can also respond to gameplay phases or scripted Verse events.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
  - `creative_device_base`
    - `gameplay_controls_device`

## 🛠️ Key Methods & Functions
| Method            | Description                                                                      |
|------------------|----------------------------------------------------------------------------------|
| `Enable()`        | Enables the device, making it ready for player assignment.                        |
| `Disable()`       | Disables the device and removes its effects from players.                        |
| `AddTo(agent)`    | Pushes the control scheme to a specific player (agent), making it their active mode. |
| `RemoveFrom(agent)` | Removes the control scheme from the specified player.                         |
| `AddToAll()`       | Applies the control scheme to all players.                                       |
| `RemoveFromAll()`  | Removes the control scheme from all players.                                     |
| `GetTransform()`   | Returns the transform of the device (rarely needed for control logic).          |
| `MoveTo()/TeleportTo()` | Moves or teleports the device in world space (not commonly used for this device). |

## 🎛 Device Configuration (Details Panel)
| Option                  | Description                                                                  |
|------------------------|------------------------------------------------------------------------------|
| **Priority**           | Sets stacking order with other control devices.                              |
| **Add to Players on Start** | Automatically assigns this control scheme to all players when the game starts. |
| **Remove on Elimination** | Removes the control scheme from players upon elimination.                  |
| **Affects Team/Class** | Limits device effects to selected teams or classes.                          |
| **Invert Team/Class**  | Applies the effect to all *except* selected teams or classes.                |

## 🧹 Typical Usage Patterns

### Dynamic Mode Switching
Use this device during **platformer sequences**, **boss battles**, or **scripted events** to dynamically switch control modes mid-game.

### Per-Player or Global Assignment
Utilize `AddTo` and `RemoveFrom` to target individual players, or `AddToAll` and `RemoveFromAll` for global changes.

### Advanced Stacking
Stack multiple `gameplay_controls_device` instances to orchestrate complex player control behavior.

---
This documentation provides a solid reference for integrating and customizing player controls using the `gameplay_controls_device` within UEFN Verse experiences.

