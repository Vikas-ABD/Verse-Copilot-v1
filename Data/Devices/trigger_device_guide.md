## trigger_device

### 🔹 Description
The `trigger_device` is a versatile relay that can activate chains of events or devices in your island. It is usually used to fire other devices (doors, traps, mutators, etc.), or as a programmable relay for anything you want to activate or sequence—by player, through Verse, or by another device.

### 📁 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- creative_object
- creative_device_base
- trigger_base_device
- trigger_device

### 🛠️ Main Functions & Methods
| Name                      | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| Enable()                 | Enables the trigger—can be activated.                                       |
| Disable()                | Disables the trigger—ignores signals or player input.                       |
| Trigger()                | Activates the device, firing its `TriggeredEvent` output.                    |
| Trigger(agent)           | Fires with a specific agent as the instigator (optional).                   |
| Reset()                  | Resets activation count.                                                     |
| SetMaxTriggerCount(int) | Sets cap on triggers (0 = no limit, up to 20).                              |
| SetResetDelay(float)    | Cooldown (seconds) before trigger device can be activated again.            |
| GetTriggerCountRemaining() | Number of activations left before device disables or locks out.          |

### 🧹 Events (Data Members)
| Name             | Type            | Description                                        |
|------------------|------------------|----------------------------------------------------|
| TriggeredEvent  | listenable(?agent) | Fires when trigger is activated—sends agent if available. |

### 🎯 Configuration Options (Details Panel)
- Trigger on receive
- Trigger on agent contact
- Enable/disable on game phase
- Trigger delayed
- Link to channels, groups, or Verse code

### 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

trigger_device_example := class(creative_device):

    @editable
    Trigger : trigger_device = trigger_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    TriggerButton : button_device = button_device{}

    @editable
    ResetButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        Trigger.TriggeredEvent.Subscribe(OnTriggered)
        EnableButton.InteractedWithEvent.Subscribe(OnEnable)
        DisableButton.InteractedWithEvent.Subscribe(OnDisable)
        TriggerButton.InteractedWithEvent.Subscribe(OnTrigger)
        ResetButton.InteractedWithEvent.Subscribe(OnReset)

        Trigger.SetMaxTriggerCount(5)
        Trigger.SetResetDelay(2.0)

    OnTriggered(Agent : ?agent) : void =
        Print("Trigger was activated by agent!")
        Remaining := Trigger.GetTriggerCountRemaining()
        Print("Triggers left before cooldown: {Remaining}")

    OnEnable(Agent : agent) : void =
        Trigger.Enable()
        Print("Trigger device enabled.")

    OnDisable(Agent : agent) : void =
        Trigger.Disable()
        Print("Trigger device disabled.")

    OnTrigger(Agent : agent) : void =
        Trigger.Trigger(Agent)
        Print("Trigger device triggered by button.")

    OnReset(Agent : agent) : void =
        Trigger.Reset()
        Print("Trigger device was reset!")
```

### Explanation:
- Subscribes to the trigger’s `TriggeredEvent` and logs the agent triggering it.
- Trigger from code, Button interaction, or any other device.
- Buttons used to enable, disable, trigger, and reset the device.
- Sets trigger limits and delay on startup.

---

### 📆 UEFN Step-by-Step Guide

#### 1. Place Devices in the Level
- Drag a `trigger_device` into your island.
- Add four `button_devices` (optional): Enable, Disable, Trigger, Reset

#### 2. Create the Verse Device
- Open **Verse Explorer** (Top menu: `Verse → Verse Explorer`)
- Right-click a folder → **Create New Verse File** (e.g., `trigger_device_example.verse`)
- Paste the code sample above and save

#### 3. Build
- Click **Verse → Build Verse Code** or press `Ctrl+Shift+B`
- Wait for "Build Succeeded"

#### 4. Place & Assign
- Drag your new Verse device (`trigger_device_example`) into your world
- Assign devices in Details:
  - `Trigger` → your `trigger_device`
  - `EnableButton`, `DisableButton`, `TriggerButton`, `ResetButton`

#### 5. Customize trigger_device in Details
- Set `Max Trigger Count`, `Reset Delay`, interaction type, etc.

#### 6. Test
- Launch or playtest your island
- Use buttons to enable, disable, trigger, or reset
- Observe log outputs and connected device logic

---

### 🧠 Tips
- Chain multiple `trigger_devices` for advanced logic.
- Use channels, agent forwarding, or agent-specific triggers.
- Great for minigames, puzzles, or custom flows.

### ❌ Common Issues & Solutions
| Issue             | Fix                                                       |
|------------------|------------------------------------------------------------|
| Doesn’t activate | Ensure device is enabled and properly linked               |
| No log/event     | Subscribe to `TriggeredEvent` in Verse                    |
| Only works once  | Set higher Max Trigger Count or use Reset() appropriately |

**Note**: The `trigger_device` acts as a universal relay—combine with buttons, zones, timers, or custom Verse logic for powerful in-game mechanics.

