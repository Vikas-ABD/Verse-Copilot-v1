# UEFN Verse Device Documentation: `capture_item_spawner_device`

## 📙 Description
The `capture_item_spawner_device` is designed to spawn and manage a **single objective item** (e.g., a flag or diamond) in your Fortnite experience. It is ideal for **objective-based games** such as *Capture the Flag*, where only one instance of the item should be active at a time.

The device enables configuration of:
- Pickup/capture rules based on teams
- Drop and return behaviors
- Score awarding on capture
- Event-driven interactions via Verse

---

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

---

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `base_item_spawner_device`
- `capture_item_spawner_device`

---

## 🧹 Data Members (Events)
| Name | Type | Description |
|------|------|-------------|
| `ItemPickedUpEvent` | `listenable(agent)` | Triggered when the item is picked up. |
| `ItemDroppedEvent` | `listenable(agent)` | Triggered when the item is dropped. |
| `ItemCapturedEvent` | `listenable(agent)` | Triggered when the item is captured. |
| `ItemReturnedEvent` | `listenable(agent)` | Triggered when a dropped item returns to the spawner. |

---

## 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| `Enable()` | Activates the spawner and allows item interaction. |
| `Disable()` | Disables the spawner and despawns the item. |
| `GetTransform()` | Retrieves the device's position, rotation, and scale. |
| `MoveTo()` / `TeleportTo()` | Moves or teleports the spawner to a new location. |

---

## 🎛 Configuration Options (Details Panel)
- **Item Definition**: The item to spawn (e.g., Flag, Diamond).
- **Friendly Team**: The team that owns the objective.
- **Captured By**: Specifies which team can capture/pick up the item.
- **Return Dropped Items**: Options include instant, delayed, or never.
- **Score Value**: Points awarded for capturing the item.
- **Accent Color/Type**: Set the visual color of the item.
- **Show Capture Messages**: Toggle display of event messages.
- **Play Capture Sounds**: Toggle event SFX.
- **Enabled At Game Start**: Initial device state.
- **Ammo Settings**: Ammo configuration if a weapon is used as the item.

---

## 🪠 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

capture_item_example := class(creative_device):

    @editable
    CaptureItem : capture_item_spawner_device = capture_item_spawner_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to capture item events
        CaptureItem.ItemPickedUpEvent.Subscribe(OnItemPickedUp)
        CaptureItem.ItemDroppedEvent.Subscribe(OnItemDropped)
        CaptureItem.ItemCapturedEvent.Subscribe(OnItemCaptured)

        # Subscribe to control buttons
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    # Event handlers
    OnItemPickedUp(Agent : agent) : void =
        Print("Item picked up by agent!")

    OnItemDropped(Agent : agent) : void =
        Print("Item dropped by agent!")

    OnItemCaptured(Agent : agent) : void =
        Print("Item captured by agent!")

    # Button control handlers
    OnEnablePressed(Agent : agent) : void =
        CaptureItem.Enable()
        Print("Capture item enabled!")

    OnDisablePressed(Agent : agent) : void =
        CaptureItem.Disable()
        Print("Capture item disabled!")
```

---

## 💪 How It Works in UEFN
1. **Place Devices in Level**:
   - Add a `capture_item_spawner_device` in the desired location.
   - Optionally, add `button_device`s for manual control.

2. **Configure the Device (Details Panel)**:
   - Choose the item (e.g., Flag).
   - Set team pickup/capture logic.
   - Adjust return rules, score value, color, etc.

3. **Create & Build Verse Script**:
   - In Verse Explorer, create a new Verse file (e.g., `capture_item_example.verse`).
   - Paste the code and save.
   - Build the script via *Verse > Build Verse Code* or `CTRL+SHIFT+B`.

4. **Place & Reference the Verse Device**:
   - Drag the custom Verse device into the level.
   - Link editable fields in the Details panel:
     - `CaptureItem` → your placed `capture_item_spawner_device`
     - `EnableButton` / `DisableButton` → corresponding buttons

5. **Test Gameplay**:
   - Enter play mode and verify interactions.
   - Watch for event-driven logs and confirm behaviors.

---

## 🧠 Best Practices
- Pair with `capture_area_device` for full capture logic.
- Use events to reward players, transition rounds, or activate systems.
- Use `Return Dropped Items` settings to simulate classic or custom drop behaviors.
- Call `Disable()` to despawn items instantly via Verse or wiring.

---

## ❌ Common Issues & Fixes
| Issue | ❌ Wrong | ✅ Correct | Explanation |
|-------|------------|--------------|-------------|
| Events not working | Checked item visually | `.Subscribe()` to events | Required for Verse event logic |
| Incomplete config | Default/blank settings | Fully configure in Details panel | Ensures proper gameplay logic |
| Multiple item conflicts | Placed multiple spawners | One device per item | Only one active item per device |
| Item never appears | Forgot `Enable()` call | Enable via Verse or panel | Device must be active |
| Verse errors | Blank `@editable` fields | Assign references | Essential for Verse runtime |

---

## 📅 Use Case
This device is ideal for:
- **Capture the Flag**
- **Heist Missions**
- **Single-Item Retrieval Modes**

Combined with other Verse logic and devices, it provides a powerful foundation for event-driven, objective-based gameplay in UEFN.

---

*End of Documentation*

