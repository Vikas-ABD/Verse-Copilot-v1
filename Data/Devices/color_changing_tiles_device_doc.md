## color_changing_tiles_device – UEFN Verse Device Documentation

### 🔹 Description
The `color_changing_tiles_device` allows creators to place interactive tiles in Fortnite that change color when stepped on or driven over by agents (players or vehicles). Each tile changes to reflect the team color of the interacting agent. The tile can be programmatically enabled, disabled, reset, shown, or hidden during runtime, with extensive configuration options for team-based gameplay, scoring, and HUD messaging.

---

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `color_changing_tiles_device`

---

### 🧩 Data Members (Events)
| Name            | Type             | Description                                      |
|-----------------|------------------|--------------------------------------------------|
| ActivatedEvent  | listenable(agent)| Triggers when a player or vehicle changes tile color |

---

### 🛠️ Functions & Methods
| Name             | Description                                                    |
|------------------|----------------------------------------------------------------|
| `Enable()`       | Activates the tile so it responds to interactions              |
| `Disable()`      | Deactivates the tile so it ignores interactions                |
| `Reset()`        | Resets the tile to its neutral starting state                 |
| `SetTeam(agent)` | Changes the tile to reflect a specific agent's team color      |
| `Show()` / `Hide()` | Makes the tile visible or hidden in the world                |
| `GetTransform()` | Retrieves tile's position, rotation, and scale                 |
| `MoveTo()` / `TeleportTo()` | Moves or teleports the tile to a new position         |

---

### 🎛 Configuration Options (Details Panel)
| Option                        | Description                                                      |
|-------------------------------|------------------------------------------------------------------|
| Enabled At Game Start         | Determines if the tile is active when game starts               |
| Starting Team                 | Sets the initial team color (or neutral)                        |
| Revert Tile                   | If on, tile reverts to neutral after a set duration             |
| Time Until Reverting          | Time before tile reverts (used with Revert Tile)               |
| Score / Steal Score           | Points added/lost when tile is captured                        |
| Appearance                    | Tile visuals: concrete, disco, icons, etc.                     |
| Visible During Game           | Whether tile is visible during gameplay                        |
| Collision During Game         | Sets tile collision behavior during play                       |
| Display Score Update on HUD   | Show HUD message on capture/change                             |
| HUD Message/Text/Colors       | Customize HUD score messaging                                  |

Note: All configurations are editable in the Details panel in UEFN.

---

### 🧰 Verse Example Usage
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

color_changing_tiles_example := class(creative_device):

    @editable
    ColorTiles : color_changing_tiles_device = color_changing_tiles_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    ResetButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        ResetButton.InteractedWithEvent.Subscribe(OnResetPressed)

    OnEnablePressed(Agent : agent) : void =
        ColorTiles.Enable()
        Print("Color changing tiles enabled!")

    OnDisablePressed(Agent : agent) : void =
        ColorTiles.Disable()
        Print("Color changing tiles disabled!")

    OnResetPressed(Agent : agent) : void =
        ColorTiles.Reset()
        Print("Color changing tiles reset!")
```

---

### 🧪 How It Works
- Control tile state (enable, disable, reset) using 3 button devices.
- OnBegin() subscribes to button events and triggers tile actions.
- Tile changes to interacting agent's team color when activated.
- You can also subscribe to `ColorTiles.ActivatedEvent.Subscribe(...)` to run custom logic.

---

### ⚙️ Setup and Usage in UEFN
1. **Place Devices in Level**
   - Add `color_changing_tiles_device` to your level.
   - Add 3 `button_device` instances to control enable/disable/reset.

2. **Configure Device in Details Panel**
   - Set options like starting team, revert time, shape, score, appearance, etc.

3. **Create & Build Verse Script**
   - In Verse Explorer: Create new Verse file (e.g., `color_changing_tiles_example.verse`).
   - Paste and save the sample code.
   - Build with **Verse → Build Verse Code** (Ctrl+Shift+B).

4. **Reference Devices in Verse**
   - In the Details panel of your Verse device, assign:
     - `ColorTiles` → your tile device
     - `EnableButton`, `DisableButton`, `ResetButton` → your placed buttons

5. **Test Gameplay**
   - Use the buttons during gameplay to control tile behavior.
   - Step or drive over the tile to observe color change.

---

### 🧠 Best Practices
- Use `.ActivatedEvent.Subscribe(...)` to implement score, UI, or audio logic.
- Configure score/revert timing for control-point or territory games.
- Combine multiple tiles for floor puzzles or area ownership mechanics.
- Use `.Show()` and `.Hide()` to create secret or puzzle mechanics.

---

### ❌ Common Issues & Fixes
| Issue                             | ❌ Wrong Example                     | ✅ Correct Example                                | Explanation                                               |
|----------------------------------|--------------------------------------|--------------------------------------------------|-----------------------------------------------------------|
| No custom event callback         | Not subscribing to ActivatedEvent    | `.ActivatedEvent.Subscribe(OnActivatedHandler)`  | Required to run logic when tile is triggered             |
| Tile inactive during gameplay    | Calls tile methods, no effect        | Use `.Enable()` or start enabled                 | Tile must be enabled to respond to interactions          |
| Verse errors from blank editables| No devices referenced                | Always assign device references in the editor    | Device links must be made in Details panel               |
| Force team color change needed   | Only relies on player interaction    | Use `.SetTeam(agent)`                            | Set color directly without needing interaction           |

---

### 📌 Notes
- Use `SetTeam(agent)` to manually assign tile team color (e.g., for rewards).
- Ideal for building team-control, zone-capture, or progressive games.
- Supports customization for HUD feedback, visual effects, and point systems.

