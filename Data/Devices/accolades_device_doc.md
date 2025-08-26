## accolades_device – UEFN Verse Device Documentation

### 🔹 Description
The `accolades_device` is used to define and award accolades — achievements or milestones that players can complete to earn Battle Pass XP on your island. Each accolade is configured within the device settings in the UEFN editor and can be awarded dynamically through Verse scripting.

This is ideal for adding progression, rewarding exploration or objectives, and encouraging replayability in your island. XP is awarded via the `Award()` function, and each device should be configured with unique accolade data like name, description, XP amount, and trigger conditions.

> ⚠️ XP can only be granted on published islands approved for XP. In unpublished sessions, use `TestAwardEvent` to simulate behavior.

---

### 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
```

---

### 🧬 Inheritance Hierarchy
| Class | Description |
|-------|-------------|
| `creative_object` | Base class for all props and devices. |
| `creative_device_base` | Adds core device behavior. |
| `accolades_device` | Device that grants players Battle Pass XP through configured accolades. |

---

### ⟲ Main Event
| Event Name | Type | Description |
|------------|------|-------------|
| `TestAwardEvent` | `listenable(agent)` | Fires only in unpublished sessions when the accolade is awarded via `Award()`. Useful for verifying the logic in development. |

#### Example Subscription:
```verse
MyAccoladeDevice.TestAwardEvent.Subscribe(OnTestAward)

OnTestAward(Player: agent): void =
    Print("Test accolade awarded to: {Player}")
```

---

### 🛠️ Core Methods
| Method Signature | Description |
|------------------|-------------|
| `Award(Player: agent): void` | Grants the configured accolade to the specified player. XP awarded in published islands with approved settings. |
| `Enable(): void` | Activates the device. |
| `Disable(): void` | Deactivates the device; XP will not be awarded. |
| `GetTransform(): transform` | Gets the transform (position, rotation, scale) in cm. Requires `IsValid()` check. |
| `MoveTo(Position, Rotation, Time): void` | Moves the device over time. |
| `MoveTo(Transform, Time): void` | Moves using a full transform. |
| `TeleportTo(Position, Rotation): void` | Instantly teleports the device. |
| `TeleportTo(Transform): void` | Instantly teleports using full transform. |

---

### ⚙️ Setup in UEFN Editor
Configure the following in the Details panel:
* 🆔 Accolade ID — Unique identifier
* 🏆 Accolade Name — Displayed to player
* 📜 Description — How it was earned
* 🌟 XP Amount — XP granted
* 🔁 Cooldown/Limit Settings — Rate control
* 👁️ Visibility — Public, hidden, secret

---

### ⚖️ Common Usage: Step-by-Step Example
```verse
using { /Fortnite.com/Devices }

accolade_awarder := class(
    @editable AccoladeDevice: accolades_device
):

    OnBegin<override>() :=
        AccoladeDevice.Enable()

    OnObjectiveComplete(Player: agent): void =
        AccoladeDevice.Award(Player)
```

---

### ❌ Incorrect Usage Examples and How to Fix
| Issue | ❌ Wrong | ✅ Fix | Explanation |
|-------|------------|----------|-------------|
| Calling Award with no player | `Award(none)` | `Award(Player)` | Must pass valid agent |
| Expecting real XP in editor | No XP during dev | Use `TestAwardEvent` | XP only granted on published islands |
| Forgetting to configure | Placed device with no data | Define Accolade ID, name, XP | Device won't function otherwise |
| Multiple awards too quickly | Repeated `Award()` calls | Use cooldowns in settings | Prevent XP farming |
| Player uses device directly | Drag into world for interaction | Trigger via Verse or other devices | Not interactable by players |
| Misassigned @editable | Not assigned post-placement | Set editable refs in Details | Avoid nil/error on use |
| Wrong argument type | `Award(player)` (wrong type) | `Award(agent)` | Must pass `agent` type only |

---

### 🧠 Best Practices
* Assign multiple accolade devices using `@editable` for different achievements.
* Use `TestAwardEvent` to test logic before publishing.
* Combine with gameplay triggers, timers, trackers, and logic devices for meaningful XP.
* Space out accolades and calibrate rewards fairly to ensure approval.
* Hidden accolades are useful for secret objectives or easter eggs.
* Use XP weighting appropriately (Very Small to Very Large) based on achievement difficulty and rarity.
* Prevent abuse by limiting award count per player.
* Epic recalibrates final XP reward values after playtesting.

---

### 🌟 Great for:
* Rewarding progress, exploration, and objectives
* Granting XP for PvP or PvE milestones
* Supporting replayability via unlockable content
* Motivating players through milestone achievements
* Creating hidden or bonus XP systems

---

