## vehicle_mod_box_spawner_device – UEFN Verse Device Documentation

### 🔹 Description
The `vehicle_mod_box_spawner_device` is used to spawn customizable vehicle mod boxes. Players can drive into these boxes to apply mods to their vehicles. It supports fine-grained control via Verse, including:
- Spawn timing
- Custom mod selection
- Mod application handling (success/failure)
- Visual and tooltip customization

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `vehicle_mod_box_spawner_device`

### 🔌 Exposed Interfaces
- `enableable` – Can be enabled/disabled through Verse.

### 🧩 Events (Data Members)
| Name | Type | Description |
|------|------|-------------|
| `BoxSpawnedEvent` | listenable(Int) | Fires when a mod box spawns. Returns the mod index (or -1 if not using custom list). |
| `BoxDestroyedEvent` | listenable(tuple<agent?, Int>) | Fires when a box is destroyed. Returns triggering agent and mod index. |
| `ModAppliedEvent` | listenable(tuple<agent?, fort_vehicle, Int>) | Fires when a mod is successfully applied. |
| `ModApplyFailedEvent` | listenable(tuple<agent?, fort_vehicle, Int>) | Fires when a mod fails to apply. |
| `ModApplyOverriddenEvent` | listenable(tuple<agent?, fort_vehicle, Int>) | Triggers if override is set. Used to apply mods manually. |
| `NoModEvent` | listenable(tuple<agent?, fort_vehicle, Int>) | Fires if a "No Mod" entry from the list tries to apply. |

### 🔢 Data Fields
- `ModBoxCustomListSettings` : `?[]vehicle_mod_box_settings` – Array for each custom mod.
- `ModBoxOverallSettings` : `?vehicle_mod_box_settings` – Overall visual style settings.

### 🛠️ Functions & Methods

#### ✅ Basic Device Control
| Function | Description |
|----------|-------------|
| `Enable()` / `Disable()` | Activate or deactivate the device. |
| `IsEnabled()` | Check if the device is enabled. |

#### 🎮 Mod Application Control
| Function | Description |
|----------|-------------|
| `TryApplyModByAgent(Index, Agent)` | Applies mod to the vehicle the agent is driving. |
| `TryApplyModByVehicle(Index, Vehicle)` | Applies mod directly to a vehicle. |
| `SetOverrideModApplyEvent(Bool)` | Enables custom logic for mod application. |

#### 🔁 Box Spawning & Cycling
| Function | Description |
|----------|-------------|
| `SpawnBox()` | Spawns (or respawns) a mod box. |
| `DespawnBox()` | Removes the mod box without firing destroy event. |
| `StartSpawnTimer()` | Starts spawn timer (after despawn). |
| `SpawnModBoxByIndex(Index)` | Spawns specific mod from list. |
| `CycleToNextValidIndex()` / `CycleToPreviousValidIndex()` | Moves to next/previous mod index. |
| `SpawnLastChosenMod()` | Respawns the last used mod box. |

#### ⏱️ Spawn Timers & State
| Function | Description |
|----------|-------------|
| `SetInitialSpawnTimer(Seconds)` | Set time before first box spawn. |
| `SetRespawnTimer(Seconds)` | Set time before box respawns. |
| `GetActiveTimerRemaining()` | Check remaining time on active timer. |
| `GetInitialSpawnTimerLength()` | Get initial spawn timer value. |
| `GetRespawnTimerLength()` | Get respawn timer value. |
| `GetSpawnCount()` | Returns count of spawned mod boxes. |

#### 🎛 Index & Mod List Control
| Function | Description |
|----------|-------------|
| `GetCurrentIndex()` | Get current spawned mod index. |
| `IsValidIndex(Index)` | Check if index is valid. |
| `SetNextModIndex(Index)` | Set next mod index to spawn. |

#### ✏️ Custom UI Text
| Function | Description |
|----------|-------------|
| `SetCustomModBoxName(Name)` | Set custom display name (max 50 chars). |
| `SetCustomPlayerTooltipText(Text)` | Tooltip when players approach box. |
| `ResetModBoxName()` / `ResetPlayerTooltip()` | Reset name/tooltip to default. |

#### 🚚 Transform & Movement
| Function | Description |
|----------|-------------|
| `GetTransform()` | Get device's transform. |
| `MoveTo(Position, Rotation, Duration)` | Smoothly move to new position. |
| `MoveTo(Transform, Duration)` | Move using full transform. |
| `TeleportTo(...)` | Instantly move the device. |

### 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }

vehicle_mod_example := class(creative_device):

    @editable
    ModSpawner : vehicle_mod_box_spawner_device = vehicle_mod_box_spawner_device{}

    OnBegin<override>()<suspends> : void =
        ModSpawner.ModAppliedEvent.Subscribe(OnModApplied)
        ModSpawner.Enable()

    OnModApplied(Data : tuple<agent?, fort_vehicle, Int>) : void =
        let (AgentOpt, Vehicle, ModIndex) = Data
        if (AgentOpt?):
            Print("Mod applied by: {AgentOpt?}")
        Print("Applied mod index: {ModIndex}")
```

### 🔧 How to Use in UEFN
1. **Place the Device**: Add `vehicle_mod_box_spawner_device` to the island.
2. **Configure Mods**: Set “Possible Mods” to “Custom List” and define entries in the Details Panel.
3. **Create & Assign Verse Logic**: Use or adapt the sample Verse class.
4. **Test**: Drive vehicles into mod boxes to test logic.

### 🧠 Best Practices
- Use `ModApplyOverriddenEvent` for full custom mod control.
- Combine with `vehicle_spawner_device` and `button_device` for upgrade systems.
- Use tooltip features to guide players on mod effects.
- Remember: `TryApplyModByAgent()` and `TryApplyModByVehicle()` require device to be enabled and index valid.

### ❌ Common Issues & Solutions
| Issue | Problem ❌ | Solution ✅ |
|-------|-----------|-------------|
| Mod doesn’t apply | Not using Custom List, or index invalid | Enable Custom List, check index with `IsValidIndex()` |
| No event fires | No subscription in Verse | Use `.Subscribe()` for events |
| Mod applies, but logic not triggered | Override not enabled | Use `SetOverrideModApplyEvent(true)` and handle manually |
| Tooltip doesn’t show | Over 50 characters or illegal symbols | Keep text short, avoid `{}`, `<`, `>`, `` ` `` |

### 📎 Tip
This device is powerful when used with mod logic, vehicle types, and event routing for creating custom garages, racing systems, or upgrade paths.

---
Let me know if you'd like a working example using `TryApplyModByAgent()` or integration with a button system.

