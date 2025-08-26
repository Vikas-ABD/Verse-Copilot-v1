📘 score_manager_device – UEFN Verse Device Documentation

🔹 Description
The score_manager_device lets you manipulate player scores using in-game triggers, Verse code, or device interactions. It supports adding, subtracting, and setting score values, as well as resetting, enabling/disabling, and providing HUD feedback. When “Activating Team” is configured to a specific team, only agents on that team (using the agent overloads) will be able to affect the score manager’s state.

🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

🔗 Inheritance Hierarchy
- creative_object
- creative_device_base
- score_manager_device

🧩 Events (Data Members)
| Name               | Type                | Description                                          |
|--------------------|---------------------|------------------------------------------------------|
| MaxTriggersEvent   | listenable(agent)   | Signaled when the device reaches its max trigger count |
| ScoreOutputEvent   | listenable(agent)   | Signaled whenever the device awards points to agent  |

🛠️ Functions & Methods
All overloads marked with `agent` are required when "Activating Team" is set for the device.

| Name                         | Description                                                      |
|------------------------------|------------------------------------------------------------------|
| Activate(agent) / Activate() | Grants points – use agent overload if team-restricted            |
| Reset(agent) / Reset()       | Resets score manager state and counters/triggers                 |
| Enable(agent) / Enable()     | Enables the device; agent overload checks team                  |
| Disable(agent) / Disable()   | Disables the device                                              |
| Increment(agent) / Increment() | Increments score value by 1 for next activation               |
| Decrement(agent) / Decrement() | Decrements score value by 1 for next activation              |
| SetScoreAward(Value:int)     | Sets score to be awarded by next activation                     |
| GetScoreAward()              | Gets score to be awarded by next activation                     |
| SetToAgentScore(agent)       | Sets next award value to agent’s current score                  |
| GetCurrentScore(agent)       | Returns the agent’s current score                               |

🎛 Configuration Options (Details Panel)
| Option Name                  | Description                                                     |
|------------------------------|------------------------------------------------------------------|
| Score Value                  | Base score awarded on activation                                 |
| Score Award Type             | Add, Subtract, Set (method of awarding score)                    |
| Activating Team              | Restrict to specific team (requires agent overloads)             |
| Times Can Trigger            | Set trigger limit (infinite or fixed)                            |
| Increment Score on Awarding | Auto-increment between triggers                                 |
| Score Change When Activated | Modify score per activation after first                         |
| Minimum/Maximum Score        | Clamp score range per activation                                |
| Enable/Disable During Phase  | Restrict to phases like Pre-game, Gameplay, etc.                |
| Display Score Update on HUD  | Show score updates in HUD                                       |
| Score HUD Message & Color    | Customize HUD feedback                                           |

🧪 Events
| Event             | When It Fires                                       |
|-------------------|------------------------------------------------------|
| MaxTriggersEvent  | When activation limit is reached                    |
| ScoreOutputEvent  | When awarding points to an agent                    |

🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

score_manager_example := class(creative_device):

    @editable
    ScoreManager : score_manager_device = score_manager_device{}

    @editable
    AddScoreButton : button_device = button_device{}

    @editable
    SetScoreButton : button_device = button_device{}

    @editable
    ResetScoreButton : button_device = button_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        AddScoreButton.InteractedWithEvent.Subscribe(OnAddScore)
        SetScoreButton.InteractedWithEvent.Subscribe(OnSetScore)
        ResetScoreButton.InteractedWithEvent.Subscribe(OnResetScore)
        EnableButton.InteractedWithEvent.Subscribe(OnEnable)
        DisableButton.InteractedWithEvent.Subscribe(OnDisable)

    OnAddScore(Agent : agent) : void =
        ScoreManager.Activate(Agent)
        Print("Added 10 to score for agent")

    OnSetScore(Agent : agent) : void =
        ScoreManager.Activate(Agent)
        Print("Set score to 100 for agent")

    OnResetScore(Agent : agent) : void =
        ScoreManager.Reset(Agent)
        Print("Reset score for agent")

    OnEnable(Agent : agent) : void =
        ScoreManager.Enable()
        Print("Score manager enabled")

    OnDisable(Agent : agent) : void =
        ScoreManager.Disable()
        Print("Score manager disabled")
```

Explanation:
- Reference score_manager_device and five button_devices (Add, Set, Reset, Enable, Disable).
- Each button calls a score operation for the local agent (especially important if "Activating Team" is used).
- Use Activate(Agent) to award points, Reset(Agent) to reset, etc.
- Enable/Disable toggles the device’s operational state.

🧠 How to Use in UEFN
1. Place the Score Manager Device
   - Drag a score_manager_device into the level.
   - Configure options in the Details panel.

2. Add Control Buttons (Optional)
   - Place five button_devices for demo control.

3. Create Your Verse Device
   - In Verse Explorer: Create new file (e.g., score_manager_example.verse), paste code.
   - Build the code (Ctrl+Shift+B) until build succeeds.

4. Assign Device References
   - In Details panel: link ScoreManager and buttons to actual devices.

5. Test and Customize
   - Launch play session and use buttons to test.
   - Use HUD options and agent checks as needed.

🧠 Best Practices
- Always use agent overloads if device is team-restricted.
- Use ScoreOutputEvent for rewards or tracking.
- Enable HUD feedback for clear player communication.
- Reset and clamp scores to prevent issues.

❌ Common Issues & Solutions
| Issue                     | Problem                       | Solution                                         |
|---------------------------|-------------------------------|--------------------------------------------------|
| Score manager inactive    | Not enabled                   | Use .Enable() or set enabled in Details panel    |
| Team restriction ignored  | Didn't use agent overloads    | Use agent overloads for all interactions         |
| No score update shown     | HUD display not enabled       | Turn on Display Score Update in Details          |
| Device won't trigger      | Trigger limit exceeded        | Increase limit or reset via Verse                |

Note:
- All score behaviors can be controlled in-game via Verse or the Details panel.
- Use ScoreOutputEvent to hook into custom logic (leaderboards, rewards, etc.).

