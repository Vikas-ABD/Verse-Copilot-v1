📘 **elimination\_manager\_device – UEFN Verse Device Documentation**

---

🔹 **Description** The `elimination_manager_device` allows you to spawn items at the location of an agent or target when they are eliminated. It's commonly used to create custom loot drops, rewards, or advanced objectives when players, creatures, sentries, or other eliminatable entities are eliminated in your Fortnite experience.

**Configurable Features:**

- Which items are dropped (by physically dropping items on the device in UEFN)
- Target types
- Drop count
- Drop chance
- Spawn distance
- Movement of items
- Item scaling and ammo configuration

---

🧱 **Verse Using Statement**

```verse
using { /Fortnite.com/Devices }
```

---

🔗 **Inheritance Hierarchy**

- creative\_object
- creative\_device\_base
- base\_item\_spawner\_device
- elimination\_manager\_device

---

🥉 **Data Members (Events)**

| Name              | Type              | Description                                                                    |
| ----------------- | ----------------- | ------------------------------------------------------------------------------ |
| EliminatedEvent   | listenable(agent) | Fires when a qualifying elimination occurs; returns agent.                     |
| EliminationEvent  | listenable(agent) | Fires when a qualifying elimination occurs; returns eliminator agent (if any). |
| ItemPickedUpEvent | listenable(agent) | Fires when an agent picks up an item spawned by this device.                   |

---

🛠️ **Functions & Methods**

| Name                  | Description                                             |
| --------------------- | ------------------------------------------------------- |
| Enable()              | Enables the device to spawn drops.                      |
| Disable()             | Disables the device; prevents future item drops.        |
| GetTransform()        | Returns device’s current position, rotation, and scale. |
| MoveTo()/TeleportTo() | Move or instantly teleport the device.                  |

---

🎮 **Configuration Options (Details Panel)**

- **Enabled At Game Start**: On/Off toggle for device activation at game start.
- **Number of Items Dropped**: Number or "All" of registered items to drop.
- **Valid on Self-Elimination**: Toggle to allow drops on self-elimination.
- **Target Type**: Specify targets (Players Only, Creatures, Sentries, etc).
- **Initial Movement of Item**: Choose item motion: None, Gravity, Toss.
- **Random Drop**: Options include Off, Random, No Repeats.
- **Drop Chance**: Percent chance (e.g., 100%, 10%) per elimination.
- **Random Spawn Distance**: Distance in meters from elimination point.
- **Run Over Pickup**: Enable to allow pickup by running over item.
- **Item Scale**: Modify the size of spawned items.
- **Initial Weapon Ammo / Spare Weapon Ammo**: Override weapon drop ammo.
- **Selected Team/Class**: Restrict drops to selected team/class.
- **Invert Selected Team/Class**: Invert team/class inclusion logic.

---

🛠️ **Verse Usage Example**

```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

elimination_manager_example := class(creative_device):

    @editable
    EliminationManager : elimination_manager_device = elimination_manager_device{}

    OnBegin<override>()<suspends> : void =
        EliminationManager.EliminatedEvent.Subscribe(OnElimination)
        EliminationManager.ItemPickedUpEvent.Subscribe(OnItemPickedUp)

    OnElimination(Agent : agent) : void =
        Print("Agent eliminated - spawning items!")

    OnItemPickedUp(Agent : agent) : void =
        Print("Item picked up by agent!")
```

**Explanation:**

- Subscribes to `EliminatedEvent` and `ItemPickedUpEvent`.
- Executes `OnElimination` when a qualifying target is eliminated.
- Executes `OnItemPickedUp` when item is collected by an agent.
- All item behavior (what drops, randomness, etc.) is configured in UEFN.

---

💪 **How to Set Up in UEFN**

1. **Place Devices in Level**

   - Add `elimination_manager_device` in scene.
   - Drop desired items on device to register them.

2. **Configure Options (Details Panel)**

   - Set target type, drop number, motion, spawn radius, etc.
   - Set random drop rules, drop chance, and team/class filters.

3. **Create & Build Verse Script**

   - In Verse Explorer: Create new file (e.g., `elimination_manager_example.verse`).
   - Paste example code and build (Ctrl+Shift+B).

4. **Place and Reference Your Verse Device**

   - Drag `elimination_manager_example` Verse device into world.
   - Assign `EliminationManager` in the Details panel.

5. **Test & Iterate**

   - Test eliminations to verify item drops and pickup logic.
   - Use logs to confirm events are triggered.

---

🧠 **Best Practices**

- For <100% drop chance, communicate rarity to players.
- Pair with device signals/channels for quests or objectives.
- Use `ItemPickedUpEvent` to reward or update player progress.

---

❌ **Common Issues & Fixes**

| Issue                     | Wrong Example                  | Correct Example                          | Explanation                                        |
| ------------------------- | ------------------------------ | ---------------------------------------- | -------------------------------------------------- |
| Drop not active           | Didn't assign items in editor  | Physically assign/drop items on device   | Must register items before runtime                 |
| Not subscribing to events | No event triggered             | Use `.Subscribe(...)` in Verse           | Required for logic to respond to game events       |
| Device not enabled        | "Enabled At Game Start" is off | Set to On or call `.Enable()` in Verse   | Device must be active                              |
| Over-restrictive filters  | Testing with wrong target type | Match filters to test scenario           | Drops only occur for selected targets              |
| Missing reference         | Left `@editable` field blank   | Assign device reference in Details panel | Verse script needs reference to function correctly |

---

📅 **Note:**

- Ideal for loot-based, progression, and collectathon games.
- Dropped items must be pre-registered per session.
- Combine with Verse and gameplay systems for powerful results.

