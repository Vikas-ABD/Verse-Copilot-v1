# pinball_flipper_device – UEFN Verse Device Documentation

## 🔹 Description
The `pinball_flipper_device` is used to move, damage, and give scores to players that interact with it. By default, it is activated when any player touches its front face: the device rotates (counterclockwise by default), knocks players upward and away, deals optional damage, and can award in-game points. Flippers are ideal for pinball-style gameplay, arcade arenas, or creative movement and scoring mechanics.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `pinball_flipper_device`

## 🧹 Events
| Name            | Type               | Description                                 |
|-----------------|--------------------|---------------------------------------------|
| ActivatedEvent  | listenable(agent)  | Fires when the flipper is activated by an agent (with the agent as parameter). |

## 🛠️ Functions & Methods
| Name             | Description                                                 |
|------------------|-------------------------------------------------------------|
| Enable()         | Enables the flipper (can then be activated by players/devices). |
| Disable()        | Disables the flipper (cannot be triggered while off).        |
| Activate(agent)  | Activates the flipper for a specific agent (triggers knockback, damage, score, etc). |

## 🎮 Configuration Options (Details Panel)
| Option                          | Description                                                                 |
|---------------------------------|-----------------------------------------------------------------------------|
| Activating Team                 | Restricts activation to a specific team or all teams.                       |
| Trigger on Proximity           | On/Off – Activates when touched by a player/agent.                         |
| Trigger on Damage              | On/Off – Activates when the flipper takes damage.                          |
| Bounce Angle Percentage        | Alters how knockback angle is affected by impact direction.                 |
| Damage                         | Sets the amount of damage to players/objects.                              |
| Enabled At Game Start          | On/Off – If On, the flipper is functional at game start.                   |
| Hit on Backswing               | Enables knockback/damage on return swing.                                  |
| Affects Creatures              | On/Off – Whether to affect creatures/NPCs.                                 |
| Display Score Update on HUD   | On/Off – Shows score feedback on screen.                                   |
| Flip Direction                 | Sets rotation direction (e.g., counterclockwise, clockwise).               |
| HUD Message, Color, Score, etc| Customizes on-screen feedback for score/messaging.                         |

## 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use pinball_flipper_device
pinball_flipper_example := class(creative_device):

    @editable
    PinballFlipper : pinball_flipper_device = pinball_flipper_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    ActivateButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        ActivateButton.InteractedWithEvent.Subscribe(OnActivatePressed)

    OnEnablePressed(Agent : agent) : void =
        PinballFlipper.Enable()
        Print("Pinball flipper enabled!")

    OnDisablePressed(Agent : agent) : void =
        PinballFlipper.Disable()
        Print("Pinball flipper disabled!")

    OnActivatePressed(Agent : agent) : void =
        PinballFlipper.Activate(Agent)
        Print("Pinball flipper activated!")
```

### Explanation:
- References one `pinball_flipper_device` and three `button_device`s for enable, disable, and activate.
- Subscribes buttons to control functions.
- Each button toggles the flipper behavior through Verse.
- Device's native proximity activation is set via the Details panel.

## ✨ How to Use in UEFN

### 1. Place the Flipper and (Optional) Control Devices
- Drag `pinball_flipper_device` into your level.
- Optionally, place 3 `button_device`s for control.

### 2. Configure the Flipper in the Details Panel
- Set proximity/damage triggers, team rules.
- Adjust score, damage, visual effects.
- Tweak backswing, bounce, and NPC interactions.

### 3. Create Your Verse File
- In Verse Explorer: Right-click a folder > Create New Verse File.
- Paste the usage example above, then Save.
- Click "Build Verse Code" (Ctrl+Shift+B) until you see "Build Succeeded".

### 4. Place and Assign Your Verse Device
- Drag your Verse device into the level.
- In its Details panel:
  - Assign `PinballFlipper` to your placed flipper.
  - Assign the button devices accordingly.

### 5. Test
- Run a play session.
- Interact with the flipper, try the control buttons.

## 🧠 Best Practices
- Adjust bounce and HUD based on gameplay type (arcade, platformer, etc).
- Use multiple flippers with bumpers for complex pinball layouts.
- Control flipper via Verse for custom challenges or time-based unlocks.

## ❌ Common Issues & Solutions
| Issue                          | Cause                                     | Solution                                      |
|--------------------------------|-------------------------------------------|-----------------------------------------------|
| Flipper not working            | Device not enabled                        | Enable in Details or via `.Enable()` in Verse |
| Doesn't activate when touched | Trigger settings are incorrect            | Set "Trigger on Proximity" to Yes             |
| No effect on some players      | Team/class restrictions active            | Check team/class settings                     |
| No Verse effect                | @editable references not assigned         | Assign all devices in the Verse device panel  |

> Note:
> - Knockback, angle, and scoring are handled by configuration.
> - Score/HUD feedback is automatic if enabled.
> - Advanced control is possible via `ActivatedEvent` logic.

