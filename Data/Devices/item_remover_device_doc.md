## item_remover_device – UEFN Verse Device Documentation

### 🔹 Description
The `item_remover_device` allows you to remove items from a player’s inventory, either by forcing them to drop or permanently deleting them. It can be used to simulate item loss, loot drops, or inventory clearing in response to specific gameplay events such as a player being Down But Not Out (DBNO), eliminated, or entering a restricted zone.

This device is essential for game modes where risk, penalty, or item transfer is part of the gameplay loop (e.g., extraction shooters, PvPvE, or survival games).

---

### 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
| Class                  | Description                                        |
|------------------------|----------------------------------------------------|
| `creative_object`      | Base class for all props and devices.              |
| `creative_device_base` | Adds enabling/disabling and transform methods.     |
| `item_remover_device`  | Used to drop or remove items from an agent's inventory. |

---

### ⟳ Main Event
This device does **not** emit listenable events. It performs its function via **direct method calls**, typically from Verse or connected devices.

---

### 🛠️ Core Methods
| Method Signature                           | Description                                                 |
|--------------------------------------------|-------------------------------------------------------------|
| `RemoveItems(Player: agent): void`         | Removes items from the specified player's inventory.        |
| `Enable(): void`                           | Enables the device.                                         |
| `Disable(): void`                          | Disables the device.                                        |
| `IsEnabled(): logic`                       | Returns whether the device is currently enabled.            |
| `GetTransform(): transform`                | Returns device transform (useful only in spatial setup).    |
| `TeleportTo(...)` / `MoveTo(...)`          | Optional — move or animate the device (not needed for basic use). |

---

### ⚙️ Configuration Options (Details Panel)
| Option                   | Description                                                        |
|--------------------------|--------------------------------------------------------------------|
| Remove Items On Activation | Whether items should be removed when the device is activated.       |
| Drop or Destroy          | Choose whether items are dropped into the world or deleted.         |
| Affect Equipped Items    | Toggle whether equipped items are affected or only carried ones.    |
| Affected Slots           | Define which inventory slots are impacted (e.g., all, specific range). |
| Team Restrictions        | Limit which players are affected by team.                          |
| Class Restrictions       | Limit behavior based on player class.                              |

---

### 🚦 Triggering
Device can be triggered through `button_device`, `trigger_device`, or any custom logic in Verse.

---

### 🛠️ Common Usage: Step-by-Step Example
```verse
using { /Fortnite.com/Devices }

item_drop_handler := class(
    @editable ItemRemover: item_remover_device
)

OnBegin<override>() :=
    ItemRemover.Enable()

ForceDropItems(Player: agent): void =
    if (ItemRemover.IsEnabled()):
        ItemRemover.RemoveItems(Player)
```

---

### 🛠️ Usage Example 2
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

item_remover_example := class(creative_device):

    @editable
    ItemRemover : item_remover_device = item_remover_device{}

    @editable
    DBNODevice : down_but_not_out_device = down_but_not_out_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        DBNODevice.AgentDownedEvent.Subscribe(OnPlayerDowned)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnPlayerDowned(Agent : agent) : void =
        ItemRemover.RemoveItems(Agent)
        Print("Items removed from downed player")

    OnEnablePressed(Agent : agent) : void =
        ItemRemover.Enable()
        Print("Item remover enabled")

    OnDisablePressed(Agent : agent) : void =
        ItemRemover.Disable()
        Print("Item remover disabled")
```

---

### 🧠 Best Practices
* Carefully set "Affected Objects" (e.g., only weapons, building resources, or all).
* Use "Drop Items" for loot mechanics; "Remove Items" for penalty mechanics.
* Use "Apply To" settings for team/class-wide effects.
* Pair with `down_but_not_out_device` or similar event triggers.
* Combine with `elimination_feed_device` or UI indicators for clarity.

---

### ❌ Incorrect Usage Examples and Fixes
| Issue                          | ❌ Wrong Example                | ✅ Correct Example                        | Explanation                                            |
|-------------------------------|-----------------------------------|---------------------------------------------|--------------------------------------------------------|
| Not assigning device ref      | Not referencing in Verse/Panel    | Reference with `@editable` and set in panel | Prevents nil/error calls                              |
| Wrong argument type           | Passing a player, not agent       | Use only valid `agent` objects              | Only agents are supported                             |
| No items removed              | Not configuring "Affected Objects"| Select correct options in Details panel     | Device won't affect anything otherwise                |
| Calling before enabling       | Calling `RemoveItems()` directly  | Always call `Enable()` before removing      | Device must be enabled to perform operations          |

---

### 🚀 Great For:
* Inventory loss in PvPvE or DBNO scenarios
* Extract-or-lose mechanics
* Penalty zones or enforcement areas
* Shared loot redistribution
* Stealing from downed/eliminated players

