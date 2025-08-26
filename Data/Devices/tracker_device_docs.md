📘 **tracker_device – UEFN Verse Device Documentation**

---

🔹 **Description**

The `tracker_device` lets you create, update, and HUD-track custom objectives for players or teams to complete in your UEFN game. It is useful for:
- Scoreboards
- Quest tracking
- Item collection
- Progress bars
- Mini-challenges
- Boss fight goals

The device supports per-agent, per-team, or all-player/agent progress tracking and can trigger events when targets are reached.

---

🧱 **Verse Using Statement**
```verse
using { /Fortnite.com/Devices }
```

---

🔗 **Inheritance Hierarchy**
- `creative_object`
- `creative_device_base`
- `tracker_device`

---

🛠️ **Key Functions & Methods**

| Name                    | Description                                                |
|-------------------------|------------------------------------------------------------|
| `SetTitleText(message)` | Sets the tracker’s HUD title (max 32 characters).           |
| `SetDescriptionText(message)` | Sets the HUD description (max 64 characters).          |
| `SetTarget(int)`        | Sets the completion value (0–10,000).                     |
| `GetTarget()`           | Gets the current target value.                             |
| `Assign(agent)`         | Assigns the device to a specific agent (player).           |
| `AssignToAll()`         | Assigns to all valid agents.                               |
| `Remove(agent)`         | Removes an agent's assignment.                             |
| `RemoveFromAll()`       | Removes assignment from all agents.                        |
| `IsActive(agent)`       | Returns true if the agent is assigned and active.          |
| `HasReachedTarget(agent)` | Checks if agent reached target.                        |
| `Increment(agent)`      | Increments agent’s tracker value by "amount to change".    |
| `Decrement(agent)`      | Decrements agent’s tracker value.                         |
| `SetValue(agent, int)`  | Sets agent’s tracker value directly.                      |
| `GetValue(agent)`       | Gets agent’s current tracker value.                        |
| `Complete(agent)`       | Marks tracker complete for an agent.                      |
| `Reset(agent)`          | Resets the agent’s tracker.                               |
| `ClearPersistence(agent)` | Clears saved progress if persistence enabled.           |
| `Save/Load(agent)`      | Saves/loads agent’s tracker progress.                    |

---

🧹 **Events (Data Members)**

| Event Name        | Type               | Description                                     |
|-------------------|--------------------|-------------------------------------------------|
| `CompleteEvent`   | `listenable(agent)`| Triggers when an agent reaches the target value |

---

🎛 **Configuration Options (Details Panel)**

- **Target Value**: Value needed for completion (integer).
- **Sharing**: Choose from Individual / Team / All.
- **HUD Tracking**: Enable to show tracker on player HUD.
- **Amount to Change**: Value used in increment/decrement.
- **Track Stat Type**: Enable stat-based tracking.
- **Persistence Use**: Save/load across sessions.
- **Completion Event**: Trigger linked devices on completion.

---

📊 **Verse Usage Example**
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

tracker_device_example := class(creative_device):

    @editable
    Tracker : tracker_device = tracker_device{}

    @editable
    ProgressButton : button_device = button_device{}

    @editable
    CompleteButton : button_device = button_device{}

    @editable
    ResetButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        Tracker.CompleteEvent.Subscribe(OnTrackerComplete)
        ProgressButton.InteractedWithEvent.Subscribe(OnProgress)
        CompleteButton.InteractedWithEvent.Subscribe(OnComplete)
        ResetButton.InteractedWithEvent.Subscribe(OnReset)

        Tracker.SetTitleText(StringToMessage("Objective Progress"))
        Tracker.SetDescriptionText(StringToMessage("Complete the objective to win!"))
        Tracker.SetTarget(10)

    OnTrackerComplete(Agent : agent) : void =
        Print("Tracker completed by agent!")

    OnProgress(Agent : agent) : void =
        Tracker.Increment(Agent)
        Print("Tracker progress incremented")

    OnComplete(Agent : agent) : void =
        Tracker.Complete(Agent)
        Print("Tracker completed")

    OnReset(Agent : agent) : void =
        Tracker.Reset(Agent)
        Print("Tracker reset")

    StringToMessage<localizes>(InString : string) : message = "{InString}"
```

---

📃 **How to Use in UEFN**

1. **Place Devices**
    - Drag a `tracker_device` onto your island.
    - Add `button_device`s for demo or control (progress, complete, reset).

2. **Configure Tracker**
    - Set `Target Value`, `Sharing`, and `Amount to Change`.
    - Enable `Show on HUD`.
    - Set title/description.

3. **Create a Verse Script**
    - In Verse Explorer: Right-click folder > Create New Verse File (e.g., `tracker_device_example.verse`).
    - Paste and save the example code.

4. **Build & Place Verse Device**
    - Click **Verse > Build Verse Code** (Ctrl+Shift+B).
    - Drag custom Verse device into world and assign references.

5. **Playtest**
    - Start a session and interact with the buttons.
    - Watch progress update on HUD and completion trigger.

---

🧠 **Tips**

- Combine `tracker_device` with `timer_device`, `item_granter_device`, or `score_manager_device`.
- Enable "Use Persistence" for saved quests.
- Use `Assign()`/`Remove()` for dynamic quests.

---

❌ **Common Issues & Solutions**

| Issue                   | Possible Reason                    | Solution                                |
|-------------------------|-------------------------------------|-----------------------------------------|
| HUD not updating        | "Show on HUD" not enabled           | Enable HUD tracking in Details panel    |
| Objective not progressing | Incorrect agent parameter used     | Use correct agent argument in functions |
| Progress not saved      | "Use Persistence" not enabled       | Enable and call Save/Load in Verse      |

---

**Note**:
- For XP/stat tracking, use stat types or custom rewards in event handlers.
- Tracker progress can be global or personalized based on Sharing config.
- Entire tracker logic can be managed in Verse for custom game logic.

