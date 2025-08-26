📘 grind_powerup_device – UEFN Verse Device Documentation

🔹 Description
The grind_powerup_device is used to grant agents (players) a temporary ability that forces them to slide on any surface. While active, the player emits spark effects and ambient audio to indicate the duration of the powerup. This effect can enhance parkour courses, challenge arenas, or serve as a temporary speed/escape buff or debuff.

🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

🔗 Inheritance Hierarchy
- creative_object
- creative_device_base
- powerup_device
- grind_powerup_device

🧹 Data Members (Events)
| Name               | Type              | Description                                  |
|--------------------|-------------------|----------------------------------------------|
| ItemPickedUpEvent | listenable(agent) | Signals when an agent picks up the powerup.  |

🛠️ Functions & Methods
| Name                | Description                                                                   |
|---------------------|-------------------------------------------------------------------------------|
| Spawn()             | Spawns the powerup in the world for agents to collect.                        |
| Despawn()           | Removes the powerup from the world.                                           |
| Pickup(agent)       | Instantly applies the sliding effect to the given agent.                      |
| GetDuration()       | Returns the configured effect duration (in seconds).                          |
| SetDuration(float)  | Sets the effect duration (in seconds); does not affect agents already buffed.|
| GetRemainingTime(agent) | Gets the remaining time of the effect for that agent.                    |
| HasEffect(agent)    | Returns true if the agent currently has the effect active.                    |
| IsSpawned()         | Returns true if the powerup is currently in the world.                        |
| Enable()/Disable()  | Enables or disables the device.                                               |
| Show()/Hide()       | Shows or hides the powerup in the world.                                      |
| TeleportTo()/MoveTo() | Relocates the device instantly or smoothly.                               |
| GetTransform()      | Retrieves the current location/rotation/scale of the device.                  |

🎛 Configuration Options (Details Panel)
| Option                      | Description                                                              |
|-----------------------------|--------------------------------------------------------------------------|
| Disables Effect On Pickup   | If Yes, cancels effect on pickup (default: No).                          |
| Pickup Radius               | Distance from which a player can pick up the powerup.                    |
| Spawn On Minigame Start     | Determines if the powerup spawns immediately or waits.                  |
| Pick Up Audio               | Enables/disables sound effect on pickup.                                 |
| Selected Team/Class         | Restrict powerup to specific teams or classes.                           |
| Apply To                    | Determines who gets the effect (Player, Team, All).                      |
| Who Can See This Powerup    | Controls device visibility (All, Eligible players, None).               |
| Effect Duration             | Duration in seconds (default 3s; can be Infinite).                       |
| Time To Respawn             | Time delay before the powerup respawns after collection.                 |
| Ambient Audio               | On/Off toggle for persistent audio while effect is active.               |

🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

grind_powerup_example := class(creative_device):

    @editable
    GrindPowerup : grind_powerup_device = grind_powerup_device{}

    @editable
    SpawnButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        GrindPowerup.ItemPickedUpEvent.Subscribe(OnPowerupPickedUp)
        SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)

    OnPowerupPickedUp(Agent : agent) : void =
        Print("Grind powerup picked up by agent!")

    OnSpawnPressed(Agent : agent) : void =
        GrindPowerup.Spawn()
        Print("Grind powerup spawned!")
```

📖 How to Use in UEFN
1. **Create the Verse Device**
   - Open *Verse Explorer*.
   - Right-click a folder, choose *Create New Verse File* (e.g., `grind_powerup_example.verse`).
   - Click *Create Empty*, paste the example code, and save.
   - Build with *Ctrl+Shift+B* until "Build Succeeded" appears.

2. **Add Devices to the Level**
   - Place your `grind_powerup_example` device into the level.
   - Add a `grind_powerup_device` and a `button_device` to your world.

3. **Assign @editable References**
   - Select the Verse device.
   - Assign:
     - `GrindPowerup` → the placed `grind_powerup_device`
     - `SpawnButton` → the placed `button_device`

4. **Configure Powerup in Details Panel**
   - Adjust properties like duration, team/class restrictions, pickup radius, audio, respawn settings.

5. **Test Your Setup**
   - Launch a session, press the spawn button.
   - Pick up the powerup to see the sliding effect and VFX/SFX.

🧠 Best Practices
- Use as a buff, debuff, or movement event trigger.
- Combine `.HasEffect(agent)` and `.GetRemainingTime(agent)` for UI or HUD elements.
- Customize duration to match challenge difficulty.
- Place multiple powerups for varied pickup spots.

❌ Common Issues & Fixes
| Issue                     | ❌ Example Error                           | ✅ Correct Approach                                   | Explanation                              |
|---------------------------|---------------------------------------------|----------------------------------------------------------|------------------------------------------|
| Not spawning on play      | Forgot `.Spawn()` or wrong spawn setting    | Call `.Spawn()` or set to spawn on game start            | Powerup must spawn to be collected        |
| Not subscribing to event  | Misses pickup detection                     | Use `.ItemPickedUpEvent.Subscribe(...)`                  | Needed to run logic when picked up       |
| Action applies forever    | No duration set                             | Use `.SetDuration(x)` and verify respawn time            | Controls effect duration                 |
| Leaving details default   | Unintended access or behaviors              | Configure class/team, pickup radius, and duration        | Avoid overly broad/default behaviors     |

💭 Note:
The grind effect overrides standard movement, forcing players into a sliding state, enhanced by spark VFX and ambient SFX. Perfect for challenge segments, event triggers, or adding a unique movement twist to your Fortnite island.

