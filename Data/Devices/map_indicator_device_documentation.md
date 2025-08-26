## 📘 map_indicator_device – UEFN Verse Device Documentation

### 🔹 Description
The `map_indicator_device` is used to create custom points of interest and markers on the minimap and overview map in your Fortnite island. With this device, you can help players orient themselves, show objectives, or mark key locations. The indicator’s appearance, visibility per team or class, text, color, icon, and dynamic pulsing can be controlled from the Details panel and via Verse.

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- creative_object
- creative_device_base
- map_indicator_device

### 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| `Enable()` | Shows the marker on the map (for configured teams/classes). |
| `Disable()` | Hides the marker from the map. |
| `ActivateObjectivePulse(agent)` | Starts an animation at the agent’s location pointing to the indicator. |
| `DeactivateObjectivePulse(agent)` | Stops the directional pulse for the agent. |
| `GetTransform()` | Returns the current location, rotation, and scale of the device. |
| `MoveTo()/TeleportTo()` | Animates or instantly moves the device in the world. |

### 🎛 Configuration Options (Details Panel)
| Option | Description |
|--------|-------------|
| Enabled On Game Start | Whether the marker is shown at game start. |
| Icon | Choose from a wide library of icons. |
| Icon Color | Sets how the icon marker appears. |
| Show On Which Map | Show on Minimap, Overview, or Both. |
| Text | Message or name shown at the location (up to 80 chars). |
| Text Color | Set the text color on the map. |
| Assigned Team/Class | Restrict see-ability by team or class. |
| Invert Team/Class | Reverse visibility restrictions. |
| Show Objective Pulse | Whether pulses show to instigator/friendly/other. |
| Icon Scale | Adjust the in-game/map size of the marker. |

> *(Configure all options in the Details panel in UEFN.)*

### 🧹 Events
This device does not expose custom Verse events, but all indicator control is available via Verse functions or direct event binding.

### 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/SpatialMath }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use map_indicator_device
map_indicator_example := class(creative_device):

    @editable
    MapIndicator : map_indicator_device = map_indicator_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    PulseButton : button_device = button_device{}

    @editable
    MoveButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to control buttons
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        PulseButton.InteractedWithEvent.Subscribe(OnPulsePressed)
        MoveButton.InteractedWithEvent.Subscribe(OnMovePressed)

    # Button control handlers
    OnEnablePressed(Agent : agent) : void =
        MapIndicator.Enable()
        Print("Map indicator enabled!")

    OnDisablePressed(Agent : agent) : void =
        MapIndicator.Disable()
        Print("Map indicator disabled!")

    OnPulsePressed(Agent : agent) : void =
        MapIndicator.ActivateObjectivePulse(Agent)
        Print("Objective pulse activated for agent!")

    OnMovePressed(Agent : agent) : void =
        # Example: Move the indicator up by 100 units
        CurrentTransform := MapIndicator.GetTransform()
        NewLocation := CurrentTransform.Translation + vector3{X := 0.0, Y := 0.0, Z := 100.0}
        if (MapIndicator.TeleportTo[NewLocation, CurrentTransform.Rotation]):
            Print("Map indicator moved up!")
```

**Explanation:**
- This example lets you control the indicator using four buttons:
  - Enable/Disable: Shows or hides the marker on the maps for eligible players.
  - Pulse: Starts a pulse (arrow/marker) pointing at the indicator just for the interacting agent.
  - Move: Shifts the indicator’s world position up by 100 units.
- `.ActivateObjectivePulse(Agent)` and `.DeactivateObjectivePulse(Agent)` are used for objective/compass pointing.
- Can be wired to triggers, events, or used for dynamic mission markers.

### 📃 How to Use in UEFN
1. **Place the Device in Your Level**
   - In the Content Browser, add a `map_indicator_device` in your scene.
   - Set its location over the point of interest you want to mark.
2. **Configure Device Options (Details Panel)**
   - Set icon, text, color, which teams/classes see it, whether it’s enabled at start, scaling, show on maps, etc.
   - Customize the indicator as needed for your gameplay.
3. **Create a Verse Device for Dynamic Control**
   - In Verse Explorer, right-click a folder → Create New Verse File (e.g., `map_indicator_example.verse`).
   - Click Create Empty, paste the example code above, and save.
   - Click Verse → Build Verse Code (`Ctrl+Shift+B`) until "Build Succeeded".
4. **Place & Wire Up Your Verse Device**
   - Drag your Verse device into the level.
   - Place any required `button_device`s for control (Enable, Disable, Pulse, Move).
   - In the Details panel for the Verse device, assign:
     - `MapIndicator` → your placed `map_indicator_device`
     - `EnableButton`, `DisableButton`, `PulseButton`, `MoveButton` → your button devices
5. **Test and Iterate**
   - Playtest your map and use the controls to show, hide, move, or pulse the map marker.

### 🧠 Best Practices
- Use separate markers for different objectives or teams—set icon, color, and text accordingly.
- Use pulses for dynamic guidance, e.g., after button press, objective changes, or elimination.
- Combine with Verse logic to script reveal of new locations or missions.

### ❌ Common Issues & Fixes
| Issue | ❌ Mistake | ✅ Correct Practice | Explanation |
|-------|---------------|------------------------|-------------|
| Marker not visible on map | Device disabled or wrong teams/classes | Enable device, set correct visibility options | Must be enabled and visible for audiences |
| Marker doesn't pulse for player | Did not call `.ActivateObjectivePulse()` | Call with agent reference for that player only | Must specify which agent |
| Marker relocates incorrectly | Used wrong transform or movement | Always use `.TeleportTo[]` or `.MoveTo[]` properly | Must provide valid location/rotation |
| `@editable` refs left blank | Did not set Verse device references | Always assign in Details panel after placement | Required for Verse features to work |

**Note:**
- The `map_indicator_device` is ideal for navigation, dynamic objectives, or event-based world markers.
- Can be used for both static and interactive map tokens, with all major visibility, pulse, and location settings run-time controllable via Verse or triggers.

