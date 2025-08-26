## post_process_device – UEFN Verse Device Documentation

### 🔹 Description
The `post_process_device` enables you to apply Post Process visual effects—such as color grading, camera filters, or special visual moods—to players dynamically via Verse or creative device logic, instead of using standard Post Process Volumes. This gives you real-time, scriptable control over scene appearance for individual players, teams, or everyone—perfect for transitions, gameplay states, cutscenes, or stylish effects.

### 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
```

### 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `post_process_device`

### 🧩 Core Methods
| Function Signature         | Description                                              |
|---------------------------|----------------------------------------------------------|
| `Enable()`                | Enables the device for all players or a specific agent.   |
| `Disable()`               | Disables the device for all players or a specific agent.  |
| `BlendIn()`               | Blends in the effect for a specific agent.                |
| `BlendInForAll()`         | Blends in the effect for all players.                     |
| `BlendOut()`              | Blends out the effect for a specific agent.               |
| `BlendOutForAll()`        | Blends out the effect for all players.                    |
| `Reset()`                 | Resets to starting strength for a specific agent.         |
| `ResetForAll()`           | Resets to starting strength for all players.              |
| `GetTransform()`          | Gets transform (position/rotation/scale); rarely needed.  |

### 📡 Key Events
| Event Name                  | Description                                              |
|----------------------------|----------------------------------------------------------|
| `BlendingInCompleteEvent`  | Called when the blend-in effect finishes.               |
| `BlendingOutCompleteEvent` | Called when the blend-out effect finishes.              |

### 🎛 Configuration Options (Details Panel)
- **Post Process Effect**: (None / Oak / Dark / Film Noir / Film Warm / etc.)
- **Effect Duration**: Infinite or custom seconds
- **Priority**: Resolves overlaps between devices
- **Starting Strength**: Default 1.0
- **Blend In Strength**: Default 0.0 and up
- **Blend In Duration**: Time in seconds to ramp up effect
- **Blend Out Duration**: Time in seconds to ramp down effect
- **Applies to Team/Class**: Restrict effect to specific team/class

*Note: Configure these per-instance in the UEFN Details panel.*

### 🛠️ Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

post_process_example := class(creative_device):

    @editable
    PostProcess : post_process_device = post_process_device{}

    OnBegin<override>()<suspends> : void =
        PostProcess.BlendingInCompleteEvent.Subscribe(OnBlendInComplete)
        PostProcess.BlendingOutCompleteEvent.Subscribe(OnBlendOutComplete)

        PostProcess.Enable()
        PostProcess.BlendInForAll()

        Sleep(5.0)
        PostProcess.BlendOutForAll()

    OnBlendInComplete(Agent : ?agent) : void =
        Print("Post process effect fully blended in!")

    OnBlendOutComplete(Agent : ?agent) : void =
        Print("Post process effect fully blended out!")
```

### 🧠 Best Practices
- Configure filter/effect and strengths in the Details panel before runtime.
- Use `BlendInForAll()`/`BlendOutForAll()` for global transitions; use single-agent variants for localized effects.
- Use events (`BlendingInCompleteEvent`, `BlendingOutCompleteEvent`) for syncing gameplay logic.
- Set `Priority` if multiple effects might overlap.
- Avoid activating more than one post_process_device per player/team unless intended for blending.

### ❌ Incorrect Usage Examples and Fixes
| Issue                        | ❌ Wrong Example                          | ✅ Correct Example                          | Explanation                                                   |
|-----------------------------|---------------------------------------------|------------------------------------------------|---------------------------------------------------------------|
| Not assigning device ref    | Using methods without Details assignment   | Reference in @editable field & assign in Details | Prevents nil/error access in Verse                           |
| Skipping blend conf         | Not setting Blend In/Out Duration          | Set durations in Details panel                  | Defaults may cause instant/hard transitions                  |
| Not setting effect/filter   | Leaving post-process effect as None        | Choose an effect in Details                     | No visual will appear without an effect selected             |

### ⚠️ Notes
- `post_process_device` is a **scripted** device, not a physical volume.
- It is **triggered** via Verse or creative logic.
- It **does not block/occlude** scene geometry.
- Adjust effect settings in **Details panel** for best visual results.

