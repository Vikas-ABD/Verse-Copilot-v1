## player_counter_device – UEFN Verse Device Documentation

### 🔹 Description
The `player_counter_device` tracks the number of players within a defined area and reacts dynamically in-game. It is ideal for scenarios where gameplay logic depends on player presence, such as group doors, co-op puzzles, win/loss conditions, or team-based events.

The device optionally displays a visual info panel that shows current and required player counts and emits events when those counts change or match the configured target.

---

### 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
| Class | Description |
|-------|-------------|
| `creative_object` | Base class for all props and devices. |
| `creative_device_base` | Adds base functionality for devices. |
| `player_counter_device` | Tracks players in a zone and emits count-based events. |

---

### ⟲ Listenable Events
| Event Name | Payload Type | Description |
|------------|---------------|-------------|
| `CountedEvent` | `agent` | Fired when a valid player enters the area and is counted. |
| `RemovedEvent` | `agent` | Fired when a counted player leaves the zone, the game, or no longer meets filter criteria. |
| `CountSucceedsEvent` | `none` | Fired when the player count matches the target. |
| `CountFailsEvent` | `none` | Fired when the count doesn't match the target. |

---

### 🧰 Core Methods
| Method | Description |
|--------|-------------|
| `Enable()` | Activates the counter. |
| `Disable()` | Deactivates the counter; no events triggered. |
| `GetCount()` | Returns the number of players currently counted. |
| `GetCountedAgents()` | Returns all currently counted agents. |
| `CompareToTarget()` | Manually triggers count comparison. |
| `IsPassingTest()` | Returns true if current count matches target. |
| `IsCounted(Player: agent)` | Checks if a specific player is counted. |
| `SetTargetCount(Value: int)` | Sets a new target and re-checks count. |
| `GetTargetCount()` | Returns the current target count. |
| `IncrementTargetCount()` | Increases target count by 1. |
| `DecrementTargetCount()` | Decreases target count by 1. |
| `Reset()` | Resets target count to default. |
| `Register(Player: agent)` | Manually counts a player. |
| `Unregister(Player: agent)` | Removes a player from the count. |
| `UnregisterAll()` | Clears all counted players. |
| `TransmitForAllCounted()` | Fires `CountedEvent` for all counted agents. |
| `ShowInfoPanel()` | Displays visual count panel. |
| `HideInfoPanel()` | Hides the info panel. |
| `IsShowingInfoPanel()` | Returns true if the info panel is visible. |
| `GetTransform()` | Gets the device's transform. |
| `MoveTo(...)` / `TeleportTo(...)` | Moves or teleports the device. |

---

### ⚙️ Configuration Options
| Option | Description |
|--------|-------------|
| `Target Player Count` | Number of players required for success. |
| `Track Registered Players` | Count players by registration or live presence. |
| `Count Display Enabled` | Shows count in-world with info panel. |
| `Check Frequency` | How often count is checked. |
| `Class / Team Restrictions` | Filters counted players. |

---

### ✅ Common Usage: Step-by-Step
```verse
using { /Fortnite.com/Devices }

team_gate_controller := class(
    @editable PlayerCounter: player_counter_device
):

    OnBegin<override>()<suspends>: void =
        PlayerCounter.Enable()
        PlayerCounter.CountSucceedsEvent.Subscribe(OnAllPlayersPresent)
        PlayerCounter.CountFailsEvent.Subscribe(OnNotEnoughPlayers)

    OnAllPlayersPresent(): void =
        Print("All players present! Opening gate...")

    OnNotEnoughPlayers(): void =
        Print("Waiting for more players...")
```

### 🛠️ Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

player_counter_example := class(creative_device):

    @editable
    PlayerCounter : player_counter_device = player_counter_device{}
    @editable
    DoorDevice : creative_device = creative_device{}

    OnBegin<override>()<suspends> : void =
        PlayerCounter.CountSucceedsEvent.Subscribe(OnTargetCountReached)
        PlayerCounter.CountFailsEvent.Subscribe(OnTargetCountFailed)
        PlayerCounter.CountedEvent.Subscribe(OnPlayerCounted)

    OnTargetCountReached() : void =
        Print("Target number of players reached!")
        DoorDevice.Enable()

    OnTargetCountFailed() : void =
        Print("Not enough players present!")
        DoorDevice.Disable()

    OnPlayerCounted(Agent : agent) : void =
        Print("Player entered area and was counted!")
```

---

### 🧠 Best Practices
* Use `CountSucceedsEvent` and `CountFailsEvent` for gates/checkpoints.
* Show info panel with `ShowInfoPanel()` for visual feedback.
* Use `IncrementTargetCount()` / `DecrementTargetCount()` for dynamic logic.
* Pair with:
  * `barrier_device` to open/close areas
  * `hud_message_device` to show prompts
  * `trigger_device` for zone activation

---

### ❌ Incorrect Usage Examples
| Issue | ❌ Wrong | ✅ Fix | Explanation |
|-------|------------|-----------|-------------|
| No `@editable` | Not assigning device | Use `@editable` for access in Details panel | Prevents nil/error calls |
| No Compare Mode | Left as "Do Not Compare" | Set correct logic (e.g., Equal To) | Events won’t trigger otherwise |
| No Subscriptions | Missing `Subscribe()` | Subscribe to events in Verse | Required to react to player changes |
| Method calls without `Enable()` | Using `GetCount()` immediately | Call `Enable()` first | Device must be active |
| Misused `CountedEvent` | Expecting a count | Use `GetCount()` for total | `CountedEvent` only gives agent |
| Expecting auto-target update | Not using setters | Use `SetTargetCount()` or increment/decrement methods | Target count is manual |

---

### 👍 Ideal Use Cases
* Puzzle rooms requiring team cooperation
* Group-activated doors or switches
* Multiplayer escape or boss events
* Dynamic logic gates for teams or co-op challenges
* Checkpoints or respawn areas based on population

