## Sentry Device – UEFN Verse Device Documentation

### 🔍 Description
The `sentry_device` generates an AI bot (sentry) that spawns at a set location and will usually attack players when they come in range. Sentries can be configured to target, defend, patrol, or interact with agents and creatures according to your island’s game logic.

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- **creative_object**: Base class for creative devices and props.
- **creative_device_base**: Base class for creative_device.
- **sentry_device**

### 🧩 Data Members (Events)
| Name                        | Type                  | Description                                                                 |
|-----------------------------|------------------------|-----------------------------------------------------------------------------|
| AlertedEvent               | listenable(agent)     | Triggered when the sentry is alerted to an agent.                          |
| AttackingEvent             | listenable(agent)     | Triggered when the sentry attacks an agent.                                |
| EliminatedEvent            | listenable(?agent)    | Triggered when sentry is eliminated.                                       |
| EliminatingACreatureEvent | listenable(tuple())   | Triggered when the sentry eliminates a creature.                           |
| EliminatingAgentEvent     | listenable(agent)     | Triggered when the sentry eliminates an agent.                             |
| EntersAlertCooldownEvent  | listenable(tuple())   | Triggered when the sentry enters the alert cooldown state.                |
| ExitsAlertEvent           | listenable(tuple())   | Triggered when the sentry exits the alert state.                           |

### 🛠️ Functions & Methods
| Name                    | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| Enable()               | Enables the sentry device.                                                 |
| Disable()              | Disables the sentry device.                                                |
| Spawn()                | Spawns the sentry at its location.                                         |
| DestroySentry()        | Destroys (removes) the current sentry.                                     |
| EnableAlert()          | Puts the sentry into the alert state.                                      |
| Pacify()               | Sets the sentry into pacify state to prevent attacking.                    |
| JoinTeam(Agent)        | Sets the sentry to the same team as the specified agent.                   |
| ResetTeam()            | Resets the sentry to its original team.                                    |
| ResetAlertCooldown()   | Resets the alert cooldown state.                                           |
| Target(Agent)          | Sets the sentry to target the specified agent.                             |
| MoveTo(Position, Rotation, Time) | Moves the sentry to a specified position and rotation over time.     |
| MoveTo(Transform, Time)         | Moves the sentry to the specified transform over a set duration.     |
| TeleportTo(Position, Rotation)  | Instantly teleports the sentry to a position and rotation.            |
| TeleportTo(Transform)          | Instantly teleports the sentry to a transform.                       |
| GetTransform()         | Returns the world transform (location/rotation/scale) of the sentry.        |

### 🧑‍💻 Example Usage in Verse
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

sentry_example := class(creative_device):

    @editable
    Sentry : sentry_device = sentry_device{}

    @editable
    SpawnButton : button_device = button_device{}

    @editable
    DestroyButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        SpawnButton.InteractedWithEvent.Subscribe(OnSpawn)
        DestroyButton.InteractedWithEvent.Subscribe(OnDestroy)
        Sentry.AlertedEvent.Subscribe(OnAlerted)
        Sentry.AttackingEvent.Subscribe(OnAttacking)
        Sentry.EliminatedEvent.Subscribe(OnEliminated)

    OnSpawn(Agent:agent):void =
        Sentry.Spawn()
        Print("Sentry spawned!")

    OnDestroy(Agent:agent):void =
        Sentry.DestroySentry()
        Print("Sentry destroyed!")

    OnAlerted(AlertingAgent:agent):void =
        Print("Sentry was alerted by a player or agent!")

    OnAttacking(TargetAgent:agent):void =
        Print("Sentry is attacking an agent!")

    OnEliminated(MaybeAgent:?agent):void =
        if (Eliminator := MaybeAgent?):
            Print("Sentry eliminated by agent!")
        else:
            Print("Sentry eliminated by environment or non-agent factor.")
```

### 🧠 Best Practices
- Set your sentry’s weapon, team, health, and targeting rules in the Details panel.
- Use events to handle eliminations, attacks, and state transitions for puzzles, arenas, and custom enemy logic.
- For dynamic gameplay, adjust position/team/alert state using Verse or device bindings.

### ❌ Common Mistakes & Solutions
| Problem                            | How to Fix                                                                        |
|------------------------------------|-----------------------------------------------------------------------------------|
| Calls device without reference     | Always set `@editable` field and assign in Details pane.                         |
| Sentry does not attack             | Double-check team, range, and targeting rules in Details/device config.          |
| Unmanaged multiple alerts          | Use Verse subscribed events to sequence or debounce custom reactions if needed.  |

### 📅 Notes
- Use `Pacify()`, `EnableAlert()`, or `Target(Agent)` for advanced sentry behavior controls.
- For zone defense, sequence multiple sentries or combine with trigger/area devices.

