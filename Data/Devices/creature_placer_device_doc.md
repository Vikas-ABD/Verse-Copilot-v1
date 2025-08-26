📘 **creature_placer_device – UEFN Verse Device Documentation**

🔹 **Description**
The `creature_placer_device` is used to spawn a single creature (such as a Fiend or other enemy NPC) at a precise location on your Fortnite island. You can configure which creature type to spawn, control spawn/despawn conditions, activation ranges, and react to creature spawn and elimination events. This device is ideal for boss fights, ambushes, minion waves, or unique challenge encounters where precise placement and behavior of a single creature is needed.

🧱 **Verse Using Statement**
```verse
using { /Fortnite.com/Devices }
```

🔗 **Inheritance Hierarchy**
- creative_object
- creative_device_base
- creature_placer_device

🧩 **Data Members (Events)**
| Name             | Type                   | Description                                                              |
|------------------|------------------------|--------------------------------------------------------------------------|
| SpawnedEvent     | listenable(agent)      | Fires when a creature is spawned; sends the spawned creature's agent.   |
| EliminatedEvent  | listenable(?agent)     | Fires when the spawned creature is eliminated; sends the eliminating agent or false if not by an agent. |

🛠️ **Functions & Methods**
| Name                   | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Spawn()                | Spawns the creature at the device’s location.                              |
| Despawn()              | Instantly despawns (removes) the spawned creature.                         |
| TeleportTo(Position, Rotation) | Instantly moves the device (and future spawns) to new position/rotation. |
| MoveTo(Position, Rotation, Time) | Moves device to new position/rotation over given time.               |
| GetTransform()         | Gets world position/rotation/scale of the device.                           |

🎛 **Configuration Options (Details Panel)**
- **Creature Type**: Choose which type (Fiend, etc.) to spawn.
- **Activation Range**: Player proximity required for activation/spawn.
- **Spawn Effects Visibility**: On/Off for showing visual spawn effects.
- **Enable on Game Phase**: Which game phase spawns the creature (Never, Game Countdown, Game Start).
- **Despawn Type**: Conditions for despawning: Distance to Enemy, Distance to Spawner, or None.
- **Despawn Range**: Range for despawn checks (if enabled).
- **Spawn Only If Needed**: Only spawns if previous creature was eliminated (On/Off).
- **Restore Player Shield on Elimination**: Player who eliminates creature receives shield restoration (On/Off).

🧰 **Verse Usage Example**
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

creature_placer_example := class(creative_device):

    @editable
    CreaturePlacer : creature_placer_device = creature_placer_device{}

    @editable
    SpawnButton : button_device = button_device{}

    @editable
    DespawnButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to creature events
        CreaturePlacer.SpawnedEvent.Subscribe(OnCreatureSpawned)
        CreaturePlacer.EliminatedEvent.Subscribe(OnCreatureEliminated)

        # Subscribe to control buttons
        SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)
        DespawnButton.InteractedWithEvent.Subscribe(OnDespawnPressed)

    # Event handlers
    OnCreatureSpawned(Creature : agent) : void =
        Print("Creature spawned at placer location!")

    OnCreatureEliminated(Eliminator : ?agent) : void =
        if(Eliminator?):
            Print("Creature eliminated by a player!")
        else:
            Print("Creature eliminated by non-agent cause.")

    # Button control
    OnSpawnPressed(Agent : agent) : void =
        CreaturePlacer.Spawn()
        Print("Spawn button pressed!")

    OnDespawnPressed(Agent : agent) : void =
        CreaturePlacer.Despawn()
        Print("Despawn button pressed!")
```

📋 **How it works in UEFN:**
1. **Place Devices in Level:**
   - Add a `creature_placer_device` at the exact spot you want your enemy to appear.
   - Place control `button_devices` (optional) if you want players or events to trigger spawn/despawn.
2. **Configure Device in Details Panel:**
   - Choose `Creature Type` (Fiend, etc.).
   - Set activation/despawn conditions, spawn FX, shield restore, etc.
3. **Create and Build the Verse Script:**
   - Create a new Verse file (e.g., `creature_placer_example.verse`), paste in the code above, and save.
   - Build Verse code (Verse → Build Verse Code, or CTRL+SHIFT+B).
4. **Place and Reference Devices:**
   - Add `creature_placer_example` from Content Browser into your world.
   - Assign:
     - `CreaturePlacer` → your placed `creature_placer_device`
     - `SpawnButton`/`DespawnButton` → your placed `button_devices` (optional)
5. **Test and Refine:**
   - Launch a session. Use the buttons to spawn or despawn creatures, and observe log messages related to their spawn and elimination.

🧠 **Best Practices**
- Use `SpawnOnlyIfNeeded = On` to avoid double spawns.
- React to `EliminatedEvent` for rewards, progress, or spawning new waves.
- Use placement and activation range to surprise players or stage big encounter moments.
- Restore Player Shield on elimination for boss fights or reward systems.
- For dynamic placement, use the `.TeleportTo()` / `.MoveTo()` methods.

❌ **Common Mistakes & Fixes**
| Issue                      | ❌ Wrong Usage                                 | ✅ Correct Usage                        | Explanation                                                  |
|---------------------------|-----------------------------------------------|----------------------------------------|--------------------------------------------------------------|
| Creature never respawns   | `SpawnOnlyIfNeeded` enabled, old creature not eliminated | Must eliminate before respawn         | Device won’t spawn another until elimination                 |
| Trying to eliminate creature from code | Use `.Despawn()` for forced removal           | Use `.Despawn()`                      | Kills/removes creature immediately                           |
| Not subscribing to events | No logic triggers on elimination              | Subscribe to `SpawnedEvent`/`EliminatedEvent` | Needed for reward/chain logic                            |

💡 **Note:**
- For advanced waves or periodic spawns, combine with Timer devices or event bindings.
- You can use Verse event handlers as illustrated to grant rewards, track progression, or spawn new enemies on elimination.

