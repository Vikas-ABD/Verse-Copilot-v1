# guard_spawner_device – UEFN Verse Device Documentation

## 🔹 Description
The `guard_spawner_device` is used to spawn AI guards (NPCs) who can patrol assigned paths and attack other agents (players, other AI). It supports advanced behaviors such as:

- Alerting or hiring guards
- Assigning patrol paths
- Reacting to eliminations
- Live device control

Guards can be configured to be friendly, neutral, or hostile, and set up for specific spawn logic and environment interaction.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `guard_spawner_device`

## 🧩 Data Members (Events)
| Name | Type | Description |
|------|------|-------------|
| `SpawnedEvent` | `listenable(agent)` | Fires when a guard is spawned; sends agent of new guard. |
| `EliminatedEvent` | `listenable(device_ai_interaction_result)` | Fires when a guard is eliminated. Provides source and target. |
| `EliminatingEvent` | `listenable(device_ai_interaction_result)` | Fires when a guard eliminates an agent. |
| `AlertedEvent` | `listenable(device_ai_interaction_result)` | Fires when guard becomes alert. |
| `HiredEvent` | `listenable(device_ai_interaction_result)` | Fires when a player hires a guard. |
| `DismissedEvent` | `listenable(device_ai_interaction_result)` | Fires when a player dismisses a hired guard. |
| `DamagedEvent` | `listenable(device_ai_interaction_result)` | Fires when a guard is damaged. |
| `SuspiciousEvent` | `listenable(agent)` | Guard becomes suspicious. |
| `TargetLostEvent` | `listenable(device_ai_interaction_result)` | Guard loses track of a target. |
| `UnawareEvent` | `listenable(agent)` | Guard no longer aware. |

## 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| `Enable()` | Enables device; guards can spawn. |
| `Disable()` | Disables device; despawns guards if configured. |
| `Spawn()` | Spawns a guard. |
| `Spawn(Instigator: agent)` | Spawns and hires guard to Instigator. |
| `Despawn()` | Despawns all guards. |
| `Despawn(Instigator: agent)` | Despawns all guards; credits eliminator. |
| `Hire(Instigator: agent)` | Hires guards to Instigator's team. |
| `DismissAllHiredGuards()` | Dismisses all hired guards. |
| `DismissAgentHiredGuards(Instigator)` | Dismisses only guards hired by Instigator. |
| `SetGuardsHireable()` | Makes guards hireable. |
| `SetGuardsNotHireable()` | Prevents guard hiring. |
| `ForceAttackTarget(Target, ...)` | Commands all guards to attack Target. |
| `Reset()` | Resets spawn count. |
| `GetSpawnLimit()` | Returns configured spawn limit. |
| `GetTransform()` | Gets device world transform. |
| `MoveTo()` / `TeleportTo()` | Moves or teleports spawner. |

## 🎠 Configuration Options (Details Panel)
- **Spawn Limit**: Max guards spawned at once
- **Auto Spawn When Enabled**: Automatically spawns guards when enabled
- **Despawn Guards When Disabled**: Instantly removes all guards when disabled
- **Patrol Path**: Assigns patrol route (via `ai_patrol_path_device`)
- **Can Be Hired / Auto Hire**: Allow hiring or automatic hiring
- **Spawn as Friendly / Neutral / Hostile**: Sets faction
- **Spawn Effects / Visible**: Visual appearance toggles
- **Group / Team**: Assign for event control

## 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /UnrealEngine.com/Temporary/Diagnostics }
using { /Verse.org/Simulation }

guard_spawner_example := class(creative_device):

  @editable
  GuardSpawner : guard_spawner_device = guard_spawner_device{}

  @editable
  PatrolPath : ai_patrol_path_device = ai_patrol_path_device{}

  @editable
  EnableButton : button_device = button_device{}

  @editable
  DisableButton : button_device = button_device{}

  @editable
  SpawnButton : button_device = button_device{}

  @editable
  DespawnButton : button_device = button_device{}

  OnBegin<override>()<suspends> : void =
    GuardSpawner.SpawnedEvent.Subscribe(OnGuardSpawned)
    GuardSpawner.EliminatedEvent.Subscribe(OnGuardEliminated)
    GuardSpawner.EliminatingEvent.Subscribe(OnGuardEliminating)

    EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
    DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
    SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)
    DespawnButton.InteractedWithEvent.Subscribe(OnDespawnPressed)

  OnGuardSpawned(Guard : agent) : void =
    Print("Guard spawned! You can assign to a patrol path in the Details panel.")

  OnGuardEliminated(Result : device_ai_interaction_result) : void =
    if (Source := Result.Source?, Target := Result.Target?):
      Print("{Source} eliminated a guard {Target}.")
    else:
      Print("A guard was eliminated.")

  OnGuardEliminating(Result : device_ai_interaction_result) : void =
    if (Source := Result.Source?, Target := Result.Target?):
      Print("Guard {Source} eliminated agent {Target}.")
    else:
      Print("A guard eliminated an agent.")

  OnEnablePressed(Agent : agent) : void =
    GuardSpawner.Enable()
    Print("Guard spawner enabled.")

  OnDisablePressed(Agent : agent) : void =
    GuardSpawner.Disable()
    Print("Guard spawner disabled.")

  OnSpawnPressed(Agent : agent) : void =
    GuardSpawner.Spawn()
    Print("Guard manually spawned.")

  OnDespawnPressed(Agent : agent) : void =
    GuardSpawner.Despawn()
    Print("All guards despawned.")
```

## ⚖️ How It Works in UEFN
1. **Place Devices in Level**
   - Add a `guard_spawner_device` and `ai_patrol_path_device`
   - Add `button_device`s for runtime control

2. **Configure in Details Panel**
   - Set spawn limit, hire settings, faction, etc.
   - Assign patrol path or wire custom logic

3. **Create & Build Verse Script**
   - Add `.verse` file (e.g., `guard_spawner_example.verse`) in Verse Explorer
   - Paste example code and build with `CTRL+SHIFT+B`

4. **Place & Reference Your Verse Device**
   - Add `guard_spawner_example` to the level
   - Assign device references in the Details panel

5. **Test Gameplay**
   - Use buttons to spawn/enable/disable/despawn guards
   - Observe patrols, hiring, reactions

## 🧠 Best Practices
- Use `ai_patrol_path_device` for interesting guard behavior
- Subscribe to events to add rewards, alarms, logic
- Call `Spawn()` and `Despawn()` for waves/challenges
- Use faction settings to manage hostility
- Ensure `Can Be Hired` is enabled if using `Hire()`

## ❌ Incorrect Usage Examples and Fixes
| Issue | ❌ Wrong | ✅ Correct | Explanation |
|-------|-------------|---------------|-------------|
| Accessing optional `Source/Target` | `Print(Result.Source)` | `if (Source := Result.Source?): Print(Source)` | Use `:?` to safely unwrap optionals |
| Incorrect event subscription | `Subscribe(OnSpawned)` with wrong param type | `Subscribe(OnGuardSpawned)` with correct param | Events must match parameter types |
| Assigning patrol path in code | `AssignPatrolPath(PatrolPath)` | Assign in Details panel | Assignments handled by UI or wiring |
| Not subscribing to event | Just `EliminatedEvent` | Use `.Subscribe()` | Must explicitly subscribe |
| Missing @editable references | Left blank | Assign in Details panel | Verse code won't function otherwise |

## ⚠️ Notes
- Carefully plan guard setup for dynamic AI and gameplay
- Always check optional values
- Use `Disable()` + "Despawn Guards When Disabled" to reset encounters quickly

