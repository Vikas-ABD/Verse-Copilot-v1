**Beacon Device – UEFN Verse Device Documentation**

---

### 📙 Description
The `beacon_device` displays visual markers in the world and/or badges (HUD markers) to highlight points of interest, objectives, or navigation aids on your island. It can show different icons, text, and colors by team/class, and is visible only to specified agents or teams. You can enable/disable the device at runtime, move its location, and control agent visibility using Verse logic.

---

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `beacon_device`

---

### 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| `Enable()` | Activates the beacon and shows effects/HUD markers. |
| `Disable()` | Hides the beacon and disables HUD marker. |
| `AddToShowList(agent)` | Makes the beacon visible to a specific agent (player/AI). |
| `RemoveFromShowList(agent)` | Removes agent from explicit show list. |
| `RemoveAllFromShowList()` | Clears manual show list. Visibility governed by team/class. |
| `MoveTo(Position, Rotation, Time)` | Animates beacon to target position and rotation. |
| `TeleportTo(Position, Rotation)` | Instantly moves beacon to new position and rotation. |
| `GetTransform()` | Gets world position, rotation, and scale of the beacon. |

---

### 🎛 Configuration Options (Details Panel)
| Option | Description |
|--------|-------------|
| Beacon To Show | Particle, Badge, or Both |
| Beacon Particle Style | Arrow, Light Beam, Flare |
| Badge UI Style | Default, Backless, etc. |
| Team Visibility | Which teams can see beacon |
| Friendly/Neutral/Hostile Class | Class-based visibility control |
| Beacon Color | Direct Color, Team Color, Relationship Color |
| Icon Identifier | Select HUD icon for marker |
| Custom Beacon/Badge Color | Set custom hex color |
| Friendly/Neutral/Hostile Icon Text | Badge HUD text (30 char max) |
| Hide HUD Icon At | Max HUD visibility distance |
| Display Distance Text | Show distance to beacon on HUD |
| Enabled on Phase | Always, Pre-Game Only, Gameplay Only, None |
| Badge Uses Beacon Color | Sync badge color with beacon color |

> All options must be set in the Details panel in UEFN.

---

### 🧹 Events
* The device does not emit custom Verse events.
* All control must be done through method calls and logic.

---

### 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/SpatialMath }
using { /UnrealEngine.com/Temporary/Diagnostics }

beacon_device_example := class(creative_device):

    @editable
    Beacon : beacon_device = beacon_device{}
    @editable
    EnableButton : button_device = button_device{}
    @editable
    DisableButton : button_device = button_device{}
    @editable
    MoveButton : button_device = button_device{}
    @editable
    TeleportButton : button_device = button_device{}
    @editable
    AddAgentButton : button_device = button_device{}
    @editable
    RemoveAgentButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        MoveButton.InteractedWithEvent.Subscribe(OnMovePressed)
        TeleportButton.InteractedWithEvent.Subscribe(OnTeleportPressed)
        AddAgentButton.InteractedWithEvent.Subscribe(OnAddAgentPressed)
        RemoveAgentButton.InteractedWithEvent.Subscribe(OnRemoveAgentPressed)

    OnEnablePressed(Agent : agent) : void =
        Beacon.Enable()
        Print("Beacon enabled!")

    OnDisablePressed(Agent : agent) : void =
        Beacon.Disable()
        Print("Beacon disabled!")

    OnMovePressed(Agent : agent) : void =
        NewPosition := Beacon.GetTransform().Translation + vector3{X := 500.0, Y := 0.0, Z := 0.0}
        NewRotation := Beacon.GetTransform().Rotation
        spawn{Beacon.MoveTo(NewPosition, NewRotation, 2.0)}
        Print("Beacon moving...")

    OnTeleportPressed(Agent : agent) : void =
        NewPosition := Beacon.GetTransform().Translation + vector3{X := 0.0, Y := 0.0, Z := 500.0}
        NewRotation := Beacon.GetTransform().Rotation
        if (Beacon.TeleportTo[NewPosition, NewRotation]):
            Print("Beacon teleported!")

    OnAddAgentPressed(Agent : agent) : void =
        Beacon.AddToShowList(Agent)
        Print("Beacon now visible to agent!")

    OnRemoveAgentPressed(Agent : agent) : void =
        Beacon.RemoveFromShowList(Agent)
        Print("Beacon no longer visible to agent!")
```

---

### 🪠 How it Works in UEFN
1. **Place Devices in Level**
   - Drag a `beacon_device` and `button_devices` into your world.
2. **Configure the Device (Details Panel)**
   - Set visual styles, visibility, icon, text, and phase settings.
3. **Create & Build Verse Script**
   - Create a Verse file in Verse Explorer.
   - Paste and save the script. Build it using `CTRL+SHIFT+B`.
4. **Place & Reference Devices**
   - Drag Verse device into the world.
   - Assign references to `Beacon` and each button in the Details panel.
5. **Test Gameplay**
   - Launch session, interact with buttons, observe beacon behavior and console logs.

---

### 🧠 Best Practices
- Use multiple beacons for waypoints or navigation.
- Use `.AddToShowList()` for per-player visibility (great for secrets/challenges).
- Use `.MoveTo()` for animation, target tracking, etc.
- Configure styles per team/mode using Details panel.

---

### ❌ Incorrect Usage & Fixes
| Issue | Wrong | Correct | Explanation |
|-------|-------|---------|-------------|
| Beacon not showing | Placed but never called `Enable()` | Call `Beacon.Enable()` | Must enable beacon to display. |
| Event subscription | `Beacon.Event.Subscribe(...)` | N/A | No custom events for this device. |
| Missing agent | `Beacon.AddToShowList()` | `Beacon.AddToShowList(Agent)` | Always provide an agent reference. |
| Missing references | Editable fields left blank | Assign all in Details panel | Device logic fails without assignments. |
| Wrong access control | `Beacon.SetTeam(...)` | Use Details panel | Team/class control must be set via options. |

---

### ℹ️ Notes
- Team/Class filters and badge/particle selections **must be** set in the Details panel.
- Cannot change team/class visibility via Verse.
- Combine with other devices and Verse logic for advanced gameplay mechanics.

