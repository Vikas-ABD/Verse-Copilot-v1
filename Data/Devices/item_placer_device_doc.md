# item_placer_device – UEFN Verse Device Documentation

## 📙 Description
The `item_placer_device` lets you place a pickup item or weapon directly in your Fortnite island, appearing naturally in the world rather than dropping from the sky or a chest. The device acts as a container: when a player interacts with the visual item, it grants that registered item to the player. If the item placer is destroyed (e.g., mounted on a destructible object), the item will drop to the ground.

Use this device for:
- Precise item placement
- Realism
- Custom spawn behavior
- Static loot locations

## 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
  - Base class for creative devices and props.
- `creative_device_base`
  - Base class for `creative_device`.
- `item_placer_device`

## 🧩 Core Methods
| Function Name | Signature / Description |
|---------------|--------------------------|
| `Enable()` | Enables this device—allows pickups to be seen and collected/interacted with. |
| `Disable()` | Disables this device—pickup cannot be collected. |
| `GetTransform()` | Returns current transform (position, rotation, scale) of the device. |
| `MoveTo()` | Moves the device to a specified position/rotation over a period. |
| `TeleportTo()` | Instantly moves device to a specified position/rotation/transform. |

## 🎛 Configuration Options (Details Panel)
| Option | Values | Description |
|--------|--------|-------------|
| Allow Interact | On, Off | Can the player interact/pick up this item? |
| Interact Text | "Pick Up {item}", custom text | Text shown to player looking at this item. Supports 150-char custom message. |
| Interact Time | Instant, time (seconds) | Time to hold interact before receiving item. |
| Allowed Team | None, Any, Pick team | Restricts which team(s) can collect. |
| Invert Team Selection | Off, On | All teams except selected may collect. |
| Allowed Class | No Class, Any, Pick class | Restricts which class(es) can interact. |
| Invert Class Selection | Off, On | All classes except selected may collect. |
| Show Rarity Effects | On, Off | Display rarity visuals on item. |
| Play Audio | On, Off | Play sound when item is enabled/interacted. |
| Enabled at Game Start | Enabled, Disabled | Is the item placer enabled at match start? |
| Allow Respawn | Off, On | Can the item respawn once collected? |
| Can Be Damaged at Game Start | Yes, No | Allow device to be destroyed by damage? |
| Item Health | 1+ | If destroyable, how much HP does it have? |
| Allowed Class to Damage | No Class, Any, Pick class | Set which class(es) can damage/destroy placer. |

## 🧰 Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example: Controlling item placer device
item_placer_example := class(creative_device):

    @editable
    ItemPlacer : item_placer_device = item_placer_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnEnablePressed(Agent : agent) : void =
        ItemPlacer.Enable()
        Print("Item placer enabled")

    OnDisablePressed(Agent : agent) : void =
        ItemPlacer.Disable()
        Print("Item placer disabled")
```

**Explanation:**
- Place an `item_placer_device` in your level, and use the Details panel to register the item/weapon you want to appear.
- You can connect Verse code (above) to enable or disable the device via button triggers or custom game logic.
- When enabled, players who meet the team or class restrictions and interact with the visual item (after the interact time) will receive the registered item in their inventory.

## 🪰 Best Practices
- Always register the desired item in the item placer before playtesting—open Details, assign, and confirm.
- Use clear "Interact Text" for instructions, especially with unusual or custom items.
- For limited pickups, set Allow Respawn to Off; for recurring or campaign items, enable respawn.
- Combine with destructible props for hidden, trap, or reward loot setups.
- Use team/class restrictions for role-based gameplay or competitive balance.

## ❌ Incorrect Usage Examples and How to Fix
| Issue | ❌ Wrong Example | ✅ Correct Example | Explanation |
|-------|--------------------|------------------------|-------------|
| No `@editable` reference | Code uses device w/o assignment | Reference and assign in Details panel | Prevents null/error calls in Verse |
| Interact Time too long/short | Setting to 0 (no time) or 60s | Choose an intuitive hold time (0.5s–3s typical) | Better player experience |
| Not registering any item | Device unconfigured | Set item in Details panel before play/test | No item appears unless chosen |

**Note:**
- The item is visible as an in-world pickup; if destroyed, it drops; if collected, it despawns (and respawns, if allowed).
- Works for all standard Fortnite weapons and most consumables or key items supported in UEFN.
- Powerful for static loot, advanced level design, and special choreographed encounters.

