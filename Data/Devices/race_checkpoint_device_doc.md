# Race Checkpoint Device – UEFN Verse Device Documentation

## 📙 Description
The `race_checkpoint_device` defines intermediate targets in a race course, working alongside the `race_manager_device` to create sequential checkpoint racing. Players must pass through each enabled checkpoint (in the correct order, if sequenced) to complete laps or races. This device controls when checkpoints are active, handles player progression, and can trigger events or signals for advanced race logic, time trials, or competitive gameplay.

## 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
  - Base class for creative devices and props.
- `creative_device_base`
  - Base class for creative_device.
- `race_checkpoint_device`

## 🧩 Core Events & Methods
| Name | Type / Signature | Description |
|------|------------------|-------------|
| `CheckpointCompletedEvent` | `listenable(agent)` | Fires when a player passes through this checkpoint. |
| `CheckpointBecomesCurrentEvent` | `listenable(agent)` | Fires when this checkpoint becomes the current objective for an agent. |
| `CheckpointBecomesCurrentForTheFirstTimeEvent` | `listenable(agent)` | Fires only the first time this checkpoint becomes current for any agent. |
| `Enable()` | `void` | Enables this checkpoint (active; can be passed by players). |
| `Disable()` | `void` | Disables this checkpoint (cannot be passed until re-enabled). |
| `SetAsCurrentCheckpoint(Agent)` | `void` | Assigns this checkpoint as current for the agent, if not yet passed. |
| `GetTransform()` | `transform` | Returns the transform of the device. Used for runtime logic. |

## 🎛 Configuration Options (Details Panel)
| Option | Description |
|--------|-------------|
| Checkpoint Number | Order in the race route (set unique numbers for each). |
| Visible Before Race Start | Yes / No |
| Enabled During Phase | Pre-Game / Gameplay / None |
| Allow Pass Without Vehicle | Yes / No |
| Current/Completed Checkpoint Color | Color for active and finished checkpoints. |
| Disable/Enable When Receiving From | Bind checkpoint state to device signals. |

## 🛠 Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

race_example := class(creative_device):

    @editable
    RaceManager : race_manager_device = race_manager_device{}

    @editable
    Checkpoints : []race_checkpoint_device = array{}

    OnBegin<override>()<suspends> : void =
        RaceManager.RaceBeganEvent.Subscribe(OnRaceStarted)
        RaceManager.RaceCompletedEvent.Subscribe(OnRaceCompleted)

        for (Checkpoint : Checkpoints):
            Checkpoint.CheckpointCompletedEvent.Subscribe(OnCheckpointCompleted)

        SetupCheckpoints()

    SetupCheckpoints() : void =
        for (Index -> Checkpoint : Checkpoints):
            if (Index = 0):
                Checkpoint.Enable()
            else:
                Checkpoint.Disable()

    OnRaceStarted(Agent : agent) : void =
        Print("Race started!")

    OnRaceCompleted(Agent : agent) : void =
        Print("Race completed!")

    OnCheckpointCompleted(Agent : agent) : void =
        Print("Checkpoint reached!")

        for (Index -> Checkpoint : Checkpoints):
            if (IsCheckpointValid[Checkpoint, Agent]):
                if (NextIndex := Index + 1, NextIndex < Checkpoints.Length):
                    if (NextCheckpoint := Checkpoints[NextIndex]):
                        NextCheckpoint.Enable()

    IsCheckpointValid(Checkpoint : race_checkpoint_device, Agent : agent)<transacts><decides> : void =
        void

    GetCheckpointIndex(Checkpoint : race_checkpoint_device)<transacts><decides> : int =
        for (Index -> CP : Checkpoints):
            if (Index = 0):
                Index
        0
```

## 🧠 How It Works
- Place multiple `race_checkpoint_device` objects in your level at each crucial section of your race.
- Assign `Checkpoint Number` (e.g., 1, 2, 3, etc.) for course order.
- Use a `race_manager_device` to coordinate player progress, laps, and display.
- Enable only the first checkpoint at the start; when a checkpoint is passed, the next in the sequence can be enabled.
- Subscribe to checkpoint (and manager) events in Verse for custom logic like split times, analytics, or alternate goals.

## 🧠 Best Practices
- Always configure each checkpoint’s number and vehicle requirement for consistent progression.
- Use `Visible Before Race Start` and color settings for player clarity.
- Bind `Disable When Receiving From` and `Enable When Receiving From` for dynamic course control (timers, triggers, etc.).
- In advanced logic, use `SetAsCurrentCheckpoint(Agent)` to assign agents to special or bonus checkpoints.

## ❌ Common Mistakes and Fixes
| Issue | ❌ Wrong Example | ✅ Correct Example | Explanation |
|-------|-------------------|-----------------------|-------------|
| No unique checkpoint numbers | All have 1 | Assign a unique number per device | Prevents skipped/repeated checkpoints |
| Not disabling unused checkpoints | All active at start | Only enable first, activate others on progress | Guides race flow and logic |
| Not subscribing to event | No event/logic tied to checkpoint | Use `CheckpointCompletedEvent.Subscribe(...)` | Enables custom race scripts |

## Note
- For full race logic, always use with a `race_manager_device` and coordinate with timers, triggers, accolade/XP devices, or UI as needed.
- The full example Verse code above shows sequential activation, event subscriptions, and best organizational practices for building races in UEFN.

