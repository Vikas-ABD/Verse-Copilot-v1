## item_spawner_device – UEFN Verse Device Documentation

### 🔊 Description
The `item_spawner_device` is a flexible tool in UEFN used to configure and spawn items that agents (players) can pick up and use in a Fortnite experience. It supports multiple registered items, manual and automatic spawning, and integrates with Verse for advanced gameplay scripting. Key features include respawn delays, item scaling, movement control, pickup logic, and more.

### 🔃 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `base_item_spawner_device`
- `item_spawner_device`

### 🥉 Data Members (Events)
| Name | Type | Description |
|------|------|-------------|
| `ItemGrantedEvent` | `listenable(agent)` | Triggered when an item is granted to an agent |

### 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| `SpawnItem()` | Spawns the currently configured item |
| `CycleToNextItem()` | Rotates to the next registered item |
| `Enable()` / `Disable()` | Enables or disables the spawner device |
| `SetEnableRespawnTimer(bool)` | Toggle respawn on timer feature |
| `SetTimeBetweenSpawns(float)` | Sets delay between spawns in seconds |
| `GetTimeBetweenSpawns()` | Returns current respawn delay |
| `GetEnableRespawnTimer()` | Checks if auto-respawn is enabled |
| `GetTransform()` | Retrieves current transform of the device |
| `MoveTo()` / `TeleportTo()` | Moves or teleports the device |

### 🎛 Configuration Options (Details Panel)
| Option | Description |
|--------|-------------|
| Enabled at Game Start | Activates device at start if true, else requires `.Enable()` call |
| Items Respawn | Determines if items return or are single-use |
| Random Spawns | Options include Off, Random, or No Repeats |
| Spawn Item On Timer | Auto-spawn items based on timer delay |
| Respawn Item On Timer | Delay before item respawn post-collection |
| Time Before First Spawn | Delay before initial item spawn |
| Initial Movement of Item | Options: None, Gravity, Toss |
| Run Over Pickup | If enabled, pickup happens on contact |
| Drop Item Position/Scale | Sets position and scale of spawned item |
| Resource Cost | Resource requirement for item spawn |
| Initial/Spare Weapon Ammo | Sets initial ammo values for weapon items |
| Visible in Game | Toggles visibility of spawner device |

*Note: Items must be registered by dragging and dropping them onto the spawner in the editor prior to gameplay.*

### 🎮 Events
| Event | Description |
|-------|-------------|
| `ItemPickedUpEvent` | Triggered when a spawned item is picked up by an agent |

### 🧠 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

item_spawner_example := class(creative_device):

    @editable
    ItemSpawner : item_spawner_device = item_spawner_device{}

    @editable
    SpawnButton : button_device = button_device{}

    @editable
    CycleButton : button_device = button_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        ItemSpawner.ItemPickedUpEvent.Subscribe(OnItemPickedUp)
        SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)
        CycleButton.InteractedWithEvent.Subscribe(OnCyclePressed)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnItemPickedUp(Agent : agent) : void =
        Print("Item picked up by agent!")

    OnSpawnPressed(Agent : agent) : void =
        ItemSpawner.SpawnItem()
        Print("Item spawned!")

    OnCyclePressed(Agent : agent) : void =
        ItemSpawner.CycleToNextItem()
        Print("Cycled to next item!")

    OnEnablePressed(Agent : agent) : void =
        ItemSpawner.Enable()
        Print("Item spawner enabled!")

    OnDisablePressed(Agent : agent) : void =
        ItemSpawner.Disable()
        Print("Item spawner disabled!")
```

### ✅ How to Use in UEFN
1. **Add Items to the Device**
   - Place an `item_spawner_device` in your world
   - Drag desired inventory items onto the device to register them

2. **Create Your Verse Device**
   - In Verse Explorer, right-click a folder → Create New Verse File
   - Paste the example code and build until "Build Succeeded"

3. **Place Devices in the World**
   - Place the Verse device, item_spawner_device, and four button_devices (for Spawn, Cycle, Enable, Disable)

4. **Assign @editable References**
   - Use the Details panel to link the placed devices to the Verse script

5. **Configure Device Options**
   - Set respawn, movement, pickup, and visibility options in the Details panel

6. **Test In-Game**
   - Interact with buttons to control item spawning and monitor pickup events

### 🧠 Best Practices
- Always drop items onto the spawner before gameplay; runtime registration is not possible
- Use `.Enable()` and `.Disable()` for interactive and puzzle elements
- Leverage `ItemPickedUpEvent` to trigger custom logic like rewards or level progression
- Tune respawn and randomization settings to match gameplay goals

### ❌ Common Issues & Fixes
| Issue | Wrong Approach | Correct Approach | Explanation |
|-------|----------------|------------------|-------------|
| Items don't spawn | Forgot to register items | Drop items onto device in editor | Items must be registered manually |
| Blank @editable fields | References not assigned | Set all references in Details panel | Verse requires proper field linking |
| No respawn | Timer not configured | Enable respawn in Details panel | Respawn logic depends on configuration |
| Wrong item cycles | Omitted `.CycleToNextItem()` | Use cycle function as needed | Needed for multi-item setups |
| Can't pick up | Improper pickup settings | Adjust pickup and team settings | Settings must allow pickup |

### 🎡 Use Cases
- Loot drops
- Puzzle key spawning
- Periodic or timed item deliveries
- Event-driven progression systems

Combine with button devices and custom Verse scripts to achieve interactive, rich experiences in Fortnite.

