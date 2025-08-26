📘 grind_rail_device – UEFN Verse Device Documentation

🔹 Description
The grind_rail_device is used in Unreal Editor for Fortnite (UEFN) to create fully customizable Grind Rails. These let players grind or slip along rails of any shape for fast traversal, stunts, or obstacle course gameplay. Grind rails can be shaped using control points, styled and colored, shown or hidden, enabled or disabled, and all interaction events are available for Verse scripting.

🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

🔗 Inheritance Hierarchy
- creative_object
- creative_device_base
- grind_rail_device

🛠️ Key Methods & Functions
| Method                | Description                                                  |
|-----------------------|--------------------------------------------------------------|
| Enable()              | Allows players to grind on this rail.                        |
| Disable()             | Prevents players from grinding (does not hide the rail).     |
| SetRailColor(color)   | Sets the color of the rail (for Standard style).             |
| Hide()                | Makes the grind rail invisible (may still be usable).        |
| Show()                | Makes the grind rail visible again.                          |
| GetTransform()        | Gets the rail’s transform (location/rotation/scale).           |
| MoveTo()/TeleportTo() | Animates or instantly moves the rail.                        |

🧹 Events (Data Members)
| Name                  | Type                 | When It Fires                                  |
|-----------------------|----------------------|-------------------------------------------------|
| StartedGrindingEvent  | listenable(agent)    | When a player starts grinding on the rail.     |
| EndedGrindingEvent    | listenable(agent)    | When a player stops grinding on the rail.      |

🎛 Device Configuration (Details Panel)
- **Visual Style**: Standard, Wire, Vine, Minerail
- **Rail Color**: Only for Standard style; choose any color
- **Wire Decoration**: For Wire style (None, Patio Lights, Festive Lights)
- **Vine Tip Type**: For Vine style (Bush or Flat)
- **Apply Vine Moss**: For Vine style (On/Off)
- **Enable During Phase**: None / Always / Pre-Game Only / Gameplay Only / Create Only
- **Visible During Phase**: Controls when the rail is visible

🧪 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

grind_rail_example := class(creative_device):

    @editable
    RailDevice : grind_rail_device = grind_rail_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        RailDevice.StartedGrindingEvent.Subscribe(OnStartedGrinding)
        RailDevice.EndedGrindingEvent.Subscribe(OnEndedGrinding)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnStartedGrinding(Agent : agent) : void =
        Print("Agent started grinding!")

    OnEndedGrinding(Agent : agent) : void =
        Print("Agent ended grinding!")

    OnEnablePressed(Agent : agent) : void =
        RailDevice.Enable()
        Print("Grind rail enabled!")

    OnDisablePressed(Agent : agent) : void =
        RailDevice.Disable()
        Print("Grind rail disabled!")
```

**Explanation:**
- **RailDevice**: Reference to placed grind_rail_device
- **Enable/DisableButton**: Button devices to control rail state
- **Events**: Subscribe to grinding events for custom logic
- **Handlers**: Trigger VFX, rewards, timers, elimination, etc.

🔧 How to Use in UEFN
1. **Place Devices**
   - Place grind_rail_device and two button_device actors

2. **Customize the Rail**
   - Adjust rail shape via control points
   - Set Visual Style, Color, and other decorations in Details

3. **Create Verse Script**
   - In Verse Explorer: Right-click > Create New Verse File (e.g., grind_rail_example.verse)
   - Paste code, build (Ctrl+Shift+B) until "Build Succeeded"
   - Place your custom Verse device actor in world

4. **Assign Editable References**
   - In Details panel: Set RailDevice, EnableButton, DisableButton

5. **Test & Extend**
   - Use buttons to test enabling/disabling
   - Check output logs for grind events
   - Expand logic for points, VFX, timers, etc.

🧠 Best Practices
- Use multiple control points for curves and jumps
- Script Enable/Disable for dynamic gameplay (e.g., unlocks)
- Combine handlers with stunts, scoring, VFX, or game phases

❌ Common Issues & Fixes
| Problem                    | Likely Reason                     | Solution                         |
|----------------------------|-----------------------------------|----------------------------------|
| Can’t grind on rail        | Rail is disabled or phase-limited | Use .Enable() and check phase    |
| Visual not updating        | Hide/Show out of sync             | Use .Show() after .Hide()        |
| Interactions not detected  | Event not subscribed or wrong ref | Ensure .Subscribe() is in code   |

**Notes:**
- Rail may be visible but inactive if disabled
- Use Hide() for full invisibility
- All behavior can be scripted for rich gameplay

