📘 **vfx_spawner_device – UEFN Verse Device Documentation**

🔹 **Description**
The `vfx_spawner_device` places visual effects on your Fortnite island, such as smoke, sparks, music notes, weather effects, explosions, or ambiance. It supports both continuous and burst effects, configurable colors, sound effects, and visibility settings by team or class. Use it to create immersive environments, signal gameplay events, or add polish to interactive spaces.

🧱 **Verse Using Statement**
```verse
using { /Fortnite.com/Devices }
```

🔗 **Inheritance Hierarchy**
- creative_object
- creative_device_base
- vfx_spawner_device

🧩 **Data Members (Events)**
| Name               | Type           | Description                                 |
|--------------------|----------------|---------------------------------------------|
| EffectEnabledEvent | listenable()   | Fires when the VFX is enabled (begins playing). |
| EffectDisabledEvent| listenable()   | Fires when the VFX is disabled (stops playing). |

🛠️ **Functions & Methods**
| Name        | Description                                       |
|-------------|---------------------------------------------------|
| Enable()    | Starts the VFX (plays the effect at its location). |
| Disable()   | Stops/hides the VFX.                              |
| Restart()   | Restarts the effect (triggers burst/loops new effect). |
| GetTransform() | Gets position/rotation/scale of the device.   |
| MoveTo(...) / TeleportTo(...) | Move or teleport the effect device. |

🎛 **Configuration Options (Details Panel)**
| Option                | Description                                                  |
|------------------------|--------------------------------------------------------------|
| Effect Type            | Continuous or Burst – sets looping effect vs. one-shot burst.|
| Visual Effect          | Select from list: fire, explosion, dust, rain, etc.         |
| Sound Effect           | Default, None, or select from available SFX.                |
| Colorize VFX           | On/Off – determines if the custom color applies.            |
| Custom Color           | Choose VFX color (when Colorize On).                        |
| Visible to Team/Class  | Restrict visibility to specific teams or classes.           |
| Invert Team/Class      | All except selected team/class see the effect.              |
| Spawn Rate             | Controls how often effect spawns/loops (for Continuous).    |
| Enabled on Phase/Reset | When device auto-enables (None, Always, Pre-Game, etc.).    |

🧰 **Verse Usage Example**
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

vfx_spawner_example := class(creative_device):

    @editable
    VFXSpawner : vfx_spawner_device = vfx_spawner_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        VFXSpawner.EffectEnabledEvent.Subscribe(OnVFXEnabled)
        VFXSpawner.EffectDisabledEvent.Subscribe(OnVFXDisabled)

        EnableButton.InteractedWithEvent.Subscribe(OnEnablePressed)
        DisableButton.InteractedWithEvent.Subscribe(OnDisablePressed)

    OnVFXEnabled() : void =
        Print("VFX spawner enabled!")

    OnVFXDisabled() : void =
        Print("VFX spawner disabled!")

    OnEnablePressed(Agent : agent) : void =
        VFXSpawner.Enable()
        Print("VFX effect enabled!")

    OnDisablePressed(Agent : agent) : void =
        VFXSpawner.Disable()
        Print("VFX effect disabled!")
```

📌 **How it works in UEFN**
1. **Place Devices in Level**
   - Add one or more `vfx_spawner_devices` where you want effects.
   - Add `button_devices` if you wish to control the effects interactively.

2. **Configure Effect in Details Panel**
   - Set the desired Visual/Burst Effect, Loop/Colorization options, Sound, Target Team/Class, and enable conditions.

3. **Create and Build Verse Script**
   - Create a new Verse file (e.g., `vfx_spawner_example.verse`) and paste in the code above.
   - Click *Verse → Build Verse Code* or press `CTRL+SHIFT+B`.

4. **Place Verse Device**
   - Drag `vfx_spawner_example` into your level from the Content Browser.
   - Assign references in its Details panel:
     - VFXSpawner → your `vfx_spawner_device`
     - EnableButton / DisableButton → configured `button_devices`

5. **Test & Adjust**
   - Launch a session. Use buttons to enable/disable effects and observe log messages.

🧠 **Best Practices**
- Use `.Enable()` and `.Disable()` for dynamic events like round start, elimination, power-up, or unlocking zones.
- Use `EffectEnabledEvent` and `EffectDisabledEvent` to trigger additional logic or feedback.
- Customize color and visibility for team/class-based gameplay.
- Prefer Burst for one-shot effects (e.g., explosions); Continuous for ambient effects (e.g., weather).

❌ **Common Mistakes & Fixes**
| Issue                         | ❌ Wrong Usage           | ✅ Correct Usage                              | Explanation                                      |
|-------------------------------|--------------------------|----------------------------------------------|--------------------------------------------------|
| Effect not visible to all     | Team/Class filter set    | Set to Any/All or correct selection           | Ensures correct players see effects              |
| Device inactive on game start | Not enabled at phase     | Set “Enabled on Phase” = Always or use Verse | Ensures effect auto-activates                    |
| Expecting sound with effect   | Sound set to None/Default| Select desired SFX in Details panel           | Sound must be explicitly set                     |
| Forgetting custom color       | Colorize not enabled     | Toggle “Colorize VFX” and pick a color       | Custom color applies only when enabled properly  |

📎 **Note**
- For reactive/advanced systems, control VFX spawning/enabling from Verse based on gameplay events.
- Test in different time conditions and team/class settings to validate immersive effects across gameplay.

