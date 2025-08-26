# animated_mesh_device – UEFN Verse Device Documentation

## 🔹 Description
The `animated_mesh_device` in Unreal Editor for Fortnite (UEFN) enables the placement of a Skeletal Mesh in your level with full control over its animation during runtime. With this device, developers can:

- Play animations
- Pause them
- Play animations in reverse

These actions can be triggered through Verse code or by directly binding events in the editor. Ideal use cases include animating custom characters, NPCs, props, or interactive animated events such as cutscenes and boss introductions.

---

## 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
```

---

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `animated_mesh_device`

---

## 🧩 Core Methods
| Function Signature | Description |
|---------------------|-------------|
| `Play(): void` | Starts or resumes playback of the assigned animation. |
| `Pause(): void` | Pauses the animation playback. |
| `PlayReverse(): void` | Starts or resumes playing the animation in reverse. |

*Note: Inherits spatial methods from `creative_object` such as `MoveTo`, `GetTransform`, `TeleportTo`.*

---

## 🎚 Configuration Options (Details Panel)
| Name | Description |
|------|-------------|
| Skeletal Mesh | Choose the Skeletal Mesh asset to display (e.g., character, prop). |
| Animation | Animation Sequence to play on this mesh. |
| Loop | If True, the animation repeats upon completion. |
| Play Rate | Speed multiplier for playback (1.0 = normal speed). |

*These options must be configured in the Details panel after placing the device.*

---

## 🔗 Direct Event Binding
Use the device’s Details panel under **Functions** to bind `Play()`, `Pause()`, or `PlayReverse()` to in-game events such as button presses or volume triggers.

---

## 🧰 Usage Example
```verse
using { /Fortnite.com/Devices }

animated_mesh_control := class(creative_device):

    @editable
    AnimatedMesh : animated_mesh_device = animated_mesh_device{}

    @editable
    PlayButton : button_device = button_device{}
    @editable
    PauseButton : button_device = button_device{}
    @editable
    ReverseButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        PlayButton.InteractedWithEvent.Subscribe(OnPlay)
        PauseButton.InteractedWithEvent.Subscribe(OnPause)
        ReverseButton.InteractedWithEvent.Subscribe(OnReverse)

    OnPlay(Agent: agent) : void =
        AnimatedMesh.Play()

    OnPause(Agent: agent) : void =
        AnimatedMesh.Pause()

    OnReverse(Agent: agent) : void =
        AnimatedMesh.PlayReverse()
```

---

## 🧠 Best Practices
- Set Skeletal Mesh and Animation assets in the Details panel before runtime.
- Use UI buttons or level triggers to control animation playback.
- Configure `Play Rate` and `Loop` options for desired animation style.
- Use multiple `animated_mesh_device` instances for independent actors.
- Combine with `Cinematic Sequence` device for immersive events.

---

## ❌ Incorrect Usage Examples and How to Fix
| Issue | ❌ Wrong Example | ✅ Correct Example | Explanation |
|-------|------------------|-------------------|-------------|
| Missing configuration | Call `Play()` without setting assets | Assign Skeletal Mesh & Animation in Details | Animation won't function without setup |
| Nil reference | Use unassigned `AnimatedMesh` | Assign device reference via Details | Prevents errors due to null reference |
| Expecting editor playback | Look for animation in editor viewport | Playtest in Fortnite client | Animations only run during live play |

---

## 📌 Additional Notes
- Animations do **not** preview in the UEFN editor viewport—always test in runtime.
- Use event triggers or Verse scripting for complex control logic.
- Optimize Skeletal Mesh and Animation assets to reduce memory usage.

---

## 🔗 Related Devices
- `button_device`
- `cinematic_sequence_device`
- `trigger_device`

---

This documentation outlines all necessary components and best practices for integrating and utilizing the `animated_mesh_device` effectively within your UEFN projects.

