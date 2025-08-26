📘 dance_mannequin_device – UEFN Verse Device Documentation

🔹 Description
The dance_mannequin_device projects a hologram of a Fortnite character performing dance emotes. You can configure character skin presets, emotes, colors, and effects, and dynamically switch skins/emotes or activate "skin capture" to copy a player's outfit. This device is ideal for stages, dance clubs, minigames, or event-driven visual effects.

🧱 Verse Using Statement
verse
using { /Fortnite.com/Devices }

🔗 Inheritance Hierarchy
* creative_object
* creative_device_base
* dance_mannequin_device

🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| Enable() | Enables the mannequin (makes hologram appear and animate). |
| Disable() | Disables the mannequin (hides the hologram). |
| ActivateDefaultPreset() | Switch mannequin to default (Preset 1: skin/emote/color as set in options). |
| ActivatePreset2() | Switch mannequin to Preset 2. |
| ActivatePreset3() | Switch mannequin to Preset 3. |
| ActivateSkinAndEmoteCapture(Agent) | Set mannequin to match the agent’s skin and emote. |
| DeactivateSkinAndEmoteCapture() | Return mannequin to normal preset-based appearance. |
| GetTransform() | World transform (location/rotation/scale) of mannequin. |
| MoveTo(...), TeleportTo(...) | Move or teleport mannequin to a new location/rotation. |

🎛 Configuration Options (Details Panel)
| Option | Description |
|--------|-------------|
| Character Skin Default/2/3 | Pick up to three skins or "Custom Character Cosmetics". |
| Dance Emote Default/2/3 | Set up to three emote presets. |
| Hue Default/2/3 | Set base color. |
| Show Pedestal | On/Off—display hologram base. |
| Show Stagelight | On/Off—display lights on hologram. |
| Strobe | Enable strobe lighting effect. |
| Pedestal Color | Light Steel, Dark Steel, etc. |
| Hue Override | Party Mode/Silhouette/Off (color effects). |
| Enabled During Phase | Choose phases where mannequin is visible. |

🧩 Events
*Does not natively emit Verse events; state changes are driven by methods and channel events.*

🧰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

dance_mannequin_example := class(creative_device):

    @editable
    DanceMannequin : dance_mannequin_device = dance_mannequin_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        # Subscribe to control buttons
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    # Button control handlers
    OnEnablePressed(Agent : agent) : void =
        DanceMannequin.Enable()
        Print("Dance mannequin enabled!")

    OnDisablePressed(Agent : agent) : void =
        DanceMannequin.Disable()
        Print("Dance mannequin disabled!")
```

📋 How it Works in UEFN:
1. **Place Devices in Level**:
   - Add a `dance_mannequin_device` for each hologram you want.
   - Add `button_devices` if you want players to enable/disable or switch the mannequin with interaction.
2. **Configure Details Panel**:
   - Choose up to three skin presets and up to three emotes.
   - Set pedestal/options, hue, strobe, and phase activation as desired.
   - Optionally configure channel events for switching presets using creative wiring.
3. **Create and Build Verse Script**:
   - Open Verse Explorer, add a new Verse file (e.g., `dance_mannequin_example.verse`).
   - Paste the code above.
   - Save and build Verse (Verse → Build Verse Code or Ctrl+Shift+B).
4. **Place and Reference Devices**:
   - Drag your Verse device from Content Browser into the world.
   - Assign its `DanceMannequin`, `EnableButton`, and `DisableButton` references in Details.
5. **Test**:
   - Launch a session. Interact with buttons to enable/disable the mannequin and see log output as emotes/skins are changed.

🧠 Best Practices
* Use up to three emote/skin presets and switch via Verse or device channels for dynamic shows.
* For live “skin capture”, use `ActivateSkinAndEmoteCapture(Agent)` in Verse or event binding to copy a player’s appearance.
* Use `Enable()`/`Disable()` to control mannequin timing during music or event sequences.
* Stack with VFX, lights, sequencers, or audience (crowd volume) for a complete stage effect.

❌ Common Mistakes & Fixes
| Issue | ❌ Wrong Usage | ✅ Correct Usage | Explanation |
|-------|----------------|------------------|-------------|
| Mannequin doesn’t show | Device disabled, wrong phase | Set correct Enabled During Phase | Device must be enabled/active |
| Skins/emotes don’t change | Didn’t use presets/channels | Use methods/channel triggers | Use correct preset switching |
| Not copying player | Didn’t call skin capture | Use `ActivateSkinAndEmoteCapture(Agent)` | For live copying player looks |

Note:
* For advanced choreography, combine multiple mannequins, sequencer devices, creative wiring, and Verse logic.
* Cannot upload arbitrary custom skins; only choices available via device's Details panel.

