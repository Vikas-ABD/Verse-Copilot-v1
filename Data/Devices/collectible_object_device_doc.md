## 📘 Collectible Object Device – UEFN Verse Device Documentation

### 🔹 Description
The `collectible_object_device` is used to place collectible items (such as coins, music notes, or custom models) directly in the world. When an agent collects this item, it can trigger scoring, item granting, win conditions, or custom Verse logic. The device has extensive settings for team/class restrictions, score handling, HUD display, and can be shown, hidden, respawned, or moved using Verse.

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- creative_object
- creative_device_base
- collectible_object_device

### 🧩 Data Members (Events)
| Name            | Type               | Description                              |
|-----------------|--------------------|------------------------------------------|
| CollectedEvent  | listenable(agent)  | Fires when the item is collected by an agent. |

### 🛠️ Functions & Methods
| Name             | Description                                                |
|------------------|------------------------------------------------------------|
| `Show()`         | Makes the collectible visible.                             |
| `Hide()`         | Hides the collectible from view.                           |
| `Respawn(agent)` | Respawns the object for the specified agent.               |
| `RespawnForAll()`| Respawns the object for all agents.                        |
| `MoveTo()`       | Moves the collectible to a new position, with animation.   |
| `TeleportTo()`   | Instantly moves the collectible.                           |
| `GetTransform()` | Gets current position, rotation, and scale.                |

### 🎛 Configuration Options (Details Panel)
- **Collecting Team**: Specify which team(s) can pick up the item.
- **Allowed Class**: Restrict pickup to certain class(es).
- **Visible to Opposing Players**: Hide from/show to teams that can't collect.
- **Visible on Game Start**: Starts visible or invisible.
- **Show Pickup Effects**: Play visual/audio effects on collect.
- **Display Score Update on HUD**: Show score on player HUD when item is collected.
- **HUD Message**: Custom text for HUD notification.
- **Reset HUD Message Score**: Start score notification at zero.
- **HUD Message Score/Color**: Value and color shown in HUD.
- **Collect Item to End / Score to End**: Set win/score conditions through item collection.
> *(Set all configuration using Details panel in UEFN.)*

### 🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use collectible_object_device
collectible_object_example := class(creative_device):

    @editable
    Collectible : collectible_object_device = collectible_object_device{}

    @editable
    ShowButton : button_device = button_device{}

    @editable
    HideButton : button_device = button_device{}

    @editable
    RespawnButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to collectible events
        Collectible.CollectedEvent.Subscribe(OnCollected)

        # Subscribe to control buttons
        ShowButton.InteractedWithEvent.Subscribe(OnShowPressed)
        HideButton.InteractedWithEvent.Subscribe(OnHidePressed)
        RespawnButton.InteractedWithEvent.Subscribe(OnRespawnPressed)

    # Event handler for collectible pickup
    OnCollected(Agent : agent) : void =
        Print("Collectible picked up by agent!")

    # Button control handlers
    OnShowPressed(Agent : agent) : void =
        Collectible.Show()
        Print("Collectible shown!")

    OnHidePressed(Agent : agent) : void =
        Collectible.Hide()
        Print("Collectible hidden!")

    OnRespawnPressed(Agent : agent) : void =
        Collectible.Respawn(Agent)
        Print("Collectible respawned!")
```

### 🗺 How it Works in UEFN
1. **Place Devices in Level**:
   - Add a `collectible_object_device` where you want a collectible item to appear.
   - Add any `button_device`s if you want to show/hide/respawn collectibles dynamically.
2. **Configure Options (Details Panel)**:
   - Choose collectible type/model.
   - Set team/class restrictions, HUD behavior, score value, win conditions, and visual/audio effects.
3. **Create & Build Verse Script**:
   - In Verse Explorer: right-click a folder, select *Create New Verse File* (e.g., `collectible_object_example.verse`), and paste the example.
   - In UEFN, click *Verse → Build Verse Code* (or Ctrl+Shift+B) until “Build Succeeded”.
4. **Place Verse Device, Assign References**:
   - Add your Verse device to the world.
   - Assign `@editable` properties:
     - `Collectible` → your `collectible_object_device`
     - `ShowButton`, `HideButton`, `RespawnButton` → your button devices as desired.
5. **Test Gameplay**:
   - Launch a session. Collect the item to test pickup events, click buttons to show/hide/respawn as needed, and observe log messages.

### 🧠 Best Practices
- Use multiple `collectible_object_device`s for collection quests, puzzles, and currency.
- Set "Collect Item to End" or "Score to End" in *My Island → Game* for win condition-based gameplay.
- Use `.CollectedEvent.Subscribe(...)` to trigger custom rewards, effects, or logic.
- For centralized HUD/scoring, integrate with `item_granter`, `score_manager`, or `win_condition_device`.

### ❌ Common Issues & Fixes
| Issue                            | ❌ Wrong Example                        | ✅ Correct Example                             | Explanation                          |
|----------------------------------|----------------------------------------|-----------------------------------------------|--------------------------------------|
| Subscribing to nonexistent events| Looked for item pickup event not on device | Use `.CollectedEvent.Subscribe(handler)`   | Use only provided device events     |
| Device not spawning/hidden      | Only placed, no Verse call or option enabled | Use `.Show()` or enable visible at start   | Option or code required              |
| Respawn for all agents not working | Used `.Respawn()` for everyone       | Use `.RespawnForAll()`                      | Method difference                    |
| Configuration not matching design | Did not set team/class/HUD options   | Use Details panel for all config             | Settings not dynamic in Verse       |
| Not referencing device in Verse | Left `@editable` fields blank         | Assign all devices as `@editable` properties | Needed for Verse to function        |

### 🔎 Notes
- Optimized for single-pickup "collect and score" logic.
- Use multiple instances or pair with item granting devices for advanced objectives.
- Use `Show`, `Hide`, `Respawn`, and `CollectedEvent` for interactive gameplay.

