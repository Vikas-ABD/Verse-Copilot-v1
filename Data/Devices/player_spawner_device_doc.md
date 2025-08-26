📘 player_spawner_device – UEFN Verse Device Documentation

🔹 Description
The player_spawner_device is used to spawn agents (players) at defined locations on your Fortnite island. Use one device per intended spawn point—you must place multiple spawners for multiplayer support or to have team/class/priority control over spawn locations. This device can be enabled/disabled, subscribes to spawn events, and supports editor options for flexible spawning scenarios.

🧱 Verse Using Statement
verse
using { /Fortnite.com/Devices }

🔗 Inheritance Hierarchy
* creative_object – Base class for creative devices and props.
* creative_device_base – Base class for creative_device.
* player_spawner_device

🧩 Data Members (Events)
| Name           | Type             | Description                                              |
|----------------|------------------|----------------------------------------------------------|
| SpawnedEvent   | listenable(agent)| Fires when an agent spawns at this device (provides the agent). |

🛠️ Functions & Methods
| Name          | Description                                                          |
|---------------|----------------------------------------------------------------------|
| Enable()      | Enables the spawner so it can be used for spawning agents.          |
| Disable()     | Disables the spawner (no agents will spawn here until enabled again).|
| GetTransform()| Returns device transform (location/rotation/scale in cm).            |
| MoveTo(...)   | Move device over time; interrupts any animation.                     |
| TeleportTo(...)| Instantly move device to new position/rotation or transform.        |

🎛 Configuration Options (Details Panel)
| Option                  | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| Enabled During Phase    | When this spawner is considered active (All, None, Countdown, Gameplay, etc.).|
| Player Team/Class       | Restricts which team/class can use this spawn pad.                          |
| Priority Group          | Determines spawn order vs. other pads; higher is preferred.                 |
| Use as Island Start     | Whether this pad is used for initial island spawn.                          |
| Visible in Game         | Show/hide pad during gameplay.                                              |
| Play Audio              | Sound effect on spawn (always, only if visible, never).                     |
| Enemy Range Check       | Prevent spawn if enemy is nearby, or allow anyway.                          |
| Display Enemy Range     | Visualizes the above during design mode.                                    |
| Respawn Alive Players   | Forces live players to respawn when triggered.                              |

🧰 Example Usage in Verse
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

player_spawner_example := class(creative_device):

    @editable
    PlayerSpawner : player_spawner_device = player_spawner_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        PlayerSpawner.SpawnedEvent.Subscribe(OnPlayerSpawned)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnPlayerSpawned(Agent : agent) : void =
        Print("Player spawned at spawner!")

    OnEnablePressed(Agent : agent) : void =
        PlayerSpawner.Enable()
        Print("Player spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        PlayerSpawner.Disable()
        Print("Player spawner disabled!")
```

🧠 Best Practices
* Name each player_spawner_device clearly in your level for easy assignment in Verse and logic clarity.
* Use Priority and Team/Class filters for advanced modes (e.g., team games, FFA, custom classes).
* Always test spawn eligibility and order when many spawners are used to avoid player stacking or misplacement.
* Subscribe to SpawnedEvent to trigger any gameplay adjustment needed right as players enter the space.

❌ Incorrect Usage Examples and How to Fix
| Issue                             | ❌ Wrong                        | ✅ Correct                               | Explanation                                  |
|----------------------------------|--------------------------------|-----------------------------------------|----------------------------------------------|
| Only one spawner for multiplayer | Only one placed for whole map  | Place one per spawn location/player     | Players need an available spot each          |
| Not enabling device              | Disabled in logic/event—no one spawns | Always call .Enable() or set enabled | Only enabled spawners function               |
| Expecting auto-team/class assignment | No filter set for team/class  | Configure desired restrictions in Details | Prevents spawn order confusion            |
| Not subscribing to SpawnedEvent  | No logic on spawn for effects/rewards | Always wire custom actions as needed | Unlocks full flexibility upon player spawn   |

📌 Note:
* The player_spawner_device only controls where an agent appears; use additional devices to set inventory, class, camera, or triggers for further setup.
* Optimally combine with player_checkpoint_device for progression/save systems.

