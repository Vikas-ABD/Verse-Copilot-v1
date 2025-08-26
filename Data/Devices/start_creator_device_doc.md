📘 **stat_creator_device – UEFN Verse Device Documentation**

---

### 🔹 Description
The `stat_creator_device` is a versatile device that creates and manages a custom stat for your island. This stat can be used for win conditions, round advancement, or scoreboard tracking. Stats may be set per player, per team, or globally for the match, and they support level progression. When a stat reaches its max value, it can trigger a level-up and reset or clamp based on settings.

Use cases include:
- XP leveling systems
- Tracked objectives
- Custom progression systems
- Elimination counters

---

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `stat_creator_device`

---

### 🛠️ Key Features & Methods
| Method | Description |
|--------|-------------|
| `SetValue(Agent, Value)` | Sets the stat value for a specific agent (player). |
| `SetValue(Team, Value)` | Sets the stat value for a specific team. |
| `SetValueForMatch(Value)` | Sets the stat value for the entire match. |
| `SetLevel(Agent, Level)` | Sets the level for a specific agent and resets their stat value. |
| `SetLevel(Team, Level)` | Sets the level for a specific team. |
| `SetLevelForMatch(Level)` | Sets the level for the entire match. |
| `GetValue(Agent)` | Gets the current stat value for a player. |
| `GetValue(Team)` | Gets the current stat value for a team. |
| `GetValueForMatch()` | Gets the stat value for the match. |
| `GetLevel(Agent)` | Gets the current level for a player. |
| `GetLevel(Team)` | Gets the current level for a team. |
| `GetLevelForMatch()` | Gets the level for the match. |
| `Enable()/Disable()` | Enables or disables the device at runtime. |
| `GetName()` | Gets the stat’s name as displayed on the UI. |

---

### 🧩 Events (Data Members)
| Name | Type | Fires When... |
|------|------|----------------|
| `ValueChangedEvent` | `listenable(?agent, int)` | Stat value changes for an agent/team/match. |
| `LevelChangedEvent` | `listenable(?agent, int)` | Stat level changes for an agent/team/match. |
| `MaximumReachedEvent` | `listenable(?agent, int)` | Stat reaches/exceeds Max Value or Max Level. |

---

### 🎛 Device Configuration (Details Panel)
- **Stat Name**: Name shown on scoreboard/UI.
- **Scope**: Player, Team, or Match.
- **Max Value**: Value needed for level-up.
- **Max Level**: Number of supported levels.
- **Per Level Points**: Points per level multiplier.
- **Can Lose Level**: If enabled, losing points lowers level.
- **Enabled Phase**: Controls when the device is active.
- **Stat Color/Icon/Bar HUD**: Visual customization.

---

### 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

stat_creator_example := class(creative_device):

    @editable
    StatDevice : stat_creator_device = stat_creator_device{}

    @editable
    IncrementButton : button_device = button_device{}

    @editable
    ResetButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        StatDevice.ValueChangedEvent.Subscribe(OnValueChanged)
        StatDevice.LevelChangedEvent.Subscribe(OnLevelChanged)
        StatDevice.MaximumReachedEvent.Subscribe(OnMaximumReached)

        IncrementButton.InteractedWithEvent.Subscribe(OnIncrementPressed)
        ResetButton.InteractedWithEvent.Subscribe(OnResetPressed)

    OnValueChanged(Agent : ?agent, NewValue : int) : void =
        Print("Stat value changed: {NewValue}")

    OnLevelChanged(Agent : ?agent, NewLevel : int) : void =
        Print("Stat level changed: {NewLevel}")

    OnMaximumReached(Agent : ?agent, Value : int) : void =
        Print("Stat maximum reached at {Value}!")

    OnIncrementPressed(Agent : agent) : void =
        if (CurrentValue := StatDevice.GetValue[Agent]):
            if (StatDevice.SetValue[Agent, CurrentValue + 1]):
                Print("Stat incremented to {CurrentValue + 1}")

    OnResetPressed(Agent : agent) : void =
        if (StatDevice.SetValue[Agent, 0]):
            if (StatDevice.SetLevel[Agent, 0]):
                Print("Stat reset to 0")

    SetStatValue(Agent : agent, Value : int) : void =
        if (StatDevice.SetValue[Agent, Value]):
            Print("Stat value set to {Value}")

    SetStatLevel(Agent : agent, Level : int) : void =
        if (StatDevice.SetLevel[Agent, Level]):
            Print("Stat level set to {Level}")

    GetStatValue(Agent : agent) : int =
        if (Value := StatDevice.GetValue[Agent]):
            Value
        else:
            0

    GetStatLevel(Agent : agent) : int =
        if (Level := StatDevice.GetLevel[Agent]):
            Level
        else:
            0
```

---

### 🧠 Best Practices
- Use `ValueChangedEvent`, `LevelChangedEvent`, and `MaximumReachedEvent` to drive gameplay logic.
- Integrate with UI/Message Devices for visual feedback.
- Use in conjunction with Victory Conditions for round/game control.
- Choose appropriate scope: Player (solo), Team (collab), Match (global objectives).

---

### ❌ Common Issues & Fixes
| Issue | ❌ Problem | ✅ Solution | Explanation |
|-------|------------|-------------|-------------|
| Stat doesn’t change | No `SetValue/SetLevel` used | Call `SetValue`/`SetLevel` | These must be set by Verse or device wiring. |
| Events not working | Didn’t subscribe | Use `.Subscribe()` in `OnBegin` | Event listeners must be actively subscribed. |
| Device references not working | Variables unassigned | Set via `@editable` and Details panel | Verse can't use unlinked devices. |
| Stat not affecting game | Not set in Island Settings | Assign stat in game win conditions | Must be linked in game rules. |

---

### 🔚 Notes
- Stat values auto-wrap/clamp as per Max Value/Level settings.
- Great for XP, level-ups, score tracking, and custom mechanics.
- Combine with triggers, counters, and Verse logic for full control.

---

**End of Documentation**

