## movement_modulator_device – UEFN Verse Device Documentation

### 🔹 Description
The `movement_modulator_device` is used to temporarily modify the speed of agents (players) and vehicles. When activated—by player touch, drive-over, Verse logic, or device wiring—it can provide a speed boost or slowdown, apply impulses (for bouncing or launching), and visually indicate its effect both on the device and the affected entity. Effects are configurable in power and duration, can be set to infinite, and can be enabled/disabled or triggered via Verse.

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `movement_modulator_device`

### 🧩 Data Members (Events)
| Name | Type | Description |
|------|------|-------------|
| ActivationEvent | listenable(agent) | Fires when the device is activated by an agent (player or vehicle driver). |

### 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| `Activate(agent)` | Applies the configured movement effect to the given agent. |
| `Enable()` | Enables the device so it can be triggered or activated. |
| `Disable()` | Disables the device; no effect or activation possible. |
| `GetTransform()` | Gets the device’s world transform. |
| `MoveTo()` / `TeleportTo()` | Animates/moves or teleports the device. |

### 🎛 Configuration Options (Details Panel)
- **Speed**: Multiplier for speed (1 = unchanged; >1 = boost; <1 = slowdown).
- **Affect Movement Speed**: On/Off — whether player speed is affected.
- **Infinite Duration**: Whether speed change lasts forever (else, set duration).
- **Effect Duration**: How long the speed boost/slow lasts (in seconds).
- **Apply Impulse**: If On, can launch the player/vehicle (extra bounce/jump).
- **Forward/Upward Impulse**: Sets amount of push/vertical kick delivered.
- **Apply Upward Impulse to Non-Characters**: Whether impulse lifts vehicles/objects.
- **Enabled During Phase**: None, Always, Pre-Game, or Gameplay.
- **Reset Delay**: Time before device resets/re-triggers.
- **Visible During Game**: Sets if device is invisible, FX-only, or fully visible.
- **Team/Class Filtering**: Restrict which teams/classes may trigger or be affected.

### 🧺 Events Overview
| Event | When It Fires |
|-------|----------------|
| `ActivationEvent` | When an agent activates/enters the device |

### 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

movement_modulator_example := class(creative_device):

    @editable
    MovementModulator : movement_modulator_device = movement_modulator_device{}

    @editable
    ActivateButton : button_device = button_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        MovementModulator.ActivationEvent.Subscribe(OnModulatorActivated)
        ActivateButton.InteractedWithEvent.Subscribe(OnActivatePressed)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnModulatorActivated(Agent : agent) : void =
        Print("Movement modulator activated by agent!")

    OnActivatePressed(Agent : agent) : void =
        MovementModulator.Activate(Agent)
        Print("Movement modulator activated for agent!")

    OnEnablePressed(Agent : agent) : void =
        MovementModulator.Enable()
        Print("Movement modulator enabled!")

    OnDisablePressed(Agent : agent) : void =
        MovementModulator.Disable()
        Print("Movement modulator disabled!")
```

### 📅 How to Use in UEFN
1. **Place the Device**
   - Drag a `movement_modulator_device` into your level.

2. **Configure Device Options (Details Panel)**
   - Set `Speed`, `Effect Duration`, `Apply Impulse`, visibility, filtering, etc.

3. **Add Button Devices for Demo/Control (Optional)**
   - Add three `button_device` actors.

4. **Create Your Verse Device**
   - In Verse Explorer, create a new file (e.g., `movement_modulator_example.verse`).
   - Paste in the example code, build the Verse code.

5. **Place and Assign Your Verse Device**
   - Place the Verse device in your world.
   - Assign the MovementModulator and Button references in the Details panel.

6. **Test the Device**
   - Playtest the map. Trigger buttons and step on the modulator to test effects.

### 🧠 Best Practices
- Adjust color/FX for clarity.
- Use multiple devices for course design.
- Filter effects to teams or classes.
- Combine with triggers for advanced logic.

### ❌ Common Issues & Fixes
| Issue | ❌ Mistake | ✅ Fix | Explanation |
|-------|----------------|-----------|-------------|
| No speed effect | Wrong speed/duration values | Configure multiplier/duration | Requires correct settings |
| Not triggering | Incorrect agent reference | Use correct `agent` from event | Agent must be specified |
| Doesn’t affect vehicle | Filtering/impulse not set | Enable impulse to non-characters | Must allow vehicle effect |
| @editable not working | References not assigned | Set in Details panel | Required for Verse linkage |

### 💡 Notes
- Ideal for courses, powerups, and action areas.
- Speed effects are momentary unless "Infinite Duration" is enabled.
- Fine-tune `Speed` and `Effect Duration` for gameplay balance.

