# Player Movement Settings Device – UEFN Verse Device Documentation

## 🔹 Description
The `player_movement_settings_device` is used to dynamically adjust player movement properties (such as speed, jump height, gravity, etc.) based on movement mode. These settings can be applied to specific agents (players) or all players in your experience. A priority-based system ensures that the highest-priority device overrides others.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `player_movement_settings_device`

## 🔌 Exposed Interfaces
- `enableable` – Can be toggled on or off via Verse.

## 🛠️ Functions & Methods
| Function | Description |
|----------|-------------|
| `AddTo(Agent: agent)` | Applies the movement settings to a single agent. Only valid for player agents. |
| `AddToAll()` | Applies movement settings to all valid player agents. |
| `RemoveFrom(Agent: agent)` | Removes settings from a specific agent. Fails if the settings weren’t applied. |
| `RemoveFromAll()` | Removes movement settings from all agents. |
| `Enable()` | Enables the device, allowing settings to take effect. |
| `Disable()` | Disables the device and revokes effects. Agent list is retained. |
| `IsEnabled()` | Returns whether the device is enabled. |
| `GetPriority()` | Returns the device’s priority level. Highest takes precedence. |
| `GetRegisteredAgents()` | Lists agents currently affected by the device. |
| `GetTransform()` | Returns the device's transform (position, rotation, scale). Use `IsValid()` first. |
| `MoveTo(Position, Rotation, Duration)` | Smoothly moves the device over time. |
| `MoveTo(Transform, Duration)` | Moves using full transform. |
| `TeleportTo(...)` | Instantly moves the device to a location and orientation. |

## 🧰 Verse Usage Example
This script applies movement settings to all players at the start and removes them after 10 seconds:
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /Verse.org/Time }

movement_settings_example := class(creative_device):

    @editable
    MovementSettings : player_movement_settings_device = player_movement_settings_device{}

    OnBegin<override>()<suspends> : void =
        MovementSettings.Enable()
        MovementSettings.AddToAll()
        Print("Movement settings applied to all players.")

        Sleep(10.0)
        MovementSettings.RemoveFromAll()
        Print("Movement settings removed from all players.")
```

## 🔧 How to Use in UEFN
1. **Place the Device**
   - Add a `player_movement_settings_device` to your island.
2. **Configure Settings**
   - Adjust movement settings (e.g., walking, sprinting, crouching) in the Details panel.
3. **Create and Assign Verse Logic**
   - Use the example script or design custom logic.
4. **Reference in Verse Device**
   - Link the `MovementSettings` field in your class to the placed device.
5. **Build and Test**
   - Compile Verse (Ctrl+Shift+B), then playtest your island.

## 🧠 Best Practices
- Use multiple devices with varying priorities to support conditional overrides (e.g., power-ups, zones).
- Always call `Enable()` before `AddTo()` or `AddToAll()`.
- Use `RemoveFrom()`/`RemoveFromAll()` to cleanly remove effects.
- Use `GetRegisteredAgents()` to debug which players are affected.

## ❌ Common Issues & Solutions
| Issue | Problem ❌ | Solution ✅ |
|-------|-----------|-------------|
| Movement settings don’t apply | Device not enabled | Call `Enable()` before applying settings |
| No visible change in movement | Priority conflict | Use `GetPriority()` or increase priority |
| Settings removed too early | Premature `RemoveFromAll()` | Ensure correct timing and logic |
| Fails for NPCs | Unsupported agent type | Use only on player-controlled agents |

## 📎 Note
This device requires Verse to apply settings to agents. It does **not** auto-apply on placement. It’s ideal for movement-based effects like sprint boosts, speed zones, or jump height changes in gameplay experiences such as races, puzzles, or action maps.

