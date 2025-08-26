📘 **player_reference_device – UEFN Verse Device Documentation**

---

### 🔹 Description
The `player_reference_device` relays an agent’s (player's) statistics to other devices and agents. It can transmit statistics such as elimination count, eliminated count, or score when configured and signal changes to those values in real time. This device can also project a hologram of the referenced agent and display customizable text around the hologram with options for position, color, animation, and style.

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- `creative_object`: Base class for creative devices and props.
- `creative_device_base`: Base class for creative_device.
- `player_reference_device`

### 🧩 Data Members (Events)
| Name | Type | Description |
|------|------|-------------|
| ActivatedEvent | listenable(agent) | Signaled when device is activated, sends referenced agent. |
| AgentReplacedEvent | listenable(agent) | Fires when the tracked agent is replaced. |
| AgentUpdatedEvent | listenable(agent) | Fires when the agent’s data is updated. |
| AgentUpdateFailsEvent | listenable(agent) | Fires if the agent failed to update. |
| TrackedStatChangedEvent | listenable(agent) | Fires when tracked stat is updated. |

### 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| Activate() | Fires ActivatedEvent for referenced agent. |
| Clear() | Clears the current agent from device. |
| Disable() | Disables the device’s functionality and visuals. |
| Enable() | Enables the device and presentation elements. |
| GetAgent() | Returns the currently referenced agent. |
| GetStatValue() | Returns the tracked stat value. |
| IsReferenced() | Checks if the referenced agent is still valid. |
| MoveTo()/TeleportTo() | Moves/teleports the device in the world. |
| Register(agent) | Sets which agent to track. |
| Lock()/Unlock() | Lock/unlock agent or stat updates. |

### 🎛 Configuration Options (Details Panel)
- **Show Hologram**: On/Off – display hologram of the agent.
- **Visible in Game**: On/Off – control visibility.
- **Color**: Direct, Team, or Team Relationship.
- **Custom Color**: Choose highlight color.
- **Show Player Details**: On/Off – show name, stats, etc.
- **Stat to Track**: None, Eliminations, Score, Eliminated.
- **Player Details Height/Curve**: Adjust text around hologram.
- **Hologram Animation**: Style (idle, flex, etc).
- **Hologram Effect Strength**: Control brightness.
- **Update/Activate/Locked Behavior**: Customize update rules.
- **Activated by Sequencers**: Enable sequencer/script activation.

### 🧰 Usage Example in Verse
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

player_reference_example := class(creative_device):

    @editable
    PlayerReference : player_reference_device = player_reference_device{}

    @editable
    ShowHologramButton : button_device = button_device{}

    @editable
    HideHologramButton : button_device = button_device{}

    @editable
    StatTracker : stat_creator_device = stat_creator_device{}

    OnBegin<override>()<suspends> : void =
        ShowHologramButton.InteractedWithEvent.Subscribe(OnShowHologram)
        HideHologramButton.InteractedWithEvent.Subscribe(OnHideHologram)

    OnShowHologram(Agent : agent) : void =
        Print("Hologram shown for agent!")

    OnHideHologram(Agent : agent) : void =
        Print("Hologram hidden for agent!")
```

### 🔍 How it Works
1. Place a `player_reference_device` in your level.
2. Configure options in the Details panel.
3. Reference a player using `.Register(Agent)` or via trigger.
4. Subscribe to events like `TrackedStatChangedEvent`.
5. Control hologram appearance via panel or code.

### 🧠 Best Practices
- Call `.Register(Agent)` at round start or on player interaction.
- Use with `stat_creator_device` for custom stat displays.
- Combine event subscriptions and state checks for real-time stat displays.
- Use Lock/Unlock to control when stats/agents can be changed.

### ❌ Incorrect Usage Examples and Fixes
| Issue | ❌ Wrong | ✅ Correct | Explanation |
|-------|---------|------------|-------------|
| Not calling `.Enable()` | Device disabled | Call `.Enable()` in Verse or set in Details | Device will not work until enabled. |
| Not registering agent | No `.Register()` | Use `.Register(Agent)` properly | Device won’t track or show stats. |
| Forgetting event subscription | Expecting events to fire | Subscribe to events in Verse | Events like `TrackedStatChangedEvent` won’t trigger otherwise. |
| Missing stat config | No stat set to track | Set "Stat to Track" in Details | Only tracks selected stat types. |

### 📌 Notes
- Use with `hud_message_device`, `leaderboard_device`, etc., for UI.
- Multiple devices can be used for teams/duels/stat boards.

