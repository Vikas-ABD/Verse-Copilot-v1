## Attribute Evaluator Device – UEFN Verse Device Documentation

### 🔹 Description
The `attribute_evaluator_device` allows testing attributes (such as eliminations, team, class, score, etc.) of agents (players/AI) at runtime. When signaled by another device (e.g., button, trigger), it evaluates the configured conditions. Based on the outcome, it broadcasts either a `PassEvent` or a `FailEvent`.

Use this device for:
- Conditional logic
- Gated areas
- Objectives
- Dynamic branching gameplay

### 🛠️ Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `trigger_base_device`
- `attribute_evaluator_device`

### 🧩 Data Members (Events)
| Name       | Type                | Description                                      |
|------------|---------------------|--------------------------------------------------|
| PassEvent  | listenable(agent)   | Fires when the agent passes all attribute checks |
| FailEvent  | listenable(agent)   | Fires when the agent fails one or more checks    |

### 🛠️ Functions & Methods
| Name                    | Description                                                             |
|-------------------------|-------------------------------------------------------------------------|
| Enable()                | Activates the device to receive and process signals                      |
| Disable()               | Deactivates the device                                                   |
| EvaluateAgent(Agent)    | Tests agent and triggers PassEvent or FailEvent                         |
| SetMaxTriggerCount()    | Sets max number of triggers (0 = unlimited)                             |
| GetMaxTriggerCount()    | Retrieves max trigger count setting                                     |
| SetResetDelay()         | Sets cooldown before device can re-trigger                             |
| SetTransmitDelay()      | Sets delay before broadcasting signal after trigger                    |
| GetTriggerCountRemaining() | Returns remaining triggers before disable                          |
| Reset()                 | Resets the device's trigger count                                       |
| GetTransform()          | Gets position, rotation, and scale                                      |
| MoveTo()/TeleportTo()   | Moves or teleports the evaluator                                        |

### 📊 Configuration Options (Details Panel)
| Option                     | Description                                                        |
|----------------------------|--------------------------------------------------------------------|
| Activating Team/Class      | Restricts which agents can trigger evaluation                      |
| Min Player Eliminations    | Minimum eliminations required to pass                              |
| Tracked Stat               | Stat used for Min Player/Team Stat check                           |
| Min Player/Team Stat       | Minimum stat value required to pass                                |
| Enabled at Game Start      | Whether the device starts in enabled state                         |
| Times Can Trigger          | Max number of times device can be triggered                        |
| Trigger Delay/Reset Delay  | Delay for evaluation and reactivation                              |
| Visible in Game/VFX/SFX    | Toggle visibility and effects during gameplay                      |

### 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

attribute_evaluator_example := class(creative_device):

    @editable
    AttributeEvaluator : attribute_evaluator_device = attribute_evaluator_device{}

    @editable
    EvaluateButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        AttributeEvaluator.PassEvent.Subscribe(OnPass)
        AttributeEvaluator.FailEvent.Subscribe(OnFail)
        EvaluateButton.InteractedWithEvent.Subscribe(OnEvaluatePressed)

    OnPass(Agent : agent) : void =
        Print("Agent passed attribute evaluation!")

    OnFail(Agent : agent) : void =
        Print("Agent failed attribute evaluation!")

    OnEvaluatePressed(Agent : agent) : void =
        AttributeEvaluator.EvaluateAgent(Agent)
        Print("Evaluating agent attributes...")
```

### ⚖️ How to Use in UEFN
1. **Place Devices in Level**
   - Add `attribute_evaluator_device`
   - Add a `button_device` or other signal device

2. **Configure Attribute Checks** (Details Panel)
   - Set restrictions like team, class, score, eliminations
   - Define if the device starts enabled
   - Adjust delays, FX/SFX, and trigger count

3. **Create and Build Verse Script**
   - Create a new file (e.g., `attribute_evaluator_example.verse`)
   - Paste and save the code
   - Build: `Verse → Build Verse Code` or `CTRL+SHIFT+B`

4. **Place and Assign Verse Device**
   - Add the Verse device to the level
   - Assign `AttributeEvaluator` and `EvaluateButton` in the Details panel

5. **Test and Iterate**
   - Launch the game
   - Press the button or signal the device
   - Check for `PassEvent` or `FailEvent`
   - Connect these to additional gameplay logic

### 🧠 Best Practices
- Chain with other devices for complex logic
- Handle both `PassEvent` and `FailEvent`
- Use reset/delay settings for better performance
- Combine with item granters, eliminators, doors, etc.

### ❌ Incorrect Usage Examples
| Issue                         | ❌ Wrong Example                                | ✅ Correct Example                                        | Explanation                                           |
|------------------------------|--------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------|
| Forgetting `.Subscribe()`    | `AttributeEvaluator.PassEvent`                  | `AttributeEvaluator.PassEvent.Subscribe(OnPass)`            | Must subscribe to listenable events                   |
| Wrong type in `.EvaluateAgent` | `AttributeEvaluator.EvaluateAgent(Player)`     | `AttributeEvaluator.EvaluateAgent(Agent)`                  | Must pass correct `agent` type                        |
| No configuration set         | All checks left at default                      | Set appropriate attribute checks in the Details panel       | Defaults to always pass if no checks are configured   |
| Trigger limit not reset      | Never call `Reset()` after limit reached       | Use `Reset()` to enable reuse                              | Needed if trigger count is limited                    |
| Editable refs not assigned   | Editable fields left blank                     | Set both `AttributeEvaluator` and `EvaluateButton` refs     | Devices must be wired for script to function          |

### 💭 Note
- The device evaluates agent state as of the triggering event.
- For rapidly changing values (e.g., eliminations), timing and event ordering is critical.
- Attribute logic is set in the Details panel. Verse only controls trigger and event response.

