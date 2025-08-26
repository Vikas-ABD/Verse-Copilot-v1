## holoscreen_device – UEFN Verse Device Documentation

### 🔹 Description
The `holoscreen_device` creates a holographic screen in the game world that can display dynamic content, such as a clock or curated images. It is a visual-only device and does not support interaction or dynamic text rendering via Verse (as of now).

### 📅 Required Import
```verse
using { /Fortnite.com/Devices }
```

### 🔗 Inheritance Hierarchy
```
creative_object
└── creative_device_base
    └── holoscreen_device
```

| Class | Description |
|-------|-------------|
| `creative_object` | Base class for all in-world devices and props. |
| `creative_device_base` | Adds movement and transform controls. |
| `holoscreen_device` | Specialized device for showing visual content (e.g., clocks, images). |

### 📩 Members
#### ❌ Data Members
* No directly exposed data members in this class via Verse.

### 🧰 Functions
| Function Name | Description |
|---------------|-------------|
| `GetTransform()` | Returns the transform (position, rotation, scale) of the device in centimeters. Use `IsValid()` before calling. |
| `MoveTo(Position, Rotation, Time)` | Moves the screen to a new location and orientation smoothly over time (in seconds). Cancels any current animations. |
| `MoveTo(Transform, Time)` | Moves to the provided full transform (including scale). |
| `TeleportTo(Position, Rotation)` | Instantly moves the screen to the specified location and rotation. |
| `TeleportTo(Transform)` | Instantly teleports the screen using full transform input. |

### 🧪 Example Usage
```verse
using { /Fortnite.com/Devices }

my_holoscreen := class(creative_device):

    @editable
    HoloScreen : holoscreen_device = holoscreen_device{}

    OnBegin<override>()<suspends> : void =
        # Wait for a few seconds before moving
        Sleep(2.0)

        # Teleport the holoscreen to a new location
        HoloScreen.TeleportTo(vector3{X := 1000.0, Y := 200.0, Z := 300.0}, rotation{})
```

### ⚠️ Notes & Best Practices
| Tip | Description |
|-----|-------------|
| Static Content | Currently, the content shown on the holoscreen (clock or image) cannot be changed dynamically via Verse. |
| Use `IsValid()` | Always validate the object if it may be destroyed or removed during gameplay. |
| Great for UI Visualization | Use holoscreens as non-interactive visual feedback (e.g., mission status, themed clocks, static posters). |
| Move and Animate | Use `MoveTo()` with delays or timelines to create cinematic effects. |

### 💡 Use Cases
| Scenario | Description |
|----------|-------------|
| Clock Display | Show the in-game or real-time clock. |
| Thematic Screens | Add story-rich or immersive environment visuals (e.g., “Warning” screen, mission info). |
| Animated Cutscenes | Use `MoveTo()` to animate screens during story moments. |
| Status Board | Though it can’t show real-time variable data, it can represent generic status icons. |

### 🔧 Limitations
* No runtime content updates via Verse.
* Non-interactive: purely visual with no click or interaction support.

### 🧠 Best Practices
* Place multiple holoscreens for immersive scoreboards, world clocks, or aesthetic elements.
* Use `.ShowHologram()` / `.HideHologram()` for scripted story moments or event triggers.
* Adjust bend, image, and phase settings for the desired atmosphere and function.

### ❌ Common Issues & Fixes
| Issue | ❌ Example | ✅ Correct Approach | Explanation |
|-------|---------------|-------------------------|-------------|
| Not referencing device | Left `@editable` blank in Verse | Assign devices in Details after placement | Required for any Verse script to run |
| Settings not updating | Changed in-game, not in Details panel | Set appearance/config BEFORE play session | Config is not runtime dynamic |
| Nothing appears in play | Device not enabled/assembled or shown | Set phase, show/proj visibility, or enable | Review device config for visibility |

**Note:**
* No event bindings exist for custom signals, but full visual control can be achieved in-game via `.ShowHologram()`, `.HideHologram()`, and position/rotation methods in Verse.
* Great for scoreboards, countdowns, direction signs, or world/story decoration.

