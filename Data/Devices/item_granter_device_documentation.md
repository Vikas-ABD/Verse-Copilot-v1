## item_granter_device – UEFN Verse Device Documentation

### 🖊 Description
The `item_granter_device` is used to grant items to agents (players) either by directly adding to their inventory or by spawning/dropping the item at their location. This device is ideal for rewarding players, distributing key items, equipping kits, or integrating with puzzle/objective systems. Items must be registered with the device by dropping them onto it in Edit mode.

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- creative_object
- creative_device_base
- item_granter_device

### 🧹 Data Members (Events)
| Name              | Type               | Description                                  |
|-------------------|--------------------|----------------------------------------------|
| ItemGrantedEvent  | listenable(agent)  | Signals when an item is granted to an agent. |

### 🛠️ Functions & Methods
| Name                  | Description                                                            |
|-----------------------|------------------------------------------------------------------------|
| GrantItem(agent)      | Immediately grants the current item to the agent.                      |
| GrantItemIndex(index, agent) | Grants item by index to agent (if registered and index in range). |
| GrantItemToAll()      | Grants item(s) to all players (must allow in device settings).         |
| CycleToNextItem(agent) | Cycle to the next item. Auto-grants if enabled.                        |
| CycleToPreviousItem(agent) | Cycle to previous item.                                             |
| CycleToRandomItem(agent) | Cycle to a random registered item.                                  |
| Enable()              | Turns on the device.                                                   |
| Disable()             | Turns off the device.                                                  |
| RestockItems()        | Resets the device's inventory count (if tracking is enabled).          |
| SetNextItem(index)    | Sets the next item to be granted (by 0-based index).                   |
| ClearSaveData(agent)  | Clears saved data so agent can receive more grants.                    |
| GetItemIndex()        | Returns the current selected item index.                               |
| GetTransform()        | Gets the device's transform.                                           |
| MoveTo() / TeleportTo() | Move or teleport the device in the world.                            |

### 🎛 Configuration Options (Details Panel)
| Option                   | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| Enabled on Game Start     | Whether the device starts enabled.                                          |
| Receiving Players         | Restrict to Triggering Player/Team/All/Pick Team.                           |
| On Grant Action           | Inventory manipulation (clear/keep items/resources on grant).              |
| Grant                    | Grant Current, All items, or random.                                       |
| Grant Condition           | Only If Empty, If Not Owned, If Space, Always.                             |
| Grant on Cycle            | Grant item when cycling (Yes/No).                                          |
| Equip Granted Item        | Whether to auto-equip a granted weapon/item.                               |
| Spawns Location           | In Inventory vs. Dropped at agent’s feet.                                  |
| Allowed Team/Class        | Restrict who can receive the item(s).                                      |
| Visible in Game           | Show/hide 3D device model during play.                                     |
| Inventory Count           | Tracks how many grants are available (optional).                           |

Note: Drop desired items onto the device in the editor to register them as potential grants.

### 🛠️ Events
| Event              | Description                                             |
|--------------------|---------------------------------------------------------|
| ItemGrantedEvent   | Fires when an item is granted, with the agent as a parameter. |

### 🛠️ Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

item_granter_example := class(creative_device):

    @editable
    ItemGranter : item_granter_device = item_granter_device{}

    @editable
    GrantButton : button_device = button_device{}

    @editable
    CycleButton : button_device = button_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        ItemGranter.ItemGrantedEvent.Subscribe(OnItemGranted)

        GrantButton.InteractedWithEvent.Subscribe(OnGrantPressed)
        CycleButton.InteractedWithEvent.Subscribe(OnCyclePressed)
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnItemGranted(Agent : agent) : void =
        Print("Item granted to agent!")

    OnGrantPressed(Agent : agent) : void =
        ItemGranter.GrantItem(Agent)
        Print("Item granted to agent via button!")

    OnCyclePressed(Agent : agent) : void =
        ItemGranter.CycleToNextItem(Agent)
        Print("Cycled to next item for agent!")

    OnEnablePressed(Agent : agent) : void =
        ItemGranter.Enable()
        Print("Item granter enabled!")

    OnDisablePressed(Agent : agent) : void =
        ItemGranter.Disable()
        Print("Item granter disabled!")
```

### How to Use in UEFN
1. **Add Items to the Device**
   - Select `item_granter_device` in the world.
   - Go to Creative inventory > Equip desired items.
   - Drop (Z/X/drag) items onto the device.
   - Each registered item shows as a floating hologram.

2. **Create Your Verse Device**
   - Right-click a folder in Verse Explorer → Create New Verse File.
   - Paste the example code.
   - Build with `Ctrl+Shift+B`.

3. **Place Devices in Your Level**
   - Drag the Verse device into the world.
   - Place `item_granter_device` and four `button_device`s.

4. **Assign @editable References**
   - In the Details panel, link devices:
     - `ItemGranter` → your `item_granter_device`
     - `GrantButton`, `CycleButton`, etc. → respective buttons

5. **Configure Item Granter Settings**
   - Adjust grant rules, equip settings, team/class limits, drop mode, etc.

6. **Test in Session**
   - Test item grants and event responses in gameplay.

### 🧠 Best Practices
- Register items before play.
- Use `.GrantItem()` and `.RestockItems()` for game logic.
- Enable "Grant on Cycle" for reward mechanics.
- Use "Grant Condition" = Only If Empty / Not Owned for single delivery.

### ❌ Common Issues & Fixes
| Issue                          | ❌ Example                      | ✅ Correct Example                  | Explanation                                   |
|--------------------------------|-----------------------------------|----------------------------------------|-----------------------------------------------|
| Item does not grant            | Did not register item             | Drop each desired item onto device     | Items must be registered manually             |
| Receiving wrong/multiple grants | Incorrect Grant Condition settings | Use accurate Grant/Condition settings  | Match grant logic to use case                 |
| Custom logic never runs        | Event not subscribed              | Subscribe with `ItemGrantedEvent.Subscribe()` | Hook the event in Verse code              |
| Blank device references        | @editable fields not assigned     | Assign all refs in Details panel       | Required for proper device interaction        |

### Notes
- Combine with minigames, puzzles, or eliminations.
- Use in team or individual setups.
- Spawning logic allows both dropped and inventory placement.
- Great for random chests, mission rewards, or one-time kits.

