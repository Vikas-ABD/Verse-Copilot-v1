📘 **fishing_zone_device – UEFN Verse Device Documentation**

---

🔹 **Description**

The `fishing_zone_device` enables fishing mechanics in your Fortnite experience. Use it for fishing competitions, collection objectives, or custom minigames featuring fishing as the core activity. This device creates a fishing zone that players can interact with using fishing rods and supports both Battle Royale loot pools and custom loot tables (by dropping items on the device). Advanced game logic can be added by handling fishing events in Verse.

---

🧱 **Verse Using Statement**
```verse
using { /Fortnite.com/Devices }
```

---

🔗 **Inheritance Hierarchy**
- creative_object
- creative_device_base
- fishing_zone_device

---

🧩 **Data Members (Events)**
| Name         | Type               | Description                                        |
|--------------|--------------------|----------------------------------------------------|
| CaughtEvent  | listenable(agent)  | Fires when a player (agent) catches a fish.       |
| EmptyEvent   | listenable(agent)  | Fires when all items are caught and the zone is empty. |

---

🛠️ **Functions & Methods**
| Name         | Description                                                   |
|--------------|---------------------------------------------------------------|
| Enable()     | Enables the fishing zone, allowing fishing.                  |
| Disable()    | Disables the device; zone becomes inactive for fishing.      |
| Reset()      | Resets available uses to the configured "Uses Allowed".      |
| Restock()    | Restocks inventory (only with Pool Type = Device Inventory). |
| GetTransform() | Returns device’s location/rotation/scale.                   |
| MoveTo(...)  | Move zone to new location/rotation over time (animated).     |
| TeleportTo(...) | Instantly move zone to new transform.                     |

---

🎛 **Configuration Options (Details Panel)**
- **Usage Type**: Infinite, Battle Royale, Limited.
- **Pool Type**: Battle Royale, Device Inventory, Trigger Only, Fish Only.
- **Number of Uses**: Set uses if Usage Type is Limited.
- **Disable When Empty**: Turns off zone if pool emptied.
- **Remove Caught Items**: Items are removed when caught.
- **Zone FX & Ripple FX**: Toggle water and ripple effects.
- **Extra Ammo**: Adds ammo if a weapon is caught.
- **Offset to Water**: Auto-aligns to nearby water devices.

---

🧰 **Verse Usage Example**
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

fishing_zone_example := class(creative_device):

    @editable
    FishingZone : fishing_zone_device = fishing_zone_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    ResetButton : button_device = button_device{}

    @editable
    RestockButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        FishingZone.CaughtEvent.Subscribe(OnFishCaught)
        FishingZone.EmptyEvent.Subscribe(OnZoneEmpty)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        ResetButton.InteractedWithEvent.Subscribe(OnResetPressed)
        RestockButton.InteractedWithEvent.Subscribe(OnRestockPressed)

    OnFishCaught(Agent : agent) : void =
        Print("Fish caught by player!")

    OnZoneEmpty(Agent : agent) : void =
        Print("Fishing zone is empty!")

    OnEnablePressed(Agent : agent) : void =
        FishingZone.Enable()
        Print("Fishing zone enabled!")

    OnDisablePressed(Agent : agent) : void =
        FishingZone.Disable()
        Print("Fishing zone disabled!")

    OnResetPressed(Agent : agent) : void =
        FishingZone.Reset()
        Print("Fishing zone reset!")

    OnRestockPressed(Agent : agent) : void =
        FishingZone.Restock()
        Print("Fishing zone restocked!")
```

---

🔧 **How it Works in UEFN**

1. **Place Devices in Level**:
   - Add a `fishing_zone_device` in water/lava.
   - Add optional `button_device`s to control the zone.

2. **Configure in Details Panel**:
   - Set usage type, pool type, loot, uses, depletion behavior.
   - Drop loot items on the device for custom pools.

3. **Create & Build Verse Script**:
   - Add a new `.verse` file.
   - Paste the above script.
   - Build via CTRL + SHIFT + B.

4. **Assign Device References**:
   - Assign the `FishingZone` and button references in Details.

5. **Test & Refine**:
   - Use a Fishing Rod to test.
   - Observe events and debug prints.

---

🧠 **Best Practices**
- Use Device Inventory for custom rewards.
- Reset at round start, restock between rounds.
- Enable/Disable based on game phase or triggers.
- Bind to Caught/Empty events for XP, prizes, or tracking.
- Use creative placement—water, lava, or props.

---

❌ **Common Mistakes & Fixes**
| Issue | ❌ Wrong Usage | ✅ Correct Usage | Explanation |
|-------|---------------|------------------|-------------|
| No loot when Device Inventory is set | Didn’t drop items | Drop fish/items on device | Must manually add loot |
| Restock called on wrong Pool Type | Using Battle Royale pool | Use only with Device Inventory | Only applicable for device-managed loot |
| Fishing not working | Never enabled device | Call `.Enable()` | Device must be active |
| Logic not triggering | Didn’t subscribe to events | Use `.Subscribe(...)` | Events must be handled |

---

💡 **Additional Notes**
- Multiple devices can support large maps or custom games.
- Combine with boat spawners, item granters, water devices.
- Use Verse or events for competitions, prizes, or tracking rounds.

