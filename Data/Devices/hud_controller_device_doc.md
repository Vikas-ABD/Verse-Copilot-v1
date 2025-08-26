📘 **hud_controller_device – UEFN Verse Device Documentation**

🔹 **Description**
The `hud_controller_device` is used to show or hide parts of the player's HUD (heads-up display) for individual players, teams, or the entire game. This device lets you control HUD elements such as the minimap, elimination counter, health/shields, player count, round timer, team info, inventory, and more. You can use it to hide the entire HUD, disable only certain elements, or customize what information is visible during gameplay phases or events. Combine it with devices like `hud_message_device`, `map_indicator_device`, and `billboard_device` to optimize how and when information appears to players.

🧱 **Verse Using Statement**
```verse
verse
using { /Fortnite.com/Devices }
```

🔗 **Inheritance Hierarchy**
* `creative_object` – Base class for creative devices and props.
* `creative_device_base` – Base class for creative_device.
* `hud_controller_device`

🧩 **Data Members (Events)**
* No public data members; all configuration is via methods and the Details panel in UEFN.

🛠️ **Functions & Methods**
| Name                     | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| Enable()                | Enables this device and applies its HUD settings to the targeted players.   |
| Disable()               | Disables this device, restoring prior HUD settings.                         |
| GetTransform()          | Returns transform (position/rotation/scale) of the device.                   |
| MoveTo(...)             | Moves the device to a specified position/rotation over time.                |
| TeleportTo(...)         | Instantly teleports device to specified position/rotation or transform.     |
| ResetAffectedClass()    | Resets the Affected Class option to its starting value.                     |
| ResetAffectedTeam()     | Resets the Affected Team option to its starting value.                      |
| UpdateAffectedClass()   | Applies the class of an agent as the affected class for this device.        |
| UpdateAffectedTeam()    | Applies the team of an agent as the affected team for this device.          |

🎛 **Configuration Options (Details Panel)**
- Show HUD: Do Not Override, Yes, No
- Show Minimap
- Show HUD Info Box
- Show Storm Timer
- Show Player Count
- Show Elimination Counter
- Show Round Timer/Details
- Show Build Menu
- Show Player Inventory
- Show Team Info
- Show Damage Numbers
- Show Health/Health Numbers
- Show Shields/Shield Numbers
- Show Battle Pass UI: Show All, Level Only, Experience Bar Only, Don’t Display
- Affected Team/Class
- Priority

🧰 **Usage Example**
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# Example device showing how to use hud_controller_device
hud_controller_example := class(creative_device):

    @editable
    HUDController : hud_controller_device = hud_controller_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnEnablePressed(Agent : agent) : void =
        HUDController.Enable()
        Print("HUD controller enabled!")

    OnDisablePressed(Agent : agent) : void =
        HUDController.Disable()
        Print("HUD controller disabled!")
```

**How it works:**
- Place a `hud_controller_device` in your level and configure HUD elements in the Details panel.
- Use Verse or device connections to enable/disable settings during events like missions, eliminations, etc.
- Use `Enable()` and `Disable()` methods with button or trigger events.

🧠 **Best Practices**
- Set elements to "Do Not Override" unless enforcing a change.
- Use `Priority` for tie-breaking between multiple devices.
- Combine with other UI-related devices for customized experience.
- Use Affected Team/Class for asymmetric game modes.
- Always playtest HUD setups in a live session.

🔗 **HUD Priority & Override Hierarchy**
1. **User Settings** – Players can always hide elements, cannot force-show hidden ones.
2. **Team Settings & Inventory Device**
3. **HUD Controller Device** *(this device)*
4. **Island Settings** – Lowest priority.

❌ **Incorrect Usage Examples and Fixes**
| Issue                                | ❌ Wrong                        | ✅ Correct                              | Explanation                                                                 |
|-------------------------------------|--------------------------------|----------------------------------------|-----------------------------------------------------------------------------|
| Only configuring, not enabling      | Device in level only           | Call `.Enable()` or enable via event   | Must be enabled to apply HUD settings                                      |
| Relying on lower priority           | Conflicting devices w/ low Prio| Set highest priority                   | Highest-priority device takes control                                       |
| Not resetting Affected Team/Class   | Lingering HUD changes          | Use `.ResetAffectedTeam()`/`.ResetAffectedClass()` | Clean up after gameplay changes                                              |
| Expecting player to restore hidden  | Depends on UI settings         | Use HUD device/island config to manage | Hidden elements can't be turned on by user UI if device overrides it       |

**Note:**
- Only the highest-priority HUD controller for a player/team applies at a time.
- Ideal for competitive, story-driven, or minimalist UI scenarios.

