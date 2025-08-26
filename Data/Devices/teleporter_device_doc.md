# Teleporter Device – UEFN Verse Device Documentation

## 🔹 Description
The `teleporter_device` is a customizable portal (rift) used for instantly transporting agents (players, AI) between locations on your island—or even across multiple islands in connected experiences. You can set up one-way, two-way, or group-based teleport networks, control visibility, target behaviors, and trigger teleportation by entering the rift or using Verse/API calls.

## 🧱 Verse Using Statement
```verse
verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `teleporter_device`

## 🛠️ Main Functions & Methods
| Name | Description |
|------|-------------|
| `Enable()` | Turns on the teleporter; it becomes active in-game. |
| `Disable()` | Turns off the teleporter; does not trigger teleportation. |
| `Activate(agent)` | Teleports the specified agent to this device’s configured target group/location. |
| `Teleport(agent)` | Instantly moves the provided agent to this device’s location. |
| `ActivateLinkToTarget()` | Sets up two-way (linked) return teleporting between source/destination teleporters. |
| `DeactivateLinkToTarget()` | Removes link previously established for two-way teleporters. |
| `ResetLinkToTarget()` | Resets/changes the destination teleporter in the target group (random selection allowed). |
| `GetTransform()` | Gets the device’s position/rotation/scale. |
| `MoveTo()` / `TeleportTo()` | Moves/teleports (instantly or smoothly) the teleporter device itself. |

## 🧩 Events (Data Members)
| Name | Type | Description |
|------|------|-------------|
| `EnterEvent` | `listenable(agent)` | Fires when an agent enters the teleporter zone. |
| `TeleportedEvent` | `listenable(agent)` | Fires when an agent emerges at the destination. |

## 🎛 Configuration Options (Details Panel)
- **Teleporter Group**: Assigns teleporter(s) to a named group for targeting.
- **Target Group**: Specifies where this teleporter sends agents.
- **Rift Visible/Invisible**: Visual/Audio effects on or off.
- **Enabled During Phase**: Which game phase(s) the device is active.
- **Team Only**: Limit to certain teams.
- **Affects Class**: Filter by player/class for access.
- **Effect Radius**: Teleports all agents within radius on trigger.
- **Maintain Relative Position**: Agents preserve orientation/momentum.
- **Randomize Target/Linked Return**: Advanced: changes target, sets up linked pairs, etc.
- **Skydive After Teleport**: Player emerges falling from the air at target.

*(Many more options available in the Details Panel for advanced behaviors.)*

## 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

teleporter_example := class(creative_device):

    @editable
    Teleporter : teleporter_device = teleporter_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to teleporter events
        Teleporter.EnterEvent.Subscribe(OnEnter)
        Teleporter.TeleportedEvent.Subscribe(OnTeleported)

        # Subscribe to control buttons
        EnableButton.InteractedWithEvent.Subscribe(OnEnable)
        DisableButton.InteractedWithEvent.Subscribe(OnDisable)

    # Event handlers
    OnEnter(Agent : agent) : void =
        Print("Agent entered teleporter area")

    OnTeleported(Agent : agent) : void =
        Print("Agent has been teleported")

    # Button control handlers
    OnEnable(Agent : agent) : void =
        Teleporter.Enable()
        Print("Teleporter enabled")

    OnDisable(Agent : agent) : void =
        Teleporter.Disable()
        Print("Teleporter disabled")
```

### Explanation:
- **References** one teleporter and two button devices (for enable/disable control).
- **Subscribes** to both `EnterEvent` (when an agent enters the rift) and `TeleportedEvent` (when the teleport completes at the other end).
- **Demonstrates** enabling and disabling with button interaction.

## 📝 How to Use in UEFN
1. **Place Devices**
   - Drag a `teleporter_device` into your world.
   - Drag two `button_devices` for enable/disable controls (optional).
2. **Configure in Details**
   - Set `Teleporter Group`, `Target Group`, visibility, team/class filters, special behaviors, etc.
3. **Create and Assign Verse Device**
   - In *Verse Explorer*, right-click a folder → Create New Verse File (e.g., `teleporter_example.verse`).
   - Click *Create Empty*, paste the code above, and save.
   - Click *Verse → Build Verse Code* (Ctrl+Shift+B) until “Build Succeeded”.
   - In *Content Browser*, drag your new Verse device into the world.
   - Assign `Teleporter`, `EnableButton`, and `DisableButton` references in Details.
4. **Test**
   - Use the buttons to activate/deactivate the teleporter; walk into the teleporter to observe events/log output.

## 🧠 Tips
- Use **Teleporter Group** and **Target Group** settings for easy creation of two-way and networked teleporters.
- Use **Verse functions** for advanced gameplay (e.g., teleport only if goals are met, chain effects, link/unlink dynamically).
- Can be combined with gameplay logic (timers, target elimination, etc.) for puzzle, minigame, or flow-control mechanics.

## ❌ Common Issues & Solutions
| Issue | Possible Reason | Solution |
|-------|------------------|----------|
| Teleporter not working | Disabled or misconfigured | Enable and assign correct target/group |
| Wrong destination | Incorrect target group | Reset/setup target groups and linking |
| No events/log output | Not subscribed in Verse | Subscribe to EnterEvent / TeleportedEvent |

### Note:
- For full control over teleport logic and networked travel, always set up and test both device options and Verse event subscriptions.
- The device works for agents of any kind (players, AI, etc.), as long as they meet any entry restrictions you’ve set.

