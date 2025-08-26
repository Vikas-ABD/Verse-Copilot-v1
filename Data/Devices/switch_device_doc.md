📘 **switch_device – UEFN Verse Device Documentation**

---

🔹 **Description**
The `switch_device` allows agents (players, Verse, or other devices) to turn it on or off, toggling connected devices or triggering custom state transitions. Common uses include doors, lights, traps, logic gates, puzzles, or as an "On/Off" input for any creative system.

🧱 **Verse Using Statement**
```verse
using { /Fortnite.com/Devices }
```

---

🔗 **Inheritance Hierarchy**
- `creative_object`: Base class for creative devices and props.
- `creative_device_base`: Base class for `creative_device`.
- `switch_device`

---

🧩 **Data Members (Events)**
| Name | Type | Description |
|------|------|-------------|
| TurnedOnEvent | listenable(agent) | Fires when turned on; passes the agent who turned it on. |
| TurnedOffEvent | listenable(agent) | Fires when turned off; passes the agent who turned it off. |
| StateChangesEvent | listenable(tuple()) | Fires when state changes (on/off). |
| StateSaveEvent | listenable(tuple()) | Fires when the switch’s persistent state is saved. |
| StateLoadEvent | listenable(agent) | Fires when switch state is loaded. |
| IfOnWhenCheckedEvent | listenable(tuple()) | Fires if "checked" and state is *on*. |
| IfOffWhenCheckedEvent | listenable(tuple()) | Fires if "checked" and state is *off*. |

---

🛠️ **Functions & Methods**
- `Enable()`: Enables this device.
- `Disable()`: Disables this device.
- `TurnOn(Agent:agent)`: Turns on the switch.
- `TurnOff(Agent:agent)`: Turns off the switch.
- `ToggleState(Agent:agent)`: Toggles switch state.
- `GetCurrentState()`: Returns state in global mode.
- `GetCurrentState(Agent:agent)`: Returns state in per-agent mode.
- `IsStatePerAgent()`: Checks if per-agent mode is used.
- `SetState(State:logic)`: Sets global state.
- `SetState(Agent:agent, State:logic)`: Sets per-agent state.
- `SetTurnOnInteractionText(Text:message)`: Sets interaction text for ON.
- `SetTurnOffInteractionText(Text:message)`: Sets interaction text for OFF.
- `SetStateResetTime(Time:float)`: Sets/reset timer (global).
- `SetStateResetTime(Agent:agent, Time:float)`: Sets/reset timer (per-agent).
- `CheckState(Agent:agent)`: Triggers check events.
- `LoadState(Agent:agent)`: Loads saved state.
- `LoadStateForAll()`: Loads state for all agents.
- `SaveState(Agent:agent)`: Saves state.
- `SaveStateForAll()`: Saves state for all agents.
- `ClearPersistenceData(Agent:agent)`: Clears agent state.
- `ClearAllPersistenceData()`: Clears all persistent states.
- `GetStateResetTime()`: Gets reset timer.
- `GetStateResetTime(Agent:agent)`: Gets reset timer (per-agent).
- `GetInteractionTime()`: Gets interaction duration.
- `SetInteractionTime(Time:float)`: Sets interaction duration.

---

🎛 **Configuration Options (Details Panel)**
| Option | Description |
|--------|-------------|
| Switch Start State | On/Off at game start. |
| Interaction Time | Toggle duration for agents. |
| Store State Per Player | Toggle per-agent vs global state. |
| State Reset Time | Auto-reset delay in seconds. |
| Enable/Disable at Game Start | Initial interactivity state. |
| Custom Turn On/Off Interact Text | UI messages for interaction. |

---

🧰 **Usage Example**
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

switch_example := class(creative_device):
    @editable
    Switch : switch_device = switch_device{}

    @editable
    TriggerButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        Switch.TurnedOnEvent.Subscribe(OnSwitchOn)
        Switch.TurnedOffEvent.Subscribe(OnSwitchOff)
        TriggerButton.InteractedWithEvent.Subscribe(OnButtonPressed)

    OnSwitchOn(Agent : agent) : void =
        Print("Switch turned ON by player!")

    OnSwitchOff(Agent : agent) : void =
        Print("Switch turned OFF by player!")

    OnButtonPressed(Agent : agent) : void =
        Switch.TurnOn(Agent)
        Print("Switch toggled ON!")
```

---

🧠 **Best Practices**
- Subscribe to events for custom logic.
- Use per-agent states for multiplayer logic.
- Set interaction and reset times for smooth flow.
- Use `.Enable()`/`.Disable()` for game phases.

---

❌ **Incorrect Usage Examples and Fixes**
| Issue | ❌ Wrong | ✅ Correct | Explanation |
|-------|----------|-------------|-------------|
| Not enabling the switch | Call TurnOn() only | Always call `.Enable()` first | Device must be enabled |
| Not subscribing to events | Expect auto toggling | Use TurnedOnEvent/TurnedOffEvent | Logic must be explicitly handled |
| Wrong agent in per-agent mode | Random/None | Correct agent | Needed for per-agent operation |
| Forgetting reset | No timer set | Set State Reset Time | Avoids stuck state |

---

**Note:**
- Great for logic gates, puzzles, round systems.
- Combine with buttons/triggers for advanced interactions.
- Always review configuration options before publishing.

