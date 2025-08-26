📘 map_controller_device – UEFN Verse Device Documentation

🔹 Description
The map_controller_device controls the behavior of the in-game map and minimap for agents (players). It allows you to automatically or programmatically activate special map/minimap settings for specific areas and scenarios. Activation can be triggered by:
* Automatic activation (set in Details panel)
* Agents entering or exiting its volume (using “Activate on Trigger”)
* Events from other devices or custom Verse scripting.

If multiple map controllers are active for an agent, the controller with the highest Map Priority in its Details panel overrides the rest.

🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

🔗 Inheritance Hierarchy
* creative_object
* creative_device_base
* map_controller_device

🧩 Data Members (Events)
This class has no direct data members—all map/minimap behavior is managed with functions and device options.

🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| Enable() | Enables the device; allows activation by triggers, events, or Verse. |
| Disable() | Disables the device, deactivating for all agents & blocking further activation (until re-enabled). |
| Activate(Agent:agent) | Adds this controller to that agent’s map controller stack, applying its settings. |
| Activate() | Adds this controller to all agents' map controller stacks. |
| Deactivate(Agent:agent) | Removes this controller from that agent’s stack (restores next-highest or default if none). |
| Deactivate() | Removes this controller from all agents’ stacks (restores next-highest or default if none). |
| SetCaptureBoxSize(Size:float) | Sets the width & length of the map image capture area and volume trigger (meters; clamp: 25–2500). |
| GetCaptureBoxSize() | Returns the current Capture Box Size (in meters). |
| GetTransform() | Returns world transform of the device (position/rotation/scale in cm). |
| MoveTo(...) / TeleportTo(...) | Standard creative_object movement methods. |

🎛 Configuration Options (Details Panel)
| Option | Description |
|--------|-------------|
| Activate Automatically | Enable to automatically activate for all players at game start. |
| Activate on Trigger | Activate for agents entering its volume. |
| Capture Box Size | Size (in meters) for map trigger & minimap capture (25–2500). |
| Map Priority | Integer value determining precedence when multiple map controllers are active. |
| Minimap Options | Show/hide region, customize minimap’s look, icons, pings, etc. |
| Enable at Game Start | Pre-enables the device for immediate use. |

🧰 Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

map_controller_example := class(creative_device):

    @editable
    MapController : map_controller_device = map_controller_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    @editable
    ActivateButton : button_device = button_device{}

    @editable
    DeactivateButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)
        ActivateButton.InteractedWithEvent.Subscribe(OnActivatePressed)
        DeactivateButton.InteractedWithEvent.Subscribe(OnDeactivatePressed)

        MapController.SetCaptureBoxSize(1000.0)
        CaptureBoxSize := MapController.GetCaptureBoxSize()
        Print("Capture box size: {CaptureBoxSize}")

    OnEnablePressed(Agent : agent) : void =
        MapController.Enable()
        Print("Map controller enabled!")

    OnDisablePressed(Agent : agent) : void =
        MapController.Disable()
        Print("Map controller disabled!")

    OnActivatePressed(Agent : agent) : void =
        MapController.Activate(Agent)
        Print("Map controller activated for agent!")

    OnDeactivatePressed(Agent : agent) : void =
        MapController.Deactivate(Agent)
        Print("Map controller deactivated for agent!")
```

✅ How it works:
* Place and configure one or more map_controller_device in your level.
* In the Details panel, set your desired area (Capture Box Size), visual settings, “Activate Automatically” or “Activate on Trigger”, and Map Priority.
* Connect with triggers or subscribe to events in Verse for advanced map swapping or dynamic UI logic.
* Manually control which agents are affected via `.Activate()` and `.Deactivate()`.
* For overlapping/multiple controllers, the device with the highest Map Priority applies for each agent.

🧠 Best Practices
* Use “Activate Automatically” for global changes; “Activate on Trigger” for region-based or event-triggered changes (e.g., entering a facility).
* Set unique Map Priority values if controllers may overlap; highest number wins for that agent.
* Use `.Activate(Agent)` and `.Deactivate(Agent)` in Verse for custom behaviors (e.g., quest progression, puzzles).
* Adjust Capture Box Size carefully so minimap coverage and volume triggers match your actual space.

❌ Incorrect Usage Examples and Fixes
| Issue | ❌ Wrong | ✅ Correct | Explanation |
|-------|---------|------------|-------------|
| Only calling `.Activate()` w/o `.Enable()` | Call `.Activate()` with device disabled | Call `.Enable()` before `.Activate()`, or set enabled in Details panel | Device must be enabled before activating |
| Overlapping controllers with same priority | Two devices at Map Priority 1 | Set unique Map Priority (higher wins) | Unique priority clarifies controller stacking |
| Adjusting Capture Box outside limits | Set size <25 or >2500 meters | Value between 25–2500 meters (clamped if out of range) | Device only supports values in this range |
| Not using right activation type | Expecting trigger or auto | Set “Activate on Trigger” or “Activate Automatically” as needed | Device only activates per selected option |

📝 Note:
* Only one controller affects minimap for each agent at a time (the highest-priority active one).
* Map controllers are ideal for custom minimap reveals, “fog of war”, area unlocking, and dynamic map UI.
* Use Verse to switch controllers for agents based on progression, puzzle solving, or event completion.

