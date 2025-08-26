## Skydome Device – UEFN Verse Device Technical Documentation

### 🔹 Description
The `skydome_device` provides full control over the appearance of your Fortnite island’s sky. It allows customization of the sun, moon, clouds, fog, starfield, and horizon, including color blending for creating atmospheric and themed visuals. Use this device to craft immersive lighting environments for day, night, or unique experiences.

### 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
- **creative_object**
  - Base class for creative devices and props.
- **creative_device_base**
  - Base class for creative_device.
- **skydome_device**

### 🛠️ Functions & Methods
| Name | Description |
|------|-------------|
| `Enable()` | Enables the skydome device and applies configured sky settings. |
| `Disable()` | Disables the device, reverting to default sky settings. |
| `GetTransform()` | Returns the device's position, rotation, and scale (in cm). Validate with `creative_object.IsValid`. |
| `MoveTo(Position, Rotation, Time)` | Animates movement to a new position and rotation over specified time (seconds). |
| `MoveTo(Transform, Time)` | Moves to a new transform (position, rotation, scale) over time. Interrupts ongoing animation. |
| `TeleportTo(Position, Rotation)` | Instantly teleports to specified position and rotation. |
| `TeleportTo(Transform)` | Instantly teleports to new transform with position, rotation, and scale. |

### 🧩 Data Members
This class has **no public data members**—all configuration is done via the **Details panel** in UEFN.

### 🎛 Configuration Options (via Details Panel)
- **Light Source**: Set to sun, moon, or none.
- **Light Source Color**: Defines color of the sun/moon.
- **Light Source Intensity**: Adjusts brightness.
- **Sky Gradient Top/Middle/Bottom Colors**: Defines vertical sky color blend.
- **Ambient Light & Intensity**: Controls overall sky ambiance.
- **Clouds**: Choose type (realistic or twisty), color, and speed.
- **Stars**: Toggle visibility and adjust intensity.
- **Fog**: Toggle and set horizon color/density.
- **Device Orientation**: Controls sun/moon direction via rotation in editor.

### 🧰 Example Usage in Verse
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

skydome_example := class(creative_device):

    @editable
    Skydome : skydome_device = skydome_device{}

    @editable
    EnableButton : button_device = button_device{}

    @editable
    DisableButton : button_device = button_device{}

    OnBegin<override>()<suspends> : void =
        EnableButton.InteractedWithEvent.Subscribe(OnEnable)
        DisableButton.InteractedWithEvent.Subscribe(OnDisable)

    OnEnable(Agent:agent):void =
        Skydome.Enable()
        Print("Skydome enabled!")

    OnDisable(Agent:agent):void =
        Skydome.Disable()
        Print("Skydome disabled!")
```

### 🧠 Best Practices
- Use **only one `skydome_device`** per island to avoid conflicts.
- Configure all visual settings in the **Details panel**.
- Rotate the device actor to set the **sun/moon direction**.
- For **dynamic day/night cycles**, use the **Day Sequence** device.

### ❌ Incorrect Usage Examples and Fixes
| Issue | ❌ Wrong | ✅ Correct | Explanation |
|-------|---------|-----------|-------------|
| Forgetting to enable device | Just placing the device | Call `.Enable()` in Verse/on interaction | Skydome settings only apply when enabled |
| Multiple skydomes enabled | Multiple devices active | Use only one enabled `skydome_device` | Only one can affect the sky |
| Expecting dynamic sky | Only skydome configured | Use `Day Sequence` device | Skydome is static, not dynamic |
| Not rotating for sun/moon | Default rotation | Rotate in editor | Rotation affects sun/moon direction |

### 📌 Note
- All visual settings must be configured in the **Details panel**.
- Use `Enable()` and `Disable()` in Verse to **switch sky settings dynamically**.
- **Deprecated** in new projects—use the **Day Sequence** device for dynamic time-of-day support.

