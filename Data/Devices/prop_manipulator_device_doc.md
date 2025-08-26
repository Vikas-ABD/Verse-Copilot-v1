## prop_manipulator_device – UEFN Verse Device Documentation

### 🔊 Description
The `prop_manipulator_device` lets you programmatically control properties of static props within a defined zone in your Fortnite island. You can change props’ visibility (show/hide), health, destructibility, and resource node status. The device is essential for puzzles, dynamic arenas, evolving environments, and prop-based mechanics responding to triggers or Verse logic.

### 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
```

### 🔗 Inheritance Hierarchy
- `creative_object`: Base class for creative devices and props.
- `creative_device_base`: Base class for `creative_device`.
- `prop_manipulator_device`

### 🧩 Core Methods & Events
| Name / Function                | Type / Signature        | Description                                                        |
|-------------------------------|-------------------------|--------------------------------------------------------------------|
| `Enable()`                    | `void`                  | Enables the device (props can then be manipulated by events/Verse).|
| `Disable()`                   | `void`                  | Disables the device (props revert/cannot be manipulated).          |
| `HideProps()`                 | `void`                  | Hides all props affected by this device.                           |
| `ShowProps()`                 | `void`                  | Shows all hidden props controlled by this device.                  |
| `RestoreHealth()`            | `void`                  | Restores health of affected props.                                 |
| `ExhaustResources()`         | `void`                  | Depletes all harvestable resources from props in device zone.      |
| `RestockResources()`         | `void`                  | Refills depleted prop resources.                                   |
| `SetResourceOverridesActive()`| `void`                 | Props use device-specified resource settings.                      |
| `DisableResourceNodeOverrides()`| `void`               | Props use original/default resource settings.                      |
| `DamagedEvent`               | `listenable(agent)`     | Fired when a prop in the zone is damaged; sends damaging agent.    |
| `DestroyedEvent`             | `listenable(agent)`     | Fired when a controlled prop is destroyed; sends responsible agent.|

### 🎛 Configuration Options (Details Panel)
| Option                    | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| Enabled at Game Start     | Should device start enabled/on?                                             |
| Start Hidden              | Props are hidden at match start.                                            |
| Override Resources        | Device controls prop resource settings; reveals further resource options.   |
| Resource Node Options     | Available, Given, Type, Depletion Mode, Restock Time                        |
| Priority                  | If zones overlap, highest priority takes control.                           |
| Affects All in Zone       | Creates a 3D zone with width, depth, height (affected props inside zone only)|
| Zone Dimensions           | Width, Depth, Height (in tiles) if Affects All In Zone is On.               |

> Configure every option in the device’s Details panel before runtime as needed.

### 🛠 Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example: controlling props with prop manipulator
prop_manipulator_example := class(creative_device):

    @editable
    PropManipulator : prop_manipulator_device = prop_manipulator_device{}

    @editable
    ShowButton : button_device = button_device{}

    @editable
    HideButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to button interactions
        ShowButton.InteractedWithEvent.Subscribe(OnShowPressed)
        HideButton.InteractedWithEvent.Subscribe(OnHidePressed)

    # Button handlers
    OnShowPressed(Agent : agent) : void =
        PropManipulator.ShowProps()
        Print("Props shown!")

    OnHidePressed(Agent : agent) : void =
        PropManipulator.HideProps()
        Print("Props hidden!")
```

### 🧠 How It Works
- Place a `prop_manipulator_device` in your level.
- In the Details panel, define the affected zone, resource overrides, start state, priority, and other behavior.
- Reference the device in Verse using `@editable`.
- Use buttons or triggers to control show/hide and other states.

### 🧬 Best Practices
- Use “Priority” to avoid conflicts when multiple manipulator zones overlap the same prop.
- Use resource overrides for custom harvesting/loot scenarios.
- Hide or restore props for path puzzles, resets, or destructible covers.
- Combine with triggers/buttons to make the environment feel dynamic and interactive.
- Use event subscriptions (DamagedEvent, DestroyedEvent) to trigger further in-game effects or logic.

### ❌ Common Usage Issues & Fixes
| Issue                   | ❌ Wrong Example                       | ✅ Correct Example                                   | Explanation                                                    |
|------------------------|-------------------------------------------|--------------------------------------------------------|----------------------------------------------------------------|
| Not linking by @editable| Code calls device w/o assignment         | Always reference via @editable and set in Details panel| Prevents nil/error control calls                              |
| Not setting correct zone| Forget to set zone in Details            | Always set zone/size if using “Affects All...”        | No props will be affected if not inside zone                  |
| Overlapping manipulators| Zones overlap, odd behaviors             | Raise priority on the intended controller              | Highest priority wins for overlapped props                    |

### 🖊 Notes
- Most properties reset if you call `Disable()`.
- Combine with round logic, Victory/End/Score devices, or player switches.
- For advanced effects (e.g., moving props), use `prop_spawner` or custom logic.

