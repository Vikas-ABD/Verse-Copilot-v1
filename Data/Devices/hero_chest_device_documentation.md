# Hero Chest Device – UEFN Verse Device Documentation

## 🔹 Description
The `hero_chest_device` is an **indestructible chest** you can place in your UEFN island. It can be **locked or unlocked** (globally or per-agent), and **only opens when unlocked**. It features **hologram/visual effects** based on its "rank" and offers **customizable interaction prompts**. The chest exposes **Verse methods and events** ideal for checkpoint, puzzle, and progression-based gameplay.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `hero_chest_device`

## 🛠️ Key Data Members & Options
| Name | Type/Config | Description |
|------|--------------|-------------|
| `ChestRank` | `?hero_chest_rank` | Determines effect and loot (Ranks: C, B, A, S) |
| `LockedDescription` | `?message` | Text shown when interacting while locked |
| `LockedLabel` | `?message` | Main interaction prompt when locked |
| `LockedSublabel` | `?message` | Additional interaction text when locked |
| `ShowHologram` | `?logic` | Controls hologram (rank FX) visibility |
| `OpenEvent` | `listenable(payload)` | Triggers when chest is opened; gives agent who opened it |

## 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| `Enable()` | Enables interaction with chest |
| `Disable()` | Disables interaction |
| `IsEnabled()` | Returns if chest is enabled |
| `IsLocked(Agent)` | Returns if chest is locked for the agent |
| `IsLockedForAll()` | Returns if chest is globally locked |
| `IsOpen()` | Returns if chest is currently open |
| `Lock(Agent)` | Locks chest for specific agent |
| `Unlock(Agent)` | Unlocks chest for specific agent |
| `LockForAll()` | Locks chest for all agents |
| `UnlockForAll()` | Unlocks chest for all agents |
| `Open()` | Opens chest if unlocked |
| `Reset()` | Closes chest, resets loot/state, restores global lock |
| `GetRankAsString()` | Returns rank as a string ("C", "B", etc.) |
| `GetTransform()` | Returns chest’s transform in world |
| `TeleportTo()` | Teleports chest to new location |
| `MoveTo()` | Animates or moves chest to position |

## 🎮 Device Configuration (Details Panel)
- **Chest Rank:** C, B, A, S (affects FX/loot)
- **Start Locked:** Yes/No (default locked state)
- **Interaction Prompts:** Customizable label/description/sublabel
- **Show Hologram:** Show/Hide holographic FX when closed

## 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

item_spawner_example := class(creative_device):

    @editable
    var ItemSpawner : item_spawner_device = item_spawner_device{}

    @editable
    LockButton : button_device = button_device{}

    @editable
    UnlockButton : button_device = button_device{}

    @editable
    OpenButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        ItemSpawner.ItemPickedUpEvent.Subscribe(OnItemPickedUp)
        LockButton.InteractedWithEvent.Subscribe(OnLockPressed)
        UnlockButton.InteractedWithEvent.Subscribe(OnUnlockPressed)
        OpenButton.InteractedWithEvent.Subscribe(OnOpenPressed)

    OnItemPickedUp(Agent : agent) : void =
        Print("Item picked up by agent!")

    OnLockPressed(Agent : agent) : void =
        ItemSpawner.Disable()
        Print("Item spawner disabled (locked)!")

    OnUnlockPressed(Agent : agent) : void =
        ItemSpawner.Enable()
        Print("Item spawner enabled (unlocked)!")

    OnOpenPressed(Agent : agent) : void =
        ItemSpawner.SpawnItem()
        Print("Item spawned!")
```

## ⚡ How to Use in UEFN
### 1. Place Devices
- Place `hero_chest_device` and three `button_device`s in the world.

### 2. Configure Devices
- Set chest rank, lock state, messages, and hologram options.
- Name buttons as "Lock", "Unlock", and "Open".

### 3. Create Verse Script
- In **Verse Explorer**, create a new Verse file (e.g., `item_spawner_example.verse`).
- Paste the above example, **save**, and **build** (Ctrl+Shift+B).

### 4. Set @editable References
- In Verse device details panel:
  - Set `ItemSpawner` to your `hero_chest_device`
  - Assign the three buttons to their respective fields

### 5. Test in Game
- Interact with buttons to test locking/unlocking/opening.
- Use `Print()` or logic in handlers for debugging and game logic.

## 🧠 Best Practices
- Use `Lock(Agent)` and `Unlock(Agent)` for **per-player interactions**.
- Use `LockForAll()` and `UnlockForAll()` for **global game flow control**.
- Use `OpenEvent.Subscribe` to trigger **rewards, cutscenes, or state progression**.
- Use `Reset()` to make the chest reusable across game rounds.
- Combine `ShowHologram`, interaction messages, and visual FX for immersive gameplay feedback.

## ❌ Common Issues & Fixes
| Issue | Example | Solution | Explanation |
|-------|---------|----------|-------------|
| Chest won’t open | Still locked or disabled | Call `UnlockForAll()` or `Enable()` | Chest must be unlocked & enabled |
| Events don’t trigger | No event handler set | Subscribe to `OpenEvent` | Required for post-open logic |
| Wrong messages | Labels unset | Set via Details or Verse | Prompts are customizable |
| Script doesn’t work | `@editable` fields empty | Set all references in Details panel | Needed for device linking |

## 📅 Use Cases
- One-time reward dispensers
- Player-specific puzzle progression
- Checkpoint unlockables
- Cutscene triggers upon interaction

---
**Note:** The `hero_chest_device` is **indestructible** by design. You must manage its state via **Verse code or gameplay logic** (not destructible mechanics).

