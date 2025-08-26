# UEFN Verse Device Documentation: `trigger_base_device`

## 📙 Description
`trigger_base_device` is the foundation class for all trigger-type devices in UEFN, such as:
- `trigger_device`
- `perception_trigger_device`
- `attribute_evaluator_device`

This class provides essential functionality for:
- Enabling/disabling the trigger
- Managing trigger counts and cooldowns
- Applying movement via Verse (teleport or smooth move)

> ⚠️ **Note**: This class does **not** emit any events by itself. Event logic is implemented in its derived classes.

---

## 📊 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

## 🔗 Inheritance Hierarchy
- `creative_object`
  - `creative_device_base`
    - `trigger_base_device`

---

## 🛠️ Functions & Methods

| Function | Description |
|---------|-------------|
| `Enable()` | Activates the trigger to allow responses to triggering conditions |
| `Disable()` | Deactivates the trigger to prevent any activation |
| `GetMaxTriggerCount()` | Returns max allowed triggers (0 = unlimited) |
| `SetMaxTriggerCount(MaxCount: Int)` | Sets max trigger limit (0–20, where 0 = no limit) |
| `GetTriggerCountRemaining()` | Returns remaining trigger activations before reaching the limit |
| `Reset()` | Resets internal counter of trigger activations |
| `GetResetDelay()` | Returns cooldown time (seconds) before it can trigger again |
| `SetResetDelay(Seconds: Float)` | Sets cooldown between triggers (in seconds) |
| `GetTransmitDelay()` | Returns delay (seconds) before sending signal post-trigger |
| `SetTransmitDelay(Seconds: Float)` | Sets delay after trigger before it transmits signal |
| `GetTransform()` | Returns current transform (position/rotation/scale) - use `IsValid()` first |
| `MoveTo(Position, Rotation, Duration)` | Smooth move to new position/rotation |
| `MoveTo(Transform, Duration)` | Smooth move using full transform object |
| `TeleportTo(Position, Rotation)` | Instantly move to new position/rotation |
| `TeleportTo(Transform)` | Instantly apply new transform (position/rotation/scale) |

> 📌 **Note**: No event system in this base class. Use a derived device for event callbacks.

---

## 🎛 Configuration Options (Details Panel)
- Most settings like trigger limits, delays, and enabled/disabled states can be configured in the Details Panel.
- These can also be changed at runtime using Verse methods listed above.

---

## 🧠 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

trigger_base_example := class(creative_device):

    @editable
    Trigger : trigger_base_device = trigger_base_device{}

    OnBegin<override>()<suspends> : void =
        if (Trigger.IsValid()):
            Print("Trigger is valid. Enabling and setting limits.")
            Trigger.Enable()
            Trigger.SetMaxTriggerCount(5)
            Trigger.SetResetDelay(3.0)
            Trigger.SetTransmitDelay(1.0)

            Print("Teleporting trigger.")
            Trigger.TeleportTo(
                Position := vector3{X := 1000.0, Y := 500.0, Z := 200.0},
                Rotation := rotation{Pitch := 0.0, Yaw := 90.0, Roll := 0.0}
            )
```

---

## 🔧 How to Use in UEFN

1. **Place Derived Device**  
   Add a `trigger_device` or `perception_trigger_device` to your level.

2. **Configure Defaults**  
   Set limits, delays, and other properties via the Details Panel.

3. **Create a Verse Script**  
   Use `trigger_base_device` or a derived class in your custom Verse code.

4. **Connect Logic**  
   Link the device using Verse methods or device wiring for interactions.

---

## 🧠 Best Practices
- Use `trigger_base_device` for shared logic across multiple triggers.
- Prefer derived types like `trigger_device` for event-driven gameplay.
- Always verify with `IsValid()` before calling methods.
- Use `Reset()` to refresh trigger states in loops or repeatable actions.

---

## ❌ Common Issues & Solutions

| Issue | Problem (❌) | Solution (✅) |
|-------|----------------|------------------|
| Trigger not responding | Trigger not enabled | Call `Enable()` or enable in editor |
| Device never triggers again | Max trigger count reached | Use `Reset()` or set higher count |
| Delays not behaving as expected | Reset vs. transmit confusion | Use `SetResetDelay()` and `SetTransmitDelay()` explicitly |
| No event callbacks | Using base class only | Use `trigger_device` for events |

---

## 📌 See Also
- [`trigger_device`](#) - For subscribing to events like `TriggeredEvent`
- [`perception_trigger_device`](#) - For AI/player proximity detection
- [`attribute_evaluator_device`](#) - For condition-based triggers using attributes

---

Let me know if you'd like a **sample with `trigger_device` and event handling!**

