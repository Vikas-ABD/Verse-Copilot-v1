# UEFN Verse Device Documentation: `stat_powerup_device`

## 🔹 Description
The `stat_powerup_device` is a powerup device used to **increase or decrease a stat** for a player (agent), team, or the whole match. It supports both built-in Fortnite stats (e.g., Score, Eliminations) and custom stats created using the `stat_creator_device`. When a player picks up this powerup, the stat change is immediately applied or begins applying depending on the configuration.

Common use cases include:
- Powerup pickups
- Environmental modifiers
- Hazard penalties
- Bonus/reward triggers

---

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `powerup_device`
- `stat_powerup_device`

---

## 🛠️ Main Functions & Methods
| Name | Description |
|------|-------------|
| `SetMagnitude(float)` | Sets the stat change value (positive = gain, negative = loss) |
| `GetMagnitude()` | Returns the current configured magnitude |
| `Enable()` | Activates the powerup for pickup/application |
| `Disable()` | Deactivates the powerup (cannot be picked up) |
| `Spawn()` | Spawns the powerup in the game world |
| `Despawn()` | Removes the powerup from the world temporarily |
| `Pickup(agent)` | Applies the stat change to a specific agent manually |
| `IsSpawned()` | Checks if the powerup is currently spawned |
| `HasEffect(agent)` | Checks if the effect is currently active on the agent |
| `GetDuration()` | Gets duration of effect post-pickup |
| `SetDuration(float)` | Sets how long the effect should last |
| `GetRemainingTime(agent)` | Returns time left for agent’s effect (-1 = infinite, 0 = not applied) |

---

## 🧹 Events (Data Members)
| Name | Type | Description |
|------|------|-------------|
| `ItemPickedUpEvent` | `listenable(agent)` | Fires when an agent picks up the powerup |

---

## 🎛 Configuration Options (Details Panel)
| Option | Description |
|--------|-------------|
| `Stat To Apply` | Choose which stat to adjust (built-in or custom) |
| `Magnitude` | Value to increase/decrease (positive/negative) |
| `Infinite Effect Duration` | Whether effect lasts forever or not |
| `Effect Duration` | How long the effect should last (in seconds) |
| `Respawn` | Should the powerup respawn after pickup? |
| `Time To Respawn` | Delay before it respawns |
| `Pick Up Options` | Define how pickup works (touch, radial, etc.) |
| `Apply To` | Target: Player, Team, or Match |
| `Persist on Elimination` | Whether the effect persists after elimination |

---

## 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

stat_powerup_example := class(creative_device):

    @editable
    Powerup : stat_powerup_device = stat_powerup_device{}

    @editable
    SpawnButton : button_device = button_device{}
    @editable
    DespawnButton : button_device = button_device{}
    @editable
    IncrementButton : button_device = button_device{}
    @editable
    DecrementButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        Powerup.ItemPickedUpEvent.Subscribe(OnPowerupPickedUp)
        SpawnButton.InteractedWithEvent.Subscribe(OnSpawnPressed)
        DespawnButton.InteractedWithEvent.Subscribe(OnDespawnPressed)
        IncrementButton.InteractedWithEvent.Subscribe(OnIncrementPressed)
        DecrementButton.InteractedWithEvent.Subscribe(OnDecrementPressed)

    OnPowerupPickedUp(Agent : agent) : void =
        Print("Powerup picked up by agent!")

    OnSpawnPressed(Agent : agent) : void =
        Powerup.Spawn()
        Print("Powerup spawned in world.")

    OnDespawnPressed(Agent : agent) : void =
        Powerup.Despawn()
        Print("Powerup despawned.")

    OnIncrementPressed(Agent : agent) : void =
        Powerup.SetMagnitude(5.0)
        Powerup.Pickup(Agent)
        Print("Applied +5 stat via powerup script!")

    OnDecrementPressed(Agent : agent) : void =
        Powerup.SetMagnitude(-3.0)
        Powerup.Pickup(Agent)
        Print("Applied -3 stat via powerup script!")
```

### Key Components:
- One `stat_powerup_device`
- Four `button_device` instances:
  - `SpawnButton`
  - `DespawnButton`
  - `IncrementButton`
  - `DecrementButton`
- Use `.SetMagnitude()` before `.Pickup()` to define stat change
- Subscribe to `ItemPickedUpEvent` for custom behavior logic

---

## ⚖️ How to Use in UEFN

### 1. Place Devices in Your Level
- Add a `stat_powerup_device`
- Add four `button_device` instances (Spawn, Despawn, Increment, Decrement)

### 2. Configure the Powerup
- Set `Stat To Apply`, `Magnitude`, `Duration`, `Respawn`, `Apply To`, etc.

### 3. Create & Add Your Verse Script
- In Verse Explorer: Create new Verse file (e.g., `stat_powerup_example.verse`)
- Paste example script, save, and build (`Ctrl+Shift+B`)
- Place Verse device in world

### 4. Assign References
- In Details Panel, assign Powerup and Button devices to corresponding @editable fields

### 5. Test
- Use buttons in playtest to spawn/despawn/apply powerups
- Observe stat changes and effect durations

---

## 🧠 Best Practices
- Combine with `stat_creator_device` for custom scoring or progression systems
- Use wiring and Verse for powerful hybrid logic
- Positive magnitude = bonus/reward, negative = penalty/hazard
- Leverage `ItemPickedUpEvent` for advanced triggers, UI feedback, etc.

---

## ❌ Common Issues & Fixes
| Issue | ❌ Problem | ✅ Solution | Explanation |
|-------|--------------|----------------|-------------|
| Powerup not in game | Not enabled or spawned | Use `.Enable()` or `.Spawn()` | Must be active to function |
| Stat won’t go negative | Clamped or limited in config | Adjust magnitude/stat config | Stats can be bounded per settings |
| No logic on pickup | No event subscribed | Add `.Subscribe()` call | Required for game logic reactions |

---

## 📅 Notes
- Must configure the exact stat to adjust in the Details panel
- Combine with triggers or volumes for automated gameplay effects
- Compatible with both built-in and custom stats

