# 📘 Customizable Light Device – UEFN Verse Device Documentation

## 🔹 Description
The `customizable_light_device` lets you add dynamic lighting that can be controlled at runtime in your Fortnite island. This device can be used as either a point light or spot light, can be turned on/off, toggled, dimmed, undimmed, and reset through Verse or creative device events. It's ideal for responsive environments, puzzles, stealth mechanics, and interactive level design.

## 🧱 Imports Required
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
```

## 🔗 Inheritance Hierarchy
- `creative_object`  
  *Base class for creative devices and props.*
- `creative_device_base`  
  *Base class for creative_device.*
- `customizable_light_device`

## 🧹 Core Methods
| Function Name | Signature / Description |
|---------------|--------------------------|
| `Enable()` | Enables the device (allows control and turns it ready for action). |
| `Disable()` | Disables the device (cannot be controlled/interacted with while disabled). |
| `Reset()` | Resets device to its initial state (color, intensity, on/off, etc). |
| `TurnOn()` | Turns light on. |
| `TurnOff()` | Turns light off. |
| `Toggle()` | Switches between on and off states. |
| `DimLight()` | Dims light by preset dimming amount (configured in Details panel). |
| `UndimLight()` | Brightens light by preset dimming amount. |
| `GetTransform()` | Returns device’s world transform. |
| `MoveTo()` | Animates movement to a given transform over time (advanced use). |
| `TeleportTo()` | Instantly moves device to a new position/rotation/scale. |

## 🎛 Configuration Options (Details Panel)
| Option | Values/Description |
|--------|---------------------|
| Enabled During Phase | None, All, Pre-Game Only, Gameplay Only |
| Initial State | On, Off |
| Light Color | Any color (Color Picker) |
| Light Intensity | Percentage of maximum (default 50%) |
| Reflection Intensity | Percentage of maximum (default 100%) |
| Light Type | Point Light (all directions), Spot Light (cone/focused) |
| Light Size | Tiny, Small, Medium, Big, Huge |
| Rhythm Preset | Constant, Flicker, Wave, Short Circuit, Party, Windy, Flash |
| Rhythm Time | Time multiplier for rhythm |
| Cast Shadows | Yes, No |
| Dimming Amount | Percent amount (default 70%) |
| Dimming Time | Time for dimming/undimming transitions |

*Set all these in the Details panel in UEFN before or during gameplay.*

## 🕿️ Direct Event Binding Support
All light control actions (`Enable`, `Disable`, `TurnOn`, `TurnOff`, `Dim`, `Undim`, `Reset`, `Toggle`) can be bound directly to device/channel events via Direct Event Binding for instant response to triggers, buttons, timers, and more.

## 🧰 Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

custom_light_example := class(creative_device):

    @editable
    Light : customizable_light_device = customizable_light_device{}

    @editable
    OnButton : button_device = button_device{}

    @editable
    OffButton : button_device = button_device{}

    @editable
    ToggleButton : button_device = button_device{}

    @editable
    DimButton : button_device = button_device{}

    @editable
    UndimButton : button_device = button_device{}

    @editable
    ResetButton : button_device = customizable_light_device{}

    OnBegin<override>()<suspends> : void =
        OnButton.InteractedWithEvent.Subscribe(OnLightOn)
        OffButton.InteractedWithEvent.Subscribe(OnLightOff)
        ToggleButton.InteractedWithEvent.Subscribe(OnLightToggle)
        DimButton.InteractedWithEvent.Subscribe(OnLightDim)
        UndimButton.InteractedWithEvent.Subscribe(OnLightUndim)
        ResetButton.TurnOff()

    OnLightOn(Agent : agent) : void =
        Light.TurnOn()
        Print("Light turned on")

    OnLightOff(Agent : agent) : void =
        Light.TurnOff()
        Print("Light turned off")

    OnLightToggle(Agent : agent) : void =
        Light.Toggle()
        Print("Light toggled")

    OnLightDim(Agent : agent) : void =
        Light.DimLight()
        Print("Light dimmed")

    OnLightUndim(Agent : agent) : void =
        Light.UndimLight()
        Print("Light undimmed")
```

## 🧠 How It Works
- Place a `customizable_light_device` in your level and configure its options in the Details panel (color, rhythm, type, etc.).
- Use buttons or other devices to trigger the light device via Verse code as above, or bind them directly in the editor using Direct Event Binding.
- Verse functions allow full runtime control for advanced lighting logic, puzzle state, ambience, stealth areas, etc.

## 🧠 Best Practices
- Optimize light intensity and size to balance visual impact and performance, especially with many dynamic lights.
- Use rhythm and color presets for ambience or signaling; experiment for best atmosphere.
- Combine with triggers, timers, and player action devices for most dynamic results.
- Prefer device binding for simple on/off; use Verse for more complex or combined logic.

## ❌ Common Mistakes and Fixes
| Issue | ❌ Wrong Example | ✅ Correct Example | Explanation |
|-------|---------------------|-----------------------|-------------|
| Skipping Details assignment | Calling `.TurnOn()` on unset device in Verse | Assign device in Details panel and to `@editable` field | Prevents errors/null pointer |
| Ignoring dim amount/time | Calling `.DimLight()` repeatedly without testing | Configure dimming in Details for smooth operation | Prevents unpredictable brightness |
| Forgetting to Enable() | Light remains off/not responding | Ensure `.Enable()` has been called (or set enabled) | Device must be enabled to act |

## ℹ️ Notes
- Color and brightness can only be dynamically set by changing device’s settings (initial color via Details panel; no runtime direct color set function in Verse as of v35.20).
- You may use multiple light devices and rhythm settings for complex patterns or sequences.
- Customizable lights do not have attached props; use them alongside mesh assets for most authentic fixtures.

