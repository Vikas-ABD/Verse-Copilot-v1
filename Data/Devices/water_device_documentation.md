📘 **water_device – UEFN Verse Device Documentation**

---

🔹 **Description**
The `water_device` is used to create and manipulate water volumes on your Fortnite island. Players can swim, fish, or drive boats in these areas. The device lets you control water level (fill/empty), enable/disable the volume, and respond to entry/exit events for agents, making it suitable for puzzles, races, fishing zones, and dynamic map events.

🧱 **Verse Using Statement**
```verse
using { /Fortnite.com/Devices }
```

---

🔗 **Inheritance Hierarchy**
- `creative_object`: Base class for creative devices and props.
- `creative_device_base`: Base class for `creative_device`.
- `water_device`

---

🧩 **Data Members (Events)**
| Name                          | Type               | Description                                                  |
|-------------------------------|--------------------|--------------------------------------------------------------|
| `AgentEntersWaterEvent`      | `listenable(agent)`| Signaled when an agent enters the water; passes the agent.  |
| `AgentExitsWaterEvent`       | `listenable(agent)`| Signaled when an agent exits the water; passes the agent.   |
| `VerticalFillingCompletedEvent` | `listenable(tuple())` | Triggered when water is filled to target level.             |
| `VerticalEmptyingCompletedEvent` | `listenable(tuple())` | Triggered when the volume is completely empty.              |

---

🛠️ **Functions & Methods**
| Name                        | Description                                                  |
|-----------------------------|--------------------------------------------------------------|
| `Enable()`                  | Enables the water volume (players can swim, effects occur). |
| `Disable()`                 | Disables the volume (removes water, disables effects).      |
| `Reset()`                   | Resets water level to the default fill percentage.          |
| `BeginVerticalFilling()`    | Starts filling the volume with water.                       |
| `BeginVerticalEmptying()`   | Starts emptying the water volume.                           |
| `StopVerticalMovement()`    | Stops ongoing fill/empty actions.                           |
| `ResumeVerticalMovement()`  | Continues previous filling or emptying process.             |
| `GetTransform()`            | Returns the device’s world transform.                       |
| `MoveTo(Position, Rotation, Time)` | Animates movement to target position/rotation.     |
| `MoveTo(Transform, Time)`   | Animates to new transform.                                  |
| `TeleportTo(Position, Rotation)` | Instantly moves to position and rotation.            |
| `TeleportTo(Transform)`     | Instantly moves to specified transform.                     |

---

🎛 **Configuration Options (Details Panel)**
- **Zone Width/Depth/Height**: Size of the water volume (tiles).
- **Default Vertical Water Percentage**: Default fill height percentage.
- **Vertical Filling/Emptying Speed**: Rate of water level change.
- **Interact with Trigger**: Whether to use trigger volumes.
- **Water Type**: Effect/colors (Default, River Styx, Red River Styx).
- **Enable During Phase**: Game phases for auto activation.
- **Team/Class Filters**: Restrict who can trigger events.

---

🧰 **Usage Example**
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

water_device_example := class(creative_device):

    @editable
    Water : water_device = water_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnEnablePressed(Agent : agent) : void =
        Water.Enable()
        Print("Water volume enabled!")

    OnDisablePressed(Agent : agent) : void =
        Water.Disable()
        Print("Water volume disabled!")
```

---

🧠 **Best Practices**
- Combine with volume, trigger, or item devices for interactive gameplay (fishing, racing, hazards).
- Listen for entry and exit events to create dynamic logic.
- Use fill/empty for puzzles, environmental changes.
- Set correct phases, water types, and triggers.

---

❌ **Incorrect Usage Examples and Fixes**
| Issue                                       | ❌ Wrong                 | ✅ Correct                              | Explanation                                                     |
|--------------------------------------------|--------------------------|----------------------------------------|-----------------------------------------------------------------|
| Fill/empty with device disabled             | Just call fill/empty     | Call `.Enable()` first                 | Must enable before action                                       |
| Not subscribing to water events             | Expect on-entry behavior | Use `.Subscribe()` to events           | Events must be explicitly handled                               |
| Unreasonable fill/empty speed               | Extreme speed values     | Use realistic filling/emptying speeds  | Unnatural values may cause glitches or poor experience          |
| Forgetting to reset                         | Only Enable/Disable      | Use `.Reset()`                         | Clears states and restores defaults                             |

---

📌 **Notes**
- Only one `water_device` should control a specific region to avoid conflicts.
- Use water manipulation for immersive gameplay and environmental control.
- Customize all properties to match game design.

