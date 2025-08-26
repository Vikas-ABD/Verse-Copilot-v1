### pinball_bumper_device – UEFN Verse Device Documentation

#### 🔹 Description
The `pinball_bumper_device` is a triggered bumper in UEFN that knocks players back, can deal damage, and can award points when activated. It is typically used to implement pinball-style mechanics, bounce pads, or arcade scoring systems in Fortnite experiences. This device can be controlled via Verse scripting or configured directly in the Details panel.

#### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

#### 🔗 Inheritance Hierarchy
- creative_object
- creative_device_base
- pinball_bumper_device

#### 🛠️ Functions & Methods
| Name        | Description                                              |
|-------------|----------------------------------------------------------|
| Enable()    | Enables the bumper to interact with players.             |
| Disable()   | Disables the bumper (prevents interaction).              |
| Activate()  | Manually triggers the bumper's bounce effect.            |

#### 🤩 Events
| Name             | Description                                                |
|------------------|------------------------------------------------------------|
| ActivatedEvent   | Fires when a player activates the bumper (returns agent).  |

#### 🎯 Configuration Options (Details Panel)
- **Activating Team**: Restrict which teams can trigger the bumper.
- **Allow Side Bounce**: Allow bouncing from the side of the bumper.
- **Side Bounce Lift**: Vertical force when bouncing from the side.
- **Allow Top Bounce**: Allow bouncing from the top of the bumper.
- **Bumper Color**: Visual effect color (Blue, Pink Glow, Gold, etc).
- **Object Direction Importance**: Influence of player's velocity on bounce direction.
- **Enabled At Game Start**: Determines if the bumper is active at game start.
- **Affects Creatures**: Whether the bumper can affect NPCs or creatures.
- **Display Score Update on HUD**: Show score gain on player HUD.
- **Reset HUD Message**: Configure score message, color, and display behavior.

*All settings are available in the Details panel in UEFN.*

#### 🪰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

pinball_bumper_example := class(creative_device):

    @editable
    PinballBumper : pinball_bumper_device = pinball_bumper_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnEnablePressed(Agent : agent) : void =
        PinballBumper.Enable()
        Print("Pinball bumper enabled!")

    OnDisablePressed(Agent : agent) : void =
        PinballBumper.Disable()
        Print("Pinball bumper disabled!")
```

**Explanation:**
- Adds a `pinball_bumper_device` and two `button_device` objects.
- Buttons allow enabling or disabling the bumper during gameplay.
- Bumper can also be manually activated via the `Activate()` function.

#### ✅ Step-by-Step Usage in UEFN
1. **Place the Devices**
   - Add a `pinball_bumper_device` in your level.
   - Optionally add `button_device` objects for control.

2. **Configure the Bumper**
   - Adjust bounce direction, team restrictions, colors, and score display in the Details panel.

3. **Create a Verse Script**
   - In Verse Explorer, create a new `.verse` file.
   - Paste the sample code, build it (Ctrl+Shift+B), and ensure build succeeds.

4. **Assign References**
   - In the Verse device's Details panel, set the correct references for the bumper and buttons.

5. **Test in Game**
   - Jump into play mode, test bumper reactions.
   - Use buttons to toggle the bumper's state.

#### 🧠 Best Practices
- Combine with multiple bumpers for arcade/obstacle mechanics.
- Use visual and HUD scoring feedback for enhanced interaction.
- Fine-tune bounce physics via Details panel.
- HUD score messages can be enabled without needing Verse scripting.

#### ❌ Common Issues & Solutions
| Issue                     | Problem                                   | Fix                                            |
|---------------------------|-------------------------------------------|-------------------------------------------------|
| Bumper doesn’t activate  | Device not enabled or wrong team assigned | Enable device and adjust team settings         |
| No knockback or damage    | Bounce/damage not enabled                 | Enable these options in the Details panel      |
| Verse control doesn’t work| Editable reference not set                | Assign all device references in Details panel  |

#### 🔹 Note
The `pinball_bumper_device` is ideal for:
- Minigames
- Arcade zones
- Obstacle courses
- Dynamic gameplay mechanics

Most interactive features (damage, bounce, scoring) are handled through device setup. Control logic (enable/disable/activate) is handled via Verse.

