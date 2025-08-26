📘 shooting\_range\_target\_device – UEFN Verse Device Documentation

🔹 Description The shooting\_range\_target\_device is a customizable pop-up target that can be hit by agents (players or AI) to trigger various events. It is useful for shooting galleries, aim practice, challenges, and minigames. This device supports pop-up/pop-down states, can be moved (hop up/down), and can signal events for hits, bullseyes, knockdowns, and more. All main functions and events can be accessed and controlled using Verse.

🧱 Verse Using Statement verse using { /Fortnite.com/Devices }

🔗 Inheritance Hierarchy

- creative\_object
- creative\_device\_base
- shooting\_range\_target\_device

🧹 Events (Data Members)

| Name             | Type         | Description                                                  |
| ---------------- | ------------ | ------------------------------------------------------------ |
| BullseyeHitEvent | listenable() | Fires when target is hit in the bullseye area.               |
| HitEvent         | listenable() | Fires when target is hit by any agent.                       |
| KnockdownEvent   | listenable() | Fires when target is knocked down (by damage, not just hit). |
| HopUpEvent       | listenable() | Fires when target moves up slightly (“hop up”).              |
| HopDownEvent     | listenable() | Fires when target moves down slightly (“hop down”).          |
| PopUpEvent       | listenable() | Fires when target pops up (transitions from flat to up).     |
| PopDownEvent     | listenable() | Fires when target pops down (transitions from up to flat).   |

🛠️ Functions & Methods

| Name                  | Description                                                 |
| --------------------- | ----------------------------------------------------------- |
| Enable()              | Enables the device (active in game).                        |
| Disable()             | Disables the device (inactive).                             |
| Reset()               | Resets the target to its initial state.                     |
| PopUp()               | Pops target up (stand upright, can be hit).                 |
| PopDown()             | Pops target down (lay flat, cannot be hit).                 |
| HopUp()               | Moves the standing (up) target upward (harder to hit).      |
| HopDown()             | Moves the standing (up) target downward (harder to hit).    |
| GetTransform()        | Gets the device’s position, rotation, and scale.            |
| MoveTo()/TeleportTo() | Moves or instantly moves the target in the world as needed. |

🎠 Configuration Options (Details Panel)

| Option Name                  | Description                                                           |
| ---------------------------- | --------------------------------------------------------------------- |
| Health                       | How many hits to knock down.                                          |
| Self-Reset                   | Whether the target will automatically reset after being knocked down. |
| Knockdown Score              | Score awarded for knocking down.                                      |
| Bullseye Score               | Score awarded for bullseye hit.                                       |
| Pop Up/Down Speed            | Animation/transition speed.                                           |
| Activation Channels          | Which game/triggers/players can activate via Verse or device logic.   |
| Audio/Visual FX              | Custom SFX, visuals for pop/hit/knockdown, etc.                       |
| (Many more in Details panel) | Explore additional options depending on your game needs.              |

🥈 Events Usage Subscribe in Verse to respond to events such as hits, bullseyes, knockdowns, etc. For example, you can award points, pop targets down/up, or add custom effects when a target is hit.

🛠️ Verse Usage Example

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

shooting_range_target_example := class(creative_device):

    @editable
    Target : shooting_range_target_device = shooting_range_target_device{}

    @editable
    ResetButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to hit and knockdown events
        Target.HitEvent.Subscribe(OnTargetHit)
        Target.KnockdownEvent.Subscribe(OnTargetKnockedDown)
        Target.BullseyeHitEvent.Subscribe(OnBullseyeHit)

        ResetButton.InteractedWithEvent.Subscribe(OnResetPressed)

        # (Optional) Pop up at game start
        Target.PopUp()

    # Event handlers
    OnTargetHit() : void =
        Print("Target was hit!")
        Target.HopUp()

    OnTargetKnockedDown() : void =
        Print("Target knocked down! Popping down target.")
        Target.PopDown()

    OnBullseyeHit() : void =
        Print("Bullseye hit!")

    # Reset handler
    OnResetPressed(Agent : agent) : void =
        Target.Reset()
        Print("Target reset")
```

Explanation:

- Reference your target device and a button for resets.
- Subscribes in Verse to HitEvent, KnockdownEvent, and BullseyeHitEvent.
- Pops up at start, hops up on any hit, pops down on knockdown, and gives a special log/message for bullseye hits.
- Button press triggers a reset.

How to Use in UEFN:

1. Place the Target Device
   - Drag one or more shooting\_range\_target\_device objects into your level.
2. Configure Options
   - Set health, scoring, reset, and FX options in the Details panel.
3. (Optional) Place Control Button(s)
   - Add button(s) for in-game target reset or extra control in your minigame.
4. Create a Verse Device
   - In Verse Explorer: Right click → Create New Verse File (e.g., shooting\_range\_target\_example.verse).
   - Create Empty, paste the code shown above, and save.
   - Click Verse → Build Verse Code (Ctrl+Shift+B) until “Build Succeeded”.
5. Assign All Device References
   - In the Details panel, assign:
     - Target → your shooting\_range\_target\_device
     - ResetButton → (optional) button\_device for manual resets
6. Test Your Experience
   - Play, shoot, and interact with the target to confirm all events work as expected.

🧠 Best Practices

- Combine multiple targets with scoring devices for aim challenges and shooting galleries.
- Use Verse events to create custom effects, advanced logic, or player feedback.
- Set appropriate reset and score options for your game’s difficulty and pacing.

❌ Common Issues & Solutions

| Issue                  | Problem (❌)                | Solution (✅)                                 |
| ---------------------- | -------------------------- | -------------------------------------------- |
| Target doesn’t respond | Device not enabled/active  | Ensure target is enabled via Details/Verse   |
| Events not handled     | Did not subscribe in Verse | Use .Subscribe() for all needed events       |
| Target won’t reset     | Self-reset not enabled     | Use manual reset/button or enable self-reset |

Note:

- All core event-driven gameplay can be handled with simple Verse code using this device’s built-in events and functions.
- For advanced mechanics, combine with timers, scoring devices, and other triggers as needed.

