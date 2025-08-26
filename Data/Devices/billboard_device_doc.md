# 📘 billboard_device – UEFN Verse Device Documentation

## 🔹 Description
The `billboard_device` is used to display custom text messages visibly in your UEFN world. Ideal for instructions, hints, feedback, or gameplay cues, billboards can show/hide text, update messages and appearance at runtime, and optionally display a border.

Text appearance (font/size/color/justification) and the message itself can be adjusted in the Details panel and modified during runtime using Verse.

## 🧱 Verse Using Statement
```verse
using { /Fortnite.com/Devices }
```

## 🔗 Inheritance Hierarchy
- `creative_object`
- `creative_device_base`
- `billboard_device`

## 🛠️ Functions & Methods
| Name                  | Description                                                |
|-----------------------|------------------------------------------------------------|
| `ShowText()`          | Show the billboard’s text.                                 |
| `HideText()`          | Hide the billboard’s text.                                 |
| `SetText(message)`    | Set the text to display on the billboard.                  |
| `SetTextSize(number)` | Set text size (clamped, e.g., 8–24).                      |
| `UpdateDisplay()`     | Refresh the display after Details panel changes.           |
| `SetShowBorder(logic)`| Enable/disable the border (and collision).                 |
| `GetShowBorder()`     | Returns the border visibility status.                      |
| `GetTextSize()`       | Returns the current configured text size.                  |
| `GetTransform()`      | Gets position, rotation, and scale.                        |
| `MoveTo()`/`TeleportTo()` | Move or teleport the device.                          |

## 🎛 Configuration Options (Details Panel)
| Option                   | Description                                                  |
|--------------------------|--------------------------------------------------------------|
| `Text`                   | Displayed message (up to 512 characters).                    |
| `Text Size`              | Text size (e.g., 8–24).                                      |
| `Font / Justification`   | Font (Roboto, Burbank, Notosans) or alignment.               |
| `Show Border`            | Enable/disable border (also controls collision).             |
| `Text Color`             | Color of the text.                                           |
| `Background Color`       | Background behind the text.                                  |
| `Display Mode`           | One Sided / Two Sided display.                               |
| `Outline/Shadow`         | Optional visual enhancements.                               |
| `View Distance`          | Distance at which the billboard is visible.                 |
| `Enabled During Phase`   | Controls visibility by game phase.                          |

## 🧹 Events
*This device does not emit Verse events. Control via methods or Details panel options.*

## 🪰 Verse Usage Example
```verse
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

billboard_device_example := class(creative_device):

    @editable
    Billboard : billboard_device = billboard_device{}

    @editable
    SetTextButton : button_device = button_device{}

    @editable
    SetTextSizeButton : button_device = button_device{}

    @editable
    ShowButton : button_device = button_device{}

    @editable
    HideButton : button_device = button_device{}

    @editable
    ToggleBorderButton : button_device = button_device{}

    var BorderEnabled : logic = false

    OnBegin<override>()<suspends> : void =
        SetTextButton.InteractedWithEvent.Subscribe(OnSetTextPressed)
        SetTextSizeButton.InteractedWithEvent.Subscribe(OnSetTextSizePressed)
        ShowButton.InteractedWithEvent.Subscribe(OnShowPressed)
        HideButton.InteractedWithEvent.Subscribe(OnHidePressed)
        ToggleBorderButton.InteractedWithEvent.Subscribe(OnToggleBorderPressed)

    OnSetTextPressed(Agent : agent) : void =
        Billboard.SetText(StringToMessage("Hello, Fortnite!"))
        Print("Billboard text set!")

    OnSetTextSizePressed(Agent : agent) : void =
        Billboard.SetTextSize(48)
        Print("Billboard text size set to 48!")

    OnShowPressed(Agent : agent) : void =
        Billboard.ShowText()
        Print("Billboard text shown!")

    OnHidePressed(Agent : agent) : void =
        Billboard.HideText()
        Print("Billboard text hidden!")

    OnToggleBorderPressed(Agent : agent) : void =
        if (BorderEnabled?):
            Print("Billboard border toggle not supported!")
            set BorderEnabled = false
        else:
            Print("Billboard border toggle not supported!")
            set BorderEnabled = true

    StringToMessage<localizes>(InString : string) : message = "{InString}"
```

## 🪠 How It Works in UEFN
1. **Place Devices in Level**
   - Add a `billboard_device` in the world to show a message.
   - Add `button_device`s to control the billboard.

2. **Configure the Device**
   - Use the Details panel to set initial text, size, font, justification, and colors.

3. **Create & Build Verse Script**
   - Right-click your folder in the Verse Explorer and create a new Verse file.
   - Paste and save the provided code.
   - Click `Verse → Build Verse Code` or press `Ctrl+Shift+B` until "Build Succeeded".

4. **Place & Reference Devices**
   - Drag your Verse device class into the map.
   - Assign your devices in the Details panel fields (billboard and buttons).

5. **Test Gameplay**
   - Launch a session.
   - Press buttons to see text update, hide/show, and attempt toggling border.

## 🧠 Best Practices
- Use short, clear wording for high visibility.
- Disable border for "floating text" effect.
- Update messages using buttons or events for dynamic feedback.
- Use the Details panel for styling; Verse doesn’t control color/font.

## ❌ Common Issues & Fixes
| Issue                            | ❌ Wrong Example          | ✅ Correct Example                        | Explanation                                                |
|----------------------------------|-----------------------------|----------------------------------------------|------------------------------------------------------------|
| Exceeding max text length        | Use very long strings       | Keep text under 512 characters               | Long text may get clipped or unreadable.                   |
| Trying to change font in Verse   | `SetFont("Roboto")`         | Set font via Details panel                   | Font and color are not runtime editable.                   |
| Expecting collision w/o border   | Border left disabled        | Enable `Show Border` in Details panel        | Border is required for collision to work.                  |
| Not assigning device references  | Editable fields left blank  | Assign devices correctly in Details panel    | Verse methods won’t work without valid references.         |

## 📅 Notes
- Use `.SetText()` to update text at runtime.
- `Show Border` controls both appearance and collision.
- Use `.ShowText()` and `.HideText()` for toggling visibility.

