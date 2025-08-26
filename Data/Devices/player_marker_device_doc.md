## UEFN Verse Device Documentation: `player_marker_device`

### 🔹 Description
The `player_marker_device` is used to mark agents (players) in the world, displaying their location on the minimap and optionally attaching custom visual data such as health bars, shield bars, distance, custom icons, and labels.

#### Common Use Cases
- Team role indicators (e.g., VIP, Medic, Leader)
- Bounty-style tracking or escort objectives
- Co-op gameplay feedback (e.g., showing distance to allies)
- Puzzle/quest design (e.g., follow the marked player)

Markers can be dynamically attached or detached using Verse. The device also supports item tracking that fires events based on inventory conditions.

---

### 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
| Class                   | Description                                               |
|------------------------|-----------------------------------------------------------|
| `creative_object`      | Base class for props and devices.                        |
| `creative_device_base` | Adds general creative device logic.                      |
| `player_marker_device` | Attaches minimap markers with customizable info to agents.|

---

### ⟳ Listenable Events
| Event Name                      | Type             | Description                                                                 |
|---------------------------------|------------------|-----------------------------------------------------------------------------|
| `FirstItemValueChangedEvent`   | listenable(agent)| Fires when the first tracked item value changes on a marked agent.          |
| `FirstItemValueReachedEvent`   | listenable(agent)| Fires when a marked agent's item quantity meets a specific threshold.       |
| `SecondItemValueChangedEvent`  | listenable(agent)| Fires when the second tracked item value changes on a marked agent.         |
| `SecondItemValueReachedEvent`  | listenable(agent)| Fires when a marked agent meets the condition for the second item tracker.  |

---

### 🧰 Core Methods
| Method Signature                    | Description                                                         |
|------------------------------------|---------------------------------------------------------------------|
| `Attach(Agent: agent): void`       | Adds a marker to the specified agent.                              |
| `Detach(Agent: agent): void`       | Removes the marker from the specified agent.                       |
| `DetachFromAll(): void`            | Removes all currently active player markers.                       |
| `Enable(): void`                   | Enables the device so it can show or manage markers.               |
| `Disable(): void`                  | Disables the device — markers will not function.                   |
| `GetTransform(): transform`        | Returns the device's transform (not commonly used).                |
| `MoveTo(...)` / `TeleportTo(...)`  | Move or reposition the device (not typically needed).              |

---

### ⚙️ Configuration Options (Details Panel)
| Option              | Description                                                                          |
|---------------------|--------------------------------------------------------------------------------------|
| Show Health Bar     | Displays a health bar on the marked agent.                                           |
| Show Shield Bar     | Adds a shield bar beneath the health display.                                        |
| Show Distance       | Shows the distance to the marked agent.                                              |
| Custom Label        | Sets a custom name/label above the agent.                                            |
| Minimap Icon        | Specifies the icon used for the marker.                                              |
| Icon Color          | Assigns a color to the minimap icon.                                                 |
| Track Item Conditions | Enables triggering events based on inventory items.                               |
| Visibility Rules    | Configures marker visibility (e.g., team-only, all players, specific classes).       |

---

### 🚦 Common Usage Example
```verse
using { /Fortnite.com/Devices }

marker_example := class(
    @editable Marker: player_marker_device
):

    OnBegin<override>()<suspends>: void =
        Marker.Enable()

    MarkPlayer(Player: agent): void =
        Marker.Attach(Player)

    UnmarkPlayer(Player: agent): void =
        Marker.Detach(Player)
```

---

### 🧠 Best Practices
- Use `Attach()` when players enter a tracked state (e.g., VIP, bounty target).
- Use `FirstItemValueReachedEvent` to trigger gameplay logic.
- Pair with `hud_message_device` or `elimination_feed_device` for announcements.
- Use `DetachFromAll()` to clear markers at round end or upon player elimination.
- Configure visibility for tactical gameplay or puzzle mechanics.

---

### ❌ Incorrect Usage Examples and Fixes
| Issue                          | ❌ Wrong         | ✅ Fix                            | Explanation                                                         |
|--------------------------------|--------------------|-------------------------------------|---------------------------------------------------------------------|
| Forgetting to call `Attach()` | Marker doesn't appear | Call `Attach()` after enabling     | Must explicitly attach the agent in Verse.                          |
| Calling before `Enable()`     | Marker doesn’t display | Enable the device first           | Device must be enabled to show markers.                            |
| Passing `none` to `Attach()`  | `Attach(none)`     | Pass a valid agent                 | Must always pass a valid player/agent.                             |
| Expecting prop to be marked   | Marks a world prop | Use only with agents/players       | Device is for agent tracking only, not objects or actors.           |

---

### ✨ Ideal Use Cases
- Tactical minimap tracking in team or co-op modes
- Highlighting key players like VIPs or medics
- Inventory-based puzzle and quest logic
- Visual role indicators in narrative-driven games
- Escort and follow objectives in questlines

