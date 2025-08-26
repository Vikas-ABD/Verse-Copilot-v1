📘 **crowd_volume_device – UEFN Verse Device Documentation**

🔹 **Description**
The `crowd_volume_device` spawns a group of crowd NPCs for scenes such as races, concerts, or events—anywhere you'd like a cheering audience without placing individual characters. It helps performance, supports randomization, and allows you to control crowd density, area, and appearance through Details panel options and Verse scripting. The crowd will animate (cheer/idle) automatically.

🧱 **Verse Using Statement**
```verse
using { /Fortnite.com/Devices }
```

🔗 **Inheritance Hierarchy**
- creative_object
- creative_device_base
- crowd_volume_device

🧩 **Data Members (Events)**
- This class does not expose events in Verse. All runtime changes are done via methods or direct event binding in UEFN.

🛠️ **Functions & Methods**
| Name          | Description                                 |
|---------------|---------------------------------------------|
| Enable()      | Spawns/enables the crowd.                   |
| Disable()     | Removes/disables the crowd.                 |
| GetTransform()| Returns world transform of the device.      |
| MoveTo(...)   | Move device to position/rotation over time. |
| TeleportTo(...)| Instantly set to a new transform.         |

🎛 **Configuration Options (Details Panel)**
- Character Angle Randomness: Randomizes direction each NPC faces (0-100%).
- Character Scale Randomness: Randomizes NPC scaling for variety (0-100%).
- Crowd Density: Percent of volume filled with crowd (default: 100%).
- Character Alignment: How strictly NPCs are on grid (0-100%).
- Zone Width/Depth/Height: Size of the crowd area (in tiles, adjustable).
- Enabled During Phase: When the device auto-enables (Always, Pre-Game Only, Gameplay Only, or None).
- *(plus all standard device transform/visibility controls)*

🧰 **Usage Example in Verse**
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

crowd_volume_example := class(creative_device):

    @editable
    CrowdVolume : crowd_volume_device = crowd_volume_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnEnablePressed(Agent : agent) : void =
        CrowdVolume.Enable()
        Print("Crowd volume enabled!")

    OnDisablePressed(Agent : agent) : void =
        CrowdVolume.Disable()
        Print("Crowd volume disabled!")
```

**How it works:**
1. **Place Devices in Level:**
   - Add a `crowd_volume_device` to your level; place more for additional crowd clusters.
2. **Configure in Details Panel:**
   - Set area (Zone Width/Depth/Height), density, grid alignment, angle/scale randomness, and enabled phase as needed.
3. **Create the Verse Script:**
   - Add a new Verse file (e.g., `crowd_volume_example.verse`), paste the code above, and save.
   - Build Verse (Ctrl+Shift+B).
4. **Place and Assign Devices:**
   - From Content Browser, drag `crowd_volume_example` into your level.
   - Assign the `CrowdVolume` reference to your placed crowd device. Assign `EnableButton`/`DisableButton` if using manual controls.
5. **Test & Adjust:**
   - Launch a session, press buttons to enable/disable the crowd, and experiment with Details panel settings for best visual results.

🧠 **Best Practices**
- Use “Enable During Phase” for automatic control, or call `.Enable()`/`.Disable()` from Verse at specific game moments.
- Tweak density and alignment for full stands vs. sparse crowds.
- Use randomness options to avoid “cloned” look.
- Crowd volumes are visual only: use emotes, sounds, and VFX for added immersion.

❌ **Common Mistakes & Fixes**
| Issue                     | ❌ Wrong Usage                      | ✅ Correct Usage                       | Explanation                                  |
|--------------------------|------------------------------------|----------------------------------------|----------------------------------------------|
| Not enabling device      | Device remains invisible           | Set “Enabled During Phase” or call .Enable() | Crowd is only visible when enabled          |
| All crowd facing same way| Angle randomness at 0%             | Increase Character Angle Randomness    | Makes crowd look more natural               |
| Overlapping crowd areas  | Too many volumes, overlap          | Space out crowds, lower density        | Avoids performance drop and visual clutter  |
| Expecting crowd to interact| Assumes crowd is real agents     | Used for visual effect/animation only  | Crowd NPCs do not react or interact         |

**Note:**
- The device does not support event subscriptions for individual NPCs.
- Control when the crowd appears/disappears using `.Enable()`/`.Disable()`—ideal for “audience cue” moments or finishing races.
- For even more immersion, add cheering SFX with VFX or device channels.

