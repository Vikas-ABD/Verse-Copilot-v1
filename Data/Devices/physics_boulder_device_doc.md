## 📘 physics_boulder_device – UEFN Verse Device Documentation

### 🔹 Description
The `physics_boulder_device` is a device representing a large, indestructible boulder resting on a rocky base. It can be dislodged to roll or fall, subject to physics and gravity, and interact with the environment by dealing configurable damage to agents, vehicles, creatures, and destructible structures it collides with. This device is ideal for hazards, puzzles, or environmental traps in your island.

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- creative_object
- creative_device_base
- prop_spawner_base_device
- physics_object_base_device
- physics_boulder_device

### 🧩 Events (Data Members)
| Name                          | Type                 | Description                                      |
|-------------------------------|----------------------|--------------------------------------------------|
| BalancedBoulderSpawnedEvent  | listenable(tuple())  | Fires when boulder respawns on its base.         |
| BalancedBoulderDestroyedEvent| listenable(tuple())  | Fires when a sitting boulder is destroyed.       |
| BaseDestroyedEvent           | listenable(tuple())  | Fires when the boulder's base is destroyed.      |
| RollingBoulderDestroyedEvent | listenable(tuple())  | Fires when the rolling boulder is destroyed.     |

### 🛠️ Functions & Methods
| Name                    | Description                                                    |
|-------------------------|----------------------------------------------------------------|
| Enable()                | Enables the device for interaction, rolling, respawning, etc.  |
| Disable()               | Disables and optionally destroys spawned boulders.             |
| DestroyAllSpawnedObjects() | Removes all props spawned by this device.                  |
| ReleaseRollingBoulder() | Dislodges the boulder if present (makes it roll).             |
| DestroyBase()           | Destroys only the rocky base of the boulder.                   |
| DestroyRollingBoulder() | Destroys the current moving boulder only.                     |
| SpawnObject()           | Spawns the boulder prop onto the base.                         |
| GetTransform()          | Gets device world transform.                                   |
| MoveTo()/TeleportTo()   | Move/teleport the device in the world.                         |

### 🎛 Configuration Options (Details Panel)
- **Damage to Players**: Max damage dealt to players by the rolling boulder.
- **Damage to Creatures**: Max damage dealt to creatures by the rolling boulder.
- **Damage To Vehicles**: Max damage dealt to vehicles by the rolling boulder.
- **Damage to Environment**: Max damage to environment structures per collision.
- **Timed Respawn**: Respawn balanced boulder after a set time.
- **Boulder Base Req. Respawn**: Requires base to be intact for respawn.
- **Spawn When Enabled**: If the boulder appears automatically when enabled.
- **Destroy When Disabled**: Auto-destroy when device is disabled.
- **Health/Environment/Base/Rolling Boulder Health**: Control destructibility.
- **Leave Base**: Whether the base remains after boulder destruction.

### 🧩 Direct Event Binding
Bind Volume or Trigger events (On Enter, On Exit) to:
- Spawn
- Enable
- Disable
- Release Rolling Boulder
- Destroy base
- Destroy rolling boulder

**Example:** Use trigger "On Exit" to release the boulder, "On Enter" to play VFX/sound.

### 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

physics_boulder_example := class(creative_device):

    @editable
    Boulder : physics_boulder_device = physics_boulder_device{}

    @editable
    EnableButton : button_device = button_device{}
    @editable
    DisableButton : button_device = button_device{}
    @editable
    ReleaseButton : button_device = button_device{}
    @editable
    RespawnButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        Boulder.BalancedBoulderSpawnedEvent.Subscribe(OnBoulderSpawned)
        Boulder.BalancedBoulderDestroyedEvent.Subscribe(OnBalancedDestroyed)
        Boulder.BaseDestroyedEvent.Subscribe(OnBaseDestroyed)
        Boulder.RollingBoulderDestroyedEvent.Subscribe(OnRollingDestroyed)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        ReleaseButton.InteractedWithEvent.Subscribe(OnReleasePressed)
        RespawnButton.InteractedWithEvent.Subscribe(OnRespawnPressed)

    OnBoulderSpawned() : void =
        Print("Boulder respawned on base!")

    OnBalancedDestroyed() : void =
        Print("The balanced boulder was destroyed!")

    OnBaseDestroyed() : void =
        Print("Boulder base destroyed!")

    OnRollingDestroyed() : void =
        Print("Rolling boulder destroyed!")

    OnEnablePressed(Agent : agent) : void =
        Boulder.Enable()
        Print("Boulder device enabled.")

    OnDisablePressed(Agent : agent) : void =
        Boulder.Disable()
        Print("Boulder device disabled.")

    OnReleasePressed(Agent : agent) : void =
        Boulder.ReleaseRollingBoulder()
        Print("Rolling boulder released!")

    OnRespawnPressed(Agent : agent) : void =
        Boulder.SpawnObject()
        Print("Boulder respawned!")
```

### How to Use in UEFN
1. **Place Devices**: Add a `physics_boulder_device` and four `button_devices`.
2. **Configure Options**: Adjust damage, respawn settings, health, etc. in the Details panel.
3. **Create Verse Script**:
   - Create a new `.verse` file (e.g., `physics_boulder_example.verse`).
   - Paste the example code.
   - Build using Ctrl+Shift+B.
4. **Assign Editable References**:
   - Link Boulder and buttons in the Verse device’s Details.
5. **Test**: Interact with buttons to trigger events and observe logging/output.

### 🧠 Best Practices
- Use triggers for dynamic environmental traps.
- Use respawn timers for recurring hazards or one-time puzzles.
- Tweak damage and health to control difficulty.
- Combine with VFX/Audio devices for better feedback.

### ❌ Common Issues & Fixes
| Issue                          | Problem                           | Solution                             |
|-------------------------------|-----------------------------------|--------------------------------------|
| Boulder doesn’t move          | Blocked by geometry/device        | Clear area or reposition device      |
| Players not damaged           | Damage to Players set too low     | Increase damage values in Details    |
| Boulder never comes back      | Timed Respawn not configured      | Enable respawn or call `SpawnObject()` |
| Events not firing in Verse    | Not subscribed to events          | Add `.Subscribe()` in `OnBegin`      |

**Note:** Damage is velocity-based at impact and capped by the max damage settings. Designed for hazards, puzzles, and traps. Use Verse scripting and device wiring for custom logic.

