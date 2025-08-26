# player\_counter\_device – UEFN Verse Device Documentation

## 🔹 Description

The `player_counter_device` is used to track the number of players within a defined area and react dynamically in-game based on that count. It is ideal for gameplay scenarios where logic depends on player presence, such as:

- Group doors
- Team-based puzzles
- Co-op events
- Win/loss conditions

The device can optionally display a visible info panel showing current and required player counts, and it emits events when the count changes or matches the configured target.

## 🧱 Imports Required

```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy

| Class                   | Description                                           |
| ----------------------- | ----------------------------------------------------- |
| `creative_object`       | Base class for all props and devices                  |
| `creative_device_base`  | Adds base functionality for devices                   |
| `player_counter_device` | Tracks players in a zone and emits count-based events |

## ⟳ Listenable Events

| Event Name           | Payload Type | Description                                                                                |
| -------------------- | ------------ | ------------------------------------------------------------------------------------------ |
| `CountedEvent`       | agent        | Fired when a valid player enters the area and is counted                                   |
| `RemovedEvent`       | agent        | Fired when a counted player leaves the zone or game, or no longer meets team/class filters |
| `CountSucceedsEvent` | none         | Fired when player count matches the target count                                           |
| `CountFailsEvent`    | none         | Fired when player count does not match the target count                                    |

## 🧠 Core Methods

| Method Signature                   | Description                                       |
| ---------------------------------- | ------------------------------------------------- |
| `Enable(): void`                   | Activates the counter device                      |
| `Disable(): void`                  | Deactivates the counter (no events are triggered) |
| `GetCount(): int`                  | Returns number of players currently counted       |
| `GetCountedAgents(): []agent`      | Returns all agents currently counted              |
| `CompareToTarget(): void`          | Manually compares current count with target count |
| `IsPassingTest(): logic`           | Returns true if current count matches target      |
| `IsCounted(Player: agent): logic`  | Returns true if specified player is counted       |
| `SetTargetCount(Value: int): void` | Sets a new target player count and compares again |
| `GetTargetCount(): int`            | Returns current target player count               |
| `IncrementTargetCount(): void`     | Increases target count by 1 and re-evaluates      |
| `DecrementTargetCount(): void`     | Decreases target count by 1 and re-evaluates      |
| `Reset(): void`                    | Resets the target player count to default         |
| `Register(Player: agent): void`    | Manually registers a player                       |
| `Unregister(Player: agent): void`  | Removes a player from the counted list            |
| `UnregisterAll(): void`            | Clears all registered players                     |
| `TransmitForAllCounted(): void`    | Triggers `CountedEvent` for all counted players   |
| `ShowInfoPanel(): void`            | Shows the visual info panel in the world          |
| `HideInfoPanel(): void`            | Hides the visual display                          |
| `IsShowingInfoPanel(): logic`      | Returns whether the panel is shown                |
| `GetTransform(): transform`        | Gets the device transform                         |
| `MoveTo(...) / TeleportTo(...)`    | Moves or teleports the device                     |

## ⚙️ Configuration Options (Details Panel)

- **Target Player Count**: Number of players required to trigger success.
- **Track Registered Players**: Whether to count by registration or live presence.
- **Count Display Enabled**: Enables visual count display panel.
- **Check Frequency**: Frequency of count checks against the target.
- **Class / Team Restrictions**: Filter counted players by team or class.

## ✈️ Common Usage: Step-by-Step Example

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

## 🧰 Usage Example

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

## 🧠 Best Practices

- Set comparison mode (equal, greater than, etc.) carefully
- Use team/class filters for co-op or versus mechanics
- Display info panel for player feedback
- Chain with `Enable()`, `SetTargetCount()`, `ShowInfoPanel()` for dynamic logic
- Combine with:
  - `barrier_device` for gate control
  - `hud_message_device` to show entry/exit prompts
  - `trigger_device` to enable counting only in key areas

## ❌ Incorrect Usage Examples and Fixes

| Issue                              | ❌ Wrong Example             | ✅ Correct Example                         | Explanation                  |
| ---------------------------------- | --------------------------- | ----------------------------------------- | ---------------------------- |
| No `@editable` assignment          | Device unassigned           | Assign via `@editable` in Details panel   | Prevents null errors         |
| Missing Compare Mode               | Compare mode left unset     | Set to appropriate logic (Equal, etc.)    | No events will trigger       |
| Not Subscribing to Events          | No `Subscribe()` called     | Subscribe to events in `OnBegin`          | Required for event handling  |
| Calling GetCount() before Enable() | `GetCount()` fails silently | Always call `Enable()` first              | Device not active yet        |
| Expecting auto target updates      | Target count never changes  | Use `SetTargetCount()` or adjust manually | Dynamic updates require code |

## 🌟 Great For:

- Puzzle or boss fights requiring multiple players
- Group-based doors or platforms
- Co-op mechanics and escape rooms
- Dynamic team logic gates
- Custom respawn or checkpoint areas

