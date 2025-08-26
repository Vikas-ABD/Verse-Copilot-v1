📘 vine_rail_device – UEFN Verse Device Documentation

🔹 Description
The vine_rail_device is a specialized grind rail device in Unreal Editor for Fortnite (UEFN) that creates a Vine-style Grind Rail. It allows players to grind along rails themed as vines, ideal for jungle, adventure, or nature-inspired islands. The rail’s shape, color, visibility, and availability can be dynamically controlled via Verse. All grinding/activity events can also be scripted.

🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

🔗 Inheritance Hierarchy
- creative_object
- creative_device_base
- grind_rail_device
- vine_rail_device

🛠️ Key Methods & Functions
| Method          | Description                                                    |
|----------------|----------------------------------------------------------------|
| Enable()       | Players can grind on the vine rail.                            |
| Disable()      | Prevents grinding; rail may remain visible.                    |
| Show()         | Makes the vine rail visible (players can see it).              |
| Hide()         | Makes the vine rail invisible (optionally still grindable).    |
| GetTransform() | Returns the rail’s world transform (location/rotation/scale).   |
| MoveTo() / TeleportTo() | Animates or teleports the vine rail to a new place.     |

🧹 Events (Data Members)
| Name                 | Type               | When It Fires                          |
|----------------------|--------------------|----------------------------------------|
| StartedGrindingEvent | listenable(agent)  | When a player starts grinding on rail. |
| EndedGrindingEvent   | listenable(agent)  | When a player ends grinding on rail.   |

🛋️ Device Configuration (Details Panel)
- **Visual Style**: Set to "Vine"
- **Vine Tip Type**: Bush / Flat
- **Apply Vine Moss**: On/Off toggle
- **Enable During Phase**: Choose gameplay phase for activation
- **Visible During Phase**: Choose visibility phase

🪰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

vine_rail_example := class(creative_device):

    @editable
    RailDevice : vine_rail_device = vine_rail_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    ShowButton : button_device = button_device{}

    @editable
    HideButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        RailDevice.StartedGrindingEvent.Subscribe(OnStartedGrinding)
        RailDevice.EndedGrindingEvent.Subscribe(OnEndedGrinding)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        ShowButton.InteractedWithEvent.Subscribe(OnShowPressed)
        HideButton.InteractedWithEvent.Subscribe(OnHidePressed)

    OnStartedGrinding(Agent : agent) : void =
        Print("Agent started grinding on vine rail!")

    OnEndedGrinding(Agent : agent) : void =
        Print("Agent ended grinding on vine rail!")

    OnEnablePressed(Agent : agent) : void =
        RailDevice.Enable()
        Print("Vine rail enabled!")

    OnDisablePressed(Agent : agent) : void =
        RailDevice.Disable()
        Print("Vine rail disabled!")

    OnShowPressed(Agent : agent) : void =
        RailDevice.Show()
        Print("Vine rail shown!")

    OnHidePressed(Agent : agent) : void =
        RailDevice.Hide()
        Print("Vine rail hidden!")
```

**Explanation:**
- **RailDevice**: Reference your placed vine_rail_device.
- **Enable/Disable/Show/HideButton**: Button devices wired via @editable.
- **Events**: Subscribes to StartedGrindingEvent and EndedGrindingEvent for custom responses.
- **Visibility vs Access**: Show/Hide controls visuals, Enable/Disable controls grindability.

🔧 How to Use in UEFN
1. **Place Devices in Your Level**
   - Add a vine_rail_device (Devices > Grind Rails > Vine Rail).
   - Add four button_device actors (Enable, Disable, Show, Hide).

2. **Configure Vine Rail in Details Panel**
   - Set **Visual Style**: Vine
   - Adjust **Vine Tip Type** and **Apply Vine Moss** as needed
   - Configure **Enable During Phase** and **Visible During Phase**

3. **Create & Add Your Verse Script**
   - Open Verse Explorer (Verse → Verse Explorer)
   - Create New Verse File (e.g., vine_rail_example.verse)
   - Paste code and save
   - Build Verse Code (Ctrl+Shift+B) until "Build Succeeded"
   - Place custom Verse actor and assign all @editable fields

4. **Test & Extend**
   - Play the session
   - Use buttons to test toggles
   - Extend logic for custom gameplay (score, hazards, progression)

🧠 Best Practices
- Use for jungle/forest platforming or traversal.
- Hide rails for surprise/timed mechanics.
- Use grind events for timers, VFX, powerups, scoring.

❌ Common Issues & Fixes
| Problem            | Likely Cause                  | Solution                                         |
|--------------------|-------------------------------|--------------------------------------------------|
| Grind not working  | Rail disabled or wrong phase  | Call Enable() and set "Enable During Phase"     |
| Rail invisible     | Hide() called or phase issue  | Call Show() and check "Visible During Phase"    |
| No events triggered| Event not subscribed properly | Ensure subscription happens in OnBegin()        |

**Notes:**
- Vine rails can be shaped using control points.
- Visibility and grindability are independent.
- Ideal for dynamic jungle traversal, time trials, and challenge-based gameplay.

