## Capture Area Device – UEFN Verse Device Documentation

### 🔹 Description
The `capture_area_device` creates a zone that triggers custom effects when players enter, exit, or interact with it. It is ideal for:
- Control points
- Capture the Flag
- Domination areas
- Periodic scoring mechanics

Configuration includes capture/contest logic, item requirements, scoring conditions, HUD display, and more.

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `capture_area_device`

### 🧩 Data Members (Events)
| Name | Type | Description |
|------|------|-------------|
| AgentEntersEvent | listenable(agent) | Fires when an agent enters the area. |
| AgentExitsEvent | listenable(agent) | Fires when an agent exits the area. |
| FirstAgentEntersEvent | listenable(agent) | Fires when the first agent enters, if unoccupied. |
| LastAgentExitsEvent | listenable(agent) | Fires when the last agent leaves (area is empty). |
| AreaIsContestedEvent | listenable(agent) | Fires when another team/agent contests the area. |
| AreaIsScoredEvent | listenable(agent) | Fires when a score is awarded for the area. |
| ControlChangeStartsEvent | listenable(agent) | Signals the start of a control change. |
| ControlChangeEvent | listenable(agent) | Signals control of the area has changed. |
| ItemIsConsumedEvent | listenable(agent) | Fires when an item is consumed. |
| ItemIsDeliveredEvent | listenable(agent) | Fires when an item is delivered. |

### 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| Enable() | Activates the device. |
| Disable() | Deactivates the device. |
| ToggleEnabled() | Toggles device state. |
| AllowCapture() | Makes zone capturable. |
| DisallowCapture() | Prevents capture (used for scoring only). |
| ToggleCaptureAllowed() | Toggles capture capability. |
| GiveControl() | Assigns control to a team. |
| Neutralize() | Clears all control. |
| Reset() | Resets capture/scoring/item state. |
| GetAgentsInVolume() | Lists agents in the zone. |
| GetRadius()/GetHeight() | Gets area dimensions. |
| SetRadius()/SetHeight() | Sets area dimensions. |
| IsInArea(agent) | Checks if agent is inside. |
| MoveTo()/TeleportTo() | Moves/teleports area. |

### 🎮 Configuration Options (Details Panel)
- **Starting Team**: Initial owner
- **Accent Color Type**: Zone color mode (Direct/Team/Relationship)
- **Accent Color**: Specific color if using Direct
- **Capture Radius/Height**: Area size
- **Visible During Game**: Collidable/visible setting
- **Item Visible In Game**: Shows item hologram
- **Periodic Scoring**: Enables timed scoring
- **Scoring Time/Amount**: Interval and points to award
- **Enemies Contest Scoring**: Score blocked if enemies present
- **Can Be Captured By Team**: Restricts who can capture
- **Control Time/Neutralize Time**: Time to capture/reset
- **Take Control Faster Per Player**: Team member capture boost
- **Partial Progress Decay Speed**: Rate of progress decay
- **HUD Elements**: On-screen markers
- **Requires Line of Sight**: Marker visibility condition
- **Hostile/Friendly Icon Text**: Custom marker text

### 🪠 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

capture_area_example := class(creative_device):

  @editable
  CaptureArea : capture_area_device = capture_area_device{}
  
  @editable
  EnableButton : button_device = button_device{}

  @editable
  DisableButton : button_device = button_device{}

  @editable
  StartScoreButton : button_device = button_device{}

  @editable
  StopScoreButton : button_device = button_device{}

  OnBegin<override>()<suspends> : void =
    CaptureArea.AgentEntersEvent.Subscribe(OnAgentEnters)
    CaptureArea.ControlChangeEvent.Subscribe(OnControlChange)
    CaptureArea.ItemIsDeliveredEvent.Subscribe(OnItemDelivered)

    EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
    DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
    StartScoreButton.InteractedWithEvent.Subscribe(OnStartScorePressed)
    StopScoreButton.InteractedWithEvent.Subscribe(OnStopScorePressed)

  OnAgentEnters(Agent : agent) : void =
    Print("Agent entered capture area!")

  OnControlChange(Agent : agent) : void =
    Print("Capture area control changed!")

  OnItemDelivered(Agent : agent) : void =
    Print("Item delivered to capture area!")

  OnEnablePressed(Agent : agent) : void =
    CaptureArea.Enable()
    Print("Capture area enabled!")

  OnDisablePressed(Agent : agent) : void =
    CaptureArea.Disable()
    Print("Capture area disabled!")

  OnStartScorePressed(Agent : agent) : void =
    CaptureArea.Enable()
    Print("Capture area scoring enabled!")

  OnStopScorePressed(Agent : agent) : void =
    CaptureArea.Disable()
    Print("Capture area scoring disabled!")
```

### 🪡 How It Works in UEFN
1. **Place Devices**:
   - Drop a `capture_area_device` into the level.
   - Add and wire up `button_device`s if needed.

2. **Configure Details Panel**:
   - Define area size, team ownership, scoring logic, etc.

3. **Build Verse Code**:
   - Create a `.verse` file in Verse Explorer.
   - Paste and build code (CTRL+SHIFT+B).

4. **Reference Devices**:
   - Assign each `@editable` property to real-world devices.

5. **Test & Iterate**:
   - Playtest the game and interact with the zone and buttons.

### 🧠 Best Practices
- Use per-team capture logic for asymmetric objectives.
- Balance scoring and decay rates.
- Use event handlers to trigger actions like doors or visual cues.
- Clear HUD with team-colored icons and labels.
- Use move/teleport for dynamic objectives.

### ❌ Common Issues & Fixes
| Issue | ❌ Wrong | ✅ Correct | Explanation |
|-------|------------|---------------|-------------|
| Event subscription missing | No `.Subscribe()` used | Always call `.Subscribe()` | Needed for interactivity |
| Overlapping zones | Stacked zones | Spread out or isolate logic | Prevents marker confusion |
| Blank @editable refs | Unassigned in Details panel | Assign each device reference | Required for Verse script to work |
| Incorrect item filter | Mismatch item setup | Configure correct item filter | Needed for delivery-based logic |

### ⚠️ Notes
- Use for objective-based games: domination, flag capture, zone control.
- For simple detection: subscribe to `AgentEntersEvent` & `AgentExitsEvent`.
- For complex control: use `ControlChangeEvent`, `AreaIsContestedEvent`, and scoring hooks.

