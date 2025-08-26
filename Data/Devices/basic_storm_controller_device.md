# UEFN Verse Device Documentation: `basic_storm_controller_device`

## 📙 Description
The `basic_storm_controller_device` provides a simplified method to add a **single-phase storm** to your Fortnite island. It creates a shrinking storm circle that damages players outside its boundary, enhancing gameplay tension and guiding players into specific zones. You can customize timing, circle sizes, movement, and behaviors.

> For multi-phase storms, use the `advanced_storm_controller_device`.

---

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `storm_controller_device`
- `basic_storm_controller_device`

---

## 🤩 Data Members (Events)
| Name | Type | Description |
|------|------|-------------|
| `PhaseEndedEvent` | `listenable(payload)` | Triggers when the storm finishes resizing/closing. |

---

## 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| `GenerateStorm()` | Spawns/starts the storm. Works only if "Generate Storm On Game Start" is set to **No**. |
| `DestroyStorm()` | Immediately removes the storm. |
| `GetTransform()` | Returns world position, rotation, and scale of the device. |
| `MoveTo()` / `TeleportTo()` | Relocates the storm device. Affects future storms only. |

---

## 🎛 Configuration Options (Details Panel)
| Option | Description |
|--------|-------------|
| Wait Time | Delay before the storm starts resizing. |
| Resize Time | Duration of the storm shrinking from start to end radius. |
| Finish Behavior | Behavior after resizing: **Stay** (remains) or **Destroy** (disappears). |
| Delay Time | Delay before the storm appears. |
| Move Delay Time | Delay before movement begins, if enabled. |
| Movement Direction | **Rotation** or **Random**: controls storm movement. |
| Minimum/Maximum Move Distance | Range (in meters) for random movement. |
| Damage Per Second | Damage dealt outside the storm (high = instant elimination). |
| Storm Sickness | Enable/disable damage over time for being in the storm too long. |
| Initial/Final Storm Radius | Sets start and end radius of the storm in meters. |
| Generate Storm on Game Start | Set to **No** for Verse or trigger control. |

---

## 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

basic_storm_controller_example := class(creative_device):

    @editable
    StormController : basic_storm_controller_device = basic_storm_controller_device{}

    @editable
    GenerateButton : button_device = button_device{}

    @editable
    DestroyButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        StormController.PhaseEndedEvent.Subscribe(OnPhaseEnded)
        GenerateButton.InteractedWithEvent.Subscribe(OnGeneratePressed)
        DestroyButton.InteractedWithEvent.Subscribe(OnDestroyPressed)

    OnPhaseEnded(PhaseIndex : tuple()) : void =
        Print("Storm phase ended.")

    OnGeneratePressed(Agent : agent) : void =
        StormController.GenerateStorm()
        Print("Storm generated!")

    OnDestroyPressed(Agent : agent) : void =
        StormController.DestroyStorm()
        Print("Storm destroyed!")
```

---

## 🔧 How It Works in UEFN
1. **Place Devices in Level**
    - Add a `basic_storm_controller_device` at your storm center.
    - Add `button_device`s (or other creative devices) to control the storm.

2. **Configure the Storm**
    - Set timing, size, movement, and damage settings.
    - Ensure `Generate Storm On Game Start` = **No** for manual control.

3. **Create & Build Verse Script**
    - In Verse Explorer, create a new file (e.g., `basic_storm_controller_example.verse`).
    - Paste and save the example code.
    - In UEFN, go to **Verse → Build Verse Code** or press `CTRL+SHIFT+B` until it shows "Build Succeeded".

4. **Place & Assign Verse Device**
    - Drag the Verse device into the world.
    - In the Details panel, assign:
        - `StormController` to your `basic_storm_controller_device`
        - `GenerateButton` and `DestroyButton` to your button devices

5. **Test Gameplay**
    - Start a session. Press `GenerateButton` to start the storm, and `DestroyButton` to clear it.
    - Watch as the storm shrinks, deals damage, and ends as configured.

---

## 🧠 Best Practices
- Combine with elimination zones for tight arena combat.
- Adjust damage and shrink times to create different levels of pressure.
- Call `.GenerateStorm()` only when auto-start is disabled.

---

## ❌ Incorrect Usage Examples & Fixes
| Issue | ❌ Wrong Example | ✅ Correct Example | Explanation |
|-------|----------------------|------------------------|-------------|
| Not disabling auto-start | Left `Generate Storm on Game Start` = Yes | Set it to **No** | Required for Verse control to function |
| Overlapping storms | Multiple devices in same location | Spread out devices | Each storm device acts independently |
| Not subscribing to events | Inspected event only | Use `.Subscribe(...)` | Needed to trigger functions |
| Blank references | Left `@editable` fields blank | Fill in all references | Required for runtime interaction |

---

## 🔹 Notes
- For **multi-phase storms**, use `advanced_storm_controller_device` and `advanced_storm_beacon_device`.
- Combine with scoring, UI, and elimination logic for engaging and dynamic matches.

