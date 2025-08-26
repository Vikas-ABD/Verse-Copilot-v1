## rng\_device – UEFN Verse Device Documentation

### 🔊 Description

The `rng_device` (Random Number Generator device) generates a random integer between two configurable values:

- **Value Limit 1**: Minimum value (inclusive)
- **Value Limit 2**: Maximum value (inclusive)

The device can be triggered to generate a random number. It signals events when numbers are generated, when the minimum or maximum value is rolled, and for custom-defined win/lose thresholds. This device is useful for dice rolls, chance-based events, minigames, and random selection logic.

### 🧱 Verse Using Statement

```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy

- `creative_object`
- `creative_device_base`
- `rng_device`

### 🛠️ Functions & Methods

| Name              | Description                                                     |
| ----------------- | --------------------------------------------------------------- |
| `Activate(agent)` | Generates a random number for the given agent and fires events. |
| `Activate()`      | Generates a random number without an instigator.                |
| `Cancel()`        | Cancels active number generation (if any).                      |
| `Enable()`        | Enables the device.                                             |
| `Disable()`       | Disables the device, preventing activation.                     |

### 🥩 Events

| Name             | Type           | Description                                       |
| ---------------- | -------------- | ------------------------------------------------- |
| `RolledMinEvent` | `listenable()` | Fired when generated number equals minimum value. |
| `RolledMaxEvent` | `listenable()` | Fired when generated number equals maximum value. |
| `WinEvent`       | `listenable()` | Fired when number >= Winning Value.               |
| `LoseEvent`      | `listenable()` | Fired when number < Winning Value.                |

### 🎛 Configuration Options (Details Panel)

| Option Name           | Description                                            | Default |
| --------------------- | ------------------------------------------------------ | ------- |
| Value Limit 1         | Sets the minimum roll value.                           | 0       |
| Value Limit 2         | Sets the maximum roll value.                           | 6       |
| Winning Value         | WinEvent triggers if result >= this value.             | 4       |
| Pick Each Number Once | Ensures all numbers are rolled before repeats.         | No      |
| Roll Time             | Duration before outcome is revealed.                   | Instant |
| Reset After Use       | Resets after each use or disables device.              | On      |
| Award Score           | When to award score (Never, Always, On Win, On Loss).  | Never   |
| Result Multiplier     | Multiplies the result for scoring.                     | 1       |
| Score Type            | Defines how the score is applied (Add, Replace, etc.). | Add     |
| *(and more...)*       | Additional settings available in UEFN Details Panel.   |         |

### 🛠️ Verse Usage Example

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use rng_device
rng_device_example := class(creative_device):

    @editable
    RNGDevice : rng_device = rng_device{}

    @editable
    RollButton : button_device = button_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to RNG events
        RNGDevice.RolledMinEvent.Subscribe(OnRolledMin)
        RNGDevice.RolledMaxEvent.Subscribe(OnRolledMax)
        RNGDevice.WinEvent.Subscribe(OnWin)
        RNGDevice.LoseEvent.Subscribe(OnLose)

        # Subscribe to button events
        RollButton.InteractedWithEvent.Subscribe(OnRollPressed)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnRolledMin() : void =
        Print("Rolled minimum value!")

    OnRolledMax() : void =
        Print("Rolled maximum value!")

    OnWin() : void =
        Print("Win event triggered!")

    OnLose() : void =
        Print("Lose event triggered!")

    OnRollPressed(Agent : agent) : void =
        RNGDevice.Activate(Agent)
        Print("RNG roll activated!")

    OnEnablePressed(Agent : agent) : void =
        RNGDevice.Enable()
        Print("RNG device enabled!")

    OnDisablePressed(Agent : agent) : void =
        RNGDevice.Disable()
        Print("RNG device disabled!")
```

### 📊 How to Use in UEFN

1. **Place the RNG Device**

   - Drag an `rng_device` into your level.

2. **Configure Options**

   - Use the Details panel to set Value Limits, Winning Value, Roll Time, etc.

3. **Add Control Buttons (Optional)**

   - Add three `button_device` actors for Roll, Enable, and Disable.

4. **Create and Build Verse Device**

   - In Verse Explorer: Right-click → Create New Verse File (e.g., `rng_device_example.verse`)
   - Paste the example code and save.
   - Use `Build Verse Code` (Ctrl+Shift+B) until you see "Build Succeeded".

5. **Assign References**

   - In your placed Verse device, assign:
     - `RNGDevice` → your `rng_device`
     - `RollButton`, `EnableButton`, `DisableButton` → your buttons

6. **Test in Play**

   - Test rolling and responding to events using the UI buttons and logs.

### 🧠 Best Practices

- Configure limits and scoring logic to suit gameplay (e.g., dice, slot machine).
- Only subscribe to events that are necessary for performance.
- Use a combination of Verse logic and event wiring for interactive logic.

### ❌ Common Issues & Solutions

| Issue                    | Problem (❌)                               | Solution (✅)                                               |
| ------------------------ | ----------------------------------------- | ---------------------------------------------------------- |
| Device won’t roll        | Not enabled or disabled by mistake        | Ensure `.Enable()` is called or device is enabled manually |
| Event actions not firing | Events not subscribed or setup in Verse   | Subscribe to all desired events in Verse explicitly        |
| Reference errors         | `@editable` refs not set in Details panel | Assign all required fields in your placed Verse device     |

**Note**: All events must be subscribed to via Verse or device wiring for them to work.

Configure the device thoroughly and combine it with creative logic to enhance interactivity and chance-based gameplay!

