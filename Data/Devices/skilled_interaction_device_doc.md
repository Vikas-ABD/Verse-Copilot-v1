📘 **skilled_interaction_device – UEFN Verse Device Documentation**

---

🔹 **Description**
The `skilled_interaction_device` is a timing-based minigame system used to challenge players with precise input timing. When activated, players see a scrubber moving from 0.0 to 1.0 and must press a button while it’s inside the defined *Good Zone* or *Perfect Zone*.

Supports queues, multiplayer interactions, difficulty tuning, and failure/success conditions — ideal for:
- Lockpicking minigames
- Crafting or repair mechanics
- Rhythm games or reaction tests
- Team-based coordination challenges

---

🧱 **Imports Required**
```verse
using { /Fortnite.com/Devices }
```

---

🔗 **Inheritance Hierarchy**
| Class                    | Description                                         |
|-------------------------|-----------------------------------------------------|
| `creative_object`       | Base class for all props/devices.                  |
| `creative_device_base`  | Adds standard device logic (enable/disable, transforms). |
| `skilled_interaction_device` | Adds interactive input-based minigame system.         |

---

🔌 **Exposed Interfaces**
| Interface   | Description                                    |
|------------|------------------------------------------------|
| `enableable` | Allows enabling and disabling the device during runtime. |

---

🔁 **Listenable Events**
| Event Name                   | Payload         | Description                                             |
|-----------------------------|------------------|---------------------------------------------------------|
| `InteractionStartedEvent`   | agent            | Fires when an agent begins the interaction.             |
| `GoodInputTriggeredEvent`   | (agent, float)   | Fires when input is within the Good Zone, but not Perfect. |
| `PerfectInputTriggeredEvent`| (agent, float)   | Fires when input is inside the Perfect Zone.            |
| `BadInputTriggeredEvent`    | (agent, float)   | Fires when input is outside the Good Zone.              |
| `InteractionSucceededEvent` | agent            | Fires when success conditions are met.                  |
| `InteractionFailedEvent`    | agent            | Fires when failure conditions are met.                  |
| `InteractionCanceledEvent`  | agent            | Fires when interaction is interrupted.                  |
| `QueueAgentEvent`           | agent            | Fires when an agent is added to the interaction queue.  |
| `RemoveAgentFromQueueEvent` | agent            | Fires when an agent is removed from the queue.          |
| `AdvanceAgentFromQueueEvent`| agent            | Fires when a queued agent begins their interaction.     |
| `EmptyQueueEvent`           | void             | Fires when the queue becomes empty.                     |

---

🧰 **Core Methods**
| Method Signature                                  | Description                                             |
|--------------------------------------------------|---------------------------------------------------------|
| `Enable(): void`                                 | Enables the device, allowing interaction.               |
| `Disable(): void`                                | Disables the device and ends interactions.              |
| `BeginInteraction(agent)` / `BeginInteraction([]agent)` | Starts interaction(s). Will queue or begin immediately based on settings. |
| `EndInteraction(agent)` / `EndInteraction([]agent)`     | Cancels current interaction(s) for agent(s). Doesn’t affect queue. |
| `GetInteractingAgents(): []agent`                | Returns all agents currently in an interaction.         |
| `GetQueue(): []agent`                            | Returns the queue of agents awaiting interaction.       |
| `ClearQueue(): []agent`                          | Clears the queue and returns removed agents.            |
| `RemoveFromQueue(agent, remove_all?: logic): int`| Removes one or all instances of the agent from the queue. |
| `IsEnabled(): logic`                             | Returns whether the device is enabled.                  |
| `GetTransform()`, `MoveTo()`, `TeleportTo()`     | Standard movement/transform logic.                      |

---

⚙️ **Key Configuration Options (Details Panel)**
| Option                          | Description                                           |
|---------------------------------|-------------------------------------------------------|
| `Good Zone Size (GoodZoneSize)` | Fraction of meter range that counts as a Good hit.   |
| `Perfect Zone Size (PerfectZoneSize)` | Fraction of Good Zone that counts as Perfect hit.    |
| `Meter Speed (MeterSpeed)`      | Speed the scrubber moves (1–400 %/sec).               |
| `Failure Limit (FailureLimit)`  | How many bad inputs allowed (0–5).                   |
| `Success Target (SuccessTarget)`| How many successful inputs required (0–5).           |
| `Interaction Time Limit (InteractTimeLimit)` | Max time allowed to complete interaction (0–120s). |
| `Lockout On Fail Time (LockOutOnFailTime)` | Optional cooldown after a bad input.                |
| `Maximum Queued Players`        | Queue size cap.                                      |
| `Synchronous Player Limit`      | Max players allowed to interact at once.             |
| `Next In Queue Execution Delay` | Delay before next queued player begins.              |
| `Allow Duplicate Player Entries`| Whether a player can queue more than once.           |

---

🚦 **Example Usage in Verse**
```verse
using { /Fortnite.com/Devices }

skill_minigame := class(
    @editable SkillDevice: skilled_interaction_device
)

OnBegin<override>()<suspends>: void =
    SkillDevice.Enable()
    SkillDevice.InteractionSucceededEvent.Subscribe(OnSuccess)
    SkillDevice.InteractionFailedEvent.Subscribe(OnFail)

StartMinigameFor(Player: agent): void =
    SkillDevice.BeginInteraction(Player)

OnSuccess(Player: agent): void =
    Print("✅ {Player} succeeded in the minigame!")

OnFail(Player: agent): void =
    Print("❌ {Player} failed the minigame.")
```

---

🧠 **Best Practices**
- Use for lock minigames, skill checks, or crafting validation.
- Tweak `MeterSpeed`, zone sizes, and `SuccessTarget` for difficulty tuning.
- Use queue logic for multiplayer fairness and pacing.
- Combine with:
  - `barrier_device` to gate progression
  - `vfx_creator_device` for skill-based effect feedback
  - `score_manager_device` to reward perfect interactions
- Use `InteractionCanceledEvent` to handle unexpected interruptions.

---

❌ **Common Mistakes & Fixes**
| Issue                    | ❌ Wrong                        | ✅ Fix                             | Explanation                               |
|-------------------------|----------------------------------|------------------------------------|-------------------------------------------|
| Device doesn’t start    | `BeginInteraction()` fails silently | Ensure device is `Enable()`d first | Device must be enabled before use.        |
| Instant failure         | `FailureLimit = 0`               | Set to 1+ for more forgiving timing | Prevents instant failure on first mistake. |
| Multiple agents overlap | `SynchronousPlayerLimit` too low | Increase limit or queue players    | Avoids interaction collisions.            |
| Queue misbehaving       | Misused `AllowDuplicatePlayerEntries` or queue size | Adjust logic carefully | Proper queue settings prevent bugs.        |

---

✅ **Great for:**
- Lockpicking, hacking, or vault-opening mechanics
- Button-press rhythm or timing puzzles
- Multiplayer skill gates
- Combat buffs based on timing
- High-skill bonus events

