**perception_trigger_device – UEFN Verse Device Documentation**

---

### 🔹 Description
The `perception_trigger_device` is a specialized device used to trigger events based on the line of sight between players (agents) and the device. Inheriting from `trigger_base_device`, it is ideal for gameplay scenarios such as puzzles, stealth mechanics, detection challenges, or objectives where an action is triggered when a player looks at or away from an object.

---

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `trigger_base_device`
- `perception_trigger_device`

---

### 🧹 Events (Data Members)
| Name | Type | Description |
|------|------|-------------|
| `AgentLooksAtDeviceEvent` | `listenable(agent)` | Triggered when an agent gains line of sight to the device. |
| `AgentLooksAwayFromDeviceEvent` | `listenable(agent)` | Triggered when an agent loses line of sight to the device. |
| `DeviceSeesAgentEvent` | `listenable(agent)` | Triggered when the device perceives an agent. |
| `DeviceLosesSightOfAgentEvent` | `listenable(agent)` | Triggered when the device loses perception of an agent. |

---

### 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| `Enable()` / `Disable()` | Enables or disables the device. |
| `GetLookingAtDeviceAgents()` | Returns an array of agents currently looking at the device. |
| `IsLookingAtDevice(agent)` | Checks if a specific agent is looking at the device. |
| `GetPerceivedAgents()` | Returns an array of agents currently seen by the device. |
| `IsPerceived(agent)` | Checks if the device sees the given agent. |
| `SetMaxTriggerCount(int)` | Sets the maximum number of allowed triggers (0 = infinite). |
| `GetTriggerCountRemaining()` | Returns the remaining number of triggers. |
| `SetResetDelay(float)` | Sets delay before retriggering is allowed. |
| `GetResetDelay()` | Returns the current reset delay in seconds. |
| `SetTransmitDelay(float)` | Sets delay before informing other devices after a trigger. |
| `GetTransmitDelay()` | Returns the current transmit delay. |
| `Reset()` | Resets the trigger activation count. |
| `GetTransform()` | Returns the transform of the device. |
| `TeleportTo()` / `MoveTo()` | Moves or teleports the device in the game world. |

---

### 🖛 Configuration Options (Details Panel)
- **Times Can Trigger**: Set how many times it can trigger (0 = infinite).
- **Device Sees A Player (Triggers)**: Configure behavior for seeing agents.
- **Player Looked At / Away (Triggers)**: Configure logic for when agents look at/away.
- **Activating Team / Allowed Class**: Restrict to specific teams/classes.
- **Transmit Every X Triggers**: Fire events only after a certain number of triggers.
- **Delay / Reset Delay**: Delay before and after trigger.
- **Enabled on Game Start**: Initial state.
- **Trigger/VFX/Sound**: Enable/disable visual or sound cues.
- **Visible in Game**: Whether the mesh is visible during gameplay.

---

### 🗃️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

perception_trigger_example := class(creative_device):

    @editable
    PerceptionTrigger : perception_trigger_device = perception_trigger_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        PerceptionTrigger.AgentLooksAtDeviceEvent.Subscribe(OnAgentLooksAt)
        PerceptionTrigger.AgentLooksAwayFromDeviceEvent.Subscribe(OnAgentLooksAway)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnAgentLooksAt(Agent : agent) : void =
        Print("Agent is looking at the device!")

    OnAgentLooksAway(Agent : agent) : void =
        Print("Agent looked away from the device!")

    OnEnablePressed(Agent : agent) : void =
        PerceptionTrigger.Enable()
        Print("Perception trigger enabled!")

    OnDisablePressed(Agent : agent) : void =
        PerceptionTrigger.Disable()
        Print("Perception trigger disabled!")
```

---

### 📅 How to Use in UEFN
1. **Place in Level**
   - Drag `perception_trigger_device` into your map, aligning its front correctly.
2. **Configure Trigger Options**
   - Use Details panel to set trigger behavior, delays, visibility, etc.
3. **Add Control Devices**
   - Optionally use `button_device` for runtime interaction.
4. **Create Your Verse File**
   - Create new Verse script, paste sample code, and build it.
5. **Connect Devices in Details Panel**
   - Assign perception trigger and buttons to your Verse device properties.
6. **Test in Session**
   - Look at device, press buttons, and observe behavior.

---

### 🧠 Best Practices
- Use in stealth missions, puzzles, or visual detection mechanics.
- Align front of device properly to ensure accurate detection.
- Fine-tune with team/class restrictions and delays.
- Combine with reward logic, enemy spawns, or objective completion systems.

---

### ❌ Common Issues & Fixes
| Issue | Mistake | Fix | Explanation |
|-------|---------|-----|-------------|
| Trigger not firing | Wrong orientation or disabled | Align correctly and enable the device | Front is the direction of sight detection |
| Verse code not responding | Events not subscribed | Use `.Subscribe()` on all events | Verse requires explicit event subscription |
| Incorrect trigger count | Misconfigured count/delay | Set proper values in Details | Controls trigger pacing and limit |
| Device not disabling | Unlimited trigger count | Set max/reset/delay options | Enforces trigger limits |

**Note**: Use props or visual cues to help players identify the detection area.

