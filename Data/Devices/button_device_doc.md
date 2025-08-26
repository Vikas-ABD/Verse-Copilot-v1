# button_device – UEFN Verse Device Documentation

## 🔹 Description
The `button_device` creates an interactive button that agents (players or AI) can press to trigger events, activate other devices, or run Verse code. You can configure its interaction time, team/class restrictions, triggers count, delays, and visible text. It's a core tool for building puzzles, switches, objective controls, and player-driven interactions in your island.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- creative_object
- creative_device_base
- button_device

## 🧹 Data Members (Events)
| Name | Type | Description |
|------|------|-------------|
| InteractedWithEvent | listenable(agent) | Fires when an agent successfully interacts (holds) with the button for the configured time. Provides the triggering agent. |

## 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| Enable() | Activates the button; agents can interact with it. |
| Disable() | Deactivates the button; ignores all interaction attempts. |
| SetInteractionText(text) | Sets the text that shows to agents when looking at the button (≤64 chars). |
| SetInteractionTime(time) | Changes how long agent must interact to activate (seconds; instant–10s). |
| SetMaxTriggerCount(count) | Sets how many activations before disable (0=infinite; max 10). |
| GetInteractionTime() | Returns current interaction time (seconds). |
| GetMaxTriggerCount() | Returns the trigger limit for this button (0=infinite). |
| GetTriggerCountRemaining() | Returns number of activations left (0 if unlimited). |
| Reset() | Resets usage count and re-enables the button if it was disabled by trigger limit. |
| TeleportTo()/MoveTo() | Instantly move or animate the button to a new world position. |

## 🎛 Configuration Options (Details Panel)
- **Interact Time:** How long to interact before triggering ("Instant"–10 seconds).
- **Activating Team/Class:** Limit which teams/classes can use this button (with inverse option).
- **Times Can Trigger:** How many times button works before disabling (Infinite/1–10).
- **Delay:** Time to wait before executing triggered actions.
- **Reset Delay:** Cooldown after use before button can be activated again.
- **Trigger Sound:** Plays sound when button triggered.
- **Interaction Text:** Text displayed when agent looks at the button (64-char limit).
- **Visible During Game:** On/Off show button model in game; off for prop interactions.
- **Interaction Radius:** How close agent must be to interact.
- **Enabled at Game Start:** Start enabled/disabled.

## 🧩 Events & Direct Event Binding
- Can directly bind to other devices in the Details (“On Interact, Send Event To”) for no-coding device interactions.
- In Verse, use `InteractedWithEvent.Subscribe(...)` to run custom gameplay logic.

## 🪠 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

button_device_example := class(creative_device):

    @editable
    Button : button_device = button_device{}

    @editable
    TargetDevice : trigger_device = trigger_device{} # Use trigger_device for triggering actions

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    SetTextButton : button_device = button_device{}

    @editable
    SetTimeButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        Button.InteractedWithEvent.Subscribe(OnButtonPressed)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        SetTextButton.InteractedWithEvent.Subscribe(OnSetTextPressed)
        SetTimeButton.InteractedWithEvent.Subscribe(OnSetTimePressed)

        Print("Button max trigger count: {Button.GetMaxTriggerCount()}")
        Print("Button interaction time: {Button.GetInteractionTime()}")

    OnButtonPressed(Agent : agent) : void =
        Print("Button pressed by agent!")
        TargetDevice.Trigger(Agent)

    OnEnablePressed(Agent : agent) : void =
        Button.Enable()
        Print("Button enabled!")

    OnDisablePressed(Agent : agent) : void =
        Button.Disable()
        Print("Button disabled!")

    OnSetTextPressed(Agent : agent) : void =
        Button.SetInteractionText(StringToMessage("Press to Activate"))
        Print("Button interaction text set!")

    OnSetTimePressed(Agent : agent) : void =
        Button.SetInteractionTime(2.0)
        Print("Button interaction time set to 2.0 seconds!")

    StringToMessage<localizes>(InString : string) : message = "{InString}"
```

## 🧬 How it works in UEFN:
1. **Place Devices in Level:**
   - Drag your `button_device` into your island.
   - Add any target devices you want to trigger (e.g. doors, item spawners, trigger devices).
   - Add more `button_device`s if you want to enable, disable, or reconfigure your main button at runtime.

2. **Configure the Device (Details Panel):**
   - Adjust `Interact Time`, `Allowed Team/Class`, `Trigger Count`, `Text`, all appearance, sound, and trigger options.

3. **Create & Build Verse Script:**
   - In Verse Explorer: right-click a folder, **Create New Verse File** (e.g., `button_device_example.verse`), and open in VS Code.
   - Paste the example code, save.
   - In UEFN, click **Verse → Build Verse Code** (or CTRL+SHIFT+B) until “Build Succeeded”.

4. **Place & Reference Devices:**
   - Drag your Verse device (`button_device_example`) into your map.
   - Assign all `@editable` fields (Button, TargetDevice, EnableButton, etc.) to your placed devices via the Details panel.

5. **Test Gameplay:**
   - Launch a session and interact with the button to activate the wired device(s), see log messages, and test enabling/disabling/text/time changes via your Verse logic.

## 🧠 Best Practices
- Combine with device/class/team restrictions for role-based or team-specific puzzles/objectives.
- Use `.Enable()`/`.Disable()` for progressive unlocks or mission logic.
- Use `.Reset()` to reuse button after reaching trigger-count limit.
- Dynamically update interaction time and text for changing gameplay.
- For instant triggers, set interaction time to 0 or "Instant".

## ❌ Common Issues & Fixes
| Issue | ❌ Wrong Example | ✅ Correct Example | Explanation |
|-------|----------------------|------------------------|-------------|
| Leaving device unassigned | Did not assign Button in Verse @editable | Assign all device references in Details panel after placement | Verse code needs proper device references |
| Not subscribing to event | Checked `.InteractedWithEvent` only | Use `.InteractedWithEvent.Subscribe(OnButtonPressed)` | Must subscribe to handle button press in Verse |
| Overusing text length | Set >64 chars for interaction text | Keep text short (≤64) | Exceeds device display limit |
| Wanting multiple triggers in event binding | Bound multiple On Interact in Details panel | Use Verse to handle complex event chains | Direct event binding supports multi-target, or use Verse for custom |

## 📅 Note
- For simple activation, wiring via editor event binding is fastest.
- Use Verse code and `.InteractedWithEvent.Subscribe(...)` for intricate or linked gameplay sequences.
- All device and interaction restrictions (team/class/etc.) are set in the Details panel and cannot be changed by Verse after play begins.

