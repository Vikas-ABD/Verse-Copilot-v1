## Using `trick_tile_device` in Unreal Editor for Fortnite (UEFN)

### 🔹 Description
The `trick_tile_device` is a trap device in UEFN that removes the building tile it's placed on when triggered. This can be used for creating:
- Falling floor traps
- Sudden obstacles
- Dynamic challenges

It supports multiple activation methods:
- Agent contact (walk-on)
- Direct triggering via Verse
- Event dispatch from other devices

It also supports tile restoration after triggering.

### 🛡️ Key Functions & Events
- **ActivatedEvent**: Fired when the tile is eliminated (after delay).
- **TriggeredEvent**: Fired when triggered by an agent or logic.
- **Enable() / Disable()**: Enable or disable the device.
- **Trigger()**: Immediately eliminates the tile.
- **Reset()**: Restores the tile.
- **EnableAgentContactTrigger() / DisableAgentContactTrigger()**: Toggles walk-on activation.
- **ToggleEnabled() / ToggleAgentContactTrigger()**: Flips current state.
- **TeleportTo() / MoveTo()**: Moves the device.

### 📊 Configuration Overview
- Must be placed on a buildable tile structure.
- Cannot destroy indestructible props.
- Configure activation delay and agent contact in Details panel.
- Combine with buttons, triggers, or channels for control.

### 🛠️ Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 💪 Full Verse Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

trick_tile_device_example := class(creative_device):

    @editable
    TrickTile : trick_tile_device = trick_tile_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    TriggerButton : button_device = button_device{}

    @editable
    ResetButton : button_device = button_device{}

    @editable
    ToggleContactButton : button_device = button_device{}

    var IsContactEnabled : logic = true

    OnBegin<override>()<suspends> : void =
        TrickTile.ActivatedEvent.Subscribe(OnTileActivated)
        TrickTile.TriggeredEvent.Subscribe(OnTileTriggered)
        EnableButton.InteractedWithEvent.Subscribe(OnEnable)
        DisableButton.InteractedWithEvent.Subscribe(OnDisable)
        TriggerButton.InteractedWithEvent.Subscribe(OnTrigger)
        ResetButton.InteractedWithEvent.Subscribe(OnReset)
        ToggleContactButton.InteractedWithEvent.Subscribe(OnToggleContact)

    OnTileActivated(Agent : agent) : void =
        Print("Trick tile activated by agent!")

    OnTileTriggered(Agent : agent) : void =
        Print("Trick tile triggered by agent!")

    OnEnable(Agent : agent) : void =
        TrickTile.Enable()
        Print("Trick tile enabled")

    OnDisable(Agent : agent) : void =
        TrickTile.Disable()
        Print("Trick tile disabled")

    OnTrigger(Agent : agent) : void =
        TrickTile.Trigger()
        Print("Trick tile triggered")

    OnReset(Agent : agent) : void =
        TrickTile.Reset()
        Print("Trick tile reset")

    OnToggleContact(Agent : agent) : void =
        if (IsContactEnabled = true):
            TrickTile.DisableAgentContactTrigger()
            set IsContactEnabled = false
            Print("Trick tile contact trigger disabled")
        else:
            TrickTile.EnableAgentContactTrigger()
            set IsContactEnabled = true
            Print("Trick tile contact trigger enabled")
```

### ⚖️ Setup Instructions

#### 1. Create Verse File & Device
- In UEFN: Top menu → Verse → Verse Explorer
- Right-click folder → Create New Verse File: `trick_tile_device_example`
- Paste above Verse code
- Click "Verse → Build Verse Code (Ctrl+Shift+B)"

#### 2. Place Devices
- Add the `trick_tile_device_example` (Verse device) into your level.
- Place one or more `trick_tile_device` traps on desired tiles.
- Add five `button_device` objects:
  - Enable trap
  - Disable trap
  - Trigger trap
  - Reset tile
  - Toggle agent-contact

#### 3. Assign Device References
- Select the Verse device
- In Details panel:
  - Assign TrickTile → your `trick_tile_device`
  - Assign each button to respective editable field

#### 4. Configure the Trick Tile
- In the `trick_tile_device` Details:
  - Set **Activation Delay** (optional)
  - Enable/disable **Agent Contact Trigger**
  - Assign channels or logic events if needed

#### 5. Launch & Test
- Press Play
- Use buttons or step on tile (if agent contact enabled)
- Watch tile destruction and printed log messages

### 🧠 Tips
- Use `Reset()` for repeatable traps
- Combine with timers, mutators, and zones for advanced mechanics
- `ActivatedEvent` fires after destruction; `TriggeredEvent` fires on detection

### ❌ Troubleshooting
| Issue | Solution |
|-------|----------|
| Trap not activating via step-on | Enable agent contact trigger |
| Reset doesn’t restore tile | Ensure `Reset()` is called after delay |
| Trap not triggered by logic | Ensure device is enabled |

**Note:**
- Only buildings/tiles above the trick tile are destroyed
- Indestructible props are not affected
- Multi-tile traps require multiple trick_tile_device setups

