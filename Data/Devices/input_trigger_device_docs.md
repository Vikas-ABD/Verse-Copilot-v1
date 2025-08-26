# input_trigger_device – UEFN Verse Device Documentation

## 🔹 Description
The `input_trigger_device` listens for when a player activates or releases specific input actions (like pressing a custom or standard button/key) in your Fortnite island. You can configure which input to track, and players can rebind the key/button in their game settings. This device is ideal for creating custom controls, minigames, or input-driven events using Verse scripting or device bindings.

## 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
```

## 🔗 Inheritance Hierarchy
- `creative_object`  
  *Base class for creative devices and props.*
- `creative_device_base`  
  *Base class for creative_device.*
- `input_trigger_device`

## 🧩 Core Events & Methods
| Name / Function       | Type/Signature                | Description                                                                 |
|-----------------------|-------------------------------|-----------------------------------------------------------------------------|
| `PressedEvent`        | `listenable(agent)`          | Event: fired when the tracked input is pressed by an agent. Sends the agent pressing the input. |
| `ReleasedEvent`       | `listenable(tuple(agent, float))` | Event: fired when the input is released. Sends the agent and duration held (in seconds). |
| `Enable()`            | `void`                       | Enables this device—begins listening for input.                           |
| `Disable()`           | `void`                       | Disables the device and removes from HUD if shown.                         |
| `Register(Agent)`     | `void`                       | Adds an agent as a valid trigger source (if using registration restriction). |
| `Unregister(Agent)`   | `void`                       | Removes an agent from the registered list.                                 |
| `UnregisterAll()`     | `void`                       | Removes all agents from valid source list.                                 |
| `IsHeld(Agent)`       | `logic`                      | Returns whether the agent is currently holding the input.                  |
| `GetTransform()`      | `transform`                  | Returns device world transform.                                            |
| `MoveTo()` / `TeleportTo()` | Creative object movement | Move/teleport device in world if needed.                                   |

## 🎛 Configuration Options (Details Panel)
- **Input Type**: Creative Input Action, Standard Action
- **Creative Input**: Selects which custom input is being tracked (e.g., Custom 1–12: Fire, Jump, Crouch, etc.)
- **Axis Direction**: (For directional input only) Listen for Negative, Positive, or Any direction
- **Standard Input**: Fire, Target, Crouch, Sprint, Jump (only for Standard Input Type)
- **Consume Input**: If enabled, input will not be passed to other actions
- **Show on HUD**: Show/hide input UI on player HUD (esp. for mobile/console)
- **Allowed Class/Team**: Restrict who can activate the input trigger

## 🛠 Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example: Listening for input trigger events
input_trigger_example := class(creative_device):

    @editable
    InputTrigger : input_trigger_device = input_trigger_device{}

    OnBegin<override>()<suspends> : void =
        InputTrigger.PressedEvent.Subscribe(OnInputPressed)
        InputTrigger.ReleasedEvent.Subscribe(OnInputReleased)

    OnInputPressed(Agent : agent) : void =
        Print("Input pressed by player!")

    OnInputReleased(Params : tuple(agent, float)) : void =
        Print("Input released by player!")
```

### Explanation:
- Drag an `input_trigger_device` into your level and configure which input you wish to monitor (via Details panel).
- You can show the HUD button, restrict to class/team, and control rebind or consume options.
- In Verse, subscribe to `PressedEvent` and `ReleasedEvent` to run your own logic (see above).
- Players can rebind Creative Input Actions in their Keyboard/Controller settings under Creative Input Action section.

## 🧠 Best Practices
- Assign a clear custom icon and text for HUD buttons for clarity, especially on mobile and controller.
- Use multiple `input_trigger_device`s for multi-button setups.
- Always use the correct `agent` in your events and method calls.
- For best player experience, clearly communicate which input(s) you expect them to use, and describe in-game.

## ❌ Incorrect Usage Examples and How to Fix
| Issue | ❌ Wrong Example | ✅ Correct Example | Explanation |
|-------|--------------------|------------------------|-------------|
| Not assigning device ref | Calling methods without Details ref | Assign as `@editable` and set in Details panel | Prevents nil/error on reference in Verse |
| Using wrong event args | `ReleasedEvent.Subscribe(func(agent))` | Use `func(tuple(agent, float))` signature | `ReleasedEvent` sends a tuple of (agent, duration) |
| Not enabling device | Using when disabled | Call `Enable()` or check "Enabled at Start" | Device must be enabled to listen for input |

### Notes:
- The device is **network/server-authoritative**, so latency may affect input response time (keep this in mind for fast-action gameplay).
- Useful for **custom ability systems**, **time challenges**, or **any custom gameplay built on user inputs**.

