📘 creature_spawner_device – UEFN Verse Device Documentation

🔹 Description
The creature_spawner_device spawns waves of one or more creatures (such as Fiends, Brutes, or other enemy NPCs) at selected intervals, supporting a variety of behaviors for wave-based minigames, horde mode/rounds, and boss fights. You can customize creature type, active creature limit, spawn interval, visual FX, spawn/despawn conditions, and integrate with other Verse logic via events for advanced gameplay.

🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

🔗 Inheritance Hierarchy
- creative_object
- creative_device_base
- creature_spawner_device

🧩 Data Members (Events)
| Name             | Type                               | Description                                                       |
|------------------|------------------------------------|-------------------------------------------------------------------|
| SpawnedEvent     | listenable(agent)                  | Fires when a creature is spawned; sends the spawned creature’s agent. |
| EliminatedEvent  | listenable(device_ai_interaction_result) | Fires when a creature is eliminated; includes eliminating agent and target. |

🛠️ Functions & Methods
| Name                   | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Enable()               | Enables the spawner to begin spawning as per its setup.                      |
| Disable()              | Disables the spawner; stops all spawning and may eliminate existing creatures. |
| EliminateCreatures()   | Eliminates all creatures currently spawned by this device.                   |
| DestroySpawner()       | Destroys the device. Useful after all waves complete or as a round-ender.    |
| GetSpawnLimit()        | Returns the max number of total spawns allowed if spawn limit is enabled.   |
| GetTransform()         | Gets world position/rotation/scale of the device.                            |
| MoveTo(...) / TeleportTo(...) | Move/teleport spawner to a new location/rotation.                          |

🎛 Configuration Options (Details Panel)
- **Spawner Type**: Cube Spawner, Ice Spawner
- **Creature Type**: Cube Random, Ice Random, Rush Random, All Random, or specific creature
- **Number of Creatures**: Maximum number of active creatures at once
- **Limit Spawned Creatures**: Enables lifetime spawn cap
- **Total Spawn Limit**: Maximum number of creatures across device's lifetime
- **Wave Timer**: Minimum interval between spawning waves
- **Activation Range**: Player proximity required to trigger spawning
- **Despawn Range**: Distance from spawner/player before creature despawns
- **Despawn Type**: Distance To Enemy, Distance To Spawner, or Do Not Despawn
- **Invincible Spawner**: Toggle player damage to spawner
- **Spawner Visibility**: Spawner visibility to players
- **Spawn Effects Visibility**: Toggle visual spawn effects
- **Damage Spawner After Spawn**: Spawner takes damage after each spawn
- **Max Spawn Distance / Through Walls**: Spawn location rules and LOS control
- **Preferred Spawn Location**: Spawn behavior (e.g. At Max Distance)
- **Enabled At Game Start**: Auto-start spawning at game start
- **Restore Player Shield on Elimination**: Player gains shield when creature is eliminated

🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

creature_spawner_example := class(creative_device):

    @editable
    CreatureSpawner : creature_spawner_device = creature_spawner_device{}

    @editable
    StartButton : button_device = button_device{}

    @editable
    StopButton : button_device = button_device{}

    var CurrentWave : int = 0
    var CreaturesRemaining : int = 0

    OnBegin<override>()<suspends> : void =
        CreatureSpawner.SpawnedEvent.Subscribe(OnCreatureSpawned)
        CreatureSpawner.EliminatedEvent.Subscribe(OnCreatureEliminated)

        StartButton.InteractedWithEvent.Subscribe(OnStartPressed)
        StopButton.InteractedWithEvent.Subscribe(OnStopPressed)

    OnCreatureSpawned(Creature : agent) : void =
        set CreaturesRemaining += 1
        Print("Creature spawned! Total: {CreaturesRemaining}")

    OnCreatureEliminated(Result : device_ai_interaction_result) : void =
        set CreaturesRemaining -= 1
        Print("Creature eliminated! Remaining: {CreaturesRemaining}")
        if (CreaturesRemaining <= 0):
            Print("Wave {CurrentWave} complete!")
            spawn{StartNextWave()}

    OnStartPressed(Agent : agent) : void =
        spawn{StartNextWave()}

    OnStopPressed(Agent : agent) : void =
        CreatureSpawner.Disable()
        set CreaturesRemaining = 0
        Print("Spawner disabled!")

    StartNextWave()<suspends> : void =
        set CurrentWave += 1
        Print("Starting wave {CurrentWave}")
        CreatureSpawner.Enable()
```

🧪 How It Works in UEFN
1. **Place Devices in Level**
   - Add `creature_spawner_device` for each wave/spawn zone
   - Add `button_device` for start/stop logic if needed

2. **Configure Devices in Details Panel**
   - Set types, counts, limits, timers, visibility, etc.
   - Use `Enabled At Game Start` as needed

3. **Implement and Build Verse Script**
   - Create a file like `creature_spawner_example.verse`, paste code, save
   - Build script: `Verse → Build Verse Code` (CTRL+SHIFT+B)

4. **Place and Reference Devices in World**
   - Add the Verse device to your map
   - Link CreatureSpawner and ButtonDevices in the Details panel

5. **Test in a Session**
   - Launch and use Start/Stop buttons
   - Check logs for wave state and creature tracking

🧠 Best Practices
- Use Wave Timer + Total Spawn Limit for controlled horde rounds
- Use `.Disable()` and `.EliminateCreatures()` to reset rounds
- Track events to scale difficulty or score
- Use invincible spawners for boss fights, hidden ones for ambushes

❌ Common Mistakes & Fixes
| Issue                    | ❌ Wrong Usage                           | ✅ Correct Usage                                      | Explanation                                     |
|--------------------------|------------------------------------------|------------------------------------------------------|-------------------------------------------------|
| Spawns never occur       | Device not enabled or range too high     | Enable device, check range                          | Match settings to trigger conditions            |
| Spawned creatures remain | No despawn logic or device stays enabled | Use Despawn Type and/or call EliminateCreatures     | Clean up after waves                            |
| Device destroyed early   | Damage Spawner on / low HP               | Make spawner invincible or tune post-spawn damage   | Avoid player interference                       |
| Overlapping events       | Multiple scripts control one spawner     | Centralize control logic                            | Prevent redundant or conflicting behavior       |

📌 Notes:
- Adjust creature count and wave timing for difficulty curves
- Enable "Restore Player Shield on Elimination" to reward survival
- Use multiple spawners + Verse triggers for complex encounters

